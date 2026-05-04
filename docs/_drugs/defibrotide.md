---
layout: default
title: Defibrotide
parent: 僅模型預測 (L5)
nav_order: 201
evidence_level: L5
indication_count: 10
---

# Defibrotide
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

# Defibrotide: 간정맥 폐쇄증(VOD/SOS)에서 가성 폰 빌레브란트병으로

## 한 문장 요약

Defibrotide는 조혈모세포이식(HSCT) 후 발생하는 **간정맥 폐쇄증/동결혈증 증후군(VOD/SOS)** 치료제로 미국 FDA(2016년) 및 EMA에서 허가된 항혈전·내피 보호제입니다. TxGNN 모델은 **가성 폰 빌레브란트병(pseudo-von Willebrand disease)**에도 효과가 있을 수 있다고 99.91%의 높은 점수로 예측하였으나, 현재 이 방향을 지지하는 **임상시험 및 문헌이 전무**합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 간정맥 폐쇄증/동결혈증 증후군 (VOD/SOS) — HSCT 후 발생 |
| 예측 신규 적응증 | 가성 폰 빌레브란트병 (pseudo-von Willebrand disease) |
| TxGNN 예측 점수 | 99.91% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미상시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터(MOA)가 Evidence Pack에 누락되어 있습니다. 알려진 정보에 따르면, Defibrotide는 단일 가닥 폴리데옥시리보핵산(sodium polydeoxyribo­nucleotide)으로, **혈관 내피세포 보호·항혈전·항염증** 효과를 나타냅니다. 구체적으로 프로스타사이클린(PGI₂) 및 조직 플라스미노겐 활성인자(tPA)를 상향 조절하고, 플라스미노겐 활성인자 억제제-1(PAI-1)을 하향 조절하여 혈관 내 혈전 형성을 억제하는 것으로 알려져 있습니다.

가성 폰 빌레브란트병(pseudo-vWD)은 혈소판 막 단백질 GPIb-α가 vWF(폰 빌레브란트 인자)에 비정상적으로 높은 친화력을 보여 고분자량 vWF 다량체가 지속적으로 소모되는 혈소판 기능 이상 질환입니다. 주요 임상 표현은 **출혈 경향**이며, 치료 원칙은 vWF 보충이 아닌 혈소판-vWF 과도 결합의 억제입니다.

**기전 연결 고리는 매우 약합니다.** Defibrotide는 GPIb-vWF 축에 직접 작용하는 기전이 알려진 바 없으며, 오히려 항혈전 성질이 이미 출혈 경향을 가진 환자에서 안전성 우려를 가중시킬 수 있습니다. TxGNN 예측 점수가 높은 것은 혈소판 관련 질환군과의 네트워크 유사성에 기인할 가능성이 높으나, 이는 임상적 타당성을 보장하지 않습니다.

---

## 임상시험 근거

현재 가성 폰 빌레브란트병에 대한 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 가성 폰 빌레브란트병에 대한 관련 문헌이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
가성 폰 빌레브란트병에 대한 임상시험 및 문헌 근거가 전무하며(L5), Defibrotide의 항혈전 기전은 이 출혈성 질환의 병태생리와 기전적으로 상충합니다.

**진행하려면 필요한 것:**
- Defibrotide MOA 상세 데이터 확보 (DrugBank API 조회 필요)
- 한국/대만 허가사항 안전성 데이터 확보 (TFDA 仿單 PDF 파싱 필요)
- pseudo-vWD 및 GPIb-vWF 축에 대한 전임상 연구

---

---

## 📊 전체 예측 적응증 요약 (Top 10)

> ⚠️ **candidate_id: multi** — 이 Evidence Pack은 10개 예측 적응증을 포함합니다. 전체 현황은 아래 표를 참조하세요.

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 | 임상시험 | 문헌 | 권장 결정 | 기전 적합성 |
|-----|-----------|-----------|---------|---------|-----|---------|-----------|
| 1 | 가성 폰 빌레브란트병 | 99.91% | L5 | 0건 | 0편 | Hold | ❌ 약함 (출혈 질환에 항혈전제) |
| 2 | 혈소판 원발성 방출 장애 | 99.91% | L4 | 1건 ⚠️ | 0편 | Hold | ⚠️ 간접적 (PGI₂/TxA₂ 조절) |
| 3 | Glanzmann 혈소판무력증 | 99.88% | L5 | 0건 | 0편 | Hold | ❌ 역방향 (출혈 가중 우려) |
| **4** | **혈전성 혈소판감소성 자반증 (TTP)** | **99.71%** | **L3** | **0건** | **11편** | **Research Question** | **✅ 부분 적합 (TA-TMA 맥락)** |
| 5 | Scott 증후군 | 99.67% | L5 | 0건 | 0편 | Hold | ❌ 역방향 (출혈 경향 질환) |
| 6 | 콜라겐 수용체 결함 출혈 체질 | 99.43% | L5 | 0건 | 0편 | Hold | ❌ 역방향 |
| 7 | 선천성 혈소판감소증 출혈 장애 | 99.39% | L5 | 0건 | 0편 | Hold | ❌ 역방향 (출혈 가중 우려) |
| 8 | 선천성 Factor V 결핍증 | 99.30% | L5 | 0건 | 0편 | Hold | ❌ 역방향 (출혈 위험 금기) |
| 9 | 태아·신생아 동종면역 혈소판감소증 | 99.23% | L5 | 0건 | 0편 | Hold | ❌ 기전 연결 없음 (IVIG 표준) |
| **10** | **혈소판감소성 자반증** | **99.22%** | **L3** | **0건** | **11편** | **Research Question** | **⚠️ TTP 아형 한정 (ITP 연결 약함)** |

