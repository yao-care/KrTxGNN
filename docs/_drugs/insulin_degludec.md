---
layout: default
title: Insulin Degludec
parent: 높은 근거 (L1-L2)
nav_order: 395
evidence_level: L1
indication_count: 6
---

# Insulin Degludec
{: .fs-9 }

근거 수준: **L1** | 예측 적응증: **6** 건
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

# 인슐린 데글루덱(Insulin Degludec): 당뇨병에서 제1형 당뇨병으로

## 한 문장 요약

인슐린 데글루덱(DrugBank ID: DB09564)은 초장시간 작용형 기저 인슐린 유사체입니다. TxGNN 모델은 **제1형 당뇨병(Type 1 Diabetes Mellitus)**에 효과가 있을 것으로 예측(점수 99.44%)했으며, 현재 **50건의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다. 다만 이 사례는 일반적인 "노후 약물의 신규 적응증 발굴"과는 성격이 다릅니다 — 제1형 당뇨병은 인슐린 데글루덱의 이미 확립된 핵심 약리 적응증(외인성 인슐린 보충)이며, TxGNN의 높은 점수는 새로운 가설이 아니라 이미 알려진 약리학적 사실을 반영한 것으로 판단됩니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (한국 허가 자료 미확보) |
| 예측 신규 적응증 | 제1형 당뇨병 (Type 1 Diabetes Mellitus) |
| TxGNN 예측 점수 | 99.44% |
| 근거 수준 | L1 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails (단, 아래 유의사항 참조) |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 확보되지 않았습니다(Drug-level 데이터 갭, 심각도 High). 다만 인슐린 데글루덱이라는 약물의 알려진 분류 정보에 따르면, 이 약물은 초장시간 작용형 기저 인슐린 유사체로, 피하 주사 후 가용성 다중헥사머를 형성하여 서서히 단량체로 분해·흡수되는 방식으로 안정적이고 지속적인 혈당강하 효과를 냅니다.

