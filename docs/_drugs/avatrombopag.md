---
layout: default
title: Avatrombopag
parent: 모델 예측만 (L5)
nav_order: 106
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Avatrombopag: 예측 신규 적응증 거대혈소판감소증… (근거 수준 L5). 기존 적응증: 확인 불가 (허가 적응증이 문서 링크로만 제공되어 구체적 내용을 확인하지 못함)"
monitor_inn: "Avatrombopag"
predicted_indications: ["marcothrombocytopenia with mitral valve insufficiency", "hereditary thrombocytopenia with normal platelets", "transient neonatal thrombocytopenia", "dense granule disease", "amyotrophic lateral sclerosis", "bilateral parasagittal parieto-occipital polymicrogyria", "lower motor neuron syndrome with late-adult onset", "amyotrophic lateral sclerosis, susceptibility to", "Mills syndrome", "monomelic amyotrophy"]
---

# Avatrombopag
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

# Avatrombopag: 만성 간질환 관련 혈소판감소증에서 거대혈소판감소증(승모판 폐쇄부전 동반)으로

## 한 문장 요약

Avatrombopag은 트롬보포이에틴 수용체(c-Mpl) 작용제로, 한국에서 도프텔렛정으로 허가되어 시판 중입니다. TxGNN 모델은 **거대혈소판감소증(승모판 폐쇄부전 동반, marcothrombocytopenia with mitral valve insufficiency)**에 효과가 있을 수 있다고 예측합니다. 다만 현재 이 방향을 지지하는 **임상시험과 문헌은 0건**이며, 모델 예측만 있는 상태입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 적응증이 문서 링크로만 제공되어 구체적 내용을 확인하지 못함) |
| 예측 신규 적응증 | 거대혈소판감소증, 승모판 폐쇄부전 동반 (marcothrombocytopenia with mitral valve insufficiency) |
| TxGNN 예측 점수 | 99.995% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 수집되지 않았습니다. 알려진 정보에 따르면 Avatrombopag은 트롬보포이에틴 수용체(c-Mpl) 작용제로, 거핵구의 증식과 분화를 촉진하여 혈소판 생성을 늘립니다. 따라서 혈소판 수가 감소한 질환에는 기전상 적용 가능성이 있습니다.

다만 유전성 거대혈소판감소증은 거핵구 성숙, 세포골격 유전자, 혈소판 방출 이상 등 원인이 다양해 TPO 수용체 작용제가 효과적일지는 원인에 따라 달라질 수 있습니다. 승모판 폐쇄부전은 구조적 심장 이상이므로 이 약이 개선할 것으로 기대하기 어렵습니다.

높은 TxGNN 점수는 지식그래프상 혈소판감소증 관련 질환과의 근접성을 반영한 것으로, 임상적 근거는 아닙니다.

### 기타 예측 적응증 (참고)

상위 10개 예측 중 나머지도 모두 L5·Hold이며, 임상시험과 문헌이 없습니다.

| 순위 | 예측 질환 | 점수 | 기전 연관성 평가 |
|------|---------|------|--------------|
| 2 | 정상 혈소판을 동반한 유전성 혈소판감소증 | 99.995% | 질환명이 모호하여 연관성이 약하고 불확실함 |
| 3 | 일과성 신생아 혈소판감소증 | 99.995% | 기전상 관련은 있으나 자연 회복되는 질환이며, 신생아 안전성·용량 자료가 없음 |
| 4 | 치밀과립 질환 | 99.995% | 혈소판 수가 아닌 기능 결함이 핵심이라 연관성이 약하고 혈전 위험 고려 필요 |
| 5, 8 | 근위축성 측삭경화증(ALS) 및 ALS 감수성 | 99.993%, 99.991% | 뚜렷한 기전 연결이 없으며 네트워크 기반 인공물로 판단됨 |
| 6 | 양측 시상부 두정-후두엽 다소뇌회증 | 99.992% | 선천성 뇌 피질 기형으로 연관성이 없음 |
| 7 | 성인 후기 발병 하위운동뉴런 증후군 | 99.992% | 운동뉴런질환과의 그래프 유사성에 기인한 것으로 보임 |
| 9 | Mills 증후군 | 99.991% | 기전상 연결이 알려져 있지 않음 |
| 10 | 단지성 근위축증 | 99.990% | 기전상 근거가 없으며 그래프 기반 인공물로 보임 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202402776 | 도프텔렛정20밀리그램 (아바트롬보팍말레산염) | 연한 노란색 양면 볼록 원형 필름코팅정 ("AVA"/"20" 각인) | 허가 적응증 텍스트는 문서 링크로만 제공되어 요약 불가 |

제조·판매사는 (주)한독입니다.

## 안전성 고려사항

허가사항의 경고 및 금기 정보는 이번 보고서 자료에 포함되지 않았습니다. 상세 내용은 허가사항을 참조하세요.

**약물 상호작용**: 총 52건이 확인되었으며, 이 중 주요 항목은 다음과 같습니다.

- **Major (중대)**: Fosphenytoin, Carbamazepine, Carfilzomib, Dabrafenib, Enzalutamide, Fluconazole, Imatinib
- **Moderate (중등도)**: Clarithromycin, Nitisinone, Cobicistat, Fosamprenavir, Gemfibrozil, Fenofibrate, Apalutamide, Atazanavir, Amprenavir, Boceprevir, Ceritinib, Delavirdine, Idelalisib

(위는 확인된 52건 중 일부이며, 전체 목록은 별도 확인이 필요합니다.)

또한 TPO 수용체 작용제 계열이므로 혈전 위험을 고려해야 하며, 신생아 등 소아 대상 안전성·용량 자료는 확립되어 있지 않습니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 매우 높지만 이를 뒷받침하는 임상시험과 문헌이 전혀 없는 L5 단계입니다. 1순위 질환은 승모판 폐쇄부전이라는 구조적 이상이 포함되어 있어 약물이 해결할 수 없는 부분이 있으며, 상위 예측 중 상당수(ALS, 다소뇌회증 등)는 기전상 근거가 없는 그래프 인공물로 보입니다.

**진행하려면 필요한 것:**
- 허가 적응증 및 경고·금기 정보 확보 (허가사항 PDF 내용 확인)
- 상세한 작용 기전 데이터 (DrugBank 등)
- 유전성 혈소판감소증의 원인 유전자별 TPO 수용체 작용제 반응성 검토
- 임상시험 및 문헌 근거 탐색 (현재 0건)
- 혈소판 수 감소가 핵심인 질환(유전성 혈소판감소증 등)을 우선 검증 대상으로 선별하고, ALS 등 기전 근거가 없는 예측은 제외
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

