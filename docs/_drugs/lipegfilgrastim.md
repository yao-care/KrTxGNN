---
layout: default
title: Lipegfilgrastim
parent: 僅模型預測 (L5)
nav_order: 444
evidence_level: L5
indication_count: 5
---

# Lipegfilgrastim
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Lipegfilgrastim: 기존 적응증 정보 없음에서 원발성 혈소판 방출 장애로

## 한 문장 요약

Lipegfilgrastim(DrugBank ID: DB13200)은 한국 내 허가 이력이 없고 기존 적응증 데이터도 등록되어 있지 않습니다. TxGNN 모델은 **원발성 혈소판 방출 장애(Primary Release Disorder of Platelets)**에 효과가 있을 수 있다고 예측하지만(예측 점수 99.93%), 이를 뒷받침하는 임상시험이나 문헌은 **현재 0건**이며, 모델 자체 기전 분석에서도 연관성이 명확히 검증되지 않았다고 명시하고 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (DrugBank/한국 허가 자료 모두 미기재) |
| 예측 신규 적응증 | 원발성 혈소판 방출 장애 (Primary Release Disorder of Platelets) |
| TxGNN 예측 점수 | 99.93% |
| 근거 수준 | L5 (모델 예측만 있음, 실제 연구 없음) |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

공식 작용기전(MOA) 데이터는 현재 등록되어 있지 않습니다(Data Gap, High severity). 다만 Evidence Pack에 포함된 기전 분석에 따르면, Lipegfilgrastim은 페길화(PEGylated)된 G-CSF 유사체로, 골수 내 과립구 전구세포의 증식·분화를 자극하는 것이 알려진 약리 기전입니다. 표적 수용체(G-CSF 수용체)는 주로 호중구 계열 세포에 발현합니다.

그러나 예측된 신규 적응증인 원발성 혈소판 방출 장애는 혈소판 과립 방출 경로(dense granule/alpha granule release)와 관련된 질환으로, G-CSF/과립구 생성 경로와의 직접적인 기전 연관성은 보고된 바 없습니다. Evidence Pack의 기전 분석 자체도 "원래 적응증·MOA 자료가 없어 이 연관성이 이미 알려진 약리학적 연장인지 교차 검증이 불가능하다"고 명시하고 있어, 현 시점에서 기전적 타당성은 낮게 평가됩니다.

참고로 함께 예측된 나머지 후보 적응증(중증 비증식성 당뇨망막병증, 가성 폰빌레브란트병, Glanzmann 혈소판무력증, 당뇨망막병증) 역시 모두 지식그래프 공동 출현에 따른 잡음(noise) 가능성이 높다고 분석되어 있으며, 뚜렷한 기전적 근거는 확인되지 않았습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

한국 내 허가된 제품이 없습니다 (미출시, 허가증 0건).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
기존 적응증·MOA·TFDA 경고/금기 데이터가 모두 비어 있어(특히 MOA는 High, 라벨 경고는 Blocking 등급 데이터 갭) 안전성 초기 평가(S1) 단계에도 진입할 수 없는 상태입니다. 예측된 신규 적응증을 뒷받침하는 임상시험·문헌 근거도 전무하며(L5), 기전 분석 자체도 연관성을 약하게 평가하고 있어 현 시점에서 진행 근거가 부족합니다.

**진행하려면 필요한 것:**
- TFDA(또는 해당 원산지 규제기관)의 공식 라벨 경고·금기사항 확보 (DG001, Blocking)
- DrugBank API를 통한 공식 작용기전(MOA) 데이터 확보 (DG002, High)
- 원발성 혈소판 방출 장애 관련 전임상/기전 연구 존재 여부 재조사
- 향후 신규 임상시험·문헌 발표 시 재평가
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

