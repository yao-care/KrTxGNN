---
layout: default
title: Doxorubicin
parent: 높은 근거 (L1-L2)
nav_order: 292
evidence_level: L1
indication_count: 8
monitor_inn: "Doxorubicin"
predicted_indications: ["Ewing sarcoma", "well-differentiated fetal adenocarcinoma of the lung", "primary pulmonary lymphoma", "pulmonary blastoma", "monocytic leukemia", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "parameningeal embryonal rhabdomyosarcoma", "rhabdomyosarcoma (disease)"]
last_modified_at: 2026-10-23
description: "Doxorubicin: 예측 신규 적응증 유잉육종 (근거 수준 L1). 기존 적응증: 확인 불가 (허가 적응증 본문 없음, 허가 문서 링크만 제공됨)"
---

# Doxorubicin
{: .fs-9 }

근거 수준: **L1** | 예측 적응증: **8** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 약사 평가 보고서

</div>

## Doxorubicin: 허가 적응증 정보 미확인에서 유잉육종으로
{: .text-alpha }

## 한 문장 요약

Doxorubicin은 한국에서 단일성분 주사제로 허가되어 있으나, 이번 데이터에는 허가 적응증 본문이 없고 허가 문서 링크만 있어 구체적인 기존 적응증을 확인할 수 없습니다.
TxGNN 모델은 **유잉육종(Ewing sarcoma)**에 효과가 있을 수 있다고 예측하며, 이 질환을 직접 다룬 **여러 임상시험**(Phase 3 포함)과 **문헌**이 있습니다.
다만 이는 이미 표준 치료에 포함된 사용으로, 새로운 재창출이라기보다 기존 임상 근거를 확인하는 성격이 강합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 적응증 본문 없음, 허가 문서 링크만 제공됨) |
| 예측 신규 적응증 | 유잉육종 |
| TxGNN 예측 점수 | 0.9990 |
| 근거 수준 | L1 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가 건수 | 12건 (단일성분 12건, 유효 12건) |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 없습니다. 알려진 정보에 따르면 Doxorubicin은 topoisomerase II 억제 및 DNA 삽입(intercalation)을 통해 작용하는 안트라사이클린 계열 세포독성 항암제입니다.

유잉육종에서는 VDC/IE, VAC/VAI 등 다제 병용 화학요법의 핵심 약물로 쓰입니다. 이 종양이 화학요법에 민감하다는 점과도 일치합니다. 따라서 높은 TxGNN 점수는 임상 현실과 부합하며, 새로운 발견이라기보다 확립된 표준 치료 사용을 재확인한 결과로 보는 것이 적절합니다.

## 임상시험 근거

