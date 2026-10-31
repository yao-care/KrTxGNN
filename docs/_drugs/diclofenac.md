---
layout: default
title: Diclofenac
parent: 모델 예측만 (L5)
nav_order: 276
evidence_level: L5
indication_count: 10
monitor_inn: "Diclofenac"
predicted_indications: ["hypotrichosis simplex of the scalp", "acromesomelic dysplasia, Hunter-Thompson type", "pseudoachondroplasia", "brachyolmia", "brachyolmia-amelogenesis imperfecta syndrome", "congenital hypotrichosis milia", "myosclerosis", "diffuse alopecia areata", "juvenile idiopathic arthritis", "WHIM syndrome"]
last_modified_at: 2026-10-31
description: "Diclofenac: 예측 신규 적응증 두피 단순 저모발증 (근거 수준 L5). 기존 적응증: 치은염, 구내염, 인두염 등 구강인두의 염증, 치과 보존치료 또는 발치 후 염증 완화 (그 밖에 골관절염, 힘줄염…"
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

<div id="pharmacist" markdown="1">

## 약사 평가 보고서

</div>

## Diclofenac: 구강인두 염증·관절 통증에서 두피 단순 저모발증으로
{: .text-alpha }

## 한 문장 요약

Diclofenac은 비스테로이드성 소염진통제(NSAID)로, 한국에서 구강인두 염증, 골관절염, 근육통 등의 통증·염증 완화에 허가되어 있습니다.
TxGNN 모델은 **두피 단순 저모발증(hypotrichosis simplex of the scalp)**에 효과가 있을 수 있다고 예측했습니다. 그러나 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**이어서 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 치은염, 구내염, 인두염 등 구강인두의 염증, 치과 보존치료 또는 발치 후 염증 완화 (그 밖에 골관절염, 힘줄염, 근육통 등) |
| 예측 신규 적응증 | 두피 단순 저모발증 |
| TxGNN 예측 점수 | 0.9969 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 18건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 데이터에는 상세한 작용 기전 정보가 비어 있습니다. 알려진 정보에 따르면 Diclofenac은 COX-1/COX-2를 억제해 프로스타글란딘 매개 염증과 통증을 줄이는 약입니다. 한국 허가 적응증도 이 항염·진통 작용에 기반합니다.

반면 두피 단순 저모증은 염증성 질환이 아니라 유전성 모발 성장 장애입니다(CDSN, APCDD1, RPL21 등의 변이). COX 억제가 이 질환의 원인 경로를 다룬다고 볼 근거는 찾지 못했습니다. 높은 TxGNN 점수는 TxGNN 모델(딥러닝)이 관련 질환 사이에서 학습한 유사성을 반영한 것일 수 있으며, 생물학적 근거는 아닙니다. 기전적·임상적 뒷받침은 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

아래는 확인된 허가 중 주요 5건입니다. 전체 허가증은 최소 20건이며 목록은 일부일 수 있습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202008458 | 조아구강청액 | 구강용 액제 | 치은염, 구내염, 인두염 등 구강인두의 염증, 치과 보존치료 또는 발치 후 염증 완화 |
| 202101212 | 아프모겐큐인후스프레이 | 정량분무용 액제 | 치은염, 구내염, 인두염 등 구강인두의 염증, 치과 보존치료 또는 발치 후 염증 완화 |
| 201802608 | 코디톱쿨플라스타 | 첩부제 | 퇴행성 관절염(골관절염), 어깨관절 주위염, 힘줄 및 힘줄윤활막염, 힘줄주위염, 위팔뼈상과염(테니스엘보 등), 근육통(근, 근막성, 허리통증 등)... |
| 201905649 | 맨담디클로엔플라스타 | 첩부제 | 퇴행성 관절염(골관절염), 어깨관절 주위염, 힘줄 및 힘줄윤활막염, 힘줄주위염, 위팔뼈상과염(테니스엘보 등), 근육통(근, 근막성, 허리통증 등)... |
| 202401785 | 류마스탑파워플라스타 | 첩부제 | 골관절염, 어깨관절 주위염, 힘줄 및 힘줄윤활막염, 힘줄 주위염, 팔꿈치 통증(테니스엘보), 근육통, 외상 후 부기 및 통증 |

## 안전성 고려사항

- **약물 상호작용**: 이번에 조회된 상호작용 100건 중 일부(20건)가 확인되었습니다.
  - 중등도: 코르티코스테로이드(hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide), 아세틸살리실산, mesalazine, balsalazide, metformin 및 설포닐우레아계 당뇨병약(acetohexamide, chlorpropamide, glimepiride, glipizide), aprepitant, exenatide, fenfluramine, dexfenfluramine
  - 경미: famotidine, ranitidine, cimetidine

주요 경고와 금기 정보는 이번 데이터에서 확보되지 않았습니다. 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
두피 단순 저모발증은 유전성 모발 질환으로 COX 억제와의 기전적 연관성이 확인되지 않으며, 지지하는 임상시험과 문헌이 전혀 없는 L5 단계의 모델 예측입니다. 현 시점에서는 개발 근거가 부족합니다.

**진행하려면 필요한 것:**
- 해당 질환과 COX 경로(프로스타글란딘)의 연관성을 보여주는 전임상·기전 연구
- 두피 저모발증에서 Diclofenac의 효과를 직접 평가한 임상 또는 문헌 근거
- 식약처 허가사항의 경고·금기 정보 확보와 상세 작용 기전 데이터 보완
- 참고: 이번 예측 후보 가운데 문헌이 확인된 것은 소아 특발성 관절염(JIA)뿐입니다. 다만 이는 이미 NSAID가 쓰이는 질환이어서 신규 재창출로 보기 어렵습니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

