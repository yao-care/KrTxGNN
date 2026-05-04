---
layout: default
title: Armodafinil
parent: 僅模型預測 (L5)
nav_order: 85
evidence_level: L5
indication_count: 1
---

# Armodafinil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Armodafinil: 기면증·수면무호흡증에서 불면증으로

## 한 문장 요약

Armodafinil은 modafinil의 R-이성질체(Nuvigil™)로, 기면증·폐쇄성 수면무호흡증(OSA)·교대근무 수면장애에 동반된 과도한 주간 졸음증 치료에 사용됩니다.
TxGNN 모델은 이 약이 **불면증(Insomnia)**에도 효과가 있을 수 있다고 예측하며,
현재 **12건의 임상시험**과 **19편의 문헌**이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 기면증, 폐쇄성 수면무호흡증(OSA), 교대근무 수면장애에 동반된 과도한 주간 졸음증 |
| 예측 신규 적응증 | 불면증 (Insomnia) |
| TxGNN 예측 점수 | 99.89% |
| 근거 수준 | L2 |
| 한국 시판 현황 | ✗ 미시판 (허가 이력 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Armodafinil은 modafinil의 R-이성질체로, **도파민 수송체(DAT) 억제**를 통해 각성을 촉진하는 약물입니다. 미국 FDA 승인 적응증은 기면증·OSA·교대근무 수면장애로, 모두 과도한 주간 졸음증을 핵심 증상으로 합니다.

이 예측에는 **기전적 역설(Mechanistic Paradox)**이 존재합니다. DAT 억제를 통한 각성 촉진은 이론적으로 원발성 불면증을 악화시킬 수 있습니다. 다만 특정 이차성 불면증 군에서는 다른 경로로 효과를 기대할 수 있습니다. 암 치료 후 극심한 낮 피로 → 주야 리듬 붕괴 → 야간 수면 악화로 이어지는 악순환에서, Armodafinil이 **주간 기능을 회복시켜 일주기 리듬을 재설정**함으로써 야간 수면 품질이 간접적으로 개선될 수 있다는 것입니다. 이 경로는 화학요법 후 피로·불면증이 공존하는 유방암 생존자 집단에서 복수의 임상시험을 통해 탐색되었습니다.

따라서 TxGNN이 예측하는 "불면증" 적응증은 **원발성 불면증이 아닌, 일주기 리듬 교란 또는 암 치료 관련 이차성 불면증** 맥락에서만 기전적 타당성이 성립합니다. 이 구분이 임상 적용 가능성 전체를 결정하는 핵심 전제조건입니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01019187](https://clinicaltrials.gov/study/NCT01019187) | Phase 2 | 완료 | 226 | 화학요법 후 유방암 생존자에서 CBT-I ± Armodafinil의 불면증·피로 개선 효과를 평가한 4군 무작위 배정 임상시험 |
| [NCT01091974](https://clinicaltrials.gov/study/NCT01091974) | Phase 2 | 완료 | 138 | 화학요법 후 유방암 환자의 수면 장애 및 피로 감소를 위한 CBT-I ± Armodafinil 비교; NCT01019187의 확인적 성격 |
| [NCT00481195](https://clinicaltrials.gov/study/NCT00481195) | Phase 2 | 완료 | 257 | 8주 이중맹검 위약 대조 설계; 양극성 I형 장애 동반 주요 우울삽화 성인에서 Armodafinil 150 mg/일 보조요법 효과 평가 |
| [NCT01011218](https://clinicaltrials.gov/study/NCT01011218) | Phase 2 | 완료 | 70 | 유방암 환자 불면증 관리 파일럿 연구; BBT-I 또는 CBT-I에 Armodafinil 150 mg/일 병용 4군 비교 |
| [NCT02552303](https://clinicaltrials.gov/study/NCT02552303) | N/A | 완료 | 39 | 수면 호흡 장애 동반 불면증 환자에서 Armodafinil 단독·CBT-I 단독·병용의 수면 연속성 개선 효과 및 CPAP 순응도 비교 |
| [NCT01305408](https://clinicaltrials.gov/study/NCT01305408) | Phase 3 | 완료 | 399 | 양극성 I형 장애 동반 주요 우울삽화에서 Armodafinil 150 mg/일 보조요법을 평가한 이중맹검 위약 대조 RCT |
| [NCT01072929](https://clinicaltrials.gov/study/NCT01072929) | Phase 3 | 완료 | 433 | 양극성 I형 장애 동반 주요 우울증에서 Armodafinil 150·200 mg/일 보조요법 효과를 평가한 이중맹검 RCT |
| [NCT01072630](https://clinicaltrials.gov/study/NCT01072630) | Phase 3 | 완료 | 492 | 양극성 I형 장애 동반 주요 우울증 관련 임상시험 중 가장 대규모(492명); 이중맹검 위약 대조 설계 |
| [NCT00678691](https://clinicaltrials.gov/study/NCT00678691) | Phase 4 | 완료 | 55 | 섬유근통 피로에 대한 Armodafinil 8주 증강 치료 효과; 샘플 수 소규모(55명), 일반 불면증 외삽성 낮음 |
| [NCT01121536](https://clinicaltrials.gov/study/NCT01121536) | Phase 3 | ⚠️ 조기 종료 | 867 | 양극성 I형 장애에서 Armodafinil 6개월 개방 연장 연구; **조기 종료됨** — 종료 원인(안전성·효능 부족 여부) 확인 필수 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [18729534](https://pubmed.ncbi.nlm.nih.gov/18729534/) | 2008 | Evidence-Based Review | Drugs | Modafinil(armodafinil의 모체)의 무작위 이중맹검 RCT 근거 종합; 기면증·OSA·교대근무 외 피로·인지 장애에서의 사용 근거 정리 |
| [27010071](https://pubmed.ncbi.nlm.nih.gov/27010071/) | 2016 | Systematic Review | Parkinsonism Relat Disord | 파킨슨병 수면 장애에 대한 약리적 개입의 체계적 문헌고찰 및 메타분석; 주간 졸음증 개선 약물의 근거 수준 분류 |
| [22021174](https://pubmed.ncbi.nlm.nih.gov/22021174/) | 2011 | EBM Review (MDS) | Movement Disorders | MDS 근거 중심 의학 검토; 파킨슨병 비운동 증상 치료에서 수면 장애 개입의 근거 수준 공식 분류 |
| [39535843](https://pubmed.ncbi.nlm.nih.gov/39535843/) | 2024 | Narrative Review | Expert Opin Pharmacother | 파킨슨병 수면 장애의 최신 약리적·비약리적 치료 전략; 주간 졸음증과 불면증의 동시 관리 접근법 포함 |
| [24272458](https://pubmed.ncbi.nlm.nih.gov/24272458/) | 2014 | Review | Neurotherapeutics | 파킨슨병 연관 수면 장애 치료; REM 수면행동장애·불면증·과도한 주간 졸음증 별 치료 옵션의 예비 근거 검토 |
| [17181377](https://pubmed.ncbi.nlm.nih.gov/17181377/) | 2006 | Review | Drugs | 교대근무 수면장애(SWSD)의 질병 부담과 관리 전략; 불면증·과도한 졸음증 공존 패턴에서의 약물 치료 근거 |
| [21904092](https://pubmed.ncbi.nlm.nih.gov/21904092/) | 2011 | Review | Postgrad Med | 교대근무 장애의 최신 이론 및 치료; 수면 장애와 불면증 공존 패턴에서 각성 촉진제의 역할과 한계 |
| [24138359](https://pubmed.ncbi.nlm.nih.gov/24138359/) | 2013 | Review | Med J Aust | 교대근무에서 수면 부족 및 일주기 리듬 교란의 건강 부담과 관리; 불면증 동반 수면 장애 치료 포함 |
| [18805301](https://pubmed.ncbi.nlm.nih.gov/18805301/) | 2008 | Review | Rev Neurol | 탈력발작 동반 기면증 종합 리뷰; 야간 수면 유지 불면증이 기면증의 주요 동반 증상임을 명시 — 각성 촉진제와 불면증의 관계 맥락 제공 |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Review | Drug Des Devel Ther | Pitolisant의 기면증 관리 프로파일; 각성 촉진 약물군 내 불면증 동반 패턴의 비교 맥락 제공 |

---

## 한국 시판 정보

Armodafinil은 한국 내 허가 이력이 없습니다 (식품의약품안전처 등록 허가증 0건). 미국에서는 Nuvigil™ 상품명으로 허가되어 있으나, 국내에서는 모체 약물인 modafinil도 향정신성의약품(마약류)으로 분류·관리되고 있어 신규 허가 신청 시 마약류 관리 규정 적용이 예상됩니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
Armodafinil의 DAT 억제를 통한 각성 촉진 기전은 **원발성 불면증을 악화시킬 수 있는 기전적 역설**을 내포하며, 현재 근거는 주로 화학요법 후 이차성 불면증·양극성 장애 동반 우울증 등 특정 공존 이환 집단에 국한됩니다. 한국 내 허가 이력이 없고 마약류 규제 장벽이 존재하므로, 적응증 정의와 안전성 데이터 보완 없이 개발 추진은 시기상조입니다.

**진행하려면 필요한 것:**
- **적응증 정의 명확화**: 원발성 불면증 vs. 일주기 리듬 교란성 이차 불면증 구분 및 목표 인구 특정
- **MOA 데이터 보완**: DrugBank API 조회를 통한 상세 작용 기전 확인
- **안전성 데이터 확보**: MFDS 허가사항 및 TFDA 仿單 PDF 파싱 (DG001 해소)
- **NCT01121536 종료 원인 조사**: 867명 대상 Phase 3 조기 종료의 안전성 신호 여부 확인
- **마약류 규제 검토**: 국내 향정신성의약품 분류 하 개발 가능 경로 사전 확인
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

