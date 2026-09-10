---
layout: default
title: Ramipril
parent: 僅模型預測 (L5)
nav_order: 589
evidence_level: L5
indication_count: 10
---

# Ramipril
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

# Ramipril: 고혈압에서 뇌졸중(Stroke)으로

> **방법론 참고**: TxGNN이 최고 점수(99.95%)로 예측한 1순위 후보 "obsolete susceptibility to ischemic stroke"는 Evidence Pack 자체 주석에서 "이미 폐기된 모호한 UMLS 개념, KG 노드 노이즈"로 판정되었으며 임상시험·문헌 근거가 전무합니다(L5/Hold). 2~5, 7~8순위 역시 근거 부재 또는 안전성 우려로 Hold 판정입니다. 따라서 본 보고서는 **근거수준 L1으로 판정된 예측 중 가장 임상적으로 의미 있는 "뇌졸중(Stroke Disorder)"**(TxGNN 10순위, score 99.85%)을 대표 후보로 채택해 작성했습니다.

## 한 문장 요약

Ramipril은 ACE 억제제 계열 약물로, 원래 고혈압 치료에 사용됩니다.
TxGNN 모델은 **뇌졸중(Stroke Disorder)**에도 효과가 있을 수 있다고 예측하며,
현재 **27건의 관련 임상시험**(HOPE, ONTARGET 등 대규모 완료 Phase 3 RCT 포함)과
**19편의 문헌**이 이 방향을 지지합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 고혈압 (ACE 억제제로서 일반적으로 알려진 적응증; 한국 허가 자료 없음) |
| 예측 신규 적응증 | 뇌졸중 (Stroke Disorder) |
| TxGNN 예측 점수 | 99.85% |
| 근거 수준 | L1 |
| 한국 시판 현황 | 미상영 (未上市) |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 Ramipril의 상세 작용기전(MOA) 데이터는 확보되지 않았습니다(Data Gap, DG002). 다만 일반적으로 알려진 약리학적 지식과 본 근거팩에 수록된 기전 서술에 따르면, Ramipril은 ACE(안지오텐신전환효소)를 억제하여 Angiotensin II 생성을 차단하는 RAAS(레닌-안지오텐신-알도스테론계) 억제제입니다. 이를 통해 혈압을 낮추고 말초혈관저항을 감소시키는 것이 고혈압 치료의 핵심 기전입니다.

