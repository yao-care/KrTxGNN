---
layout: default
title: Telmisartan
parent: 僅模型預測 (L5)
nav_order: 662
evidence_level: L5
indication_count: 10
---

# Telmisartan
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

# Telmisartan: 고혈압에서 뇌졸중(Stroke)으로

## 한 문장 요약

Telmisartan은 안지오텐신 II 수용체 차단제(ARB) 계열의 항고혈압제로, 원래 고혈압 치료에 사용되었습니다.
TxGNN 모델은 **뇌졸중(Stroke Disorder)**에 효과가 있을 수 있다고 예측하며,
현재 **27건 이상의 임상시험**과 **20편의 문헌**(ONTARGET·TRANSCEND·PRoFESS 등 대형 RCT 포함)이 이 방향을 지지합니다.
다만 뇌졸중 재발 방지를 직접 검증한 PRoFESS 시험은 유의한 우월성을 보이지 못해, 신중한 해석이 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 고혈압(본태성 고혈압) — 국내 허가 자료 없음 |
| 예측 신규 적응증 | 뇌졸중 (Stroke Disorder) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L1 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

DrugBank의 공식 작용기전(MOA) 데이터는 현재 확인되지 않았습니다(작용기전 데이터 갭). 다만 확보된 임상·전임상 문헌에 따르면, Telmisartan은 안지오텐신 II 1형 수용체(AT1)를 차단하는 ARB이면서 동시에 PPAR-γ 부분 효능제(partial agonist) 활성을 가진 독특한 약물입니다. 이 이중 기전으로 혈압을 낮추는 것 외에도 항염증·항산화·혈관내피 보호 등 pleiotropic 효과를 나타내는 것으로 보고됩니다.

고혈압은 뇌졸중의 대표적 위험 인자이며, 여러 동물 뇌중동맥폐색(MCAO) 모델에서 telmisartan이 경색 부피를 줄이고 산화 스트레스·신경염증을 억제하는 신경보호 효과를 보였습니다. 실제로 telmisartan은 ONTARGET(n=31,546), TRANSCEND, PRoFESS(n=20,332) 등 대규모 심뇌혈관 결과 시험에서 뇌졸중을 포함한 심혈관 복합 종점으로 광범위하게 평가된 바 있어, 임상적 타당성이 이미 상당 부분 검증된 약물입니다.

