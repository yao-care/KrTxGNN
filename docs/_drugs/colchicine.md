---
layout: default
title: Colchicine
parent: 僅模型預測 (L5)
nav_order: 184
evidence_level: L5
indication_count: 3
---

# Colchicine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Colchicine: 통풍 치료에서 열대열 말라리아·가족성 지중해열로

---

## 한 문장 요약

Colchicine은 수천 년 역사의 식물 유래 알칼로이드로, 전 세계적으로 통풍 급성 발작 및 가족성 지중해열(FMF) 치료에 사용되나 **한국 내 현재 미등록 상태**입니다.
TxGNN 모델은 **열대열 말라리아**(Rank 1, 99.60%), **가족성 지중해열 자가우성형**(Rank 2, 99.38%), **피부섬유육종**(Rank 3, 99.37%) 세 적응증을 예측하며, FMF는 **1건의 임상시험**과 **20편의 문헌**이 지지하고, 말라리아는 **6편의 전임상 문헌**만 확인됩니다.
FMF는 Colchicine의 국제적 표준 치료로 확립되어 있어 국내 허가 검토 가치가 높으며, 말라리아 예측은 기전적으로 흥미롭지만 임상 적용을 위해서는 상당한 추가 연구가 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 국내 미등록 (글로벌: 통풍, 가족성 지중해열) |
| 1순위 예측 적응증 | 열대열 말라리아 (Plasmodium falciparum malaria) |
| TxGNN 예측 점수 (Rank 1) | 99.60% |
| 근거 수준 (Rank 1) | L4 — 전임상·기전 연구 |
| 한국 시판 현황 | ✗ 미등록 |
| 허가증 수 | 0건 |
| 권장 결정 (Rank 1) | Research Question |

---

## 다중 적응증 요약

| 순위 | 적응증 | TxGNN 점수 | 근거 수준 | 권장 결정 |
|------|--------|-----------|---------|---------|
| 1 | 열대열 말라리아 (*Plasmodium falciparum* malaria) | 99.60% | L4 | Research Question |
| 2 | 가족성 지중해열 자가우성형 (FMF, autosomal dominant) | 99.38% | L1 | Proceed with Guardrails |
| 3 | 피부섬유육종 (Dermatofibrosarcoma protuberans) | 99.37% | L5 | Hold |

---

## 이 예측이 타당한 이유는?

### Rank 1: 열대열 말라리아

현재 상세한 작용 기전 데이터가 없으나(Data Gap), Colchicine은 β-tubulin에 결합하여 미세소관 중합을 억제하는 약물로 널리 알려져 있습니다.

*Plasmodium falciparum*은 분열소자 분열 및 적혈구 침입에 필수적인 기능적 α/β-tubulin 시스템을 보유합니다. 여러 미세소관 표적 화합물(tubulozoles, 세포골격 결합제)이 *P. falciparum*에 대한 체외 항말라리아 활성을 보인다는 문헌들이 간접적인 기전 근거를 제공합니다. 1990년 Dieckmann-Schuppert 등은 Colcemid(콜히친 유도체)와 tubulozole이 유사한 단백질 합성 억제 효과를 보임을 보고하였습니다.

그러나 Colchicine 자체의 치료 혈중 농도(ng/mL 수준)가 항말라리아 유효 농도(통상 μM 수준)에 도달하기 어렵고, 치료 지수가 극히 좁다는 심각한 용량 창(dosing window) 문제가 있습니다. 이 예측은 기전적으로 흥미롭지만 임상 적용을 위해서는 직접적인 체외·체내 효능 연구가 선행되어야 합니다.

### Rank 2: 가족성 지중해열 (FMF)

FMF는 MEFV 유전자 돌연변이로 인해 Pyrin 단백질 기능이 비정상화되어 NLRP3/Caspase-1 염증소체가 과도하게 활성화되고, IL-1β 과다 분비 및 호중구 매개 장막염을 반복적으로 유발하는 자가염증 질환입니다.

Colchicine은 이 병태생리에 다중 기전으로 작용합니다: ① 미세소관 억제 → 호중구 화학주성 및 탈과립 차단, ② NLRP3 염증소체 조립 억제 → IL-1β 분비 감소, ③ E-selectin 발현 억제 → 호중구 조직 침투 감소. 이는 FMF에서 Colchicine이 국제 표준 치료로 확립된 명확한 기전적 근거이며, 1977년 Lancet 랜드마크 논문 이후 수십 년간 근거가 축적되어 있습니다.