> ⚠️ **rank 2의 임상시험(NCT02851407)**: Phase 3 VOD/SOS 예방 시험으로, 혈소판 방출 장애와 직접적 연관 없음. 등록된 맥락(내피 손상·혈소판 활성화)으로 인해 해당 적응증에 귀속된 것임.

---

## 🔍 심층 분석: 혈전성 혈소판감소성 자반증(TTP) — Rank 4

> **근거 수준 L3 · 권장: Research Question**
> 10개 예측 중 실질적 문헌 근거가 가장 풍부한 적응증입니다.

### 이 예측이 타당한 이유는? (TTP 맥락)

TTP는 ADAMTS13 효소 결핍 또는 기능 장애로 인해 초고분자량 vWF 다량체가 축적되어 미세혈관 내 혈전이 형성되는 혈전성 미세혈관병증(TMA)입니다. HSCT 후 발생하는 이식 관련 TMA(TA-TMA)는 화학요법·방사선·면역억제제로 인한 **혈관 내피 손상**이 주요 병인입니다.

Defibrotide의 핵심 기전인 **내피세포 보호, tPA 증가, PAI-1 억제**는 바로 TA-TMA의 핵심 병인과 기전적으로 맞닿아 있습니다. 이는 Defibrotide가 이미 허가된 VOD/SOS의 병인(내피 손상 기반)과 TA-TMA가 공통된 병태생리를 공유한다는 점에서 생물학적 타당성이 상당합니다.

단, 특발성 TTP(idiopathic TTP, ADAMTS13 자가면역 기전)에서는 내피 보호 기전만으로 충분하지 않을 수 있으며, 병인 이질성이 커 모든 TTP 아형에 동일하게 적용하기 어렵습니다.

### 문헌 근거 (TTP, rank 4)

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [37001283](https://pubmed.ncbi.nlm.nih.gov/37001283/) | 2023 | 시험관 내 연구 | Thrombosis Research | Defibrotide가 COVID-19 및 관련 혈관병증(TTP, aHUS, VOD) 환자 혈장에 의해 유발된 미세혈관 내피세포 손상을 완화 — 내피 보호 기전 직접 확인 |
| [11960280](https://pubmed.ncbi.nlm.nih.gov/11960280/) | 2002 | 사례 시리즈 | Bone Marrow Transplantation | BMT 후 TTP 환자에서 Defibrotide의 유망한 치료 효과 보고 |
| [10775024](https://pubmed.ncbi.nlm.nih.gov/10775024/) | 2000 | 사례 보고/소규모 | Clin Appl Thromb Hemost | 재발성 TTP 치료에서 Defibrotide 사용, 중장기 관해 유도 접근 |
| [8317470](https://pubmed.ncbi.nlm.nih.gov/8317470/) | 1993 | 증례 보고 | Am J Hematol | TTP에서 Defibrotide 치료 증례 |
| [6547211](https://pubmed.ncbi.nlm.nih.gov/6547211/) | 1984 | 사례 시리즈 | Nephron | HUS 및 TTP로 인한 급성 신부전에서 항혈전제(Defibrotide) 조기 사용 보고 |
| [3754836](https://pubmed.ncbi.nlm.nih.gov/3754836/) | 1986 | 연구 | Haemostasis | 혈전성 미세혈관병증 동반 급성 신부전에서 Defibrotide 효과 |
| [11100281](https://pubmed.ncbi.nlm.nih.gov/11100281/) | 2000 | 후향적 코호트 | Bone Marrow Transplantation | BMT 받은 소아 백혈병 환자 131명에서 TTP 발생 빈도 및 위험 인자 분석 |
| [19228075](https://pubmed.ncbi.nlm.nih.gov/19228075/) | 2009 | 리뷰 | Drugs | HSCT에서 이식 관련 혈전성 미세혈관병증(TA-TMA) 진단 및 치료 종합 리뷰 |
| [17603513](https://pubmed.ncbi.nlm.nih.gov/17603513/) | 2007 | 리뷰 | Bone Marrow Transplantation | TA-TMA 진단 및 치료 현황 — 병태생리 이해 부족으로 인한 한계 논의 |
| [30305540](https://pubmed.ncbi.nlm.nih.gov/30305540/) | 2018 | 리뷰/가이드라인 | 日本臨床血液學會誌 | 이식 관련 TMA 관리 가이드라인 — 내피 손상 기전 중심 |

> ⚠️ **안전 신호 주의:** [PMID 7896218](https://pubmed.ncbi.nlm.nih.gov/7896218/) (Haematologica, 1994) — Defibrotide **치료 후** TTP 발생이 보고된 이상반응 사례입니다. TTP 적응증에서의 사용은 이 역설적 신호를 반드시 사전 검토해야 합니다.

### TTP 소결론

**결정: Research Question**

Defibrotide의 내피 보호·항혈전 기전은 **HSCT 후 TA-TMA/TTP 맥락**에서 생물학적으로 합리적이며, 1984년부터 2023년까지 다수의 증례·기전 연구·리뷰 문헌이 이를 지지합니다. 그러나 다음 한계로 인해 현재 Research Question 단계에 머뭅니다:

- **병인 이질성:** TA-TMA와 idiopathic TTP(ADAMTS13 자가면역)에서 효능 예측 불일치
- **역설적 안전 신호:** Defibrotide 투여 후 TTP 발생 보고(PMID 7896218)
- **전향적 연구 부재:** 기존 근거 전체가 소규모 증례 및 리뷰에 한정

**다음 단계:**
- HSCT 후 TA-TMA를 명확히 타겟으로 하는 전향적 파일럿 연구 설계
- ADAMTS13 활성도를 기반으로 한 TTP 아형 계층화 분석
- Defibrotide MOA 상세 데이터(DrugBank) 및 안전성 프로파일(TFDA 仿單) 확보
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

