---
layout: default
title: Clonazepam
parent: 僅模型預測 (L5)
nav_order: 180
evidence_level: L5
indication_count: 3
---

# Clonazepam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Clonazepam: 뇌전증·공황장애에서 하지불안증후군으로

## 한 문장 요약

Clonazepam은 GABA-A 수용체를 활성화하는 벤조디아제핀계 약물로, 전 세계적으로 뇌전증과 공황장애 치료에 사용됩니다. TxGNN 모델은 1순위 적응증으로 **하지불안증후군(Restless Legs Syndrome, RLS)**에 효과가 있을 수 있다고 예측하며, 코크란 체계적 문헌고찰 및 AASM 임상 진료 가이드라인을 포함한 **20편의 문헌**이 이를 지지합니다. 2순위 예측인 **불면증(Insomnia)**은 12건의 임상시험과 18편의 문헌으로 더 강력한 L2 근거를 보유하고 있어 함께 검토가 필요합니다.

---

## 빠른 개요 (1순위: 하지불안증후군)

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 미허가 (글로벌 허가 기준: 뇌전증, 공황장애) |
| 예측 신규 적응증 | 하지불안증후군 (Restless Legs Syndrome) |
| TxGNN 예측 점수 | 99.65% |
| 근거 수준 | L3 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Clonazepam은 벤조디아제핀(Benzodiazepine, BZD)계 약물로, GABA-A 수용체의 벤조디아제핀 결합 부위에 결합하여 클로라이드(Cl⁻) 이온 채널 개방 빈도를 증가시킵니다. 이로 인해 신경세포가 과분극 상태가 되어 척수 및 피질하 신경원의 과도한 발화가 억제됩니다.

하지불안증후군(RLS)은 도파민·철분 경로 이상 외에 GABAergic 억제 기능 저하가 병태생리 기전으로 보고됩니다. Clonazepam의 GABA-A 증강 효과는 RLS 환자에서 수면 중 나타나는 주기성 사지운동증(Periodic Limb Movements, PLM)을 억제하고, 수면 잠복기를 단축하며 비 REM 수면 비율을 개선합니다. 단, 이는 RLS의 근본 병인(철분 결핍, 도파민 경로)에 직접 작용하는 것이 아닌 증상 조절 기전임에 유의해야 합니다.

임상 현장에서도 RLS 환자의 약 25%가 벤조디아제핀으로 치료를 받고 있으며(Walters et al., 2024), 1984년 Montagna 등의 무작위 이중맹검 교차 임상시험에서 clonazepam이 수면의 질과 하지 이상감각 개선에 유의한 효과를 보임이 확인되었습니다. 코크란 체계적 문헌고찰(2017)과 AASM 임상 진료 가이드라인(2025)에서도 RLS 치료 옵션으로 clonazepam을 명시적으로 언급하고 있습니다.

---

## 임상시험 근거

