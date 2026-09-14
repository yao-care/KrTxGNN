---
layout: default
title: Simvastatin
parent: 僅模型預測 (L5)
nav_order: 637
evidence_level: L5
indication_count: 8
---

# Simvastatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Simvastatin: 원 적응증 미기재(허가 자료 없음)에서 가족성 고콜레스테롤혈증으로

## 한 문장 요약

Simvastatin은 전 세계적으로 널리 사용되는 HMG-CoA 환원효소 억제제(스타틴 계열) 약물이나, 본 Evidence Pack에는 원 적응증 및 작용기전(MOA)이 구조화 자료로 기재되어 있지 않고 한국에는 현재 허가 제품이 없습니다.
TxGNN 모델은 **가족성 고콜레스테롤혈증(Familial Hypercholesterolemia)**에 효과가 있을 것으로 예측하며, 현재 **19건의 임상시험**과 **20편 이상의 문헌**이 이 방향을 지지합니다. 다만 이는 스타틴 계열의 이미 확립된 표준 치료 영역과 사실상 겹치는 예측입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 미기재 (허가 자료·원 적응증 데이터 없음) |
| 예측 신규 적응증 | 가족성 고콜레스테롤혈증 (Familial Hypercholesterolemia) |
| TxGNN 예측 점수 | 99.63% |
| 근거 수준 | L1 (완료된 Phase 3 RCT 다수 확인) |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용기전(MOA) 데이터는 확보되어 있지 않습니다(High severity 데이터 갭). 다만 Simvastatin은 국제적으로 HMG-CoA 환원효소 억제제(스타틴 계열)로 분류되는 약물로, 간에서의 콜레스테롤 합성을 억제하고 LDL 수용체 발현을 증가시켜 혈중 LDL-콜레스테롤을 낮추는 기전이 학계에 널리 알려져 있습니다.

