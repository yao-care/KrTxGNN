---
layout: default
title: Pantoprazole
parent: 모델 예측만 (L5)
nav_order: 578
evidence_level: L5
indication_count: 1
monitor_inn: "pantoprazole"
predicted_indications: ["duodenal obstruction"]
last_modified_at: 2026-10-27
description: "Pantoprazole: 예측 신규 적응증 십이지장 폐색 (duodenal obstruction) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201208632/EE"
---

# Pantoprazole
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

## Pantoprazole: 양성자 펌프 억제제 → 십이지장 폐색 (duodenal obstruction)
{: .text-alpha }

## 한 문장 요약

Pantoprazole은 위산 분비를 억제하는 양성자 펌프 억제제 계열의 약물입니다.
TxGNN 모델은 **십이지장 폐색(duodenal obstruction)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 연구한 임상시험이나 문헌은 없어 근거 수준은 **L5**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201208632/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201205628/EE |
| 예측 신규 적응증 | 십이지장 폐색 (duodenal obstruction) |
| TxGNN 예측 점수 | 0.9921 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 2건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 pantoprazole은 위산 분비를 줄이는 약물로 알려져 있으나, 이번 자료에서는 이를 뒷받침하는 기전 정보가 확인되지 않았습니다.

십이지장 폐색은 협착, 종괴, 외부 압박 등 기계적 원인이 대부분입니다. 위산 억제는 동반된 궤양성 질환이나 증상을 완화할 수는 있어도 폐색 자체를 치료하기는 어렵습니다. 따라서 명확한 기전적 연결고리는 확인되지 않습니다. 높은 예측 점수는 치료적 근거보다는 십이지장 궤양 등 인접 질환과의 연관성을 반영한 것으로 보입니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [35305006](https://pubmed.ncbi.nlm.nih.gov/35305006/) | 2022 | 증례 보고 | Acta Gastro-Enterologica Belgica | 근위부 소장 폐색의 예상치 못한 원인을 다룬 증례. 정맥 pantoprazole 투여에도 증상이 지속되었으며, pantoprazole의 효능을 보여주는 근거는 아님 |

관련 임상시험 등록은 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201208632 | 레토프라정10밀리그램(에스-판토프라졸나트륨삼수화물) | 분홍색 장용성 필름코팅 타원형 정제 | 허가 적응증 텍스트가 기록되어 있지 않음 |
| 201205628 | 레토프라정20밀리그램(에스-판토프라졸나트륨 삼수화물) | 노란색 장용성 필름코팅 타원형 정제 | 허가 적응증 텍스트가 기록되어 있지 않음 |

## 안전성 고려사항

- **약물 상호작용**: 총 597건의 상호작용이 조회되었습니다. 주요(Major) 등급 예시는 다음과 같습니다.
  - Acalabrutinib
  - Atazanavir

  그 외 중등도(Moderate) 등급으로 hydrochlorothiazide, atorvastatin, fenofibrate, amphotericin B, amikacin, bosutinib, bumetanide 등이 있으며, cyanocobalamin, acetylsalicylic acid 등은 경미(Minor) 등급입니다.

허가사항의 경고 및 금기 정보는 허가 문서를 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
십이지장 폐색에 대해 pantoprazole의 효능을 직접 연구한 임상시험이나 문헌이 없고, 기계적 폐색에 산 억제제가 작용할 기전적 근거도 불분명합니다. 높은 예측 점수만으로 진행하기에는 근거가 부족합니다.

**진행하려면 필요한 것:**
- 약물 작용 기전(MOA) 데이터 확보
- 허가사항(경고, 금기, 적응증)의 확인
- 십이지장 폐색 또는 관련 증상에서 pantoprazole의 효과를 직접 평가한 연구
- 병용 약물(특히 Major 등급 상호작용)에 대한 안전성 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

