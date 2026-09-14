---
layout: default
title: Theophylline
parent: 僅模型預測 (L5)
nav_order: 673
evidence_level: L5
indication_count: 7
---

# Theophylline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Theophylline: 호흡기 질환(기관지확장제)에서 혈전성 질환(Thrombotic Disease)으로

## 한 문장 요약

Theophylline은 잔틴계 기관지확장제로 전통적으로 천식·COPD 등 호흡기 질환에 사용되어 온 약물입니다. TxGNN 모델은 이번 candidate에서 **혈전성 질환(Thrombotic Disease)**을 1순위로 예측(99.62%)했지만, 관련 임상시험은 전무하고 인용된 문헌 19편 중 대부분이 항혈전 기전과 무관한 것으로 분석되어 **위양성 가능성이 높은 예측**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 구조화된 데이터 없음 (Data Gap — 일반적으로 기관지천식·COPD 치료제로 알려짐) |
| 예측 신규 적응증 | 혈전성 질환 (Thrombotic Disease) |
| TxGNN 예측 점수 | 99.62% (rank 7046) |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미상시 (未上市) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 없습니다(Data Gap — DG002). Theophylline의 기존 적응증 정보 역시 구조화된 데이터로 제공되지 않았습니다(Data Gap).

Evidence Pack에 포함된 자체 분석(repurposing_rationale)에 따르면, 이번 예측에는 **직접적인 기전적 연관 증거가 없습니다.** 인용된 19편의 문헌은 대부분 (1) 다른 항혈소판제(ticlopidine)의 약동학 연구, (2) 혈소판 활성 바이오마커 측정 방법론 연구, (3) theophylline 검출용 바이오센서 개발 연구 등으로, theophylline의 실제 항혈전 임상 효과와는 관련이 없습니다. 즉 KG 모델의 그래프 구조상 유사성에 의한 **위양성(false positive) 가능성이 높은 케이스**로 평가됩니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Review (무관 약물) | Clinical Pharmacokinetics | Ticlopidine의 약동학 리뷰 — theophylline과 무관 |
| [21719422](https://pubmed.ncbi.nlm.nih.gov/21719422/) | 2011 | 관찰 연구 | Rheumatology | Behçet's disease 환자의 혈소판·호중구 활성화 — theophylline 미언급 |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Crit Rev Biochem | Prostaglandin/혈소판/죽상경화증 일반 기전 리뷰 |
| [32824700](https://pubmed.ncbi.nlm.nih.gov/32824700/) | 2020 | 방법론 연구 | Cells | 혈액 microRNA 시그니처 정량 방법론 — theophylline 미관련 |
| [15475744](https://pubmed.ncbi.nlm.nih.gov/15475744/) | 2004 | 관찰 연구 | Inflammatory Bowel Diseases | IBD 환자의 혈소판-백혈구 응집체 형성 |
| [25856065](https://pubmed.ncbi.nlm.nih.gov/25856065/) | 2015 | 방법론 연구 | Platelets | sCLEC-2 바이오마커 측정법 개발 |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | 방법론 연구 | Br J Haematol | 혈소판 인자4(PF4) 방사면역측정 — theophylline은 채혈시 항응고 보조제로만 언급 |
| [197665](https://pubmed.ncbi.nlm.nih.gov/197665/) | 1977 | Review | Stroke | 뇌졸중 관련 뇌부종 리뷰 — theophylline 미관련 |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | 분석화학 (바이오센서) | Analytica Chimica Acta | Theophylline 검출용 금나노입자 전기화학 센서 개발 — 치료 효과와 무관 |
| [29956444](https://pubmed.ncbi.nlm.nih.gov/29956444/) | 2018 | 기초 연구 | J Thromb Haemost | Weibel-Palade body 분비과립 방출 조절 기전 연구 |

> 위 10편 모두 theophylline의 항혈전 임상 효과를 직접 지지하지 않습니다.

## 한국 시판 정보

Theophylline은 현재 한국(등록 기준) 미상시 상태이며, 허가 정보가 존재하지 않습니다.

## 안전성 고려사항

TFDA 허가사항 데이터(Data Gap — DG001, Blocking)가 확보되지 않아 안전성 초기 평가(S1)를 진행할 수 없습니다. 주요 경고, 금기, 약물 상호작용 정보 모두 미제공 상태입니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 점수는 높지만 임상시험 근거가 전무하고, 인용 문헌 대부분이 항혈전 기전과 무관해 위양성 가능성이 높습니다. 또한 국내 미상시 약물로 허가사항·안전성 데이터가 없어 안전성 초기평가(S1)조차 진입할 수 없는 상태입니다.

**진행하려면 필요한 것:**
- TFDA(또는 MFDS) 허가사항 확보 (경고/금기) — DG001 (Blocking)
- DrugBank 작용기전(MOA) 데이터 확보 — DG002 (High)
- 혈전성 질환에 대한 직접적 기전 연구(전임상) — 현재 근거는 방법론/무관 약물 연구뿐
- 국내 시판 여부 및 허가 경로 재검토

---

### 부록: 같은 Candidate 내 상대적으로 근거가 더 강한 예측

이 candidate에는 rank 1 외에도 theophylline 자체의 기관지평활근 이완 기전과 직접 연결되는 예측이 포함되어 있어 참고용으로 병기합니다.

| Rank | 적응증 | 근거 수준 | 권장 | 비고 |
|------|--------|----------|------|------|
| 4 | Tracheal disease | L3 | Research Question | 기도 평활근 이완 전임상 다수 + 견종 기관 허탈 후향적 연구 |
| 5 | Obstructive lung disease | pending (실질적으로 매우 풍부) | — | COPD/천식 Phase 2-4 RCT 다수(NCT02261727, NCT03984188 등) — theophylline의 **기존** 용도와 사실상 중복 가능성 있음, 원 적응증 데이터 확인 필요 |
| 6 | Pharyngitis | L4 | Hold | 간접적, macrolide 병용 문헌 위주 |

rank 5(obstructive lung disease)는 evidence가 가장 풍부하지만 original_indications 필드가 비어 있어 "신규 예측"인지 "기존 적응증 재확인"인지 구분이 안 됩니다. 원 적응증 데이터(Data Gap)를 먼저 보완하는 것이 candidate 전체의 재평가에 필요합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

