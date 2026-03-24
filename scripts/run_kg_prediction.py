#!/usr/bin/env python3
"""執行知識圖譜方法預測

使用 TxGNN 知識圖譜進行老藥新用預測。

使用方法:
    uv run python scripts/run_kg_prediction.py

前置條件:
    1. 已執行 process_fda_data.py
    2. 已執行 prepare_external_data.py (或已複製 external 資料)

產生檔案:
    data/processed/repurposing_candidates.csv
"""

from pathlib import Path

import pandas as pd
import yaml

# KrTxGNN 模組
from krtxgnn.data.loader import load_fda_drugs, filter_active_drugs, get_drug_summary
from krtxgnn.mapping.drugbank_mapper import map_fda_drugs_to_drugbank
from krtxgnn.mapping.disease_mapper import (
    map_fda_indications_to_diseases,
    get_indication_mapping_stats,
)
from krtxgnn.predict.repurposing import find_repurposing_candidates


def load_field_config() -> dict:
    """載入欄位映射設定"""
    config_path = Path(__file__).parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    print("=" * 60)
    print("KrTxGNN - 執行知識圖譜方法預測")
    print("韓國 MFDS 藥品老藥新用預測")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    config = load_field_config()
    field_mapping = config["field_mapping"]

    # 檢查必要檔案
    fda_data_path = base_dir / "data" / "raw" / "kr_fda_drugs.json"
    if not fda_data_path.exists():
        print("錯誤：找不到 MFDS 藥品資料")
        print(f"  預期位置: {fda_data_path}")
        print()
        print("請先執行: uv run python scripts/process_fda_data.py")
        return

    external_dir = base_dir / "data" / "external"
    if not (external_dir / "drugbank_vocab.csv").exists():
        print("錯誤：找不到 DrugBank 詞彙表")
        print(f"  預期位置: {external_dir / 'drugbank_vocab.csv'}")
        print()
        print("請先執行: uv run python scripts/prepare_external_data.py")
        return

    # 1. 載入藥品資料
    print("1. 載入 MFDS 藥品資料...")
    fda_df = load_fda_drugs()
    print(f"   總藥品數: {len(fda_df)}")

    active_df = filter_active_drugs(fda_df)
    print(f"   有效藥品數: {len(active_df)}")

    summary = get_drug_summary(active_df)
    print(f"   有成分資料: {summary.get('with_ingredient', 'N/A')}")

    # 2. DrugBank 映射
    print()
    print("2. 執行 DrugBank 映射...")
    drug_mapping = map_fda_drugs_to_drugbank(
        active_df,
        ingredient_field=field_mapping["ingredients"],
        license_field=field_mapping["license_id"],
        name_field=field_mapping["brand_name_local"]
    )
    mapped_count = drug_mapping["drugbank_id"].notna().sum() if len(drug_mapping) > 0 else 0
    total_count = len(drug_mapping)
    mapping_rate = mapped_count / total_count * 100 if total_count > 0 else 0
    print(f"   映射成功: {mapped_count} / {total_count} ({mapping_rate:.2f}%)")

    # 3. 疾病映射
    print()
    print("3. 執行疾病映射...")
    indication_mapping = map_fda_indications_to_diseases(
        active_df,
        indication_field=field_mapping["indication"],
        license_field=field_mapping["license_id"],
        brand_field=field_mapping["brand_name_local"]
    )
    indication_stats = get_indication_mapping_stats(indication_mapping)
    print(f"   提取適應症數: {indication_stats['total_indications']}")
    print(f"   映射成功: {indication_stats['mapped_indications']} ({indication_stats['mapping_rate']*100:.2f}%)")
    print(f"   唯一疾病數: {indication_stats['unique_diseases']}")

    # 4. 尋找老藥新用候選
    print()
    print("4. 尋找老藥新用候選...")
    candidates = find_repurposing_candidates(drug_mapping, indication_mapping)
    print(f"   候選數: {len(candidates)}")

    # 5. 儲存結果
    print()
    print("5. 儲存結果...")
    output_dir = base_dir / "data" / "processed"
    output_dir.mkdir(parents=True, exist_ok=True)

    # 儲存候選結果
    candidates_path = output_dir / "repurposing_candidates.csv.gz"
    candidates.to_csv(candidates_path, index=False)
    print(f"   已儲存至: {candidates_path}")

    # 儲存中間結果 (可選)
    drug_mapping.to_csv(output_dir / "drug_mapping.csv", index=False)
    indication_mapping.to_csv(output_dir / "indication_mapping.csv", index=False)
    print(f"   中間結果已儲存至: {output_dir}")

    # 顯示統計摘要
    print()
    print("=" * 60)
    print("預測結果摘要")
    print("=" * 60)
    print(f"  MFDS 藥品總數: {len(fda_df)}")
    print(f"  有效藥品數: {len(active_df)}")
    print(f"  DrugBank 映射率: {mapping_rate:.2f}%")
    print(f"  疾病映射率: {indication_stats['mapping_rate']*100:.2f}%")
    print(f"  老藥新用候選數: {len(candidates)}")
    print()
    print("下一步: 生成 FHIR 資源")
    print("  uv run python scripts/generate_fhir_resources.py")


if __name__ == "__main__":
    main()
