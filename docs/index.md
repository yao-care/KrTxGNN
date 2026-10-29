---
layout: default
title: 약물 재창출 예측 — 대한민국
nav_order: 1
---

# KrTxGNN - 한국 의약품 약물재창출 예측

한국 의약품 약물재창출 예측 시스템

{: .warning }
> **연구 참고용** - 본 결과는 연구 참고용으로만 사용되며, 의료 조언을 구성하지 않습니다.

---

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## 대한민국: 이 사이트의 수록 범위

이 사이트는 [MFDS](https://www.mfds.go.kr/) 허가 정보(대한민국)에 수록된 의약품 **{{ site.data.drug_stats.total_drugs }}**개 품목의 보고서를 공개합니다.

근거 수준별 보고서 수: L1 {{ site.data.drug_stats.level_counts.L1 }} · L2 {{ site.data.drug_stats.level_counts.L2 }} · L3 {{ site.data.drug_stats.level_counts.L3 }} · L4 {{ site.data.drug_stats.level_counts.L4 }} · L5 {{ site.data.drug_stats.level_counts.L5 }}

### 이 사이트에서 근거 수준이 가장 높은 의약품

| 의약품 | 근거 수준 |
|---|---|
| [Bromfenac](/drugs/bromfenac/) | L1 |
| [Busulfan](/drugs/busulfan/) | L1 |
| [Lanadelumab](/drugs/lanadelumab/) | L1 |
| [Rifabutin](/drugs/rifabutin/) | L1 |
| [Tegafur](/drugs/tegafur/) | L1 |
| [Cefprozil](/drugs/cefprozil/) | L1 |
| [Hydrocortisone](/drugs/hydrocortisone/) | L1 |
| [Hydrocortisone Acetate](/drugs/hydrocortisone-acetate/) | L1 |
| [Clofarabine](/drugs/clofarabine/) | L1 |
| [Doxorubicin](/drugs/doxorubicin/) | L1 |

### 30개 TxGNN 사이트 중 이 사이트에만 수록된 의약품

| 의약품 | 근거 수준 |
|---|---|
| [Propacetamol](/drugs/propacetamol/) | L3 |
| [Pranlukast](/drugs/pranlukast/) | L4 |
| [Cefamandole Nafate](/drugs/cefamandole-nafate/) | L5 |
| [Magnesium Lactate](/drugs/magnesium-lactate/) | L5 |
| [Pegteograstim](/drugs/pegteograstim/) | L5 |
| [Proxyphylline](/drugs/proxyphylline/) | L5 |
| [Talniflumate](/drugs/talniflumate/) | L5 |
| [Cyclofenil](/drugs/cyclofenil/) | L5 |
| [Polmacoxib](/drugs/polmacoxib/) | L5 |
| [Anagliptin](/drugs/anagliptin/) | L5 |
| [Clevudine](/drugs/clevudine/) | L5 |
| [Ethyl Loflazepate](/drugs/ethyl-loflazepate/) | L5 |
| [Hydrocortisone Probutate](/drugs/hydrocortisone-probutate/) | L5 |
| [Oxiracetam](/drugs/oxiracetam/) | L5 |
| [Tiemonium Iodide](/drugs/tiemonium-iodide/) | L5 |

<!-- local-home:end -->

## KrTxGNN 소개

KrTxGNN은 [TxGNN](https://github.com/mims-harvard/TxGNN) 모델(딥러닝)을 사용하여 식품의약품안전처(MFDS) 허가 의약품의 약물재창출(drug repurposing) 가능성을 예측합니다.

### 데이터 출처

| 출처 | 설명 |
|------|------|
| **MFDS** | 식품의약품안전처 의약품 데이터 |
| **DrugBank** | 약물-표적-질환 관계 |
| **TxGNN** | 지식 그래프로 학습한 그래프 신경망 모델 |
| **PubMed** | 문헌 근거 |
| **ClinicalTrials.gov** | 임상시험 |
| **CRIS** | 한국 임상연구정보서비스 |

---

## 빠른 탐색

- [약물 보고서](/drugs/) - 개별 약물의 약물 재창출 예측 보고서 보기
- [FHIR API](/fhir/metadata) - FHIR R4 형식으로 예측 데이터에 접근

---

## 면책 조항

{: .important }
본 프로젝트의 결과는 연구 참고용으로만 제공됩니다. 약물재창출 후보는 임상 검증을 거쳐야 적용할 수 있습니다.

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
국가별 의약품 허가 데이터 통합, 지식 그래프에 이미 기록된 용도를 제외한 딥러닝 예측, PubMed / ClinicalTrials
근거 등급화, SMART on FHIR 전자의무기록 연동을 포함합니다.
