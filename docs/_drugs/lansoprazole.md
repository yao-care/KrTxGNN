---
layout: default
title: Lansoprazole
parent: 모델 예측만 (L5)
nav_order: 459
evidence_level: L5
indication_count: 1
monitor_inn: "LANSOPRAZOLE"
predicted_indications: ["duodenal obstruction"]
last_modified_at: 2026-10-28
description: "Lansoprazole: 예측 신규 적응증 십이지장 폐쇄 (duodenal obstruction) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200401591/EE"
---

# Lansoprazole
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **1** 건
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

## Lansoprazole: 프로톤 펌프 억제제 → 십이지장 폐쇄 (duodenal obstruction)
{: .text-alpha }

## 한 문장 요약

Lansoprazole은 위산 분비를 억제하는 프로톤 펌프 억제제 계열의 약물입니다.
TxGNN 모델은 **십이지장 폐쇄(duodenal obstruction)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 **임상시험은 0건, 문헌도 0편**으로 모델 예측 단계에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200401591/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201208079/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201501764/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201110631/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200402541/EE;  |
| 예측 신규 적응증 | 십이지장 폐쇄 (duodenal obstruction) |
| TxGNN 예측 점수 | 0.9968 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 20건 (일부 기록만 포함되었을 수 있음) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

이 보고서를 위해 정리된 데이터에는 상세한 작용 기전 자료가 없습니다. 일반적으로 lansoprazole은 위산 분비를 줄이는 약물로 알려져 있으며, 이 점이 소화성 궤양 질환 관리와 연결됩니다.

그러나 십이지장 폐쇄는 협착, 윤상 췌장, 악성 종양, 궤양 후 흉터 등 구조적·기계적 원인으로 생기는 경우가 많아 내시경 또는 수술적 치료가 필요합니다. 산 억제가 궤양 같은 기저 원인을 관리하는 데 도움이 될 수는 있어도, 폐쇄 자체를 치료한다고 보기는 어렵습니다. 따라서 명확한 기전적 연결고리는 확인되지 않았습니다.

0.9968이라는 높은 예측 점수는 모델 내부의 예측값일 뿐이며, 십이지장 궤양 관련 적응증과의 근접성을 반영했을 가능성이 있습니다. 실제 임상적 근거를 의미하지는 않습니다.

## 한국 시판 정보

허가증 20건이 모두 유효 단일 성분 기록으로 확인되며, 아래는 그중 주요 5건입니다. 목록은 일부일 수 있습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200401591 | 뉴란소정(수출용) | 장용 코팅정 | 허가 문서 링크만 제공됨 |
| 201208079 | 란가톤캡슐15밀리그램 | 경질캡슐 | 허가 문서 링크만 제공됨 |
| 201501764 | 모노리툼플라스정15밀리그램 | 정제 | 허가 문서 링크만 제공됨 |
| 201110631 | 란프톤캡슐30밀리그램 | 경질캡슐 | 허가 문서 링크만 제공됨 |
| 200402541 | 란소롤정(수출용) | 장용 코팅정 | 허가 문서 링크만 제공됨 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

참고로, 약물 상호작용 조회에서 100건이 확인되었으며 이 중 일부는 다음과 같습니다.
- **주요(Major) 등급**: Acalabrutinib, Atazanavir
- **중등도(Moderate) 등급**: Hydrochlorothiazide, Amphotericin B, Atorvastatin, Aprepitant 등
- **경미(Minor) 등급**: Acetylsalicylic acid, Cyanocobalamin 등

## 결론 및 다음 단계

**결정: Hold**

**사유:**
십이지장 폐쇄에 대한 임상시험과 문헌이 전혀 없고, 질환의 기계적 특성상 산 억제제의 직접적인 기전적 연결고리도 불분명합니다. 모델 예측만 있는 L5 단계입니다.

**진행하려면 필요한 것:**
- 십이지장 폐쇄 자체를 직접 다룬 임상시험 또는 문헌 근거
- 상세한 작용 기전(MOA) 데이터
- 허가사항(경고·금기) 확인 및 안전성 검토
- 한국 시판 현황의 정확한 확인 (허가 취소 여부 등)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

