---
layout: default
title: Mercaptopurine
parent: 僅模型預測 (L5)
nav_order: 468
evidence_level: L5
indication_count: 10
---

# Mercaptopurine
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

# Mercaptopurine: 급성 림프모구성 백혈병에서 급성 림프모구성 백혈병(기존 표준치료 역할)으로

## 한 문장 요약

Mercaptopurine(6-MP)은 퓨린 유사체 계열 세포독성 항대사물로, 국제적으로 급성 림프모구성 백혈병(ALL) 유지요법의 핵심 약물로 이미 널리 사용되고 있습니다. TxGNN 모델은 이 약물이 **급성 림프모구성 백혈병(Acute Lymphoblastic Leukemia)**에 효과가 있을 것으로 예측했으며, 현재 **50건의 임상시험**과 **20편의 문헌**이 이를 뒷받침합니다. 다만 이는 완전히 새로운 적응증이 아니라 이미 확립된 표준치료 역할이라는 점에 유의해야 합니다 — 데이터 상 `original_indications`가 비어 있는 것은 자료 수집상의 결함(Data Gap)으로 판단됩니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 자료 없음(한국 허가 정보 없음) — 단, 국제적으로 급성 림프모구성 백혈병 유지요법에 기허가된 약물 |
| 예측 신규 적응증 | 급성 림프모구성 백혈병 (Acute Lymphoblastic Leukemia) |
| TxGNN 예측 점수 | 99.94% |
| 근거 수준 | L1 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails (단, 아래 "결론 및 다음 단계" 참조) |

## 이 예측이 타당한 이유는?

6-Mercaptopurine은 thiopurine 계열 퓨린 유사체로, 체내에서 HGPRT(hypoxanthine-guanine phosphoribosyltransferase)에 의해 활성형 6-thioguanine nucleotide(6-TGN)로 전환됩니다. 이 대사물은 DNA/RNA에 삽입되고 de novo 퓨린 합성을 억제하여, 빠르게 분열하는 림프모구의 증식을 차단합니다. 이 기전은 ALL 관해 후 유지요법의 핵심 축으로 수십 년간 임상에서 검증되어 왔습니다.

**중요 caveat**: 이번 예측은 엄밀한 의미의 "약물 재창출(신규 적응증 발굴)"이 아닙니다. Mercaptopurine은 이미 국제적으로 ALL 치료의 표준 약제이며, TxGNN이 예측한 적응증은 이 약물의 기존 역할과 사실상 동일합니다. Evidence Pack의 `original_indications` 필드가 비어 있는 것은 데이터 수집 단계의 공백으로 추정되며, 진정한 신규성 평가를 위해서는 별도 확인이 필요합니다.

