---
layout: default
title: Triflusal
parent: 僅模型預測 (L5)
nav_order: 704
evidence_level: L5
indication_count: 5
---

# Triflusal
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Triflusal: 항혈소판제(추정)에서 Factor V 과잉 자발성 혈전증으로

## 한 문장 요약

> Triflusal(DrugBank DB08814)은 예측 근거 자료에 따르면 혈소판 COX-1/포스포디에스터라제를 억제하는 항혈소판제로 추정되나, 정확한 기존 적응증과 작용기전(MOA) 데이터는 등록되어 있지 않습니다.
> TxGNN 모델은 **Factor V 과잉으로 인한 자발성 혈전증(Factor 5 Excess with Spontaneous Thrombosis)**에 효과가 있을 수 있다고 예측하지만,
> 이를 뒷받침하는 **임상시험이나 문헌은 현재 전혀 없으며**, 기전상으로도 정합성이 낮다는 평가가 함께 제시되어 있습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (원 적응증 데이터 미등록) |
| 예측 신규 적응증 | Factor V 과잉 자발성 혈전증 (Factor 5 Excess with Spontaneous Thrombosis) |
| TxGNN 예측 점수 | 99.60% (rank 7297) |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 DrugBank 기준 상세 작용기전(MOA) 데이터는 "[Data Gap]"으로 등록되어 있어 공식적으로 확인되지 않습니다. 다만 예측 근거(rationale) 자료에 따르면 Triflusal은 혈소판 COX-1 및 포스포디에스터라제를 억제하는 항혈소판제로 알려져 있습니다.

그러나 Factor V 과잉으로 인한 자발성 혈전증은 응고인자 이상에 의한 **정맥 혈전 경향** 질환으로, Triflusal이 작용하는 **동맥 혈소판 활성화 경로**와는 병태생리학적 기전이 다릅니다. 이 질환의 표준 치료는 일반적으로 항응고제이며, 항혈소판제는 기전상 직접 대응하지 않습니다.

근거 자료 자체에서도 "TxGNN이 'thrombosis'라는 키워드에 과도하게 연결된 결과일 가능성"이 명시적으로 언급되어 있어, 이 예측은 기전적 타당성이 약한 것으로 평가됩니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 한국 시판 정보

현재 한국에 시판 중인 허가 제품이 없습니다 (허가증 0건, 미출시 상태).

---

## 안전성 고려사항

안전성 정보(주요 경고, 금기, 약물 상호작용)가 등록되어 있지 않으며, 이 약물은 한국에 시판 허가가 없어 참고할 수 있는 국내 허가사항도 없습니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 근거 수준이 L5(모델 예측만 존재, 임상시험·문헌 근거 전무)이며, 기전 정합성도 낮다는 평가가 근거 자료 자체에 명시되어 있습니다.
- 이 약물은 한국 미허가/미출시 상태이고, 작용기전(DG002, High)과 허가사항 경고·금기(DG001, Blocking)가 모두 누락되어 있어 안전성 초기 평가(S1) 단계 진입 자체가 불가능합니다.

**진행하려면 필요한 것:**
- TFDA(현지 허가당국) 원 적응증 및 허가사항(경고/금기) 확보 — Blocking gap 해소 필수
- DrugBank API를 통한 정확한 MOA 데이터 확보
- Factor V 과잉/혈전성향 관련 질환에 대한 임상시험·관찰연구 존재 여부 재조사
- 항혈소판제가 응고인자 매개 혈전증에 미치는 실제 효과에 대한 문헌 검토

**참고:** 동일 Evidence Pack 내 rank 4 후보(thrombophilia, L4)는 약리학적 문헌(PMID 8200721) 1건이 존재해 rank 1보다 상대적으로 근거가 있는 편이나, 여전히 임상 대상군 특이적 증거는 없어 우선순위 판단 시 함께 비교 검토가 필요합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

