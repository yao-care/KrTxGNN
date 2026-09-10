---
layout: default
title: Fluconazole
parent: 僅模型預測 (L5)
nav_order: 327
evidence_level: L5
indication_count: 1
---

# Fluconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Fluconazole: 기존 적응증 정보 없음 → 점상 상피 각결막염(Punctate Epithelial Keratoconjunctivitis) 예측

## 한 문장 요약

Fluconazole(DrugBank ID: DB00196)은 국내 허가 자료와 원 적응증 정보가 확보되지 않아 기존 치료 용도를 확인할 수 없습니다.
TxGNN 모델은 **점상 상피 각결막염(Punctate Epithelial Keratoconjunctivitis)**에 효과가 있을 수 있다고 예측했으나(예측 점수 99.24%),
이를 뒷받침하는 임상시험이나 문헌은 현재 **0건**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 자료 없음 |
| 예측 신규 적응증 | 점상 상피 각결막염 (Punctate Epithelial Keratoconjunctivitis) |
| TxGNN 예측 점수 | 99.24% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 없습니다. 다만 fluconazole은 트리아졸(triazole)계 항진균제로 널리 알려져 있으며,
진균의 CYP51(lanosterol 14α-demethylase)을 억제해 ergosterol 합성을 차단하고 진균 세포막을 파괴하는 기전으로 작용합니다.

점상 상피 각결막염은 대부분 바이러스(아데노바이러스, HSV) 또는 건조안 관련 상피 손상이 원인이며, 진균성 각막염에서만 드물게
초기 점상 병변 형태로 나타납니다. 병인이 진균성으로 명확히 한정되지 않는 한, fluconazole의 작용 기전과 이 적응증 사이의
연관성은 간접적·비특이적 수준에 머무릅니다. TxGNN 점수(99.24%)는 지식그래프 상의 관계 예측일 뿐 병인 수준의 기전 증거를
제공하지 않으며, 원 적응증(original_indications) 및 MOA 데이터 공백으로 인해 이 예측을 교차 검증할 근거도 부족합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

국내 허가 정보가 없습니다 (미출시, 허가증 0건).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 점수는 높으나(99.24%) 이를 뒷받침하는 임상시험·문헌 근거가 전혀 없고(근거 수준 L5), 기전적 연관성도
병인 특이성이 부족해 간접적 수준에 그칩니다. 또한 허가사항 경고·금기 정보(DG001, Blocking)가 확보되지 않아
안전성 초기평가(S1) 단계 진입 자체가 불가능합니다.

**진행하려면 필요한 것:**
- 식약처 허가 자료 기반 경고사항·금기·상호작용 정보 확보 (DG001)
- DrugBank API를 통한 상세 작용 기전(MOA) 확보 (DG002)
- 진균성 각막염 한정 여부를 포함한 추가 임상시험·문헌 검색
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

