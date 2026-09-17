---
layout: default
title: Pegaspargase
parent: 높은 근거 (L1-L2)
nav_order: 535
evidence_level: L1
indication_count: 10
---

# Pegaspargase
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

# Pegaspargase: 기존 적응증 자료 미확보에서 전구림프모구백혈병/림프종으로

## 한 문장 요약

Pegaspargase(DrugBank DB00059)는 현재 한국에 허가된 제품이 없어 국내 규제 자료상 기존 적응증 정보가 확보되지 않았습니다. TxGNN 모델은 **전구림프모구백혈병/림프종(Precursor Lymphoblastic Leukemia/Lymphoma)**에 매우 높은 점수(99.96%)로 효과가 있을 것으로 예측하며, 현재 **69건 이상의 임상시험**과 **20편의 문헌**이 이를 뒷받침합니다. 다만 이 예측은 실제로는 pegaspargase의 **이미 확립된 표준 적응증(ALL 치료)** 을 재확인한 결과로 판단되며, "신규 적응증"이라기보다 원 적응증 데이터 누락(Data Gap)에 따른 결과일 가능성이 높습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (한국 미시판으로 등록된 허가 적응증 자료 없음) |
| 예측 신규 적응증 | 전구림프모구백혈병/림프종 (Precursor Lymphoblastic Leukemia/Lymphoma) |
| TxGNN 예측 점수 | 99.96% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Pegaspargase의 상세한 작용기전(MOA) 데이터는 확보되지 않았으나, 근거 자료의 재창출 근거(rationale)에서 핵심 약리 기전이 확인됩니다: pegaspargase는 혈장 내 asparagine을 분해·고갈시키는 효소 제제입니다. 급성림프모구백혈병(ALL)의 B/T계열 림프모구는 asparagine synthetase 효소가 결핍되어 있어 스스로 asparagine을 합성하지 못하고, 외부에서 공급받는 asparagine에 전적으로 의존합니다. 따라서 혈장 asparagine이 고갈되면 백혈병 세포는 단백질 합성이 차단되어 사멸하는 반면, asparagine synthetase를 정상적으로 발현하는 정상 세포는 영향을 받지 않습니다.

