#!/usr/bin/env python3
"""
產生新聞監測用的關鍵字清單 - 韓國版本

從現有資料提取：
- 藥物名稱（英文 + 韓文商品名）
- 原始適應症（韓文）
- 預測適應症（英文）

輸出：data/news/keywords.json
"""

import json
import re
from datetime import datetime
from pathlib import Path

# 專案根目錄
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"


def load_json(path: Path) -> dict | list:
    """載入 JSON 檔案"""
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_korean_terms(text: str) -> list[str]:
    """從韓文文字中提取獨立的詞彙"""
    if not text:
        return []
    # 分隔符：逗號、句號、分號、冒號
    terms = re.split(r"[,，。；;:\s]+", text)
    # 清理空白並過濾空字串
    return [t.strip() for t in terms if t.strip() and len(t.strip()) >= 2]


def load_synonyms(path: Path) -> dict:
    """載入同義詞對照表"""
    if not path.exists():
        return {"indication_synonyms": {}, "drug_synonyms": {}}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# 通用關鍵字模式（跨語言適用）
GENERIC_KEYWORD_PATTERNS = {
    "_generic_cancer": [
        "cancer", "carcinoma", "tumor", "tumour", "neoplasm", "malignant",
        "leukemia", "lymphoma", "melanoma", "sarcoma", "myeloma",
        "암", "종양", "악성종양", "백혈병", "림프종"
    ],
    "_cardiovascular": [
        "cardiovascular", "atherosclerosis", "arteriosclerosis",
        "coronary", "vascular disease",
        "심혈관", "동맥경화", "관상동맥"
    ],
    "_heart_disease": [
        "heart disease", "heart failure", "cardiac", "myocardial",
        "arrhythmia", "angina", "cardiomyopathy",
        "심장병", "심부전", "부정맥", "협심증"
    ],
    "stroke": [
        "stroke", "ischemic stroke", "cerebrovascular",
        "뇌졸중", "뇌경색", "뇌출혈"
    ],
    "diabetes": [
        "diabetes", "diabetic", "glucose", "insulin",
        "당뇨병", "당뇨", "혈당"
    ],
    "hypertension": [
        "hypertension", "high blood pressure",
        "고혈압", "혈압"
    ],
    "dementia": [
        "dementia", "alzheimer", "cognitive impairment",
        "치매", "알츠하이머"
    ],
}


def build_keywords_from_synonyms(synonyms: dict) -> dict:
    """從同義詞表建立關鍵字索引"""
    keywords = {}

    # 疾病/適應症同義詞
    indication_synonyms = synonyms.get("indication_synonyms", {})
    for en_name, ko_list in indication_synonyms.items():
        key = en_name.lower()
        keywords[key] = {
            "english": [en_name],
            "korean": ko_list if isinstance(ko_list, list) else [ko_list],
            "type": "indication"
        }

    # 藥物同義詞
    drug_synonyms = synonyms.get("drug_synonyms", {})
    for en_name, ko_list in drug_synonyms.items():
        key = en_name.lower()
        keywords[key] = {
            "english": [en_name],
            "korean": ko_list if isinstance(ko_list, list) else [ko_list],
            "type": "drug"
        }

    # 添加通用關鍵字模式
    for pattern_name, pattern_list in GENERIC_KEYWORD_PATTERNS.items():
        english_terms = [t for t in pattern_list if not any('\uac00' <= c <= '\ud7a3' for c in t)]
        korean_terms = [t for t in pattern_list if any('\uac00' <= c <= '\ud7a3' for c in t)]

        keywords[pattern_name] = {
            "english": english_terms,
            "korean": korean_terms,
            "type": "generic"
        }

    return keywords


def build_keywords_from_predictions(predictions_path: Path) -> dict:
    """從預測結果建立關鍵字索引"""
    keywords = {}

    if not predictions_path.exists():
        return keywords

    try:
        import pandas as pd
        df = pd.read_csv(predictions_path)

        # 收集唯一的藥物和適應症
        if "drugbank_id" in df.columns:
            for drug_id in df["drugbank_id"].dropna().unique():
                key = str(drug_id).lower()
                keywords[key] = {
                    "english": [str(drug_id)],
                    "korean": [],
                    "type": "drug"
                }

        if "disease_name" in df.columns or "potential_indication" in df.columns:
            indication_col = "potential_indication" if "potential_indication" in df.columns else "disease_name"
            for indication in df[indication_col].dropna().unique():
                key = str(indication).lower()
                if key not in keywords:
                    keywords[key] = {
                        "english": [str(indication)],
                        "korean": [],
                        "type": "indication"
                    }

    except Exception as e:
        print(f"警告：無法載入預測結果: {e}")

    return keywords


def generate_keywords():
    """生成完整的關鍵字列表"""
    print("=" * 60)
    print("KrTxGNN - 生成新聞監測關鍵字")
    print("=" * 60)
    print()

    # 載入同義詞
    synonyms_path = DATA_DIR / "news" / "synonyms.json"
    synonyms = load_synonyms(synonyms_path)
    print(f"載入同義詞: {synonyms_path}")

    # 從同義詞建立關鍵字
    keywords = build_keywords_from_synonyms(synonyms)
    print(f"同義詞關鍵字數: {len(keywords)}")

    # 從預測結果補充關鍵字
    predictions_path = DATA_DIR / "processed" / "repurposing_candidates.csv.gz"
    if predictions_path.exists():
        pred_keywords = build_keywords_from_predictions(predictions_path)
        for key, value in pred_keywords.items():
            if key not in keywords:
                keywords[key] = value
        print(f"預測結果關鍵字數: {len(pred_keywords)}")

    # 生成輸出
    output = {
        "generated": datetime.now().isoformat(),
        "version": "1.0.0",
        "country": "KR",
        "total_keywords": len(keywords),
        "keywords": keywords
    }

    # 儲存
    output_path = DATA_DIR / "news" / "keywords.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print()
    print(f"已儲存至: {output_path}")
    print(f"總關鍵字數: {len(keywords)}")

    # 統計
    drug_count = sum(1 for k in keywords.values() if k.get("type") == "drug")
    indication_count = sum(1 for k in keywords.values() if k.get("type") == "indication")
    generic_count = sum(1 for k in keywords.values() if k.get("type") == "generic")

    print()
    print("關鍵字分類統計:")
    print(f"  - 藥物: {drug_count}")
    print(f"  - 適應症: {indication_count}")
    print(f"  - 通用模式: {generic_count}")


if __name__ == "__main__":
    generate_keywords()
