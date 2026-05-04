---
layout: default
title: Deutetrabenazine
parent: 僅模型預測 (L5)
nav_order: 210
evidence_level: L5
indication_count: 10
---

# Deutetrabenazine
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

# Deutetrabenazine: 헌팅턴병 무도증에서 만성 틱 장애로

## 한 문장 요약

Deutetrabenazine은 소포성 모노아민 수송체 2형(VMAT2)을 선택적으로 억제하는 약물로, 미국 FDA에서 헌팅턴병 관련 무도증(chorea) 및 지연성 이상운동증(tardive dyskinesia) 치료에 승인되어 있으나 한국에는 아직 허가되지 않았습니다. TxGNN 모델은 정신성 운동장애(Psychogenic Movement Disorders)를 최상위 예측 적응증(98.73%)으로 제시하는 등 상위 10개 예측 적응증 전체가 과활동성 운동장애 스펙트럼에 속하며, 이 중 **만성 틱 장애(Chronic Tic Disorder)**에 대해 *JAMA Network Open*에 게재된 무작위 대조시험(RCT) 2건을 포함하여 **17편의 문헌**이 deutetrabenazine의 직접적인 효능을 뒷받침합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 헌팅턴병 관련 무도증, 지연성 이상운동증 (미국 FDA 승인; 한국 미허가) |
| TxGNN 예측 #1 적응증 | 정신성 운동장애 (Psychogenic Movement Disorders) — 98.73% |
| 주요 분석 적응증 | 만성 틱 장애 (Chronic Tic Disorder) — TxGNN #5, 98.31% |
| 근거 수준 | L1 (완료된 RCT 2건, *JAMA Network Open* 게재) |
| 한국 시판 현황 | ✗ 미허가 |
| 허가증 수 | 0건 |
| 권장 결정 | **Proceed with Guardrails** |

---

## 이 예측이 타당한 이유는?

Deutetrabenazine은 선조체(striatum)에서 VMAT2를 억제함으로써, 도파민을 포함한 모노아민이 시냅스 전 소포에 저장되지 못하도록 합니다. 그 결과 도파민 방출이 감소하고, 이는 과도한 불수의 운동을 유발하는 도파민계 과활성을 억제합니다. 이 기전은 헌팅턴병 무도증 및 지연성 이상운동증 치료에 이미 입증되어 있으며, 동일한 경로가 만성 틱 장애에도 적용됩니다.

만성 틱 장애, 특히 투레트 증후군(Tourette Syndrome)의 핵심 병인은 기저핵–피질–시상 회로에서의 도파민 조절 이상입니다. 도파민 수용체 차단제(항정신병약)가 틱 억제에 기존부터 사용되어 왔으나, VMAT2 억제는 수용체를 차단하지 않고 더 상류에서 도파민 공급 자체를 감소시킵니다. 이는 항정신병약 관련 추체외로 부작용(EPS)을 피하면서 동일한 도파민계를 조절할 수 있다는 기전적 장점이 있습니다.

Deutetrabenazine은 모체 약물인 테트라베나진(tetrabenazine)에 중수소(deuterium)를 도입한 유도체로, 활성 대사체의 반감기가 길어지고 최고혈중농도(Cmax)가 낮아져 하루 2회 투여가 가능하며 일부 부작용 발생률이 낮습니다. 이는 소아·청소년 틱 장애 환자에게 보다 순응도 높은 치료 옵션을 제공합니다. TxGNN 상위 10개 예측 적응증이 정신성 운동장애, 진전, 틱, 이상운동증, 추체외로 질환 등 과활동성 운동장애 스펙트럼에 집중되어 있다는 사실은 이 약물의 기전적 타당성과 완전히 일치합니다.

---

## 임상시험 근거

