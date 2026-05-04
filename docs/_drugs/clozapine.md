---
layout: default
title: Clozapine
parent: 僅模型預測 (L5)
nav_order: 183
evidence_level: L5
indication_count: 10
---

# Clozapine
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

# CLOZAPINE: 치료저항성 조현병에서 양극성 조증 장애로

## 한 문장 요약

Clozapine은 기존 항정신병약에 반응하지 않는 치료저항성 조현병 환자를 위해 전 세계적으로 사용되는 비정형 항정신병약으로, 독보적인 항자살 효과로도 잘 알려져 있습니다. TxGNN 모델은 **양극성 조증 장애(Manic Bipolar Affective Disorder)**를 가장 유망한 신규 적응증으로 예측하며(예측 점수 99.95%), 현재 **6건의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다. 한국 내 시판 이력이 전무한 상태로, 임상 도입 전 허가 경로 확보가 선행되어야 합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 치료저항성 조현병 (한국 허가 없음, 글로벌 승인 기반) |
| 예측 신규 적응증 | 양극성 조증 장애 (Manic Bipolar Affective Disorder) |
| TxGNN 예측 점수 | 99.95% |
| 근거 수준 | L2 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, Clozapine은 비정형 항정신병약(atypical antipsychotic)으로서 도파민 D1-D4 수용체, 세로토닌 5-HT2A/2C 수용체, 무스카린 M1-M5 수용체, 히스타민 H1 수용체, 아드레날린 α1/α2 수용체 등에 광범위하게 작용합니다. 다른 항정신병약과 달리 D2 친화력이 상대적으로 낮은 대신 D4 및 5-HT2A에 강한 친화력을 보이며, 이 독특한 다수용체 프로파일이 다른 약제에 반응하지 않는 환자에서의 우월한 효능을 설명합니다.

조현병과 양극성 조증 장애는 도파민 과활성이라는 공통 병태생리를 공유합니다. Clozapine의 D2/D4 차단 작용은 조증 발작기의 충동 행동을 억제할 수 있으며, 5-HT2C 차단은 기분 안정 효과를 추가적으로 제공합니다. 광범위한 다수용체 차단 패턴은 리튬(lithium) 및 발프로에이트(valproate)와의 병용 시 상호 보완적인 기분 안정 시너지를 기대할 수 있습니다. 또한 FDA가 별도로 승인한 항자살 효과는 자살 위험이 25배 이상 높은 양극성 장애 환자군에 특히 의미 있는 임상적 가치를 제공합니다.

