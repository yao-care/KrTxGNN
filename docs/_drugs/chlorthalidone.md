---
layout: default
title: Chlorthalidone
parent: 僅模型預測 (L5)
nav_order: 161
evidence_level: L5
indication_count: 10
---

# Chlorthalidone
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

# Chlorthalidone: 고혈압에서 원발성 유전성 녹내장으로

---

## 한 문장 요약

Chlorthalidone은 원위 세뇨관의 Na-Cl 공동수송체(NCC)를 억제하는 티아지드 유사 이뇨제로, 고혈압 치료에 오랫동안 사용되어 온 약물입니다. TxGNN 모델은 **원발성 유전성 녹내장(Primary Hereditary Glaucoma)**을 비롯한 10개 신규 적응증을 예측하였으나, 이를 직접 지지하는 임상 근거는 매우 제한적이며, 가장 강한 직접 근거(L3)는 **만성 폐성 심장병(Rank 8)**에 대한 역사적 임상 연구 2건에 그칩니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 고혈압 (한국 내 허가 미보유) |
| 예측 신규 적응증 (Rank 1) | 원발성 유전성 녹내장 (Primary Hereditary Glaucoma) |
| TxGNN 예측 점수 | 99.92% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 전체 예측 적응증 요약

| 순위 | 적응증 | TxGNN 점수 | 근거 수준 | 권장 결정 |
|------|--------|-----------|----------|---------|
| 1 | 원발성 유전성 녹내장 (Primary Hereditary Glaucoma) | 99.92% | L5 | Hold |
| 2 | 개방각 녹내장 (Open-Angle Glaucoma) | 99.90% | L5 | Hold |
| 3 | 악성 신혈관성 고혈압 (Malignant Renovascular Hypertension) | 99.89% | L4 | Research Question |
| 4 | 악성 고혈압성 신장병 (Malignant Hypertensive Renal Disease) | 99.89% | L4 | Research Question |
| 5 | 폐 질환/저산소증에 의한 폐고혈압 (PH Group 3) | 99.88% | L5 | Hold |
| 6 | 불명 다인자 기전 폐고혈압 (PH Group 5) | 99.88% | L5 | Hold |
| 7 | Braddock 증후군 | 99.85% | L5 | Hold |
| **8** | **만성 폐성 심장병 (Chronic Pulmonary Heart Disease)** | **99.82%** | **L3** | **Research Question** |
| 9 | 급성 폐성 심장병 (Acute Pulmonary Heart Disease) | 99.32% | L4 | Hold |
| 10 | 선천성 모발 희소증-비립종 (Congenital Hypotrichosis Milia) | 99.19% | L5 | Hold |

---

## 이 예측이 타당한 이유는? (Rank 1: 원발성 유전성 녹내장)

현재 상세한 DrugBank 작용 기전 데이터가 수집되지 않았습니다. 알려진 정보에 따르면, Chlorthalidone은 티아지드 유사 이뇨제로 원위 세뇨관의 Na-Cl 공동수송체(NCC)를 억제하여 나트륨·수분 배설을 증가시키고, 혈액량 및 말초 혈관 저항 감소를 통해 혈압을 낮추는 약물입니다.

이론적으로 티아지드 유사 이뇨제는 안방수(aqueous humor) 생성 감소를 통해 안압(IOP)을 경미하게 낮출 수 있습니다. 그러나 이 효과는 탄산탈수효소 억제제(acetazolamide)에 비해 효력이 현저히 약하며, 임상적으로 유의미한 안압 강하로 이어지기 어렵습니다.

원발성 유전성 녹내장의 핵심 병리는 MYOC, OPTN 등의 유전자 돌연변이로 인한 구조적 방각(房角) 발육 이상입니다. 이는 단순한 안압 조절 문제가 아닌 유전적 구조 결함에 기인하므로, chlorthalidone의 이뇨 기전이 해당 유전 병리에 직접 작용할 가능성은 낮은 것으로 평가됩니다. TxGNN의 고점수는 지식 그래프 내 녹내장-안압-이뇨제 노드 간의 간접 연결에서 비롯된 것으로 추정됩니다.

---

## 임상시험 근거 (Rank 1: 원발성 유전성 녹내장)

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거 (Rank 1: 원발성 유전성 녹내장)

현재 관련 문헌이 없습니다.

---

## 심층 분석: 만성 폐성 심장병 (Rank 8 — 최고 근거 수준 L3)

이 팩에서 가장 강한 직접 근거를 보유한 적응증입니다. Chlorthalidone을 직접 사용한 역사적 임상 연구가 존재하여 L3 수준으로 분류됩니다.

