# KrTxGNN - 韓國藥品老藥新用預測

使用 TxGNN 知識圖譜對韓國 MFDS 藥品進行老藥新用（drug repurposing）預測。

## 注意事項

- 본 프로젝트 결과는 연구 참고용으로만 사용되며, 의료 조언을 구성하지 않습니다
- 本專案結果僅供研究參考，不構成醫療建議
- 老藥新用候選需經過臨床驗證才能應用

## 資料來源

- **藥監局**: MFDS (식품의약품안전처)
- **藥品資料**: https://nedrug.mfds.go.kr/

## 安裝

```bash
uv sync
```

## 使用方式

```bash
# 處理 FDA 資料
uv run python scripts/process_fda_data.py

# 準備詞彙表資料
uv run python scripts/prepare_external_data.py

# 執行知識圖譜預測
uv run python scripts/run_kg_prediction.py

# 生成 FHIR 資源
uv run python scripts/generate_fhir_resources.py
```

## License

MIT