아래 임상시험은 deutetrabenazine의 과활동성 운동장애(추체외로 및 운동질환, TxGNN 예측 #7) 분야 근거입니다. 만성 틱 장애(TxGNN #5) 자체에 대한 ClinicalTrials.gov 등록 시험은 현재 확인되지 않았으나, 투레트 증후군 대상 RCT 결과가 문헌으로 게재되어 있습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03813238](https://clinicaltrials.gov/study/NCT03813238) | Phase 3 | 완료 (2022.07) | 63 | 소아·청소년 뇌성마비 운동이상증(DCP)에서 deutetrabenazine의 무작위 이중맹검 위약대조 효능·안전성 평가 |
| [NCT04200352](https://clinicaltrials.gov/study/NCT04200352) | Phase 3 | 종료 (2023.02) | 44 | NCT03813238 완료 후 연장: 뇌성마비 운동이상증 소아·청소년 대상 장기(55주) 안전성·유효성 개방표지 연장 연구 |
| [NCT06997198](https://clinicaltrials.gov/study/NCT06997198) | Phase 4 | 모집 예정 (2026.03~) | 25 | 지적·발달장애(IDD) 동반 성인의 지연성 이상운동증에서 deutetrabenazine 효능·안전성 평가 |

---

## 문헌 근거

아래 문헌은 만성 틱 장애(Chronic Tic Disorder, TxGNN 예측 #5)에 대한 deutetrabenazine의 직접 근거입니다. 총 17편 중 가장 관련성 높은 10편을 제시합니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [34661664](https://pubmed.ncbi.nlm.nih.gov/34661664/) | 2021 | RCT | *JAMA Network Open* | 소아·청소년 투레트 증후군 대상 고정용량 deutetrabenazine: 틱 증상 유의한 감소 및 안전성 확인 |
| [34609495](https://pubmed.ncbi.nlm.nih.gov/34609495/) | 2021 | RCT | *JAMA Network Open* | 소아·청소년 투레트 증후군 대상 유연용량 deutetrabenazine: 안전성 및 효능 평가 (무작위 대조시험) |
| [37772282](https://pubmed.ncbi.nlm.nih.gov/37772282/) | 2023 | 개방표지 연장 | *Movement Disorders Clinical Practice* | 투레트 증후군 소아·청소년 대상 deutetrabenazine 장기 사용 안전성·효능: 개방표지 연장 연구 결과 확인 |
| [37301806](https://pubmed.ncbi.nlm.nih.gov/37301806/) | 2023 | 실사용 연구 | *Journal of Neurology* | 투레트 증후군에서 VMAT2 억제제 3종(tetrabenazine, deutetrabenazine, valbenazine) 실사용 경험: 효능·이상반응·접근성 비교 분석 |
| [40489853](https://pubmed.ncbi.nlm.nih.gov/40489853/) | 2025 | 서술적 고찰 | *Medicine* | 소아·성인·고령자 투레트 증후군의 Phase III/IV 임상시험 약물 치료 현황 종합 고찰 |
| [27917309](https://pubmed.ncbi.nlm.nih.gov/27917309/) | 2016 | 파일럿 임상 | *Tremor and Other Hyperkinetic Movements* | 투레트 증후군 청소년 대상 deutetrabenazine 안전성·내약성·초기 효능 탐색: VMAT2 억제를 통한 도파민 고갈 메커니즘 확인 |
| [31955299](https://pubmed.ncbi.nlm.nih.gov/31955299/) | 2020 | 고찰 | *Journal of Neural Transmission* | 투레트 증후군 틱 치료 종합 고찰: 도파민 고갈제(deutetrabenazine 포함), 항정신병약, 알파작용제 등 치료 전략 비교 |
| [29335879](https://pubmed.ncbi.nlm.nih.gov/29335879/) | 2018 | 고찰 | *CNS Drugs* | 투레트 증후군 약물 치료 최신 접근법: VMAT2 억제제를 포함한 신규 치료 전략 검토 |
| [32454050](https://pubmed.ncbi.nlm.nih.gov/32454050/) | 2020 | 고찰 | *Pharmacology & Therapeutics* | VMAT2 억제제의 지연성 이상운동증·헌팅턴병 무도증·틱 장애 치료 역할 및 약리학적 최적화 검토 |
| [28387387](https://pubmed.ncbi.nlm.nih.gov/28387387/) | 2017 | 고찰 | *Drugs of Today* | Deutetrabenazine의 헌팅턴병·지연성 이상운동증·투레트 증후군 치료: 약동학적 특성 및 임상 데이터 종합 고찰 |

---

## 한국 시판 정보

Deutetrabenazine은 현재 한국 식품의약품안전처(MFDS)에 허가된 제품이 없습니다. 미국에서는 Teva Pharmaceuticals의 **Austedo®** (즉방형) 및 **Austedo XR®** (서방형)으로 헌팅턴병 관련 무도증 및 지연성 이상운동증 적응증으로 판매되고 있습니다. 한국 도입을 위해서는 MFDS 신약 허가 신청(NDA) 절차가 필요합니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

이 Evidence Pack에서 경고, 금기, 약물 상호작용 데이터가 수집되지 않았습니다. Deutetrabenazine 사용 시 VMAT2 억제제 계열 공통 주의사항(우울증·자살 충동 위험 증가, 졸음, QTc 연장 가능성, MAO 억제제 병용 금기)에 유의하고, 상세한 안전성 정보는 미국 FDA 승인 처방 정보(USPI, Austedo®)를 참조하시기 바랍니다.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
만성 틱 장애(투레트 증후군)에 대해 *JAMA Network Open*에 게재된 RCT 2건(2021년)과 장기 개방표지 연장 연구(2023년) 등 총 17편의 직접 문헌이 deutetrabenazine의 효능을 강하게 지지하며, 뇌성마비 운동이상증에 대한 Phase 3 완료 임상시험이 추가로 존재합니다. 그러나 한국 미허가 약물이므로 규제 전략 수립 및 안전성 데이터 확보가 선행되어야 합니다.

**진행하려면 필요한 것:**
- 한국 MFDS 신약 허가 신청(NDA) 가능성 및 규제 경로 검토
- MFDS 허가사항 경고·금기·약물 상호작용 데이터 확보 (현재 공백)
- 한국인 대상 약동학 데이터 검토 (CYP2D6 대사형 비율 등 인종별 차이 고려)
- 소아·청소년 대상 안전성 모니터링 계획 수립 (우울증, QTc 연장, 졸음 등)
- 한국 틱 장애 환자군 역학 자료 및 미충족 의료 수요 조사
- 건강보험 급여 적용 가능성 및 비용 효과성 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