가족성 고콜레스테롤혈증은 LDL 수용체 유전자 이상 등으로 인해 LDL-콜레스테롤이 만성적으로 상승하는 유전 질환으로, 스타틴의 핵심 약리 기전과 직접적으로 부합합니다. 실제로 근거 자료를 보면 이 예측은 완전히 새로운 발견이라기보다, **이미 국제 가이드라인(ACC/AHA 등)에서 1차 치료제로 확립된 용도를 TxGNN이 재확인한 결과**에 가깝습니다. 소아·청소년 이형접합 및 동형접합 가족성 고콜레스테롤혈증 환자를 대상으로 한 다수의 완료된 Phase 3 시험(ENHANCE 시험 등)이 이를 뒷받침합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | 완료 | 720 | ENHANCE 시험: 이형접합 가족성 고콜레스테롤혈증에서 ezetimibe+고용량 simvastatin 병용 vs simvastatin 단독의 죽상경화 진행 억제 효과 비교 |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3 | 완료 | 442 | 이형접합 가족성 고콜레스테롤혈증 포함 Fredrickson IIa/IIb 이상지질혈증 환자에서 rosuvastatin 대비 simvastatin의 신장 영향 평가 |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Phase 3 | 완료 | 248 | 10-17세 이형접합 가족성 고콜레스테롤혈증 청소년에서 ezetimibe+simvastatin 병용요법의 유효성·안전성 |
| [NCT00465088](https://clinicaltrials.gov/study/NCT00465088) | Phase 3 | 완료 | 199 | 고지혈증/혼합형 이상지질혈증에서 niacin ER+simvastatin 대비 atorvastatin의 HDL-C 상승 효과 비교 |
| [NCT00145574](https://clinicaltrials.gov/study/NCT00145574) | Phase 4 | 완료 | 194 | 스타틴(simvastatin 포함) 안정 용량 복용 중인 소아 이형접합 가족성 고콜레스테롤혈증 환자 대상 colesevelam 추가요법 평가 |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | 완료 | 50 | 동형접합 가족성 고콜레스테롤혈증에서 atorvastatin 또는 simvastatin 병용 ezetimibe 10mg의 유효성·안전성 |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | 완료 | 44 | 상기 시험의 24개월 장기 연장 연구, simvastatin 병용 ezetimibe 장기 안전성·내약성 평가 |
| [NCT01859455](https://clinicaltrials.gov/study/NCT01859455) | Phase 1 | 완료 | 25 | atorvastatin 또는 simvastatin 안정 용량 복용 중인 고콜레스테롤혈증 환자 대상 LGT209 병용 PK/PD 평가 |
| [NCT01623115](https://clinicaltrials.gov/study/NCT01623115) | Phase 3 | 완료 | 486 | 스타틴(simvastatin 등) 배경치료에서 조절 안 되는 이형접합 가족성 고콜레스테롤혈증에 alirocumab 추가요법 평가 |
| [NCT02107898](https://clinicaltrials.gov/study/NCT02107898) | Phase 3 | 완료 | 216 | 스타틴 배경치료 하 이형접합 가족성 고콜레스테롤혈증/고심혈관위험군에 alirocumab 추가요법 LDL-C 감소 효과 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | RCT | The New England Journal of Medicine | ENHANCE 시험 본 논문: 이형접합 가족성 고콜레스테롤혈증에서 simvastatin 단독 대비 ezetimibe 병용의 죽상경화 진행 효과 |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | RCT | Nutrition, Metabolism, and Cardiovascular Diseases | 이형접합 가족성 고콜레스테롤혈증에서 atorvastatin과 simvastatin의 LDL-C 목표 도달률 비교 |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Systematic Review (Cochrane) | Cochrane Database of Systematic Reviews | 소아 가족성 고콜레스테롤혈증에서 스타틴(simvastatin 포함) 치료의 체계적 문헌고찰 |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | 관찰연구 | Journal of the American College of Cardiology | 이형접합 가족성 고콜레스테롤혈증에서 스타틴 치료가 관상동맥질환·전체 사망률에 미치는 영향 |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Review | Drug Safety | 가족성 고콜레스테롤혈증 환자에서 simvastatin의 효익-위험 평가 |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Review | Expert Opinion on Drug Safety | 가족성 고콜레스테롤혈증에서 simvastatin의 장기 효익-위험 평가 |
| [30270066](https://pubmed.ncbi.nlm.nih.gov/30270066/) | 2018 | 관찰연구 | Atherosclerosis | 슬로바키아 실사용 데이터 기반 가족성 고콜레스테롤혈증 치료 패턴 및 LDL-C 목표 도달 현황 |
| [35629051](https://pubmed.ncbi.nlm.nih.gov/35629051/) | 2022 | 단면연구 | Journal of Clinical Medicine | Simvastatin 치료 중인 소아 가족성 고콜레스테롤혈증 환자의 세포성 면역 지표 평가 |
| [15199433](https://pubmed.ncbi.nlm.nih.gov/15199433/) | 2004 | Review | Seminars in Vascular Medicine | 소아 가족성 고콜레스테롤혈증의 진단·임상·치료적 측면 총설 |
| [1346327](https://pubmed.ncbi.nlm.nih.gov/1346327/) | 1992 | 임상연구 | The Lancet | Simvastatin이 리포단백질(a) 수치에 미치는 영향 |

## 안전성 고려사항

안전성 관련 구조화 자료(경고, 금기, 약물상호작용)가 확보되지 않았습니다. 이 항목은 **Blocking 등급 데이터 갭(DG001)**으로 분류되어 있어, 안전성 초기평가(S1) 단계 진입이 현재 불가능한 상태입니다. 별도의 허가사항 원문 확보가 필요합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
가족성 고콜레스테롤혈증에 대한 simvastatin의 유효성 근거는 완료된 Phase 3 RCT 다수와 체계적 문헌고찰로 매우 견고합니다(L1). 그러나 이는 이미 국제적으로 확립된 스타틴 표준치료 영역을 재확인한 것에 가까우며, 한국에는 현재 허가 제품이 없고(0건) 안전성 정보(경고·금기·DDI)가 전혀 확보되지 않은 Blocking 데이터 갭이 있어 안전성 초기평가 단계로 진행할 수 없습니다.

**진행하려면 필요한 것:**
- MFDS(식약처) 허가사항 원문 확보 및 경고·금기 사항 파싱 (DG001, Blocking)
- DrugBank 기반 상세 작용기전(MOA) 데이터 보완 (DG002, High)
- 한국 내 실제 허가/시판 현황 재확인 (현재 미출시로 기재됨)
- rank 1 예측이 "신규 재창출"이 아닌 "기존 확립 용도 재확인"에 해당하는지에 대한 임상 전문가 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

