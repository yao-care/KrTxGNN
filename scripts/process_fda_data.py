#!/usr/bin/env python3
"""處理 MFDS 藥品資料

將下載的韓國 MFDS (식품의약품안전처) 藥品資料轉換為標準 JSON 格式。

使用方法:
    uv run python scripts/process_fda_data.py

前置條件:
    需要先從 MFDS 의약품통합정보시스템 下載資料
    https://nedrug.mfds.go.kr/

產生檔案:
    data/raw/kr_fda_drugs.json
"""

import json
import zipfile
import csv
from pathlib import Path
from typing import Optional
import xml.etree.ElementTree as ET


def find_data_file(raw_dir: Path) -> Optional[Path]:
    """在 raw 目錄中尋找資料檔案

    MFDS 資料可能是以下格式：
    - ZIP 檔案（內含 JSON、CSV 或 XML）
    - JSON 檔案
    - CSV 檔案
    - XML 檔案

    Args:
        raw_dir: data/raw/ 目錄路徑

    Returns:
        找到的資料檔案路徑，若無則返回 None
    """
    # 優先尋找 JSON
    for pattern in ["*.json", "*.zip", "*.csv", "*.xml"]:
        data_files = list(raw_dir.glob(pattern))
        # 排除已處理的輸出檔案
        data_files = [f for f in data_files if not f.name.startswith("kr_fda_")]
        if data_files:
            return data_files[0]

    return None


def process_json_file(input_path: Path) -> list:
    """處理 JSON 格式資料"""
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # MFDS API 回應可能在 body.items 或直接是列表
    if isinstance(data, dict):
        if "body" in data and "items" in data["body"]:
            return data["body"]["items"]
        elif "items" in data:
            return data["items"]
        elif "data" in data:
            return data["data"]
    return data if isinstance(data, list) else [data]


def process_csv_file(input_path: Path) -> list:
    """處理 CSV 格式資料"""
    data = []
    with open(input_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(dict(row))
    return data


def process_xml_file(input_path: Path) -> list:
    """處理 XML 格式資料"""
    tree = ET.parse(input_path)
    root = tree.getroot()

    data = []
    # 嘗試常見的 XML 結構
    items = root.findall(".//item") or root.findall(".//row") or root.findall(".//record")

    for item in items:
        record = {}
        for child in item:
            record[child.tag] = child.text
        data.append(record)

    return data


def process_zip_file(input_path: Path) -> list:
    """處理 ZIP 壓縮檔"""
    print("解壓縮中...")
    with zipfile.ZipFile(input_path, 'r') as zf:
        # 尋找內部檔案
        for name in zf.namelist():
            if name.endswith('.json'):
                print(f"找到 JSON 檔案: {name}")
                with zf.open(name) as f:
                    content = f.read().decode('utf-8')
                    return json.loads(content)
            elif name.endswith('.csv'):
                print(f"找到 CSV 檔案: {name}")
                with zf.open(name) as f:
                    content = f.read().decode('utf-8-sig')
                    reader = csv.DictReader(content.splitlines())
                    return [dict(row) for row in reader]
            elif name.endswith('.xml'):
                print(f"找到 XML 檔案: {name}")
                with zf.open(name) as f:
                    content = f.read().decode('utf-8')
                    # 簡易 XML 解析
                    root = ET.fromstring(content)
                    data = []
                    items = root.findall(".//item") or root.findall(".//row")
                    for item in items:
                        record = {}
                        for child in item:
                            record[child.tag] = child.text
                        data.append(record)
                    return data

    raise ValueError("ZIP 檔案中找不到支援的資料格式（JSON/CSV/XML）")


def process_data_file(input_path: Path, output_path: Path) -> Path:
    """處理資料檔案並轉換為 JSON

    Args:
        input_path: 輸入檔案路徑
        output_path: 輸出 JSON 檔案路徑

    Returns:
        輸出檔案路徑
    """
    print(f"讀取資料檔案: {input_path}")
    print(f"檔案大小: {input_path.stat().st_size / 1024 / 1024:.1f} MB")

    suffix = input_path.suffix.lower()

    if suffix == ".zip":
        data = process_zip_file(input_path)
    elif suffix == ".json":
        data = process_json_file(input_path)
    elif suffix == ".csv":
        data = process_csv_file(input_path)
    elif suffix == ".xml":
        data = process_xml_file(input_path)
    else:
        raise ValueError(f"不支援的檔案格式: {suffix}")

    # 確保是列表
    if not isinstance(data, list):
        data = [data]

    # 確保輸出目錄存在
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # 儲存 JSON
    print(f"儲存至: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"完成！共 {len(data)} 筆藥品資料")

    # 顯示欄位資訊
    if data:
        print(f"\n發現的欄位: {list(data[0].keys())}")

    return output_path


def main():
    print("=" * 60)
    print("處理 MFDS 藥品資料 (韓國 식품의약품안전처)")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    raw_dir = base_dir / "data" / "raw"
    output_path = raw_dir / "kr_fda_drugs.json"

    # 確保 raw 目錄存在
    raw_dir.mkdir(parents=True, exist_ok=True)

    # 尋找資料檔案
    input_path = find_data_file(raw_dir)

    if input_path is None:
        print("找不到資料檔案！")
        print()
        print("請從 MFDS 의약품통합정보시스템 下載資料：")
        print("  https://nedrug.mfds.go.kr/")
        print()
        print("下載後將檔案放到:")
        print(f"  {raw_dir}/")
        print()
        print("支援的格式: JSON, CSV, XML, ZIP")
        return

    process_data_file(input_path, output_path)

    print()
    print("下一步: 準備詞彙表資料")
    print("  uv run python scripts/prepare_external_data.py")


if __name__ == "__main__":
    main()
