---
layout: default
title: Dexamethasone
parent: 높은 근거 (L1-L2)
nav_order: 268
evidence_level: L2
indication_count: 10
monitor_inn: "Dexamethasone"
predicted_indications: ["alopecia areata", "alopecia mucinosa", "telogen effluvium", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions", "alopecia universalis onychodystrophy vitiligo", "prolapse of lacrimal gland"]
last_modified_at: 2026-10-31
description: "Dexamethasone: 예측 신규 적응증 원형탈모증 (근거 수준 L2). 기존 적응증: 습진·피부염군, 양진군, 벌레물린데, 건선, 손·발바닥 농포증, 편평태선, 홍피증, 만성원판상홍반, 약진·중독진…"
---

# Dexamethasone
{: .fs-9 }

근거 수준: **L2** | 예측 적응증: **10** 건
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

## Dexamethasone: 피부 염증성 질환에서 원형탈모증으로
{: .text-alpha }

## 한 문장 요약

Dexamethasone은 강력한 글루코코르티코이드 계열 약물로, 한국 허가 정보상 피부염·건선 등 피부 질환의 치료에 사용됩니다.
TxGNN 모델은 **원형탈모증(alopecia areata)**에 효과가 있을 수 있다고 예측하며, 현재 임상시험 등록은 없으나 **20편의 문헌**(무작위 대照시험 1편 포함)이 이 방향을 다룹니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 습진·피부염군, 양진군, 벌레물린데, 건선, 손·발바닥 농포증, 편평태선, 홍피증, 만성원판상홍반, 약진·중독진, 원형탈모증 (덱사톱크림 허가 문구) |
| 예측 신규 적응증 | 원형탈모증 |
| TxGNN 예측 점수 | 0.9999 |
| 근거 수준 | L2 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 17건) |
| 허가증 수 | 최소 20건 (목록이 일부일 수 있음) |
| 권장 결정 | Proceed with Guardrails |

> 참고: 원형탈모증은 덱사톱크림(외용제) 허가 문구에 이미 포함되어 있습니다. 따라서 외용제 기준으로는 허가 범위 내 사용이며, 이 보고서의 "예측"은 주로 전신(경구·정맥) 투여 용법에 해당합니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, Dexamethasone은 강력한 글루코코르티코이드로서 면역 억제 및 항염증 작용을 가집니다.

원형탈모증은 모낭의 면역 특권이 무너지고 T세포가 모낭을 공격하는 자가면역성 탈모입니다. 글루코코르티코이드는 이러한 면역 반응을 억제할 수 있어 기전상 적용 가능성이 있습니다. 특히 경구 소량 간헐(mini-pulse) 투여는 전신 면역 억제 효과를 얻으면서 누적 스테로이드 노출을 줄이려는 방식입니다.

