---
layout: default
title: Ebastine
parent: 僅模型預測 (L5)
nav_order: 237
evidence_level: L5
indication_count: 2
---

# Ebastine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Ebastine: 알레르기 비염에서 관상동맥 질환으로

## 한 문장 요약

Ebastine은 2세대 H1 수용체 길항제(항히스타민제)로, 알레르기 비염 및 만성 두드러기 치료에 사용되는 약물입니다.
TxGNN 모델은 **관상동맥 질환(Coronary Artery Disease)**에 효과가 있을 수 있다고 예측하며,
현재 **임상시험은 0건**이고 **1편의 전산 연구 문헌**이 간접적으로 관련됩니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 알레르기 비염, 만성 두드러기 (한국 허가 데이터 없음) |
| 예측 신규 적응증 | 관상동맥 질환 (Coronary Artery Disease) |
| TxGNN 예측 점수 | 99.18% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터(MOA)가 입력되지 않은 상태입니다. 알려진 정보에 따르면, Ebastine은 선택적 2세대 H1 수용체 길항제로, 히스타민에 의한 알레르기 반응을 차단하여 비염·두드러기 증상을 완화합니다. 뇌혈관 장벽 투과성이 낮아 졸음 유발이 적은 것이 특징입니다.

관상동맥 질환과의 연관성은 **CYP2J2 효소를 통한 간접 경로**로 추론됩니다. Ebastine은 CYP2J2의 기질(substrate)로 알려져 있으며, CYP2J2는 심장 조직에서 높게 발현되어 아라키돈산을 epoxyeicosatrienoic acids(EETs)로 대사하는 역할을 합니다. EETs는 혈관 확장, 항염증, 심근세포 보호 효과를 지닌 물질로, 동물 모델에서 심근 허혈 보호 효과가 보고된 바 있습니다.

그러나 이 경로는 현재로서는 **추측성**입니다. Ebastine이 CYP2J2 결합 시 효소를 억제할 경우 오히려 EET 생성이 감소하여 심장에 불리하게 작용할 가능성이 있으며, H1 차단이라는 주요 작용 기전은 관상동맥 질환과 직접적인 관련이 없습니다. 기전의 방향성(유익 vs. 유해)이 현재 실험 데이터로는 확인되지 않습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [18004755](https://pubmed.ncbi.nlm.nih.gov/18004755/) | 2008 | Computational/In Silico | Proteins | CYP2J2의 3차원 구조 동원성 모델링 및 분자 동력학 시뮬레이션을 통해 ebastine 등의 결합 양식을 분석. CYP2J2가 관상동맥 질환·고혈압과 관련된 EET 생성을 촉매함을 기술하며, 약물 결합 특성이 관련 질환 연구에 활용될 수 있음을 시사 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
관상동맥 질환에 대한 Ebastine의 재창출을 지지하는 임상적 근거가 전무하며, 유일한 관련 문헌은 전산 모델링 연구(Tier 3)로 간접적인 기전 연관성만 시사합니다. 기전적 가설 자체도 CYP2J2 억제 시 EET 감소로 이어질 가능성이 있어 실질적 효과 방향이 불명확하고, 한국 내 허가 이력도 없어 규제 경로 확인부터 필요합니다.

**진행하려면 필요한 것:**
- Ebastine의 공식 MOA 및 DrugBank 상세 데이터 확보
- 한국 MFDS 허가 현황 조회
- CYP2J2-EET 경로에서 Ebastine이 억제제인지 단순 기질인지 명확화하는 전임상 실험
- 관상동맥 질환 또는 심근 허혈 동물 모델에서의 효능 검증
- 경고, 금기, 약물 상호작용을 포함한 안전성 정보 보충 (MFDS/EMA/FDA 허가사항 참조)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

