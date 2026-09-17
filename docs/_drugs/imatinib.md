---
layout: default
title: Imatinib
parent: 높은 근거 (L1-L2)
nav_order: 388
evidence_level: L2
indication_count: 10
---

# Imatinib
{: .fs-9 }

근거 수준: **L2** | 예측 적응증: **10** 건
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

# Imatinib: 만성골수성백혈병·위장관기질종양(GIST)에서 결합조직형성 섬유육종(Fibrosarcoma)으로

## 한 문장 요약

Imatinib은 BCR-ABL/KIT/PDGFR 티로신키나아제 억제제로, 원래 만성골수성백혈병(CML)과 위장관기질종양(GIST) 치료제로 개발되었습니다(문헌 근거, 허가 자료 아님). TxGNN 모델은 **결합조직형성 섬유육종 계열 종양(conventional fibrosarcoma 등)**에도 효과가 있을 수 있다고 예측했으며, 그중 가장 근거가 탄탄한 적응증(conventional fibrosarcoma)은 **완료된 Phase 2 임상시험 1건**과 **9편의 문헌**(PDGFB 융합 양성 피부섬유육종 관련)의 지지를 받고 있습니다. 다만 한국 내 허가 자료 및 안전성 데이터가 전무해 실질적 진행에는 제약이 큽니다.

## 빠른 개요

TxGNN은 10개의 후보 적응증을 예측했으며, 대부분 섬유육종/육종 계열입니다. 아래는 **근거 수준이 가장 높은 candidate(conventional fibrosarcoma, rank 3)** 기준입니다. (TxGNN 점수 1위인 heart fibrosarcoma는 점수는 가장 높지만 근거 수준 L4로 실질적 지지가 약함.)

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 만성골수성백혈병(CML), 위장관기질종양(GIST) — 문헌 기반, 한국 허가 자료 없음 |
| 예측 신규 적응증 | Conventional Fibrosarcoma (결합조직형성 섬유육종 계열) |
| TxGNN 예측 점수 | 99.93% (rank 1906/전체) |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미상시 (Not marketed) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

구조화 데이터상 MOA는 [작용기전 데이터 없음]으로 표기되어 있으나, 확보된 문헌(PMID 18230575, 15794712)에 따르면 Imatinib(Gleevec/Glivec)은 c-ABL, c-KIT, PDGFR(혈소판유래성장인자수용체) 티로신키나아제를 선택적으로 억제하는 소분자 표적치료제입니다. 원래 CML(BCR-ABL 양성)과 GIST(KIT 양성) 치료제로 개발되었고, 이후 PDGFR 관련 종양으로 적응증이 확대되어 왔습니다.

피부섬유육종융기증(Dermatofibrosarcoma protuberans, DFSP)과 그 섬유육종화 변이형은 t(17;22)(q22;q13) 전위로 인한 **COL1A1-PDGFB 융합**이 특징이며, 이는 PDGFR 신호를 지속적으로 활성화시킵니다. Imatinib이 이 융합 단백질의 하위 신호를 차단할 수 있다는 것이 다수 문헌(PMID 25852058, 19635106, 27806849)의 공통된 기전 설명입니다. 즉, "conventional fibrosarcoma" 예측 자체는 PDGFR 구동 육종(특히 DFSP 및 그 섬유육종화형)과의 기전적 연관성에서 나온 것으로 보이며, 순수한 고전적 conventional fibrosarcoma(비-PDGFR 구동형)에 대한 직접 근거는 아직 약합니다.

반면 heart fibrosarcoma(TxGNN 1위 예측)는 "PDGFB 구동 심장 원발 섬유육종이라면 이론상 연관"이라는 순수 기전 외삽에 그치며, 직접 임상 근거는 없습니다.

## 임상시험 근거

