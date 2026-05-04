---
layout: default
title: Cholecalciferol
parent: 僅模型預測 (L5)
nav_order: 163
evidence_level: L5
indication_count: 7
---

# Cholecalciferol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Cholecalciferol: 비타민 D 결핍에서 PTH 분비 장애성 가족성 단독 부갑상선기능저하증으로

## 한 문장 요약

Cholecalciferol(비타민 D3)은 비타민 D 결핍 예방과 칼슘·골 대사 조절을 위해 널리 사용되는 지용성 비타민 보충제입니다.
TxGNN 모델은 **PTH 분비 장애에 의한 가족성 단독 부갑상선기능저하증(familial isolated hypoparathyroidism due to impaired PTH secretion)**에 효과가 있을 수 있다고 예측하였으나,
현재 이를 직접 지지하는 **임상시험 및 문헌 근거가 전혀 없어(L5)** Hold 권고가 유지됩니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 비타민 D 결핍 및 관련 골대사 이상 (보충제) |
| 예측 신규 적응증 | PTH 분비 장애성 가족성 단독 부갑상선기능저하증 |
| TxGNN 예측 점수 | 99.79% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Cholecalciferol은 자외선(UVB) 조사 또는 식이 섭취를 통해 얻는 비타민 D의 비활성 전구체입니다. 간에서 25-hydroxyvitamin D(calcidiol)로 1차 전환된 뒤, 주로 신장의 1α-hydroxylase 효소에 의해 활성형인 1,25-dihydroxyvitamin D(calcitriol)로 최종 전환됩니다. Calcitriol은 장내 칼슘·인 흡수 증진, 신장 칼슘 재흡수 조절, 골 무기질화 유지에 핵심 호르몬으로 기능합니다.

PTH 분비 장애성 가족성 단독 부갑상선기능저하증은 유전적 원인으로 PTH 분비 자체가 결핍되어 저칼슘혈증과 고인산혈증이 나타나는 희귀 내분비 질환입니다. 이론적으로 cholecalciferol은 PTH 비의존성 경로를 통해 장내 칼슘 흡수를 일부 보완할 가능성이 있습니다. 그러나 **PTH 결핍 환경에서는 신장 1α-hydroxylase 활성이 심각하게 억제되어 cholecalciferol의 활성형 전환 효율이 현저히 저하**되는 것이 근본적 한계입니다.

임상 표준치료는 전구체인 cholecalciferol이 아닌 활성형 calcitriol을 직접 투여하는 방식입니다. TxGNN 예측 점수 99.79%는 지식 그래프 내 칼슘 대사 경로의 위상학적 인접성을 반영한 결과이며, 직접적인 약리 근거를 의미하지 않습니다. 이 적응증에 대한 임상시험 또는 문헌 증거는 현재 존재하지 않습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 한국 시판 정보

한국 내 허가 이력이 없습니다 (시판 현황: 미시판).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
이 적응증을 직접 지지하는 임상시험 및 문헌 근거가 전혀 없으며, 기전상으로도 PTH 결핍 환경에서 cholecalciferol의 활성형 전환이 억제되어 직접적인 치료 효과를 기대하기 어렵습니다. 현행 임상 표준치료인 calcitriol과의 역할 차별화 근거 확보가 선행되어야 합니다.

**진행하려면 필요한 것:**
- 이 적응증에 특화된 전임상(세포주·동물 모델) 연구
- PTH 비의존성 칼슘 흡수 경로에서 cholecalciferol의 역할을 직접 평가하는 기전 연구
- Cholecalciferol 대 calcitriol의 비교 효능 데이터
- 약물 작용 기전(MOA) 상세 데이터 확보 (DrugBank API 조회 권장)
- 안전성 정보 확보 (허가사항 PDF 파싱 필요)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

