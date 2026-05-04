---
layout: default
title: Salbutamol
parent: 僅模型預測 (L5)
nav_order: 301
evidence_level: L5
indication_count: 10
---

# Salbutamol
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

# Salbutamol: 기관지 천식에서 유두성 결막염으로

## 한 문장 요약

Salbutamol은 β₂ 아드레날린 수용체를 선택적으로 자극하여 기관지 평활근을 이완시키는 속효성 기관지확장제로, 기관지 천식 및 기관지경련 치료의 전 세계 표준 약제입니다. TxGNN 모델은 **유두성 결막염(Papillary Conjunctivitis)**을 최우선 신규 적응증으로 예측하였으며, 기관지염·과민반응·폐쇄성 폐질환 등 총 10가지 적응증에 대한 재창출 가능성을 제시합니다. 현재 **기관지염(임상시험 50건 이상, L2)** 및 **폐쇄성 폐질환(임상시험 50건 이상, L1)**에서 강력한 근거가 확인되나, 최상위 예측 적응증인 유두성 결막염에 대한 임상 근거는 전무합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (한국 미허가) |
| 예측 신규 적응증 | 유두성 결막염 (Papillary Conjunctivitis) |
| TxGNN 예측 점수 | 99.9964% |
| 근거 수준 | L5 (임상 근거 없음) |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Salbutamol은 기관지 평활근 내 β₂ 아드레날린 수용체에 결합하여 adenylyl cyclase를 활성화하고 세포 내 cAMP를 증가시켜 평활근 이완을 유도합니다. 흡입 후 수 분 이내에 기관지 확장 효과가 나타나며, 천식과 COPD에서 구조(rescue) 약물로 수십 년간 광범위하게 사용되어 왔습니다. 현재 DrugBank API를 통한 상세 작용 기전 데이터는 미수집 상태입니다.

유두성 결막염(Giant Papillary Conjunctivitis, GPC)은 콘택트렌즈·봉합사 등의 기계적 자극 또는 알레르기 반응에 의해 결막 비만세포와 호산구가 활성화되는 염증 질환입니다. β₂ 수용체는 기관지 외에도 비만세포 표면에 분포하며, β₂ 작용제가 비만세포 탈과립을 억제한다는 전임상 근거가 일부 존재합니다. 이 기전이 이론적으로 유두성 결막염에 적용될 수 있으나, 이 특정 적응증에 대한 전임상 또는 임상 연구는 현재 전혀 보고되지 않았습니다.

TxGNN의 높은 예측 점수(99.9964%)는 Salbutamol의 β₂ 기전과 알레르기 매개 질환 사이의 지식 그래프(Knowledge Graph) 내 간접적 연결성에서 기인한 것으로 판단되며, 직접적인 치료 효능의 근거로 해석하기 어렵습니다. 보다 유망한 재창출 후보는 **과민반응(아나필락시스 동반 기관지경련, L3)**과 **아토피성 결막염(동물 연구 근거, L4)**이며, 기관지염과 폐쇄성 폐질환은 Salbutamol의 기존 적응증과 직접 연관된 영역입니다.

---

## 전체 예측 적응증 요약

| 순위 | 적응증 | TxGNN 점수 | 근거 수준 | 권장 결정 |
|------|--------|-----------|---------|---------|
| 1 | 유두성 결막염 (Papillary Conjunctivitis) | 99.9964% | L5 | Hold |
| 2 | 비강 질환 (Nasal Cavity Disease) | 99.9945% | L4 | Hold |
| 3 | 인두염 (Pharyngitis) | 99.9944% | L4 | Hold |
| 4 | 기관지염 (Bronchitis) | 99.9920% | **L2** | Proceed with Guardrails |
| 5 | 급성 후두인두염 (Acute Laryngopharyngitis) | 99.9915% | L5 | Hold |
| 6 | 과민반응 (Anaphylaxis) | 99.9632% | **L3** | Research Question |
| 7 | 감기 (Common Cold) | 99.9541% | **L3** | Research Question |
| 8 | 아토피성 결막염 (Atopic Conjunctivitis) | 99.9462% | L4 | Research Question |
| 9 | 항문직장 협착 (Anorectal Stricture) | 99.9450% | L5 | Hold |
| 10 | 폐쇄성 폐질환 (Obstructive Lung Disease) | 99.9448% | **L1** | Proceed with Guardrails |

---

## 임상시험 근거

### 유두성 결막염 (Rank 1 — 최우선 예측)

현재 관련 임상시험 등록이 없습니다.

---

