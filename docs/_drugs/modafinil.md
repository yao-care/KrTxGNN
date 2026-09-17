---
layout: default
title: Modafinil
parent: 중등도 근거 (L3-L4)
nav_order: 487
evidence_level: L3
indication_count: 1
---

# Modafinil
{: .fs-9 }

근거 수준: **L3** | 예측 적응증: **1** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 약사 평가 보고서

</div>

# Modafinil: 기면증·수면무호흡증·교대근무 수면장애에서 불면증으로

## 한 문장 요약

Modafinil은 각성을 촉진하는 촉진제(wake-promoting agent)로, 원래 **기면증, 폐쇄성수면무호흡증(OSA) 잔여 졸음, 교대근무 수면장애**의 주간 과다졸림 치료에 사용되었습니다. TxGNN 모델은 **불면증(Insomnia)**에도 효과가 있을 수 있다고 예측(점수 99.85%)하지만, 현재 근거는 **29건의 임상시험**과 **19편의 문헌** 대부분이 불면증을 직접 겨냥하지 않고 암/화학요법 후 피로 관리나 파킨슨병 주간졸림 등 인접 주제를 다루고 있어, 근거 수준은 L3(관찰/전임상 수준)에 그칩니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 기면증, OSA 잔여 졸림, 교대근무 수면장애 (각성 촉진 목적) |
| 예측 신규 적응증 | 불면증 (Insomnia) |
| TxGNN 예측 점수 | 99.85% |
| 근거 수준 | L3 |
| 한국 시판 현황 | ✗ 미판매 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

Modafinil은 도파민 재흡수 억제와 시상하부 하이포크레틴/오렉신(orexin) 시스템 조절을 통해 각성 수준을 높이는 촉진제(wake-promoting agent)입니다. 승인된 적응증은 기면증, OSA의 잔여 졸림, 교대근무 수면장애로, 모두 "과도한 졸림"을 줄이는 방향의 치료입니다.

문제는 불면증 치료는 반대로 진정/수면 유도 방향의 기전을 필요로 한다는 점입니다. 즉 Modafinil의 약리 방향과 불면증 치료 목적이 정반대입니다. TxGNN의 높은 예측 점수는 지식그래프 내 "수면장애" 관련 노드들이 서로 밀접하게 연결되어 나타난 군집 효과일 가능성이 있으며, 모델이 "각성 촉진"과 "수면 유도"라는 방향성 차이를 구분하지 못했을 가능성이 있습니다.

