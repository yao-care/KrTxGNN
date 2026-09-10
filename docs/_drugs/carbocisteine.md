---
layout: default
title: Carbocisteine
parent: 僅模型預測 (L5)
nav_order: 175
evidence_level: L5
indication_count: 1
---

# Carbocisteine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Carbocisteine: 호흡기 질환(거담)에서 통풍으로

## 한 문장 요약

> Carbocisteine은 점액용해제(mucolytic)로 호흡기 점액 당단백질의 이황화 결합을 절단해 가래 점도를 낮추는 약물로 알려져 있으나, 이번 Evidence Pack에는 공식 작용기전(MOA)과 기존 적응증 자료가 확보되지 않았습니다.
> TxGNN 모델은 **통풍(Gout)**에 효과가 있을 수 있다고 예측(점수 99.67%)했지만, 이를 뒷받침하는 **임상시험 0건, 문헌 0건**으로 순수 모델 예측 단계에 머물러 있습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 자료 없음 (한국 허가 정보·원 적응증 미확보; 다만 일반적으로 거담제로 분류) |
| 예측 신규 적응증 | 통풍 (Gout) |
| TxGNN 예측 점수 | 99.67% (rank 6274) |
| 근거 수준 | L5 (모델 예측만 존재, 실제 연구 없음) |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용기전(MOA) 데이터가 없습니다(Data Gap). Evidence Pack에 포함된 예측 근거 설명(repurposing rationale)에 따르면, Carbocisteine은 호흡기 점액 당단백질의 이황화 결합을 절단하여 가래 점도를 낮추는 점액용해제이며, 임상적으로 만성기관지염·COPD 등 가래 과다 상황에 사용되는 약물로 기재되어 있습니다.

같은 근거 설명은 이 기전과 통풍의 병리(요산 대사 이상으로 인한 고요산혈증, 관절 내 요산염 결정 침착에 따른 염증 반응) 사이에 **알려진 생리학적 접점이 없다**고 명시하고 있습니다. 원 적응증 목록도 비어 있어 약물 기초 정보 자체가 불완전한 상태이며, 현재의 TxGNN 점수(99.67%)는 순수한 네트워크 위상/임베딩 유사도에 기반한 예측일 뿐, 기전적 타당성을 의미하지는 않습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 근거 수준이 L5(모델 예측만 존재)로, 임상시험·문헌·기전 자료가 전무합니다.
- Evidence Pack의 자체 기전 분석에서도 점액용해 작용과 통풍 병리 사이의 생물학적 연관성이 확인되지 않는다고 명시하고 있어, 예측을 뒷받침할 근거가 부족합니다.

**진행하려면 필요한 것:**
- DrugBank API를 통한 정식 작용기전(MOA) 데이터 확보 (DG002, High)
- TFDA(또는 해당 관할 규제기관) 仿單 경고·금기 자료 확보 — 안전성 초평가(S1) 진입 필수 조건 (DG001, Blocking)
- Carbocisteine과 요산 대사/통풍 관련 전임상 또는 기전 연구 확보
- 통풍 적응증에 특이적인 임상시험·문헌 근거 축적 후 재평가
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

