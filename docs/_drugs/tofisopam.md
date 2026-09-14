---
layout: default
title: Tofisopam
parent: 僅模型預測 (L5)
nav_order: 683
evidence_level: L5
indication_count: 1
---

# Tofisopam
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

# Tofisopam: 항불안에서 불면증으로

## 한 문장 요약

Tofisopam은 2,3-benzodiazepine 계열의 비정형 항불안제로, 전통적인 BZD와 달리 진정/수면/근육이완 작용이 없는 것이 특징입니다. TxGNN 모델은 **불면증(Insomnia)**에 효과가 있을 수 있다고 예측했으나(점수 99.16%), 이를 지지하는 임상시험이나 문헌은 현재 **전혀 없으며**, 오히려 약물의 알려진 약리 기전은 이 예측 방향과 상충됩니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 항불안 (2,3-benzodiazepine 계열 비정형 항불안제, 국내 미허가) |
| 예측 신규 적응증 | 불면증 (Insomnia) |
| TxGNN 예측 점수 | 99.16% |
| 근거 수준 | L5 (모델 예측만, 실제 연구 없음) |
| 한국 시판 현황 | 미출시 (未上市) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

DrugBank에 등록된 상세 MOA 데이터는 없습니다([Data Gap], DG002). 다만 알려진 약리 정보에 따르면, Tofisopam은 GABA-A 수용체에 작용하지만 diazepam 등 전통적 1,4-benzodiazepine과는 결합 부위가 다른 2,3-benzodiazepine 유도체입니다. 임상적으로는 진정/수면/근육이완/항경련 작용이 없다는 점이 다른 BZD와의 차별점으로 명시되어 있으며, 주간 항불안제로 사용됩니다.

이 때문에 TxGNN이 산출한 높은 예측 점수(0.99)는 GABA-A 경로에 대한 지식그래프 구조적 유사성에서 기인했을 가능성이 크고, 실제 불면증에 대한 약리학적 방향성과는 반대될 수 있습니다. 즉 기전상 근거가 아니라 계산상 유사성에 의한 예측으로 해석해야 하며, 실제 임상적 타당성은 현재 근거로 뒷받침되지 않습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (TFDA 원개발국 허가사항/경고 정보 확보가 차단 항목(DG001)으로 남아 있어, 국내 허가사항도 존재하지 않습니다.)

## 결론 및 다음 단계

**결정: Hold**

**사유:**
이 예측은 모델 계산에만 근거한 L5 수준으로, 지지하는 임상시험이나 문헌이 전혀 없습니다. 오히려 Tofisopam의 알려진 비진정성 항불안 기전은 불면증 적응증과 방향이 상충되며, 한국 내 시판 허가도 없고 안전성 정보(TFDA 경고/금기)조차 확보되지 않은 차단(Blocking) 상태입니다.

**진행하려면 필요한 것:**
- TFDA 원개발국 仿單(경고·금기 사항) 확보 — S1 안전성 초평가 진입 필수 (DG001)
- DrugBank/문헌을 통한 상세 MOA 확인 (DG002)
- GABA-A 결합 부위 차이에 따른 기전 방향성 재검토
- 불면증 관련 임상시험/문헌 근거 축적 여부 지속 모니터링
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

