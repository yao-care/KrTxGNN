---
layout: default
title: Dexamethasone
parent: 모델 예측만 (L5)
nav_order: 268
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Dexamethasone: 예측 신규 적응증 원형탈모증 (Alopecia Areata) (근거 수준 L5). 기존 적응증: 습진·피부염군, 양진군, 벌레물린데, 건선, 손·발바닥 농포증, 편평태선, 홍피증, 만성원판상홍반…"
monitor_inn: "Dexamethasone"
predicted_indications: ["alopecia areata", "alopecia mucinosa", "telogen effluvium", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions", "tenosynovitis", "granulomatous slack skin disease"]
---

# Dexamethasone
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

# Dexamethasone: 피부 염증 질환에서 원형탈모증으로

## 한 문장 요약

Dexamethasone은 강력한 글루코코르티코이드로, 한국에서 염증성 질환 치료에 사용되어 왔으며 외용제는 원형탈모증을 포함한 피부질환에 허가되어 있습니다.
TxGNN 모델은 **원형탈모증(Alopecia Areata)**에 효과가 있을 수 있다고 예측하며, 이 예측을 지지하는 **문헌 20편**이 확인되었습니다(임상시험 등록은 없음).
이 중 소아 대상 무작위 대조 시험(RCT) 1건과 다수의 코호트·증례 연구가 경구 소량 펄스 요법의 효과를 보고합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 습진·피부염군, 양진군, 벌레물린데, 건선, 손·발바닥 농포증, 편평태선, 홍피증, 만성원판상홍반, 약진·중독진과 원형탈모증의 치료 (덱사톱크림 기준) |
| 예측 신규 적응증 | 원형탈모증 (Alopecia Areata) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L2 (소규모 RCT 1건 포함, 다만 Phase 2/3 완료 시험은 아님) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 |
| 권장 결정 | Proceed with Guardrails |

> 참고: 외용제(덱사톱크림)의 허가 적응증에 이미 원형탈모증이 포함되어 있어, 이번 예측은 새로운 질환이라기보다 **경구·정맥 펄스 투여로의 투여 경로·용법 확장**에 가깝습니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Dexamethasone은 강력한 글루코코르티코이드로, 면역 반응을 억제하는 항염증 약물입니다. 원형탈모증은 T세포가 모낭을 공격하는 자가면역 질환이며, 면역 특권(immune privilege)이 무너지면서 발생합니다. Dexamethasone은 이 자가면역 공격을 억제할 수 있습니다.

기존 적응증인 습진, 건선, 편평태선 등은 모두 면역·염증이 관여하는 피부질환입니다. 따라서 같은 항염증 기전이 원형탈모증에도 적용될 수 있습니다. 실제로 주 2일 연속 5 mg을 복용하는 경구 소량 펄스 요법이 임상에서 이미 사용되고 있습니다.

다만 전신 투여는 스테로이드 관련 이상반응이 있고, 투여를 중단하면 재발하는 경우가 흔합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [36086930](https://pubmed.ncbi.nlm.nih.gov/36086930/) | 2022 | RCT | Dermatologic Therapy | 중증 소아 원형탈모증 30명 대상, Dexamethasone 경구 소량 펄스와 DPCP 접촉감작 요법의 효과·안전성 비교 |
| [39042154](https://pubmed.ncbi.nlm.nih.gov/39042154/) | 2024 | 체계적 문헌고찰/네트워크 메타분석 | Arch Dermatol Res | 중증 원형탈모증에서 전신 스테로이드, JAK 억제제, 접촉면역요법의 효능 비교 |
| [35330017](https://pubmed.ncbi.nlm.nih.gov/35330017/) | 2022 | 전향적 코호트 | J Clin Med | 실제 임상 환경에서 경구 소량 펄스 요법의 효과·안전성 및 반응 관련 인자 평가 |
| [36070222](https://pubmed.ncbi.nlm.nih.gov/36070222/) | 2022 | 다기관 코호트 | Dermatologic Therapy | 중등도~중증 원형탈모증에서 경구 Dexamethasone 소량 펄스 요법 평가 |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | 리뷰 | Pediatric Dermatology | 소아 원형탈모증에서 펄스 코르티코스테로이드의 용량 및 투여 방식 검토 |
| [31579982](https://pubmed.ncbi.nlm.nih.gov/31579982/) | 2019 | 전향적 연구 | Dermatologic Therapy | 소아 중증 원형탈모증 73명, 1일 vs 3일 정맥 펄스와 국소 스테로이드 병용 비교 |
| [26179196](https://pubmed.ncbi.nlm.nih.gov/26179196/) | 2015 | 장기 추적 연구 | Dermatologic Therapy | 소아 65명, 경구 펄스와 국소 스테로이드 병용의 장기(중앙값 96개월) 추적 |
| [10535249](https://pubmed.ncbi.nlm.nih.gov/10535249/) | 1999 | 임상 연구 | J Dermatol | 광범위 원형탈모증 30명에서 주 2회 5 mg 경구 펄스 요법 평가 |
| [41872082](https://pubmed.ncbi.nlm.nih.gov/41872082/) | 2026 | 후향적 연구 | Eur J Dermatol | 중증 원형탈모증에서 Baricitinib 반응이 없을 때 Dexamethasone 펄스 구제요법 경험 |
| [41243342](https://pubmed.ncbi.nlm.nih.gov/41243342/) | 2025 | 증례 보고 | J Dermatol Treat | JAK 억제제 사용이 어려운 중증 환자에서 경구 소량 펄스로 지속적 관해 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200201703 | 덱사톱크림 (덱사메타손프로피오네이트) | 크림제 | 습진·피부염군, 양진군, 벌레물린데, 건선, 손·발바닥 농포증, 편평태선, 홍피증, 만성원판상홍반, 약진·중독진과 원형탈모증의 치료 |
| 198902460 | 페리덱스연고 (덱사메타손) | 연고제 | 미란 또는 궤양을 수반하는 난치성 구내염 및 설염에 의한 염증의 완화 |
| 202004515 | 이바나파연고 (덱사메타손) | 연고제 | 미란 또는 궤양을 수반하는 난치성 구내염 및 설염에 의한 염증의 완화 |
| 196300064 | 부광덱사메타손정 | 정제 | 허가 적응증 본문은 문서 링크로만 제공됨 |
| 199602981 | 유한덱사메타손정 | 정제 | 허가 적응증 본문은 문서 링크로만 제공됨 |

전체 20건 가운데 정제·주사제·점안제·안연고 등 다양한 제형이 허가되어 있으며, 모두 단일 성분 제제입니다.

## 안전성 고려사항

- **약물 상호작용**: 약물 상호작용 데이터베이스에서 100건이 확인되었습니다. 이 중 주요(Major) 등급은 다음과 같습니다.
  - Fentanyl
  - Adalimumab
- 중등도(Moderate) 등급에는 Paclitaxel, Zidovudine, Abemaciclib, Acalabrutinib, Isotretinoin, Ketorolac, Ibuprofen, Nifedipine 등이 포함됩니다.
- 전신 투여 시 스테로이드 관련 이상반응이 있을 수 있고, 중단 후 재발이 흔합니다.

경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
소아 RCT 1건, 네트워크 메타분석, 다수의 코호트 연구가 경구·정맥 펄스 요법의 효과를 뒷받침하며, 외용제는 이미 원형탈모증에 허가되어 있습니다. 다만 완료된 Phase 2/3 임상시험은 없고, 전신 투여에 따른 안전성 우려와 재발 문제가 있어 조건부로 진행합니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기) 확인 및 전신 투여 시 안전성 모니터링 계획 수립
- 작용 기전 데이터 보완
- 경구 펄스 요법에 대한 적절한 용량·기간을 정하는 대규모 대조 시험 또는 가이드라인 근거 확보
- 재발 관리 전략과 JAK 억제제 대비 위치 설정

---

### 참고: 기타 예측 적응증

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 | 권장 결정 |
|---|---|---|---|---|
| 2 | Alopecia mucinosa | 99.99% | L5 | Hold |
| 3 | Telogen effluvium | 99.99% | L5 | Hold |
| 4 | Folliculitis decalvans | 99.99% | L5 | Hold |
| 5 | Alopecia antibody deficiency | 99.99% | L5 | Hold |
| 6 | 반복성 피부 수포를 동반한 유전성 저모증 | 99.99% | L5 | Hold |
| 7 | 탈모-지적장애-성선기능저하증 증후군 | 99.99% | L5 | Hold |
| 8 | 구진성 병변을 동반한 무모증 | 99.95% | L5 | Hold |
| 9 | 건초염 (Tenosynovitis) | 99.83% | L2 | Proceed with Guardrails |
| 10 | 육아종성 이완피부병 | 99.78% | L4 | Hold |

건초염은 Phase 3·4 시험 2건이 있으나 모두 조기 종료되었고, 국소 스테로이드 주사가 이미 임상에서 통용되는 용도입니다. 나머지는 직접적인 근거가 없거나 관련성이 낮은 문헌만 확인되어 보류를 권장합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