실제로 관련 임상시험 대부분은 암 화학요법 후 피로·불면 동반 증상 관리에서 Modafinil을 CBT-I(불면증 인지행동치료)의 보조 역할로 사용하고 있어, Modafinil 자체가 불면증의 1차 치료제로 검증된 근거는 아직 약합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01011218](https://clinicaltrials.gov/study/NCT01011218) | Phase 2 | 완료 | 70 | 유방암 환자 불면증 관리 예비 연구. BBT-I/CBT-I ± Armodafinil 병용 비교. 불면증을 직접 대상으로 한 가장 관련성 높은 시험 |
| [NCT01019187](https://clinicaltrials.gov/study/NCT01019187) | Phase 2 | 완료 | 226 | 화학요법 후 유방암 생존자의 불면증·피로에 CBT ± Armodafinil 효과 평가 |
| [NCT01091974](https://clinicaltrials.gov/study/NCT01091974) | Phase 2 | 완료 | 138 | 화학요법 후 불면증·피로에 CBT-I ± Armodafinil 효과, Armodafinil은 피로 보조 역할 가능성 |
| [NCT00124384](https://clinicaltrials.gov/study/NCT00124384) | Phase 4 | 완료 | 40 | 원발성 불면증 환자의 주간 기능·수면에 대한 Modafinil 단독/CBT-I 병용 효과 |
| [NCT02552303](https://clinicaltrials.gov/study/NCT02552303) | N/A | 완료 | 39 | 수면호흡장애 동반 불면증에 Armodafinil 및/또는 CBT-I 효과 평가 |
| [NCT00626210](https://clinicaltrials.gov/study/NCT00626210) | Phase 4 | 조기종료 | 2 | 노인 수면/각성 장애에 Modafinil 치료, 등록 부족으로 조기종료 |
| [NCT01965925](https://clinicaltrials.gov/study/NCT01965925) | Phase 4 | 완료 | 18 | 안정형 양극성장애의 일주기·인지기능 문제에 Modafinil, 불면증이 주요 종점은 아님 |
| [NCT01305408](https://clinicaltrials.gov/study/NCT01305408) | Phase 3 | 완료 | 399 | 양극성장애 I형 주요우울삽화에 Armodafinil 보조요법, 적응증이 불면증과 직접 관련 없음 |
| [NCT03620253](https://clinicaltrials.gov/study/NCT03620253) | Phase 3 | 조기종료 | 9 | 우울증 관해 후 잔존 인지기능장애에 Modafinil 효과, 불면증과 직접 관련 없음 |
| [NCT00481195](https://clinicaltrials.gov/study/NCT00481195) | Phase 2 | 완료 | 257 | 양극성장애 I형 주요우울삽화에 Armodafinil 보조요법 (150mg/day) |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [27010071](https://pubmed.ncbi.nlm.nih.gov/27010071/) | 2016 | Systematic Review (Tier 1) | Parkinsonism & Related Disorders | 파킨슨병의 주간졸림·수면장애에 대한 약물 중재 체계적 문헌고찰/메타분석 |
| [22021174](https://pubmed.ncbi.nlm.nih.gov/22021174/) | 2011 | 근거중심 가이드라인 (Tier 1) | Movement Disorders | 파킨슨병 비운동증상 치료에 대한 MDS 근거중심 리뷰 업데이트 |
| [39535843](https://pubmed.ncbi.nlm.nih.gov/39535843/) | 2024 | Review (Tier 2) | Expert Opin Pharmacother | 파킨슨병 수면장애의 약물/비약물 관리 |
| [18729534](https://pubmed.ncbi.nlm.nih.gov/18729534/) | 2008 | Review (Tier 2) | Drugs | Modafinil의 승인 및 연구 중인 용도에 대한 근거중심 리뷰 |
| [24312590](https://pubmed.ncbi.nlm.nih.gov/24312590/) | 2013 | Systematic Review/Meta-analysis (Tier 2) | PLoS ONE | 신경계 질환 관련 피로·주간과다졸림에 대한 Modafinil 효능 메타분석 |
| [20082966](https://pubmed.ncbi.nlm.nih.gov/20082966/) | 2009 | Review (Tier 2) | Parkinsonism & Related Disorders | 파킨슨병의 주간졸림 |
| [18805301](https://pubmed.ncbi.nlm.nih.gov/18805301/) | 2008 | Review (Tier 3, 주제 이탈) | Revue Neurologique | 탈력발작을 동반한 기면증 리뷰, 불면증과 직접 관련 낮음 |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Review (Tier 3, Modafinil 무관) | Drug Des Devel Ther | Pitolisant의 기면증 치료 프로파일, Modafinil 근거 아님 |
| [17060310](https://pubmed.ncbi.nlm.nih.gov/17060310/) | 2006 | Case Series (Tier 3) | Am J Hosp Palliat Care | Charcot-Marie-Tooth병 1A형의 피로에 Modafinil 사례 시리즈 |
| [26317009](https://pubmed.ncbi.nlm.nih.gov/26317009/) | 2014 | Review (Tier 3, 주제 이탈) | J Neurodegener Dis | 운동신경원병 다학제 관리, 불면증과 관련 낮음 |

## 한국 시판 정보

현재 한국(대상 레지스트리 기준)에 Modafinil 관련 허가 품목이 없습니다 (허가증 0건, 미판매).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
Modafinil은 각성 촉진 기전을 가진 약물로 불면증 치료 목적과 약리학적 방향이 상반되며, 수집된 임상시험·문헌 대부분이 불면증을 1차 치료 목표가 아닌 암 치료 후 피로 관리나 타 신경계 질환의 주간졸림 관리에서 보조적으로 다루고 있습니다. 근거 수준 L3로 TxGNN의 높은 예측 점수를 뒷받침할 만한 직접적 근거가 부족합니다.

**진행하려면 필요한 것:**
- TFDA/한국 식약처 허가사항의 경고·금기 정보 확보 (현재 Blocking 데이터 갭, S1 안전성 초평가 진입 불가)
- DrugBank 공식 작용기전(MOA) 데이터 확인 (현재 High 데이터 갭)
- 불면증을 1차 종점으로 설계한 무작위대조시험 확인 또는 신규 수행 필요
- Modafinil의 각성 촉진 기전과 불면증 치료 목적 간 상충 여부에 대한 약리 전문가 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

