---
layout: default
title: Guselkumab
parent: 모델 예측만 (L5)
nav_order: 397
evidence_level: L5
indication_count: 8
monitor_inn: "Guselkumab"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "renal osteodystrophy", "congenital hypotrichosis with juvenile macular dystrophy", "primary release disorder of platelets", "Glanzmann thrombasthenia", "non-renal secondary hyperparathyroidism"]
last_modified_at: 2026-10-28
description: "Guselkumab: 예측 신규 적응증 약물 유발 골다공증 (drug-induced osteoporosis) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202104066/EE"
---

# Guselkumab
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **8** 건
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

## Guselkumab: IL-23 억제 단클론항체 → 약물 유발 골다공증 (drug-induced osteoporosis)
{: .text-alpha }

## 한 문장 요약

Guselkumab은 IL-23를 표적으로 하는 유전자재조합 단클론항체 주사제입니다.
TxGNN 모델은 **약물 유발 골다공증(drug-induced osteoporosis)**에 효과가 있을 수 있다고 예측하지만, 현재 이 방향을 직접 지지하는 **임상시험은 0건**, **문헌도 0편**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202104066/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201801604/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202502173/EE |
| 예측 신규 적응증 | 약물 유발 골다공증 (drug-induced osteoporosis) |
| TxGNN 예측 점수 | 0.9984 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 3건 (단일제 3건, 모두 유효) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. Guselkumab은 IL-23 신호 경로를 억제하는 단클론항체로 알려져 있으며, IL-23/IL-17 축은 뼈 재형성과 이론적으로 연관될 수 있습니다.

그러나 글루코코르티코이드 등 약물로 인한 골소실에 guselkumab이 효과가 있다는 직접 근거는 제공된 데이터에 없습니다. 이 예측은 현 단계에서 모델 점수에만 의존합니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202104066 | 트렘피어원프레스오토인젝터주(구셀쿠맙,유전자재조합) | 오토인젝터 장착 프리필드시린지 주사제 | 적응증 텍스트 미기재 (허가 문서 링크만 제공) |
| 201801604 | 트렘피어프리필드시린지주(구셀쿠맙,유전자재조합) | 프리필드시린지 주사제 | 적응증 텍스트 미기재 (허가 문서 링크만 제공) |
| 202502173 | 트렘피어정맥주사(구셀쿠맙, 유전자재조합) | 유리바이알 주사제 | 적응증 텍스트 미기재 (허가 문서 링크만 제공) |

## 안전성 고려사항

- **약물 상호작용**: 조회된 상호작용은 총 100건이며, 그중 일부는 다음과 같습니다.
  - **Major**: Adalimumab
  - **Moderate**: Simvastatin, Apixaban, Warfarin, Rivaroxaban, Dicoumarol, Lidocaine, Hydrocodone, Theophylline, Roflumilast, Aminophylline, Oxtriphylline, Tacrolimus, Fentanyl, Nifedipine, 파상풍 톡소이드 항원
  - **Minor**: 아연 제제(Zinc sulfate, acetate, gluconate, chloride)

주요 경고와 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 약물 유발 골다공증에 대한 임상시험과 문헌이 모두 없어 근거 수준이 L5(모델 예측만 존재)입니다.
- IL-23 억제와 약물 유발 골소실 사이의 기전적 연결도 입증되지 않았습니다.

**진행하려면 필요한 것:**
- 약물 유발 골다공증과 IL-23/IL-17 축의 관련성을 다루는 전임상 및 기전 연구
- 허가사항(경고, 금기)의 확인과 안전성 검토
- 상세한 작용 기전(MOA) 데이터 확보
- 한국 시판 상태(허가 유지 여부) 확인
- 골 관련 평가변수를 포함한 임상 연구 설계 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