기전적 근거는 실제 임상 데이터로 뒷받침됩니다. 2020년 체계적 문헌고찰·메타분석(PMID 32182485)과 2015년 체계적 문헌고찰(PMID 25346322)은 치료저항성 양극성 장애에서 Clozapine의 효능을 지지하며, 완료된 Phase 2 이중맹검 RCT(NCT00029458)는 조증 발작기에 대한 가장 직접적인 대조군 근거를 제공합니다. 현재 1,254명 규모의 대형 Phase 3 RCT가 진행 중으로 향후 더 강력한 근거가 확보될 것으로 기대됩니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00029458](https://clinicaltrials.gov/study/NCT00029458) | Phase 2 | 완료 | 42 | 치료저항성 조증(양극성 장애 조증기)에서 Clozapine 효능·안전성을 평가한 이중맹검 RCT. 본 적응증에 대한 가장 직접적인 대조군 증거 |
| [NCT05603104](https://clinicaltrials.gov/study/NCT05603104) | Phase 3 | 모집 중 | 1,254 | 조현병·양극성 우울증·주요 우울증 환자의 1차 치료 실패 후 강화 약물치료 효과를 비교하는 대규모 RCT |
| [NCT07047651](https://clinicaltrials.gov/study/NCT07047651) | Phase 4 | 모집 중 | 40 | 치료저항성 양극성 장애 환자 대상 회복 지향 프로그램(RECOVERYTRSBDGR)과 약물병합 요법의 효과 평가 |
| [NCT06993662](https://clinicaltrials.gov/study/NCT06993662) | Phase 1 | 모집 종료(진행 중) | 107 | 정신병성·정동 장애 환자에서 약물치료와 개인 인지행동치료(CBT) 병합 요법 평가 |
| [NCT03651674](https://clinicaltrials.gov/study/NCT03651674) | N/A | 불명 | 200 | ECT가 조현병·양극성 장애 환자의 뇌 구조·기능 변화에 미치는 영향을 추적한 MRI 종단 연구 |
| [NCT07398365](https://clinicaltrials.gov/study/NCT07398365) | N/A | 모집 중 | 100 | NHS 성인 정신과 입원환자의 의학적·정신과적 표현형을 특성화하는 관찰 연구 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [32182485](https://pubmed.ncbi.nlm.nih.gov/32182485/) | 2020 | Systematic Review & Meta-analysis | J Psychiatric Research | 양극성 장애에서 Clozapine의 임상 효능 및 부작용 프로파일을 체계적으로 평가 |
| [25346322](https://pubmed.ncbi.nlm.nih.gov/25346322/) | 2015 | Systematic Review | Bipolar Disorders | 치료저항성 양극성 장애에서 Clozapine의 효능·안전성에 대한 체계적 문헌고찰 |
| [33719158](https://pubmed.ncbi.nlm.nih.gov/33719158/) | 2021 | Narrative Review | Bipolar Disorders | 양극성 장애에서 Clozapine에 대해 현재까지 알려진 근거와 향후 연구 방향 검토 |
| [31488793](https://pubmed.ncbi.nlm.nih.gov/31488793/) | 2019 | Clinical Review | Psychiatria Danubina | 양극성 장애 자살 위험에서 Clozapine의 항자살 효과 가능성: 독특한 약리학적 특성 및 항충동 효과 검토 |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Clinical Guideline Review | Acta Psychiatrica Scandinavica | 양극성 조증 치료 근거 기반 가이드라인: 기분안정제 및 항정신병약 선택에 대한 제안 |
| [40174308](https://pubmed.ncbi.nlm.nih.gov/40174308/) | 2025 | Retrospective Cohort | J Psychiatric Research | **한국** 전국 건강보험 데이터를 활용한 Clozapine·리튬·발프로에이트의 조현병·양극성 장애 환자에서 항자살 효과 비교 |
| [37068038](https://pubmed.ncbi.nlm.nih.gov/37068038/) | 2023 | Cross-sectional Cohort | J Clinical Psychopharmacology | 아시아 정신과 약물 처방 패턴 컨소시엄의 양극성 장애에서 Clozapine 사용 분석 (한국·대만 포함) |
| [16432528](https://pubmed.ncbi.nlm.nih.gov/16432528/) | 2006 | Review | Molecular Psychiatry | 치료저항성 양극성 장애: 급성 조증·우울·유지 치료 모두에서 불충분한 반응 현황 및 옵션 포괄적 검토 |
| [11280956](https://pubmed.ncbi.nlm.nih.gov/11280956/) | 2001 | Review | Bulletin of the Menninger Clinic | 치료저항성 양극성 장애에서 Clozapine을 포함한 신규 약물치료 옵션 검토 |
| [10682225](https://pubmed.ncbi.nlm.nih.gov/10682225/) | 2000 | Case Series Review | Clinical Neuropharmacology | 36명 환자에서 ECT+Clozapine 병합 치료 리뷰: 67% 호전, 대체로 안전하고 내약성 양호 |

---

## 한국 시판 정보

현재 Clozapine은 한국 내 시판 허가 이력이 없습니다 (허가증 0건). 임상 도입을 위해서는 식품의약품안전처(MFDS)를 통한 신규 품목 허가 신청이 필요하며, 희귀·난치성 정신질환 치료제로의 지정 가능성도 검토할 수 있습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
완료된 Phase 2 이중맹검 RCT(NCT00029458, n=42)와 2건의 체계적 문헌고찰이 치료저항성 양극성 조증에서 Clozapine의 유효성을 지지하며 L2 수준 근거가 확보되어 있습니다. 대규모 Phase 3 RCT(NCT05603104, n=1,254)가 현재 진행 중으로 근거 수준의 추가 상향이 기대됩니다. 단, Clozapine은 무과립구증 등 심각한 부작용 위험이 있어 엄격한 혈액 모니터링 체계가 반드시 수반되어야 합니다.

**진행하려면 필요한 것:**
- MFDS 허가사항 원문 확보 및 안전성 프로파일 완성 (DG001 해소: 무과립구증 모니터링 계획 수립 필수)
- 상세 작용 기전(MOA) 데이터 보완 (DG002 해소: DrugBank API 조회)
- 한국 내 허가 경로 확정 (신규 품목허가 또는 희귀의약품 지정)
- REMS(Risk Evaluation and Mitigation Strategy) 준용 혈액 모니터링 프로토콜 확립
- 진행 중인 Phase 3 RCT(NCT05603104) 결과 모니터링

---

## 다중 적응증 요약

본 Evidence Pack(TW-DB00363-multi)은 Clozapine에 대한 TxGNN 상위 10개 예측 적응증을 포함합니다. 아래 표는 전체 예측 결과를 요약합니다.

| 순위 | 적응증 | TxGNN 점수 | 근거 수준 | 임상시험 | 문헌 | 권장 결정 |
|-----|-------|:----------:|:-------:|:-------:|:---:|---------|
| 1 | 양극성 조증 장애 | 99.95% | L2 | 6건 | 20편 | Proceed with Guardrails |
| 2 | 뚜렛 증후군 | 99.91% | L4 | 0건 | 20편 | Research Question |
| 3 | 발모벽 | 99.90% | L5 | 0건 | 0편 | Hold |
| 4 | 정신분열증형 장애 | 99.69% | L3 | 6건 | 20편 | Proceed with Guardrails |
| **5** | **양극성 장애** | **99.62%** | **L1** | **23건** | **20편** | **Proceed with Guardrails** |
| 6 | 주요 정동 장애 | 99.48% | L3 | 14건 | 20편 | Proceed with Guardrails |
| 7 | ADHD | 99.31% | L4 | 1건 | 20편 | Hold |
| 8 | ADHD 주의력결핍형 | 99.21% | L5 | 0건 | 0편 | Hold |
| **9** | **정신병적 장애** | **99.12%** | **L1** | **50건** | **20편** | **Proceed with Guardrails** |
| 10 | Malan 과성장 증후군 | 99.02% | L5 | 0건 | 0편 | Hold |

**우선 검토 권장 순서:** 정신병적 장애(순위 9, L1) → 양극성 장애(순위 5, L1) → 양극성 조증 장애(순위 1, L2) → 정신분열증형 장애(순위 4, L3) → 주요 정동 장애(순위 6, L3)

> **참고**: 정신병적 장애(순위 9)는 Clozapine의 전 세계 핵심 승인 적응증으로, L1 수준의 가장 강력한 근거를 보유합니다. 한국 시장 도입 시 정신병적 장애(치료저항성 조현병)를 첫 번째 허가 목표 적응증으로 설정하고, 이후 양극성 장애로의 적응증 확장을 순차적으로 검토하는 전략이 효율적입니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

