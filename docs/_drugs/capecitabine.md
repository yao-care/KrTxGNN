---
layout: default
title: Capecitabine
parent: 僅模型預測 (L5)
nav_order: 169
evidence_level: L5
indication_count: 10
---

# Capecitabine
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

# Capecitabine: 진행성 위선암에서 위분문부 선암(Gastric Cardia Adenocarcinoma)으로

## 한 문장 요약

Capecitabine은 경구용 fluoropyrimidine 계열 세포독성 항암제로, 이미 국제적으로 진행성·전이성 위선암 및 위식도접합부암(REAL-2 요법 등)의 표준 화학요법 일부로 확립되어 있습니다.
이번 평가에서 TxGNN 모델은 총 10건의 위암 관련 세부 적응증을 예측했으며, 그중 근거가 가장 강한 후보는 **위분문부 선암(Gastric Cardia Adenocarcinoma)**으로, 현재 **6건의 임상시험**(완료된 Phase 3 포함)과 **8편의 문헌**이 이를 지지합니다.
다만 한국(대만) 규제 자료상 이 약물은 **미시판** 상태이며, 안전성 라벨 정보(TFDA 경고/금기)가 확보되지 않아 안전성 초평가(S1) 진입이 차단된 상태(Blocking Data Gap)임을 함께 고지합니다.

> ⚠️ 본 평가팩(`TW-DB01101-multi`)은 10건의 예측 적응증을 포함한 다중 후보 팩입니다. 아래 본문은 근거 수준이 가장 높은 **위분문부 선암** 후보를 중심으로 작성하였으며, 나머지 9건은 보고서 말미 [부록]에 요약하였습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 전이성·진행성 위선암 및 위식도접합부암 표준 화학요법의 일부로 이미 확립 (국내 허가 자료는 없음) |
| 예측 신규 적응증 | 위분문부 선암 (Gastric Cardia Adenocarcinoma) |
| TxGNN 예측 점수 | 99.91% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 확보되지 않았습니다(Data Gap DG002, High severity). 다만 이번 평가에 포함된 근거 문헌 및 임상시험 정보를 종합하면, Capecitabine은 경구용 5-FU 전구약물로서 **thymidylate synthase를 억제하여 DNA 합성을 차단**하는 fluoropyrimidine 계열 표준 세포독성 화학요법 기전을 가진 것으로 확인됩니다.

위분문부 선암은 위선암의 해부학적 아형 중 하나로, 원위부(체부·유문부) 위암과 동일한 분자병리 및 화학요법 반응 기전을 공유합니다. 실제로 REAL-2 등 국제 대형 임상시험을 통해 capecitabine은 이미 위암 및 위식도접합부암 치료에서의 지위를 확립하였으며, 본 평가팩에 포함된 다수의 완료 임상시험(NCT00040859, NCT01295086 등)도 capecitabine을 위분문부/위식도접합부 선암에 직접 사용한 사례를 보여줍니다.

