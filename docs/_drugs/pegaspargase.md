---
layout: default
title: Pegaspargase
parent: 모델 예측만 (L5)
nav_order: 581
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Pegaspargase: 예측 신규 적응증 전구 림프모구성 림프종/백혈병 (precursor lymphoblastic lymphoma/leukemia) (근거 수준 L5). 기존 적응증: 허가 적응증 본문이 링크 형태로만 제공되어 구체적 문구를 확인할 수 없음 (허가사항 PDF 참조)"
monitor_inn: "PEGASPARGASE"
predicted_indications: ["chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation", "pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma", "follicular lymphoma", "methylcobalamin deficiency type cblE", "lymphoid neoplasm", "Hodgkins lymphoma", "blast phase chronic myelogenous leukemia, BCR-ABL1 positive"]
---

# Pegaspargase
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

## Pegaspargase: 급성 림프모구성 백혈병에서 전구 림프모구성 림프종/백혈병으로
{: .text-alpha }

## 한 문장 요약

Pegaspargase는 PEG화된 L-아스파라지나제로, 한국에서 허가를 받아 시판 중인 항종양 효소제입니다.
TxGNN 모델은 **전구 림프모구성 림프종/백혈병(precursor lymphoblastic lymphoma/leukemia)**에 효과가 있을 수 있다고 예측하며, 현재 **35건의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다. 다만 이 적응증은 기존 사용 범위와 거의 겹쳐 있어 엄밀한 의미의 새로운 재창출이라기보다 기존 용도의 확인에 가깝습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 링크 형태로만 제공되어 구체적 문구를 확인할 수 없음 (허가사항 PDF 참조) |
| 예측 신규 적응증 | 전구 림프모구성 림프종/백혈병 (precursor lymphoblastic lymphoma/leukemia) |
| TxGNN 예측 점수 | 99.96% |
| 근거 수준 | L1 (완료된 Phase 3 임상시험 다수: NCT00967057, NCT00103285 등) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 DrugBank 항목에 없습니다. 다만 본 보고서를 위해 정리된 데이터에 따르면, Pegaspargase는 순환 아스파라긴을 고갈시키는 PEG화 L-아스파라지나제입니다. 림프모구는 아스파라긴 합성효소 발현이 낮아 세포외 아스파라긴에 의존하므로, 아스파라긴이 고갈되면 단백질 합성이 억제되고 세포사멸이 유도됩니다.

이 기전은 급성 림프모구성 백혈병(ALL)과 림프모구성 림프종 치료의 핵심입니다. 따라서 전구 림프모구성 림프종/백혈병은 기존 허가 범위 안이거나 매우 가까운 적응증으로 보이며, 가장 중요한 과제는 허가 문구와의 일치 여부 확인과 독성 관리입니다.

## 임상시험 근거

