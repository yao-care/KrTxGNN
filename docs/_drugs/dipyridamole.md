---
layout: default
title: Dipyridamole
parent: 僅模型預測 (L5)
nav_order: 225
evidence_level: L5
indication_count: 10
---

# Dipyridamole
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

%; 운동 병행 시 87%로 향상 |
| [8417062](https://pubmed.ncbi.nlm.nih.gov/8417062/) | 1993 | 기타 | JACC | Dipyridamole 유발 허혈 시 심근 에코밀도 증가 관찰: 허혈의 새로운 초음파 마커 |
| [8634169](https://pubmed.ncbi.nlm.nih.gov/8634169/) | 1996 | 기타 | Rev Port Cardiol | 정상 dipyridamole-탈륨 스캔 환자의 3년 심혈관 예후 |
| [2022043](https://pubmed.ncbi.nlm.nih.gov/2022043/) | 1991 | Review | Circulation | 관상동맥 협착 비침습적 기능 평가 방법론 검토: dipyridamole 역할 및 한계 |
| [7628141](https://pubmed.ncbi.nlm.nih.gov/7628141/) | 1995 | 기타 | Clin Nucl Med | 편두통·변이형 협심증 동반 환자에서 dipyridamole 부하 시 후벽 허혈 확인 사례 |
| [2221701](https://pubmed.ncbi.nlm.nih.gov/2221701/) | 1990 | 기타 | Ann NY Acad Sci | 일과성 심근 허혈의 심전도 진단 민감도·특이도 분석 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
15편의 문헌 전체가 dipyridamole이 Prinzmetal 협심증 치료제가 아닌 관상동맥 경련 유발 도구임을 보고하며, 치료 재창출 연구는 부적합합니다.

**진행하려면 필요한 것:**
- 이 예측은 재창출 연구 대상으로 적합하지 않습니다. 진행 불가.
- Prinzmetal 협심증 환자에서의 dipyridamole 사용 위험을 의약품 안전 정보에 반영하는 것을 권장합니다.

---

## 전체 예측 적응증 요약 (10개 후보)

| 순위 | 적응증 | TxGNN 점수 | 근거 수준 | 권장 결정 | 핵심 내용 |
|------|--------|-----------|---------|---------|---------|
| 1 | Prinzmetal 협심증 | 99.99% | L4 | ⛔ Hold | 역방향 증거: 경련 유발 위험 |
| **2** | **뇌졸중 (Stroke Disorder)** | **99.95%** | **L1** | **✅ Proceed with Guardrails** | ESPS-2, ESPRIT, PRoFESS 대형 RCT |
| 3 | 혈전성 질환 | 99.94% | L3 | 🔍 Research Question | 기전 타당성 있으나 직접 RCT 부족 |
| 4 | 병적 동방 결절 증후군 2형 | 99.89% | L5 | ⛔ Hold | 잠재적 유해: 아데노신↑ → 서맥 악화 |
| **5** | **일과성 허혈 발작 (TIA)** | **99.87%** | **L1** | **✅ Proceed with Guardrails** | ESPRIT 핵심 적응증, 직접 L1 근거 |
| 6 | 육종당단백병증 | 99.82% | L5 | ⛔ Hold | 근육 구조단백 결함 — 기전적 가양성 |
| 7 | Wildervanck 증후군 | 99.78% | L5 | ⛔ Hold | 선천성 구조 기형 — 기전적 가양성 |
| 8 | 대두증-안면기형-정신운동지연 | 99.77% | L5 | ⛔ Hold | 신경발육 장애 — 기전적 가양성 |
| 9 | 횡정맥동 혈전증 | 99.72% | L5 | ⛔ Hold | 정맥혈전: 항응고 영역, 항혈소판 미적용 |
| 10 | 해면정맥동 혈전증 | 99.72% | L5 | ⛔ Hold | 감염성 정맥혈전: 항생제+항응고 표준치료 |

> **핵심 요약**: 임상적으로 가장 의미 있는 예측은 **뇌졸중(2위)**과 **TIA(5위)**로, 두 적응증 모두 복수의 대규모 Phase 3/4 RCT와 Cochrane 체계적 문헌고찰로 지지됩니다. 1순위 예측(Prinzmetal 협심증)과 4순위 예측(병적 동방 결절 증후군)은 치료 기회가 아닌 **안전성 주의 대상**입니다.

---

## 보충 보고서 A: 뇌졸중 예방 (Rank 2, L1) — Proceed with Guardrails

### 빠른 개요

| 항목 | 내용 |
|------|------|
| 예측 적응증 | 뇌졸중 (Stroke Disorder) |
| TxGNN 예측 점수 | 99.95% |
| 근거 수준 | **L1** |
| 임상시험 수 | 31건 |
| 문헌 수 | 18편 |
| 권장 결정 | **Proceed with Guardrails** |

### 예측이 타당한 이유

Dipyridamole은 ①PDE 억제(혈소판 내 cAMP/cGMP↑ → 혈소판 응집 억제)와 ②아데노신 재흡수 억제(내피 유래 NO 효과 증강, 항염증)의 이중 기전으로 뇌졸중 예방에 효과적입니다.

ESPS-2(n=6,602)에서 아스피린+서방형 dipyridamole(Aggrenox)이 아스피린 단독 대비 뇌졸중 재발을 **37% 감소**시켰으며, ESPRIT(n=2,763, Phase 4)는 복합 혈관 사건 위험을 **20% 추가 감소**시킴을 확인했습니다. PRoFESS(n=20,332)는 Aggrenox가 클로피도그렐과 동등한 뇌졸중 예방 효과를 갖는다는 직접 비교 근거를 제공합니다. 다수의 Cochrane 체계적 문헌고찰(2003·2006·2007)이 이 효과를 일관되게 지지합니다.

### 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00153062](https://clinicaltrials.gov/study/NCT00153062) | Phase 4 | 완료 | 20,332 | PRoFESS: ER-dipyridamole+아스피린 vs 클로피도그렐 — 뇌졸중 재발 이차 예방 직접 비교 |
| [NCT00161070](https://clinicaltrials.gov/study/NCT00161070) | Phase 4 | 완료 | 4,500 | ESPRIT: 아스피린+dipyridamole vs 아스피린 단독 — 복합 혈관 사건 20% 감소 |
| [NCT00311402](https://clinicaltrials.gov/study/NCT00311402) | Phase 3 | 완료 | 1,295 | JASAP: Aggrenox vs 아스피린 81mg — 일본인 뇌경색 재발 예방 비교 |
| [NCT01661322](https://clinicaltrials.gov/study/NCT01661322) | Phase 3 | 조기종료 | 3,096 | 고위험 중풍 환자 삼중 vs 이중 항혈소판(dipyridamole 포함) — 안전성 우려로 종료 |
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | 완료 | 664 | PFO 봉합 vs 항응고제 vs 항혈소판(dipyridamole 포함) — 뇌졸중 재발 예방 3군 비교 |
| [NCT00738894](https://clinicaltrials.gov/study/NCT00738894) | N/A | 완료 | 664 | REDUCE: PFO 봉합기 vs 항혈소판(dipyridamole+아스피린) — 잠재성 뇌졸중 예방 |
| [NCT00562588](https://clinicaltrials.gov/study/NCT00562588) | Phase 4 | 완료 | 551 | EARLY: 뇌졸중 발생 24시간 이내 Aggrenox 조기 투여 vs 7일 후 투여 비교 |
| [NCT01295567](https://clinicaltrials.gov/study/NCT01295567) | Phase 4 | 완료 | 95 | Dipyridamole의 CABG 수술 중 허혈-재관류 손상 심근보호 효과 탐색 |
| [NCT02630862](https://clinicaltrials.gov/study/NCT02630862) | N/A | 완료 | 240 | 경동맥 재혈관화 후 dipyridamole 항산화 활성 및 뇌혈관 산화 스트레스 감소 확인 |
| [NCT02966119](https://clinicaltrials.gov/study/NCT02966119) | Phase 3 | 조기종료 | 23 | RESTART-FR: 뇌출혈 후 항혈소판제(dipyridamole 포함) 재개 vs 중단 이익/위험 비교 |

### 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|------|------|------|---------|
| [12535415](https://pubmed.ncbi.nlm.nih.gov/12535415/) | 2003 | Cochrane SR | Cochrane DB | 혈관 위험 환자에서 dipyridamole 혈관 사건 예방 효과; 아스피린 병용 시 추가 이익 |
| [17636684](https://pubmed.ncbi.nlm.nih.gov/17636684/) | 2007 | Cochrane SR | Cochrane DB | 업데이트: 아스피린+dipyridamole이 아스피린 단독 대비 22% 위험 감소 |
| [16625549](https://pubmed.ncbi.nlm.nih.gov/16625549/) | 2006 | Cochrane SR | Cochrane DB | Dipyridamole 뇌졸중/혈관 사건 예방 체계적 문헌고찰 (중간 업데이트) |
| [15569877](https://pubmed.ncbi.nlm.nih.gov/15569877/) | 2005 | Meta-analysis | Stroke | 개인 환자 데이터 메타분석: 재발성 허혈 뇌졸중 예방에서 dipyridamole 단독 및 병용 효과 |
| [11786451](https://pubmed.ncbi.nlm.nih.gov/11786451/) | 2002 | Meta-analysis | BMJ | 항혈소판 요법 사망·MI·뇌졸중 예방: 고위험 환자 무작위 시험 협력 메타분석 |
| [8981292](https://pubmed.ncbi.nlm.nih.gov/8981292/) | 1996 | RCT | J Neurol Sci | ESPS-2: 아스피린+dipyridamole 병용이 뇌졸중 이차 예방에서 각 단독 대비 우월 |
| [20955428](https://pubmed.ncbi.nlm.nih.gov/20955428/) | 2010 | Review | Ann NY Acad Sci | 급성 뇌졸중 중 dipyridamole의 항혈전·신경보호 이중 기전 탐색 |
| [18174451](https://pubmed.ncbi.nlm.nih.gov/18174451/) | 2008 | Review | Arterioscler Thromb Vasc Biol | Dipyridamole 중개 치료학: PDE 억제, NO 증강, 항염증 기전 종합 |
| [30649687](https://pubmed.ncbi.nlm.nih.gov/30649687/) | 2019 | Cohort | CNS Drugs | 아스피린 불내용 심근경색+뇌졸중 환자에서 dipyridamole+클로피도그렐 병용의 이차 예방 효과 |
| [9744826](https://pubmed.ncbi.nlm.nih.gov/9744826/) | 1998 | Review | Neurology | Dipyridamole 뇌졸중 예방 임상시험 역사: ESPS-1, ESPS-2 결과 및 임상적 의의 |

### 결론

**결정: Proceed with Guardrails**

**사유:**
ESPS-2, ESPRIT, PRoFESS 등 복수의 대규모 Phase 3/4 RCT와 다수의 Cochrane 체계적 문헌고찰이 dipyridamole+아스피린의 뇌졸중 이차 예방 효과를 일관되게 지지합니다. Aggrenox는 미국 FDA 및 유럽에서 뇌졸중 이차 예방 적응증을 보유합니다.

**진행하려면 필요한 것:**
- 국내 미허가 상태이므로 허가 신청을 위한 규제 전략 수립 필요
- 약물 작용 기전 데이터(MOA) 보완 (현재 Data Gap)
- 국내 뇌졸중 표준치료(클로피도그렐) 대비 위치 설정 검토
- 안전성 경고·금기 사항 (TFDA/MFDS 허가사항) 확인

---

## 보충 보고서 B: 일과성 허혈 발작 (TIA) (Rank 5, L1) — Proceed with Guardrails

### 빠른 개요

| 항목 | 내용 |
|------|------|
| 예측 적응증 | 일과성 허혈 발작 (TIA) |
| TxGNN 예측 점수 | 99.87% |
| 근거 수준 | **L1** |
| 임상시험 수 | 15건 |
| 문헌 수 | 20편 |
| 권장 결정 | **Proceed with Guardrails** |

### 예측이 타당한 이유

TIA는 실제 경색 없이 일시적 신경기능 이상으로 나타나는 허혈 이벤트로, 뇌졸중과 동일한 아테로혈전 기전을 공유합니다. Dipyridamole의 이중 항혈소판 기전은 TIA 재발 방지에 직접 적용됩니다.

**ESPRIT(NCT00161070, Phase 4, n=4,500)**은 TIA 또는 소규모 뇌졸중 환자를 직접 대상으로 아스피린+dipyridamole이 아스피린 단독 대비 복합 혈관 사건을 **20% 감소**시켰음을 증명한 핵심 근거입니다(RR=0.80, 95% CI 0.66–0.98). ESPS-2의 TIA 하위분석도 일관된 효과를 보였으며, 실제 Aggrenox의 전세계 허가 주요 적응증이 TIA 후 이차 예방입니다.

### 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00161070](https://clinicaltrials.gov/study/NCT00161070) | Phase 4 | 완료 | 4,500 | **ESPRIT 핵심 근거**: TIA/소규모 뇌졸중 후 아스피린+dipyridamole → 복합 혈관 사건 20% 감소 |
| [NCT00311402](https://clinicaltrials.gov/study/NCT00311402) | Phase 3 | 완료 | 1,295 | JASAP: Aggrenox vs 아스피린 81mg — 일본인 TIA 포함 뇌경색 재발 예방 비교 |
| [NCT00153062](https://clinicaltrials.gov/study/NCT00153062) | Phase 4 | 완료 | 20,332 | PRoFESS: ER-dipyridamole+아스피린 vs 클로피도그렐 — TIA 후 뇌졸중 재발 포함 |
| [NCT01661322](https://clinicaltrials.gov/study/NCT01661322) | Phase 3 | 조기종료 | 3,096 | 고위험 TIA/뇌졸중 환자 항혈소판 강도 비교 (dipyridamole 포함 치료군) |
| [NCT00738894](https://clinicaltrials.gov/study/NCT00738894) | N/A | 완료 | 664 | REDUCE: PFO 봉합 vs 항혈소판(dipyridamole+아스피린) — TIA 포함 재발 예방 |
| [NCT00562588](https://clinicaltrials.gov/study/NCT00562588) | Phase 4 | 완료 | 551 | EARLY: TIA/뇌졸중 환자에서 Aggrenox 조기(24시간 내) vs 지연 투여 비교 |
| [NCT05763862](https://clinicaltrials.gov/study/NCT05763862) | N/A | 모집 중 | 350 | 유전자형 기반 항혈소판 치료: TIA 환자에서 dipyridamole 포함 선택지 포함 |
| [NCT02630862](https://clinicaltrials.gov/study/NCT02630862) | N/A | 완료 | 240 | TIA 환자 포함 경동맥 재혈관화 후 dipyridamole의 항산화 효과 검증 |
| [NCT01613755](https://clinicaltrials.gov/study/NCT01613755) | Phase 4 | 완료 | 18 | TIA/뇌졸중 환자에서 dipyridamole이 메트포르민 약동학에 미치는 영향 (hENT4 억제) |
| [NCT03688815](https://clinicaltrials.gov/study/NCT03688815) | N/A | 완료 | 50 | L-아르기닌 경로 대사물과 dipyridamole 유발 단기 심근 허혈 — TIA 관련 기전 탐색 |

### 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|------|------|------|---------|
| [34399713](https://pubmed.ncbi.nlm.nih.gov/34399713/) | 2021 | Systematic Review/Meta-analysis | BMC Neurology | 허혈 뇌졸중/TIA 이차 예방 항혈소판 약물 네트워크 메타분석: dipyridamole 병용 효과 확인 |
| [15569877](https://pubmed.ncbi.nlm.nih.gov/15569877/) | 2005 | Meta-analysis | Stroke | 개인 환자 데이터 메타분석: TIA 포함 허혈 뇌졸중 재발 예방에서 dipyridamole 효과 |
| [12535415](https://pubmed.ncbi.nlm.nih.gov/12535415/) | 2003 | Cochrane SR | Cochrane DB | TIA 환자의 혈관 사건 예방: dipyridamole의 역할 체계적 검토 |
| [26304937](https://pubmed.ncbi.nlm.nih.gov/26304937/) | 2015 | Network Meta-analysis | JAHA | 허혈 뇌졸중/TIA 후 장기 항혈소판 단독·병용 요법 계층 분석 |
| [24157563](https://pubmed.ncbi.nlm.nih.gov/24157563/) | 2014 | Review | Front Neurol Neurosci | TIA 항혈전 치료: 아스피린+dipyridamole 병용의 근거와 한계 |
| [22277143](https://pubmed.ncbi.nlm.nih.gov/22277143/) | 2012 | Review | J Clin Hypertens | TIA 항혈소판 요법: 아스피린, dipyridamole, 클로피도그렐 비교 임상 근거 |
| [17389280](https://pubmed.ncbi.nlm.nih.gov/17389280/) | 2007 | Review | Circulation | TIA/뇌졸중 이차 예방에서 더 강력한 혈소판 억제의 필요성: dipyridamole 기전 분석 |
| [20170841](https://pubmed.ncbi.nlm.nih.gov/20170841/) | 2010 | Review | Lancet Neurology | TIA/허혈 뇌졸중 재발 예방 항혈전 요법: 아스피린+ER-dipyridamole의 위치 |
| [18343263](https://pubmed.ncbi.nlm.nih.gov/18343263/) | 2008 | Pharmacodynamic | Clin Ther | TIA 병력 당뇨 환자에서 ER-dipyridamole+아스피린 vs 클로피도그렐±아스피린 항혈소판 프로파일 비교 |
| [35470408](https://pubmed.ncbi.nlm.nih.gov/35470408/) | 2022 | Practice Survey | Acta Neurol Taiwan | 싱가포르 신경과 전문의의 허혈 뇌졸중/TIA 환자 항혈소판·항응고 치료 실제 처방 패턴 |

### 결론

**결정: Proceed with Guardrails**

**사유:**
ESPRIT(Phase 4, n=4,500)이 TIA 환자에서 dipyridamole+아스피린의 직접적 L1 근거를 제공하며, 이는 Aggrenox의 전세계 허가 주요 적응증입니다. 뇌졸중 보충 보고서와 동일한 규제 경로 접근이 가능합니다.

**진행하려면 필요한 것:**
- 뇌졸중 예방과 동일 패키지로 국내 허가 신청 검토 가능
- 아스피린 불내용 TIA 환자에서 dipyridamole 단독 요법 타당성 검토
- MOA 데이터 및 국내 허가사항 안전성 정보 확보
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

