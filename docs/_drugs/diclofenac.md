---
layout: default
title: Diclofenac
parent: 모델 예측만 (L5)
nav_order: 276
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Diclofenac: 예측 신규 적응증 골관절염 감수성 (osteoarthritis susceptibility) — 1순위 예측 (근거 수준 L5). 기존 적응증: 치은염, 구내염, 인두염 등 구강인두의 염증, 치과 보존치료 또는 발치 후 염증의 완화"
monitor_inn: "Diclofenac"
predicted_indications: ["hypotrichosis simplex of the scalp", "acromesomelic dysplasia, Hunter-Thompson type", "pseudoachondroplasia", "brachyolmia", "brachyolmia-amelogenesis imperfecta syndrome", "congenital hypotrichosis milia", "myosclerosis"]
---

# Diclofenac
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

# Diclofenac: 구강인두 염증·근골격계 통증에서 골관절염(Osteoarthritis)으로

## 한 문장 요약

Diclofenac은 비스테로이드성 소염진통제(NSAID)로, 한국에서 구강인두 염증과 근골격계 통증·염증 치료에 사용되고 있습니다.
TxGNN 모델은 **골관절염 감수성(osteoarthritis susceptibility)**을 최상위 예측으로 제시했지만, 이는 치료 가능한 질환이 아니라 유전적 감수성 표현형입니다. 실질적으로 의미 있는 예측은 2순위인 **골관절염**으로, **다수의 임상시험(Phase 3 포함)**과 **다수의 문헌**이 뒷받침합니다. 다만 골관절염은 이미 허가된 적응증이므로 새로운 재창출 기회가 아니라 기존 적응증의 재확인입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 치은염, 구내염, 인두염 등 구강인두의 염증, 치과 보존치료 또는 발치 후 염증의 완화 |
| 예측 신규 적응증 | 골관절염 감수성 (osteoarthritis susceptibility) — 1순위 예측 |
| TxGNN 예측 점수 | 99.82% |
| 근거 수준 | L4 (1순위 예측 기준). 참고: 2순위 골관절염은 L1 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 |
| 권장 결정 | Hold (1순위 예측 기준). 참고: 2순위 골관절염은 Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Diclofenac은 COX-1/COX-2를 억제하여 프로스타글란딘 매개 염증과 통증을 줄이는 NSAID이며, 구강인두 염증과 근골격계 통증·염증에서 효능이 확립되어 있어 관절 염증 질환에도 기전상 적용 가능합니다.

다만 1순위 예측인 "골관절염 감수성"은 유전적 감수성 표현형으로, Diclofenac이 감수성 자체를 바꾼다는 근거는 없습니다. 연결된 문헌도 골관절염 통증 관리와 Diclofenac 안전성에 관한 것이어서, 임상 질환으로서의 골관절염을 간접적으로 지지할 뿐입니다.

2순위 골관절염의 경우, 활막 염증과 통증을 줄이는 기전이 명확합니다. 여러 Phase 3 임상시험과 체계적 문헌고찰이 경구 및 국소 제형의 효능을 지지합니다. 이미 한국 허가 적응증(퇴행성 관절염, 골관절염)에 포함되어 있으므로 새로운 적응증이 아닌 기존 적응증의 확인입니다.

## 임상시험 근거

