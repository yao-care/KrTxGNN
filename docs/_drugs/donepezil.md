---
layout: default
title: Donepezil
parent: 僅模型預測 (L5)
nav_order: 228
evidence_level: L5
indication_count: 8
---

# Donepezil
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

# Donepezil: 알츠하이머 치매에서 만성 틱 장애로

> **다중 적응증(Multi-Indication) 분석** — TxGNN이 예측한 8개 운동장애 적응증 중 가장 높은 근거 수준의 적응증을 중심으로 서술합니다.

---

## 한 문장 요약

Donepezil은 아세틸콜린에스테라제(AChE) 억제제로, 전 세계적으로 알츠하이머 치매 치료에 사용되고 있습니다.
TxGNN 모델은 **만성 틱 장애(Chronic Tic Disorder)** 를 포함한 8개 운동장애 관련 적응증에 효과가 있을 수 있다고 예측하며,
현재 **0건의 임상시험**과 **5편의 문헌**이 만성 틱 장애를 직접 지지하고 있으며, **혀-안면-구강 이상운동증(rank 8)** 에는 추가로 **20편의 문헌**이 존재합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 알츠하이머 치매 (한국 미시판) |
| 예측 신규 적응증 | 만성 틱 장애 (Chronic Tic Disorder) |
| TxGNN 예측 점수 | 99.19% |
| 근거 수준 | L3 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Research Question |

---

## 이 예측이 타당한 이유는?

현재 이 Evidence Pack에는 상세한 작용 기전(MOA) 데이터가 포함되어 있지 않습니다. 알려진 정보에 따르면, Donepezil은 **아세틸콜린에스테라제(AChE) 억제제**로, 시냅스 틈새에서 아세틸콜린의 분해를 억제하여 콜린성 신경전달을 강화합니다. 알츠하이머 치매에서 관찰되는 기저전뇌 콜린성 뉴런의 소실에 의한 인지 기능 저하를 보완하기 위해 개발된 약물입니다.

만성 틱 장애(투렛 증후군 포함)에 대한 적용 타당성은 **선조체 콜린성-도파민성 균형 가설**로 설명됩니다. 기저핵 내에서 아세틸콜린과 도파민은 길항적 관계로 조절되며, AChE 억제를 통해 콜린성 긴장도를 높이면 과도한 도파민 활성이 억제되어 틱 증상 완화로 이어질 수 있습니다. 투렛 증후군 환자에서 니코틴성 아세틸콜린 수용체(nAChR) 기능 이상이 보고되어 있으며, 니코틴(nAChR 작동제)이 틱 증상을 개선한다는 임상 경험이 이 가설을 간접적으로 지지합니다.

나아가 PMID 16045972는 마우스에서 Donepezil이 5-HT₂A 수용체 매개 DOI-induced head twitch response(투렛 틱 동물 모델)를 유의하게 억제함을 보여, 세로토닌 조절 경로가 보조적 기전으로 작용할 수 있음을 시사합니다. 이처럼 도파민·콜린·세로토닌 다중 경로를 통한 기전적 연결이 알츠하이머 치매와 운동장애 사이의 재창출 근거를 형성합니다.

---

## 전체 예측 적응증 현황

TxGNN은 총 8개 운동장애 관련 적응증을 예측하였습니다. 아래 **굵은 표시** 3개 적응증에서 L3 수준의 문헌 근거가 확인되었으며, 나머지 5개는 임상·문헌 근거 부재로 Hold 권장입니다.

| 순위 | 적응증 | TxGNN 점수 | 근거 수준 | 권장 결정 |
|------|--------|-----------|---------|---------|
| 1 | 심인성 운동장애 (Psychogenic Movement Disorders) | 99.23% | L5 | Hold |
| **2** | **만성 틱 장애 (Chronic Tic Disorder) ★** | **99.19%** | **L3** | **Research Question** |
| 3 | 원발성 직립성 진전 (Primary Orthostatic Tremor) | 99.17% | L5 | Hold |
| **4** | **추체외로 및 운동질환 (Extrapyramidal & Movement Disease)** | **99.16%** | **L3** | **Research Question** |
| 5 | 양성 전율 발작 — 소아 (Benign Shuddering Attacks) | 99.16% | L5 | Hold |
| 6 | 진전-안진-십이지장궤양 증후군 | 99.15% | L5 | Hold |
| 7 | 소아 양성 발작성 강직성 상향 주시+운동실조 | 99.12% | L5 | Hold |
| **8** | **혀-안면-구강 이상운동증 (Lingual-Facial-Buccal Dyskinesia)** | **99.02%** | **L3** | **Research Question** |

