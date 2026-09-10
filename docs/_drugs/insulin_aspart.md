---
layout: default
title: Insulin Aspart
parent: 僅模型預測 (L5)
nav_order: 394
evidence_level: L5
indication_count: 10
---

# Insulin Aspart
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

# Insulin Aspart: 당뇨병 치료제에서 제1형 당뇨병(기존 표준요법 근거 재확인)으로

## 한 문장 요약

Insulin Aspart(DrugBank ID: DB01306)는 속효성 인슐린 유사체로, 국제적으로 당뇨병 환자의 혈당 조절에 사용되어 온 약물입니다. TxGNN 모델은 **제1형 당뇨병(Type 1 Diabetes Mellitus)**에 효과가 있을 것으로 예측하며, 현재 **50건 이상의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다. 다만 이 예측은 새로운 적응증 발굴이라기보다 **기존 표준 치료 근거를 데이터 기반으로 재확인**한 결과에 가깝습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 당뇨병(혈당 조절) — 국내 허가 데이터 없음, 원 적응증 상세 항목은 데이터 갭 |
| 예측 신규 적응증 | 제1형 당뇨병 (Type 1 Diabetes Mellitus) |
| TxGNN 예측 점수 | 99.95% |
| 근거 수준 | L1 |
| 한국 시판 현황 | 미상시 (허가 정보 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Evidence Pack에는 구조화된 MOA(작용기전) 필드가 채워져 있지 않습니다(데이터 갭). 다만 인슐린 아스파트는 임상적으로 잘 알려진 속효성 인슐린 유사체로, 내인성 인슐린을 대체하여 말초조직의 포도당 흡수를 촉진하고 간의 포도당 신생합성을 억제함으로써 혈당을 낮추는 방식으로 작용합니다.

이번에 예측된 신규 적응증인 '제1형 당뇨병'은 사실상 인슐린 제제의 표준 적응증과 동일한 질환입니다. TxGNN 점수가 99.95%로 매우 높게 나타난 것은 지식그래프 상에서 인슐린-당뇨병 간 연결이 이미 매우 조밀하게 형성되어 있기 때문이며, 근거 데이터 자체(Evidence Pack의 rationale)도 "非典型 老藥新用 예측이 아니라 기존 임상 표준치료 근거의 재확인"이라고 명시하고 있습니다.

참고로 같은 Evidence Pack에는 permanent neonatal diabetes mellitus(순위 5위, L3, 유전자 변이로 인한 인슐린 분비 결핍이라는 기전적 근거 보유)처럼 상대적으로 더 진정한 의미의 재창출 후보도 포함되어 있어, 향후 파이프라인에서는 이러한 순위 하위 후보를 별도로 추적할 가치가 있습니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01486940](https://clinicaltrials.gov/study/NCT01486940) | Phase 3 | 완료 | 598 | T1DM 환자 대상 insulin detemir+aspart vs NPH+human soluble insulin 혈당조절 비교 |
| [NCT01513473](https://clinicaltrials.gov/study/NCT01513473) | Phase 3 | 완료 | 350 | 소아/청소년 T1DM에서 degludec vs detemir(둘 다 aspart 병용) 26주+26주 연장 안전성 비교 (BEGIN Young 1) |
| [NCT02670915](https://clinicaltrials.gov/study/NCT02670915) | Phase 3 | 완료 | 834 | 소아/청소년 T1DM에서 faster-acting aspart vs NovoRapid, degludec 병용 유효성·안전성 비교 |
| [NCT02688933](https://clinicaltrials.gov/study/NCT02688933) | Phase 4 | 완료 | 638 | T1DM 성인 대상 Toujeo(글라진 U300) vs Lantus 아침 투여 CGM 혈당조절 비교 |
| [NCT00700648](https://clinicaltrials.gov/study/NCT00700648) | N/A | 완료 | 3024 | 아시아 입원환자 대상 정맥 내 NovoRapid(인슐린 아스파트) 관찰 연구, 안전성·유효성 평가 |
| [NCT01490112](https://clinicaltrials.gov/study/NCT01490112) | N/A | 완료 | 1239 | 아시아 지역 NovoRapid 재심사용 시판 후 감시(PMS) 연구 |
| [NCT04711382](https://clinicaltrials.gov/study/NCT04711382) | N/A | 완료 | 438 | 벨기에 T1DM 환자에서 전통 식사인슐린→Fiasp 전환 실제임상 경험 |
| [NCT01134107](https://clinicaltrials.gov/study/NCT01134107) | Phase 3 | 완료 | 133 | T1DM CSII 환자에서 insulin lispro vs insulin aspart 이중맹검 교차비교 |
| [NCT00447382](https://clinicaltrials.gov/study/NCT00447382) | Phase 3 | 완료 | 330 | T1DM basal-bolus(aspart 볼루스) 환자에서 insulin detemir 신·구 생산공정 안전성 비교 |
| [NCT00046150](https://clinicaltrials.gov/study/NCT00046150) | Phase 3 | 완료 | 59 | T1DM CSII 펌프 사용 환자에서 HMR1964 vs insulin aspart 안전성 비교 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT 시험: T1DM 임신부에서 insulin degludec vs detemir(둘 다 aspart 병용) 비열등성 비교 |
| [21333580](https://pubmed.ncbi.nlm.nih.gov/21333580/) | 2011 | RCT(체계적 문헌고찰) | Diabetes Metab | T1DM/T2DM에서 속효성 insulin aspart와 사람 인슐린의 유효성·안전성 비교 |
| [41697686](https://pubmed.ncbi.nlm.nih.gov/41697686/) | 2026 | Review | JAMA | 제1형 당뇨병 개관: 자가면역 베타세포 파괴, 전 세계 840만 명 유병, 미세/대혈관 합병증 |
| [15871555](https://pubmed.ncbi.nlm.nih.gov/15871555/) | 2003 | Review | Treat Endocrinol | Insulin aspart(NovoLog/NovoRapid) 개관: T1/T2DM에서 사람 인슐린 대비 빠른 흡수 및 HbA1c 개선 |
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | Phase 3a RCT | Lancet | ONWARDS 6: T1DM basal-bolus 요법에서 주 1회 insulin icodec vs 1일 1회 degludec 비교 |
| [12215068](https://pubmed.ncbi.nlm.nih.gov/12215068/) | 2002 | Review | Drugs | Insulin aspart의 T1/T2DM 치료 사용에 대한 개관, 식후 혈당·저혈당 개선 |
| [25143741](https://pubmed.ncbi.nlm.nih.gov/25143741/) | 2014 | Review | Vasc Health Risk Manag | Insulin degludec/insulin aspart 복합제제의 T1/T2DM 치료 개관 |
| [30789066](https://pubmed.ncbi.nlm.nih.gov/30789066/) | 2019 | Review | Expert Opin Drug Metab Toxicol | T1DM에서 premix insulin(degludec/aspart) 도입 배경 및 활용 검토 |
| [18710361](https://pubmed.ncbi.nlm.nih.gov/18710361/) | 2008 | Review | Expert Opin Pharmacother | T1DM 치료에서 biphasic insulin aspart 30의 근거 기반 평가 |
| [31902063](https://pubmed.ncbi.nlm.nih.gov/31902063/) | 2020 | Narrative Review | Diabetes Ther | 성인 T1DM 인슐린 치료 전략 개관(basal-bolus, CSII 포함) |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (Evidence Pack 상 TFDA/국내 라벨 경고·금기·DDI 데이터가 모두 확보되지 않은 Blocking 등급 데이터 갭으로 표시되어 있습니다.)

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
제1형 당뇨병에 대한 인슐린 아스파트의 근거는 다수의 완료된 Phase 3 RCT(L1)로 이미 충분히 확립되어 있으나, 이는 신규 적응증 발굴이 아니라 기존 표준 치료의 데이터 기반 재확인에 해당합니다. 또한 국내 미시판 상태이며 라벨(경고·금기) 데이터가 Blocking 수준으로 결여되어 있어, 실제 진행 시 별도 안전성·허가 검토가 필요합니다.

**진행하려면 필요한 것:**
- TFDA/국내 규제기관 라벨 데이터(경고·금기·DDI) 확보 — 현재 Blocking 데이터 갭(DG001)
- 공식 MOA 문서화(DrugBank API 조회) — High 심각도 데이터 갭(DG002)
- 국내 시판 여부 및 허가 전략 검토(현재 허가 0건)
- 재창출 파이프라인 관점에서는 본 후보보다 permanent neonatal diabetes mellitus(순위 5위, L3) 등 하위 순위 후보를 별도 검토 우선순위로 고려 권장
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

