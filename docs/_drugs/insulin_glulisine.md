---
layout: default
title: Insulin Glulisine
parent: 모델 예측만 (L5)
nav_order: 427
evidence_level: L5
indication_count: 9
monitor_inn: "INSULIN GLULISINE"
predicted_indications: ["thiamine-responsive dysfunction syndrome", "opsismodysplasia", "focal stiff limb syndrome", "classic stiff person syndrome", "autoimmune oophoritis", "pancreatic agenesis", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy"]
last_modified_at: 2026-10-31
description: "Insulin Glulisine: 예측 신규 적응증 티아민 반응성 기능장애 증후군 (thiamine-responsive dysfunction syndrome) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200511127/EE"
---

# Insulin Glulisine
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

## Insulin glulisine: 속효성 인슐린 유사체 → 티아민 반응성 기능장애 증후군 (thiamine-responsive dysfunction syndrome)
{: .text-alpha }

## 한 문장 요약

Insulin glulisine은 속효성 인슐린 유사체로, 한국에서 단일 성분 제제로 허가되어 있습니다.
TxGNN 모델은 **티아민 반응성 기능장애 증후군(thiamine-responsive dysfunction syndrome)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200511127/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200511129/EE |
| 예측 신규 적응증 | 티아민 반응성 기능장애 증후군 (thiamine-responsive dysfunction syndrome) |
| TxGNN 예측 점수 | 0.9947 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Insulin glulisine은 인슐린 계열 약물이며, 혈당 조절 효능이 확립되어 있습니다.

이 증후군은 티아민 수송체 결함으로 생기는 티아민 반응성 거대적아구성 빈혈과 관련이 있으며, 흔히 당뇨병이 동반됩니다. 이 동반 당뇨병 부분에는 이론적으로 인슐린이 반응할 수 있습니다. 다만 이 연결은 컴퓨터 모델의 예측일 뿐이며, 당뇨병 표현형을 반영한 결과일 가능성이 있습니다. 질환 자체를 치료하는 것이 아니라 당뇨 증상에 대한 대증 치료에 그칠 것입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200511127 | 애피드라주바이알(인슐린글루리신,유전자재조합) | 무색 또는 거의 무색의 맑은 용액이 들어있는 바이알 | 허가 적응증 텍스트 미기재 |
| 200511129 | 애피드라주솔로스타(인슐린글루리신,유전자재조합) | 펜 모양의 프리필드 주사제 | 허가 적응증 텍스트 미기재 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건의 상호작용이 확인되었으며, 대부분 중등도입니다. 주요 항목은 다음과 같습니다.
  - 중등도: Phenylephrine, Acebutolol, Acetazolamide, Formoterol, Pseudoephedrine, Doxycycline, Epinephrine, Ethinylestradiol, Hydrocortisone, Albiglutide, Salbutamol, Ethanol, Hydrochlorothiazide, Alogliptin, Metformin, Pioglitazone, Estradiol, Alpelisib
  - 경미: Hydrocortisone(외용), Alclometasone(외용)

그 밖의 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
이 예측을 뒷받침하는 임상시험과 문헌이 없고 모델 예측만 있어 근거 수준은 L5입니다. 예측이 당뇨병 동반 표현형을 반영한 것일 가능성이 있어, 질환 자체에 대한 치료 효과로 보기 어렵습니다.

**진행하려면 필요한 것:**
- 이 증후군에서 인슐린 사용을 직접 다룬 임상시험 또는 증례 문헌
- 상세한 약물 작용 기전(MOA) 데이터
- 허가 적응증, 경고 및 금기를 포함한 허가사항 전문 확인
- 당뇨 동반 증상 치료와 질환 수정 효과의 구분 계획
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