1순위 예측(골관절염 감수성)에는 연결된 임상시험이 없습니다. 아래는 2순위 골관절염에 대한 주요 시험입니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00171652](https://clinicaltrials.gov/study/NCT00171652) | Phase 3 | 완료 | 360 | 수지 골관절염에서 Diclofenac 겔의 효능·안전성 평가 |
| [NCT00542087](https://clinicaltrials.gov/study/NCT00542087) | Phase 3 | 완료 | 516 | 무릎·고관절 골관절염에서 etoricoxib vs Diclofenac 6주 안전성·내약성 비교 |
| [NCT00108992](https://clinicaltrials.gov/study/NCT00108992) | Phase 3 | 완료 | 750 | 무릎 골관절염에서 국소+경구 Diclofenac 병용의 효능·안전성 |
| [NCT02596451](https://clinicaltrials.gov/study/NCT02596451) | Phase 3 | 완료 | 1164 | 무릎 골관절염에서 Diclofenac 1% 겔 제네릭의 Voltaren 겔 대비 치료적 동등성 |
| [NCT02121002](https://clinicaltrials.gov/study/NCT02121002) | Phase 3 | 완료 | 1176 | 무릎 골관절염에서 제네릭 Diclofenac 겔 vs Voltaren 겔 |
| [NCT00250445](https://clinicaltrials.gov/study/NCT00250445) | Phase 3 | 완료 | 23,498 | 골관절염·류마티스 관절염에서 etoricoxib vs Diclofenac의 심혈관·위장관 안전성 비교 |
| [NCT00546832](https://clinicaltrials.gov/study/NCT00546832) | Phase 3 | 완료 | 650 | 무릎 골관절염에서 Diclofenac 국소 스프레이 vs celecoxib·위약 |
| [NCT01967550](https://clinicaltrials.gov/study/NCT01967550) | Phase 3 | 완료 | 304 | 무릎 골관절염에서 Diclofenac diethylamine 2.32% 겔 vs 위약 |
| [NCT06693648](https://clinicaltrials.gov/study/NCT06693648) | Phase 3 | 완료 | 549 | 무릎 골관절염에서 1일 1회 Diclofenac 겔(AMZ001) vs 위약 (Diclofenac의 역할은 확인 불가) |
| [NCT00141102](https://clinicaltrials.gov/study/NCT00141102) | Phase 4 | 완료 | 4484 | 위장관 고위험 환자에서 celecoxib vs Diclofenac+omeprazole의 위장관 이상반응 비교 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [34642179](https://pubmed.ncbi.nlm.nih.gov/34642179/) | 2021 | 메타분석 | BMJ | 무릎·고관절 골관절염에서 NSAID, 오피오이드의 효과와 안전성에 대한 네트워크 메타분석 |
| [40065343](https://pubmed.ncbi.nlm.nih.gov/40065343/) | 2025 | 메타분석 | BMC Musculoskelet Disord | 무릎 골관절염에서 국소 Diclofenac 제형(겔, 용액, 패치)의 효능·안전성 |
| [29436380](https://pubmed.ncbi.nlm.nih.gov/29436380/) | 2018 | 메타분석 | Br J Sports Med | 골관절염에서 국소 NSAID의 상대적 효능·안전성 비교 |
| [40333622](https://pubmed.ncbi.nlm.nih.gov/40333622/) | 2025 | 메타분석 | PLoS One | 골관절염에서 여러 NSAID의 효능·안전성에 대한 RCT 기반 네트워크 메타분석 |
| [28497473](https://pubmed.ncbi.nlm.nih.gov/28497473/) | 2017 | 리뷰 | Cochrane Database Syst Rev | 성인 급·만성 통증에 대한 국소 진통제 Cochrane 리뷰 개관 |
| [30975196](https://pubmed.ncbi.nlm.nih.gov/30975196/) | 2019 | RCT | Trials | 무릎 골관절염에서 커큐민 vs Diclofenac의 효능·안전성 |
| [26212849](https://pubmed.ncbi.nlm.nih.gov/26212849/) | 2015 | RCT | Br J Gen Pract | 1차 진료에서 무릎 골관절염 환자 대상 Diclofenac vs 파라세타몰 |
| [32797224](https://pubmed.ncbi.nlm.nih.gov/32797224/) | 2021 | 메타분석 | Pain Med | 무릎 골관절염에서 celecoxib vs Diclofenac 비교 |
| [14575648](https://pubmed.ncbi.nlm.nih.gov/14575648/) | 2003 | 리뷰 | Toxicol Appl Pharmacol | Diclofenac 유발 간손상: 특이체질성 약물 독성의 대표 사례 |
| [2232043](https://pubmed.ncbi.nlm.nih.gov/2232043/) | 1990 | 증례 보고 | JAMA | Diclofenac 관련 간독성 7례 (사망 1례 포함) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202008458 | 조아구강청액(디클로페낙) | 액제 | 치은염, 구내염, 인두염 등의 구강인두 염증, 치과 보존치료 또는 발치 후 염증의 완화 |
| 201802608 | 코디톱쿨플라스타(디클로페낙나트륨) | 첩부제 | 퇴행성 관절염(골관절염), 어깨관절 주위염, 힘줄 및 힘줄윤활막염, 힘줄주위염, 위팔뼈상과염(테니스엘보 등)... |
| 202101212 | 아프모겐큐인후스프레이(디클로페낙) | 정량분무용 액제 | 치은염, 구내염, 인두염 등의 구강인두 염증, 치과 보존치료 또는 발치 후 염증의 완화 |
| 202401785 | 류마스탑파워플라스타(디클로페낙나트륨) | 첩부제 | 골관절염, 어깨관절 주위염, 힘줄 및 힘줄윤활막염, 힘줄 주위염, 팔꿈치 통증(테니스엘보), 근육통, 외상 후 부기 및 통증 |
| 202003874 | 휴디낙점안액(디클로페낙나트륨) | 점안액 | 허가 적응증 본문 확인 필요 (허가사항 참조) |

## 안전성 고려사항

- **약물 상호작용**: 데이터 조회 결과 총 100건이 확인되었으며, 대표적으로 다음 약물과의 상호작용이 보고되었습니다.
  - 중등도(Moderate): 아세틸살리실산(아스피린), 코르티코스테로이드(hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), metformin, 설폰요소계 혈당강하제(glimepiride, glipizide, chlorpropamide, acetohexamide), mesalazine, balsalazide, aprepitant, exenatide, fenfluramine 계열
  - 경미(Minor): famotidine, ranitidine, cimetidine
- **문헌에서 확인된 위험**: 드물지만 중대한 특이체질성 간독성(PMID 14575648, 2232043, 10414481). 이 외에 NSAID 계열의 심혈관·위장관·신장 위험이 임상시험과 문헌에서 논의됩니다. 이러한 위험은 국소 제형에서 상대적으로 낮은 것으로 알려져 있습니다.

허가사항의 경고 및 금기 항목은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold** (1순위 예측 "골관절염 감수성" 기준)

**사유:**
1순위 예측은 유전적 감수성 표현형으로 치료 대상 질환이 아니며, Diclofenac이 감수성을 변화시킨다는 근거가 없어 재창출 후보로서 의미가 없습니다. 2순위 골관절염은 다수의 Phase 3 시험과 메타분석으로 근거가 강하지만(L1, Proceed with Guardrails) 이미 한국에서 허가된 적응증이므로 새로운 재창출 기회가 아닙니다. 이 밖에 상위 예측인 희귀 유전성 질환들(모발 저형성증, 말단중간부 이형성증, 가성연골무형성증, 단완증 등)은 연결된 임상시험과 문헌이 없고 기전적 연관성도 확인되지 않아 보류(Hold)가 적절합니다. 근위축성 근경화증과 구별되는 근경화증(myosclerosis)은 증상 완화 가능성이 있으나 가설 수준의 연구 질문에 머뭅니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기) 확보: 현재 안전성 정보가 확보되지 않아 안전성 1차 검토를 진행할 수 없음
- 상세한 약물 작용 기전(MOA) 데이터 확보
- 골관절염 외 관절병증(TMJ 통증 등)에 대한 신규 적응증 평가가 필요하면 별도의 적응증 단위 분석
- 심혈관·위장관·신장·간 위험을 고려해, 위험 환자에는 국소 제형 우선, 최소 유효 용량·최단 기간 사용 원칙을 적용
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

