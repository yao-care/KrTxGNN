---
layout: default
title: Travoprost
parent: 僅模型預測 (L5)
nav_order: 697
evidence_level: L5
indication_count: 10
---

# Travoprost
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

Using no specialized skill here — this is a direct content-generation task per the drug-repurposing report template, not a coding/debugging/brainstorming task.

# Travoprost: 녹내장(안압 하강)에서 내장성 석회화방지증(Visceral Calciphylaxis)으로

## 한 문장 요약

Travoprost는 FP 수용체 작용제로, 임상시험 자료에 근거해 볼 때 녹내장·고안압증 치료용 점안제로 사용되어 온 약물입니다.
TxGNN 모델은 **내장성 석회화방지증(Visceral Calciphylaxis)**에 효과가 있을 수 있다고 예측하지만,
현재 이를 뒷받침하는 **임상시험 0건**, **문헌 0편**으로 순수 알고리즘 예측에 불과합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 녹내장 / 고안압증 (안압 하강, FP 수용체 작용제 점안제) — 공식 허가 텍스트 없음, 임상시험 자료 기반 추정 |
| 예측 신규 적응증 | 내장성 석회화방지증 (Visceral Calciphylaxis) |
| TxGNN 예측 점수 | 99.9998% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 확보되지 않았습니다([Data Gap]). 다만 근거 자료 내 서술에 따르면 Travoprost는 FP 수용체 작용제(prostaglandin F2α 유사체)로, 안압 하강을 목적으로 한 점안제 형태로 연구되어 왔습니다.

내장성 석회화방지증(visceral calciphylaxis)은 혈관 석회화 및 조직 허혈을 특징으로 하는 질환으로, FP 수용체 작용과의 약리학적 연결고리가 명확하지 않습니다. 근거 팩 자체도 "FP 受體促效劑用於鈣化防禦症"에 대한 뚜렷한 기전 근거가 없다고 명시하고 있습니다.

즉 이 예측은 TxGNN의 그래프 기반 유사도 점수에만 의존하며, 기존 적응증(안과 질환)과 신규 예측 적응증(전신 혈관 석회화 질환) 사이에 조직학적·기전적 연관성을 뒷받침할 근거가 현재는 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> 참고: 이 후보 약물은 TFDA/식약처 수준의 경고·금기 정보(DG001, Blocking)가 아직 확보되지 않아 안전성 초기 평가(S1) 단계에 진입할 수 없는 상태입니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 내장성 석회화방지증에 대한 예측은 TxGNN 알고리즘 점수 외에 임상시험·문헌 근거가 전무한 L5 수준이며, 기전적 타당성도 뒷받침되지 않습니다.
- 안전성 초기 평가(S1)에 필요한 허가사항 경고/금기 정보가 확보되지 않아(DG001, Blocking) 현 단계에서 진행이 불가능합니다.

**진행하려면 필요한 것:**
- DrugBank를 통한 상세 작용 기전(MOA) 확보 (DG002)
- 식약처/TFDA 원문 허가사항(경고, 금기) 확보 — 안전성 초기 평가(S1) 진입 필수 조건 (DG001)
- 내장성 석회화방지증에 대한 전임상/기전 연구 존재 여부 추가 조사
- 참고: 동일 예측 세트 중 순위 5위 "vascular disease"는 관련 임상시험 15건·문헌 20편이 존재하나, 모두 녹내장/안압 관련 연구로 적응증 불일치(off-target)로 평가되어 있어 함께 재검토할 가치가 있습니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

