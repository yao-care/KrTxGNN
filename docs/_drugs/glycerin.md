---
layout: default
title: Glycerin
parent: 僅模型預測 (L5)
nav_order: 276
evidence_level: L5
indication_count: 10
---

# Glycerin
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

# Glycerin: 삼투압 조절제에서 마미증후군(Cauda Equina Syndrome)으로

## 한 문장 요약

Glycerin(글리세린, DB09462)은 고삼투압제(hyperosmotic agent)로서 안압 강하, 삼투성 완하, 의약품 부형제 등 다양한 용도로 사용되나, 본 데이터셋에는 공식 허가 적응증 이력이 없습니다.
TxGNN 모델은 **마미증후군(Cauda Equina Syndrome)**을 1순위 예측 적응증으로 제시하나(예측 점수: 99.60%),
현재 이를 지지하는 **임상시험과 문헌이 전혀 없어** 근거 수준 L5로 평가됩니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 이력 없음 (삼투압 조절제·의약품 부형제로 광범위 사용) |
| 예측 신규 적응증 | 마미증후군 (Cauda Equina Syndrome) |
| TxGNN 예측 점수 | 99.60% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, Glycerin은 고삼투압제로서 혈장 삼투압을 상승시켜 조직 내 수분을 혈관 내로 이동시키고 국소 부종을 감소시킵니다. 이는 만니톨(mannitol)과 유사한 원리로, 이론적으로 척수 주변 부종 완화에 적용될 수 있습니다.

그러나 마미증후군은 척수 하단의 신경 다발(마미)이 물리적으로 압박되어 발생하는 신경학적 응급 상황으로, 표준 치료는 즉각적인 외과적 감압술입니다. 삼투압 조절을 통한 glycerol이 이 질환의 병태생리에 의미 있는 영향을 미친다는 기초 연구나 임상 사례는 현재 존재하지 않습니다.

TxGNN 예측 점수 0.996은 **오직 지식 그래프의 위상적 추론(topological inference)** 에만 기반하며, 독립적인 생물학적 검증이 없습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 전체 예측 적응증 현황

TxGNN이 예측한 10가지 적응증 전체 현황입니다.

| 순위 | 적응증 | TxGNN 점수 | 근거 수준 | 임상시험 | 문헌 수 | 권장 결정 |
|------|--------|-----------|---------|---------|--------|---------|
| 1 | 마미증후군 (Cauda Equina Syndrome) | 99.60% | L5 | 0건 | 0편 | Hold |
| **2** | **개방각 녹내장 (Open-Angle Glaucoma)** | **99.59%** | **L3** | **1건** | **16편** | **Research Question** |
| 3 | 원발성 유전성 녹내장 (Primary Hereditary Glaucoma) | 99.56% | L5 | 0건 | 0편 | Hold |
| 4 | 탈모증 (Alopecia) | 99.55% | L4 | 1건 | 13편 | Hold |
| 5 | 선천성 소모증·속립진 (Congenital Hypotrichosis Milia) | 99.50% | L5 | 0건 | 0편 | Hold |
| 6 | 과민성 장증후군 (Irritable Bowel Syndrome) | 99.49% | L4 | 1건 | 15편 | ⚠️ Hold |
| 7 | 두피 단순 소모증 (Hypotrichosis Simplex of the Scalp) | 99.47% | L5 | 0건 | 0편 | Hold |
| 8 | 미만성 원형탈모 (Diffuse Alopecia Areata) | 99.45% | L5 | 0건 | 0편 | Hold |
| 9 | 편두통 (Migraine Disorder) | 99.27% | L4 | 1건 | 18편 | ⚠️ Hold |
| 10 | 뇌간 전조 편두통 (Migraine with Brainstem Aura) | 99.18% | L4 | 0건 | 2편 | Hold |

---

## 주목할 예측 — 개방각 녹내장 (Rank 2, L3)

10개 예측 중 **근거 수준이 가장 높은** 개방각 녹내장은 별도 검토가 필요합니다.

**기전 근거**: Glycerol은 혈장 삼투압을 상승시켜 유리체 탈수를 유도하고 안압(IOP)을 급성으로 낮추는 임상 기전이 역사적으로 활용되어 왔습니다. 섬모체 상피의 AQP3(수통관 단백-3)가 glycerol을 수송하여 방수(房水) 생성 동역학에 영향을 미칠 수 있다는 기초 연구도 있습니다.

**임상적 제한**: Glycerol의 IOP 강하 효과는 **급성이고 일시적**입니다. 만성 개방각 녹내장의 장기 치료에서 프로스타글란딘 유사체·β-차단제 등 1차 치료제를 대체할 수 없습니다.

### 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04676126](https://clinicaltrials.gov/study/NCT04676126) | Phase 4 | 취소 (WITHDRAWN) | 0 | 황반 색소 보충제와 시야 기능 관련 연구. Glycerin 직접 연구 아님 — 유효 증거 없음 |

