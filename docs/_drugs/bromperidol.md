---
layout: default
title: Bromperidol
parent: 僅模型預測 (L5)
nav_order: 154
evidence_level: L5
indication_count: 1
---

# Bromperidol
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

# Bromperidol: 항정신병약에서 불면증으로

## 한 문장 요약

Bromperidol은 Butyrophenone 계열의 항정신병약으로, 도파민 D2 수용체 길항제로 작용합니다.
TxGNN 모델은 **불면증(Insomnia)**에 효과가 있을 수 있다고 예측하지만,
현재 이를 지지하는 **임상시험 및 문헌 근거가 전무**하며, 기전상 위험·효익 비율도 매우 불리합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 항정신병 (Butyrophenone 계열, 한국 미허가) |
| 예측 신규 적응증 | 불면증 (Insomnia) |
| TxGNN 예측 점수 | 99.85% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 이 예측이 타당한 이유는?

Bromperidol은 Butyrophenone 계열의 전형적 항정신병약으로, Haloperidol과 구조적으로 매우 유사합니다. 주요 작용 기전은 도파민 D2 수용체 강력 길항으로, 이를 통해 정신증 증상을 억제합니다. 단, 본 약물의 상세 MOA 데이터는 현재 수집되지 않은 상태(Data Gap)로, 아래 분석은 계열 특성에 기반한 추론입니다.

일부 항정신병약(예: Quetiapine, Chlorpromazine)은 히스타민 H1 수용체 길항 활성을 통한 강한 진정 효과를 가지며, 이를 근거로 불면증 적응증에 응용됩니다. TxGNN의 고점수(0.9985)는 지식 그래프 내 **「항정신병약 → 진정 작용 → 불면증」** 간접 경로 연관성에서 기인한 것으로 추정됩니다.

그러나 Bromperidol의 경우 H1 수용체 친화력이 동계열 약물에 비해 현저히 낮으며, D2 수용체에 대한 높은 선택성으로 인해 추체외로 증상(EPS), 지발성 운동장애 등 심각한 부작용 위험이 동반됩니다. 비정신질환(불면증) 환자에게 이러한 위험을 감수하는 것은 현재의 근거 수준에서 정당화되기 어렵습니다. 이 예측은 **계산 추론(computational inference)** 에 해당하며 임상 실증이 아닙니다.

---

## 임상시험 근거

현재 Bromperidol × 불면증에 관한 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 Bromperidol × 불면증에 관한 관련 문헌이 없습니다.

---

## 한국 시판 정보

Bromperidol은 현재 한국에서 허가된 제품이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
Bromperidol의 불면증 예측은 TxGNN 모델의 지식 그래프 내 간접 경로에서 유래한 계산 추론에 불과하며, 이를 뒷받침하는 임상시험·문헌 근거가 전혀 존재하지 않습니다(L5). 아울러 D2 고선택성으로 인한 심각한 추체외로 증상 위험은 불면증이라는 비정신과적 적응증에서의 위험·효익 비율을 극히 불리하게 만듭니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 상세 데이터 확보 (DrugBank API 조회)
- 한국 식약처 허가사항 또는 글로벌 규제기관(EMA·FDA) 안전성 정보 확보
- 불면증에서의 D2 길항제 관련 전임상/기전 연구 문헌 검색
- H1 수용체 결합 친화력 데이터로 진정 효과 가능성 정량화
- 동계열 약물(Haloperidol 등) 대비 차별성 근거 마련 시 재평가 고려
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