MOA 관련 상세 DrugBank 데이터(DG002, High severity)는 현재 확보되지 않았으나, 위 기전은 evidence pack 내 문헌·시험 근거로 충분히 뒷받침됩니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01190930](https://clinicaltrials.gov/study/NCT01190930) | Phase 3 | 진행 중(모집 종료) | 9,350 | COG 대규모 표준위험군 B-ALL 시험, 6-MP가 유지요법의 핵심 약물 중 하나 |
| [NCT01117441](https://clinicaltrials.gov/study/NCT01117441) | Phase 3 | 완료 | 6,136 | 소아·청소년 ALL 대상 국제 공동 병용화학요법 프로토콜 비교 |
| [NCT02883049](https://clinicaltrials.gov/study/NCT02883049) | Phase 3 | 진행 중(모집 종료) | 5,949 | 신규 진단 고위험 B-ALL 대상 dasatinib 병용 화학요법 평가 |
| [NCT00613457](https://clinicaltrials.gov/study/NCT00613457) | Phase 3 | 완료 | 2,039 | AIEOP LLA 2000, 소아 ALL 진단·치료 다기관 연구 |
| [NCT00002514](https://clinicaltrials.gov/study/NCT00002514) | Phase 3 | 완료 | 1,929 | 1차 관해 ALL에서 조혈모세포이식 vs 강화 화학요법 비교 |
| [NCT00819351](https://clinicaltrials.gov/study/NCT00819351) | Phase 3 | 완료 | 650 | NOPHO 프로토콜, PEG-asparaginase 투여 간격 비교(6-MP 병용 유지요법) |
| [NCT00549848](https://clinicaltrials.gov/study/NCT00549848) | Phase 3 | 완료 | 600 | Total Therapy XVI, PEG-asparaginase 고용량 vs 표준용량 비교 |
| [NCT02042690](https://clinicaltrials.gov/study/NCT02042690) | Phase 3 | 완료 | 131 | 표준위험 성인 ALL에서 반일치 이식 vs 화학요법(6-MP 포함) 비교 |
| [NCT00526305](https://clinicaltrials.gov/study/NCT00526305) | Phase 4 | 완료 | 100 | LAL-Ph-2000, Ph+ ALL 표준치료 프로토콜(유지단계 6-MP 포함) |
| [NCT00526175](https://clinicaltrials.gov/study/NCT00526175) | Phase 4 | 완료 | 150 | LAL-BR/2001, 저위험군 ALL 공고요법 프로토콜 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [35157496](https://pubmed.ncbi.nlm.nih.gov/35157496/) | 2022 | RCT | J Clin Oncol | SWOG 1318, 고령 Ph- B-ALL에서 blinatumomab 유도 후 POMP(6-MP 포함) 유지요법 |
| [10653870](https://pubmed.ncbi.nlm.nih.gov/10653870/) | 2000 | Cohort | J Clin Oncol | Hyper-CVAD 강화 화학요법의 성인 ALL 효능·독성 평가 |
| [38230823](https://pubmed.ncbi.nlm.nih.gov/38230823/) | 2024 | Cohort/PGx | JNCI | TPMT·NUDT15 병용 변이가 소아 ALL의 6-MP 독성에 미치는 부가효과 |
| [31283407](https://pubmed.ncbi.nlm.nih.gov/31283407/) | 2019 | Cohort | J Clin Oncol | Interfant-06 국제 Phase 3 연구, 영아 ALL 치료 결과 |
| [38936894](https://pubmed.ncbi.nlm.nih.gov/38936894/) | 2024 | Cohort/PGx | In Vivo | 인도네시아 소아 ALL에서 NUDT15 다형성과 6-MP 혈액독성 연관성 |
| [37550838](https://pubmed.ncbi.nlm.nih.gov/37550838/) | 2023 | Cohort | Clin Pharmacol Ther | AIEOP-BFM ALL 2009 프로토콜에서 6-MP 대사물이 치료 결과에 미치는 영향 |
| [35501736](https://pubmed.ncbi.nlm.nih.gov/35501736/) | 2022 | 연구 프로토콜 | BMC Cancer | TEAM 연구, 6-MP/MTX 기반 유지요법에 저용량 6-thioguanine 추가 평가 |
| [33750748](https://pubmed.ncbi.nlm.nih.gov/33750748/) | 2021 | Cohort | J Pediatr Hematol Oncol | Allopurinol 병용이 소아·청년 ALL 환자의 6-MP 이상반응 예방에 미치는 효과 |
| [29352703](https://pubmed.ncbi.nlm.nih.gov/29352703/) | 2018 | Phase 2 단일군 시험 | Lancet Oncol | 고령 Ph- ALL에서 inotuzumab ozogamicin 병용 저강도 화학요법 |
| [9286287](https://pubmed.ncbi.nlm.nih.gov/9286287/) | 1997 | Review | Pediatr Clin North Am | 급성 림프모구성 백혈병 총론 및 치료 전략 리뷰 |

## 한국 시판 정보

현재 한국에 등재된 허가 정보가 없습니다 (미출시 의약품).

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (Thiopurine/퓨린 항대사물 계열) |
| 골수억제 위험 | 고위험 — TPMT/NUDT15 유전자 다형성에 따라 심각한 혈액독성(백혈구감소증 등) 발생률이 크게 달라짐(문헌 근거: PMID 38230823, 38936894 등 다수 PGx 연구) |
| 구토 유발성 등급 | 저~중등도 |
| 모니터링 항목 | CBC(분류 포함), 간기능(LFT), TPMT/NUDT15 유전형 검사(가능 시), 신기능 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails (단, 조건부)**

**사유:**
- Evidence Pack 내 근거 수준(L1, 대규모 완료 Phase 3 시험 다수)만 보면 "진행"을 지지하지만, 예측된 적응증(ALL)은 Mercaptopurine의 **이미 확립된 기존 표준치료 역할**이며 신규 재창출 후보로 보기 어렵습니다. `original_indications`가 비어 있는 것은 자료 수집 공백(Data Gap)으로 판단되므로, 이 후보를 "신규 적응증 발굴"로 보고하는 것은 오해의 소지가 있습니다.
- 참고로 동일 Evidence Pack 내 rank 10 (소세포폐암, L3, 1985년 Phase 2 시험 + 2023년 기전 연구)이 오히려 더 진정성 있는 재창출 후보로 보이나, 근거가 오래되고 임상시험 수가 0건(현재 등록된 시험 없음)이라 초기 연구 단계입니다.

**진행하려면 필요한 것:**
- TFDA/MFDS 등 규제기관 허가사항의 경고·금기 정보 확보 (DG001, Blocking)
- DrugBank API를 통한 상세 MOA 및 독성 데이터 확보 (DG002, High)
- `original_indications` 데이터 공백 원인 확인 및 보정 — 이 약물이 실제로 "신규" 예측인지, 기존 적응증 중복 등재인지 재검증
- 소세포폐암(rank 10) 등 진정한 신규 후보에 대한 별도 심층 평가 착수 고려
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

