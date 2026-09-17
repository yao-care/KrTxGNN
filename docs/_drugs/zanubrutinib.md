---
layout: default
title: Zanubrutinib
parent: 모델 예측만 (L5)
nav_order: 727
evidence_level: L5
indication_count: 6
---

# Zanubrutinib
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **6** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 약사 평가 보고서

</div>

# Zanubrutinib: B세포 혈액암(CLL/SLL)에서 골수성 백혈병으로

## 한 문장 요약

Zanubrutinib은 BTK(Bruton's tyrosine kinase) 억제제로, 근거 팩 내 문헌에 따르면 만성 림프구성 백혈병/소림프구성 림프종(CLL/SLL) 치료에 주로 사용되어 왔습니다(한국 공식 허가 정보는 확인되지 않음). TxGNN 모델은 **골수성 백혈병(Myeloid Leukemia)**에도 효과가 있을 수 있다고 예측(점수 99.65%)하지만, 관련 임상시험 2건은 모두 Zanubrutinib이 아닌 다른 약물을 시험한 것이고 문헌 9편도 대부분 CLL/SLL에 관한 것으로, 이 예측을 직접 지지하는 근거는 현재 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 미허가 (문헌 근거상 만성 림프구성 백혈병/소림프구성 림프종[CLL/SLL] 치료에 사용) |
| 예측 신규 적응증 | 골수성 백혈병 (Myeloid Leukemia) |
| TxGNN 예측 점수 | 99.65% |
| 근거 수준 | L5 (모델 예측만 존재, 해당 적응증에 특이적인 임상/문헌 근거 없음) |
| 한국 시판 현황 | 미상 (미시판) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

공식 DrugBank MOA 데이터는 확보되지 않았습니다(Data Gap). 다만 근거 팩 내 기전 분석에 따르면 Zanubrutinib은 BTK 억제제로 B세포 수용체(BCR) 신호전달경로를 표적으로 하며, 생리적 발현이 B림프구계 세포에 집중되어 있습니다.

반면 골수성 백혈병(AML/CML)의 주요 드라이버는 FLT3, BCR-ABL, KIT 등이며, BTK 신호경로와의 중첩은 제한적입니다. 근거 팩의 기전 분석도 동일하게 지적하고 있습니다: *"TxGNN 고점수는 지식그래프 상 kinase inhibitor 계열 구조적 유사성을 반영한 결과일 가능성이 있으며, 직접적인 생물학적 증거가 아니다."*

즉, 이 예측은 기전상 개연성이 약하며 현재로서는 실제 생물학적 근거보다는 약물 클래스 유사성에 기반한 모델 아티팩트일 가능성을 배제할 수 없습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04477291](https://clinicaltrials.gov/study/NCT04477291) | Phase 1 | 종료(TERMINATED) | 45 | CG-806(luxeptinib, 다른 pan-FLT3/BTK 억제제)의 재발·불응 AML/고위험 MDS 안전성·항종양 활성 평가. **Zanubrutinib 직접 근거 아님** (관련도 C등급) |
| [NCT05665530](https://clinicaltrials.gov/study/NCT05665530) | Phase 1 | 완료 | 86 | PRT2527(CDK9 억제제) 단독 및 Zanubrutinib/Venetoclax 병용 혈액암 시험. Zanubrutinib은 병용 약제 중 하나일 뿐, 골수성 백혈병 특이적 근거 아님 (관련도 C등급) |

⚠ 두 시험 모두 Zanubrutinib 자체를 골수성 백혈병에 시험한 것이 아니며, 관련도 등급 C(약함)로 평가되었습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [39647999](https://pubmed.ncbi.nlm.nih.gov/39647999/) | 2025 | RCT | J Clin Oncol | SEQUOIA 시험 5년 추적: 치료 경험 없는 CLL/SLL에서 Zanubrutinib vs BR — **CLL/SLL 대상, 골수성 백혈병 아님** |
| [40334067](https://pubmed.ncbi.nlm.nih.gov/40334067/) | 2025 | Cohort | Blood Advances | Ibrutinib/Acalabrutinib 불내성 CLL/SLL 환자에서 Zanubrutinib 내약성·유효성 |
| [40829104](https://pubmed.ncbi.nlm.nih.gov/40829104/) | 2026 | Cohort/Review | Blood Advances | del(17p)/TP53 변이 CLL/SLL에서 Zanubrutinib 효능·안전성 (SEQUOIA, ALPINE 통합분석) |
| [36400069](https://pubmed.ncbi.nlm.nih.gov/36400069/) | 2023 | Cohort | Lancet Haematol | BTK 억제제 불내성 B세포 혈액암에서 Zanubrutinib 단일군 Phase 2 시험 |
| [34959482](https://pubmed.ncbi.nlm.nih.gov/34959482/) | 2021 | Review | Pharmaceutics | 만성 백혈병(CML/CLL)에서 TKI 치료 개관 — 배경 리뷰, 직접 근거 아님 |
| [36402930](https://pubmed.ncbi.nlm.nih.gov/36402930/) | 2023 | Review | Leukemia | Waldenström 거대글로불린혈증에서 BTK 억제제 관리 |
| [37150651](https://pubmed.ncbi.nlm.nih.gov/37150651/) | 2023 | Review | Clin Lymphoma Myeloma Leuk | BTK 억제제 투여 환자의 B형간염 재활성화 |
| [36325357](https://pubmed.ncbi.nlm.nih.gov/36325357/) | 2022 | Case Report | Front Immunol | WM과 B-ALL 동반 증례 |
| [38288815](https://pubmed.ncbi.nlm.nih.gov/38288815/) | 2024 | Review(화학합성) | Anti-cancer Agents Med Chem | FDA 승인 항암제 합성법 개관 — Zanubrutinib 화학구조만 언급, 임상 근거 아님 |

⚠ 9편 중 골수성 백혈병(AML/CML)을 직접 다룬 문헌은 없습니다. 대부분 CLL/SLL 또는 다른 B세포 질환에 관한 것이며, 골수성 백혈병 관련성은 아직 "pending"(미평가) 상태입니다.

## 한국 시판 정보

한국 내 Zanubrutinib 허가 제품이 없습니다 (미시판, 허가증 0건).

## 세포독성 (항종양약에만 해당)

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (BTK 억제제 계열) — 전통적 세포독성 화학요법과 구분됨 |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 점수는 높지만(99.65%), 관련 임상시험 2건은 모두 Zanubrutinib이 아닌 다른 약물을 대상으로 하며, 문헌 9편도 대부분 골수성 백혈병이 아닌 CLL/SLL에 관한 것입니다. 기전상으로도 BTK 신호경로와 골수성 백혈병의 주요 드라이버(FLT3, BCR-ABL, KIT) 간 연결성이 약해, 이 예측은 실제 생물학적 근거보다 약물 클래스 구조 유사성에 기인한 모델 아티팩트일 가능성이 있습니다. 또한 한국 미시판 상태로 처방정보(경고·금기)가 전무하여 초기 안전성 평가(S1) 단계조차 진행할 수 없습니다.

**진행하려면 필요한 것:**
- TFDA 처방정보(경고/금기사항) 확보 — **Blocking**, S1 안전성 초평 필수 선행조건
- DrugBank를 통한 상세 작용기전(MOA) 확인 — High priority
- 골수성 백혈병에 특이적인 전임상 또는 실제 임상 데이터 확보
- 한국 내 허가 신청·시판 현황 지속 모니터링
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

