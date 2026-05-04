---
layout: default
title: Darolutamide
parent: 僅模型預測 (L5)
nav_order: 196
evidence_level: L5
indication_count: 10
---

# Darolutamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Darolutamide: 전립선암에서 동형접합 가족성 고콜레스테롤혈증으로

## 한 문장 요약

Darolutamide는 안드로겐 수용체(AR) 길항제로, 전립선암 치료에 사용되는 약물입니다.
TxGNN 모델은 **동형접합 가족성 고콜레스테롤혈증(Homozygous Familial Hypercholesterolemia)**에 효과가 있을 수 있다고 예측하나,
이를 지지하는 **임상시험 및 문헌이 전무하며(L5)**, 기전상 타당성 또한 매우 낮아 현 단계에서 진행이 권고되지 않습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 전립선암 (AR 길항제; 한국 허가사항 별도 확인 필요) |
| 예측 신규 적응증 | 동형접합 가족성 고콜레스테롤혈증 (Homozygous Familial Hypercholesterolemia) |
| TxGNN 예측 점수 | 99.11% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, Darolutamide는 **안드로겐 수용체(AR) 길항제**로, 비전이성 거세 저항성 전립선암(nmCRPC) 및 전이성 호르몬 감수성 전립선암(mHSPC) 치료에서의 효능이 입증되어 있습니다.

기전상 추론을 살펴보면, AR 신호 경로는 간세포의 LDL 수용체(LDL-R) 발현 및 콜레스테롤 합성(SREBP 경로)을 조절하는 것으로 알려져 있습니다. 이론적으로는 AR 길항이 LDL-R 발현을 상향 조절하여 혈중 LDL 콜레스테롤 수치를 낮출 수 있다는 가설이 가능합니다.

그러나 **동형접합 가족성 고콜레스테롤혈증(HoFH) 환자는 양쪽 LDL 수용체 유전자가 모두 돌연변이로 기능을 완전히 상실한 상태**입니다. LDL-R 발현량 자체를 증가시켜도 수용체 기능이 없으므로 실질적인 치료 효과를 기대하기 어렵습니다. 이 기전 추론은 HoFH의 근본적인 병태생리와 부합하지 않아 예측의 생물학적 타당성은 매우 낮습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 한국 시판 정보

Darolutamide는 현재 한국에 시판 허가가 없습니다 (허가증 0건, 미시판).

---

## 세포독성

Darolutamide는 전립선암 치료제로, 항종양 약물 분류에 해당합니다. 다만, 전통적 세포독성 화학요법이 아닌 표적치료제(AR 길항제)입니다.

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (안드로겐 수용체 길항제, AR Antagonist) |
| 골수억제 위험 | 저 (AR 길항제는 전통적 골수억제 기전 없음; 허가사항 확인 필요) |
| 구토 유발성 등급 | 저 |
| 모니터링 항목 | 간기능, 심혈관 지표, 피로 및 권태감 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
동형접합 가족성 고콜레스테롤혈증에 대한 임상시험 및 문헌 근거가 전무하며(L5), AR 길항 기전이 LDL 수용체 기능 자체가 소실된 HoFH의 병태생리와 근본적으로 부합하지 않습니다. 안전성·기전 데이터 모두 추가 확인이 필요합니다.

**진행하려면 필요한 것:**
- 상세한 작용 기전 데이터 확보 (DrugBank API 재조회)
- 한국 허가사항 확인 (MFDS 공식 문서; 경고·금기 포함)
- HoFH에서 AR 신호 경로와 콜레스테롤 대사 간 관계를 규명하는 전임상 연구
- 한국 미시판 약물이므로, 규제 전략 및 도입 가능성 사전 검토

---

## 부록: 전체 예측 적응증 요약 (Rank 1–10)

이 보고서는 복합 후보(multi) 평가 결과입니다. 10개 예측 적응증 전체의 현황은 다음과 같습니다.

| 순위 | 적응증 | TxGNN 점수 | 근거 수준 | 임상시험 | 문헌 | 결정 | 비고 |
|------|--------|-----------|----------|----------|------|------|------|
| 1 | Homozygous Familial Hypercholesterolemia | 99.11% | L5 | 0건 | 0편 | Hold | 기전 타당성 극히 낮음 |
| 2 | Multiple Endocrine Neoplasia | 99.06% | L4 | 1건 | 0편 | Hold | 시험 조기 종료, 등록 2명 |
| 3 | HIV Infectious Disease | 99.04% | L5 | 0건 | 0편 | Hold | 간접 기전, 특이 연구 없음 |
| 4 | Feline Acquired Immunodeficiency Syndrome | 98.70% | L5 | 0건 | 0편 | Hold | ⚠️ 동물 질환, 인간 재창출 대상 아님 |
| 5 | Simian Immunodeficiency Virus Infection | 98.70% | L5 | 0건 | 0편 | Hold | ⚠️ 동물 질환, 인간 재창출 대상 아님 |
| 6 | Neurodevelopmental Disorder (ataxic gait, absent speech) | 98.56% | L5 | 0건 | 0편 | Hold | 혈뇌장벽 투과 낮음, 기전 불일치 |
| 7 | Cytomegalovirus Infection | 98.33% | L5 | 0건 | 0편 | Hold | 표준 치료 기전과 상이 |
| 8 | Thrombotic Disease | 98.29% | L4 | 0건 | 1편 | Hold | ⚠️ 문헌이 부작용 보고(부종양 증후군)이며 치료 근거 아님 |
| 9 | Malignant Catarrh | 98.18% | L5 | 0건 | 0편 | Hold | ⚠️ 소 질환(BHV), KG 위양성 가능성 |
| 10 | Infectious Bovine Rhinotracheitis | 98.18% | L5 | 0건 | 0편 | Hold | ⚠️ 소 질환(BoHV-1), KG 위양성 가능성 |

> **종합 평가:** 10개 예측 적응증 중 인간 임상 재창출 가능성이 있는 후보는 **Multiple Endocrine Neoplasia(MEN, rank 2)** 와 **HIV Infectious Disease(rank 3)** 가 기전 합리성 측면에서 상대적으로 높습니다. 다만 모든 후보가 현 단계에서 Hold이며, Darolutamide 고유의 임상적·안전성 데이터 확보가 선행되어야 합니다. Rank 4, 5, 9, 10은 동물 질환으로 인간 약물 재창출 대상에서 제외를 권고합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

