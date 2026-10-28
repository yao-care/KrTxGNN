---
layout: default
title: Esomeprazole
parent: 모델 예측만 (L5)
nav_order: 318
evidence_level: L5
indication_count: 1
monitor_inn: "ESOMEPRAZOLE"
predicted_indications: ["duodenal obstruction"]
last_modified_at: 2026-10-27
description: "Esomeprazole: 예측 신규 적응증 십이지장 폐쇄 (duodenal obstruction) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200410324/EE"
---

# Esomeprazole
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

## Esomeprazole: 양성자 펌프 억제제 → 십이지장 폐쇄 (duodenal obstruction)
{: .text-alpha }

## 한 문장 요약

Esomeprazole은 위산 분비를 억제하는 양성자 펌프 억제제 계열의 약물입니다.
TxGNN 모델은 **십이지장 폐쇄(duodenal obstruction)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 **임상시험은 0건**, **문헌은 0편**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200410324/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201403894/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201403728/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201403085/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201606894/EE;  |
| 예측 신규 적응증 | 십이지장 폐쇄 (duodenal obstruction) |
| TxGNN 예측 점수 | 0.9945 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 8건 (유효 8건, 취소 0건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 esomeprazole은 위산 분비를 줄이는 계열의 약물이며, 산 관련 상부 위장관 질환에서 사용됩니다.

다만 십이지장 폐쇄는 종양, 협착, 윤상 췌장 등 기계적 원인으로 생기는 경우가 많아, 위산 억제만으로 치료되기 어렵습니다. 궤양과 연관된 협착처럼 이차적인 소화성 합병증에서만 보조적 도움이 될 가능성이 있습니다. 따라서 뚜렷한 기전적 연결고리는 확인되지 않으며, 높은 모델 점수는 어디까지나 예측값일 뿐입니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200410324 | 넥시움주(에스오메프라졸나트륨) | 주사용 바이알(다공성 덩어리 또는 분말) | 허가 문서 링크만 제공됨 |
| 201403894 | 나프라졸정 | 필름코팅정(3층) | 허가 문서 링크만 제공됨 |
| 201403728 | 에소록센정(나프록센, 에스오메프라졸) | 필름코팅정(3층) | 허가 문서 링크만 제공됨 |
| 201403085 | 나프메드정500/20밀리그램 | 필름코팅정(3층) | 허가 문서 링크만 제공됨 |
| 201606894 | 오엠피에스주40밀리그램(에스오메프라졸나트륨) | 주사용 바이알(동결건조물) | 허가 문서 링크만 제공됨 |

위 표는 주요 5건만 나열한 것이며, 전체 허가증은 8건입니다.

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 그중 주요(Major) 등급으로는 acalabrutinib, atazanavir 등이 있습니다. 중등도(Moderate) 등급으로는 hydrochlorothiazide, amphotericin B, amikacin, amphetamine, fenofibrate, apalutamide, armodafinil, atorvastatin, bendamustine, bosutinib, bumetanide 등이 있습니다. 경미(Minor) 등급으로는 acetylsalicylic acid, axitinib, bortezomib, brivaracetam, cyanocobalamin 등이 있습니다.

허가사항상의 경고 및 금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
십이지장 폐쇄에 대한 임상시험과 문헌이 전혀 없고, 기전상으로도 연결고리가 불분명하여 근거 수준은 L5(모델 예측만 있음)입니다.

**진행하려면 필요한 것:**
- 십이지장 폐쇄(특히 궤양성 협착 등 산 관련 원인)에 대한 임상 또는 관찰 연구 근거
- 상세한 작용 기전(MOA) 데이터
- 허가사항(경고·금기)의 확인 및 정리
- 적용 가능한 투여 경로(주사/경구)에 대한 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

