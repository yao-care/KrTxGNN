---
layout: default
title: Guselkumab
parent: 僅模型預測 (L5)
nav_order: 369
evidence_level: L5
indication_count: 10
---

# Guselkumab
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

# Guselkumab: 건선에서 약물유발성 골다공증(Drug-induced Osteoporosis)으로

## 한 문장 요약

Guselkumab은 IL-23 억제 기전의 생물학적제제로, 원래 건선(psoriasis) 치료를 위해 개발되었습니다.
TxGNN 모델은 이번 평가에서 1순위 예측으로 **약물유발성 골다공증(Drug-induced Osteoporosis)**에 효과가 있을 수 있다고 제시했으나(예측 점수 **99.84%**), 이를 뒷받침하는 임상시험이나 문헌은 **현재 전혀 없습니다**.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 건선 (Psoriasis) — 근거팩 내 기전 근거(rank 3)에서 원 승인 적응증으로 확인됨. 단, 본 근거팩의 한국 허가 데이터에는 기록 없음 |
| 예측 신규 적응증 | 약물유발성 골다공증 (Drug-induced Osteoporosis) |
| TxGNN 예측 점수 | 99.84% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미상장 (허가 0건) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 확보되어 있지 않습니다. 다만 근거팩 내 다른 예측 항목(건선, 궤양성대장염)의 기전 서술을 통해, Guselkumab이 IL-23의 p19 소단위에 결합하여 Th17 세포 분화와 하위 IL-17/IL-22 생성을 억제하는 인간화 IgG1λ 단클론항체임을 확인할 수 있습니다.

약물유발성 골다공증과의 연관성은 골면역학(osteoimmunology) 가설에 근거합니다: Th17 세포가 RANKL을 통해 파골세포(osteoclast) 활성화를 촉진한다는 문헌이 있어, 이론상 IL-23/Th17 축 억제가 골흡수를 줄일 가능성이 제기됩니다.

그러나 이는 간접적·추론적 연결에 불과하며, Guselkumab이 약물유발성 골다공증에 실제 효과가 있는지를 직접 검증한 임상시험이나 문헌은 전무합니다. TxGNN의 높은 점수는 지식그래프 상의 경로 유사성을 반영할 뿐, 임상적 타당성을 검증한 결과가 아닙니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 점수는 높지만(99.84%), 약물유발성 골다공증에 대해 이를 뒷받침하는 임상시험, 문헌, 전임상 기전 연구가 전혀 없습니다(L5, S0 단계). 골면역학 가설은 이론적으로만 존재하며, 실제 검증 데이터가 없는 상태에서 임상 개발을 진행할 근거가 부족합니다.

**진행하려면 필요한 것:**
- Guselkumab의 골대사 지표(BMD, 골표지자 등)에 대한 전임상 또는 관찰 연구
- 약물유발성 골다공증 환자 코호트에서의 후향적/전향적 데이터
- 상세 작용기전(MOA) 및 TFDA/식약처 허가사항(경고·금기) 확보
- 골면역학 가설을 뒷받침할 IL-23/Th17-RANKL 경로의 직접적 실험 근거
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

