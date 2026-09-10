---
layout: default
title: Iopromide
parent: 僅模型預測 (L5)
nav_order: 403
evidence_level: L5
indication_count: 10
---

# Iopromide
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

# Iopromide: X선/CT 조영제에서 골관절염 소인(Osteoarthritis Susceptibility)으로

## 한 문장 요약

Iopromide는 비이온성 요오드화 X선/CT 조영제로, 원래 영상 진단 시 대비 증강 목적으로만 사용됩니다.
TxGNN 모델은 **골관절염 소인(Osteoarthritis Susceptibility)**에 효과가 있을 수 있다고 예측했지만,
현재 이를 뒷받침하는 **임상시험과 문헌이 전혀 없으며**, 평가팀 자체 판단으로도 지식그래프의 위양성(false positive) 가능성이 높다고 지적하고 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인된 허가 적응증 없음 (참고: X선/CT 영상 조영 증강용 조영제) |
| 예측 신규 적응증 | 골관절염 소인 (Osteoarthritis Susceptibility) |
| TxGNN 예측 점수 | 99.57% |
| 근거 수준 | L5 (임상시험 0건, 문헌 0건) |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다(Data Gap). 확보된 정보에 따르면 Iopromide는 비이온성 요오드화 X선 조영제로, X선/CT 영상에서 대비를 높이는 물리적 작용만 가지며, 관절 퇴행 경로에 관여한다고 알려진 약리 기전은 없습니다.

평가팀의 자체 분석(repurposing_rationale)도 이 예측에 대해 "기존 적응증과 MOA 데이터가 모두 없는 상태에서 기전 근거가 부재하며, TxGNN 지식그래프의 위양성 가능성이 높다"고 명시하고 있습니다. 즉 기존 적응증-신규 적응증 간 기전적 연관성을 뒷받침할 근거가 현재로서는 확인되지 않습니다.

참고로 순위 2위인 "osteoarthritis"(골관절염, 소인이 아닌 확정 질환) 항목에는 문헌 2편이 연결되어 있으나, 두 편 모두 조영제를 이용한 **진단적 영상 촬영**(CT 유도 신경 차단 위치 확인, MRI 연골 두께 측정) 연구로, 치료적 효과를 시사하는 근거는 아닙니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

한국 내 허가된 제품 정보가 없습니다 (미시판, 허가증 0건).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 신규 적응증(골관절염 소인)에 대한 임상시험 및 문헌 근거가 전무하며(L5), 평가팀 자체 분석에서도 기전적 근거 부재로 위양성 가능성이 높다고 판단했습니다. 또한 한국 내 시판 이력 및 허가 정보가 없어 규제적 기반도 갖추지 못한 상태입니다.

**진행하려면 필요한 것:**
- Iopromide의 작용 기전(MOA) 데이터 확보 (DrugBank 등)
- 식약처(MFDS) 허가사항 및 경고·금기 정보 확보 (현재 Blocking 등급 데이터 갭)
- 골관절염 관련 실제 치료적 임상/전임상 근거 추가 확보 여부 재검토
- 근거 미확보 시 후속 평가 대상에서 제외 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

