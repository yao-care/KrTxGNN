---
layout: default
title: Tenoxicam
parent: 모델 예측만 (L5)
nav_order: 727
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Tenoxicam: 예측 신규 적응증 류마티스 관절염 (Rheumatoid Arthritis) (근거 수준 L5). 기존 적응증: 허가 문서 링크만 제공되어 구체적 문구 확인 불가 (허가사항 참조)"
monitor_inn: "Tenoxicam"
predicted_indications: ["rheumatoid arthritis", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "osteoarthritis susceptibility", "headache disorder", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "trigeminal autonomic cephalalgia", "alopecia"]
---

# Tenoxicam
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

## Tenoxicam: 류마티스 관절염(기허가 적응증)에서 류마티스 관절염으로 — 재창출이 아닌 기존 적응증 확인
{: .text-alpha }

## 한 문장 요약

Tenoxicam은 옥시캄(oxicam) 계열의 비스테로이드성 소염진통제(NSAID)로, 한국에서 단일제로 허가되어 시판되고 있습니다.
TxGNN 모델은 **류마티스 관절염(rheumatoid arthritis)**을 최상위 예측 질환으로 제시했으며, 이는 새로운 적응증이라기보다 이미 임상에서 널리 확립된 용도에 가깝습니다.
이 방향을 지지하는 문헌은 **19편**이며, 이 질환에 대한 등록된 임상시험은 없습니다. 참신한 후보로는 **두통 질환(편두통)**에서 진행 중인 Phase 4 시험 1건이 있습니다.

> 참고: 한국 허가증의 적응증 항목은 문서 링크만 제공되어 있어, 허가 적응증 문구를 직접 확인하지 못했습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 문서 링크만 제공되어 구체적 문구 확인 불가 (허가사항 참조) |
| 예측 신규 적응증 | 류마티스 관절염 (Rheumatoid Arthritis) |
| TxGNN 예측 점수 | 99.90% |
| 근거 수준 | L1 (데이터 편집 기준. 다만 아래 임상 근거 참조) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Proceed with Guardrails |

> 근거 수준 L1은 이번 보고서용 데이터의 평가를 따른 것입니다. 엄밀한 규칙(완료된 Phase 3 RCT 2건 이상)으로는 등록 임상시험이 없어 확인되지 않으며, 문헌상 이중맹검 RCT가 존재하는 점을 반영한 판정입니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 없습니다. 알려진 약물 계열 정보에 따르면 Tenoxicam은 옥시캄계 NSAID로, 사이클로옥시게나제(COX-1/COX-2)를 억제해 프로스타글란딘 합성을 줄입니다. 프로스타글란딘은 류마티스 관절염의 염증, 통증, 부종에 관여합니다.

류마티스 관절염은 사실상 Tenoxicam의 기존 사용 영역입니다. 문헌에서도 하루 20 mg 용량이 피록시캄과 동등한 효능을 보인 것으로 보고되어, 높은 TxGNN 점수는 기존 임상 근거와 일치합니다. 다만 이는 진정한 의미의 재창출이 아니라 확립된 용도의 재확인입니다.

그 외 예측 질환 중 **두통 질환**은 프로스타글란딘 매개 염증이 편두통 통증에 관여하고 NSAID가 급성 편두통 치료에 쓰인다는 점에서 기전상 그럴듯합니다. 반면 희귀 선천성 증후군(합지증-단지증 증후군, 소안구증 관련 증후군 등)과 탈모 관련 질환은 기전적 연결이 확인되지 않아 지식 그래프의 인공물로 판단됩니다.

## 임상시험 근거