### 기전적 연관성

만성 폐성 심장병(폐심증, Cor Pulmonale)은 만성 폐질환으로 인한 폐 혈관 저항 증가 → 우심실 비대 → 우심부전으로 이어지는 병태입니다. Chlorthalidone은 장효 이뇨제(반감기 ~40–60시간)로서 체순환 울혈 및 말초 부종을 동반한 우심부전에서 전부하(preload)를 감소시켜 증상을 완화하는 역할을 할 수 있습니다. 다만 현대 관리에서는 SGLT2 억제제, 사쿠비트릴/발사르탄 등 새로운 치료 옵션이 등장하였으므로, 이들과의 비교 위치 설정이 필요합니다.

### 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT05580510](https://clinicaltrials.gov/study/NCT05580510) | Phase 2/3 | 불명 | 160 | 선천성 심장병 관련 심부전에서 Empagliflozin + Sacubitril/Valsartan 평가. Chlorthalidone을 포함하지 않아 직접 근거로 활용 불가; 해당 적응증의 현대적 임상 활동을 간접적으로 보여줌 |

### 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [5597001](https://pubmed.ncbi.nlm.nih.gov/5597001/) | 1967 | 역사적 임상 연구 (증례군) | La Clinica terapeutica | 만성 폐심병 유발 울혈성 심부전에 Chlorthalidone 이뇨 요법을 직접 적용한 보고 — 이 팩에서 유일한 Chlorthalidone 직접 근거 |
| [431831](https://pubmed.ncbi.nlm.nih.gov/431831/) | 1979 | 역사적 임상 연구 | Minerva medica | 만성 기관지폐질환 환자 5명에 depletion 요법(이뇨제 포함) 적용 시 방사선·임상·기능 변화 관찰; 간접적 지지 근거 |
| [28711447](https://pubmed.ncbi.nlm.nih.gov/28711447/) | 2017 | 서술적 고찰 | JACC. Heart Failure | 고혈압에서 심부전으로의 이행 과정 리뷰; 혈압 조절 약물(Chlorthalidone 포함)의 심장 보호 효과에 대한 배경 근거 제공 |

---

## 참고 분석: 악성 고혈압 관련 적응증 (Ranks 3–4)

악성 신혈관성 고혈압(Rank 3)과 악성 고혈압성 신장병(Rank 4)은 동일한 TxGNN 점수(99.89%)와 동일한 지식 그래프 노드를 공유하며, L4 근거로 "Research Question"에 해당합니다.

ALLHAT Phase 3 RCT는 일반 고혈압에서 chlorthalidone의 효능을 L1 수준으로 지지하나, 이 특수 아형에 대한 직접 연구는 없습니다. 두 가지 임상적 제약이 주요 고려 사항입니다:
- 악성 신혈관성 고혈압에서 일차 치료는 RAS 차단제(ACEI/ARB)이며, 이뇨제는 보조적 역할
- eGFR < 30 mL/min 시 티아지드 계열의 이뇨 효과가 현저히 감소하여 loop diuretics로의 전환이 권고됨

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold (Rank 1 — 원발성 유전성 녹내장 기준)**

**사유:**
원발성 유전성 녹내장에 대한 임상 근거가 전무하며, 유전적 구조 결함이 주요 병리인 해당 질환에 chlorthalidone의 이뇨 기전이 직접 작용할 약리적 근거가 부족합니다.

---

**10개 적응증 종합 권장 결정:**

| 결정 | 적응증 |
|------|--------|
| **Research Question** | 만성 폐성 심장병 (Rank 8, L3) — 현대적 표준치료 대비 보조 이뇨제로서의 역할 검토 가능 |
| **Research Question** | 악성 신혈관성 고혈압 (Rank 3, L4), 악성 고혈압성 신장병 (Rank 4, L4) — 특수 아형 연구 필요 |
| **Hold** | 나머지 7개 적응증 (근거 없음 또는 기전 연관성 부재) |

**진행하려면 필요한 것:**
- 한국 허가 및 안전성 정보 수집 (DG001 Blocking 갭 해소 — TFDA 仿單 PDF 파싱)
- DrugBank MOA 데이터 확보 (DG002 High 갭 해소)
- 만성 폐성 심장병에 대한 현대적 임상 문헌 추가 검색 (PMID 5597001은 1967년 연구로 현대적 재검토 필요)
- 만성 폐질환 동반 우심부전 가이드라인에서 티아지드 이뇨제의 현재 권고 위치 확인
- 한국 내 허가 신청 또는 출시 타당성 기초 조사
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

