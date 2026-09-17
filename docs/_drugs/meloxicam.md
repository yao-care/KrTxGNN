---
layout: default
title: Meloxicam
parent: 모델 예측만 (L5)
nav_order: 464
evidence_level: L5
indication_count: 10
---

# Meloxicam
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

# Meloxicam: NSAID 계열 소염진통제에서 소아 특발성 관절염(JIA)으로

## 한 문장 요약

Meloxicam(DB00814)은 COX-2 선택적 억제 기전을 가진 NSAID 계열 약물입니다. TxGNN이 제시한 10개 예측 적응증 중 순위 1~5, 9, 10위는 유전성 골격/구조 이상 질환으로, 근거 텍스트 자체가 "지식그래프 임베딩 유사도로 인한 假訊號(허위 신호)"라고 명시하고 있어 임상적 의미가 없습니다. 실질적으로 근거가 있는 후보는 **류마티스인자 양성 다관절형 소아 특발성 관절염(JIA)**으로, 문헌 1편(안전성 코호트 연구)이 이를 뒷받침하며 다국가에서 meloxicam 경구 현탁액이 이미 JIA에 승인된 전례가 있습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 자료 없음 (evidence pack에 original_indications 미기재, TFDA 허가 정보 0건) |
| 예측 신규 적응증 | 류마티스인자 양성 다관절형 소아 특발성 관절염 (Rheumatoid factor-positive polyarticular JIA) |
| TxGNN 예측 점수 | 99.44% (rank 9234 / 전체 후보 중) |
| 근거 수준 | L3 (관찰/코호트 안전성 연구) |
| 한국(대만) 시판 현황 | 미상市 (허가 0건) |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** (약물 수준 Blocking 데이터 갭으로 인해 S1 안전성 초기평가 진입 불가) |

---

## 이 예측이 타당한 이유는?

현재 `drug.original_moa` 필드는 [Data Gap]으로 상세 기전 데이터가 없습니다. 다만 evidence pack 내 개별 적응증 근거 텍스트에서 Meloxicam을 "COX-2 우선형 NSAID로, 프로스타글란딘 합성 억제를 통해 항염/진통 효과를 나타낸다"고 설명하고 있어, 이 정보를 근거로 판단합니다.

TxGNN이 제시한 상위 10개 예측 중 acromesomelic dysplasia, brachyolmia, myosclerosis, pseudoachondroplasia, WHIM syndrome, colobomatous microphthalmia-rhizomelic dysplasia syndrome은 모두 유전자 돌연변이에 의한 구조적/발달성 질환으로, 각 항목의 `repurposing_rationale`이 스스로 "NSAID 기전과 무관", "지식그래프 골격계 노드 근접으로 인한 假陽性"이라고 판정하고 있습니다. 이들은 임상적으로 채택할 수 없는 노이즈입니다.

반면 JIA(순위 8위)는 관절 염증이 핵심 병태생리이며, NSAID의 항염/진통 기전이 직접 적용됩니다. 근거 텍스트에도 "다국가에서 meloxicam 경구 현탁액이 JIA에 이미 승인되어 있다"고 명시되어 있어, 새로운 가설이라기보다는 기존 임상 실무를 확인하는 성격에 가깝습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다. (JIA 적응증에 대해 clinicaltrials.gov, ICTRP 조회 결과 모두 0건)

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [25057265](https://pubmed.ncbi.nlm.nih.gov/25057265/) | 2014 | Review/Cohort (안전성 등록 연구) | Pediatric Rheumatology Online Journal | JIA 환자에서 celecoxib 및 비선택적 NSAID(nsNSAID)를 실제 임상에서 장기 투여했을 때의 안전성 및 발달 데이터를 평가한 4상 등록 연구 |

---

## 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| — | — | — | — |

현재 등록된 허가증이 없으며(0건), 시판 현황은 "미상市"입니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

(key_warnings, contraindications, DDI 조회 결과 모두 데이터 없음 — DDI는 "not_found" 상태)

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 약물 수준 데이터 갭(DG001: TFDA 허가 경고/금기 정보 부재)이 **Blocking** 등급으로, S1 안전성 초기평가 자체에 진입할 수 없는 상태입니다.
- 개별 적응증 중 JIA는 L3 근거·S2 단계로 "Proceed with Guardrails" 수준이지만, 약물 전체 게이트가 Hold이므로 이 후보만 별도로 진행할 수 없습니다.
- TxGNN 상위 랭킹 후보 7건(순위 1~5, 9, 10)은 근거 부재 및 자체 rationale상 기전 무관으로 판단되어 후속 조사 대상에서 제외합니다.

**진행하려면 필요한 것:**
- TFDA(또는 해당 국가 규제기관) 공식 허가사항 PDF 확보 및 경고/금기 파싱 (DG001 해소)
- DrugBank API를 통한 공식 MOA 데이터 확보 (DG002 해소)
- JIA 적응증에 대한 추가 문헌/임상시험 검색 확대(비영어권 데이터베이스 포함)
- 순위 6~8위(spondyloarthropathy susceptibility, rheumatoid nodulosis, JIA) 후보에 대한 사람에 의한 기전 재검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

