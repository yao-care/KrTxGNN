---
layout: default
title: Mirtazapine
parent: 모델 예측만 (L5)
nav_order: 483
evidence_level: L5
indication_count: 3
---

# Mirtazapine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **3** 건
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

# Mirtazapine: 우울증(항우울제)에서 Ohdo 증후군으로

## 한 문장 요약

Mirtazapine은 α2-아드레날린 수용체 길항, 5-HT2/5-HT3 길항, H1 길항 기전을 가진 항우울제입니다. TxGNN 모델은 **Ohdo 증후군 및 변이형(Ohdo syndrome and variants)**에 효과가 있을 수 있다고 예측했으나, 이를 지지하는 임상시험이나 문헌은 **0건**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 우울증 (항우울제, 공식 허가 데이터 없음) |
| 예측 신규 적응증 | Ohdo 증후군 및 변이형 (Ohdo syndrome and variants) |
| TxGNN 예측 점수 | 99.42% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 확보되지 않았습니다(DrugBank API 조회 필요, High severity data gap). 다만 알려진 정보에 따르면 Mirtazapine은 α2-아드레날린 수용체 길항, 5-HT2/5-HT3 세로토닌 수용체 길항, H1 히스타민 수용체 길항을 통해 작용하는 항우울제(NaSSA 계열)입니다.

Ohdo 증후군(SBBYSS형 포함)은 KAT6A/KAT6B 등 히스톤 아세틸전달효소 유전자 돌연변이로 인한 선천성 발달장애로, 병인이 염색질 조절 이상이며 신경전달물질 불균형과는 무관합니다. Mirtazapine의 수용체 조절 기전은 이러한 유전적·발생학적 경로와 알려진 연관성이 없습니다. TxGNN의 높은 점수(99.42%)는 지식 그래프 내 '항우울제-정신/행동 증상' 노드 간 간접 연결에서 비롯된 잡음일 가능성이 높으며, 기전상 타당성을 반영한다고 보기 어렵습니다.

같은 근거로 예측된 2순위(blepharophimosis - intellectual disability syndrome, Ohdo type, 99.11%)와 3순위(benign paroxysmal torticollis of infancy, 99.11%) 후보 역시 모두 임상시험·문헌 근거가 전무하며, 각각 유전적 병인(2순위) 및 소아 특이 병태생리(3순위, 이온통로 관련 편두통 변이형 추정)로 인해 기전상 근거가 약합니다. 3건 모두 평가 단계 S0, 권장 Hold로 판정되었습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
Ohdo 증후군은 유전적·후성유전적 병인을 가진 희귀 발달장애로 Mirtazapine의 신경전달물질 수용체 기전과 알려진 연관성이 없으며, 이를 뒷받침할 임상시험이나 문헌이 전혀 없습니다(근거 수준 L5). 또한 국내 미출시 상태이며 TFDA 수준의 허가 안전성 정보(경고/금기)가 확보되지 않아 안전성 초기 평가(S1)조차 진행할 수 없습니다.

**진행하려면 필요한 것:**
- DrugBank API를 통한 Mirtazapine 상세 작용 기전(MOA) 데이터 확보
- TFDA(또는 해당 규제기관) 공식 허가사항의 경고/금기 정보 확보 (현재 Blocking 등급 data gap)
- Ohdo 증후군 관련 전임상/사례보고 등 실제 연구 근거 축적 여부 모니터링
- 2·3순위 후보(blepharophimosis-Ohdo type, benign paroxysmal torticollis of infancy)에 대해서도 동일하게 근거 축적 여부 추적
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

