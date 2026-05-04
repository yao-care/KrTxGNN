---
layout: default
title: Brolucizumab
parent: 僅模型預測 (L5)
nav_order: 151
evidence_level: L5
indication_count: 4
---

# Brolucizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Brolucizumab: 신생혈관성 황반변성에서 미토콘드리아 산화적 인산화 장애로

## 한 문장 요약

Brolucizumab은 VEGF-A와 그 수용체(VEGFR-1/VEGFR-2)의 결합을 차단하는 단일 사슬 항체 단편(scFv)으로, 신생혈관성 황반변성(wet AMD) 및 당뇨병성 황반부종 치료를 위한 유리체 내 주사제로 사용됩니다.
TxGNN 모델은 **미토콘드리아 산화적 인산화 장애(Mitochondrial Oxidative Phosphorylation Disorder Due to Nuclear DNA Anomalies)**에 효과가 있을 수 있다고 예측하나,
이를 지지하는 **임상시험 및 문헌이 전무하며**, 기전적 연관성 역시 극히 낮습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 신생혈관성 황반변성 (wet AMD), 당뇨병성 황반부종 |
| 예측 신규 적응증 | 미토콘드리아 산화적 인산화 장애 (Mitochondrial OXPHOS Disorder Due to Nuclear DNA Anomalies) |
| TxGNN 예측 점수 | 99.67% |
| 근거 수준 | L5 |
| 대만 시판 현황 | 미허가 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Brolucizumab은 VEGF-A와 그 수용체 VEGFR-1/VEGFR-2의 결합을 차단하는 기전을 통해 망막 내 비정상적 혈관 신생과 혈관 투과성을 억제합니다. 이 약물은 유리체 내 주사 제형으로만 투여되며, 전신 생체이용률은 2% 미만으로 극히 낮습니다.

미토콘드리아 산화적 인산화 장애(OXPHOS disorder)는 핵 DNA 변이에 의해 전자 전달계(ETC) 복합체에 결함이 생겨 ATP 생산이 저해되는 에너지 대사 질환입니다. 이 병태 생리는 VEGF 신호 경로와 직접적인 연관이 없습니다. 일부 문헌에서 VEGF가 미토콘드리아에 간접적 보호 효과를 가질 수 있다고 언급하나, 이는 매우 추측적인 연결고리에 불과합니다.

결정적으로 Brolucizumab은 전신 투여 제형이 아니기 때문에, 전신성 대사 질환인 OXPHOS disorder에 치료 효과를 발휘할 만한 전신 약물 농도에 도달하는 것이 구조적으로 불가능합니다. TxGNN의 높은 예측 점수(0.9967)는 지식 그래프에 작용 기전(MoA) 노드 정보가 누락된 것에서 비롯된 위양성(false positive)일 가능성이 높습니다.

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
모든 예측 적응증에서 근거 수준이 L5(모델 예측만 있음)이며, 기전적 연관성이 극히 낮고 유리체 내 주사 제형의 전신 노출 한계로 인해 전신성 미토콘드리아 질환에 대한 실질적 적용이 불가능합니다. TxGNN 고점수는 지식 그래프의 MoA 정보 누락으로 인한 위양성으로 판단되어, 현 시점에서는 추가 탐색을 권장하지 않습니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 데이터를 지식 그래프에 반영하여 예측 신뢰도 재검증
- 대만 허가 현황 및 안전성 정보(경고/금기 사항) 확보
- VEGF와 미토콘드리아 기능 간 직접적 연관성을 입증하는 전임상 데이터가 존재할 경우에 한해 재평가 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

