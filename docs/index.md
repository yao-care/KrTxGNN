---
layout: default
title: 약물 재창출 예측 — 대한민국
description: "TxGNN 약물재창출 보고서: 의약품안전나라(nedrug) 허가 의약품 673개에 대해 임상시험·문헌 근거에 따른 L1–L5 근거 수준을 제공합니다."
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

데이터셋: [의약품안전나라(nedrug) 의약품 검색](https://nedrug.mfds.go.kr/searchDrug). 매주 월요일 자동으로 내려받아 대조합니다. 자세한 내용: [데이터 출처]({{ '/sources/' | relative_url }}).

근거 수준별 보고서 수:

| 근거 수준 | 보고서 수 | 비율 |
|---|---|---|
| L1 | {{ site.data.drug_stats.level_counts.L1 }} | {{ site.data.drug_stats.level_counts.L1 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L2 | {{ site.data.drug_stats.level_counts.L2 }} | {{ site.data.drug_stats.level_counts.L2 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L3 | {{ site.data.drug_stats.level_counts.L3 }} | {{ site.data.drug_stats.level_counts.L3 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L4 | {{ site.data.drug_stats.level_counts.L4 }} | {{ site.data.drug_stats.level_counts.L4 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L5 | {{ site.data.drug_stats.level_counts.L5 }} | {{ site.data.drug_stats.level_counts.L5 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
{% assign na = site.data.drug_stats.total_drugs | minus: site.data.drug_stats.level_counts.L1 | minus: site.data.drug_stats.level_counts.L2 | minus: site.data.drug_stats.level_counts.L3 | minus: site.data.drug_stats.level_counts.L4 | minus: site.data.drug_stats.level_counts.L5 %}{% if na > 0 %}| N/A | {{ na }} | {{ na | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |{% endif %}

이 사이트의 예측 약물–질환 쌍 94개는 30개 TxGNN 사이트 중 다른 사이트에는 없습니다.

### 이 사이트에서 근거 수준이 가장 높은 의약품

| 의약품 | 근거 수준 |
|---|---|
| [Bromfenac](/drugs/bromfenac/) | L1 |
| [Busulfan](/drugs/busulfan/) | L1 |
| [Cefprozil](/drugs/cefprozil/) | L1 |
| [Clofarabine](/drugs/clofarabine/) | L1 |
| [Doxorubicin](/drugs/doxorubicin/) | L1 |
| [Ketorolac](/drugs/ketorolac/) | L1 |
| [Dapsone](/drugs/dapsone/) | L1 |
| [Acetylcysteine](/drugs/acetylcysteine/) | L2 |
| [Desoximetasone](/drugs/desoximetasone/) | L2 |
| [Diazepam](/drugs/diazepam/) | L2 |

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
본 프로젝트의 결과는 연구 참고용으로만 제공되며, 의료 조언을 구성하지 않습니다. 약물재창출 후보는 임상 검증을 거쳐야 적용할 수 있습니다.

---

## 개발사 소개

본 플랫폼은 **藥提醒科技有限公司** (yao.care)가 개발하고 운영합니다. 회사 정보, TxGNN 모델의 배경,
제품군 전체 사이트 목록은 <a href="{{ '/about/' | relative_url }}">소개</a> 페이지에서 확인할 수 있습니다.
