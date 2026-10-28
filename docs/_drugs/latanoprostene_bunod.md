---
layout: default
title: Latanoprostene Bunod
parent: 모델 예측만 (L5)
nav_order: 463
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Latanoprostene Bunod: 예측 신규 적응증 내장 칼시필락시스 (Visceral calciphylaxis) (근거 수준 L5). 기존 적응증: 개방각 녹내장 및 고안압증 (허가증에는 문서 링크만 기재되어 있어, 약물 정보에 근거해 요약함)"
monitor_inn: "LATANOPROSTENE BUNOD"
predicted_indications: ["visceral calciphylaxis", "venous thoracic outlet syndrome", "arterial thoracic outlet syndrome", "neurogenic thoracic outlet syndrome", "vascular disease", "idiopathic spontaneous coronary artery dissection", "angiodysplasia of stomach", "lymphangiectasis", "hemangioendothelioma"]
---

# Latanoprostene Bunod
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

## Latanoprostene Bunod: 녹내장·고안압증에서 내장 칼시필락시스로
{: .text-alpha }

## 한 문장 요약

Latanoprostene bunod는 점안제로 사용되는 약물로, 원래 개방각 녹내장 및 고안압증 치료에 사용되었습니다.
TxGNN 모델은 **내장 칼시필락시스(visceral calciphylaxis)**에 효과가 있을 수 있다고 예측하지만, 이 예측을 뒷받침하는 임상시험이나 문헌은 현재 없습니다(근거 수준 L5).
따라서 모델 예측만 존재하는 가설 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 개방각 녹내장 및 고안압증 (허가증에는 문서 링크만 기재되어 있어, 약물 정보에 근거해 요약함) |
| 예측 신규 적응증 | 내장 칼시필락시스 (Visceral calciphylaxis) |
| TxGNN 예측 점수 | 0.9976 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 허가 정보에 정리되어 있지 않습니다. 알려진 정보에 따르면, Latanoprostene bunod는 대사되어 latanoprost acid(프로스타글란딘 F2α 유사체)와 산화질소(NO)를 방출합니다. 이를 통해 포도막공막 유출로와 섬유주 유출로를 모두 늘려 안압을 낮춥니다.

신규 적응증과의 유일한 이론적 연결고리는 NO에 의한 혈관 확장입니다. 그러나 칼시필락시스는 전신적·대사성 소혈관 질환이며, 점안 투여는 전신 노출이 매우 적습니다. 따라서 이 연결은 높은 TxGNN 점수에만 의존하며, 기전상 설득력은 제한적입니다.

## 임상시험 근거

현재 내장 칼시필락시스와 관련된 임상시험 등록이 없습니다.

## 문헌 근거

현재 내장 칼시필락시스와 관련된 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202101149 | 비줄타점안액0.024% (라타노프로스틴부노드) | 점안제 (2.5mL, 5mL) | 개방각 녹내장 또는 고안압증 (제조사: 바슈헬스코리아) |

## 안전성 고려사항

- **약물 상호작용**: 약물 간 상호작용으로 보고된 항목은 없습니다. 약리학적 표적은 프로스타노이드 FP 수용체(PTGFR)이며, 이 수용체에 대한 작용제로 작용합니다.

그 외 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
내장 칼시필락시스 예측은 TxGNN 점수에만 근거하며, 임상시험과 문헌이 전혀 없습니다. 또한 점안 투여로는 전신 노출이 최소여서 전신 질환에 대한 기전적 타당성이 낮습니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기)의 확보 및 분석
- 상세한 작용 기전 데이터 (MOA)
- 칼시필락시스에 대한 전임상 또는 기전 연구 근거
- 전신 노출 및 투여 경로 적합성 평가

---

### 참고: 다른 예측 적응증

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 | 비고 |
|------|-----------|-----------|----------|------|
| 6 | 혈관 질환 | 0.9953 | L5 | 관련 시험(NCT03931317, 완료, 70명)은 녹내장 환자의 망막 혈관 밀도를 보는 연구로 간접 근거에 그침 |
| 10 | 혈관내피종 | 0.9947 | L5 | 유일한 문헌(PMID 38113361)은 프로스타글란딘 유사체 사용 중 포도주색 반점 환자의 장액성 망막박리 사례로, 효능이 아닌 안전성 신호임 |
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

