---
layout: default
title: Dimenhydrinate
parent: 모델 예측만 (L5)
nav_order: 280
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-31
description: "Dimenhydrinate: 예측 신규 적응증 알레르기성 두드러기 (Allergic Urticaria) (근거 수준 L5). 기존 적응증: 멀미에 의한 어지러움·구토·두통의 예방 및 완화"
monitor_inn: "DIMENHYDRINATE"
predicted_indications: ["allergic urticaria", "cold urticaria"]
---

# Dimenhydrinate
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **2** 건
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

## Dimenhydrinate: 멀미에서 알레르기성 두드러기로
{: .text-alpha }

## 한 문장 요약

Dimenhydrinate는 diphenhydramine과 8-chlorotheophylline의 염으로, 원래 멀미에 의한 어지러움·구토·두통의 예방 및 완화에 사용되었습니다.
TxGNN 모델은 **알레르기성 두드러기(Allergic Urticaria)**에 효과가 있을 수 있다고 예측하지만, 현재 **임상시험은 0건**이며 관련 **문헌은 1편**(개를 대상으로 한 약동학 파일럿 연구)뿐입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 멀미에 의한 어지러움·구토·두통의 예방 및 완화 |
| 예측 신규 적응증 | 알레르기성 두드러기 (Allergic Urticaria) |
| TxGNN 예측 점수 | 0.9974 |
| 근거 수준 | L5 (전임상·기전 수준) |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 dimenhydrinate는 diphenhydramine과 8-chlorotheophylline의 염이며, 이 중 diphenhydramine은 1세대 H1 수용체 길항제입니다. 멀미 증상 완화에 쓰이는 약물이며, H1 차단은 두드러기의 가려움과 팽진 같은 히스타민 매개 증상을 줄일 수 있는 기전입니다.

다만 이 연관성은 간접적입니다. 유효 성분(diphenhydramine)의 약리에 근거한 추론이며, dimenhydrinate 자체의 두드러기 임상 자료는 없습니다. 0.9974이라는 높은 TxGNN 점수는 컴퓨터 예측일 뿐 임상 근거가 아닙니다.

TxGNN은 두 번째 예측으로 **한랭 두드러기(Cold Urticaria)**(점수 0.9924)도 제시했습니다. 이 역시 히스타민 매개 질환이라 H1 길항이 기전상 가능하지만, 관련 임상시험과 문헌이 없습니다. 이 질환의 표준 치료는 2세대 항히스타민제이므로, 진정 및 항콜린 작용이 있는 1세대 약물을 쓸 근거는 비교 자료 없이는 부족합니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [30779257](https://pubmed.ncbi.nlm.nih.gov/30779257/) | 2019 | 약동학 연구 (개 대상 파일럿) | Veterinary Dermatology | 건강한 개에서 diphenhydramine 경구·정맥 투여와 dimenhydrinate 경구 투여 후 약동학, 히스타민 유발 팽진 형성에 대한 약력학 효과를 평가. dimenhydrinate가 diphenhydramine의 경구 흡수를 더 좋게 한다는 보고가 있음 |

임상시험은 현재 관련 등록이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201303989 | 디카엠정 | 필름코팅정 | 멀미에 의한 어지러움·구토·두통의 예방 및 완화 |
| 201908325 | 해피트립액 | 액제 | 멀미에 의한 어지러움, 구토, 두통의 예방 및 완화 |
| 202008047 | 오네론액 | 내용액제 | 멀미에 의한 어지러움, 구토, 두통의 예방 및 완화 |
| 199300981 | 이지롱내복액 | 액제 | 멀미에 의한 어지러움·구토·두통 등의 예방 및 완화 |
| 201706970 | 마레오키즈시럽 | 시럽제 | 멀미에 의한 어지러움·구토·두통의 예방 및 완화 |

위 표는 전체 20건 중 5건만 나열한 것이며, 모두 단일제로 유효 상태입니다.

## 안전성 고려사항

- **약물 상호작용**: 데이터에 67건이 확인되었으며, 주요 항목은 다음과 같습니다.
  - **Major**: Potassium citrate, Potassium chloride
  - **Moderate**: 항콜린제 계열(Atropine, Scopolamine, Hyoscyamine, Dicyclomine, Glycopyrronium, Trospium 등), Morphine, Opium, Loperamide, Metoclopramide, Nabilone, Eluxadoline, Prucalopride
- **지식 그래프상 금기 관련 질환** (허가사항이 아닌 예측 모델의 지식 그래프 기반): 고혈압, 간질환, 담낭질환, 혈소판감소증, 소화성 궤양, 당뇨병, 양성 전립선 비대증, 통풍, 혈액응고 질환, 관상동맥 질환, 심근경색, 폐쇄각 녹내장, 유문 협착, 갑상선기능항진증, 방광경부 폐색 등

허가사항의 경고 및 금기 정보는 이번 데이터에 포함되지 않았으므로 허가사항을 직접 확인해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
알레르기성 두드러기에 대한 지지 근거는 TxGNN 예측과 diphenhydramine의 H1 차단이라는 간접적 기전뿐이며, 임상시험은 없고 문헌도 동물 약동학 파일럿 1편에 그칩니다. 두드러기에는 2세대 항히스타민제가 표준이라 1세대 복합 성분을 쓸 이점도 불분명합니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기) 확보 및 분석: 안전성 선별 단계로 넘어가기 위한 필수 조건
- 상세한 작용 기전(MOA) 데이터 확보
- 두드러기 환자 대상 dimenhydrinate 또는 diphenhydramine의 임상 문헌 검토, 2세대 항히스타민제와의 비교 자료
- 진정·항콜린 부작용과 상호작용(특히 칼륨 제제)을 고려한 위험·이득 평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