*(conventional fibrosarcoma 기준)*

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00085475](https://clinicaltrials.gov/study/NCT00085475) | Phase 2 | 완료 | 17 | t(17;22)(q22;q13) 전위로 COL1A1/PDGF-β 융합단백질을 발현하는 국소진행성/전이성 연조직육종(DFSP, 거대세포섬유아세포종 포함)에서 Imatinib 효과 평가. 관련성 등급 B — Phase 2이나 fibrosarcoma 특이적이 아닌 광범위 STS 대상, 표본수 17명으로 제한적 |

## 문헌 근거

*(conventional fibrosarcoma 기준, 관련성 우선순위: Review > Cohort > Case Report > 미분류)*

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [27806849](https://pubmed.ncbi.nlm.nih.gov/27806849/) | 2016 | Review | Annals of Diagnostic Pathology | DFSP의 병리·유전학·치료전략 종설. COL1A1-PDGFB 융합전사체가 특징이며 표적치료 근거 정리 |
| [25852058](https://pubmed.ncbi.nlm.nih.gov/25852058/) | 2015 | Cohort | Molecular Cancer Therapeutics | Imatinib은 절제불가/전이성 DFSP 환자 약 50%에서 임상적 이득. CDKN2A/p16 소실 시 Imatinib 저항성과 관련, CDK4가 대안 표적 |
| [19635106](https://pubmed.ncbi.nlm.nih.gov/19635106/) | 2009 | Cohort | Histopathology | DFSP 20예에서 COL1A1-PDGFB 전사체 분석, 치료적 함의 논의 |
| [16733451](https://pubmed.ncbi.nlm.nih.gov/16733451/) | 2006 | Case Report | Annales de Dermatologie et de Vénéréologie | 소아기 발병 다발성 위축성 섬유육종(DFSP 아형) 증례 |
| [30901500](https://pubmed.ncbi.nlm.nih.gov/30901500/) | 2019 | 미분류 | Drug Development Research | Imatinib+Dexketoprofen 표적 리포좀/나노코클리에이트 제형의 섬유육종 억제 효능(전임상) |
| [15794712](https://pubmed.ncbi.nlm.nih.gov/15794712/) | 2005 | 미분류 | Expert Opinion on Drug Safety | Imatinib의 개발과 적용 전반 개관 |
| [22285046](https://pubmed.ncbi.nlm.nih.gov/22285046/) | 2012 | 미분류 | Actas Dermo-Sifiliográficas | DFSP 종설, COL1A1-PDGFB 전위가 진단에 기여 |
| [17397592](https://pubmed.ncbi.nlm.nih.gov/17397592/) | 2007 | 미분류 | Actas Dermo-Sifiliográficas | DFSP의 임상병리 특징 및 치료 개관 |
| [32059813](https://pubmed.ncbi.nlm.nih.gov/32059813/) | 2020 | 미분류 | Bulletin du Cancer | 저소득국가에서 국소진행성 DFSP의 절제 및 재건수술 경험 |

## 세포독성 (항종양약)

Imatinib은 표적 티로신키나아제 억제제(TKI)로 항종양약에 해당합니다.

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (BCR-ABL/KIT/PDGFR 선택적 억제제, 고전적 세포독성 화학요법과 구별) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 데이터 갭(DG001, Blocking)으로 인해 한국 허가사항의 경고·금기 정보가 전무하여 안전성 초평가(S1) 단계 진입이 불가능합니다.
- 근거가 가장 우수한 conventional fibrosarcoma조차 L2 수준(단일 Phase 2, 비특이적 대상군, n=17)에 그치고, TxGNN 점수 1위인 heart fibrosarcoma를 포함한 나머지 9개 예측 적응증 대부분은 L4~L5로 직접 근거가 거의 없습니다.
- 한국 내 미상시 상태로 제형·투여경로 적합성도 확인되지 않았습니다.

**진행하려면 필요한 것:**
- TFDA(또는 한국 식약처 상당) 공식 허가 자료 확보 — 경고, 금기, 약물상호작용(DG001 해소)
- DrugBank 기반 상세 작용기전(MOA) 데이터 확보(DG002 해소)
- conventional fibrosarcoma vs. DFSP/DFSP-섬유육종화형의 정확한 조직학적 구분에 따른 재평가 — 현재 예측이 PDGFR 구동 아형에만 유효할 가능성
- heart fibrosarcoma 등 기전 외삽에만 의존하는 후보들은 추가 전임상/사례보고 근거 확보 전까지 우선순위에서 제외 권장
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

