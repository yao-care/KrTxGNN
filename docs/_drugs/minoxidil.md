---
layout: default
title: Minoxidil
parent: 모델 예측만 (L5)
nav_order: 518
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Minoxidil: 예측 신규 적응증 두피 단순 저모증 (Hypotrichosis simplex of the scalp) (근거 수준 L5). 기존 적응증: 남성형 탈모증(안드로젠탈모증)"
monitor_inn: "Minoxidil"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "pseudopelade of Brocq", "pulmonary arterial hypertension", "pulmonary arteriovenous malformation (disease)", "pulmonary arterial hypertension associated with congenital heart disease", "primary hereditary glaucoma", "pulmonary arterial hypertension associated with schistosomiasis"]
---

# Minoxidil
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

# Minoxidil: 남성형 탈모증에서 두피 단순 저모증(Hypotrichosis simplex of the scalp)으로

## 한 문장 요약

Minoxidil은 원래 남성형 탈모증(안드로젠탈모증) 치료에 사용되는 약입니다.
TxGNN 모델은 **두피 단순 저모증(hypotrichosis simplex of the scalp)**에 효과가 있을 수 있다고 예측합니다. 현재 이를 지지하는 근거는 **임상시험 0건**과 병용요법 증례 중심의 **문헌 3편**뿐입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 남성형 탈모증(안드로젠탈모증) |
| 예측 신규 적응증 | 두피 단순 저모증 (Hypotrichosis simplex of the scalp) |
| TxGNN 예측 점수 | 99.9999% |
| 근거 수준 | L4 (증례 보고와 기전 추정 수준) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 다만 문헌에 따르면 Minoxidil은 K-ATP 채널을 열어 혈관을 확장시킵니다. 또한 성장기(anagen)를 연장하고 위축된 모낭을 키우는 것으로 알려져 있습니다. 남성형 탈모증에서 효능이 입증된 기전입니다.

유전성 두피 단순 저모증은 모낭이 점차 작아지는 비반흔성 탈모 질환입니다. 모낭 위축이라는 병태가 남성형 탈모증과 비슷해서, 같은 기전이 적용될 수 있다고 추정됩니다. TxGNN 점수도 매우 높습니다.

다만 이 질환은 *CDSN* 유전자 변이 등 단일 유전자 이상으로 생기는 희귀 질환입니다. 기존 근거는 모두 Minoxidil을 성장인자, 식물 추출물, 혈소판풍부혈장(PRP)과 함께 쓴 소규모 보고여서, Minoxidil 단독 효과는 구분할 수 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [35761391](https://pubmed.ncbi.nlm.nih.gov/35761391/) | 2022 | 증례 보고/소규모 증례군 | Dermatologic Therapy | 유전성 두피 단순 저모증에 경구 Minoxidil과 성장인자를 병용해 치료함 |
| [36651821](https://pubmed.ncbi.nlm.nih.gov/36651821/) | 2023 | 증례 보고 | J Dermatol Treat | 14세 환자에서 PRP 주사와 2% 외용 Minoxidil 병용으로 치료에 성공함. 만족스러운 기존 치료법이 없던 질환임 |
| [39902296](https://pubmed.ncbi.nlm.nih.gov/39902296/) | 2024 | 증례 보고 | Frontiers in Genetics | *CDSN* 변이로 진단된 8세 남아에게 식물 추출물과 Minoxidil을 병용함. 확립된 치료법이 없는 질환임 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201803770 | 모나이지액 | 액제 | 남성형 탈모증(안드로젠탈모증) |
| 201905258 | 마이모닉액5% | 액제 | 남성형 탈모증(안드로젠탈모증) |
| 200710117 | 메디녹실액5% | 액제 | 남성형 탈모증(안드로젠탈모증) |
| 200811440 | 마이딜액3% | 외용액제 | 남성형 및 여성형 탈모증(안드로젠탈모증) |
| 201702434 | 마이녹실겔3% | 겔 | 남성형 및 여성형 탈모증(안드로젠탈모증) |

허가증은 총 20건이며 모두 단일제입니다. 이 중 일부 경구 정제는 수출용 허가입니다.

## 안전성 고려사항

- **약물 상호작용**: 약물 상호작용 데이터베이스에서 총 100건이 확인되었습니다. 이 중 확인된 항목은 대부분 중등도(Moderate)입니다.
  - 코르티코스테로이드: Hydrocortisone, Prednisolone, Prednisone, Dexamethasone, Betamethasone, Triamcinolone, Budesonide
  - SGLT2 억제제: Canagliflozin, Dapagliflozin, Empagliflozin, Ertugliflozin
  - 그 외: Bupropion, Morphine, Opium, Dronabinol, Nabilone, Sapropterin
- 등급이 불명(Unknown)인 항목으로 Calcitriol, Clotrimazole, Metformin이 있습니다.
- 경구 저용량 Minoxidil을 쓰면 다모증, 체액 저류, 빈맥, 심낭삼출이 생길 수 있어 심혈관 질환 환자는 주의해야 합니다. 그 밖의 경고와 금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
모델 점수는 매우 높고 기전상 타당성도 있습니다. 그러나 등록된 임상시험이 없고, 근거가 모두 병용요법 증례 3건이라 Minoxidil 단독 효과를 판단할 수 없습니다. 현재는 연구 질문 단계로 보는 것이 적절합니다.

**진행하려면 필요한 것:**
- Minoxidil 단독 또는 대조군을 둔 전향적 연구 (병용 성분의 영향 분리)
- 상세한 작용 기전 데이터 (DrugBank 등)
- 허가사항(경고·금기)의 확인 및 정리
- 소아 환자 대상 용량과 투여 경로(외용/경구) 안전성 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