유잉육종을 직접 대상으로 하고 Doxorubicin이 포함된 시험 중 대표적인 것을 정리했습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | 완료 | 642 | 비전이성 유잉육종에서 표준 5제 요법(vincristine, doxorubicin, cyclophosphamide, ifosfamide, etoposide)에 VTC 추가 비교 |
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | 완료 | 278 | 비전이성 유잉육종에서 용량 강화 치료 대 표준 치료 비교 |
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Phase 3 | 완료 | 587 | 유잉육종에서 화학요법 압축 투여를 통한 강화 비교 |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | 활성, 모집 종료 | 312 | 전이성 유잉육종에서 다제 화학요법에 ganitumab 추가 |
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Phase 3 | 불명 | 1200 | EURO-E.W.I.N.G.99, 화학요법 및 방사선·줄기세포이식 비교 |
| [NCT00038142](https://clinicaltrials.gov/study/NCT00038142) | Phase 2 | 조기 종료 | 46 | 고위험 유잉육종에서 VAC+dexrazoxane에 ImmTher 추가 여부 비교 |
| [NCT00003667](https://clinicaltrials.gov/study/NCT00003667) | Phase 2 | 완료 | 정보 없음 | 고위험 유잉육종에서 VAC+dexrazoxane에 ImmTher 추가 여부 비교 |
| [NCT00002466](https://clinicaltrials.gov/study/NCT00002466) | Phase 2 | 완료 | 정보 없음 | doxorubicin 포함 다제 화학요법 후 절제·방사선 치료 |
| [NCT01864109](https://clinicaltrials.gov/study/NCT01864109) | Phase 2 | 활성, 모집 종료 | 83 | 신규 진단 유잉육종에서 irinotecan·temozolomide 추가 (doxorubicin은 기본 요법) |
| [NCT07194044](https://clinicaltrials.gov/study/NCT07194044) | Phase 1 | 모집 중 | 15 | 전이성 유잉육종 일정 최적화 접근 |

위 Phase 3 시험들은 대부분 doxorubicin 포함 표준 요법을 기반으로 다른 요소(추가 약물, 투여 간격, 용량)를 비교한 것입니다. Doxorubicin 단독 효과를 분리해 평가한 시험은 아닙니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | RCT | N Engl J Med | 신규 진단 유잉육종·원시신경외배엽종양에서 표준 화학요법에 ifosfamide·etoposide 추가 |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | RCT (Phase 3) | Lancet | EE2012, 신규 진단 유잉육종에서 두 가지 화학요법 요법 비교 |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | RCT (Phase 3) | J Clin Oncol | 전이성 유잉육종에서 ganitumab과 간격 압축 화학요법 |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | RCT | J Clin Oncol | 국소 유잉육종에서 간격 압축 화학요법의 효과 |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | RCT 프로토콜 | Trials | EURO EWING 2012 프로토콜 |
| [1833556](https://pubmed.ncbi.nlm.nih.gov/1833556/) | 1991 | 용량강도 분석 | J Natl Cancer Inst | 골육종·유잉육종에서 doxorubicin 용량강도와 반응·예후의 관계 |
| [37403815](https://pubmed.ncbi.nlm.nih.gov/37403815/) | 2023 | Review | Cancer | 유잉육종 관리에 대한 국가 종양위원회 합의 권고안 |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Review | J Clin Oncol | 유잉육종의 현재 치료와 향후 접근 |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | Review | Lancet Oncol | 유잉육종 개괄 |
| [30231396](https://pubmed.ncbi.nlm.nih.gov/30231396/) | 2018 | Review | ASCO Educ Book | 안트라사이클린 심독성의 예측과 예방 (소아 유잉육종 치료 포함) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199201595 | 한국유나이티드염산독소루비신주 (수출용) | 동결건조분말 바이알 | 허가 문서 링크만 제공됨 (적응증 본문 없음) |
| 199000353 | 일동아드리아마이신피.에프.에스.주사액10밀리그램 | 액상 주사제 | 허가 문서 링크만 제공됨 (적응증 본문 없음) |
| 199806569 | 케릭스주사 (리포좀화한독소루비신염산염) | 리포좀 현탁 주사제 | 허가 문서 링크만 제공됨 (적응증 본문 없음) |
| 199001007 | 에이디마이신주사액 | 액상 주사제 | 허가 문서 링크만 제공됨 (적응증 본문 없음) |
| 199203366 | 독소루빈주사0.2% | 액상 바이알 | 허가 문서 링크만 제공됨 (적응증 본문 없음) |

총 12건이 모두 단일성분이며 유효 상태입니다. 이 중 수출용 허가도 여럿 포함되어 있습니다. 위 표는 대표 5건만 나열한 것입니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (안트라사이클린 계열, topoisomerase II 억제제) |
| 골수억제 위험 | 고 |
| 구토 유발성 등급 | 중~고 |
| 모니터링 항목 | CBC(분류 포함), 간기능, 신기능, 심기능(심초음파 등) |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

이 분류는 이번 데이터에 직접 기재된 내용이 아니라 약물 계열에 근거한 일반적 평가입니다. 자세한 내용은 허가사항의 경고 및 주의사항을 참조하세요.

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 이 중 주요(Major) 상호작용은 다음과 같습니다.
  - Dolasetron
  - Cisapride
  - Papaverine
- 중등도(Moderate) 상호작용에는 ondansetron, granisetron, palonosetron, aprepitant, rolapitant, dexamethasone, clarithromycin, levofloxacin 등이 있습니다. 항구토제 및 QT 연장 관련 약물이 다수 포함되어 있습니다.
- 경미한(Minor) 상호작용으로는 ascorbic acid, metronidazole 등이 있습니다.

경고 및 금기 정보는 허가사항을 참조하세요. 안트라사이클린 심독성은 문헌에서도 주요 이슈로 언급됩니다.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
유잉육종을 직접 다룬 완료된 Phase 3 시험이 여러 건 있고, Doxorubicin은 표준 다제 화학요법의 구성 약물입니다. 다만 허가 적응증 본문, 작용 기전, 경고·금기 정보가 없어 한국 허가 범위에 이 질환이 포함되는지 확인되지 않았습니다.

**진행하려면 필요한 것:**
- 식약처 허가사항 PDF를 내려받아 적응증, 경고, 금기 확인
- DrugBank 등에서 작용 기전 데이터 보완
- 누적 용량에 따른 심독성 모니터링 계획 수립
- 한국 허가 적응증에 유잉육종이 포함되는지 확인하고, 포함되지 않으면 허가 외 사용 절차 검토

### 참고: 기타 예측 질환 (간략)

| 예측 질환 | TxGNN 점수 | 근거 수준 | 권고 |
|---------|-----------|---------|------|
| 폐 태아성 고분화 선암 | 0.9986 | L5 | Hold |
| 원발성 폐 림프종 | 0.9985 | L5 | Research Question |
| 폐 모세포종 | 0.9985 | L3 | Proceed with Guardrails |
| 단핵구성 백혈병 | 0.9974 | L5 | Hold |
| 질 포도상 배아성 횡문근육종 | 0.9972 | L5 | Hold |
| 뇌수막 주변 배아성 횡문근육종 | 0.9971 | L5 | Hold |
| 횡문근육종 | 0.9970 | L1 | Proceed with Guardrails |

원발성 폐 림프종, 폐 모세포종, 단핵구성 백혈병 등은 해당 질환을 직접 대상으로 한 doxorubicin 시험이 제시되지 않아 근거 수준을 L5로 조정했습니다. 횡문근육종도 제시된 Phase 3 시험들이 주로 연부조직육종 전반을 다룬 것이어서, 이 질환을 직접 연구한 근거가 충분한지 추가 검토가 필요합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

