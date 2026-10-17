---
layout: default
title: Human C1-Esterase Inhibitor
parent: 모델 예측만 (L5)
nav_order: 400
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Human C1-Esterase Inhibitor: 예측 신규 적응증 중증 비증식성 당뇨망막병증 (Severe Nonproliferative Diabetic Retinopathy) (근거 수준 L5). 기존 적응증: 허가 적응증 원문은 MFDS 허가정보 링크로만 제공되어 구체적인 질환명을 확인할 수 없음"
monitor_inn: "HUMAN C1-ESTERASE INHIBITOR"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "primary release disorder of platelets", "diabetic retinopathy", "pseudo-von Willebrand disease"]
---

# Human C1-Esterase Inhibitor
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **4** 건
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

# 사람 C1-에스테라제 억제제(Human C1-Esterase Inhibitor): 유전성 혈관부종 계열 약물에서 중증 비증식성 당뇨망막병증으로

## 한 문장 요약

사람 C1-에스테라제 억제제는 국내에서 "베리너트주500아이유"로 허가되어 시판 중인 혈장 유래 단백질 주사제입니다.
TxGNN 모델은 **중증 비증식성 당뇨망막병증(Severe Nonproliferative Diabetic Retinopathy)**에 효과가 있을 수 있다고 예측하지만, 현재 이 방향을 지지하는 **임상시험과 문헌은 한 건도 확인되지 않았습니다**.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 원문은 MFDS 허가정보 링크로만 제공되어 구체적인 질환명을 확인할 수 없음 |
| 예측 신규 적응증 | 중증 비증식성 당뇨망막병증 (Severe Nonproliferative Diabetic Retinopathy) |
| TxGNN 예측 점수 | 99.61% |
| 근거 수준 | L5 (모델 예측만 있음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 C1-에스테라제 억제제는 칼리크레인-키닌계와 보체·접촉 활성화 경로를 조절하는 혈장 단백질로 알려져 있으나, 이번 자료로는 이를 확인할 수 없습니다.

가설적 연결고리는 다음과 같습니다. 혈장 칼리크레인에 의한 혈관 투과성 증가와 염증이 당뇨망막병증의 망막 혈관 누출에 관여한다고 알려져 있습니다. C1-에스테라제 억제제가 이 경로를 억제한다면 이론상 적용 가능성이 있습니다.

다만 이는 검증되지 않은 가설입니다. 전신 투여된 혈장 유래 단백질이 혈액-망막 장벽을 통과해 망막에 도달할 수 있는지도 불분명합니다. 이 예측은 그래프 기반 모델 결과일 뿐입니다.

같이 예측된 다른 질환의 성격은 다음과 같습니다.
- **당뇨망막병증(상위 질환)**: 위와 동일한 가설이 적용되며 독립적인 근거가 아닙니다. (점수 99.25%)
- **혈소판 분비 장애 및 슈도 폰빌레브란트병**: 기전적으로 뚜렷한 연결고리가 없어 매우 추측적입니다. (각각 99.31%, 99.09%)

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201109899 | 베리너트주500아이유 (사람 C1-에스테라제 억제제) | 동결건조 분말 주사제 (주사용수에 용해 시 무색투명한 액, 씨에스엘코리아) | 허가 적응증 원문은 MFDS 허가정보를 참조 |

## 안전성 고려사항

- **약물 상호작용**: 총 41건이 확인되었으며, 이 중 주요 항목은 다음과 같습니다.
  - **Major**: Carfilzomib
  - **Moderate**: 안드로겐·동화 스테로이드(Oxandrolone, Oxymetholone, Stanozolol, Testosterone, Danazol), 에스트로겐 및 호르몬제(Ethinylestradiol, Estradiol, Conjugated estrogens, Diethylstilbestrol, Drospirenone), 혈전용해제(Alteplase, Anistreplase), 조혈인자(Darbepoetin alfa, Erythropoietin) 등

경고 및 금기 등 그 밖의 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
높은 TxGNN 점수(99.61%)에도 불구하고, 뒷받침하는 임상시험과 문헌이 전혀 없는 모델 예측 단계(L5)입니다. 작용 기전 데이터도 없어 기전적 타당성을 확인할 수 없고, 혈액-망막 장벽 통과 문제 등 약동학적 의문도 남아 있습니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 데이터 확보
- 허가사항(경고, 금기, 허가 적응증) 원문 확보 및 분석
- 칼리크레인-키닌계와 당뇨망막병증 관련 전임상·문헌 근거 조사
- 망막 전달 가능성(전신 투여 시 혈액-망막 장벽 투과, 대안 투여경로) 평가
- 관련 임상시험 및 문헌 재검색
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