뇌졸중 예방으로의 적응 확장은 단순한 혈압 강하 효과를 넘어섭니다. 근거팩에 포함된 HOPE 연구(NEJM, 2000)는 심부전이 없는 심혈관 고위험군에서 Ramipril이 혈압 강하 정도로는 설명되지 않는 수준의 심혈관사건·뇌졸중 감소 효과를 보였음을 입증했으며, 이는 RAAS 억제를 통한 혈관내피 기능 개선, 산화스트레스 감소, 죽상동맥경화 진행 억제 등 혈관보호(vasoprotective) 기전이 별도로 작용함을 시사합니다. 이후 ONTARGET 연구(NEJM, 2008, N=31,546)가 telmisartan과의 비교를 통해 이 효과를 재확인하면서, 뇌졸중 예방은 Ramipril의 항고혈압 효과와 기전적으로 연관되면서도 독립적 가치를 지니는 적응증으로 자리잡았습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00153101](https://clinicaltrials.gov/study/NCT00153101) | Phase 4 | 완료 | 31,546 | ONTARGET/TRANSCEND: 고위험 심혈관질환자에서 telmisartan+ramipril 병용 대비 ramipril 단독의 심혈관사망·심근경색·뇌졸중·심부전입원 복합종점 비교 |
| [NCT02596126](https://clinicaltrials.gov/study/NCT02596126) | Phase 3 | 완료 | 2,499 | 아스피린+ramipril+atorvastatin 폴리필 전략이 심근경색 후 노인 환자의 심혈관사망·비치명적 허혈성뇌졸중 등 이차예방 종점에 미치는 효과 평가 |
| [NCT01646437](https://clinicaltrials.gov/study/NCT01646437) | Phase 3 | 완료 | 7,793 | TIPS-3: Polycap(ramipril 포함)+저용량 아스피린+비타민D의 심혈관질환·뇌졸중 1차예방 효과, 10개국 참여 |
| [NCT00000620](https://clinicaltrials.gov/study/NCT00000620) | Phase 3 | 완료 | 10,251 | ACCORD: 제2형 당뇨병 환자에서 집중 혈당·혈압·지질 관리가 심근경색·뇌졸중·심혈관사망 예방에 미치는 영향 평가 |
| [NCT02924727](https://clinicaltrials.gov/study/NCT02924727) | Phase 3 | 완료 | 5,669 | 급성심근경색 고위험군에서 sacubitril/valsartan(LCZ696) vs ramipril의 이환율·사망률 비교 |
| [NCT00095654](https://clinicaltrials.gov/study/NCT00095654) | Phase 3 | 완료 | 5,000 | DREAM: 당뇨병 예방이 주목적이나 뇌졸중 등 심혈관 안전성 종점을 함께 평가 |
| [NCT00741585](https://clinicaltrials.gov/study/NCT00741585) | Phase 4 | 완료 | 21,983 | HYGIA: 24시간 활동혈압 패턴 기반 심혈관·뇌혈관·대사·신장 위험 예측 및 투약 시간대가 예후에 미치는 영향 |
| [NCT04354350](https://clinicaltrials.gov/study/NCT04354350) | N/A | 완료 | 63,744 | 실사용 청구데이터를 활용한 ONTARGET RCT 결과의 재현성 검증 연구 |
| [NCT00140647](https://clinicaltrials.gov/study/NCT00140647) | Phase 3 | 완료 | 1,200 | Ramipril+rosiglitazone이 경동맥 내중막두께(죽상동맥경화 진행)에 미치는 영향 평가 |
| [NCT05963568](https://clinicaltrials.gov/study/NCT05963568) | Phase 3 | 모집 예정 | 680 | SMAART-II: 뇌졸중 병력자 대상 Polycap 기반 이차 혈관위험 감소전략 평가 예정 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [10639539](https://pubmed.ncbi.nlm.nih.gov/10639539/) | 2000 | RCT | The New England Journal of Medicine | HOPE 연구: 심혈관 고위험군에서 Ramipril이 심혈관사망·심근경색·뇌졸중 위험을 유의하게 감소시킴 |
| [18378520](https://pubmed.ncbi.nlm.nih.gov/18378520/) | 2008 | RCT | The New England Journal of Medicine | ONTARGET: telmisartan, ramipril, 병용요법의 혈관질환/고위험 당뇨환자 심혈관사건 예방효과 비교 |
| [11967789](https://pubmed.ncbi.nlm.nih.gov/11967789/) | 2000 | RCT | Journal of the Renin-Angiotensin-Aldosterone System | HOPE 연구 리뷰: ACEI(ramipril)군에서 위약 대비 심혈관사망·MI·뇌졸중 유의 감소, 당뇨병 하위군 포함 분석 |
| [33186492](https://pubmed.ncbi.nlm.nih.gov/33186492/) | 2021 | RCT | The New England Journal of Medicine | Polypill(ramipril 포함)이 아스피린 병용 여부와 관계없이 심혈관질환 위험을 감소시킴 |
| [36018037](https://pubmed.ncbi.nlm.nih.gov/36018037/) | 2022 | Review | The New England Journal of Medicine | 심근경색 후 이차예방에서 아스피린+ACE억제제+스타틴 폴리필 전략의 근거 요약 |
| [19587553](https://pubmed.ncbi.nlm.nih.gov/19587553/) | 2009 | Review | Journal of Hypertension Supplement | PRoFESS·ONTARGET·TRANSCEND 프로그램을 통한 RAAS 차단제의 뇌졸중 예방효과 종합 |
| [12182524](https://pubmed.ncbi.nlm.nih.gov/12182524/) | 2002 | Review | American Family Physician | ACE억제제의 적절한 사용: 고혈압 외 심부전·심근경색·당뇨병·만성신부전·죽상동맥경화성 심혈관질환에서의 이환율/사망률 감소 근거 정리 |
| [11389798](https://pubmed.ncbi.nlm.nih.gov/11389798/) | 2001 | Review | Current Atherosclerosis Reports | 뇌졸중 위험인자 관리 및 예방전략 리뷰, 항고혈압 치료의 역할 포함 |
| [18300867](https://pubmed.ncbi.nlm.nih.gov/18300867/) | 2008 | Cohort(동물실험) | Journal of Hypertension | Ramipril과 candesartan의 뇌졸중 후 신경보호효과 비교(랫드 모델), candesartan만 유의한 효과 확인 |
| [12768220](https://pubmed.ncbi.nlm.nih.gov/12768220/) | 2001 | Review | Drugs of Today | Ramipril의 당뇨병성 신장질환 관련 RAAS 억제 기전 정리 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (TFDA 경고/금기 자료는 Blocking 등급 Data Gap으로 확보되지 않았습니다 — DG001)

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
HOPE, ONTARGET 등 대규모(N>3만) 완료된 Phase 3/4 RCT가 뇌졸중 위험 감소를 직접 입증하여 근거수준 L1으로 판정됩니다. 다만 한국(대만) 내 허가 자료 부재(미상영, 허가증 0건)와 TFDA 경고·금기·MOA 데이터 갭이 안전성 초기평가(S1) 진입을 막고 있어, 가드레일을 전제로 한 진행이 필요합니다.

**진행하려면 필요한 것:**
- TFDA/한국 식약처 허가사항(경고·금기·DDI) 확보 — 현재 Blocking 등급 Data Gap
- DrugBank 등에서 상세 MOA 데이터 확보
- 한국 내 시판/허가 현황 재확인 (현재 미상영으로 등록됨)
- 뇌졸중 적응증 확장을 위한 별도 임상 프로토콜(1차 vs 2차 예방 대상군 구분) 설계
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

