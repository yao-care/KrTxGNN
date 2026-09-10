---
layout: default
title: Nadolol
parent: 僅模型預測 (L5)
nav_order: 495
evidence_level: L5
indication_count: 5
---

# Nadolol
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

# Nadolol: 원 적응증 미확인 상태에서 악성 신혈관성 고혈압(예측)으로

## 한 문장 요약

Nadolol(DrugBank ID: DB01203)은 원래 적응증 및 작용기전(MOA) 데이터가 확보되지 않은 상태입니다.
TxGNN 모델은 **악성 신혈관성 고혈압(Malignant Renovascular Hypertension)**에 효과가 있을 수 있다고 예측하지만,
이 조합을 지지하는 임상시험이나 문헌은 현재 **0건**이며, 순수하게 모델 예측 점수(99.59%)에만 근거하고 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (original_indications 미제공, MOA 미확인) |
| 예측 신규 적응증 | 악성 신혈관성 고혈압 (Malignant Renovascular Hypertension) |
| TxGNN 예측 점수 | 99.59% (rank 7442) |
| 근거 수준 | L5 (모델 예측만 있음, 실제 연구 없음) |
| 대만 시판 현황 | ✗ 미시판 (未上市) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 없습니다. Nadolol은 약리학적으로 비선택적 β 수용체 차단제 계열로 알려져 있으며, 이 계열은 일반적으로 혈압 조절과 관련된 효과를 가집니다. 다만 본 Evidence Pack에는 original_moa와 original_indications가 모두 비어 있어, 이 예측이 실제 약리 기전에 기반한 것인지 확인할 근거가 부족합니다.

악성 신혈관성 고혈압은 통상 혈관 개입(스텐트/혈관성형술) 또는 RAAS 억제제 기반 처치가 표준 치료로 사용되는 중증 질환으로, 단순 β 차단제 단독요법이 일차 치료로 권장되는 경우는 아닙니다. 따라서 이 예측은 TxGNN 모델의 점수 기반 추론 결과이며, 기전적·임상적으로 직접 뒷받침하는 근거는 확인되지 않았습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

> 참고: 예측 순위 3위 후보인 "pulmonary hypertension owing to lung disease and/or hypoxia"에는 문헌 20편이 검색되었으나, 검토 결과 모두 저산소증 세포생물학·암대사·신경퇴행 관련 기초연구로 nadolol 또는 폐고혈압 치료와 직접 관련이 없어 위양성(false positive) 연관으로 판단됩니다.

## 대만 시판 정보

대만에서 현재 시판 허가 이력이 없습니다 (총 허가증 0건, market_status: 未上市).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

(TFDA 경고/금기 정보 및 DDI 조회 결과 모두 확인되지 않았습니다. 이는 안전성 초기 평가(S1) 진입을 막는 Blocking 등급 데이터 갭입니다.)

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 상위 5개 후보(악성 신혈관성 고혈압, 악성 고혈압성 신질환, 폐고혈압 2건, Braddock 증후군) 모두 근거 수준 L5로, 임상시험·문헌·기전 데이터 어느 것도 뒷받침하지 못하며 순수 모델 점수에만 의존합니다. 일부 후보(폐고혈압 계열)는 오히려 비선택적 β 차단제 사용 시 우심실 부담 증가 등 안전성 우려가 이론적으로 존재합니다. 또한 TFDA 경고/금기 정보 부재로 안전성 초기 평가(S1) 자체가 불가능한 상태입니다.

**진행하려면 필요한 것:**
- TFDA 원 적응증 및 작용기전(MOA) 데이터 확보 (DrugBank API 재조회)
- TFDA 공식 경고문/금기사항 확보 (Blocking 데이터 갭, DG001)
- 악성 신혈관성 고혈압에 특화된 전임상 또는 관찰 연구 확보
- 대만 시판 여부 재확인 (필요 시 해외 허가 현황으로 대체 검토)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

