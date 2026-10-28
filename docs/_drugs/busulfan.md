---
layout: default
title: Busulfan
parent: 높은 근거 (L1-L2)
nav_order: 165
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-28
description: "Busulfan: 예측 신규 적응증 골수이형성증후군 (Myelodysplastic Syndrome) (근거 수준 L5). 기존 적응증: 확인 불가 (허가 적응증 정보가 문서 링크로만 제공되어 본문을 확인하지 못함)"
monitor_inn: "BUSULFAN"
predicted_indications: ["myelodysplastic syndrome", "refractory cytopenia of childhood", "unclassified myelodysplastic syndrome", "partial deletion of the long arm of chromosome 5", "aregenerative anemia", "severe congenital hypochromic anemia with ringed sideroblasts", "HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "seborrheic keratosis", "feline acquired immunodeficiency syndrome"]
---

# Busulfan
{: .fs-9 }

근거 수준: **L1** | 예측 적응증: **10** 건
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

## Busulfan: 기존 적응증에서 골수이형성증후군으로
{: .text-alpha }

## 한 문장 요약

Busulfan은 알킬화 계열의 세포독성 항암제로, 한국에서 주사제와 정제 형태로 허가되어 있습니다. 다만 이번 보고서에 정리된 자료에는 허가 적응증 본문이 포함되어 있지 않아, 기존 적응증은 확인하지 못했습니다.
TxGNN 모델은 **골수이형성증후군(Myelodysplastic Syndrome, MDS)**에 효과가 있을 수 있다고 예측하며, 현재 **임상시험 39건**과 **문헌 20편**이 이 방향과 관련되어 있습니다. 이 근거는 대부분 동종 조혈모세포이식 전처치 요법(conditioning)에 busulfan이 쓰인 연구입니다. 단독 질병 치료제로서의 근거가 아닙니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 적응증 정보가 문서 링크로만 제공되어 본문을 확인하지 못함) |
| 예측 신규 적응증 | 골수이형성증후군 (Myelodysplastic Syndrome) |
| TxGNN 예측 점수 | 0.9962 |
| 근거 수준 | L1 (완료된 Phase 3 RCT 2건 이상: NCT00822393, NCT00005866) |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 4건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 busulfan은 DNA를 교차결합시키는 이관능성 알킬화제이며, 고용량에서는 골수를 제거(myeloablation)하는 효과가 있습니다.

MDS는 조혈모세포의 클론성 질환이며, 동종 조혈모세포이식이 유일하게 완치를 기대할 수 있는 치료입니다. Busulfan은 fludarabine, clofarabine, cyclophosphamide 등과 함께 전처치 요법의 중심 약물로 쓰입니다. 악성 클론을 제거하고 공여 줄기세포가 자랄 골수 공간을 만드는 역할입니다.

따라서 이 예측은 질병을 직접 변화시키는 단독 요법이 아니라, **이식 전처치제로서의 용도**로 해석하는 것이 타당합니다. 대부분의 시험에서 busulfan은 여러 약물과 병용되므로 busulfan 단독 효과를 분리하기 어렵습니다.

## 임상시험 근거