### 기관지염 (Rank 4)

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02233985](https://clinicaltrials.gov/study/NCT02233985) | Phase 4 | 완료 | 64 | 소아 중등도~중증 급성 기관지염에서 Salbutamol/3% 고장 생리식염수 병용의 호흡 곤란 완화 효능 직접 평가 |
| [NCT00114478](https://clinicaltrials.gov/study/NCT00114478) | N/A | 미상 | 600 | 기관지염에서 에피네프린 vs 알부테롤(Salbutamol) 무작위 대조 시험 |
| [NCT01112241](https://clinicaltrials.gov/study/NCT01112241) | Phase 4 | 완료 | 17 | 조혈모세포이식 후 폐쇄성 세기관지염에서 Salbutamol 급성 기관지확장 반응 평가 |
| [NCT00667797](https://clinicaltrials.gov/study/NCT00667797) | Phase 4 | 완료 | 486 | 천식·COPD 입원 환자에서 레발부테롤 vs 알부테롤(Salbutamol) 약물경제학적 결과 비교 (n=486) |
| [NCT00696540](https://clinicaltrials.gov/study/NCT00696540) | Phase 2 | 미상 | 74 | RSV 유행기 기관지염 외래 소아에서 Salbutamol 3% 고장/0.9% 등장 생리식염수 희석액 비교 |
| [NCT01065272](https://clinicaltrials.gov/study/NCT01065272) | Phase 1 | 완료 | 200 | 아토피·천식 가족력 있는 기관지염 소아에서 덱사메타손+Salbutamol vs 위약, 임상 중증도 점수 평가 |
| [NCT01238445](https://clinicaltrials.gov/study/NCT01238445) | N/A | 완료 | 29 | 기관지염에서 알부테롤 반응성 평가: 개인별 반응자 선별 기법 연구 |
| [NCT03199976](https://clinicaltrials.gov/study/NCT03199976) | Phase 4 | 조기 종료 | 80 | 영·유아 반복 천명에서 간헐적 티오트로피움+Salbutamol vs 플루티카손+Salbutamol 비교 |
| [NCT02760719](https://clinicaltrials.gov/study/NCT02760719) | Phase 2 | 조기 종료 | 100 | 입원 소아 급성 바이러스성 기관지염에서 Salbutamol+고장 생리식염수 vs 표준 지지 요법 비교 |
| [NCT03900494](https://clinicaltrials.gov/study/NCT03900494) | N/A | 완료 | 80 | 급성 기관지 폐쇄 영·유아에서 Salbutamol 투여 시 두 종류 공간형 기구(VHC) 효능 비교 |

---

### 과민반응 (Rank 6)

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT05653024](https://clinicaltrials.gov/study/NCT05653024) | Phase 3 | 조기 종료 | 24 | 식품 알레르기 반응 시 급성 복통에 대한 흡입용 Salbutamol 효능 평가 — 유일한 직접 RCT이나 조기 종료(n=24)로 결론 미확정 |
| [NCT03918772](https://clinicaltrials.gov/study/NCT03918772) | N/A | 완료 | 153 | 수술 전후 즉시형 과민반응의 임상 결정인자 분석: Salbutamol을 구조 약물로 포함 |
| [NCT04207840](https://clinicaltrials.gov/study/NCT04207840) | Phase 4 | 완료 | 28 | 흡입성 에피네프린 vs 알부테롤(ProAir) 전신 노출 약동학 비교 (과민반응 맥락) |

---

### 폐쇄성 폐질환 (Rank 10)

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01096017](https://clinicaltrials.gov/study/NCT01096017) | Phase 3 | 완료 | 24 | 일본 성인 천식(폐쇄성 폐질환) 환자에서 Salbutamol pMDI vs 테르부탈린 Turbuhaler 직접 동등성 비교 |
| [NCT02427165](https://clinicaltrials.gov/study/NCT02427165) | Phase 2 | 완료 | 29 | 만성 천식에서 신약 RPL554(7용량 교차) vs Salbutamol 폐기능 비교 |
| [NCT02170532](https://clinicaltrials.gov/study/NCT02170532) | Phase 4 | 완료 | 10 | 폐쇄성 기도 질환에서 알부테롤 이성질체 흡입 요법 및 신형 분무 기구의 소기도 개방 효과 평가 |
| [NCT00523991](https://clinicaltrials.gov/study/NCT00523991) | Phase 4 | 완료 | 457 | 유지 치료 미경험 COPD에서 티오트로피움 + PRN Salbutamol vs 위약 + PRN Salbutamol 24주 비교 |
| [NCT01274325](https://clinicaltrials.gov/study/NCT01274325) | Phase 3 | 완료 | 51 | 천식에서 Seroflo 125 vs Seretide 125의 기도 항염증 효과 비교 (Salbutamol 구조 약물 포함) |

---

## 문헌 근거

### 유두성 결막염 (Rank 1)

현재 관련 문헌이 없습니다.

---

### 과민반응 (Rank 6)

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [26918144](https://pubmed.ncbi.nlm.nih.gov/26918144/) | 2015 | Review | F1000Research | 과민반응 종합 관리 리뷰: β₂ 작용제를 기관지경련 보조 치료로 포함하여 권고 |
| [34366098](https://pubmed.ncbi.nlm.nih.gov/34366098/) | 2021 | Case Series | JACI In Practice | "낡은 약의 새 역할": 위장관 과민반응 복통에서 Salbutamol의 GI 평활근 이완 기전 가설 제시 |
| [19092569](https://pubmed.ncbi.nlm.nih.gov/19092569/) | 2008 | Review | Pediatr Emerg Care | 소아 과민반응 관리 지침: 에피네프린 투여 후 β₂ 작용제를 기관지경련 보조 치료로 강력 권고 |
| [29351501](https://pubmed.ncbi.nlm.nih.gov/29351501/) | 2018 | Observational | Prehospital Emerg Care | 소아 과민반응 원외 처치에서 알부테롤과 에피네프린 투여 패턴 분석 |
| [115530](https://pubmed.ncbi.nlm.nih.gov/115530/) | 1979 | Animal Study | Br J Pharmacol | Salbutamol이 쥐 피부·복막 수동 과민반응 억제 및 폐 SRS-A(류코트리엔 전구체) 분비 감소 확인 |
| [18447148](https://pubmed.ncbi.nlm.nih.gov/18447148/) | 2008 | Case Report | J Investig Allergol | Salbutamol 자체에 의한 아나필락시스 사례 — 역설적 안전성 위험, 과민반응 적응증 검토 시 특별 유의 필요 |

---

### 아토피성 결막염 (Rank 8)

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [3666475](https://pubmed.ncbi.nlm.nih.gov/3666475/) | 1987 | Animal Study | Graefe's Arch Clin Exp Ophthalmol | 국소 Salbutamol 0.1%이 기니피그 즉시형 알레르기성 결막염 98% 억제; β 차단제 전처치 시 효과 완전 소실로 β₂ 기전 확인 |
| [2906082](https://pubmed.ncbi.nlm.nih.gov/2906082/) | 1985 | Preclinical | J Ocular Pharmacol | β₂ 작용제 국소 투여가 결막 후모세혈관 내피세포 수축 억제 → 혈관 투과성 감소 → 항염증 효과 가능성 확인 |

---

### 폐쇄성 폐질환 (Rank 10)

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [34816917](https://pubmed.ncbi.nlm.nih.gov/34816917/) | 2021 | RCT | Rev Assoc Med Bras | COPD 급성 악화에서 독소필린+Salbutamol 병용이 단독 치료 대비 폐기능 유의하게 개선 |
| [1729064](https://pubmed.ncbi.nlm.nih.gov/1729064/) | 1992 | RCT | Chest | 비가역성 COPD(n=12)에서 Salbutamol이 테오필린과 동등한 FEV1 개선 효과 (이중 맹검 4-arm 교차 연구) |
| [30580341](https://pubmed.ncbi.nlm.nih.gov/30580341/) | 2017 | Observational | KUMJ | 혼합성(폐쇄+제한) 폐기능 장애 환자에서 Salbutamol 기관지확장 가역성 검사의 임상적 유용성 평가 |
| [15293593](https://pubmed.ncbi.nlm.nih.gov/15293593/) | 2004 | Review | JAOA | 천식·COPD에서 레발부테롤(Salbutamol R-이성질체) 치료 효능 및 부작용 감소 가능성 종합 검토 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold (최우선 예측 적응증: 유두성 결막염)**

**사유:**
TxGNN이 가장 높은 점수(99.9964%)로 예측한 유두성 결막염은 임상시험 및 문헌 근거가 전혀 없어(L5) 현재 단계에서 개발 진행을 권장하기 어렵습니다. 본 다중 적응증 평가에서 진정한 재창출 관심 후보는 **과민반응(L3, Research Question)**이며, 기관지염(L2)과 폐쇄성 폐질환(L1)은 사실상 Salbutamol의 기존 적응증 영역에 해당합니다.

**진행하려면 필요한 것:**
- Salbutamol DrugBank ID 및 MOA 데이터 보완 (DrugBank API 조회)
- 유두성 결막염 전임상 연구(동물 모델) 기획 여부 검토
- 과민반응 직접 RCT(NCT05653024) 조기 종료 원인 및 중간 데이터 확인
- 아토피성 결막염 적응증: 국소 β₂ 작용제 안약(0.1% Salbutamol 점안제) 신규 개발 타당성 탐색
- 한국 MFDS 허가 경로 사전 검토 (현재 한국 미허가 약물)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

