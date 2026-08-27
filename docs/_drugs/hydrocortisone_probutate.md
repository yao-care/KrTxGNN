---
layout: default
title: Hydrocortisone Probutate
parent: 僅模型預測 (L5)
nav_order: 301
evidence_level: L5
indication_count: 1
---

# Hydrocortisone Probutate
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

# Hydrocortisone Probutate: 적응증 미상(자료 없음)에서 홍채 질환(Iris Disease)으로

## 한 문장 요약

Hydrocortisone Probutate(DrugBank ID: DB14543)는 한국에 허가된 제품이 없어 원래 어떤 질환에 사용되었는지 확인할 수 있는 자료가 없습니다.
TxGNN 모델은 **홍채 질환(Iris Disease)**에 효과가 있을 수 있다고 예측하며 예측 점수는 **99.13%**로 높지만, 이를 뒷받침하는 실제 근거는 관련성이 낮게 평가된 **임상시험 1건**(등급 C)뿐이며 지지 문헌은 없어 실질적인 근거 수준은 낮습니다(L4).

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 자료 없음 (한국 미허가, DrugBank 원 적응증 정보 미확인) |
| 예측 신규 적응증 | 홍채 질환 (Iris Disease) |
| TxGNN 예측 점수 | 99.13% (전체 순위 12,934위) |
| 근거 수준 | L4 |
| 한국 시판 현황 | 미상 시판 (허가 제품 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 Hydrocortisone Probutate의 상세 작용 기전(MOA) 데이터는 확보되어 있지 않습니다(Data Gap). 다만 약물명(hydrocortisone 계열, butyrate 에스터화 형태)으로 미루어 코르티코스테로이드(glucocorticoid) 계열 약물로 추정되며, 이 계열은 임상적으로 다양한 안(眼) 염증 질환(전방포도막염/홍채염 등)에 국소 사용되는 것이 일반적으로 알려져 있어 홍채 질환과의 이론적 연관성은 존재합니다.

그러나 이번 예측을 뒷받침하는 유일한 임상시험은 대상 질환이 "만성 건성안(chronic dry eye disease)"으로, 예측 대상인 "홍채 질환"과는 해부학적 부위(눈 표면 vs. 포도막/홍채)와 병리 기전이 다릅니다. 이는 TxGNN의 적응증 용어 매핑 과정에서 발생한 오분류일 가능성이 있습니다. 또한 해당 시험에 사용된 약물은 hydrocortisone 0.335%(Softacort®) 제제로, 예측 대상인 hydrocortisone probutate 본체와는 다른 에스터 형태이기 때문에 "동일 계열 스테로이드의 안구 국소 안전성"에 대한 간접적 방증 정도로만 볼 수 있으며, 약물 특이적인 직접 근거로 보기는 어렵습니다.

종합하면, 이번 예측은 코르티코스테로이드 계열 전체 수준의 약리학적 개연성은 있으나, 약물 특이성 및 질환 특이성 측면에서 직접 근거가 부족한 상태입니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03907865](https://clinicaltrials.gov/study/NCT03907865) | Phase 4 | 완료 | 60 | 만성 건성안 및 안구 표면 염증 환자에서 국소 Hydrocortisone 0.335%(Softacort®)의 임상 효능 평가. **주의**: 대상 질환이 예측 적응증(홍채 질환)과 불일치하며, 사용 약물도 probutate 에스터가 아닌 다른 제형이라 간접 근거로만 참고 가능(관련성 등급 C) |

*※ 위 시험 외 ICTRP 등록 시험은 없습니다.*

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 한국 시판 정보

현재 한국에 허가된 Hydrocortisone Probutate 제품이 없습니다 (허가증 0건, 미상 시판).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

*(주요 경고, 금기, 약물상호작용 자료가 모두 확보되지 않았습니다.)*

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
현재 근거 수준은 L4로, 지지 근거가 대상 질환과 약물 형태가 모두 불일치하는 임상시험 1건에 불과하며 이는 TxGNN 적응증 매핑 오류일 가능성이 있습니다. 여기에 더해 한국 허가 정보, 작용 기전(MOA), 안전성 자료(경고·금기·DDI)가 모두 확보되지 않아 안전성 초기 평가(S1) 단계로도 진입할 수 없는 상태(Blocking data gap)입니다.

**진행하려면 필요한 것:**
- 한국 규제기관(식약처) 허가 자료 및 사용상 주의사항(경고·금기) 확보 — 현재 Blocking 등급 데이터 갭
- DrugBank API를 통한 작용 기전(MOA) 확인 — High 등급 데이터 갭
- NCT03907865와 "홍채 질환" 간 연관성이 실제 적합한 매핑인지, 혹은 TxGNN 용어 매핑 오류인지 수동 재검토
- Hydrocortisone Probutate 본체에 특이적인 추가 임상시험·문헌·ICTRP 자료 수집
- 약물상호작용(DDI) 및 금기 정보 확보
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

