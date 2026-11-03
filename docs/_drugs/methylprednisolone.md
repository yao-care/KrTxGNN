---
layout: default
title: Methylprednisolone
parent: 모델 예측만 (L5)
nav_order: 511
evidence_level: L5
indication_count: 8
monitor_inn: "Methylprednisolone"
predicted_indications: ["alopecia mucinosa", "telogen effluvium", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions", "alopecia universalis onychodystrophy vitiligo"]
last_modified_at: 2026-11-03
description: "Methylprednisolone: 예측 신규 적응증 점액성 탈모증 (alopecia mucinosa) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201804425/EE"
---

# Methylprednisolone
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

## Methylprednisolone: 점액성 탈모증 (alopecia mucinosa)
{: .text-alpha }

## 한 문장 요약

Methylprednisolone은 글루코코르티코이드 계열의 항염증 약물로, 한국에서 단일 성분 정제로 시판되고 있습니다. TxGNN 모델은 **점액성 탈모증(alopecia mucinosa)**에 효과가 있을 수 있다고 예측합니다(예측 점수 0.9999). 다만 이 질환을 직접 다룬 임상시험과 문헌은 **0건**이어서, 현재는 모델 예측 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201804425/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200403914/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201207586/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201601595/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200300111/EE;  |
| 예측 신규 적응증 | 점액성 탈모증 (alopecia mucinosa) |
| TxGNN 예측 점수 | 0.9999 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

허가증 수는 현재 확인된 목록 기준이며, 전체 목록의 일부일 수 있습니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 다만 Methylprednisolone은 글루코코르티코이드 계열로 알려져 있어, 염증 반응을 억제하는 작용이 기대됩니다.

점액성 탈모증(모낭 점액증)은 모낭에 점액(mucin)이 침착되고 림프구 침윤이 동반되는 질환입니다. 항염증 작용이 있는 글루코코르티코이드가 이 염증성 침윤에 작용할 가능성은 이론적으로 있습니다.

그러나 이는 예측 수준의 추정입니다. 이 질환에 대한 임상시험이나 문헌이 확인되지 않았습니다. 높은 예측 점수는 다른 탈모 질환과의 유사성에서 비롯되었을 가능성이 큽니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

확인된 허가증은 모두 단일 성분 제제이며 유효 상태입니다. 아래는 그중 주요 5건입니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201804425 | 프레드윈정 | 정제 | 허가 문서 참조 |
| 200403914 | 프레솔론정16밀리그람 (수출용) | 정제 | 허가 문서 참조 |
| 201207586 | 코니솔론정4밀리그램 | 정제 | 허가 문서 참조 |
| 201601595 | 메솔롬정 | 정제 | 허가 문서 참조 |
| 200300111 | 메솔론정 | 정제 | 허가 문서 참조 |

## 안전성 고려사항

- **약물 상호작용**: 약물 상호작용 조회 결과 100건이 확인되었습니다. 주요 항목은 다음과 같습니다.
  - **Major 등급**: Bupropion, Clarithromycin
  - **Moderate 등급**: 혈당강하제(Acarbose, Metformin, Pioglitazone, Alogliptin, Saxagliptin, Canagliflozin, Dapagliflozin, Empagliflozin, Chlorpropamide, Albiglutide, Dulaglutide), Amphotericin B, Aprepitant, Acetylsalicylic acid 등
  - **Minor 등급**: Zinc sulfate

그 외 경고·금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 점액성 탈모증에 대한 임상시험과 문헌이 없고, 근거는 모델 예측뿐이어서 근거 수준이 L5입니다.
- 높은 예측 점수만으로는 임상적 유용성을 판단하기 어렵습니다.

**진행하려면 필요한 것:**
- 점액성 탈모증에서 글루코코르티코이드 사용을 직접 다룬 증례, 관찰 연구 또는 임상시험 근거
- 상세한 작용 기전 데이터
- 허가사항(경고·금기)의 확인과 안전성 검토
- 병용약물(혈당강하제, Clarithromycin, Bupropion 등)에 대한 상호작용 관리 계획

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

