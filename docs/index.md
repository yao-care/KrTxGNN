---
layout: default
title: Home
nav_order: 1
---

# KrTxGNN - 韓國藥品老藥新用預測

한국 의약품 약물재창출 예측 시스템

{: .warning }
> **연구 참고용** - 본 결과는 연구 참고용으로만 사용되며, 의료 조언을 구성하지 않습니다.
>
> **僅供研究參考** - 本結果僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證才能應用。

---

## 關於 KrTxGNN

KrTxGNN 使用 [TxGNN](https://github.com/mims-harvard/TxGNN) 知識圖譜方法，對韓國 MFDS（식품의약품안전처）許可藥品進行老藥新用（drug repurposing）預測。

### 資料來源

| 來源 | 說明 |
|------|------|
| **MFDS** | 韓國食品醫藥品安全處藥品資料 |
| **DrugBank** | 藥物-靶點-疾病關係 |
| **TxGNN** | 知識圖譜預測模型 |
| **PubMed** | 文獻證據 |
| **ClinicalTrials.gov** | 臨床試驗 |
| **CRIS** | 韓國臨床試驗資訊服務 |

---

## 快速導航

- [藥物報告](/drugs/) - 查看個別藥物的老藥新用預測報告
- [FHIR API](/fhir/metadata) - 以 FHIR R4 格式存取預測資料
- [新聞監測](/news/) - 相關健康新聞動態

---

## 免責聲明 / 면책 조항

{: .important }
본 프로젝트의 결과는 연구 참고용으로만 제공됩니다. 약물재창출 후보는 임상 검증을 거쳐야 적용할 수 있습니다.

本專案結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。

The results of this project are for research reference only and do not constitute medical advice. Drug repurposing candidates require clinical validation before application.
