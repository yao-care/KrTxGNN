---
layout: default
title: Fenofibrate
parent: 僅模型預測 (L5)
nav_order: 318
evidence_level: L5
indication_count: 7
---

# Fenofibrate
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

# FENOFIBRATE: 이상지질혈증(고중성지방혈증)에서 동형접합 가족성 고콜레스테롤혈증으로

## 한 문장 요약

FENOFIBRATE(DrugBank ID: DB01039)는 PPAR-α 활성화를 통해 작용하는 fibrate 계열 지질강하제로, 국내(한국) 허가 정보는 현재 확인되지 않습니다(미시판, 허가증 0건).
TxGNN 모델은 **동형접합 가족성 고콜레스테롤혈증(Homozygous Familial Hypercholesterolemia, HoFH)**에 효과가 있을 수 있다고 예측(점수 99.91%)하지만, 현재 확보된 **1건의 임상시험**(fenofibrate가 아닌 다른 약물 시험)과 **11편의 문헌**(대부분 가이드라인·리뷰·간접 근거)만으로는 이 적응증을 직접 뒷받침하기 어려운 수준입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (한국 허가 정보 미확보) |
| 예측 신규 적응증 | 동형접합 가족성 고콜레스테롤혈증 (Homozygous Familial Hypercholesterolemia) |
| TxGNN 예측 점수 | 99.91% |
| 근거 수준 | L4 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 없습니다. 알려진 정보에 따르면 FENOFIBRATE는 PPAR-α(peroxisome proliferator-activated receptor alpha) 계열 fibrate이며, 관련 문헌들은 이 약물이 지질단백질 대사(중성지방·LDL·HDL 조절)에 작용함을 일관되게 보여줍니다.

다만 이번 예측 대상인 HoFH는 LDL 수용체가 거의 완전히 결손된 유전 질환으로, 표준 치료는 PCSK9 억제제나 apheresis처럼 수용체 비의존적 청소 경로를 활용합니다. Evidence Pack에 포함된 자체 기전 분석(repurposing_rationale)에 따르면, FENOFIBRATE의 PPAR-α 기전은 이러한 수용체 비의존적 경로에 대한 작용력이 약하며, 확보된 문헌 역시 HoFH 특이적 fenofibrate 개입 연구가 아니라 일반 이상지질혈증 가이드라인이나 오래된 소규모 연구에 그칩니다. 즉 TxGNN의 예측 점수는 높지만, 기전적·임상적 근거는 상대적으로 약한 조합입니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | 완료 | 18 | 8-17세 소아·청소년 HoFH 환자 대상 Alirocumab(PCSK9 억제제) 유효성·안전성 평가 시험. **Fenofibrate를 직접 시험한 연구가 아니며, HoFH 환자군만 동일**(관련성 등급 C) |

FENOFIBRATE를 직접 평가한 HoFH 관련 임상시험은 현재 등록되어 있지 않습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocrine Practice | AACE/ACE 이상지질혈증 관리 및 심혈관질환 예방 가이드라인 |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart Journal | 비스타틴계 지질강하제 개관. Fenofibrate 단독요법의 가장 명확한 적응증은 공복 중성지방 500mg/dL 초과 시 급성췌장염 위험 감소 |
| [26432726](https://pubmed.ncbi.nlm.nih.gov/26432726/) | 2015 | Review | Indian Heart Journal | LDL-C, 스타틴, PCSK9 억제제 개관. 중증 고콜레스테롤혈증에서 스타틴+에제티미브 등 병용요법 논의 |
| [24946816](https://pubmed.ncbi.nlm.nih.gov/24946816/) | 2014 | Review | Internal Medicine Journal | 신흥 지질강하요법 시대의 HoFH 간이식 치료 사례 및 대안 약물 소개 |
| [6593751](https://pubmed.ncbi.nlm.nih.gov/6593751/) | 1984 | Clinical Study | Pharmacological Research Communications | Type II 고지단백혈증 환자 22명 대상 fenofibrate 300mg/day, 4-12개월 투여. HoFH 환자 1명 포함되어 총콜레스테롤·LDL 최대 감소 관찰(HoFH 특이적 연구는 아님) |
| [35499807](https://pubmed.ncbi.nlm.nih.gov/35499807/) | 2022 | pending | Current Atherosclerosis Reports | 임신 중 이상지질혈증 관리 현황과 가이드라인 부재 문제 고찰 |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | pending | Annals of the New York Academy of Sciences | 소아·청소년 이상지질혈증 약물·수술 치료 개관. Fenofibrate 등 여러 요법의 성공 사례 기술 |
| [14620392](https://pubmed.ncbi.nlm.nih.gov/14620392/) | 2003 | pending | Pharmacotherapy | Ezetimibe(선택적 콜레스테롤 흡수억제제) 개관 (fenofibrate 직접 관련 아님) |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | pending | Drugs | Atorvastatin 약리학 및 치료적 유용성 개관 (fenofibrate 직접 관련 아님) |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | pending | Pharmacotherapy | Lomitapide와 기존 지질강하요법(atorvastatin, simvastatin, rosuvastatin, fenofibrate, ezetimibe, niacin) 간 약동학적 상호작용 분석 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 점수는 높으나(99.91%), 확보된 임상시험은 fenofibrate가 아닌 타 약물(Alirocumab) 시험이며 문헌 근거도 HoFH 특이적 fenofibrate 개입 연구가 아닌 일반 가이드라인·리뷰·소규모 구시대 연구 수준(L4)입니다. 자체 기전 분석에서도 HoFH의 병태생리(LDL 수용체 결손)에 FENOFIBRATE의 PPAR-α 기전이 직접적으로 부합하지 않는다고 평가되어, 현 단계에서는 진행을 보류하고 추가 근거 확보가 필요합니다.

**진행하려면 필요한 것:**
- TFDA(식약처) 수준 허가사항(경고/금기) 확보 — 현재 Blocking 등급 데이터 갭(S1 안전성 초평가 진입 불가)
- 상세 작용 기전(MOA) 데이터 확보 — DrugBank API 조회 필요(High 등급 데이터 갭)
- HoFH 환자 대상 FENOFIBRATE 직접 개입 임상시험 또는 최신 관찰 연구
- 한국 내 허가·시판 현황 재확인(현재 라이선스 0건, 미시판 상태)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