관련성이 높은 시험 위주로 정리했습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00967057](https://clinicaltrials.gov/study/NCT00967057) | Phase 3 | 완료 | 470 | 재발/불응성 ALL 복합 화학요법 (아스파라지나제 계열 포함, 개별 기여도는 분리되지 않음) |
| [NCT00103285](https://clinicaltrials.gov/study/NCT00103285) | Phase 3 | 완료 | 5377 | 표준위험 B-전구 ALL에서 복합 화학요법 비교 (pegaspargase가 표준 구성요소) |
| [NCT02003222](https://clinicaltrials.gov/study/NCT02003222) | Phase 3 | 활성, 모집 종료 | 488 | 신규 진단 B-ALL에서 blinatumomab 추가 평가 (pegaspargase 포함 기본 요법) |
| [NCT00905034](https://clinicaltrials.gov/study/NCT00905034) | Phase 2 | 완료 | 37 | 구제 ALL에서 메토트렉세이트·빈크리스틴·PEG-아스파라지나제·덱사메타손(MOAD) |
| [NCT00890656](https://clinicaltrials.gov/study/NCT00890656) | Phase 2 | 완료 | 90 | ALL 구제요법으로서 augmented hyper-CVAD |
| [NCT05602194](https://clinicaltrials.gov/study/NCT05602194) | Phase 3 | 활성, 모집 종료 | 440 | 아스파라지나제 관련 간독성 예방을 위한 levocarnitine (안전 사용 관련) |
| [NCT01403415](https://clinicaltrials.gov/study/NCT01403415) | Phase 1 | 완료 | 13 | 재발 ALL/비호지킨 림프종에서 temsirolimus + 재유도요법 |
| [NCT06554626](https://clinicaltrials.gov/study/NCT06554626) | Phase 2 | 모집 중 | 20 | blinatumomab·venetoclax·inotuzumab 요법 (화학요법 절감 설계, 간접 관련) |
| [NCT02419469](https://clinicaltrials.gov/study/NCT02419469) | Phase 2 | 조기 종료 | 1 | augmented BFM + ofatumumab (1명 등록, 정보 가치 낮음) |
| [NCT01483690](https://clinicaltrials.gov/study/NCT01483690) | Phase 1/2 | 조기 종료 | 23 | 재발 ALL에서 decitabine·vorinostat + 화학요법 |

대부분은 pegaspargase가 포함된 복합 요법 시험이어서 pegaspargase 단독 효과를 분리해 보기는 어렵습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [35271306](https://pubmed.ncbi.nlm.nih.gov/35271306/) | 2022 | RCT | J Clin Oncol | 신규 진단 T-ALL/림프종에서 bortezomib를 평가한 COG AALL1231 Phase 3 |
| [32813610](https://pubmed.ncbi.nlm.nih.gov/32813610/) | 2020 | RCT | J Clin Oncol | 신규 진단 T-ALL에서 nelarabine을 평가한 COG AALL0434 |
| [27114587](https://pubmed.ncbi.nlm.nih.gov/27114587/) | 2016 | RCT | J Clin Oncol | 고위험 B-ALL에서 덱사메타손과 고용량 메토트렉세이트가 결과 개선 (AALL0232) |
| [37276451](https://pubmed.ncbi.nlm.nih.gov/37276451/) | 2023 | 코호트 | Blood Adv | 성인 ALL에서 pegaspargase를 더한 위험도 기반 프로그램 (GIMEMA LAL1913) |
| [31030380](https://pubmed.ncbi.nlm.nih.gov/31030380/) | 2019 | Review | Drugs | ALL에서 pegaspargase에 대한 종합 리뷰 |
| [40109190](https://pubmed.ncbi.nlm.nih.gov/40109190/) | 2025 | Review | Haematologica | 성인 ALL에서 아스파라지나제 관련 이상반응의 인지·예방·관리 전문가 합의 |
| [40858769](https://pubmed.ncbi.nlm.nih.gov/40858769/) | 2025 | 코호트 | Ann Hematol | 55세 이상 ALL 환자에서 pegaspargase 투여 및 내약성 |
| [30917738](https://pubmed.ncbi.nlm.nih.gov/30917738/) | 2020 | Review | J Oncol Pharm Pract | PEG화 아스파라지나제의 용량, 모니터링, 관리 기관 지침 |
| [27643446](https://pubmed.ncbi.nlm.nih.gov/27643446/) | 2017 | Review | Leuk Lymphoma | pegaspargase 정맥 vs 근육 주사 시 과민반응 비교 |
| [9161659](https://pubmed.ncbi.nlm.nih.gov/9161659/) | 1997 | Review | Ann Pharmacother | pegaspargase의 약리, 임상 활성, 이상반응 개관 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202101033 | 온카스파동결건조주사(페그아스파르가제) | 동결건조 주사제 (용해 후 투명한 무색 용액) | 허가사항 PDF 참조 (본문 텍스트 미확인) |

제조사는 한국세르비에(주)입니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 항종양 효소제 (아스파라긴 고갈 기전). 전통적 DNA 손상형 세포독성 약물과는 구분됨 |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 문헌상 과민반응, 췌장염, 혈전증, 간독성, 고중성지방혈증, 고혈당 모니터링 권고. 아스파라지나제 활성 모니터링 병행 |
| 취급 방호 | 허가사항 및 기관의 항암제 취급 규정을 따르세요 |

## 안전성 고려사항

- **주요 경고 (문헌 기반)**: 과민반응, 췌장염, 혈전증, 간독성, 고중성지방혈증이 보고되었습니다. 성인과 고령, 비만 환자에서 독성 위험이 커질 수 있어 용량 상한(capping)과 연령별 용량 조절이 논의되고 있습니다.
- **약물 상호작용**: 상호작용 100건이 확인되었으며, 표시된 항목은 모두 중등도(Moderate)입니다. 주요 예로 hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide 등 코르티코스테로이드, metformin·acarbose·alogliptin·canagliflozin·dapagliflozin 등 혈당강하제, acetylsalicylic acid, doxycycline·tetracycline·clarithromycin, bupropion이 있습니다. 혈당 변동이 알려진 약물이므로 혈당강하제와의 병용에는 특히 주의가 필요합니다.

허가사항상 경고·금기 정보는 이번 데이터에서 확인되지 않았으므로 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
ALL과 림프모구성 림프종에서 pegaspargase 포함 요법을 뒷받침하는 완료된 대규모 Phase 3 시험이 다수 있어 근거 수준은 L1입니다. 다만 이 적응증은 사실상 기존 허가 범위에 해당하여 신규 재창출이라기보다 기존 사용의 확인이며, 독성 관리가 필수입니다.

**진행하려면 필요한 것:**
- 한국 허가사항 PDF에서 허가 적응증과 경고·금기 확인 (현재 본문이 확인되지 않아 안전성 심사의 차단 요소)
- DrugBank 기반 상세 작용 기전 데이터 보충
- 과민반응, 췌장염, 혈전증, 간독성, 고중성지방혈증, 고혈당에 대한 모니터링 계획과 아스파라지나제 활성 측정, 연령별 용량 조절 지침

**참고: 다른 예측 적응증**
- 만성 림프구성 백혈병 계열, 여포성 림프종, methylcobalamin 결핍(cblE)은 TxGNN 점수만 높고 임상시험과 문헌이 없어 **Hold**입니다. cblE는 기전적 연관성이 없어 지식 그래프의 인공적 결과일 가능성이 큽니다.
- 호지킨 림프종과 CML 림프모구 위기는 연결된 시험이 ALL 시험이어서 직접 근거가 없으며 **연구 질문** 수준입니다. 호지킨 림프종 쪽 문헌은 실제로는 NK/T세포 림프종에서 pegaspargase 병용 요법의 활성을 다룹니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

