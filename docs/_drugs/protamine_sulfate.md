---
layout: default
title: Protamine Sulfate
parent: 僅模型預測 (L5)
nav_order: 584
evidence_level: L5
indication_count: 10
---

# Protamine Sulfate
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

# Protamine Sulfate: 적응증 정보 없음에서 Severe Intellectual Disability-Progressive Postnatal Microcephaly-Midline Stereotypic Hand Movements Syndrome으로

## 한 문장 요약

Protamine sulfate는 임상적으로 헤파린 중화(항응고 작용 길항) 목적으로 알려진 약물이나, 이번 Evidence Pack에는 기존 승인 적응증·작용기전(MOA) 데이터가 모두 결측되어 있습니다.
TxGNN 모델은 **Severe intellectual disability-progressive postnatal microcephaly-midline stereotypic hand movements syndrome**에 효과가 있을 수 있다고 예측했으나, 예측 점수는 0.5(전체 약 182만 순위)로 유의미한 신호로 보기 어렵고, 이를 지지하는 임상시험이나 문헌은 **한 건도 없습니다**.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 등록된 정보 없음 (원본 적응증 데이터 결측) |
| 예측 신규 적응증 | Severe intellectual disability-progressive postnatal microcephaly-midline stereotypic hand movements syndrome |
| TxGNN 예측 점수 | 50% (순위 1,827,536 / 전체 후보 중) |
| 근거 수준 | L5 (모델 예측만 있음, 실제 연구 없음) |
| 한국 시판 현황 | 미상영업 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 없습니다. Evidence Pack 내 다른 예측 항목(rank 2~10)의 근거 서술을 종합하면, Protamine sulfate는 강한 양전하를 띠는 단백질로 **헤파린과 결합하여 항응고 작용을 중화**하는 약리 특성이 알려져 있으나, 이는 원본 MOA 필드가 아닌 개별 예측 항목의 정성적 서술에서만 확인됩니다.

1위로 예측된 신경발달 증후군(지적장애·소두증·상동 손동작)과 헤파린 중화 기전 사이에는 **생물학적으로 타당한 연결고리가 제시되어 있지 않습니다**. 실제로 해당 예측 항목은 scoring·rationale 필드 자체가 "pending" 상태로 남아 있어, 다른 하위 순위 항목들과 달리 기전적 타당성 검토조차 완료되지 않은 것으로 판단됩니다. 하위 순위 항목들(신생아 피부근염, 신생아 자가면역 용혈성 빈혈, 항인지질증후군 등)도 공통적으로 "무관련 기전, 순수 KG 점수 잡음"으로 평가되어 있어, 이번 예측 세트 전반의 신뢰도가 낮습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 근거 수준이 L5(모델 예측만 존재)이며, TxGNN 예측 점수(50%, 순위 약 182만 위)도 유의미한 신호로 보기 어렵습니다.
- 1위 예측 항목은 기전적 타당성 평가(rationale) 자체가 미완료(pending) 상태이며, 다른 순위 항목들도 모두 "기전적 연관성 없음 → Hold"로 평가되어 있어 예측 세트 전반의 질이 낮습니다.
- MOA(High 등급 결측), TFDA/한국 허가사항 경고·금기 정보(**DG001, Blocking 등급 결측**)가 모두 확보되지 않아 S1 안전성 초기 평가 단계 진입이 원천적으로 불가능합니다.
- 한국 내 시판 이력이 없어(허가증 0건) 실사용 데이터 기반 보완도 어렵습니다.

**진행하려면 필요한 것:**
- DrugBank/TFDA를 통한 작용기전(MOA) 데이터 확보
- TFDA 공식 사이트에서 안전성 경고·금기 정보(DG001) 확보 — S1 진입의 필수 선행 조건
- 1위 예측 항목의 scoring/rationale 재산출 (현재 "pending" 상태로 데이터 품질 이슈 존재)
- 해당 신경발달 증후군과 protamine 약리작용 간 최소 1건 이상의 전임상 또는 기전 연구 근거 확보
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

