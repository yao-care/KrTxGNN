---
layout: default
title: Piroxicam
parent: 모델 예측만 (L5)
nav_order: 606
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Piroxicam: 예측 신규 적응증 Osteoarthritis susceptibility (골관절염 감수성) (근거 수준 L5). 기존 적응증: 퇴행성관절염(골관절염), 어깨관절주위염, 건·건초염, 건주위염, 상완골상과염(테니스 엘보우 등), 근육통(근염, 근막염 등)…"
monitor_inn: "Piroxicam"
predicted_indications: ["osteoarthritis susceptibility", "rheumatoid arthritis", "osteoarthritis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "arthropathy"]
---

# Piroxicam
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

# Piroxicam: 퇴행성관절염에서 골관절염 susceptibility로 (검토 후 실질 후보: 관절병증·골관절염 근거 확인)

> 참고: 예측 1순위(osteoarthritis susceptibility)는 치료 가능한 임상 질환이 아닌 유전적 소인 개념입니다. 아래 보고서는 요청된 첫 번째 예측을 기준으로 작성하되, 근거가 가장 충실한 후보(골관절염, 관절병증)를 함께 평가합니다.

## 한 문장 요약

Piroxicam은 비선택적 COX 억제 NSAID로, 한국에서 퇴행성관절염(골관절염), 건초염, 근육통, 외상 후 동통 등에 사용되어 왔습니다.
TxGNN 모델은 **osteoarthritis susceptibility**를 1순위로 예측했지만(99.99%), 이는 실제 치료 대상이 아니라 유전적 소인 개념이어서 **신규 재창출이라 보기 어렵습니다**.
관련 후보 중에서는 **골관절염**(임상시험 2건, 문헌 19편)과 **관절병증**(임상시험 3건, 문헌 22편)에 근거가 있으나, 골관절염은 이미 허가된 적응증입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 퇴행성관절염(골관절염), 어깨관절주위염, 건·건초염, 건주위염, 상완골상과염(테니스 엘보우 등), 근육통(근염, 근막염 등), 외상 후의 종창·동통의 진통·소염 |
| 예측 신규 적응증 | Osteoarthritis susceptibility (골관절염 감수성) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L4 (1순위 기준). 골관절염·관절병증은 L1, 류마티스 관절염은 L3 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 |
| 권장 결정 | Hold (1순위 기준). 골관절염·관절병증은 Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 확보되지 않았습니다. 알려진 정보에 따르면 Piroxicam은 COX-1/COX-2를 억제해 프로스타글란딘 합성을 줄이고, 이를 통해 관절의 염증과 통증을 완화하는 NSAID입니다.

1순위 예측인 "osteoarthritis susceptibility"는 유전적 위험·소인을 뜻하는 개념이라 COX 억제로 치료할 대상이 아닙니다. 뒷받침하는 문헌도 외용 진통제에 대한 Cochrane 개요와 1988년 NSAID 위장관 손상 예방 시험뿐이라 간접적인 근거에 그칩니다.

반면 골관절염은 이미 한국 허가 적응증이므로 이번 예측은 새로운 재창출이라기보다 기존 효능의 재확인입니다. 관절병증은 골관절염과 염증성 관절질환을 포괄하는 범주여서 Piroxicam의 소염·진통 작용과 기전상 연결됩니다. 류마티스 관절염은 한국 허가 적응증에 없으나 증상 완화 목적의 사용 근거가 있습니다. 다만 질환 경과를 바꾸는 치료는 아니며, 근거도 1983~1995년의 오래된 연구가 중심입니다.

## 임상시험 근거

1순위(osteoarthritis susceptibility)에는 등록된 임상시험이 없습니다. 아래는 관련성이 높은 골관절염·관절병증 후보의 시험입니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT07475663](https://clinicaltrials.gov/study/NCT07475663) | Phase 3 | 완료 | 180 | Piroxicam + 카운터이리턴트 겔 vs 다른 국소 NSAID(Piroxicam 단독 겔, Diclofenac 겔)의 근골격계 통증 효능·안전성 비교 (결과 데이터 미제공) |
| [NCT00670475](https://clinicaltrials.gov/study/NCT00670475) | Phase 2 | 완료 | 60 | 무릎 골관절염에서 올리브 오일 vs 표준 Piroxicam 겔 비교 (Piroxicam은 대조군) |
| [NCT06508203](https://clinicaltrials.gov/study/NCT06508203) | 해당 없음 | 완료 | 40 | 측두하악관절 관절세척술 중 Piroxicam 추가 시 개구량·수술 후 통증 평가 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [29436380](https://pubmed.ncbi.nlm.nih.gov/29436380/) | 2018 | 메타분석 | Br J Sports Med | 골관절염에 대한 국소 NSAID의 상대적 효능·안전성 네트워크 메타분석 |
| [28497473](https://pubmed.ncbi.nlm.nih.gov/28497473/) | 2017 | Review | Cochrane Database Syst Rev | 성인 급·만성 통증에 대한 국소 진통제 Cochrane 리뷰 개요 |
| [21770475](https://pubmed.ncbi.nlm.nih.gov/21770475/) | 2011 | Review | Drugs | 골관절염 통증에 국소 NSAID 효능과 안전성을 뒷받침하는 근거 정리 |
| [8064597](https://pubmed.ncbi.nlm.nih.gov/8064597/) | 1994 | RCT | J Am Podiatr Med Assoc | 발 골관절염에서 Piroxicam과 Naproxen 비교 |
| [2150187](https://pubmed.ncbi.nlm.nih.gov/2150187/) | 1990 | RCT | Curr Med Res Opin | 무릎 골관절염(65명)에서 Etodolac vs Piroxicam 이중맹검 비교 |
| [8458044](https://pubmed.ncbi.nlm.nih.gov/8458044/) | 1993 | RCT | Clin Ther | 류마티스 관절염(118명)에서 Etodolac vs Piroxicam 12주 비교 |
| [6609700](https://pubmed.ncbi.nlm.nih.gov/6609700/) | 1983 | RCT | Bangladesh Med Res Counc Bull | 류마티스 관절염에서 Piroxicam과 Ibuprofen이 유사한 효과이며, 1일 1회 복용이 장점 |
| [7818568](https://pubmed.ncbi.nlm.nih.gov/7818568/) | 1995 | RCT | Arthritis Rheum | 류마티스 관절염에서 Tenidap과 Piroxicam의 급성기 단백·사이토카인 비교 |
| [2957205](https://pubmed.ncbi.nlm.nih.gov/2957205/) | 1987 | Cohort | Eur J Rheumatol Inflamm | 소아 류마티스 관절염(26명)에서 Piroxicam vs Naproxen 안전성·효능 |
| [8054251](https://pubmed.ncbi.nlm.nih.gov/8054251/) | 1994 | PK/DDI 연구 | Br J Clin Pharmacol | 류마티스 관절염 환자에서 NSAID(Piroxicam 포함)와 메토트렉세이트 병용 시 약동학 평가 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201805282 | 피록스겔 | 겔제 | 퇴행성관절염(골관절염), 어깨관절주위염, 건·건초염, 건주위염, 상완골상과염(테니스 엘보우 등), 근육통... |
| 198800043 | 로시덴겔 | 겔제 | 퇴행성관절염(골관절염), 어깨관절주위염, 건·건초염, 건주위염, 상완골상과염(테니스 엘보우 등), 근육통... |
| 202008405 | 트라스트플라스타 | 첩부제 | 퇴행성관절염(골관절염), 건초염(힘줄윤활막염), 근육통, 골관절통, 외상후 동통(통증) 및 골절 치유후의 동통(통증) |
| 199401576 | 트라스트패취 | 패취제 | 퇴행성관절염(골관절염), 건초염(힘줄윤활막염), 근육통, 골관절통, 외상후 동통(통증) 및 골절 치유후의 동통(통증) |
| 201903189 | 일양피록시겔 | 겔제 | 퇴행성관절염(골관절염), 어깨관절주위염, 건·건초염, 건주위염, 상완골상과염(테니스 엘보우 등), 근육통... |

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었습니다. 주요 항목은 다음과 같습니다.
  - 중등도: Acetylsalicylic acid, Hydrocortisone, Dexamethasone, Betamethasone, Triamcinolone, Budesonide, Metformin, Glimepiride, Chlorpropamide, Mesalazine, Balsalazide, Aprepitant, Potassium citrate, Potassium bicarbonate 등
  - 경미: Famotidine, Ranitidine, Cimetidine, Linaclotide 등
- 메토트렉세이트와 NSAID 병용 시 약동학 변화가 보고되어 있어(PMID 8054251) 병용 시 주의가 필요합니다.
- 그 외 경고·금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold** (1순위 osteoarthritis susceptibility 기준)
골관절염·관절병증 후보는 **Proceed with Guardrails**

**사유:**
- 1순위 예측은 치료 가능한 임상 질환이 아닌 유전적 소인이라 재창출 후보로 부적절하며, 직접적인 근거도 없습니다.
- 골관절염과 관절병증은 완료된 Phase 3 시험(NCT07475663)과 메타분석이 있으나, 골관절염은 이미 허가된 적응증이고 Phase 3 결과 데이터도 제공되지 않았습니다.
- 관절병증의 L1 등급은 골관절염 근거와 겹치는 것이어서, 관절병증 자체에 대한 독립적 Phase 3 근거는 아닙니다.
- 나머지 예측(희귀 골격 이형성증 등 rank 4~9)은 모델 예측만 있고 기전적 연관성도 없어 Hold가 적절합니다.

**진행하려면 필요한 것:**
- NCT07475663의 결과 데이터 확인
- MFDS 허가사항(경고·금기) 확보 및 작용 기전 데이터 보완
- 위장관·심혈관·신장 위험과 높은 약물 상호작용 부담을 고려한 모니터링 계획 (고위험 환자는 국소 제형 우선 검토)
- 비골관절염 관절병증 하위 유형(류마티스 관절염 등)에 대한 적응증별 근거 확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

