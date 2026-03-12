#!/usr/bin/env python3
"""
從 nedrug.mfds.go.kr 抓取韓國藥品資料

使用快取頁面 API 取得藥品詳細資訊
"""

import json
import re
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

BASE_URL = "https://nedrug.mfds.go.kr"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "ko-KR,ko;q=0.9,en;q=0.8",
}


def get_drug_detail(item_seq: str, verbose: bool = False) -> dict | None:
    """從快取頁面取得藥品詳細資料"""
    url = f"{BASE_URL}/pbp/CCBBB01/getItemDetailCache"
    params = {"cacheSeq": item_seq}

    try:
        response = requests.get(url, params=params, headers=HEADERS, timeout=15)
        if response.status_code != 200:
            return None

        # 檢查頁面是否有效
        if "존재하지 않습니다" in response.text or len(response.text) < 2000:
            return None

        soup = BeautifulSoup(response.text, "lxml")

        drug_info = {"품목기준코드": item_seq}

        # 從表格取得基本資訊
        tables = soup.select("table")
        for table in tables:
            for row in table.select("tr"):
                th = row.select_one("th")
                td = row.select_one("td")
                if th and td:
                    key = th.get_text(strip=True)
                    value = td.get_text(strip=True)

                    if key == "제품명" and "품목명" not in drug_info:
                        drug_info["품목명"] = value
                    elif key == "성상" and "성상" not in drug_info:
                        drug_info["성상"] = value
                    elif key == "업체명" and "업체명" not in drug_info:
                        drug_info["업체명"] = value
                    elif key == "저장방법" and "저장방법" not in drug_info:
                        drug_info["저장방법"] = value

        # 從成分表取得主成分
        for table in tables:
            headers = [th.get_text(strip=True) for th in table.select("tr th")]
            if "성분명" in headers:
                ingredients = []
                for tr in table.select("tbody tr"):
                    tds = tr.select("td")
                    if len(tds) >= 2:
                        ingredient = tds[1].get_text(strip=True)
                        if ingredient and len(ingredient) > 1:
                            # 將韓文成分名轉為英文（如果有括號內的英文）
                            # 或直接使用
                            ingredients.append(ingredient)
                if ingredients:
                    drug_info["주성분"] = ";".join(ingredients[:5])
                break

        # 取得효능효과
        for h3 in soup.select("h3"):
            if "효능" in h3.get_text():
                next_div = h3.find_next("div", class_="info_box")
                if next_div:
                    text = next_div.get_text(strip=True)
                    if text:
                        drug_info["효능효과"] = text[:1000]
                break

        # 驗證必要欄位
        if "품목명" not in drug_info:
            return None

        if verbose:
            print(f"  Found: {drug_info.get('품목명', 'N/A')[:40]}")

        return drug_info

    except Exception as e:
        return None


def find_valid_seqs_around(base_seq: str, range_size: int = 100) -> list[str]:
    """在已知代碼附近搜尋有效代碼"""
    valid_seqs = []
    base_num = int(base_seq)

    for offset in range(-range_size, range_size + 1):
        seq = str(base_num + offset)
        valid_seqs.append(seq)

    return valid_seqs


def scrape_drugs(target_count: int = 100) -> list[dict]:
    """抓取藥品資料"""
    drugs = []
    seen_names = set()
    tried_seqs = set()

    # 已知可用的藥品代碼（經過驗證）
    known_working_seqs = [
        "200708054",  # 이토메드정 (已驗證可用)
    ]

    print(f"目標：抓取 {target_count} 筆藥品資料")
    print()

    # 首先測試已知代碼
    print("1. 測試已知代碼...")
    for seq in known_working_seqs:
        drug_info = get_drug_detail(seq, verbose=True)
        if drug_info and drug_info.get("품목명"):
            name = drug_info["품목명"]
            if name not in seen_names:
                seen_names.add(name)
                drugs.append(drug_info)
                tried_seqs.add(seq)
        time.sleep(0.3)

    print(f"   找到 {len(drugs)} 筆")

    # 在已知代碼附近搜尋
    print()
    print("2. 搜尋有效代碼...")

    # 常見的代碼範圍（根據 200708054 推測格式為 年份+序號）
    # 嘗試不同年份的相近代碼
    search_ranges = [
        (200700000, 200799999, 500),   # 2007年
        (200800000, 200899999, 500),   # 2008年
        (200600000, 200699999, 500),   # 2006年
        (200500000, 200599999, 500),   # 2005年
        (200900000, 200999999, 500),   # 2009年
        (201000000, 201099999, 500),   # 2010年
        (199900000, 199999999, 500),   # 1999年
        (199800000, 199899999, 500),   # 1998年
        (201100000, 201199999, 500),   # 2011年
        (201200000, 201299999, 500),   # 2012年
    ]

    for start, end, step in search_ranges:
        if len(drugs) >= target_count:
            break

        print(f"   搜尋範圍 {start} - {end}...")

        for seq_num in range(start, min(end, start + 10000), step):
            if len(drugs) >= target_count:
                break

            seq = str(seq_num)
            if seq in tried_seqs:
                continue

            tried_seqs.add(seq)
            drug_info = get_drug_detail(seq)

            if drug_info and drug_info.get("품목명"):
                name = drug_info["품목명"]
                if name not in seen_names:
                    seen_names.add(name)
                    drugs.append(drug_info)
                    print(f"     找到: {name[:40]} ({seq})")

                    # 找到一個後，嘗試附近的代碼
                    for nearby_offset in [-1, 1, -2, 2, -3, 3, -5, 5, -10, 10]:
                        nearby_seq = str(seq_num + nearby_offset)
                        if nearby_seq not in tried_seqs:
                            tried_seqs.add(nearby_seq)
                            nearby_drug = get_drug_detail(nearby_seq)
                            if nearby_drug and nearby_drug.get("품목명"):
                                nearby_name = nearby_drug["품목명"]
                                if nearby_name not in seen_names:
                                    seen_names.add(nearby_name)
                                    drugs.append(nearby_drug)
                                    print(f"     找到: {nearby_name[:40]} ({nearby_seq})")

                                    if len(drugs) >= target_count:
                                        break
                            time.sleep(0.1)

            time.sleep(0.1)

    return drugs


def main():
    print("=" * 60)
    print("MFDS nedrug.mfds.go.kr 藥品資料抓取工具")
    print("=" * 60)
    print()

    output_path = Path(__file__).parent.parent / "data" / "raw" / "kr_fda_drugs.json"

    # 抓取藥品
    drugs = scrape_drugs(target_count=100)

    print()
    print(f"成功抓取 {len(drugs)} 筆藥品資料")

    # 統計
    with_ingredients = sum(1 for d in drugs if d.get("주성분"))
    with_indications = sum(1 for d in drugs if d.get("효능효과"))
    print(f"  - 有成分資料: {with_ingredients}")
    print(f"  - 有適應症資料: {with_indications}")

    # 儲存
    if drugs:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(drugs, f, ensure_ascii=False, indent=2)

        print()
        print(f"已儲存至: {output_path}")

        # 顯示範例
        print()
        print("=" * 60)
        print("範例資料 (前5筆):")
        print("=" * 60)
        for drug in drugs[:5]:
            print(f"  품목명: {drug.get('품목명', 'N/A')}")
            print(f"  주성분: {drug.get('주성분', 'N/A')[:60]}")
            print(f"  효능효과: {drug.get('효능효과', 'N/A')[:60]}...")
            print()
    else:
        print("未找到任何藥品資料")


if __name__ == "__main__":
    main()
