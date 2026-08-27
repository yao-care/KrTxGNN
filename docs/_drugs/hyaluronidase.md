---
layout: default
title: Hyaluronidase
parent: 僅模型預測 (L5)
nav_order: 298
evidence_level: L5
indication_count: 10
---

# Hyaluronidase
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

이 Evidence Pack은 `predicted_indications` 배열에 10개의 후보 적응증이 담겨 있는데, 프롬프트 규칙상 보고서는 `predicted_indications[0]` (TxGNN 예측 순위 1위)을 기준으로 작성합니다. 아래는 그 규칙에 따른 정식 보고서이며, 마지막에 이 Evidence Pack에서 발견한 특이사항(더 근거가 강한 후보가 별도로 존재함)을 짧게 덧붙였습니다.

---

# Hyaluronidase: 적응증 미상에서 내사시(Esotropia)로

## 한 문장 요약

Hyaluronidase는 한국 내 허가 및 원 적응증 데이터가 확보되어 있지 않은 상태입니다. TxGNN 모델은 **내사시(Esotropia)**에 효과가 있을 것으로 예측했으나(예측 점수 99.89%, 전체 예측 순위 2,875위), 현재까지 이를 뒷받침하는 임상시험과 문헌은 **각각 0건**으로, 근거 수준이 가장 낮은 등급(L5, 모델 예측 단독)에 해당합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (등록된 한국 허가 정보 및 원 적응증 데이터 없음) |
| 예측 신규 적응증 | 내사시 (Esotropia) |
| TxGNN 예측 점수 | 99.89% (전체 예측 순위 2,875위) |
| 근거 수준 | L5 (모델 예측만 존재, 임상시험·문헌 없음) |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 Hyaluronidase의 상세한 작용 기전(MOA) 데이터가 확보되어 있지 않습니다. 또한 한국 내 허가 정보나 기존 적응증 데이터도 존재하지 않아, 이 약물이 원래 어떤 질환에 사용되었는지 근거 자료로 확인할 수 없습니다.

TxGNN 모델은 내사시(Esotropia)에 대해 99.89%의 높은 예측 점수를 부여했지만, 이는 지식그래프 기반 패턴 매칭 결과일 뿐입니다. Evidence Pack에 기록된 기전 분석에 따르면, 내사시는 안구 외 근육의 긴장도 및 신경근 조절 이상에 의한 질환으로, hyaluronidase의 히알루론산(hyaluronic acid) 기질 분해 작용과는 알려진 기전상 연관성이 없습니다. 실제로 관련 임상시험이나 문헌도 전혀 확인되지 않아(0건), 이 예측은 순수하게 모델 점수에만 의존하고 있으며 기전적 타당성을 뒷받침할 근거는 현재 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

현재 한국에 허가된 Hyaluronidase 제품이 없습니다 (미시판, 허가증 0건).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
근거 수준이 L5(모델 예측만 존재)로 가장 낮으며, 임상시험과 문헌이 전무하고 기전적 연관성도 확인되지 않았습니다. 현 단계에서 추가 검토를 진행할 근거가 부족합니다.

**진행하려면 필요한 것:**
- 식약처 허가사항(경고·금기 사항) 확보 — 현재 Blocking 등급 데이터 갭(DG001)으로 안전성 초기 평가(S1) 진입 불가
- DrugBank 등에서 작용기전(MOA) 데이터 확보 (DG002)
- 내사시 관련 전임상 또는 초기 임상 근거 확보 (현재 0건)
- DrugBank ID 등 약물 식별 정보 보완

---

### 참고: Evidence Pack 내 다른 후보 적응증에 대한 안내

이번 Evidence Pack에는 Hyaluronidase에 대해 총 10개의 예측 적응증이 포함되어 있으며, TxGNN 순위 1위인 내사시(위 보고서 주제)는 근거가 전혀 없는 반면, **순위 6위 "당뇨병성 망막병증(Diabetic Retinopathy)"**은 훨씬 강한 근거 수준(L1)을 보유하고 있습니다:

- 완료된 Phase 3 대조시험 2건 (NCT00198497, n=510 / NCT00198510, n=750) — 양 시험 모두 ovine hyaluronidase 제제 "Vitrase"의 유리체내 주사를 통한 유리체 출혈(vitreous hemorrhage) 제거 효능·안전성 평가
- 관련 Phase 2 공개 시험 1건 (NCT00198471, n=10)
- 기전: hyaluronidase가 유리체 내 히알루론산 기질을 분해하여 출혈/혼탁을 제거 — 전신 치료가 아닌 안과적 국소(유리체내) 적응증

이 후보는 근거 수준 기준으로 L1(≥2건의 완료된 Phase 3 RCT)에 해당하여, "Research Question" 단계로 진행할 근거가 충분합니다. 만약 팀에서 근거가 뒷받침되는 재창출 후보를 검토하시려면, 이 항목을 `predicted_indications[0]`으로 지정하여 별도 보고서 생성을 요청해 주세요.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

