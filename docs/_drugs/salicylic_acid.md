---
layout: default
title: Salicylic Acid
parent: 모델 예측만 (L5)
nav_order: 682
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Salicylic Acid: 예측 신규 적응증 유두결막염 (Papillary Conjunctivitis) (근거 수준 L5). 기존 적응증: 여드름 치료"
monitor_inn: "Salicylic acid"
predicted_indications: ["papillary conjunctivitis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "rosacea conjunctivitis", "acromesomelic dysplasia, Hunter-Thompson type", "pseudoachondroplasia", "myosclerosis", "brachyolmia"]
---

# Salicylic Acid
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **9** 건
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

## Salicylic acid: 여드름·티눈·사마귀에서 유두결막염(papillary conjunctivitis)으로
{: .text-alpha }

## 한 문장 요약

Salicylic acid(살리실산)는 한국에서 외용제로 여드름, 티눈, 못(굳은살), 사마귀 치료에 사용되어 왔습니다.
TxGNN 모델은 **유두결막염(Papillary Conjunctivitis)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 **임상시험은 0건**, **문헌도 0편**입니다.
따라서 이 예측은 모델 계산 결과일 뿐이며, 실제 연구 근거는 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 여드름 치료 |
| 예측 신규 적응증 | 유두결막염 (Papillary Conjunctivitis) |
| TxGNN 예측 점수 | 0.9988 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 살리실산은 각질용해 작용을 하는 외용 성분이며, COX 억제와 NF-κB 조절 등 항염 작용이 제안되어 있습니다. 다만 공개된 생리활성 데이터로는 이 기전을 확인하지 못했습니다.

항염 작용은 알레르기성 또는 염증성 안구 표면 질환과 이론적으로 연관될 수 있습니다. 그러나 각질용해 외용제는 안구 사용을 전제로 설계되지 않았으며, 자극과 각막 손상 우려가 있습니다. 기존 적응증(여드름, 티눈, 사마귀)과 유두결막염의 병태 생리도 직접적인 연관성이 약합니다.

참고로 예측 상위 10개 중 대부분은 유전성 골격 이형성증 등 희귀 선천성 질환으로, 기전상 연결고리가 확인되지 않아 점수는 TxGNN 모델(딥러닝)이 관련 질환 사이에서 학습한 유사성이 반영된 결과일 수 있으며 생물학적 근거는 아닙니다. 비교적 가능성이 있는 후보는 안구 질환(유두결막염, 주사비 결막염)이나, 이들도 근거가 간접적이거나 약합니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201907451 | 아크원팁스왑액(살리실산) | 면봉 흡착 액제 | 여드름 치료 |
| 200001731 | 티눈스립에이액 | 액제 | 티눈, 못(굳은살) |
| 201703185 | 유클리어톡외용액(살리실산) | 외용액 | 여드름 치료 |
| 201306847 | 클리어틴외용액2%(살리실산) | 외용액 | 여드름 치료 |
| 202001351 | 듀오케어액 | 액제 | 사마귀, 티눈, 못(굳은살) |

그 외 허가 15건은 경고제, 겔, 연고, 첩부제, 두피 케어액 등이며, 수출용 제품이 일부 포함됩니다.

## 안전성 고려사항

- **약물 상호작용**: 약리학 데이터상 ASIC3 표적과의 관련성이 1건 확인되었으나, 임상적 상호작용 등급은 제시되지 않았습니다.
- **재창출 관련 주의**: 현재 허가 제형은 모두 피부 외용제이며, 안구 적용 시 자극과 각막 손상 위험이 우려됩니다.

그 외 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
유두결막염 예측은 TxGNN 점수(0.9988)만 있고 임상시험과 문헌이 없어 근거 수준이 L5입니다. 또한 기존 제형이 안구 사용에 적합하지 않아 안전성 우려가 있습니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기)의 확보 및 분석
- 상세한 작용 기전(MOA) 데이터 확보
- 유두결막염 관련 전임상 또는 문헌 근거 탐색
- 안구 적용 가능한 제형 및 투여 경로의 적합성 검토와 안구 안전성 평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

