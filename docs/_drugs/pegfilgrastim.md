---
layout: default
title: Pegfilgrastim
parent: 모델 예측만 (L5)
nav_order: 582
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Pegfilgrastim: 예측 신규 적응증 중증 비증식성 당뇨망막병증 (severe nonproliferative diabetic retinopathy) (근거 수준 L5). 기존 적응증: 허가 적응증 본문 확인 불가 (허가증에는 문서 링크만 있음)"
monitor_inn: "PEGFILGRASTIM"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy"]
---

# Pegfilgrastim
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **2** 건
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

# Pegfilgrastim: 허가 적응증 확인 필요에서 중증 비증식성 당뇨망막병증으로

## 한 문장 요약

Pegfilgrastim은 장기 지속형 G-CSF(과립구 집락자극인자) 제제로 한국에서 시판 중이지만, 허가 적응증 본문은 이번에 정리된 데이터에서 확인되지 않았습니다.
TxGNN 모델은 **중증 비증식성 당뇨망막병증(severe nonproliferative diabetic retinopathy)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 **임상시험과 문헌은 0건**으로 모델 예측만 존재하는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문 확인 불가 (허가증에는 문서 링크만 있음) |
| 예측 신규 적응증 | 중증 비증식성 당뇨망막병증 (severe nonproliferative diabetic retinopathy) |
| TxGNN 예측 점수 | 99.89% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Pegfilgrastim은 호중구 생성을 촉진하는 장기 지속형 G-CSF이며, 조혈 전구세포와 내피 전구세포를 동원하는 것으로 알려져 있습니다.

이 특성에서 망막 혈관 회복과의 연관성을 가설로 세울 수 있습니다. 그러나 이번 데이터에서는 이를 뒷받침하는 근거가 없습니다. 반대로 G-CSF가 유발하는 염증과 신생혈관 형성이 망막 병변을 악화시킬 수도 있어 효과의 방향 자체가 불확실합니다. 따라서 이 연관성은 추측 단계이며 전임상 및 기전 연구를 통한 검증이 필요합니다.

참고로 상위 범주인 **당뇨망막병증(diabetic retinopathy)**도 점수 99.73%로 함께 예측되었습니다. 두 예측은 포괄 관계이므로 독립된 근거로 볼 수 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202400068 | 싸이쎄그프리필드시린지주6mg/0.6mL (싸이젠코리아) | 프리필드시린지 주사제 | 본문 미확인 (허가사항 문서 참조) |
| 201203772 | 뉴라스타프리필드시린지주 (한국쿄와기린) | 프리필드시린지 주사제 | 본문 미확인 (허가사항 문서 참조) |

## 안전성 고려사항

- **약물 상호작용**: 상호작용 조회 결과 총 100건이 확인되었으며, 이 중 일부 상세 항목은 모두 중등도(Moderate)입니다. 주요 항목은 다음과 같습니다.
  - 항암제 및 세포독성 약물: Paclitaxel, Mercaptopurine, Azacitidine, Arsenic trioxide, Altretamine, Trimetrexate, Abemaciclib
  - 면역·항체 치료제: Alemtuzumab, Aldesleukin, Belantamab mafodotin, Asparaginase
  - 방사성 의약품: Iobenguane (I-131), Tositumomab (I-131), Ibritumomab tiuxetan, Fludeoxyglucose (18F)
  - 기타: Pegvaliase, Levamisole, Acalabrutinib, Avapritinib

주요 경고와 금기는 이번 데이터에서 확인되지 않았으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 매우 높지만 임상시험과 문헌 근거가 전혀 없는 L5 단계입니다. 작용 기전 데이터와 허가 경고·금기 정보도 확보되지 않았고, G-CSF가 망막 병변을 악화시킬 가능성도 배제할 수 없어 현 시점에서 진행하기는 어렵습니다.

**진행하려면 필요한 것:**
- 식약처(MFDS) 허가사항 문서에서 적응증, 경고, 금기 정보 확보
- DrugBank 등에서 작용 기전(MOA) 데이터 확보
- 당뇨망막병증 모델에서 G-CSF의 효과와 병적 신생혈관 형성 위험을 평가하는 전임상·기전 연구
- 관련 임상시험 및 문헌 재검색
- 투여 경로 적합성 평가 (이번 데이터에서는 미확인)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

