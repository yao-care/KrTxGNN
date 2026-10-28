---
layout: default
title: Lenalidomide
parent: 높은 근거 (L1-L2)
nav_order: 466
evidence_level: L2
indication_count: 4
monitor_inn: "LENALIDOMIDE"
predicted_indications: ["myeloid leukemia", "refractory cytopenia of childhood", "aregenerative anemia", "severe congenital hypochromic anemia with ringed sideroblasts"]
last_modified_at: 2026-10-28
description: "Lenalidomide: 예측 신규 적응증 골수성 백혈병 (myeloid leukemia) (근거 수준 L2). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201706896/EE"
---

# Lenalidomide
{: .fs-9 }

근거 수준: **L2** | 예측 적응증: **4** 건
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

## Lenalidomide: 면역조절제(CRBN 기반 단백질 분해 유도) → 골수성 백혈병 (myeloid leukemia)
{: .text-alpha }

## 한 문장 요약

Lenalidomide는 세레블론(CRBN)에 결합하여 IKZF1/IKZF3 등의 단백질 분해를 유도하는 경구용 면역조절제입니다.
TxGNN 모델은 **골수성 백혈병(myeloid leukemia)**에 효과가 있을 수 있다고 예측하며, 이 예측에 대해 수집된 자료에는 **임상시험 44건**과 **문헌 20편**이 있으나, 이 중 상당수는 골수이형성증후군(MDS) 또는 다른 질환을 다룹니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201706896/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201706892/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201900220/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201706898/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201802378/EE;  |
| 예측 신규 적응증 | 골수성 백혈병 (myeloid leukemia) |
| TxGNN 예측 점수 | 0.9949 |
| 근거 수준 | L2 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 12건 (단일 성분) |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터(DrugBank)는 수집되지 않았습니다. 다만 문헌에 따르면 lenalidomide는 CRBN에 결합해 CRL4-CRBN E3 유비퀴틴 리가아제가 IKZF1/IKZF3를 분해하도록 유도하며, del(5q) 세포에서는 CK1α 분해에도 관여합니다. 이와 함께 T세포·NK세포 활성화 등 면역조절 효과와 항증식 효과를 나타냅니다.

이러한 기전은 MDS와 급성 골수성 백혈병(AML) 같은 골수성 악성 종양, 특히 CK1α 반수체 부족으로 감수성이 높은 del(5q) 질환에서 타당성이 있습니다. 2025년 연구에서는 CRBN 안정화가 AML 세포의 lenalidomide 감수성을 높일 수 있음이 보고되었습니다.

다만 인용된 시험들은 AML, 고위험 MDS, 이식 후 유지요법 등으로 이질적이어서, 특정한 한 가지 골수성 백혈병 아형에 대한 신호로 보기는 어렵습니다.

## 임상시험 근거

