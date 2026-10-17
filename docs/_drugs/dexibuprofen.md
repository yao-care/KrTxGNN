---
layout: default
title: Dexibuprofen
parent: 모델 예측만 (L5)
nav_order: 270
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Dexibuprofen: 예측 신규 적응증 골관절염 감수성 (Osteoarthritis Susceptibility) (근거 수준 L5). 기존 적응증: 만성 다발성 관절염, 류마티스관절염, 관절증, 강직척추염, 외상 및 수술 후 통증성 부종 또는 염증…"
monitor_inn: "Dexibuprofen"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia"]
---

# Dexibuprofen
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

# Dexibuprofen: 만성 다발성 관절염·류마티스관절염 등에서 골관절염 감수성(Osteoarthritis Susceptibility)으로

## 한 문장 요약

Dexibuprofen은 S(+)-ibuprofen 단일 성분 소염진통제로, 한국에서 만성 다발성 관절염, 류마티스관절염, 관절증, 강직척추염 등의 치료와 급성 상기도 감염 시 해열에 사용되어 왔습니다.
TxGNN 모델은 **골관절염 감수성(Osteoarthritis Susceptibility)**에 효과가 있을 것으로 최상위 예측했지만, 이 질환 항목에 대한 **임상시험은 0건, 문헌은 0편**이라 근거는 모델 예측 수준(L5)에 머뭅니다.
다만 같은 관절 질환인 일반 **골관절염(Osteoarthritis)**에는 임상시험 2건과 문헌 10편이 있습니다. 이 적응증은 이미 허가 범위(관절증)와 겹치므로 신규 재창출로 보기는 어렵습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 만성 다발성 관절염, 류마티스관절염, 관절증, 강직척추염, 외상 및 수술 후 통증성 부종 또는 염증, 염증·통증·발열을 수반하는 감염증의 치료보조 |
| 예측 신규 적응증 | 골관절염 감수성 (Osteoarthritis Susceptibility) |
| TxGNN 예측 점수 | 99.95% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Dexibuprofen은 ibuprofen의 활성 거울상이성질체(S(+)-ibuprofen)인 NSAID입니다. COX-1/COX-2를 억제해 프로스타글란딘 매개 염증과 통증을 줄이는 것으로 알려져 있습니다. 관절염 계열 질환에서 효능이 입증되어 있어, 기전상 관절 질환의 증상 완화에는 적용 가능할 수 있습니다.

그러나 "골관절염 감수성"은 치료 가능한 임상 질환이 아니라 유전적 소인 개념입니다. Dexibuprofen은 증상성 골관절염의 통증과 염증을 완화할 수는 있어도 감수성 자체를 치료하지는 못합니다. 따라서 이 예측은 질환 노드(골관절염)와 그래프상 가까워서 생긴 결과일 가능성이 높습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 참고: 근거가 있는 인접 예측 후보

상위 10개 예측 중 근거가 확인되는 항목은 아래 두 가지이며, 모두 기존 허가 적응증과 겹칩니다.

