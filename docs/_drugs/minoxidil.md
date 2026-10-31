---
layout: default
title: Minoxidil
parent: 모델 예측만 (L5)
nav_order: 518
evidence_level: L5
indication_count: 10
monitor_inn: "Minoxidil"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "pseudopelade of Brocq", "pulmonary arterial hypertension", "pulmonary arteriovenous malformation (disease)", "pulmonary arterial hypertension associated with congenital heart disease", "primary hereditary glaucoma", "pulmonary arterial hypertension associated with schistosomiasis", "pulmonary arterial hypertension associated with chronic hemolytic anemia"]
last_modified_at: 2026-10-31
description: "Minoxidil: 예측 신규 적응증 두피 단순 저모발증 (hypotrichosis simplex of the scalp) (근거 수준 L5). 기존 적응증: 남성형 탈모증(안드로젠탈모증)"
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

## Minoxidil: 남성형 탈모증에서 두피 단순 저모발증으로
{: .text-alpha }

## 한 문장 요약

Minoxidil은 한국에서 남성형 탈모증(안드로젠탈모증) 치료제로 허가되어 있으며, 일부 제품은 여성형 탈모증에도 허가되어 있습니다.
TxGNN 모델은 **두피 단순 저모발증(hypotrichosis simplex of the scalp)**에 효과가 있을 수 있다고 예측합니다.
다만 이 질환을 직접 다룬 근거는 **소규모 증례 보고 3편**뿐이고 등록된 임상시험은 없으며, 모두 병용요법이라 Minoxidil 단독 효과는 확인할 수 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 남성형 탈모증(안드로젠탈모증) |
| 예측 신규 적응증 | 두피 단순 저모발증 (hypotrichosis simplex of the scalp) |
| TxGNN 예측 점수 | 1.0000 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

근거 수준은 L5로 판정했습니다. 직접 해당 질환을 다룬 문헌은 3편이 있으나, 모두 병용요법 증례 보고라서 Minoxidil 단독 효과를 평가할 수 없고, 임상시험도 없기 때문입니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Minoxidil은 활성 대사체인 minoxidil sulfate를 통해 ATP 민감성 칼륨 채널을 열고, 성장기(anagen)를 연장하며, 모낭 혈관 확장과 VEGF 발현을 촉진하는 것으로 알려져 있습니다.

두피 단순 저모발증은 CDSN 유전자 변이와 관련된 드문 상염색체 우성 유전 질환으로, 비흉터성 모발 가늘어짐을 보입니다. 모낭 성장을 자극하는 기전은 이 질환에도 적용될 수 있습니다. 그러나 이는 가설적 연결이며, 확립된 치료법이 아직 없는 질환이라는 점도 문헌에서 언급됩니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [35761391](https://pubmed.ncbi.nlm.nih.gov/35761391/) | 2022 | 증례 보고/시리즈 | Dermatologic Therapy | 유전성 두피 단순 저모발증에서 경구 Minoxidil과 성장인자 병용 치료 |
| [39902296](https://pubmed.ncbi.nlm.nih.gov/39902296/) | 2024 | 증례 보고 | Frontiers in Genetics | CDSN 변이로 인한 HSS 8세 남아에서 식물 추출물과 Minoxidil 병용 치료 |
| [36651821](https://pubmed.ncbi.nlm.nih.gov/36651821/) | 2023 | 증례 보고 | J Dermatol Treat | 14세 환자에서 PRP 주사와 국소 Minoxidil 2% 병용 치료로 호전 보고 |

세 편 모두 병용요법이므로 Minoxidil 자체의 효과는 분리할 수 없습니다.

## 한국 시판 정보

기존 허가 적응증은 한국 허가증 기준입니다. 아래는 주요 허가 5건이며, 전체 목록은 일부일 수 있습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201803770 | 모나이지액 | 액제 | 남성형 탈모증(안드로젠탈모증) 치료 |
| 201905258 | 마이모닉액5% | 액제 | 남성형 탈모증(안드로젠탈모증) 치료 |
| 200811440 | 마이딜액3% | 외용액제 | 남성형 및 여성형 탈모증(안드로젠탈모증) 치료 |
| 201702434 | 마이녹실겔3% | 겔 | 남성형 및 여성형 탈모증(안드로젠탈모증) 치료 |
| 198701670 | 마이녹실액3% | 액제 | 남성형 및 여성형 탈모증(안드로젠탈모증) 치료 |

## 안전성 고려사항

- **약물 상호작용**: 약물 상호작용 데이터베이스에서 총 100건이 확인되었습니다. 주요 항목은 중등도(Moderate)로, 코르티코스테로이드(hydrocortisone, dexamethasone, prednisone 등), SGLT2 억제제(dapagliflozin, empagliflozin 등), bupropion, morphine 등이 포함됩니다.

경고 및 금기 등 그 외 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
두피 단순 저모발증에 대한 근거는 병용요법 증례 보고 3편뿐이며, 임상시험이 없고 Minoxidil 단독 효과를 확인할 수 없습니다. TxGNN 점수는 매우 높지만 이는 모델 예측일 뿐이며, 현 단계에서는 추가 연구 질문으로 다루는 것이 적절합니다.

**진행하려면 필요한 것:**
- Minoxidil 단독 효과를 평가할 수 있는 대조 연구 또는 체계적 증례 수집
- 작용 기전(MOA) 데이터 확보
- 허가사항 기반의 경고·금기 정보 확보 (현재 안전성 선별을 진행하기에 부족함)
- 소아 환자 등 대상 집단에 대한 안전성 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

