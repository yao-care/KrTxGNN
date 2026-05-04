---
layout: default
title: Digoxin
parent: 僅模型預測 (L5)
nav_order: 221
evidence_level: L5
indication_count: 6
---

# Digoxin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# DIGOXIN: 심부전/심방세동에서 변이형 협심증(Prinzmetal angina)으로

---

## 한 문장 요약

Digoxin은 Na⁺/K⁺-ATPase를 억제하는 강심배당체(cardiac glycoside)로, 전통적으로 심부전 및 심방세동(AF) 치료에 사용되어 왔습니다.
TxGNN 모델은 **변이형 협심증(Prinzmetal angina)**을 최우선 예측 적응증으로 제시하였으나,
임상시험은 전무하며 **2편의 문헌**만 존재하고, **기전적 분석 결과 오히려 잠재적 위해(harm) 가능성**이 확인됩니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 심부전, 심방세동 (허가 데이터 없음 — 약리학적 알려진 용도) |
| 예측 신규 적응증 | 변이형 협심증 (Prinzmetal angina) |
| TxGNN 예측 점수 | 99.81% |
| 근거 수준 | L4 (기전 연구 수준) |
| 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 이 예측이 타당한 이유는?

> ⚠️ **경고: 이 예측은 치료 효능이 아닌 잠재적 위해(harm)를 시사합니다.**

상세한 작용 기전 데이터(MOA)가 현재 Evidence Pack에 포함되어 있지 않습니다. 그러나 Digoxin의 잘 알려진 약리 작용에 따르면, 이 약물은 **Na⁺/K⁺-ATPase를 억제**하여 세포 내 Na⁺ 농도를 높이고, 이어서 Na⁺/Ca²⁺ 교환체를 통해 **세포 내 Ca²⁺ 농도를 상승**시킵니다. 심근에서는 이 기전이 수축력 증가(양성 강심 효과)로 작용하지만, 혈관 평활근에서는 **수축 촉진**으로 이어집니다.

변이형 협심증(Prinzmetal angina)은 관상동맥 혈관경련(vasospasm)에 의해 발생하는 질환입니다. Digoxin이 세포 내 Ca²⁺를 상승시키는 기전은 혈관 평활근 수축을 촉진하여 오히려 **관상동맥 경련을 악화**시킬 수 있습니다. 이는 변이형 협심증의 병리 방향과 정반대입니다.

변이형 협심증의 표준 치료는 칼슘 채널 차단제(CCB)와 질산염(nitrate)으로, Ca²⁺ 유입을 억제하고 혈관을 이완시키는 방향으로 작용합니다. TxGNN의 예측 점수(99.81%)가 높음에도 불구하고, 기전적 분석은 Digoxin이 이 적응증에서 치료제가 아닌 **금기 약물에 가깝다**는 결론을 지지합니다.

---

## 임상시험 근거

현재 변이형 협심증(Prinzmetal angina)에 대한 Digoxin 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Review | Acta Physiol Pharmacol Bulg | 항고혈압 치료의 일주기리듬(chronopharmacology) 고찰. 혈압 변동 및 시간별 약리 특성 분석. Digoxin의 변이형 협심증 치료 효능에 대한 직접 근거 없음 |
| [9206110](https://pubmed.ncbi.nlm.nih.gov/9206110/) | 1996 | Review | Chin Med Sci J | 앙아위 협심증(angina decubitus) 환자 30명 연구. 발작 전 심근 산소 소비량(MOC) 증가 확인. 변이형 협심증 치료로서 Digoxin 사용을 지지하는 근거 없음 |

> **편집자 주**: 검색된 2편의 문헌 모두 Digoxin의 변이형 협심증 **치료 효능**을 지지하지 않습니다. 문헌들은 심혈관 약리학의 일반적 맥락에서 검색되었으며, 예측 타당성을 부정하는 간접 근거로 해석됩니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
Digoxin의 Na⁺/K⁺-ATPase 억제 기전은 세포 내 Ca²⁺를 상승시켜 혈관 평활근 수축을 촉진하므로, 관상동맥 혈관경련을 기전으로 하는 변이형 협심증에 오히려 유해하게 작용할 가능성이 있습니다. 임상시험 근거는 전무하며, 기전적 분석 결과는 재창출 타당성을 지지하지 않습니다.

**진행하려면 필요한 것:**
- DrugBank API를 통한 공식 MOA 데이터 확인 (DG002 해소)
- 변이형 협심증 환자에서의 Digoxin 부작용 사례 보고 체계적 검색
- 전임상(세포/동물) 수준에서 Ca²⁺ 과부하와 혈관경련 악화 여부 검증

---

> **📋 예측 전체 요약 (6개 적응증)**

| 순위 | 적응증 | 점수 | 근거 수준 | 결정 | 기각 이유 |
|------|--------|------|----------|------|---------|
| 1 | Prinzmetal angina | 99.81% | L4 | **Hold** | 기전적 위해 가능성 (Ca²⁺ 상승 → 혈관경련 악화) |
| 2 | Duodenal obstruction | 99.70% | L5 | **Hold** | 기계적 폐색에 약물 蠕動 조절 무효 |
| 3 | Duodenal ulcer | 99.59% | L5 | **Hold** | 억산 기전 없음; Digoxin GI 독성이 潰瘍 증상 모방 (부정적 근거) |
| 4 | Duodenogastric reflux | 99.53% | L5 | **Hold** | 근거 없음; GI 독성과 증상 혼용 위험 극대 |
| 5 | Ischemic stroke susceptibility | 99.29% | L5 | **Hold** | 폐기된 온톨로지 용어(obsolete); 독립 신경보호 기전 없음 |
| 6 | Hypoalphalipoproteinemia | 99.20% | L5 | **Hold** | Na⁺/K⁺-ATPase 억제와 HDL 대사 경로 간 교집합 없음 |

> **종합 평가**: 이번 Evidence Pack의 6개 예측 적응증은 모두 **기각(Hold)** 권고이며, 일부는 기전적으로 위해 가능성까지 존재합니다. 높은 TxGNN 예측 점수(99.2–99.8%)에도 불구하고, 이는 지식 그래프(KG) 내 공병(comorbidity) 경로를 통한 **간접 연결 artifacts**일 가능성이 높습니다. Digoxin의 기존 적응증(심부전, 심방세동)에서 파생된 KG 연결이 인접 질환으로 전파된 것으로 판단됩니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