### 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [4832172](https://pubmed.ncbi.nlm.nih.gov/4832172/) | 1974 | Clinical Report | Ann Ophthalmol | 개방각 녹내장 치료의 역사적 돌파구 — glycerin 임상 활용 초기 보고 |
| [6717920](https://pubmed.ncbi.nlm.nih.gov/6717920/) | 1984 | Clinical Study | Ophthalmology | 레이저 섬유주절개술 당일 안압 반응 관찰 (POAG, n=57) — 삼투압 조절 맥락 |
| [20872359](https://pubmed.ncbi.nlm.nih.gov/20872359/) | 2011 | Clinical Study | Eur J Ophthalmol | 삼투보호제(osmoprotection)가 녹내장 치료 중 안구 표면 손상 및 눈물막에 미치는 효과 |
| [3931670](https://pubmed.ncbi.nlm.nih.gov/3931670/) | 1985 | Clinical Study | Br J Ophthalmol | 레이저 섬유주절개술 후 초기 안압 반응 추적 (n=38) |
| [32890110](https://pubmed.ncbi.nlm.nih.gov/32890110/) | 2020 | Retrospective Case Series | J Glaucoma | Glycerin 보존 각막 공막 이식편의 GDD 수술 적용 — **glycerin은 보존제로 사용** |
| [22955016](https://pubmed.ncbi.nlm.nih.gov/22955016/) | 2014 | Retrospective Comparative | J Glaucoma | Glycerol 보존 각막 vs. 심낭막의 배액 튜브 피복 비교 — **glycerin은 보존제로 사용** |
| [41034373](https://pubmed.ncbi.nlm.nih.gov/41034373/) | 2025 | Metabolomics | Sci Rep | POAG 혈장에서 해당 과정 및 TCA 회로 이상 — 기초 과학, glycerin 간접 관련 |
| [32012845](https://pubmed.ncbi.nlm.nih.gov/32012845/) | 2020 | Data Mining | Metabolites | POAG 대사체학 탐색 연구 — 기초 과학 |

---

## 개별 적응증 특이사항

### ⚠️ 과민성 장증후군 (Rank 6) — 양방향 효과 경고

Glycerin 관장제는 IBS-C(변비형)에 국소 완하 효과를 나타내나, **PMID [8566580](https://pubmed.ncbi.nlm.nih.gov/8566580/)** (1996)은 장내 glycerol 주사가 복통 및 내장 과민성을 **유발하는** IBS 동물 모델로 활용됨을 보고합니다. **PMID [11396539](https://pubmed.ncbi.nlm.nih.gov/11396539/)** (2001) 역시 직장 내 glycerol 주사가 건강인에서 직장 팽창 과민성을 유발한다고 보고합니다. 투여 경로와 농도에 따라 완하 효과와 점막 자극/염증 유발이라는 반대 결과가 나타날 수 있어, 적응증 추진 전 경로별 안전성 재평가가 필수입니다.

### ⚠️ 편두통 (Rank 9) — 화학적 혼동 경고

편두통 연구에서 자주 등장하는 **"Glycerol Trinitrate"(GTN, 니트로글리세린)**는 CGRP 통로를 통해 편두통을 **유발하는** 실험 모델 물질입니다(PMID 38607011, 40380328). 이는 **Glycerin(글리세롤, 프로판-1,2,3-트리올)**과 화학 구조가 완전히 다른 별개의 물질이며, 두 물질을 혼동해서는 안 됩니다. 관련 문헌 18편 중 glycerin이 편두통 치료에 직접 기여한 연구는 없으며, 대부분 glycerin은 제형 내 부형제로만 등장합니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
10개 예측 적응증 중 1순위인 마미증후군은 생물학적 근거와 임상 증거가 전혀 없으며(L5), TxGNN 예측 점수는 지식 그래프 위상 추론에만 기반합니다. 가장 근거 수준이 높은 개방각 녹내장(Rank 2, L3)도 glycerol의 효과가 급성·일시적 IOP 강하에 국한되어 만성 치료 적응증으로의 확대는 추가 임상 연구가 필요합니다. 과민성 장증후군(Rank 6)은 오히려 증상 악화 가능성이, 편두통(Rank 9)은 화학적 혼동 문제가 있어 별도 평가가 선행되어야 합니다.

**진행하려면 필요한 것:**
- Glycerin의 DrugBank 공식 MOA 및 약물 분류 데이터 확인
- 개방각 녹내장의 급성 IOP 위기 처치에서 단기·간헐적 사용 임상 프로토콜 검토
- MFDS(식품의약품안전처) 허가사항 및 안전성 가이드라인 확인
- AQP3-glycerol 수송 기전과 방수 생성 관련 체계적 문헌 고찰
- 과민성 장증후군에서 투여 경로별(경구·직장) glycerin 효과 차이에 대한 안전성 재평가
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