**중요한 주의사항**: 이 기전은 신규 발견이 아니라 pegaspargase(Oncaspar®)가 이미 전 세계적으로 소아·성인 ALL 표준 다제병용 화학요법의 핵심 구성 성분으로 수십 년간 사용되어 온 **기존 확립 적응증**입니다. 근거 자료의 재창출 근거 항목에서도 "이는 pegaspargase 핵심 약리 기전이며 신규 적응증이 아니고, original_indications가 Data Gap으로 표기된 것은 자료 수집 누락 때문"이라고 명시하고 있습니다. 즉 이번 TxGNN 예측은 새로운 치료 가설이라기보다, 원 적응증 데이터베이스 구축 과정에서 누락된 정보를 지식그래프가 역으로 재확인해 준 사례로 해석하는 것이 타당합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01190930](https://clinicaltrials.gov/study/NCT01190930) | Phase 3 | 진행중(모집종료) | 9,350 | 신규진단 표준위험군 B-ALL/국소성 B-LLy 소아 환자 대상 위험도별 병용화학요법 비교, pegaspargase가 치료 골격 |
| [NCT01117441](https://clinicaltrials.gov/study/NCT01117441) | Phase 3 | 완료 | 6,136 | 소아·청소년 ALL 국제협력 치료 프로토콜, pegaspargase가 표준 구성요소로 포함된 다수 병용화학요법 비교 |
| [NCT03914625](https://clinicaltrials.gov/study/NCT03914625) | Phase 3 | 진행중(모집종료) | 6,720 | 신규진단 표준위험 B-ALL/B-LLy(다운증후군 포함)에서 blinatumomab + pegaspargase 포함 화학요법 병용 효과 평가 |
| [NCT03959085](https://clinicaltrials.gov/study/NCT03959085) | Phase 3 | 모집중 | 5,951 | 고위험 B-ALL 신규진단 환자에서 inotuzumab ozogamicin 추가 후 위험도맞춤 후속치료 전략 평가 |
| [NCT00671034](https://clinicaltrials.gov/study/NCT00671034) | Phase 3 | 완료 | 166 | 고위험 ALL에서 calaspargase pegol(SC-PEG) vs pegaspargase 직접 비교, 유효성·약동학 데이터 확보 |
| [NCT02716233](https://clinicaltrials.gov/study/NCT02716233) | Phase 3 | 진행중(모집종료) | 2,044 | 소아·청소년 ALL 프랑스 프로토콜, L-asparaginase(ASNase) 최적 사용법 연구 |
| [NCT00549848](https://clinicaltrials.gov/study/NCT00549848) | Phase 3 | 완료 | 600 | Total Therapy XVI 연구 - 고용량 vs 표준용량 PEG-asparaginase 효능·약동학·약력학 비교 |
| [NCT00819351](https://clinicaltrials.gov/study/NCT00819351) | Phase 3 | 완료 | 650 | NOPHO 프로토콜 - 간헐적 vs 지속적 PEG-asparaginase 투여 비교, asparagine 고갈 효과 평가 |
| [NCT02013167](https://clinicaltrials.gov/study/NCT02013167) | Phase 3 | 조기종료 | 405 | 재발/불응 B계열 성인 ALL에서 blinatumomab vs 표준화학요법 전체생존율 비교(TOWER 연구) |
| [NCT00187083](https://clinicaltrials.gov/study/NCT00187083) | Phase 3 | 완료 | 40 | 재발/불응 소아 ALL에서 native asparaginase vs PEG-asparaginase 유효성 직접 비교 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [34228505](https://pubmed.ncbi.nlm.nih.gov/34228505/) | 2021 | Cohort | J Clin Oncol | DFCI 11-001 연구: calaspargase pegol과 pegaspargase의 소아 ALL 치료 효능·독성 비교 |
| [37276451](https://pubmed.ncbi.nlm.nih.gov/37276451/) | 2023 | Cohort | Blood Advances | GIMEMA LAL1913 연구: 성인 ALL에서 pegaspargase 추가 위험도맞춤 치료 성적 |
| [40109190](https://pubmed.ncbi.nlm.nih.gov/40109190/) | 2025 | 전문가 합의(Consensus) | Haematologica | 성인 ALL 환자의 asparaginase/pegaspargase 관련 이상반응 인지·예방·관리 전문가 패널 합의 |
| [31030380](https://pubmed.ncbi.nlm.nih.gov/31030380/) | 2019 | Review | Drugs | Pegaspargase(Oncaspar®)의 ALL 치료 전반에 대한 종합 리뷰 |
| [17696798](https://pubmed.ncbi.nlm.nih.gov/17696798/) | 2007 | Review | Expert Opin Pharmacother | PEG-asparaginase의 약리학·임상활성·과민반응 관련 종합 고찰 |
| [21454191](https://pubmed.ncbi.nlm.nih.gov/21454191/) | 2011 | Cohort | Clin Lymphoma Myeloma Leuk | 재발 성인 ALL 구제요법에서 vincristine/dexamethasone/asparaginase 용량강화 hyper-CVAD 성적 |
| [40163215](https://pubmed.ncbi.nlm.nih.gov/40163215/) | 2025 | Phase 2 다기관 연구 | Int J Hematol | 일본인 신규진단 미치료 ALL 환자 대상 pegaspargase 효능·안전성·약동학 평가 |
| [39322712](https://pubmed.ncbi.nlm.nih.gov/39322712/) | 2024 | Phase 2 추적연구 | Leukemia | T-ALL/LBL에서 venetoclax + hyper-CVAD + nelarabine + pegylated asparaginase 장기추적 결과 |
| [9161659](https://pubmed.ncbi.nlm.nih.gov/9161659/) | 1997 | Review | Ann Pharmacother | Pegaspargase의 약리·약동학·투여지침에 대한 초기 종합 고찰 |
| [36227415](https://pubmed.ncbi.nlm.nih.gov/36227415/) | 2022 | 비용효과 분석 | Clin Drug Investig | 그리스에서 소아·청소년·성인 ALL 치료 시 pegaspargase 비용-효용 분석 |

---

## 한국 시판 정보

현재 한국에서 허가된 pegaspargase 품목이 없습니다 (미시판).

---

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 효소 기반 대사길항 항종양제 (Asparagine 고갈형 — 전통적 세포독성 화학요법과는 별도의 기전) |
| 골수억제 위험 | 낮음~중등도 — 직접적 골수억제보다 응고장애(혈전/출혈), 췌장염, 간독성, 고중성지방혈증이 특징적 이상반응으로 문헌에 다수 보고됨 |
| 구토 유발성 등급 | 저~중등도 |
| 모니터링 항목 | 응고인자(피브리노겐 등), 아밀라제/리파아제(췌장염 감시), 간기능, 중성지방·혈당, 과민반응/알레르기 징후 |
| 취급 방호 | 세포독성/항종양 의약품 취급 규정 준수 필요 (조제 시 생물학적 안전 캐비닛 사용 권장) |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
- 임상적 유효성 근거(L1, Phase 3 대규모 RCT 다수) 자체는 매우 견고합니다. 그러나 이는 "신규 적응증 발굴"이 아니라 pegaspargase의 기존 표준 적응증(ALL)을 재확인한 결과로 판단되므로, 재창출(repurposing) 후보로서의 신규성은 낮습니다. 실질적 의사결정 이슈는 효능이 아니라 **한국 내 허가·유통 현황 부재**와 **원 적응증/MOA 데이터 누락(DG001, DG002)** 입니다.

**진행하려면 필요한 것:**
- 한국 식약처(MFDS) 허가 여부 및 향후 도입 계획 확인 (현재 0건 허가, 미시판)
- DrugBank/제조사 자료를 통한 정식 MOA 및 원 적응증 필드 보완 (DG002)
- 한국 허가사항(경고·금기·상호작용) 확보 후 S1 안전성 초평가 진행 (DG001, Blocking)
- 참고: 동일 평가에서 함께 예측된 CLL/SLL, 여포성 림프종, cblE형 대사질환 등은 근거 수준 L5(임상/문헌 근거 전무)로 별도 검증 없이는 Hold 상태를 유지해야 함
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

