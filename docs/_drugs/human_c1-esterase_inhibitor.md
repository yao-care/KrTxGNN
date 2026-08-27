---
layout: default
title: Human C1-Esterase Inhibitor
parent: 僅模型預測 (L5)
nav_order: 297
evidence_level: L5
indication_count: 4
---

# Human C1-Esterase Inhibitor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Human C1-Esterase Inhibitor: 적응증 미상에서 중증 비증식성 당뇨병성 망막병증으로

## 한 문장 요약

Human C1-Esterase Inhibitor(DrugBank ID: DB06404)는 대만에서 아직 허가되지 않은 미시판 약물로, 확보된 원 적응증 및 작용기전 데이터가 없습니다. TxGNN 모델은 **중증 비증식성 당뇨병성 망막병증(Severe Nonproliferative Diabetic Retinopathy)**에 효과가 있을 수 있다고 예측하며(예측 점수 99.61%), 현재 이 특정 적응증을 직접 지지하는 임상시험이나 문헌은 전혀 없어 모델 예측 단계(L5)에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (대만 미허가, 원 적응증 정보 미확보) |
| 예측 신규 적응증 | 중증 비증식성 당뇨병성 망막병증 (Severe Nonproliferative Diabetic Retinopathy) |
| TxGNN 예측 점수 | 99.61% (전체 후보 중 순위 7,146위) |
| 근거 수준 | L5 (모델 예측만 존재, 실제 연구 없음) |
| 대만 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용기전(MOA) 데이터가 없습니다. 또한 이 약물의 원 적응증 정보도 확보되어 있지 않아, 기존 적응증과의 연관성을 근거로 기전상 타당성을 설명하기 어렵습니다.

Evidence Pack에 기록된 예측 근거(rationale)에 따르면, 이 예측은 "일반적인 당뇨병성 망막병증(DR)이 공유하는 보체(complement) 매개 염증 기전"이라는 이론적 가설에 기반합니다. C1-Esterase Inhibitor는 고전적 보체 경로(C1r/C1s)를 억제하는 천연 단백질로, 이론적으로는 망막 미세혈관의 보체 매개 염증 손상을 줄일 가능성이 제기될 수 있습니다.

다만 이번 예측 대상은 DR 중에서도 "중증 비증식성(severe NPDR)"이라는 특정 중증도 단계이며, 이 단계에 특화된 직접적인 문헌이나 시험 자료는 전혀 없습니다. 참고로 같은 Evidence Pack 내 더 넓은 범주인 "당뇨병성 망막병증(전체)"에 대해서는 보체 경로 유전자(SERPING1, C5)와 DR 위험도의 연관성을 보고한 유전학 연구(PMID 26989329)가 1건 확인되지만, 이는 질병 기전에 대한 간접적 유전학적 관찰일 뿐, 본 약물을 이용한 중재 연구가 아니며 severe NPDR에 국한된 근거도 아닙니다. 따라서 이번 예측은 TxGNN의 지식 그래프 유사성 기반 추론(점수 0.996)에 전적으로 의존하며, 임상적 타당성은 아직 검증되지 않았습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 대만 시판 정보

이 약물은 대만에서 허가된 제품이 없습니다 (미시판, 허가증 0건).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
이 예측은 TxGNN 모델의 지식 그래프 유사성 추론에만 기반하며, 예측 대상인 중증 비증식성 당뇨병성 망막병증에 특화된 임상시험이나 문헌이 전혀 없어 근거 수준이 최저 단계(L5)입니다. 또한 이 약물은 대만에서 미시판 상태이고, 원 적응증·작용기전·안전성 정보가 모두 확보되지 않아 가설 검증 이전 단계에 머물러 있습니다.

**진행하려면 필요한 것:**
- TFDA(또는 원 허가국) 허가사항의 경고·금기 정보 확보 (Blocking 등급 데이터 갭)
- DrugBank 등에서 작용기전(MOA) 상세 정보 확보 (High 등급 데이터 갭)
- severe NPDR에 특화된 전임상 또는 초기 임상 근거 확보 (현재 0건)
- 관련 상위 범주인 당뇨병성 망막병증(PMID 26989329)에 대한 심층 검토를 통해 보체 매개 기전 가설의 타당성 보강
- 원 적응증 정보 확보 후 기존 적응증-신규 적응증 간 연관성 재평가
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

