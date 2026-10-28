---
layout: default
title: Adalimumab
parent: 모델 예측만 (L5)
nav_order: 24
evidence_level: L5
indication_count: 3
monitor_inn: "ADALIMUMAB"
predicted_indications: ["hypermobility of coccyx", "Kummell disease", "vertebral disease"]
last_modified_at: 2026-10-28
description: "Adalimumab: 예측 신규 적응증 꼬리뼈 과가동성 (hypermobility of coccyx) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202402438/EE"
---

# Adalimumab
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **3** 건
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

## Adalimumab: TNF-α 억제 항체 → 꼬리뼈 과가동성 (hypermobility of coccyx)
{: .text-alpha }

## 한 문장 요약

Adalimumab은 TNF-α를 억제하는 항체 의약품으로, 한국에서 단일 성분 제품으로 허가되어 있습니다.
TxGNN 모델은 **꼬리뼈 과가동성 (hypermobility of coccyx)**에 효과가 있을 수 있다고 예측합니다.
그러나 이 예측을 직접 뒷받침하는 **임상시험은 0건**, **문헌도 0편**입니다. 따라서 현재는 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202402438/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202106947/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202303340/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202303341/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202600554/EE;  |
| 예측 신규 적응증 | 꼬리뼈 과가동성 (hypermobility of coccyx) |
| TxGNN 예측 점수 | 0.9977 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 19건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 작용 기전(MOA) 상세 데이터는 확보되지 않았습니다. 다만 adalimumab은 TNF-α 차단 계열 생물학적 제제로 알려져 있으며, 효과는 TNF가 주도하는 염증 질환에서 기대됩니다.

꼬리뼈 과가동성은 염증보다는 기계적·구조적 문제에 가까운 상태입니다. TNF가 병태의 핵심이라는 근거는 분명하지 않습니다. 높은 TxGNN 점수는 계산상의 예측일 뿐이며, 이를 뒷받침하는 임상시험이나 문헌도 없습니다. 기존 적응증과의 유사성 분석 역시 아직 진행되지 않았습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

19건이 모두 단일 성분 제제이며 유효 상태입니다. 아래는 주요 5건입니다. 허가 적응증 텍스트는 식약처 허가 문서 링크로만 제공됩니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202402438 | 심란디펜주40mg/0.4mL | 펜 내장 프리필드시린지 주사제 | [허가 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202402438/EE) 참조 |
| 202106947 | 유플라이마프리필드시린지주40mg/0.4mL | 프리필드시린지 주사제 | [허가 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202106947/EE) 참조 |
| 202303340 | 젤렌카오토인젝터주40mg/0.4mL | 오토인젝터 주사제 | [허가 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202303340/EE) 참조 |
| 201704557 | 휴미라프리필드시린지주40mg/0.4mL | 프리필드시린지 주사제 | [허가 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201704557/EE) 참조 |
| 202300028 | 아달로체펜주40mg/0.4mL | 펜 내장 프리필드시린지 주사제 | [허가 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202300028/EE) 참조 |

## 안전성 고려사항

- **약물 상호작용**: 조회된 상호작용은 총 100건입니다. 아래는 그중 일부입니다.
  - **주요(Major)**: 코르티코스테로이드 계열(betamethasone, budesonide, dexamethasone, hydrocortisone, prednisolone, prednisone, triamcinolone), deferiprone, ibritumomab tiuxetan, iobenguane (I-131), tositumomab 및 tositumomab (I-131)
  - **중등도(Moderate)**: metronidazole, tinidazole, rosuvastatin, simvastatin
  - **경미(Minor)**: 아연 제제(zinc acetate, zinc gluconate, zinc sulfate)

경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
꼬리뼈 과가동성에 대한 점수는 모델 예측일 뿐입니다. 이 질환은 TNF 주도 염증과의 기전적 연결이 불분명하고, 직접 뒷받침하는 임상시험과 문헌도 없습니다. 근거 수준은 L5입니다.

**진행하려면 필요한 것:**
- 꼬리뼈 과가동성과 TNF 경로의 연관성을 보여주는 기전 또는 전임상 근거
- 해당 질환을 직접 다루는 임상시험 또는 문헌
- 작용 기전(MOA) 상세 데이터 확보
- 허가사항의 경고·금기 정보 확보 및 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