현재 하지불안증후군에 대한 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [6380197](https://pubmed.ncbi.nlm.nih.gov/6380197/) | 1984 | RCT | Acta Neurol Scand | RLS 6명 대상 무작위 이중맹검 교차 위약대조 시험; clonazepam이 수면의 질 및 하지 이상감각 개선에 유의한 효과 확인 |
| [31942156](https://pubmed.ncbi.nlm.nih.gov/31942156/) | 2019 | RCT | J Mid-Life Health | 40세 이상 여성 RLS 환자에서 clonazepam vs nortriptyline 비교; 전향적 오픈라벨 무작위 연구 |
| [28319266](https://pubmed.ncbi.nlm.nih.gov/28319266/) | 2017 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | RLS에 대한 벤조디아제핀 사용 코크란 체계적 문헌고찰; clonazepam의 근거 및 AASM 권고사항 정리 |
| [39324694](https://pubmed.ncbi.nlm.nih.gov/39324694/) | 2025 | Clinical Practice Guideline | J Clin Sleep Med | AASM 성인·소아 RLS 및 PLMD 치료 임상 진료 가이드라인 |
| [36692194](https://pubmed.ncbi.nlm.nih.gov/36692194/) | 2023 | Systematic Review + Meta-analysis | J Clin Sleep Med | RLS 환자에서 PLMS에 대한 약물 반응성 체계적 문헌고찰 및 메타분석 |
| [11313161](https://pubmed.ncbi.nlm.nih.gov/11313161/) | 2001 | Placebo-controlled Study | Eur Neuropsychopharmacol | 위약대조 수면 실험실 연구; clonazepam 1mg의 RLS/PLMD 환자 수면 및 각성 변수에 대한 급성 효과 측정 |
| [38708125](https://pubmed.ncbi.nlm.nih.gov/38708125/) | 2024 | Historical Review | Tremor Other Hyperkinetic Mov | RLS 16,694명 설문: 약 25%가 BZD 치료 중; clonazepam 관련 17편 문헌 포함 역사적 고찰 |
| [18925578](https://pubmed.ncbi.nlm.nih.gov/18925578/) | 2008 | Evidence-based Review | Mov Disord | MDS 태스크포스의 RLS 치료 근거 중심 검토; 각 약물 군의 효능 분류 체계 |
| [24363103](https://pubmed.ncbi.nlm.nih.gov/24363103/) | 2014 | Narrative Review | Neurotherapeutics | RLS 치료의 최근 변화 및 약물 분류별(도파민 작용제, BZD, 오피오이드 등) 효과 정리 |
| [17876423](https://pubmed.ncbi.nlm.nih.gov/17876423/) | 2007 | Expert Consensus | Arq Neuropsiquiatr | 브라질 RLS 연구 그룹 전문가 합의; Class I 근거 약물 분류 및 BZD 치료 위치 기술 |

---

## 추가 예측 분석: 불면증 (Insomnia, 2순위)

### 개요

| 항목 | 내용 |
|------|------|
| TxGNN 예측 점수 | 99.32% |
| 근거 수준 | L2 |
| 임상시험 수 | 12건 |
| 문헌 수 | 18편 |
| 권장 결정 | Proceed with Guardrails |

### 기전 연관성

Clonazepam은 GABA-A 수용체 활성화를 통해 대뇌 피질 각성 역치를 낮추어 수면 잠복기를 단축하고, 총 수면 시간 및 비 REM 수면 비율을 증가시킵니다. 특히 REM 수면 억제 효과는 REM 수면 행동장애(RBD) 동반 불면증의 주요 치료 기전으로 작용합니다. 긴 반감기(18~50시간)는 야간 전체 수면 유지에 유리하나, 주간 잔류 효과(daytime residual effect) 및 인지기능 저하 위험을 수반합니다.

### 주요 임상시험

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03977441](https://clinicaltrials.gov/study/NCT03977441) | Phase 4 | UNKNOWN | 240 | 파킨슨병 수면장애·우울증에서 agomelatine vs 표준치료(clonazepam 포함) 다기관 무작위 이중맹검 위약대조 연구; 결과 확인 필요 |
| [NCT03255642](https://clinicaltrials.gov/study/NCT03255642) | NA | COMPLETED | 34 | 특발성 REM 수면 행동장애에서 melatonin vs clonazepam(Rivotril) 전향적 무작위 연구; 수면다원검사 지표 평가 |
| [NCT00025740](https://clinicaltrials.gov/study/NCT00025740) | Phase 4 | COMPLETED | 78 | PTSD에서 clonazepam + paroxetine 병용 치료 Phase 4 완료 연구; 수면 증상을 주요 평가 항목에 포함 |
| [NCT04884503](https://clinicaltrials.gov/study/NCT04884503) | Phase 2 | COMPLETED | 58 | 원발성 구강작열감 증후군(BMS) 치료 평가 Phase 2 완료 연구; 수면 및 심리적 장애 포함 평가 |
| [NCT06606418](https://clinicaltrials.gov/study/NCT06606418) | NA | NOT_YET_RECRUITING | 30 | RBD에서 침술 vs clonazepam(대조군) 무작위 대조 연구; clonazepam이 활성 비교 약물로 포함 |

### 주요 문헌

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [37940498](https://pubmed.ncbi.nlm.nih.gov/37940498/) | 2024 | RCT | Clinical Therapeutics | 고령 중등도 불면증 환자에서 고용량(1mg) vs 저용량(0.5mg) clonazepam + CBT-i 효과 비교 |
| [26923575](https://pubmed.ncbi.nlm.nih.gov/26923575/) | 2015 | Cohort Study | Neurological Research | 만성 원발성 불면증 clonazepam 치료 환자 30명 대상 실행 기능(executive function) 평가 |
| [39297769](https://pubmed.ncbi.nlm.nih.gov/39297769/) | 2024 | Cross-sectional Study | Clin Neuropharmacol | 급성 및 만성 불면증 진단 환자 대상 약물 관리 현황 단면 연구 |
| [32921425](https://pubmed.ncbi.nlm.nih.gov/32921425/) | 2021 | Clinical Guideline | Rev Neurol | 프랑스 의학연구 수면학회(SFRMS)의 수면장애 치료 권고문; 신경계 질환 및 불면증 포함 |
| [39535843](https://pubmed.ncbi.nlm.nih.gov/39535843/) | 2024 | Review | Expert Opin Pharmacother | 파킨슨병 수면 장애의 약물·비약물 관리 검토; clonazepam 역할 포함 |

---

## 3순위 예측: 삼차신경 종양 (Trigeminal Nerve Neoplasm)

**근거 수준: L5 / 권장 결정: Hold**

삼차신경 종양은 구조적 병변으로, GABA-A 수용체 조절을 통한 증상 완화와 기전상 직접적인 연결이 없습니다. TxGNN 지식 그래프 내 "삼차신경 → 신경통 → BZD 치료" 경로에서 발생한 개념적 혼동으로 판단됩니다. 문헌 근거는 케이스 리포트 2편(PMID [29589986](https://pubmed.ncbi.nlm.nih.gov/29589986/), [16717232](https://pubmed.ncbi.nlm.nih.gov/16717232/))에 불과하며, 현 단계에서 추가 평가를 권고하지 않습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
하지불안증후군(L3)과 불면증(L2)에 대한 Clonazepam의 사용을 지지하는 코크란 체계적 문헌고찰, AASM 임상 진료 가이드라인, 직접적인 RCT 데이터가 존재합니다. 그러나 벤조디아제핀 특유의 의존성·내성·인지기능 저하 우려로 인해 신중한 적응증 선택, 투여 기간 제한, 사용 모니터링이 필수적입니다.

**진행하려면 필요한 것:**
- 한국 MFDS 허가사항의 경고·금기·약물상호작용 정보 수집 (현재 Data Gap — 우선 해결 필요)
- DrugBank API를 통한 작용 기전(MOA) 상세 데이터 보완
- 한국 내 Clonazepam 처방 현황 및 규제 환경(Schedule 분류 등) 파악
- 의존성·인지기능 저하 관련 장기 안전성 모니터링 계획 수립
- 고령 환자, 호흡기 질환(수면 무호흡 등) 동반 환자에서의 특별 주의사항 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

