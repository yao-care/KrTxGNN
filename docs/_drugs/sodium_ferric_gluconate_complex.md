---
layout: default
title: Sodium Ferric Gluconate Complex
parent: 모델 예측만 (L5)
nav_order: 696
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-31
monitor_inn: "SODIUM FERRIC GLUCONATE COMPLEX"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "anaphylaxis", "bronchitis", "food-dependent exercise-induced anaphylaxis", "diabetic cataract"]
description: "Sodium Ferric Gluconate Complex: 예측 신규 적응증 중증 비증식성 당뇨망막병증 (severe nonproliferative diabetic retinopathy) (근거 수준 L5). 기존 적응증: 이 약은 철 결핍성 빈혈에 사용합니다"
---

# Sodium Ferric Gluconate Complex
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **6** 건
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

## Sodium Ferric Gluconate Complex: 중증 비증식성 당뇨망막병증 (severe nonproliferative diabetic retinopathy)
{: .text-alpha }

## 한 문장 요약

Sodium Ferric Gluconate Complex는 철분 보충제로, 원래 철 결핍성 빈혈 치료에 사용되었습니다.
TxGNN 모델은 **중증 비증식성 당뇨망막병증(Severe Nonproliferative Diabetic Retinopathy)**에 효과가 있을 수 있다고 예측하지만, 이를 지지하는 **임상시험과 문헌은 한 건도 없습니다**.
따라서 이 예측은 TxGNN 모델(딥러닝)의 계산 결과에 그치며, 관련 질환 간에 모델이 학습한 유사성을 반영할 뿐 생물학적 근거는 아니므로, 현재로서는 우연한 연관일 가능성이 높습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 이 약은 철 결핍성 빈혈에 사용합니다.; 이 약은 임신·수유기, 병중·병후(병을 앓는 동안이나 회복 후)의 체력 저하 시 비타민 B6의 보급과 구각염(입꼬리염), 구순염(입술염), 구내염(입안염), 설염(혀염), 습진, 피부염의 완화와 철 결핍성 빈혈의 예방 및 치료에 사용합니다.; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200000570/EE |
| 예측 신규 적응증 | 중증 비증식성 당뇨망막병증 (severe nonproliferative diabetic retinopathy) |
| TxGNN 예측 점수 | 0.9976 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 3건 / 전체 3건) |
| 허가증 수 | 3건 (유효 3건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, 이 약은 철분 보충제로서 철 결핍성 빈혈의 치료와 예방에 허가되어 있습니다.

그러나 철분 보충이 당뇨망막병증에서 치료 역할을 한다고 알려진 바는 없습니다. 오히려 과량의 철은 이론적으로 망막에 산화 스트레스를 더할 수 있습니다. 기존 적응증과 예측 적응증 사이에 확립된 기전적 연결고리가 없으므로, 이 점수는 TxGNN 모델(딥러닝)이 관련 질환 간에 학습한 유사성을 반영할 뿐 생물학적 근거는 아니며, 높은 예측 점수에도 불구하고 이 예측은 신뢰하기 어렵습니다.

같은 방식으로 상위 예측인 당뇨망막병증(0.9967)과 당뇨병성 백내장(0.9920)도 동일한 당뇨 합병증 신호를 공유하는 것으로 보이며, 마찬가지로 근거가 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200000569 | 훼리탑캡슐(글루콘산제이철나트륨착염) | 경질 캡슐제 | 철 결핍성 빈혈 |
| 200607969 | 산타몬플러스캡슐 | 경질 캡슐제 | 임신·수유기, 병중·병후(병을 앓는 동안이나 회복 후)의 체력 저하 시 비타민 B6의 보급과 구각염(입꼬리염), 구순염(입술염), 구내염(입안염), 설염(혀염)... |
| 200000570 | 훼리탑액(글루콘산제이철나트륨착염)(수출용) | 액제 | 수출용 제품 |

## 안전성 고려사항

- **약물 상호작용**: 이 약과 관련해 총 5건의 상호작용이 확인되었습니다.
  - **중대(Major)**: Dimercaprol
  - **중등도(Moderate)**: Iron, Ferrous fumarate, Ferrous gluconate, Chloramphenicol

철분 제제 간 중복 투여 시 상호작용에 유의해야 합니다. 그 밖의 경고·금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 점수는 매우 높지만 임상시험과 문헌이 전혀 없고 기전적 연결고리도 확립되어 있지 않아 근거 수준이 L5에 머뭅니다. 철분의 이론적 산화 스트레스 우려까지 있어 현 시점에서 재창출을 진행할 근거가 부족합니다.

**진행하려면 필요한 것:**
- 허가사항(첨부문서)의 경고·금기 정보 확보 (식약처 허가 정보 확인)
- 약물의 작용 기전(MOA) 데이터 확보 (DrugBank 조회)
- 철 대사와 당뇨망막병증 사이의 기전적 연관성을 검증하는 전임상 연구
- 철 과부하에 따른 망막 산화 스트레스 위험 평가

**참고: 기타 예측 적응증**
- **아나필락시스, 식이 의존성 운동 유발 아나필락시스**: 문헌은 이 약의 이상반응(아나필락시스 유사 반응)을 다룬 것으로, 치료 대상이 아닙니다. 이 약으로 아나필락시스를 치료하는 것은 근거가 없으며 원칙적으로 부적절합니다.
- **기관지염**: 등록된 2건의 4상 시험(NCT00224055, NCT00224042)은 만성 신장질환 환자의 철 결핍 치료 시험으로, 기관지염의 효능을 평가하지 않았습니다.
- 위 모든 예측 적응증에 대한 권장 결정은 Hold입니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

