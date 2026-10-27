---
layout: default
title: Lenalidomide
parent: 모델 예측만 (L5)
nav_order: 466
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Lenalidomide: 예측 신규 적응증 골수성 백혈병 (myeloid leukemia) (근거 수준 L5). 기존 적응증: 허가 적응증 본문은 이번 데이터에 포함되지 않았습니다 (허가증 링크만 확인됨)"
monitor_inn: "LENALIDOMIDE"
predicted_indications: ["myeloid leukemia", "refractory cytopenia of childhood", "aregenerative anemia", "severe congenital hypochromic anemia with ringed sideroblasts", "partial deletion of the long arm of chromosome 5"]
---

# Lenalidomide
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **6** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 약사 평가 보고서

</div>

## Lenalidomide: 다발골수종·골수이형성증후군에서 골수성 백혈병으로
{: .text-alpha }

## 한 문장 요약

Lenalidomide는 한국에서 12건의 허가증으로 시판 중인 면역조절 항종양제입니다. TxGNN 모델은 **골수성 백혈병(myeloid leukemia)**에 효과가 있을 수 있다고 예측하며, 현재 **40여 건의 임상시험**과 **18편의 문헌**이 이 방향과 관련되어 있습니다. 다만 대부분 소규모 단일군 또는 병용요법 연구로, 확증적 근거는 아직 부족합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문은 이번 데이터에 포함되지 않았습니다 (허가증 링크만 확인됨) |
| 예측 신규 적응증 | 골수성 백혈병 (myeloid leukemia) |
| TxGNN 예측 점수 | 99.49% |
| 근거 수준 | L2 (완료된 Phase 2 시험이 있으나 대부분 소규모·단일군이며, 무작위 Phase 2/3 확증 근거는 없음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 12건 |
| 권장 결정 | Proceed with Guardrails (연구 질문 단계) |

## 이 예측이 타당한 이유는?

DrugBank 기반의 상세 작용 기전 데이터는 이번 데이터에 포함되어 있지 않습니다. 다만 알려진 기전 분석에 따르면 Lenalidomide는 cereblon(CRBN)에 결합하여 CRL4-CRBN E3 ligase가 IKZF1/IKZF3를 분해하도록 유도하며, del(5q) 세포에서는 CK1α도 분해합니다. 또한 T세포·NK세포를 활성화하는 면역조절 작용과 항증식 작용을 보입니다.

이러한 기전은 골수이형성증후군(MDS)과 급성골수성백혈병(AML)에서도 적용될 수 있으며, 특히 del(5q) 질환에서는 CK1α 반수체 부족으로 감수성이 높습니다. 2025년 연구(PMID 39881283)에서는 CRBN 안정화가 AML 세포의 Lenalidomide 감수성을 높인다고 보고했습니다.

주의할 점은 근거가 된 시험들이 AML, 고위험 MDS, 이식 후 유지요법 등으로 이질적이어서, 단일 골수성 백혈병 질환에 특이적인 신호는 아니라는 것입니다.

## 임상시험 근거

관련성 평가가 높은 순서로 대표 시험 10건을 제시합니다. 이 외에도 AML·MDS 대상 시험이 다수 등록되어 있습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02126553](https://clinicaltrials.gov/study/NCT02126553) | Phase 2 | 완료 | 29 | 관해 상태의 고위험 AML에서 Lenalidomide 유지요법 (단일군, 소규모) |
| [NCT00360672](https://clinicaltrials.gov/study/NCT00360672) | Phase 2 | 완료 | 27 | 5번 염색체 이상이 있는 재발/불응성 AML 또는 고위험 MDS에서 단독요법 |
| [NCT00352001](https://clinicaltrials.gov/study/NCT00352001) | Phase 1/2 | 완료 | 37 | 진행성 MDS에서 Lenalidomide + Azacitidine (병용으로 단독 효과 구분 어려움) |
| [NCT00831766](https://clinicaltrials.gov/study/NCT00831766) | Phase 1/2 | 완료 | 51 | Idarubicin + Cytarabine 후 Lenalidomide, 미치료 AML/MDS |
| [NCT01681537](https://clinicaltrials.gov/study/NCT01681537) | Phase 1 | 완료 | 36 | AML 재유도요법에서 MEC 화학요법과 병용 (용량 탐색·안전성) |
| [NCT01578954](https://clinicaltrials.gov/study/NCT01578954) | Phase 1 | 완료 | 20 | 60세 이상 AML에서 재유도/공고 및 유지요법 용량 탐색 |
| [NCT01254578](https://clinicaltrials.gov/study/NCT01254578) | Phase 1 | 완료 | 17 | 동종 조혈모세포이식 후 고위험 혈액암 유지요법 (GVHD 안전성 고려) |
| [NCT01358734](https://clinicaltrials.gov/study/NCT01358734) | Phase 2 | 완료 | 88 | 고령 신규 AML에서 Lenalidomide, Azacitidine 순차요법, Azacitidine 단독 비교 (무작위) |
| [NCT01301820](https://clinicaltrials.gov/study/NCT01301820) | Phase 2 | 완료 | 120 | 고령 AML 관해 후 Lenalidomide와 Azacitidine 교대 유지요법 |
| [NCT04490707](https://clinicaltrials.gov/study/NCT04490707) | Phase 3 | 불명 | 60 | 고령·부적합 AML에서 MRD 기반 Azacitidine + Lenalidomide 유지요법 |

## 문헌 근거

AML 및 MDS와 직접 관련된 문헌을 중심으로 선별했습니다. 이번 데이터에는 무작위 대조시험(RCT)이 포함되어 있지 않으며, 대부분 리뷰입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [32899586](https://pubmed.ncbi.nlm.nih.gov/32899586/) | 2020 | Review | Cancers | AML 치료에서 면역조절제(IMiD)의 역할 고찰 |
| [23316859](https://pubmed.ncbi.nlm.nih.gov/23316859/) | 2013 | Review | Expert Opin Investig Drugs | Lenalidomide를 AML의 새로운 치료제로 검토. del(5q) MDS 승인 및 고위험 MDS/AML 시험 정리 |
| [39881283](https://pubmed.ncbi.nlm.nih.gov/39881283/) | 2025 | 기초 연구 | Cell Mol Biol Lett | KDM5C가 CRBN을 안정화하여 AML 세포의 Lenalidomide 감수성을 높임 |
| [37288607](https://pubmed.ncbi.nlm.nih.gov/37288607/) | 2023 | Review | Am J Hematol | MDS의 진단, 위험도 분류, 치료 최신 정보 |
| [42400116](https://pubmed.ncbi.nlm.nih.gov/42400116/) | 2026 | Review | Am J Hematol | MDS 2026년 업데이트 |
| [37874917](https://pubmed.ncbi.nlm.nih.gov/37874917/) | 2023 | Review | Blood | MDS의 임상 의사결정과 치료 |
| [41348013](https://pubmed.ncbi.nlm.nih.gov/41348013/) | 2025 | Review | Hematology ASH Educ Program | 저/중간위험 MDS 치료 최신 동향 |
| [29795386](https://pubmed.ncbi.nlm.nih.gov/29795386/) | 2018 | Review | Blood Cancer J | MDS 치료 알고리즘 |
| [24656536](https://pubmed.ncbi.nlm.nih.gov/24656536/) | 2014 | Review | Lancet | MDS의 병태생리와 치료 개관 |
| [17488990](https://pubmed.ncbi.nlm.nih.gov/17488990/) | 2007 | 리뷰성 문헌 | J Clin Oncol | 고령 AML/MDS 환자의 치료 접근 |

## 한국 시판 정보

허가 적응증 본문은 이번 데이터에 포함되지 않았고 허가증 문서 링크만 제공되었습니다. 아래는 주요 허가 5건입니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201706896 | 레날도캡슐20mg (수출용) | 경질 캡슐 | [허가증 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201706896/EE) |
| 201706898 | 레날도캡슐10mg | 경질 캡슐 | [허가증 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201706898/EE) |
| 201900220 | 레블리킨캡슐5밀리그램 | 경질 캡슐 | [허가증 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201900220/EE) |
| 201802378 | 레블리킨캡슐25밀리그램 | 경질 캡슐 | [허가증 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201802378/EE) |
| 201706895 | 레날도캡슐25mg | 경질 캡슐 | [허가증 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201706895/EE) |

제조사는 광동제약(레날도)과 보령(레블리킨)이며, 전체 12건이 모두 단일제로 유효합니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 면역조절제 (thalidomide 유도체, 기존 세포독성 약물과 구분) |
| 골수억제 위험 | 높음 (지식그래프상 혈소판감소증, 호중구감소증, 무과립구증과 연관) |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 혈구검사(CBC, 분류 포함), 신기능 (지식그래프상 신기능 장애 관련), 혈전 증상 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **금기 관련 질환 (지식그래프 기반, 허가 문서 아님)**: 혈소판감소증, 호중구감소증, 무과립구증, 폐색전증, 신기능 장애, 암, 배아종
- **약물 상호작용**: 총 100건이 조회되었습니다. 주요(Major) 등급으로 확인된 항목은 다음과 같습니다.
  - Rosuvastatin
  - Simvastatin
  - 중등도(Moderate): Eliglustat, Naltrexone

허가 문서상의 경고 및 금기는 이번 데이터에서 확인되지 않았으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
AML/MDS에서 Lenalidomide를 평가한 완료된 Phase 2 시험이 여러 건 있고 기전적 근거(CRBN, 특히 del(5q))도 타당합니다. 그러나 대부분 소규모 단일군이거나 병용요법이어서 단독 효과를 입증하지 못했으며, 골수억제 위험이 큽니다. 따라서 확증 근거 없이 적용하기보다 연구 질문 단계로 신중하게 진행해야 합니다.

**진행하려면 필요한 것:**
- 허가 적응증 본문과 경고·금기 등 허가사항 확인 (MFDS 허가증 문서 분석)
- DrugBank 기반의 상세 작용 기전 데이터 보완
- 대상 질환(AML, del(5q) 고위험 MDS 등)을 구체화한 무작위 대조 Phase 2/3 근거 확인
- 골수억제 및 혈전 위험을 고려한 모니터링 계획
- 허가된 용도와의 차이를 고려한 임신 예방 등 위험관리 계획 검토

### 참고: 기타 예측 적응증

| 순위 | 질환 | TxGNN 점수 | 근거 수준 | 권장 |
|------|------|-----------|----------|------|
| 2 | 분류불능 골수이형성증후군 | 99.43% | L3 | Research Question |
| 3 | 소아 불응성 혈구감소증 | 99.35% | L3 | Hold |
| 4 | 재생불량성 빈혈(aregenerative anemia) | 99.32% | L3 | Hold |
| 5 | 중증 선천성 저색소성 빈혈(고리철적모구 동반) | 99.28% | L5 | Hold |
| 6 | 5번 염색체 장완 부분 결실 | 99.27% | L5 | Research Question |

이 중 6위(5번 염색체 장완 부분 결실)는 del(5q) MDS의 승인 기전과 겹칠 가능성이 높아, 후속 정리 작업에서 기존 근거와의 연결을 확인할 필요가 있습니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

