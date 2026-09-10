---
layout: default
title: Gemcitabine
parent: 僅模型預測 (L5)
nav_order: 344
evidence_level: L5
indication_count: 10
---

# Gemcitabine
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

# Gemcitabine: 적응증 정보 없음에서 유방암(Female Breast Carcinoma)으로

## 한 문장 요약

Gemcitabine(DB00441)은 deoxycytidine 뉴클레오시드 유사체 계열의 세포독성 항암제입니다. 다만 이번 Evidence Pack에는 기존 승인 적응증 및 정식 작용기전(MOA) 데이터가 확보되지 않았습니다. TxGNN 모델은 **유방암(Female Breast Carcinoma)**에 효과가 있을 수 있다고 예측하며, 현재 직접 등록된 임상시험은 없지만 **20편의 문헌**(paclitaxel·carboplatin·trastuzumab 등과의 병용 경험 포함)이 이 방향을 지지합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 자료 없음 (Evidence Pack에 미기재) |
| 예측 신규 적응증 | 유방암 (Female Breast Carcinoma) |
| TxGNN 예측 점수 | 99.98% (rank 800) |
| 근거 수준 | L2 |
| 한국(대만) 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

정식 MOA 필드는 데이터 갭이지만, Evidence Pack의 기전 근거(repurposing rationale)는 다음과 같이 설명합니다.

Gemcitabine은 deoxycytidine 뉴클레오시드 유사체로, ribonucleotide reductase를 억제하고 DNA에 삽입되어 사슬종결을 유발함으로써 빠르게 분열하는 세포에 세포독성 효과를 나타냅니다. 이 기전은 유방암 세포처럼 증식 속도가 빠른 종양 세포에도 적용 가능합니다.

실제로 임상 실무에서는 이미 paclitaxel, carboplatin, docetaxel, trastuzumab 등과 병용되어 전이성 유방암 치료에 폭넓게 사용된 경험이 문헌으로 축적되어 있으며, 이는 TxGNN 예측의 기전적 타당성을 뒷받침합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다. (ClinicalTrials.gov, ICTRP 조회 결과 모두 0건)

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [40779028](https://pubmed.ncbi.nlm.nih.gov/40779028/) | 2025 | 병용요법 시험 | Breast Cancer Res Treat | Carboplatin+Gemcitabine+Mifepristone Phase I, GR 양성 유방암/난소암 대상 |
| [38262235](https://pubmed.ncbi.nlm.nih.gov/38262235/) | 2024 | Phase 1 | Gynecologic Oncology | Mirvetuximab soravtansine + Gemcitabine, FRα양성 삼중음성유방암 포함 MTD 평가 |
| [25398698](https://pubmed.ncbi.nlm.nih.gov/25398698/) | 2015 | Phase 2 (단일군 구제요법) | Cancer Chemother Pharmacol | Docetaxel+Gemcitabine+Bevacizumab, HER2음성 전이성 유방암 |
| [14768404](https://pubmed.ncbi.nlm.nih.gov/14768404/) | 2003 | Review | Oncology (Williston Park) | Gemcitabine과 anthracycline/taxane 병용요법 개관 |
| [15685821](https://pubmed.ncbi.nlm.nih.gov/15685821/) | 2004 | Review | Oncology (Williston Park) | 전이성 유방암에서 Gemcitabine+백금계 병용 화학요법 |
| [24295415](https://pubmed.ncbi.nlm.nih.gov/24295415/) | 2013 | Review | Future Oncology | 리포좀 제형 화학요법제 개관, Gemcitabine 사례 포함 |
| [15685819](https://pubmed.ncbi.nlm.nih.gov/15685819/) | 2004 | Review | Oncology (Williston Park) | 전이성 유방암에서 Gemcitabine+Paclitaxel 병용 리뷰 |
| [34580061](https://pubmed.ncbi.nlm.nih.gov/34580061/) | 2021 | 전임상 | Cancer Research | ALDH1A1 활성과 유방암 진행 관련 기전 연구 |
| [12057039](https://pubmed.ncbi.nlm.nih.gov/12057039/) | 2002 | 전임상 | Clinical Breast Cancer | Gemcitabine+Trastuzumab, 유방암/폐암 세포주 전임상 연구 |
| [15685824](https://pubmed.ncbi.nlm.nih.gov/15685824/) | 2004 | 전임상 | Oncology (Williston Park) | HER2 과발현 유방암 세포에서 Gemcitabine+Trastuzumab±백금계 상호작용 |

## 한국(대만) 시판 정보

한국(대만) 내 등록된 시판 허가 정보가 없습니다. (market_status: 미출시, 허가증 0건)

## 세포독성

Gemcitabine은 뉴클레오시드 유사체 계열의 세포독성 항암제로 판단됩니다 (기전 근거: DNA 사슬종결, 빠르게 분열하는 세포에 대한 세포독성 — 위 "예측이 타당한 이유" 참조).

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 항암제 (뉴클레오시드 유사체/항대사물질) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 (구체적 독성 자료 없음) |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | CBC(백혈구·혈소판 포함), 간·신기능 (세포독성 항암제 일반 모니터링 원칙) |
| 취급 방호 | 세포독성 의약품 표준 취급 규정 준수 필요 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
직접 등록된 임상시험은 없으나, paclitaxel·carboplatin·trastuzumab 등과의 병용을 통해 전이성 유방암에서 축적된 다수의 Phase 1/2 임상 경험과 리뷰 문헌이 존재하여 근거 수준 L2로 평가되었습니다. 다만 기존 적응증 및 MOA, 안전성 데이터의 공백이 있어 무조건적 진행은 시기상조입니다.

**진행하려면 필요한 것:**
- TFDA(또는 해당 관할 규제기관) 허가사항의 경고·금기 정보 확보 (DG001, Blocking)
- DrugBank 등에서 정식 작용기전(MOA) 데이터 확보 (DG002, High)
- 기존 승인 적응증 정보 확인 (현재 Evidence Pack에 미기재)
- 한국(또는 대만) 내 시판/허가 현황 최신화 확인 (현재 미출시)
- 유방암 적응증에 특화된 전향적 임상시험 설계 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

