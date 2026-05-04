---
layout: default
title: Cimetidine
parent: 僅模型預測 (L5)
nav_order: 167
evidence_level: L5
indication_count: 9
---

# Cimetidine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Cimetidine: 소화성 궤양에서 서서히 진행하는 전신 비만세포증으로

## 한 문장 요약

Cimetidine은 히스타민 H2 수용체를 차단하여 위산 분비를 억제하는 고전적인 소화성 궤양 치료제로, 1976년 최초 H2 차단제로 임상에 도입되었습니다. TxGNN 모델은 **서서히 진행하는 전신 비만세포증(Smouldering Systemic Mastocytosis)**에 효과가 있을 수 있다고 예측하나, 현재 이 방향을 지지하는 임상시험 및 문헌 근거는 존재하지 않습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 소화성 궤양 (Peptic Ulcer Disease) |
| 예측 신규 적응증 | 서서히 진행하는 전신 비만세포증 (Smouldering Systemic Mastocytosis) |
| TxGNN 예측 점수 | 99.80% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Cimetidine은 위 벽세포의 히스타민 H2 수용체를 경쟁적으로 차단하여 기저 위산 분비와 자극성 위산 분비를 모두 억제하는 약물입니다. 이 기전이 소화성 궤양의 핵심 치료 원리로서, 상세한 MOA 데이터는 현재 확보되어 있지 않으나 약물 분류상 H2 수용체 길항제(H2RA)에 속하며 수십 년간의 임상 사용을 통해 약리 프로파일이 잘 알려져 있습니다.

서서히 진행하는 전신 비만세포증(Smouldering Systemic Mastocytosis, SSM)은 비만세포가 골수 및 다양한 조직에 비정상적으로 축적되는 희귀 혈액 질환입니다. 비만세포 활성화 시 히스타민을 포함한 다양한 매개 물질이 대량 방출되며, 방출된 히스타민이 H2 수용체를 자극하면 위산 과다 분비, 소화불량, 저혈압 등 전신 증상이 유발될 수 있습니다. 이론적으로 Cimetidine(H2 차단제)을 H1 차단제와 병용하면 히스타민 과다로 인한 증상을 체계적으로 조절할 수 있다는 기전적 타당성이 있습니다.

그러나 현재 이 Evidence Pack 내에는 해당 적응증에 대한 임상 근거가 전혀 확인되지 않았습니다. 이 예측은 H2 차단제의 작용 기전과 비만세포증의 히스타민 병태생리 간 이론적 연결에 기반한 순수한 기전적 추론 수준이며, TxGNN 모델 예측이 근거의 전부입니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 한국 시판 정보

현재 한국 내 Cimetidine 허가 제품이 없습니다 (허가증 0건).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
서서히 진행하는 전신 비만세포증에 대한 Cimetidine의 효능을 지지하는 임상시험 및 문헌 근거가 전혀 없어 근거 수준 L5에 해당합니다. TxGNN 예측 점수(99.80%)는 높으나, 기전적 타당성만으로는 임상 진행을 결정하기 어렵습니다.

**진행하려면 필요한 것:**
- 비만세포증 환자에서 H2 차단제 병용 요법(H1+H2 차단제)에 관한 체계적 문헌 검색 수행
- Cimetidine의 상세 작용 기전 데이터(MOA) 확보 (DrugBank API 조회 권장)
- 안전성 정보 확보: 허가 경고문, 금기, 약물 상호작용 (TFDA/MFDS 허가 사항 또는 FDA label 검토)
- 한국 내 허가 가능성 검토 및 시장 진입 전략 수립 (현재 미허가)
- 전임상 또는 탐색적 임상 연구 프로토콜 개발 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

