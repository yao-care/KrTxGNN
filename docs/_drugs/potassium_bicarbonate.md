---
layout: default
title: Potassium Bicarbonate
parent: 僅模型預測 (L5)
nav_order: 565
evidence_level: L5
indication_count: 1
---

# Potassium Bicarbonate
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

# POTASSIUM BICARBONATE: 미상 적응증에서 위십이지장염(Gastroduodenitis)으로

## 한 문장 요약

Potassium Bicarbonate(중탄산칼륨)는 전해질/미네랄 보충제로 추정되나 원래 적응증과 작용 기전 데이터가 확보되지 않았습니다.
TxGNN 모델은 **위십이지장염(Gastroduodenitis)**에 효과가 있을 수 있다고 예측했으나(예측 점수 99.72%),
이를 뒷받침하는 임상시험이나 문헌은 **현재 전혀 없습니다**.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (데이터 없음) |
| 예측 신규 적응증 | 위십이지장염 (Gastroduodenitis) |
| TxGNN 예측 점수 | 99.72% |
| 근거 수준 | L5 (모델 예측만 존재, 실증 연구 없음) |
| 한국 시판 현황 | 미상 (한국 내 허가 정보 없음, 원 데이터는 台灣 미상시) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. Potassium Bicarbonate는 전해질/미네랄 보충제 계열로 추정되나, DrugBank 조회에서도 기존 적응증 및 MOA가 확보되지 않았습니다.

TxGNN 예측 점수가 99.72%로 매우 높지만, 이는 지식그래프 상에서 이 약물의 노드 연결이 희소하거나 대사 경로 공출현으로 인해 발생한 결과일 가능성이 있습니다. 전해질류 화합물은 특성상 광범위한 대사·산-염기 균형 경로에 연결되어 있어, 모델이 실제 생물학적 타당성과 무관하게 높은 점수를 산출하는 경우가 흔합니다. 현재로서는 위십이지장염과의 기전적 연관성을 뒷받침할 근거가 전혀 없습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 한국 시판 정보

현재 시판 허가 정보가 없습니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 점수는 높으나 이를 뒷받침하는 임상시험, 문헌, 기전 데이터가 전무하여(L5 등급) 현 단계에서 진행 근거가 부족합니다. 원 적응증과 MOA조차 확인되지 않아 안전성 초기 평가(S1)도 진행할 수 없는 상태입니다.

**진행하려면 필요한 것:**
- 원 적응증 및 작용 기전(MOA) 확인 (DrugBank API 재조회 또는 문헌 검색)
- 허가사항 경고·금기 정보 확보 (TFDA 등 관련 규제기관 조회)
- 위십이지장염 관련 전임상/기전 연구 존재 여부 확인
- 최소 관찰 연구 또는 체계적 문헌고찰 수준의 근거 확보 전까지 재평가 보류
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

