---
layout: default
title: Polmacoxib
parent: 높은 근거 (L1-L2)
nav_order: 561
evidence_level: L1
indication_count: 10
---

# Polmacoxib
{: .fs-9 }

근거 수준: **L1** | 예측 적응증: **10** 건
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

# Polmacoxib: 골관절염(Osteoarthritis) 적응증 재평가

> **참고**: TxGNN 예측 1위인 "osteoarthritis susceptibility"(유전적 감수성 노드)는 실제 치료 가능한 질병 개체가 아니며, 근거 수준 L5·Hold로 평가되어 본 보고서에서는 임상적으로 유의미하고 근거가 실질적으로 뒷받침되는 **2순위 예측(osteoarthritis)** 을 중심으로 평가합니다.

## 한 문장 요약

Polmacoxib(CG100649)은 COX-2와 탄산탈수효소(CA-I/II)를 동시에 억제하는 신규 NSAID 계열 약물로, 문헌상 이미 골관절염 치료 목적으로 개발·연구되어 왔습니다.
TxGNN 모델은 **골관절염(Osteoarthritis)**에 대해 높은 예측 점수를 부여했으며, 이를 뒷받침하는 **완료된 Phase 3 RCT(362명)를 포함한 4건의 임상시험**과 **RCT 2건을 포함한 7편의 문헌**이 확인됩니다. 다만 현재 데이터셋 기준으로는 한국 내 허가 정보와 안전성(경고·금기) 정보가 확보되어 있지 않습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인되지 않음 (허가 정보 미확보; 문헌상 원래 골관절염 치료제로 개발·연구됨) |
| 예측 신규 적응증 | 골관절염 (Osteoarthritis) |
| TxGNN 예측 점수 | 99.999% |
| 근거 수준 | L1 |
| 한국 시판 현황 | 미상판매 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

DrugBank 기반의 상세 MOA 데이터는 현재 확보되어 있지 않습니다. 다만 확보된 문헌(PMID 34974943, 26095375 등)에 따르면, Polmacoxib은 **COX-2와 탄산탈수효소(CA-I/II)를 이중 억제**하는 신규 NSAID로, COX-2 억제를 통해 관절 염증과 통증을 직접 조절합니다. CA-II 억제는 기존 COX-2 선택적 억제제에서 문제가 되었던 심혈관 위험을 낮추기 위한 차별화 설계로 보고되어 있습니다.

이러한 기전은 골관절염의 핵심 병태생리(관절 내 프로스타글란딘 매개 염증·통증)와 직접적으로 연결되며, 실제로 여러 국가(한국, 인도 등)에서 진행된 임상시험에서 celecoxib 대비 비열등성 및 위약 대비 우월성이 반복적으로 확인되었습니다. 따라서 TxGNN의 예측은 이미 축적된 임상 근거와 기전적으로 일치합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01765296](https://clinicaltrials.gov/study/NCT01765296) | Phase 3 | 완료 | 362 | 고관절/슬관절 골관절염 환자 대상, Polmacoxib 2mg의 celecoxib 200mg 대비 비열등성 및 위약 대비 우월성을 WOMAC-Pain 지표로 입증 (6주 치료) |
| [NCT01341405](https://clinicaltrials.gov/study/NCT01341405) | Phase 2 | 완료 | 125 | 2용량 반복투여 2b상, celecoxib 대비 비열등성 확인 |
| [NCT00530452](https://clinicaltrials.gov/study/NCT00530452) | Phase 2 | 상태 불명 | 240 | 위약 대비 3가지 부하·유지 용량요법의 21일간 안전성·유효성 평가 (상태 불명으로 근거력 제한) |
| [NCT00780325](https://clinicaltrials.gov/study/NCT00780325) | Phase 1 | 중단 | 26 | 건강인 대상 COX-1/2, CA-I/II 억제 효과를 celecoxib·naproxen·acetazolamide와 비교한 PK 연구 (조기 종료, 안전성/약동학적 배경 자료로만 활용 가능) |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [29201297](https://pubmed.ncbi.nlm.nih.gov/29201297/) | 2017 | RCT | Clinics in Orthopedic Surgery | Polmacoxib 2mg의 위약 대비 우월성 및 celecoxib 200mg 대비 비열등성을 입증한 다기관 3상 RCT |
| [39545640](https://pubmed.ncbi.nlm.nih.gov/39545640/) | 2024 | RCT | Pain Management | 경증~중등도 특발성 고관절/슬관절 골관절염 환자에서 Polmacoxib 2mg vs celecoxib 200mg 비교, 유효성·안전성 유사 |
| [34974943](https://pubmed.ncbi.nlm.nih.gov/34974943/) | 2022 | 코호트(집단약동학) | Clinical Therapeutics | 건강인 및 골관절염 환자 대상 집단 PK/PD 분석, 한국에서 골관절염 치료제로 최근 승인됨을 명시 |
| [41257112](https://pubmed.ncbi.nlm.nih.gov/41257112/) | 2025 | 코호트(전향적) | Cureus | 인도 환자 대상 고관절/슬관절 골관절염에서 Polmacoxib 2mg의 유효성, 발현시간, 내약성 평가 |
| [41100334](https://pubmed.ncbi.nlm.nih.gov/41100334/) | 2025 | Review | JAPI | 골관절염 및 급성 통증 상태에서 Polmacoxib의 안전성·유효성 종합 검토 |
| [38765421](https://pubmed.ncbi.nlm.nih.gov/38765421/) | 2024 | Review | Cureus | 골관절염 치료제로서 Polmacoxib(신규 NSAID)의 특성 개관 |
| [26095375](https://pubmed.ncbi.nlm.nih.gov/26095375/) | 2015 | Review(분자모델링) | Protein and Peptide Letters | COX-2/CA-II 이중억제 기전을 밀도범함수이론(DFT)으로 분석, 한국 MFDS 승인 배경 설명 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
완료된 Phase 3 RCT(NCT01765296, 362명)를 포함해 celecoxib 대비 비열등성·위약 대비 우월성을 반복적으로 입증한 RCT 및 코호트 연구가 다수 확보되어 있어(근거 수준 L1) 골관절염 적응증에 대한 임상적 근거는 충분합니다. 다만 한국 시장 허가 현황(현재 데이터상 미상판매·0건)과 안전성(경고·금기·DDI) 정보가 확보되지 않아 안전성 초기평가(S1) 단계를 완료할 수 없는 상태입니다.

**진행하려면 필요한 것:**
- TFDA/MFDS 공식 허가사항(경고·금기·DDI) 확보 — 현재 Blocking 데이터 갭
- DrugBank 등을 통한 공식 MOA 데이터 확인 — 현재 High 우선순위 데이터 갭
- 한국 내 실제 허가·시판 현황 재확인 (문헌상 한국 승인 언급과 현재 등록 데이터 간 불일치 해소 필요)
- rank 8 "arthropathy", rank 10 "ankylosing spondylitis" 등 관련 적응증에 대한 독립적 임상 근거 확보 여부 추적
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