### Rank 3: 피부섬유육종 (DFSP)

DFSP의 주요 발암 기전은 COL1A1-PDGFB 융합 유전자로 인한 PDGF 신호 과활성화입니다. Colchicine의 미세소관 파괴가 광범위한 항증식 효과를 나타낼 수 있으나, DFSP 표준 치료(수술 절제 + Imatinib)에 비해 기전 특이성이 현저히 낮고 이를 지지하는 문헌 또는 전임상 데이터가 전무합니다. TxGNN의 높은 점수(0.9937)는 지식 그래프 내 일반적인 "항증식제 → 종양" 일반화 관련성을 반영할 가능성이 높습니다.

---

## 임상시험 근거

### Rank 1: 열대열 말라리아

현재 관련 임상시험 등록이 없습니다.

### Rank 2: 가족성 지중해열

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT06838143](https://clinicaltrials.gov/study/NCT06838143) | N/A | 모집 중 | 25 | Canakinumab(IL-1β 단클론항체)을 Colchicine 내성·불내성 FMF 포함 유전성 주기열 증후군 환자에게 투여하는 실사용 관찰 연구. Colchicine 실패가 입상 조건으로, Colchicine의 FMF 표준치료 지위를 간접 확인 |

### Rank 3: 피부섬유육종

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

### Rank 1: 열대열 말라리아

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [2221861](https://pubmed.ncbi.nlm.nih.gov/2221861/) | 1990 | 체외 기전 연구 | Antimicrob Agents Chemother | Tubulozole 계열의 항말라리아 기전 탐색; Colcemid(미세소관 억제제)과 유사한 단백질 합성 억제 효과 관찰 — Colchicine과 기전적 연관성 가장 직접적 |
| [2670249](https://pubmed.ncbi.nlm.nih.gov/2670249/) | 1989 | 체외 스크리닝 | Cell Biol Int Rep | 9종 튜불린 결합 물질의 *P. falciparum* 적혈구 내 발달 억제; 포유류 tubulin과 말라리아 원충 tubulin의 분자적 차이 확인 |
| [2655935](https://pubmed.ncbi.nlm.nih.gov/2655935/) | 1989 | 체외 스크리닝 | Cell Biol Int Rep | 세포골격 결합 화합물의 *P. falciparum* 체외 억제 활성 확인 (위 연구 후속) |
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | 체외 기전 연구 | PLoS One | Curcumin의 *P. falciparum* 미세소관 구조 교란 효과 — 미세소관 표적 항말라리아 전략에 대한 간접 지지 (Colchicine과 직접 관련 낮음) |
| [6362934](https://pubmed.ncbi.nlm.nih.gov/6362934/) | 1984 | 임상 면역 연구 | Clin Exp Immunol | 급성 말라리아 환자 혈청에서 중간세사(intermediate filament) 자가항체 검출 — 말라리아와 세포골격 단백질의 연관성 시사 |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | 분자생물학 | Mol Cell Biol | *P. falciparum* pfmdr1 유전자의 클로로퀸 내성 관련 연구 — Colchicine과 직접 관련 낮음, 참고 수준 |

### Rank 2: 가족성 지중해열

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [68234](https://pubmed.ncbi.nlm.nih.gov/68234/) | 1977 | 임상시험 | Lancet | **랜드마크 논문**: Colchicine의 FMF 발작 예방 유효성 최초 보고 — 이후 수십 년간 표준 치료 근거의 출발점 |
| [37298536](https://pubmed.ncbi.nlm.nih.gov/37298536/) | 2023 | Review | Int J Mol Sci | FMF 최신 업데이트: 치료 내성·순응도 포함 포괄적 고찰, Colchicine 표준 치료 지위 재확인 |
| [30686512](https://pubmed.ncbi.nlm.nih.gov/30686512/) | 2019 | Review | Presse Med | FMF 병태생리·진단·치료 전반; Colchicine의 발작 및 아밀로이드증 예방 효과 기술 |
| [28413100](https://pubmed.ncbi.nlm.nih.gov/28413100/) | 2017 | Review | Semin Arthritis Rheum | FMF에서 Colchicine 내성·불내성의 정의, 원인, 대안 치료 정리; Colchicine 금표준(gold standard) 지위 명시 |
| [38354004](https://pubmed.ncbi.nlm.nih.gov/38354004/) | 2023 | Review | Rev Prat | FMF 진단·치료 가이드; Colchicine의 장기 발작 예방 효과 및 소아 환자 적용 강조 |
| [37903671](https://pubmed.ncbi.nlm.nih.gov/37903671/) | 2023 | 가이드라인/프로토콜 | Rev Med Interne | 프랑스 FMF 진단·관리 공식 프로토콜; Colchicine 1차 치료 권고 명시 |
| [20586571](https://pubmed.ncbi.nlm.nih.gov/20586571/) | 2010 | Review/독성학 | Clin Toxicol | Colchicine 중독의 임상 스펙트럼 — 좁은 치료 지수, 의도치 않은 독성 위험, 치명적 용량 경계 불명확성 상세 기술 |
| [35789271](https://pubmed.ncbi.nlm.nih.gov/35789271/) | 2023 | 코호트 | Mod Rheumatol | FMF 환자에서 Colchicine 내성 조기 예측 인자 탐색 — 내성 발생 위험 환자 선별 기준 제시 |
| [40040547](https://pubmed.ncbi.nlm.nih.gov/40040547/) | 2025 | 코호트 | Int J Rheum Dis | FMF 환자에서 Canakinumab 단독 vs. Colchicine 병용 비교: 발작 특성, 급성기 반응물, 신장 예후 분석 |
| [35061158](https://pubmed.ncbi.nlm.nih.gov/35061158/) | 2022 | 후향적 코호트 | Int Emerg Med | 늦은 발병 FMF(40세 이후) 환자 분석: Colchicine 반응 및 임상·유전 특성 비교 |

### Rank 3: 피부섬유육종

현재 관련 문헌이 없습니다.

---

## 한국 시판 정보

현재 한국 내 Colchicine 허가 기록이 **없습니다** (미등록 약물).

전 세계적으로는 통풍 및 FMF 치료제로 미국(FDA), 유럽(EMA), 일본(PMDA) 등 다수 국가에서 허가되어 시판 중입니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> **중요 주의사항**: Colchicine은 치료 지수가 극히 좁은 약물로, 독성·사망 사례 보고가 있습니다. 비독성 용량, 독성 용량, 치명 용량 간의 경계가 불명확하여 임상 혼란을 초래할 수 있습니다 (PMID [20586571](https://pubmed.ncbi.nlm.nih.gov/20586571/) 참고). 현재 데이터 갭(DG001: 경고/금기, DG002: 작용 기전)이 존재하며, 안전성 평가 진행 전 반드시 해결이 필요합니다.

---

## 결론 및 다음 단계

---

### Rank 1: 열대열 말라리아

**결정: Research Question**

**사유:**
기전적으로 흥미로운 가설이나, 체외 연구 수준의 간접 증거만 존재하며 치료 혈중 농도 대비 항말라리아 유효 농도 간 심각한 용량 창 문제가 미해결 상태입니다.

**진행하려면 필요한 것:**
- Colchicine 자체의 *P. falciparum* 직접 체외 IC₅₀ 측정 연구
- 치료 혈중 농도 대비 항말라리아 유효 농도 비교 분석
- 동물 말라리아 모델(마우스 *P. berghei* 등)에서의 체내 효능 확인

---

### Rank 2: 가족성 지중해열 (FMF)

**결정: Proceed with Guardrails**

**사유:**
Colchicine은 FMF의 국제 금표준 치료제로 1977년부터 근거가 축적되어 있으며, 다수의 가이드라인 권고 문헌이 존재합니다. 한국 내 미등록 상태이나 확립된 근거를 감안할 때 국내 허가 신청 검토 가치가 높습니다.

**진행하려면 필요한 것:**
- **DG001 해결**: TFDA/MFDS 허가사항 PDF 확보 및 경고·금기 데이터 추출 (Blocking 데이터 갭)
- **DG002 해결**: DrugBank API 조회를 통한 작용 기전 데이터 보완
- 한국 FMF 환자 유병률 및 역학 데이터 확인
- 주요 MEFV 돌연변이 유형별 Colchicine 반응성 데이터 검토
- 국내 허가 신청 전략 수립 (희귀질환 지정 여부 포함)

---

### Rank 3: 피부섬유육종 (DFSP)

**결정: Hold**

**사유:**
지지 문헌 및 임상시험이 전무하며, 기전 특이성이 현행 표준 치료(Imatinib)에 비해 현저히 낮습니다. TxGNN 고점수는 지식 그래프 내 일반적 항증식-종양 관련성의 일반화를 반영할 가능성이 높습니다.

**진행하려면 필요한 것:**
- 현 단계에서 추가 투자 불필요; 향후 DFSP-특이적 미세소관 의존성 연구 결과 출현 시 재검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

