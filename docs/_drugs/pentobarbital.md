---
layout: default
title: Pentobarbital
parent: 僅模型預測 (L5)
nav_order: 542
evidence_level: L5
indication_count: 10
---

# Pentobarbital
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

# Pentobarbital: 진정·마취 바르비투르산염에서 불면증으로

## 한 문장 요약

Pentobarbital은 GABA-A 수용체를 정방향 조절하는 전형적인 바르비투르산염 계열 약물로, 진정·최면·항경련 및 마취 유도 목적으로 오랫동안 사용되어 왔습니다.
TxGNN 모델은 **불면증(Insomnia)**에 효과가 있을 것으로 예측했으나(예측 점수 99.9995%), 실제로는 이미 잘 알려진 이 약물의 기존 약리 특성이며, 현재 근거는 **관련 임상시험 0건**과 **동물/기전 연구 위주의 문헌 20편**(대부분 다른 천연물의 수면 효과를 측정할 때 pentobarbital을 "대조 도구"로 사용한 연구)에 그칩니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 자료 없음 (Evidence Pack 내 허가 정보 미기재, 국내 미시판) |
| 예측 신규 적응증 | 불면증 (Insomnia) |
| TxGNN 예측 점수 | 99.9995% |
| 근거 수준 | L4 (전임상/기전 연구 수준) |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

공식 DrugBank MOA 데이터는 현재 확보되지 않았습니다([Data Gap], DG002). 다만 Evidence Pack의 재창출 근거 텍스트에 따르면, Pentobarbital은 **GABA-A 수용체 정방향 조절제**로서 중추신경계를 비특이적으로 억제해 진정·수면 유도 효과를 나타내는 것으로 알려져 있습니다. 이는 교과서 수준으로 확립된 약리 기전입니다.

다만 중요한 점은, 이 예측이 **진짜 새로운 재창출 가설이 아니라는 것**입니다. Evidence Pack 자체가 명시하듯, 불면증에 대한 진정·수면 효과는 Pentobarbital의 **원래 약리 특성**이지 새롭게 발견된 적응증이 아닙니다. 실제로 검색된 문헌 대부분은 Pentobarbital 자체를 치료제로 연구한 것이 아니라, 다른 천연물·한약 성분의 수면 효과를 검증할 때 "Pentobarbital 유발 수면시험"의 **대조/도구 약물**로 사용한 연구들입니다. 즉, 근거의 양은 많아 보이지만 실질적으로 이 약물을 새 적응증에 재창출할 근거로서의 가치는 제한적입니다.

또한 현대 임상에서는 치료역이 좁고 의존성·호흡억제 위험이 큰 바르비투르산염 대신 벤조디아제핀계·Z-drug이 불면증 표준 치료로 자리잡았다는 점도 고려해야 합니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [40023510](https://pubmed.ncbi.nlm.nih.gov/40023510/) | 2025 | 동물시험 | Sleep medicine | Icariin의 진정·최면 효과가 GABA 작용 경로를 통해 나타남을 확인 (Pentobarbital 자체 연구 아님) |
| [39770888](https://pubmed.ncbi.nlm.nih.gov/39770888/) | 2024 | 동물시험 | Nutrients | 대추씨(Zizyphi Semen) 추출물이 GABA성 전달 조절을 통해 수면 질 개선, Pentobarbital 수면시험을 평가 도구로 사용 |
| [36288650](https://pubmed.ncbi.nlm.nih.gov/36288650/) | 2023 | 네트워크 약리학/동물시험 | Phytomedicine | Sishen Wan(한약)의 불면증 신규 적응증 기전 규명, Pentobarbital은 평가 모델에 활용 |
| [34509822](https://pubmed.ncbi.nlm.nih.gov/34509822/) | 2021 | 미분류(동물모델) | Biomedicine & Pharmacotherapy | 변형 Suanzaoren탕이 Orexin-A/HPA축 조절로 수면 유도, PCPA 유발 불면 마우스 모델 |
| [38403005](https://pubmed.ncbi.nlm.nih.gov/38403005/) | 2024 | 미분류(동물모델) | Journal of Ethnopharmacology | Guhan Yangsheng Jing이 NLRP3/Caspase1/GSDMD 경로 통한 신경보호 및 수면 개선 |
| [40493075](https://pubmed.ncbi.nlm.nih.gov/40493075/) | 2025 | 미분류(동물모델) | Psychopharmacology | Ginsenoside Rg1이 Nrf2/HO-1 경로로 PCPA 유발 불면 완화 |
| [32240473](https://pubmed.ncbi.nlm.nih.gov/32240473/) | 2020 | 미분류(동물모델) | Chinese J Integrative Medicine | Polygala tenuifolia의 고령 불면 랫드 모델 진정·최면 효과 및 전사체 분석 |
| [40347763](https://pubmed.ncbi.nlm.nih.gov/40347763/) | 2025 | 미분류(동물모델) | J Pharm Biomed Analysis | Yiyin Anshen 과립의 진정·최면 효과; Pentobarbital sodium 유발 수면시험을 평가 방법으로 직접 사용 |
| [40354840](https://pubmed.ncbi.nlm.nih.gov/40354840/) | 2025 | 미분류(동물모델) | Journal of Ethnopharmacology | Jujuboside A가 PVT의 GABA성 조절을 통해 불면 개선 |
| [30344286](https://pubmed.ncbi.nlm.nih.gov/30344286/) | 2018 | 미분류(동물모델) | Medicina (Kaunas) | Lagenaria vulgaris/Cucurbita pepo 추출물의 수면 연장 효과, Pentobarbital 유발 수면 및 flumazenil/naloxone 길항시험으로 기전 규명 |

> ⚠ 위 문헌 대부분은 **Pentobarbital 자체의 불면증 치료 효능을 검증한 연구가 아니라**, 다른 물질의 수면 유도 효과를 측정할 때 Pentobarbital을 실험 도구(양성 대조군)로 사용한 연구입니다. 이는 이미 확립된 Pentobarbital의 약리학적 특성을 재확인하는 정도의 근거이며, "새로운 적응증"을 지지하는 직접 증거로 보기 어렵습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> ⚠ 참고: 본 Evidence Pack에서는 **주요 경고, 금기, DDI 정보가 모두 확보되지 않았으며**(DG001, Blocking 등급), 이는 안전성 초기 평가(S1) 진행 자체를 막는 수준의 데이터 공백입니다. 실제 검토 진행 전 TFDA/허가사항 원문 확보가 필수입니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
불면증 예측은 Pentobarbital의 **기존에 이미 알려진 약리 특성**을 재확인하는 수준이며, 실제 재창출 가설로서의 신규성이 낮습니다. 또한 뒷받침 근거가 대부분 동물/기전 연구이고 관련 인체 임상시험이 전무하며(임상시험 0건), 무엇보다 허가사항(경고·금기) 자료가 Blocking 등급으로 누락되어 있어 안전성 초기 평가조차 진행할 수 없는 상태입니다.

**진행하려면 필요한 것:**
- TFDA/식약처 허가사항(경고·금기) 원문 확보 — DG001 (Blocking)
- DrugBank 등 공식 MOA 자료 확보 — DG002 (High)
- 불면증에 대한 실제 인체 대상 임상시험 자료 확보 (현재 없음)
- 국내 허가/시판 현황 재확인 (현재 미시판, 허가증 0건)
- 벤조디아제핀·Z-drug 대비 치료적 차별점 및 안전역 재평가
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