관련성이 높은 시험을 우선하여 10건을 정리했습니다(단일 군 또는 소규모 시험이 대부분입니다).

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02126553](https://clinicaltrials.gov/study/NCT02126553) | Phase 2 | 완료 | 29 | 관해 상태의 고위험 AML에서 lenalidomide 유지요법. 직접 관련되나 단일 군·소규모 |
| [NCT00360672](https://clinicaltrials.gov/study/NCT00360672) | Phase 2 | 완료 | 27 | 5번 염색체 이상이 있는 재발·불응성 AML 또는 고위험 MDS에서 단독 요법 |
| [NCT00352365](https://clinicaltrials.gov/study/NCT00352365) | Phase 2 | 완료 | 41 | 관해 유도 화학요법을 거부한 60세 이상 del(5q) AML 환자 대상 |
| [NCT00546897](https://clinicaltrials.gov/study/NCT00546897) | Phase 2 | 완료 | 48 | 5q 이상이 없는 60세 이상 미치료 AML 환자 대상 안전성·효능 평가 |
| [NCT01358734](https://clinicaltrials.gov/study/NCT01358734) | Phase 2 | 완료 | 88 | 65세 이상 신규 진단 AML에서 고용량 lenalidomide, azacitidine 순차 병용, azacitidine 단독 비교 |
| [NCT01301820](https://clinicaltrials.gov/study/NCT01301820) | Phase 2 | 완료 | 120 | 고령 AML 첫 완전관해 후 lenalidomide와 azacitidine 교대 유지요법 |
| [NCT00957385](https://clinicaltrials.gov/study/NCT00957385) | Phase 2 | 완료 | 24 | AML 관해 유지에서 lenalidomide 효과 평가(무작위 배정) |
| [NCT02538965](https://clinicaltrials.gov/study/NCT02538965) | Phase 2 | 완료 | 17 | 소아 재발·불응성 AML에서 활성·안전성·약동학 평가 |
| [NCT04490707](https://clinicaltrials.gov/study/NCT04490707) | Phase 3 | 불명 | 60 | 고령·부적합 AML에서 MRD 기반 azacitidine+lenalidomide 유지요법 |
| [NCT01038635](https://clinicaltrials.gov/study/NCT01038635) | Phase 1/2 | 완료 | 94 | 고위험 MDS 및 AML에서 5-azacitidine과 lenalidomide 병용 |

## 문헌 근거

이 예측에 연결된 문헌은 대부분 MDS·AML 관련 종설이며, 무작위 대조 임상시험은 포함되지 않았습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [23316859](https://pubmed.ncbi.nlm.nih.gov/23316859/) | 2013 | Review | Expert Opin Investig Drugs | AML에 대한 lenalidomide 신규 치료 가능성 검토. 저위험 del(5q) MDS와 다발골수종에서 승인된 약으로 소개 |
| [32899586](https://pubmed.ncbi.nlm.nih.gov/32899586/) | 2020 | 종설 | Cancers | AML 치료에서의 면역조절제(IMiD) 역할 정리 |
| [39881283](https://pubmed.ncbi.nlm.nih.gov/39881283/) | 2025 | 기전 연구 | Cell Mol Biol Lett | KDM5C가 CRBN을 안정화하여 AML 세포의 lenalidomide 감수성을 높임 |
| [37288607](https://pubmed.ncbi.nlm.nih.gov/37288607/) | 2023 | Review | Am J Hematol | MDS의 진단, 위험도 분류 및 치료 2023 업데이트 |
| [42400116](https://pubmed.ncbi.nlm.nih.gov/42400116/) | 2026 | Review | Am J Hematol | MDS 진단, 위험도 분류 및 치료 2026 업데이트 |
| [41348013](https://pubmed.ncbi.nlm.nih.gov/41348013/) | 2025 | Review | Hematology ASH Educ Program | 저·중간위험 MDS 치료 최신 동향 |
| [37874917](https://pubmed.ncbi.nlm.nih.gov/37874917/) | 2023 | Review | Blood | MDS의 임상적 의사결정과 치료 |
| [29795386](https://pubmed.ncbi.nlm.nih.gov/29795386/) | 2018 | 종설 | Blood Cancer J | MDS 치료 알고리즘 2018 |
| [24656536](https://pubmed.ncbi.nlm.nih.gov/24656536/) | 2014 | Review | Lancet | 골수이형성증후군 개괄 |
| [22483153](https://pubmed.ncbi.nlm.nih.gov/22483153/) | 2012 | 종설 | Curr Cancer Drug Targets | AML의 신규 및 개발 중인 약물 |

## 한국 시판 정보

한국에서 lenalidomide 단일 성분 유효 허가 12건이 확인되며, 허가 적응증 본문은 PDF 링크로만 제공되어 데이터에서 직접 확인되지 않았습니다. 주요 5건은 다음과 같습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201706896 | 레날도캡슐20mg(수출용) | 경질 캡슐 | 허가 문서 링크만 제공됨 |
| 201706892 | 레날도캡슐7.5mg(수출용) | 경질 캡슐 | 허가 문서 링크만 제공됨 |
| 201900220 | 레블리킨캡슐5밀리그램 | 경질 캡슐 | 허가 문서 링크만 제공됨 |
| 201706898 | 레날도캡슐10mg | 경질 캡슐 | 허가 문서 링크만 제공됨 |
| 201802378 | 레블리킨캡슐25밀리그램 | 경질 캡슐 | 허가 문서 링크만 제공됨 |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 면역조절제(IMiD, 탈리도마이드 유도체). 전통적 세포독성 화학요법제와는 구분됨 |
| 골수억제 위험 | 높음. 호중구감소증·혈소판감소증은 흔히 주의해야 할 위험으로 알려져 있음 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 전혈구 검사(CBC, 분류 포함), 신기능 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **금기 관련 질환(데이터 기반 연관 정보, 허가 문구 아님)**: 혈소판감소증, 호중구감소증, 무과립구증, 폐색전증, 신기능 장애, 암, 배아종
- **약물 상호작용**: 총 100건이 조회되었습니다. 주요(Major) 등급으로는 rosuvastatin, simvastatin이 있고, 중등도(Moderate) 등급으로는 eliglustat, naltrexone이 있습니다.

허가사항의 경고·금기 원문은 확보되지 않았으므로 허가사항을 직접 확인해야 합니다.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
AML을 대상으로 한 Phase 2 시험이 다수 있어 근거 수준은 L2로 판정되지만, 대부분 단일 군·소규모이며 병용요법이 많아 lenalidomide 단독 효과를 분리하기 어렵습니다. 또한 연결된 시험이 AML, 고위험 MDS, 이식 후 유지요법 등으로 이질적이어서 특정 골수성 백혈병 아형에 대한 결론은 제한적입니다.

**진행하려면 필요한 것:**
- 허가 문서의 적응증, 경고, 금기 원문 확보(현재 자료 공백으로 안전성 선별을 진행할 수 없음)
- 상세한 작용 기전 데이터(DrugBank) 보완
- 아형(AML, del(5q) 등)별로 구분한 효능 근거 정리 및 무작위 대조시험 확인
- 골수억제(호중구감소증·혈소판감소증)와 혈전 위험에 대한 모니터링 계획 수립
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

