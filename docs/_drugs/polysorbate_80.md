---
layout: default
title: Polysorbate 80
parent: 僅模型預測 (L5)
nav_order: 563
evidence_level: L5
indication_count: 1
---

# Polysorbate 80
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

# Polysorbate 80: 부형제(적응증 없음)에서 선천성 어린선양 홍피증으로

## 한 문장 요약

Polysorbate 80(DB11063)은 치료 목적의 의약품이 아니라 **비이온성 계면활성제/유화제로 사용되는 부형제**이며, 국내에는 시판 중인 허가 제품이 없습니다.
TxGNN 모델은 **선천성 어린선양 홍피증(Congenital Ichthyosiform Erythroderma)**에 효과가 있을 수 있다고 예측했으나(점수 99.43%), 이를 뒷받침하는 임상시험이나 문헌 근거는 **전혀 없습니다**.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 없음 (부형제/유화제 용도, 치료 적응증 미보유) |
| 예측 신규 적응증 | 선천성 어린선양 홍피증 (Congenital Ichthyosiform Erythroderma) |
| TxGNN 예측 점수 | 99.43% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미상시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 없습니다. Polysorbate 80은 약리학적 활성 성분이 아니라 의약품 제형에서 유화·증용 목적으로 쓰이는 부형제이며, 기존 치료 적응증 자체가 존재하지 않습니다.

선천성 어린선양 홍피증은 표피 장벽 단백질 및 지질 대사 관련 유전자 돌연변이로 발생하는 상염색체 열성 유전 피부 질환입니다. TxGNN이 부여한 높은 점수는 지식그래프 상에서 polysorbate 80이 외용 제형·유화 기제 등 피부과 관련 주제와 **위상적으로 가깝게 위치**하기 때문일 가능성이 높으며, 실제 약리학적 연관성을 반영한다고 보기 어렵습니다.

이 성분과 해당 질환 사이에 확인 가능한 기전 경로가 없어, 예측의 임상적 타당성은 현재로서는 근거가 매우 약합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
근거 수준이 L5(모델 예측만 존재, 실제 연구 없음)이며, 임상시험·문헌 근거가 전무합니다. 또한 이 물질은 치료용 의약품이 아닌 부형제로, 작용 기전 자체가 확인되지 않아 예측의 생물학적 타당성을 판단할 수 없습니다.

**진행하려면 필요한 것:**
- Polysorbate 80의 작용 기전(MOA) 및 약리학적 데이터 확보
- TFDA 등 규제기관의 안전성 정보(경고, 금기) 확보 (현재 Blocking 등급 데이터 갭)
- 예측이 그래프 위상적 인공물(artifact)인지 실제 생물학적 신호인지 구분하기 위한 전임상/기전 연구
- 최소 L3 수준(관찰 연구 또는 체계적 문헌고찰) 근거 확보 전까지 추가 검토 보류 권장
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

