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

---

## 개발사 소개

본 플랫폼은 **藥提醒科技有限公司** (yao.care, 사업자등록번호 83620786, 12F, No. 220, Sec. 2,
Taiwan Blvd., West Dist., Taichung City, Taiwan)가 개발하고 운영합니다.

KrTxGNN은 이 회사의 "TxGNN 약물재창출" 제품군 중 대한민국 사이트입니다.
동일한 시스템이 30개 국가 및 지역에 배포되어 있으며, 각각 `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN 등)으로 명명되어 `{cc}txgnn.yao.care`에서 운영됩니다.
제품 개요: <https://www.yao.care/medical/txgnn/>.

TxGNN 모델 자체는 Harvard Medical School의 Zitnik Lab이 개발하여 *Nature Medicine*에
발표했습니다. 본 플랫폼은 藥提醒科技有限公司가 해당 모델을 기반으로 구축한 운영 시스템으로,
국가별 의약품 허가 데이터 통합, 지식 그래프와 딥러닝의 이중 예측, PubMed / ClinicalTrials
근거 등급화, SMART on FHIR 전자의무기록 연동을 포함합니다.