류마티스 관절염에 대한 등록 임상시험은 현재 없습니다. 참고로 차순위 후보인 두통 질환에는 다음 시험이 있습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT06786650](https://clinicaltrials.gov/study/NCT06786650) | Phase 4 | 진행 중 (모집 종료) | 100 | 급성 편두통 발작에서 정맥 Tenoxicam과 정맥 Ibuprofen의 진통 효과 비교. 결과 미발표 |

## 문헌 근거

류마티스 관절염 관련 주요 문헌입니다(RCT·리뷰 우선).

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [8894360](https://pubmed.ncbi.nlm.nih.gov/8894360/) | 1996 | RCT | Clin Rheumatol | 류마티스 관절염 292명에서 aceclofenac과 Tenoxicam의 효능·안전성을 3개월간 이중맹검 비교 |
| [2695152](https://pubmed.ncbi.nlm.nih.gov/2695152/) | 1989 | 이중맹검 비교시험 | Br J Clin Pract | 골관절염·류마티스 관절염 1,328명에서 Tenoxicam과 piroxicam 비교. Tenoxicam이 전반 평가에서 약간 우세 |
| [1593574](https://pubmed.ncbi.nlm.nih.gov/1593574/) | 1992 | 비교시험 | J Rheumatol | 류마티스 관절염 102명에서 Tenoxicam과 piroxicam의 효능 차이 없음 |
| [3915885](https://pubmed.ncbi.nlm.nih.gov/3915885/) | 1985 | 이중맹검 임상시험 | Eur J Rheumatol Inflamm | 20 mg 1일 1회 용량에서 piroxicam과 같거나 그 이상의 효과 |
| [1711963](https://pubmed.ncbi.nlm.nih.gov/1711963/) | 1991 | Review | Drugs | 경구·직장·비경구 Tenoxicam이 류마티스 질환의 증상 치료에 효과적 |
| [3315620](https://pubmed.ncbi.nlm.nih.gov/3315620/) | 1987 | Review | Drugs | 약력학·약동학 및 치료 효능 예비 검토. 하루 20 mg이 piroxicam과 동등 |
| [3317800](https://pubmed.ncbi.nlm.nih.gov/3317800/) | 1987 | Review | Scand J Rheumatol Suppl | 133건의 임상시험 개관. 위약 대조 이중맹검에서 효능 입증, 최적 용량 20 mg |
| [2292331](https://pubmed.ncbi.nlm.nih.gov/2292331/) | 1990 | 다기관 임상연구 | J Int Med Res | 일반 진료 환경에서 2,963명 대상 12주 투여 후 증상 개선 |
| [8137596](https://pubmed.ncbi.nlm.nih.gov/8137596/) | 1994 | 약동학 리뷰 | Clin Pharmacokinet | 경구 완전 흡수, 혈장 단백 결합률 약 99% |

두통 질환 후보에서는 [27813032](https://pubmed.ncbi.nlm.nih.gov/27813032/) (2016, 편두통 발작에서 트립탄·NSAID·병용 비교)가 있으나 Tenoxicam 특이적 근거는 아닙니다. 또한 탈모(alopecia)에서는 Tenoxicam 부작용으로서의 탈모 증례 보고([9303679](https://pubmed.ncbi.nlm.nih.gov/9303679/), 1997)만 있어 치료 용도가 아닌 안전성 신호로 해석해야 합니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199100422 | 일동테녹시캄정20밀리그램(수출용) | 필름코팅정 | 허가사항 참조 (문서 링크만 제공) |
| 199102714 | 파우민주20밀리그램(테녹시캄)(수출용) | 주사제(냉동건조 분말 바이알) | 허가사항 참조 (문서 링크만 제공) |

두 제품 모두 "수출용"으로 허가된 품목입니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
류마티스 관절염은 문헌상 RCT와 다수의 리뷰로 효능이 뒷받침되는 기존 용도이므로 재창출이라기보다 확인 단계입니다. 그 외 예측 질환 대부분은 기전적 근거가 없어 보류(Hold)가 적절하며, 두통 질환만 연구 과제(Research Question) 수준입니다.

**진행하려면 필요한 것:**
- 허가증 PDF에서 허가 적응증, 경고, 금기 정보 확보 (현재 안전성 스크리닝 진행을 막는 핵심 공백)
- DrugBank 등에서 상세 작용 기전(MOA) 데이터 확보
- 진행 중인 편두통 Phase 4 시험(NCT06786650)의 결과 확인
- 탈모 부작용 신호를 포함한 안전성 모니터링 계획
- 한국 허가 제품이 수출용에 한정되므로, 국내 사용을 검토할 경우 허가 상태 재확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