관련성이 높은 순서로 정리했습니다. 이 목록에서 완료된 Phase 3 시험은 두 건이며, 나머지는 Phase 2 또는 Phase 2/3입니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00822393](https://clinicaltrials.gov/study/NCT00822393) | Phase 3 | 완료 | 570 | 이식 표준 전처치가 어려운 AML/MDS 환자에서 treosulfan 기반 vs 감량 busulfan 기반 전처치 비교 |
| [NCT00005866](https://clinicaltrials.gov/study/NCT00005866) | Phase 3 | 완료 | 240 | 진행성 MDS 또는 MDS 관련 AML에서 Busulfan-TBI vs Cyclophosphamide-TBI 전처치 비교 |
| [NCT04708054](https://clinicaltrials.gov/study/NCT04708054) | Phase 2/3 | 모집 중 | 324 | 고위험 AML/MDS에서 분할 busulfan 요법에 venetoclax 추가 |
| [NCT05453552](https://clinicaltrials.gov/study/NCT05453552) | Phase 2/3 | 불명 | 242 | 고위험 MDS에서 G-CSF+decitabine+BuCy vs BF 전처치 비교 |
| [NCT04713956](https://clinicaltrials.gov/study/NCT04713956) | Phase 2/3 | 불명 | 242 | RAEB-1/2 및 MDS 이행 AML에서 동일한 두 전처치 비교 |
| [NCT00502905](https://clinicaltrials.gov/study/NCT00502905) | Phase 2 | 완료 | 200 | AML/MDS에서 정맥 busulfan + fludarabine 이식 전처치 |
| [NCT02250937](https://clinicaltrials.gov/study/NCT02250937) | Phase 2 | 활성(모집 종료) | 116 | AML/MDS에서 venetoclax + 순차 busulfan/cladribine/fludarabine 전처치 |
| [NCT01168219](https://clinicaltrials.gov/study/NCT01168219) | Phase 2 | 완료 | 68 | 고위험 MDS에서 busulfan/fludarabine/ATG 이식 후 azacitidine 추가 |
| [NCT01643668](https://clinicaltrials.gov/study/NCT01643668) | Phase 2 | 완료 | 34 | 감량 강도 busulfan/clofarabine 전처치 후 동종이식 |
| [NCT06247917](https://clinicaltrials.gov/study/NCT06247917) | Phase 2 | 불명 | 59 | MDS에서 FLU-BU-MEL 전처치 단일군 시험 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [31606445](https://pubmed.ncbi.nlm.nih.gov/31606445/) | 2020 | RCT | Lancet Haematol | 고령 AML/MDS에서 treosulfan+fludarabine vs 감량 busulfan+fludarabine 전처치 비열등성 Phase 3 시험 |
| [35617104](https://pubmed.ncbi.nlm.nih.gov/35617104/) | 2022 | RCT | Am J Hematol | 위 Phase 3 시험의 최종 분석. 고령 AML/MDS에서 treosulfan이 감량 busulfan보다 이식 성적 개선 |
| [36702138](https://pubmed.ncbi.nlm.nih.gov/36702138/) | 2023 | RCT | Lancet Haematol | MDS-RAEB/이차성 AML에서 G-CSF+decitabine+BuCy vs BuCy 전처치의 재발 비교 Phase 3 시험 |
| [42285355](https://pubmed.ncbi.nlm.nih.gov/42285355/) | 2026 | RCT | Transplant Cell Ther | AML/MDS에서 busulfan 분할 일정 2가지 비교 Phase 2 무작위 시험 |
| [40079242](https://pubmed.ncbi.nlm.nih.gov/40079242/) | 2025 | Review | Am J Hematol | 골수섬유증 및 MDS에서 동종이식에 대한 최신 종설 |
| [33425740](https://pubmed.ncbi.nlm.nih.gov/33425740/) | 2020 | 체계적 문헌고찰/메타분석 | Front Oncol | MDS/AML에서 treosulfan 기반 vs busulfan 기반 전처치의 장기 성적 비교 |
| [34692485](https://pubmed.ncbi.nlm.nih.gov/34692485/) | 2021 | 메타분석 | Front Oncol | AML/MDS에서 감량 강도 vs 골수제거 전처치 RCT 메타분석 |
| [34489555](https://pubmed.ncbi.nlm.nih.gov/34489555/) | 2021 | 후향 연구 | Bone Marrow Transplant | MDS에서 Flu/Bu4 vs Bu4/Cy 성향점수 매칭 분석 |
| [35296446](https://pubmed.ncbi.nlm.nih.gov/35296446/) | 2022 | 후향 연구 | Transplant Cell Ther | MDS에서 골수제거 vs 감량 강도 Flu/Bu 비교 |
| [37856098](https://pubmed.ncbi.nlm.nih.gov/37856098/) | 2024 | 위험 평가 | Pediatr Blood Cancer | Busulfan 노출과 이차 악성종양 위험에 대한 근거 기반 평가 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200908906 | 부설펙스주(바이알)(부설판) | 주사제 (바이알, 무색 액상) | 허가 적응증 본문 미확인 |
| 202301532 | 부설칸주(부설판) | 주사제 (바이알) | 허가 적응증 본문 미확인 |
| 200402422 | 이텍스부설판정(부설판)(수출용) | 정제 (흰색 원형) | 허가 적응증 본문 미확인 |
| 201007762 | 설판정(부설판)(수출용) | 정제 (백색 원형) | 허가 적응증 본문 미확인 |

정제 2건은 수출용 허가입니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (알킬화제) |
| 골수억제 위험 | 고 (고용량에서 골수제거 효과가 있고, 이를 이용해 이식 전처치에 사용) |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | CBC(분류 포함), 간기능 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

## 안전성 고려사항

- **약물 상호작용**: 이번 보고서에 정리된 자료에서 100건의 상호작용이 확인되었으며, 일부는 다음과 같습니다.
  - 주요(Major): Metronidazole
  - 중등도(Moderate): Aprepitant, Miconazole
  - 경미(Minor): Levofloxacin
  - 등급 미상: Amphotericin B, 제산제·위산억제제(omeprazole 등), 코르티코스테로이드(dexamethasone 등), 항구토제(ondansetron 등) 외 다수
- **지식그래프 기반 금기 질환(허가 문서 기준이 아님)**: 혈소판감소증, 호중구감소증, 무과립구증, 빈혈, 폐섬유증, 간질, 감염성 질환 등이 연관되어 있습니다. 허가사항 확인 후 해석해야 합니다.
- **이차 악성종양**: busulfan 노출과 이차 악성종양의 연관성이 문헌에서 평가되고 있습니다 (PMID 37856098).

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
MDS 이식 전처치에서 busulfan의 사용을 지지하는 Phase 3 시험이 2건 완료되었고, 추가 Phase 2/3 시험과 RCT 문헌도 있습니다. 다만 근거는 병용 요법 전처치에 한정되며, busulfan의 기여를 분리하기 어렵고 단독 치료제로서의 근거는 없습니다. 또한 한국 허가 적응증과 안전성 정보를 아직 확인하지 못했습니다.

**진행하려면 필요한 것:**
- 한국 허가사항(적응증, 경고, 금기) 확인: 허가 문서 PDF를 내려받아 분석 필요
- 상세 작용 기전(MOA) 데이터 확보: DrugBank 조회
- 허가 적응증에 이식 전처치가 이미 포함되어 있는지 확인
- 이식 전처치 용도로 한정한 적응증 범위 설정 (단독 치료로는 해석하지 않음)
- 골수억제, 이차 악성종양, 간독성 등에 대한 모니터링 및 안전성 계획 수립

### 참고: 기타 예측 질환

| 순위 | 질환 | 점수 | 근거 수준 | 권장 |
|------|------|------|----------|------|
| 2 | 소아 불응성 혈구감소증 | 0.9954 | L2 | Proceed with Guardrails |
| 3 | 분류불능 MDS | 0.9953 | L5 | Research Question |
| 4 | 5번 염색체 장완 부분 결손 | 0.9951 | L5 | Hold |
| 5 | 재생불량성 빈혈 유형 | 0.9949 | L5 | Proceed with Guardrails |
| 6 | 고리철적모구를 동반한 선천성 저색소성 빈혈 | 0.9949 | L5 | Hold |
| 7 | HIV 감염 | 0.9944 | L3 | Research Question |

순위 5번(재생불량성 빈혈 유형)의 L1 판정은 광범위한 이식 집단을 대상으로 한 Phase 3 시험에 근거하므로, 해당 질환에 대한 직접 근거로 보기는 어렵습니다. 순위 8~10번은 기전적 근거가 없는 모델 예측일 뿐입니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