★ 본 보고서 주요 분석 대상

---

## 임상시험 근거

현재 8개 예측 적응증 모두에 대해 등록된 관련 임상시험이 없습니다.

---

## 문헌 근거

### 만성 틱 장애 (Rank 2 — 주 분석 대상)

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [18343255](https://pubmed.ncbi.nlm.nih.gov/18343255/) | 2008 | 오픈라벨 임상연구 | Clinical Therapeutics | 아동·청소년 틱+ADHD에서 18주 Donepezil 투여 후 증상 개선 관찰 |
| [10440471](https://pubmed.ncbi.nlm.nih.gov/10440471/) | 1999 | 증례 보고 | J Clin Psychopharmacology | 투렛 증후군+ADHD에서 Donepezil 사용 경험 보고 |
| [16045972](https://pubmed.ncbi.nlm.nih.gov/16045972/) | 2005 | 동물 연구 | Pharmacol Biochem Behav | Donepezil이 마우스 중추 세로토닌계를 통해 DOI-induced HTR(투렛 틱 동물 모델) 억제 |
| [14643839](https://pubmed.ncbi.nlm.nih.gov/14643839/) | 2003 | 동물 연구 | Pharmacol Biochem Behav | DOI-induced head twitch 모델에서 Donepezil의 틱 억제 효과 확인 |
| [16986157](https://pubmed.ncbi.nlm.nih.gov/16986157/) | 2006 | 증례 보고 | Movement Disorders | 투렛 증후군에서 Donepezil 치료 효과 가능성 보고 |

### 추체외로 및 운동질환 (Rank 4)

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [40224553](https://pubmed.ncbi.nlm.nih.gov/40224553/) | 2025 | 체계적 고찰 | Brain Circulation | AChEI(도네페질 포함)가 알츠하이머 환자에서 운동장애를 유발·악화시킬 수 있음 — ⚠️ 양방향 효과 경고 |
| [15669896](https://pubmed.ncbi.nlm.nih.gov/15669896/) | 2005 | 후향적 임상연구 | J Clinical Psychiatry | 노인 지연성 운동장애에서 Donepezil의 유익한 효과 보고 |
| [14676467](https://pubmed.ncbi.nlm.nih.gov/14676467/) | 2004 | 서술적 고찰 | Dementia Geriatr Cogn Disord | Lewy Body 치매에서 Donepezil을 통한 파킨슨 유사 운동 증상 관리 가능성 |
| [12671528](https://pubmed.ncbi.nlm.nih.gov/12671528/) | 2003 | 증례 시리즈 | Clinical Neuropharmacology | 알츠하이머 동반 정신 증상에서 Donepezil 보조 치료 효과 |

### 혀-안면-구강 이상운동증 (Rank 8 — 최다 문헌)

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [29553158](https://pubmed.ncbi.nlm.nih.gov/29553158/) | 2018 | Cochrane 체계적 고찰 | Cochrane Database | 항정신병약 유발 지연성 이상운동증에서 콜린성 약물의 효과 전반 검토 |
| [15610922](https://pubmed.ncbi.nlm.nih.gov/15610922/) | 2004 | 메타분석 | Prog Neuropsychopharmacol | 신경차단제 유발 TD에서 콜린성 약물 RCT 메타분석 (도네페질 포함) |
| [12137608](https://pubmed.ncbi.nlm.nih.gov/12137608/) | 2002 | 체계적 고찰 | Cochrane Database | 신경차단제 유발 TD에서 콜린성 약물의 효능 체계적 평가 |
| [19142126](https://pubmed.ncbi.nlm.nih.gov/19142126/) | 2009 | 연구 | J Clin Psychopharmacology | 지연성 이상운동증에 대한 Donepezil 직접 효과 연구 |
| [15689723](https://pubmed.ncbi.nlm.nih.gov/15689723/) | 2005 | 증례 연구 | J AACAP | 지연성 이상운동증과 Donepezil 관계 사례 |
| [18321753](https://pubmed.ncbi.nlm.nih.gov/18321753/) | 2008 | ⚠️ 부작용 증례 | Parkinsonism Relat Disord | ⚠️ Donepezil 투여 후 턱 떨림(구강 이상운동) 발생 — 역설적 부작용 사례 |
| [40791064](https://pubmed.ncbi.nlm.nih.gov/40791064/) | 2025 | 체계적 고찰 | J Huntington's Disease | 헌팅턴병 인지 증상에서 콜린에스테라제 억제제의 효능·안전성 체계적 고찰 |
| [12611743](https://pubmed.ncbi.nlm.nih.gov/12611743/) | 2003 | 근거 기반 임상 가이드라인 | Am J Geriatric Psychiatry | AChEI(도네페질 포함)의 근거 기반 임상 적용 권고안 |
| [23917951](https://pubmed.ncbi.nlm.nih.gov/23917951/) | 2013 | 서술적 고찰 | Drugs | 파킨슨병의 비도파민성 운동 치료에서 콜린성 계통의 역할 |
| [10634264](https://pubmed.ncbi.nlm.nih.gov/10634264/) | 2000 | 연구 | Movement Disorders | 헌팅턴병에서 Donepezil 사용 보고 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

**⚠️ 운동장애 재창출 관련 특별 주의사항**: 이번 문헌 검색에서 Donepezil이 운동장애를 **치료하는 동시에 유발·악화시킬 수 있다**는 양방향 효과(bidirectional effect)가 확인되었습니다.

- **PMID 40224553** (2025, 체계적 고찰): 알츠하이머 환자에서 AChEI 관련 운동장애 체계적 검토 — 도네페질 포함 AChEI가 운동장애를 유발할 수 있음을 체계적으로 입증
- **PMID 18321753** (2008, 증례): Donepezil 투여 후 구강 이상운동(턱 떨림) 발생 — 목표 적응증이 곧 잠재적 부작용이 될 수 있는 역설적 상황

따라서 대상 인구 집단의 신중한 선정과 개별 위험-이익 평가가 필수적입니다.

---

## 결론 및 다음 단계

**결정: Research Question (만성 틱 장애 / 추체외로 운동질환 / 혀-안면-구강 이상운동증)**

**사유:**
8개 예측 적응증 중 5개는 임상 및 문헌 근거가 전혀 없어 Hold가 적절합니다. 만성 틱 장애(rank 2), 추체외로 운동질환(rank 4), 혀-안면-구강 이상운동증(rank 8)은 각각 L3 수준의 문헌 근거를 보유하고 있어 Research Question 단계의 추가 탐색 가치가 있으나, Donepezil의 운동장애에 대한 양방향 효과가 문헌에서 확인된 만큼 적용 인구 집단의 세밀한 정의가 선행되어야 합니다.

**진행하려면 필요한 것:**
- **[DG002 해소]** 작용 기전(MOA) 데이터 확보 — DrugBank API 조회
- **[DG001 해소]** 한국 식약처(MFDS) 허가 현황 및 안전성 정보(경고·금기) 확인
- 대상 인구 집단 구체화: 성인 지연성 이상운동증 vs. 소아청소년 투렛 증후군 vs. 만성 틱 장애
- AChEI 유발 운동장애 위험인자 분석 (PMID 40224553 근거) 및 안전성 모니터링 계획 수립
- 만성 틱 장애에 대한 소규모 무작위 대조 임상시험 설계 가능성 검토
- 한국 임상시험 등록 시스템(CRIS) 포함 국내 임상시험 현황 재조회
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