다만 재발과 스테로이드 부작용이 주된 우려 사항입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [36086930](https://pubmed.ncbi.nlm.nih.gov/36086930/) | 2022 | RCT | Dermatol Ther | 중증 소아 원형탈모증에서 저용량 dexamethasone 경구 mini-pulse와 DPCP 접촉 감작요법의 효과·안전성 비교 (30명) |
| [39042154](https://pubmed.ncbi.nlm.nih.gov/39042154/) | 2024 | 체계적 문헌고찰·네트워크 메타분석 | Arch Dermatol Res | 중증 원형탈모증에서 전신 스테로이드, JAK 억제제, 접촉 면역요법의 비교 효능 |
| [35330017](https://pubmed.ncbi.nlm.nih.gov/35330017/) | 2022 | 전향적 코호트 | J Clin Med | Dexamethasone mini-pulse의 실제 임상 효과와 반응 관련 인자 평가 |
| [36070222](https://pubmed.ncbi.nlm.nih.gov/36070222/) | 2022 | 다기관 연구 | Dermatol Ther | 중등도~중증 원형탈모증에서 경구 dexamethasone mini-pulse 요법 평가 |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | 리뷰 | Pediatr Dermatol | 소아 원형탈모증에서 펄스 코르티코스테로이드의 용량과 투여 방식 검토 |
| [10535249](https://pubmed.ncbi.nlm.nih.gov/10535249/) | 1999 | 임상 연구 | J Dermatol | 광범위 원형탈모증에서 주 2회 5 mg dexamethasone 경구 펄스 |
| [31579982](https://pubmed.ncbi.nlm.nih.gov/31579982/) | 2019 | 전향적 연구 | Dermatol Ther | 소아 중증 원형탈모증에서 정맥 펄스 1일·3일 요법 비교 (73명) |
| [26179196](https://pubmed.ncbi.nlm.nih.gov/26179196/) | 2015 | 장기 추적 연구 | Dermatol Ther | 소아 중증 원형탈모증에서 경구 펄스와 국소 스테로이드 병용 요법 |
| [41872082](https://pubmed.ncbi.nlm.nih.gov/41872082/) | 2026 | 후향적 차트 리뷰 | Eur J Dermatol | baricitinib 병용 시 dexamethasone 펄스 구제요법 (19명) |
| [41243342](https://pubmed.ncbi.nlm.nih.gov/41243342/) | 2025 | 증례 보고 | J Dermatol Treat | JAK 억제제 사용이 어려운 경우 dexamethasone mini-pulse로 지속 관해 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200201703 | 덱사톱크림 | 크림제 | 습진·피부염군, 양진군, 벌레물린데, 건선, 손·발바닥 농포증, 편평태선, 홍피증, 만성원판상홍반, 약진·중독진과 원형탈모증... |
| 198902460 | 페리덱스연고 | 연고제 | 미란(짓무름) 또는 궤양을 수반하는 난치성 구내염 및 설염에 의한 염증의 완화 |
| 202004515 | 이바나파연고 | 연고제 | 미란(짓무름) 또는 궤양을 수반하는 난치성 구내염 및 설염에 의한 염증의 완화 |
| 196300064 | 부광덱사메타손정 | 정제 | 허가 적응증 본문 미확인 |
| 199602981 | 유한덱사메타손정 | 정제 | 허가 적응증 본문 미확인 |

허가 목록은 일부일 수 있으며, 정제·주사제·점안제·안연고 등 다양한 제형이 포함되어 있습니다. 위 표에는 적응증 문구가 확인된 제품을 우선 기재했습니다.

## 안전성 고려사항

**약물 상호작용** (총 100건 조회, 일부 예시):
- **주요(Major)**: Fentanyl, Adalimumab
- **중등도(Moderate)**: Zidovudine, Paclitaxel, Abemaciclib, Isotretinoin, Acalabrutinib, Acarbose, Acebutolol, Codeine, Acetazolamide, Ketorolac, Nifedipine, Ibuprofen 등
- **경미(Minor)**: Dolutegravir, Lidocaine, Formoterol

문헌상 주된 우려는 투여 중단 후 재발과 스테로이드 부작용입니다. 그 외 경고·금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
원형탈모증에 대해 무작위 대조시험 1편, 코호트 연구, 체계적 문헌고찰 등 이 질환을 직접 다룬 연구가 있습니다. 다만 등록된 임상시험이 없고 대부분 소규모·관찰 연구이며, 재발과 스테로이드 부작용 우려가 있어 안전장치를 갖춘 진행을 권장합니다.

**진행하려면 필요한 것:**
- 허가사항의 경고·금기 정보 확보 (현재 확보되지 않아 안전성 선별 단계 진행에 제약이 있음)
- 작용 기전(MOA) 데이터 보완
- 전신 투여 제형(정제·주사제)의 허가 적응증 본문 확인
- 재발 및 장기 스테로이드 노출에 대한 모니터링 계획 수립
- 상호작용 주의 약물(Fentanyl, Adalimumab 등) 병용 시 관리 방안

## 기타 예측 적응증 (참고)

| 순위 | 질환 | 예측 점수 | 근거 수준 | 권장 결정 |
|----|------|---------|---------|---------|
| 2 | 점액성 탈모증 | 0.9999 | L5 | Hold |
| 3 | 휴지기 탈모 | 0.9999 | L5 | Hold |
| 4 | 탈모성 모낭염 | 0.9999 | L5 | Hold |
| 5 | 탈모-항체 결핍 | 0.9999 | L5 | Hold |
| 6 | 반복성 피부 수포를 동반한 유전성 저모증 | 0.9999 | L5 | Hold |
| 7 | 탈모-지적장애-성선기능저하 증후군 | 0.9999 | L5 | Hold |
| 8 | 구진성 병변을 동반한 무모증 | 0.9995 | L5 | Hold |
| 9 | 전신 탈모·손발톱이영양증·백반증 | 0.9976 | L5 | Hold |
| 10 | 눈물샘 탈출증 | 0.9965 | L5 | Hold |

이들은 모델 예측만 있거나 직접 근거가 없어 보류를 권장합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