### 골관절염 (Osteoarthritis, TxGNN 99.87%)

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01066676](https://clinicaltrials.gov/study/NCT01066676) | Phase 4 | 완료 | 482 | 고관절·슬관절 골관절염에서 Dexibuprofen 400 mg 현탁용 산제와 Ibuprofen 400 mg의 안전성·내약성·효능 비교 |
| [NCT01638962](https://clinicaltrials.gov/study/NCT01638962) | 해당 없음 | 완료 | 93 | 무릎 골관절염에서 진통제 사용 교육과 신경근 운동의 관절 하중 비교 (약물은 직접 중재 아님, 간접 관련) |

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [24740137](https://pubmed.ncbi.nlm.nih.gov/24740137/) | 2014 | RCT | Wiener klinische Wochenschrift | 고관절·슬관절 골관절염 489명에서 Dexibuprofen과 Ibuprofen의 안전성·내약성 비열등성 비교 |
| [12708604](https://pubmed.ncbi.nlm.nih.gov/12708604/) | 2003 | RCT | Int J Clin Pharmacol Ther | 고관절 골관절염에서 Dexibuprofen과 celecoxib의 효능·내약성 비교 |
| [11771571](https://pubmed.ncbi.nlm.nih.gov/11771571/) | 2001 | RCT | Clin Rheumatol | 고관절 골관절염 178명에서 Dexibuprofen과 2배 용량 ibuprofen의 동등 효능 및 용량-반응 확인, 1년 내약성 연구 포함 |
| [10667832](https://pubmed.ncbi.nlm.nih.gov/10667832/) | 2000 | RCT | Int J Clin Pharmacol Ther | WOMAC 지표로 Dexibuprofen의 용량-반응 관계와 racemic ibuprofen 대비 효능 평가 |
| [9123945](https://pubmed.ncbi.nlm.nih.gov/9123945/) | 1997 | RCT | Wiener klinische Wochenschrift | 슬관절 골관절염 110명에서 Dexibuprofen 900 mg과 diclofenac 150 mg의 동등 효능 확인 |
| [11771569](https://pubmed.ncbi.nlm.nih.gov/11771569/) | 2001 | Review | Clin Rheumatol | Dexibuprofen 임상 자료 개관 (8건 임상시험, 1,463명) |

데이터상 이 항목의 근거 수준은 L1이고 권장 결정은 Proceed with Guardrails입니다. 다만 Phase 3 완료 RCT 2건 이상이라는 판정은 이중맹검 비교 연구의 제목에서 추정한 것이므로 원문 확인이 필요합니다. 등록된 임상시험은 Phase 4입니다.

### 류마티스관절염 (Rheumatoid Arthritis, TxGNN 99.92%)

이미 한국 허가 적응증(만성 다발성 관절염, 류마티스관절염)에 포함되어 있어 신규 재창출 후보가 아닙니다. 확인된 문헌은 전반적 개관, 과거 연구 재평가, 제형 연구뿐이며 류마티스관절염 전용 RCT는 확인되지 않습니다. 근거 수준은 L4, 권장 결정은 Hold입니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200512203 | 솔루펜연질캡슐 | 연질캡슐 | 만성 다발성 관절염, 류마티스관절염, 관절증, 강직척추염, 외상 및 수술 후 통증성 부종 또는 염증, 염증, 통증 및 발열을 수반하는... |
| 200100960 | 펜타우드정 | 필름코팅정 | 만성 다발성관절염, 류마티스관절염, 관절증, 강직척추염, 외상 및 수술 후 통증성 부종 또는 염증 그리고 염증, 통증 및 발열을 수반하는... |
| 201903568 | 독립덱시부펜시럽 | 시럽제 | 급성 상기도 감염으로 인한 발열 시 해열 |
| 202401446 | 펜다나프로연질캡슐 | 연질캡슐 | 만성 다발성 관절염, 류마티스 관절염, 관절증, 강직척추염 / 외상 및 수술 후 통증성 부종 또는 염증 및 염증, 통증, 발열을 수반하는... |
| 201308922 | 에스부펜정 | 필름코팅정 | 만성 다발성 관절염, 류마티스관절염, 관절증, 강직척추염, 외상 및 수술 후 통증성 부종 또는 염증 그리고 염증, 통증 및 발열을 수반하는... |

전체 20건이 모두 유효한 단일제 허가입니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
1순위 예측인 "골관절염 감수성"은 치료 가능한 질환이 아닌 유전적 소인 개념이고, 임상시험과 문헌이 없는 모델 예측(L5)일 뿐입니다. 근거가 있는 골관절염과 류마티스관절염은 이미 허가 범위와 겹쳐 신규 재창출로 보기 어렵습니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기) 확인: 안전성 선별 단계로 넘어가기 위한 필수 데이터
- 작용 기전(MOA) 데이터 확보
- 골관절염 항목의 L1 판정 검증: Phase 3 RCT 여부를 원문에서 확인
- 실제 치료 대상이 될 수 있는 임상적 적응증으로 후보 재정의 (감수성 개념 제외)
- 골관절염 방향으로 진행할 경우 NSAID 공통 심혈관·위장관·신장 주의사항을 반영한 가드레일 마련
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