다만 PRoFESS 시험은 재발 뇌졸중 예방에서 telmisartan이 위약 대비 통계적으로 유의한 우월성을 보이지 못한 중립적(neutral) 결과를 냈습니다. 이는 "혈압 조절을 통한 뇌졸중 위험 감소"라는 기전적 타당성과, "재발 방지의 임상적 효과 입증"이라는 실제 결과 사이에 간극이 있음을 의미하며, 적응증 확대를 검토할 때 반드시 고려해야 할 지점입니다. 참고로 TxGNN은 동일 약물에 대해 뇌혈관질환(cerebrovascular disorder), 뇌경색(cerebral infarction), 뇌동맥폐색(cerebral artery occlusion) 등 관련 진단명도 유사하게 높은 점수로 예측하고 있어, 이 신호가 개별 우연이 아닌 일관된 기전적 연관성을 반영함을 시사합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00153101](https://clinicaltrials.gov/study/NCT00153101) | Phase 4 | 완료 | 31,546 | ONTARGET/TRANSCEND — telmisartan 단독 및 ramipril 병용이 CV사망·심근경색·뇌졸중·심부전 입원의 복합 종점에 미치는 영향 평가 |
| [NCT00153062](https://clinicaltrials.gov/study/NCT00153062) | Phase 4 | 완료 | 20,332 | PRoFESS — 재발 뇌졸중 환자에서 telmisartan vs 위약의 2차 예방 효과 비교(배경 항고혈압 치료 병행) |
| [NCT04354376](https://clinicaltrials.gov/study/NCT04354376) | N/A | 완료 | 40,048 | TRANSCEND 시험을 실사용 의료청구 데이터로 재현한 연구 |
| [NCT00316095](https://clinicaltrials.gov/study/NCT00316095) | Phase 3 | 완료 | 1,695 | Telmisartan(20/80mg)과 simvastatin 병용 대비 단독요법의 고혈압·이상지질혈증 치료 효과 비교 |
| [NCT01011660](https://clinicaltrials.gov/study/NCT01011660) | Phase 4 | 불명 | 13,542 | 고심혈관위험 고혈압 환자에서 ARB vs 이뇨제의 심·뇌혈관 사건 감소 전략 비교 |
| [NCT00741585](https://clinicaltrials.gov/study/NCT00741585) | Phase 4 | 완료 | 21,983 | HYGIA 연구 — 활동혈압 모니터링 및 투여 시간(chronotherapy)이 심혈관·뇌혈관·대사·신장 위험에 미치는 영향 |
| [NCT01198496](https://clinicaltrials.gov/study/NCT01198496) | Phase 4 | 불명 | 5,000 | 뇌졸중 병력이 있는 본태성 고혈압 환자에서 강화 혈압관리가 재발 뇌졸중 예방에 유용한지 평가 |
| [NCT00153023](https://clinicaltrials.gov/study/NCT00153023) | Phase 4 | 완료 | 885 | VIVALDI — 제2형 당뇨성 신증 고혈압 환자에서 telmisartan 80mg vs valsartan 160mg 비교 |
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Phase 3 | 완료 | 1,671 | TRIDENT 하위연구 — 뇌출혈 병력 환자에서 강화 혈압관리(Triple Pill)의 재발 뇌졸중 예방 효과 |
| [NCT03006341](https://clinicaltrials.gov/study/NCT03006341) | N/A | 완료 | 140,187 | EMR 기반 뇌졸중 고위험 비판막성 심방세동 환자의 경구항응고제 선택 예측인자 검증 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [18378520](https://pubmed.ncbi.nlm.nih.gov/18378520/) | 2008 | RCT | N Engl J Med | ONTARGET — 혈관질환/고위험 당뇨 환자에서 ramipril, telmisartan, 병용요법의 심혈관 사건(뇌졸중 포함) 비교 |
| [19797187](https://pubmed.ncbi.nlm.nih.gov/19797187/) | 2009 | RCT 하위분석 | Stroke | PRoFESS 하위분석 — 급성 경증 허혈성 뇌졸중 환자에서 telmisartan의 기능적 예후·재발·혈압에 대한 영향 |
| [22115399](https://pubmed.ncbi.nlm.nih.gov/22115399/) | 2011 | Review | Expert Rev Clin Pharmacol | Telmisartan의 심혈관 질병·사망률 감소 효과 종합 리뷰 |
| [17845921](https://pubmed.ncbi.nlm.nih.gov/17845921/) | 2007 | Cohort | J Stroke Cerebrovasc Dis | 허혈성 뇌졸중 환자에서 losartan·telmisartan의 항혈소판 효과 비교 |
| [40536710](https://pubmed.ncbi.nlm.nih.gov/40536710/) | 2025 | Review | Pharmacol Rep | 중추신경계 질환에서 telmisartan의 응용 — AT1R 차단 및 PPAR-γ 활성화 이중 기전 정리 |
| [24065095](https://pubmed.ncbi.nlm.nih.gov/24065095/) | 2013 | Review | Int J Mol Sci | ARB(telmisartan·irbesartan·candesartan)의 HMGB1/RAGE 축 억제를 통한 뇌졸중 예방·급성기 치료 가능성 |
| [19587553](https://pubmed.ncbi.nlm.nih.gov/19587553/) | 2009 | Review | J Hypertens Suppl | PRoFESS·ONTARGET·TRANSCEND 시험 프로그램을 통한 뇌졸중 예방 전략 개관 |
| [12781906](https://pubmed.ncbi.nlm.nih.gov/12781906/) | 2003 | 배경/설계 논문 | Am J Cardiol | ONTARGET 프로그램의 배경 및 AT1 수용체 경로의 병리적 역할 |
| [21152242](https://pubmed.ncbi.nlm.nih.gov/21152242/) | 2010 | Review | Clin Interv Aging | 고령 고혈압 환자에서 telmisartan 단독/병용요법의 혈압 및 혈관 위험 조절 효과 |
| [34280191](https://pubmed.ncbi.nlm.nih.gov/34280191/) | 2021 | Cohort | PLoS Medicine | 제2형 당뇨 합병 고혈압 환자 대상 인구기반 코호트 — telmisartan 사용과 치매 위험의 연관성 |

---

## 한국 시판 정보

현재 한국 내 시판 허가 정보가 확인되지 않습니다 (시판 상태: **미출시**, 허가증 0건).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
Telmisartan-뇌졸중 연관성은 ONTARGET·TRANSCEND·PRoFESS 등 대형 Phase 3/4 RCT와 다수의 전임상 신경보호 기전 연구로 뒷받침되어 근거 수준 L1에 해당합니다. 그러나 재발 뇌졸중 예방을 직접 검증한 PRoFESS 시험이 위약 대비 유의한 우월성을 보이지 못한 중립적 결과였으므로, "적응증 확대"보다는 "기존 항고혈압 치료를 통한 뇌졸중 위험 관리 근거 보강" 수준으로 신중하게 접근해야 합니다.

**진행하려면 필요한 것:**
- DrugBank 등 공식 소스를 통한 작용기전(MOA) 데이터 확보 (현재 데이터 갭)
- 한국 MFDS 허가사항(경고·금기·상호작용) 확보 — 현재 전혀 없음 (Blocking 데이터 갭)
- PRoFESS 등 중립적 결과 시험에 대한 하위군 분석(용량, 병용요법별) 추가 검토
- 뇌졸중 1차/2차 예방 목적의 국내·아시아인 대상 임상 데이터 확인
- 한국 내 시판 여부 및 도입 가능성에 대한 규제 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

