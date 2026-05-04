---
layout: default
title: Acarbose
parent: 僅模型預測 (L5)
nav_order: 16
evidence_level: L5
indication_count: 9
---

# Acarbose
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

# Acarbose: 2형 당뇨병에서 Classic Stiff Person Syndrome으로

## 한 문장 요약

Acarbose는 장관 내 α-글루코시다아제(alpha-glucosidase)를 억제하여 탄수화물 흡수를 지연시키는 약물로, 2형 당뇨병의 식후 혈당 조절에 사용되어 왔습니다.
TxGNN 모델은 **Classic Stiff Person Syndrome**에 효과가 있을 수 있다고 예측하나,
현재 이를 직접 지지하는 임상시험이나 문헌은 **전무하며**, 근거 수준은 모델 예측에만 의존하는 **L5**입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 2형 당뇨병 (한국 허가 정보 없음) |
| 예측 신규 적응증 | Classic Stiff Person Syndrome |
| TxGNN 예측 점수 | 99.65% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

공식 작용 기전(MOA) 데이터가 수집되지 않았습니다. 그러나 예측 근거 분석에 따르면, Acarbose는 장관 내 α-글루코시다아제를 억제하여 이당류·다당류의 포도당 분해를 늦추고, 식후 혈당 급등을 완화하는 약물입니다. 인슐린 분비나 감수성에는 직접 작용하지 않습니다.

Classic Stiff Person Syndrome(SPS)은 자가면역성 신경계 질환으로, GAD65(글루탐산 탈카르복실화효소)에 대한 자가항체가 척수 및 뇌간의 GABA성 억제 신경원 기능을 교란하여 심한 근강직과 유발성 경련을 일으킵니다. GAD65는 GABA 합성 효소이기도 하지만, 동시에 췌장 β세포에서 인슐린 분비와도 연관됩니다. TxGNN 지식 그래프는 이 공유 노드(당뇨병 ↔ GAD65 ↔ SPS)를 통해 연결고리를 형성한 것으로 추정됩니다.

그러나 Acarbose의 직접 작용점은 장관 내 α-글루코시다아제이며, GAD65 자가면역 반응 억제, GABA성 신경 기능 회복, 또는 면역조절 경로에 개입한다는 증거가 없습니다. 두 질환의 기전적 연관성은 극히 낮으며, 높은 TxGNN 예측 점수는 생물학적 타당성보다 지식 그래프상 간접 연결에 기인할 가능성이 높습니다.

---

## 임상시험 근거

현재 Acarbose와 Classic Stiff Person Syndrome을 연결하는 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 Acarbose와 Classic Stiff Person Syndrome을 직접 연구한 관련 문헌이 없습니다.

> **참고 — 췌장 무형성(Pancreatic Agenesis, 9순위 예측):** 해당 적응증에 대해 11편의 문헌이 검색되었으나, 모두 2형 당뇨병 총론·인슐린 자가면역 증후군·동물 실험 등 간접 관련 논문으로, Acarbose를 췌장 무형성 환자에 직접 적용한 연구는 포함되어 있지 않습니다.

---

## 전체 예측 요약

| 순위 | 적응증 | TxGNN 점수 | 근거 수준 | 권장 결정 |
|------|--------|-----------|---------|---------|
| 1 | Classic Stiff Person Syndrome | 99.65% | L5 | Hold |
| 2 | Focal Stiff Limb Syndrome | 99.65% | L5 | Hold |
| 3 | Thiamine-responsive Dysfunction Syndrome | 99.62% | L5 | Hold |
| 4 | Opsismodysplasia | 99.62% | L5 | Hold |
| 5 | Drug-induced Localized Lipodystrophy | 99.24% | L5 | Hold |
| 6 | Centrifugal Lipodystrophy | 99.22% | L5 | Hold |
| 7 | Pressure-induced Localized Lipoatrophy | 99.20% | L5 | Hold |
| 8 | Idiopathic Localized Lipodystrophy | 99.17% | L5 | Hold |
| 9 | Pancreatic Agenesis | 99.16% | **L4** | Hold |

> 2순위 Focal Stiff Limb Syndrome은 Classic SPS의 국소 변이형으로, TxGNN 점수가 동일하여 독립적 예측 근거가 아닌 동일한 지식 그래프 경로의 출력으로 판단됩니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN이 예측한 9개 적응증 전체가 임상시험과 직접 관련 문헌의 뒷받침이 없으며, 최고 순위 예측인 Classic Stiff Person Syndrome과 Acarbose의 기전적 연관성은 극히 낮습니다. 높은 예측 점수는 지식 그래프의 공유 노드(당뇨병/GAD65)에 따른 간접 연결에 기인하는 것으로 판단되며, 현재 상태에서 재창출 추진은 근거가 불충분합니다.

**진행하려면 필요한 것:**
- 공식 MOA 데이터(DrugBank API) 수집 — 기전 관련성 분석의 전제 조건
- 한국/대만 허가 사항(경고, 금기, 약물 상호작용) 확보 — 안전성 초기 평가 차단 해제
- Stiff Person Syndrome 및 당뇨 관련 희귀질환에서의 α-글루코시다아제 억제 전임상 연구 탐색
- 보다 기전적으로 타당한 후보 적응증(예: 당뇨 동반 희귀 대사 질환, TRMA의 혈당 보조 관리) 재평가 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