따라서 이 예측은 완전히 새로운 기전 적용이라기보다, **이미 검증된 위암 화학요법 범위를 해부학적으로 더 세분화된 하위 진단(분문부)까지 명확히 인정하는** 성격에 가깝습니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00040859](https://clinicaltrials.gov/study/NCT00040859) | Phase 2 | 완료 | 48 | Oxaliplatin+Capecitabine 병용요법을 전이성 식도/위식도접합부/위분문부 선암 환자에서 평가 (약물·적응증 직접 일치) |
| [NCT01295086](https://clinicaltrials.gov/study/NCT01295086) | 용량결정(NA) | 완료 | 27 | HER2 양성 절제불가 위·분문부·식도암 1차 치료로 Xeloda(Capecitabine)+Taxotere+Eloxatin+Herceptin 용량결정 연구 |
| [NCT00374036](https://clinicaltrials.gov/study/NCT00374036) | Phase 3 | 완료 | 416 | 전이성/국소진행성 위 및 분문부 선암에서 병용화학요법 순서를 비교한 대규모 Intergroup 3상 전략 연구 (capecitabine 포함 여부는 치료군 상세 확인 필요) |
| [NCT00938470](https://clinicaltrials.gov/study/NCT00938470) | Phase 2 | 완료 | 73 | 국소진행성 식도/위식도접합부/위분문부암에서 신조기 화학방사선요법 비교 (Docetaxel+Oxaliplatin+Capecitabine+Fluorouracil+방사선 vs Fluorouracil+Oxaliplatin+방사선) |
| [NCT00414271](https://clinicaltrials.gov/study/NCT00414271) | Phase 2 | 완료 | 18 | 국소진행성 위암 신조기 화학요법에서 thymidylate synthase 발현과 5-FU계 약물 반응성의 상관관계 평가 |
| [NCT07000253](https://clinicaltrials.gov/study/NCT07000253) | Phase 2/3 | 모집 예정 | 290 (예정) | 핍전이성 식도/위선암에서 1차 전신치료 후 국소치료(수술/방사선) 시행 시기를 비교하는 RCT (아직 모집 시작 전, capecitabine 특정 개입 아님) |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [16303863](https://pubmed.ncbi.nlm.nih.gov/16303863/) | 2006 | Phase 2 코호트 | Annals of Oncology | NCCTG Phase 2 연구: 전이성 식도/위식도접합부/위분문부 선암 1차 치료로 Oxaliplatin+Capecitabine 병용요법의 활성 확인 |
| [30692459](https://pubmed.ncbi.nlm.nih.gov/30692459/) | 2018 | 증례보고 | Gan to Kagaku Ryoho | 위분문부 종양(T4aN2M1) 환자에서 Capecitabine+Cisplatin(XP) 2주기 후 원발종양 및 림프절의 병리학적 완전관해(pCR) 달성 |
| [35895528](https://pubmed.ncbi.nlm.nih.gov/35895528/) | 2022 | 후향적 비교연구 | Magyar Sebeszet | 진행성 위식도접합부 선암 신조기 치료에서 ECX(Epirubicin+Cisplatin+Capecitabine) vs FLOT 요법의 단기 수술 성적 비교 |
| [28900996](https://pubmed.ncbi.nlm.nih.gov/28900996/) | 2017 | 후향적 코호트 | 中華胃腸外科雜誌 | 위 간양선암(hepatoid adenocarcinoma, 분문부 포함 증례) 임상병리학적 특징 및 예후 분석 |
| [38676903](https://pubmed.ncbi.nlm.nih.gov/38676903/) | 2024 | 증례보고 | Journal of Gastrointestinal Cancer | 4기 위선암 복막전이 환자에서 XELOX+HIPEC+항PD-1 면역치료 병용으로 병리학적 완전관해 달성 |
| [27123071](https://pubmed.ncbi.nlm.nih.gov/27123071/) | 2016 | 증례/문헌고찰 | Oncology Letters | AFP 생성 위암 증례(분문부 벽비후, 광범위 림프절 전이) |
| [38644313](https://pubmed.ncbi.nlm.nih.gov/38644313/) | 2024 | 증례보고 | Gan to Kagaku Ryoho | 다발성 간전이 동반 4기 위암(HER2 양성, 분문-체부 병변) 화학요법 후 원발종양 절제, 3.5년 무재발 생존 |
| [25731335](https://pubmed.ncbi.nlm.nih.gov/25731335/) | 2014 | 증례보고 | Gan to Kagaku Ryoho | 횡행결장암에서 전이한 드문 전이성 위암 증례, XELOX 화학요법 시행 |

---

## 한국 시판 정보

현재 국내(한국) 허가 자료가 없습니다 — 본 평가팩상 Capecitabine(DB01101)은 **미시판** 상태이며 등록된 허가증이 0건입니다.

---

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 화학요법제 (Fluoropyrimidine 계열, 경구 5-FU 전구약물) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | CBC(전혈구 수), 간·신기능, 전해질 (fluoropyrimidine 계열 표준 모니터링 항목) |
| 취급 방호 | 세포독성 항암제 취급 규정 준수 필요 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> 참고: TFDA 仿單 경고/금기 정보는 **Blocking 등급 데이터 갭(DG001)**으로 분류되어 있어, 안전성 초평가(S1) 단계 진입 자체가 현재 차단된 상태입니다. 약물상호작용(DDI) 조회도 결과 없음(not_found)으로 확인되었습니다.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
- 10건의 예측 후보 중 위분문부 선암이 유일하게 L1 근거 수준(완료된 Phase 3 포함, 다수의 Phase 2 직접 관련 시험)과 "Proceed with Guardrails" 권고를 받았습니다.
- 다만 이 결정은 **DG001(TFDA 라벨 경고/금기 정보 부재, Blocking)** 이 해소되기 전까지는 안전성 초평가(S1) 단계로 넘어갈 수 없다는 전제하의 조건부 진행입니다.

**진행하려면 필요한 것:**
- TFDA(또는 국내 규제기관) 공식 仿單 PDF 확보 및 경고·금기 정보 파싱 (DG001 해소, Blocking)
- DrugBank API 조회를 통한 상세 작용기전(MOA) 데이터 보강 (DG002)
- NCT00374036, NCT00938470 등 대형 시험에서 capecitabine이 실제 치료군에 포함되었는지 치료군 상세 재확인
- 국내(한국) 시판/허가 여부 재확인 — 현재 미시판 상태이므로 허가 경로 검토 필요
- 나머지 9개 저근거 후보(부록 참조)는 추가 임상/문헌 데이터 확보 전까지 Hold 또는 Research Question 상태 유지

---

## 부록: 전체 예측 후보 목록 (10건)

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 | 권장 결정 |
|------|------------|-----------|----------|----------|
| 1 | 위선암 및 근위부 위 용종증후군 (GAPPS) | 99.94% | L5 | Hold |
| 2 | 위관상선암 (Tubular Adenocarcinoma) | 99.94% | L4 | Research Question |
| 3 | 위印환세포암 (Signet Ring Cell) | 99.94% | L3 | Research Question |
| 4 | 미세침윤성 위암 | 99.94% | L5 | Hold |
| 5 | **위분문부 선암 (Gastric Cardia)** | 99.91% | **L1** | **Proceed with Guardrails** |
| 6 | 타액선형 위암종 | 99.91% | L4 | Research Question |
| 7 | 위유문부 암종 | 99.91% | L5 | Hold |
| 8 | 위체부 암종 | 99.90% | L3 | Research Question |
| 9 | EBV 관련 위암 | 99.90% | L5 | Hold |
| 10 | 악성 위 과립세포종 | 99.89% | L5 | Hold |

> 본 결과는 연구 참고용이며 의료적 조언을 구성하지 않습니다. 노약재창출 후보는 임상적 검증을 거쳐야 실제 적용이 가능합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

