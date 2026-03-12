#!/usr/bin/env python3
"""
從 MFDS 下載韓國藥品資料

使用 nedrug.mfds.go.kr 網站的快取頁面取得藥品資料
"""

import json
import re
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

BASE_URL = "https://nedrug.mfds.go.kr"

# 常見藥品的品目基準코드列表（從搜尋結果中收集）
# 這些是已知存在的藥品代碼
SAMPLE_ITEM_SEQS = [
    "200708054",  # 이토메드정
    "199302061",  # 듀오락스정
    "200700800",  # 텐텐츄정
    "201708285",  # 헥사메딘액
    "198400278",  # 알마겔현탁액
    "202000645",  # 센코딜에프정
]


def get_drug_detail(item_seq: str) -> dict | None:
    """取得單一藥品的詳細資料"""
    url = f"{BASE_URL}/pbp/CCBBB01/getItemDetailCache?cacheSeq={item_seq}"

    try:
        response = requests.get(url, timeout=30)
        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, "lxml")

        # 解析表格資料
        drug_info = {"품목기준코드": item_seq}

        # 找到所有 th-td 配對
        for row in soup.select("tr"):
            th = row.select_one("th")
            td = row.select_one("td")

            if th and td:
                key = th.get_text(strip=True)
                value = td.get_text(strip=True)

                # 映射欄位名稱
                field_map = {
                    "제품명": "품목명",
                    "업체명": "업체명",
                    "전문/일반": "전문일반",
                    "허가일": "허가일자",
                    "표준코드": "표준코드",
                    "저장방법": "저장방법",
                    "포장정보": "포장정보",
                    "성상": "성상",
                    "취소/취하구분": "취소여부",
                }

                if key in field_map:
                    drug_info[field_map[key]] = value

        # 嘗試取得效能效果
        ee_section = soup.find("h3", string=re.compile("효능효과"))
        if ee_section:
            ee_content = ee_section.find_next("div", class_="cont_area")
            if ee_content:
                drug_info["효능효과"] = ee_content.get_text(strip=True)[:500]

        # 嘗試取得成分資訊
        ingredient_table = soup.find("th", string="성분명")
        if ingredient_table:
            ingredients = []
            tbody = ingredient_table.find_parent("table")
            if tbody:
                for tr in tbody.select("tbody tr"):
                    tds = tr.select("td")
                    if len(tds) >= 2:
                        ingredient_name = tds[1].get_text(strip=True)
                        if ingredient_name:
                            ingredients.append(ingredient_name)
            if ingredients:
                drug_info["주성분"] = ";".join(ingredients)

        return drug_info if len(drug_info) > 1 else None

    except Exception as e:
        print(f"Error fetching {item_seq}: {e}")
        return None


def search_drugs(keyword: str = "", page: int = 1) -> list[str]:
    """搜尋藥品並返回品目基準코드列表"""
    # 注意：這需要解析搜尋結果頁面
    # 由於 MFDS 網站的限制，這裡返回已知的代碼
    return SAMPLE_ITEM_SEQS


def download_all_drugs(output_path: Path, max_items: int = 100):
    """下載藥品資料"""
    drugs = []

    # 使用已知的藥品代碼
    item_seqs = SAMPLE_ITEM_SEQS

    print(f"開始下載 {len(item_seqs)} 個藥品資料...")

    for seq in tqdm(item_seqs, desc="下載中"):
        drug_info = get_drug_detail(seq)
        if drug_info:
            drugs.append(drug_info)
        time.sleep(0.5)  # 避免請求過快

    # 儲存結果
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(drugs, f, ensure_ascii=False, indent=2)

    print(f"\n已下載 {len(drugs)} 筆藥品資料")
    print(f"儲存至: {output_path}")

    return drugs


def main():
    print("=" * 60)
    print("MFDS 藥品資料下載工具")
    print("=" * 60)
    print()

    output_path = Path(__file__).parent.parent / "data" / "raw" / "kr_fda_drugs.json"

    # 檢查是否有 sample 檔案
    sample_path = Path(__file__).parent.parent / "data" / "raw" / "kr_fda_drugs_sample.json"
    if sample_path.exists() and not output_path.exists():
        print("發現範例資料，正在複製...")
        import shutil
        shutil.copy(sample_path, output_path)
        print(f"已複製至: {output_path}")
        print("\n注意：這是範例資料，如需完整資料請：")
        print("1. 前往 https://nedrug.mfds.go.kr/pbp/CCBGA01")
        print("2. 下載「의약품 제품허가목록」Excel/CSV 檔案")
        print("3. 放到 data/raw/ 目錄")
        print("4. 執行 process_fda_data.py 處理資料")
        return

    # 嘗試下載資料
    drugs = download_all_drugs(output_path)

    if drugs:
        print("\n下載完成！")
        print("下一步: uv run python scripts/run_kg_prediction.py")
    else:
        print("\n下載失敗，請手動下載資料。")


if __name__ == "__main__":
    main()