이 후보는 일반적인 재창출 사례와 다릅니다. 근거팩의 기전 분석에 따르면, 제1형 당뇨병은 인슐린 데글루덱의 **핵심·기존 약리 적응증** 그 자체(수용체 수준에서 직접 작용하는 외인성 인슐린 보충 요법)이며, TxGNN이 지식그래프 추론을 통해 발견한 간접적 신규 연관성이 아닙니다. 즉 99.44%라는 높은 점수는 "새로운 가설"이 아니라 "이미 확립된 사실"을 재확인한 결과로 해석해야 합니다. 이 때문에 아래 임상 근거는 매우 풍부하지만, 진정한 의미의 "노후 약물 신규 적응증 발굴" 사례로 취급하기보다는 데이터 파이프라인 상 검토·제외 대상 여부를 사람이 확인할 필요가 있습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01513473](https://clinicaltrials.gov/study/NCT01513473) | Phase 3 | 완료 | 350 | 소아·청소년 T1DM에서 인슐린 데글루덱 vs 데테미르 비교(BEGIN™ Young 1), 다국가·다기관 RCT |
| [NCT02030600](https://clinicaltrials.gov/study/NCT02030600) | Phase 3 | 완료 | 721 | 인슐린 데글루덱 vs 글라진 무작위 교차 비교(SWITCH 2) |
| [NCT02670915](https://clinicaltrials.gov/study/NCT02670915) | Phase 3 | 완료 | 834 | 소아·청소년 T1DM에서 fast-acting 아스파트 병용 데글루덱 효능·안전성 비교 |
| [NCT06199505](https://clinicaltrials.gov/study/NCT06199505) | Phase 2 | 완료 | 153 | 신약 GZR101과의 head-to-head 비교(적응증 검증이 아닌 약물 간 비교) |
| [NCT02392117](https://clinicaltrials.gov/study/NCT02392117) | N/A | 완료 | 1,262 | T1DM/T2DM 실사용 환경 안전성·유효성 관찰 연구(Tresiba®) |
| [NCT00982228](https://clinicaltrials.gov/study/NCT00982228) | Phase 3 | 완료 | 629 | T1DM에서 데글루덱 vs 글라진 52주 비교(BEGIN™: BB T1 LONG/T1) |
| [NCT03740919](https://clinicaltrials.gov/study/NCT03740919) | Phase 3 | 완료 | 751 | 소아·청소년 T1DM에서 LY900014 vs 인슐린 리스프로 비교 |
| [NCT04974528](https://clinicaltrials.gov/study/NCT04974528) | Phase 3 | 완료 | 319 | 소아 T1DM/T2DM에서 흡입형 인슐린 vs 속효성 인슐린+기저인슐린 비교(INHALE-1) |
| [NCT03938740](https://clinicaltrials.gov/study/NCT03938740) | Phase 2 | 완료 | 61 | T1DM에서 간표적 인슐린 리스프로 vs 데글루덱 기저 인슐린 용량 알고리즘 비교 |
| [NCT06238778](https://clinicaltrials.gov/study/NCT06238778) | Phase 2 | 진행 중 | 227 | 데글루덱 병용 중인 T1DM 성인에서 HDV-인슐린 리스프로 비교 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | 임신한 T1DM 여성에서 데글루덱 vs 데테미르 비열등성 시험(EXPECT) |
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | Phase 3a RCT | Lancet | 주 1회 인슐린 아이코덱 vs 매일 데글루덱, T1DM 대상 치료목표 도달 시험(ONWARDS 6) |
| [39270686](https://pubmed.ncbi.nlm.nih.gov/39270686/) | 2024 | Phase 3 RCT | Lancet | 주 1회 efsitora alfa vs 데글루덱, T1DM 비열등성 시험(QWINT-5) |
| [34643020](https://pubmed.ncbi.nlm.nih.gov/34643020/) | 2022 | RCT | Diabetes Obes Metab | 야간 중증 저혈당 취약 T1DM 환자에서 데글루덱 vs 글라진 U100 교차 비교(HypoDeg) |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | 체계적 문헌고찰/메타분석 | Clin Ther | T1DM·T2DM에서 데글루덱과 타 장시간 기저 인슐린 유효성·내약성 비교 |
| [35476308](https://pubmed.ncbi.nlm.nih.gov/35476308/) | 2022 | 체계적 문헌고찰 | Int J Clin Pharm | T1DM에서 데글루덱 U100 vs 글라진 U300 안전성·유효성·비용효과 간접비교 |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | 체계적 문헌고찰/네트워크 메타분석 | Value Health | 성인 T1DM 기저 인슐린 요법 비교 |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Review | Lancet Diabetes Endocrinol | 임신 중 T1DM 관리(생활습관·약물·신기술 포함) |
| [31055056](https://pubmed.ncbi.nlm.nih.gov/31055056/) | 2020 | Review | Diabetes Metab | RCT 및 관찰연구 기반 T1DM/T2DM에서 데글루덱 현황 |
| [23890782](https://pubmed.ncbi.nlm.nih.gov/23890782/) | 2014 | Review | Endocrinol Nutr | T1DM/T2DM 치료용 초장시간 기저 인슐린 데글루덱의 임상연구 발전 |

## 한국 시판 정보

현재 한국에 시판 중인 인슐린 데글루덱 제품이 없습니다 (허가증 0건, 미시판).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails** *(단, 아래 유의사항 전제)*

**사유:**
- 임상 근거 자체는 매우 강력합니다(완료된 Phase 3 RCT 다수, 근거 수준 L1). 그러나 이 후보는 진정한 "노후 약물 신규 적응증"이 아니라 인슐린 데글루덱의 기존 핵심 적응증(T1DM)을 TxGNN이 재확인한 사례일 가능성이 높습니다. 파이프라인 상 실제 재창출 후보로 분류할지, 아니면 학습 데이터 편향(기존 적응증 재발견)으로 제외할지 사람의 판단이 필요합니다.
- Blocking 데이터 갭(DG001: 식약처 라벨 경고·금기사항 부재)이 해결되지 않아 안전성 초기평가(S1) 단계를 정식으로 통과하지 못한 상태입니다.

**진행하려면 필요한 것:**
- 식약처(허가기관) 라벨 PDF 확보 및 경고·금기·DDI 정보 파싱 (DG001, Blocking)
- DrugBank API를 통한 상세 작용기전(MOA) 데이터 보완 (DG002, High)
- 이 후보가 "신규 적응증 발굴"인지 "기존 적응증 재확인"인지에 대한 전문가 검토 및 분류
- 한국 시판 현황 모니터링(현재 미시판이므로 향후 허가 여부 추적)

참고: 같은 근거팩에 포함된 나머지 5개 예측 적응증(자가면역 난소염, opsismodysplasia, 티아민 반응성 기능장애 증후군, 전형적/국소형 뻣뻣한 사람 증후군)은 모두 임상시험·문헌 근거가 전무한 근거 수준 L5(모델 예측만 존재)로, 권장 결정은 Hold입니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

