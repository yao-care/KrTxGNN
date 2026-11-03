---
layout: default
title: Dexamethasone
parent: 모델 예측만 (L5)
nav_order: 268
evidence_level: L5
indication_count: 9
monitor_inn: "Dexamethasone"
predicted_indications: ["alopecia mucinosa", "telogen effluvium", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions", "alopecia universalis onychodystrophy vitiligo", "prolapse of lacrimal gland"]
last_modified_at: 2026-11-03
description: "Dexamethasone: 예측 신규 적응증 점액성 탈모증 (alopecia mucinosa) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/196300064/EE"
---

# Dexamethasone
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

## Dexamethasone: 점액성 탈모증 (alopecia mucinosa)
{: .text-alpha }

## 한 문장 요약

Dexamethasone은 항염증·면역억제 작용을 가진 글루코코르티코이드 계열 약물로, 국내에서 정제, 주사제, 점안제, 연고, 크림 등 여러 제형으로 허가되어 있습니다.
TxGNN 모델은 **점액성 탈모증(alopecia mucinosa)**에 효과가 있을 수 있다고 예측하지만, 현재 이 질환을 직접 다룬 **임상시험과 문헌은 한 건도 없습니다**.
따라서 모델 예측 단계에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/196300064/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200200559/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201111067/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199602981/EE; 이 약은 습진·피부염군(진행성 지장각피증, 만성단순태선, 일광피부염 포함), 양진군(구진두드러기 포함), 벌 |
| 예측 신규 적응증 | 점액성 탈모증 (alopecia mucinosa) |
| TxGNN 예측 점수 | 0.9999 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 17건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

허가증 목록은 일부만 확인된 것일 수 있습니다.

## 이 예측이 타당한 이유는?

현재 Dexamethasone의 상세한 작용 기전 데이터는 확보되지 않았습니다. 다만 글루코코르티코이드 계열로서 염증 반응과 면역 반응을 억제한다는 점은 널리 알려져 있습니다.

점액성 탈모증은 모낭 주변에 염증이 생기는 질환입니다. 다른 염증성 탈모 질환과 비슷한 특성이 있어, 모델이 이런 유사성을 반영해 높은 점수를 준 것으로 보입니다.

이 연결은 어디까지나 추정입니다. 이 질환에 대한 임상시험이나 문헌이 없어 직접 뒷받침하는 자료는 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

유효 허가는 17건, 취소 허가는 3건입니다. 아래는 유효한 단일 성분 허가 중 주요 5건입니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200201703 | 덱사톱크림 | 크림제 | 습진·피부염군, 양진군, 벌레물린데, 건선, 손·발바닥 농포증, 편평태선, 홍피증, 만성원판상홍반, 약진·중독진과 원형탈모증... |
| 198902460 | 페리덱스연고 | 연고제 | 미란(짓무름) 또는 궤양을 수반하는 난치성 구내염 및 설염에 의한 염증의 완화 |
| 202004515 | 이바나파연고 | 연고제 | 미란(짓무름) 또는 궤양을 수반하는 난치성 구내염 및 설염에 의한 염증의 완화 |
| 196300064 | 부광덱사메타손정 | 정제 | 허가 적응증 본문 미확인 |
| 199602981 | 유한덱사메타손정 | 정제 | 허가 적응증 본문 미확인 |

## 안전성 고려사항

- **주요 경고 및 금기**: 허가사항의 경고·금기 정보는 이번 자료에 포함되지 않았으므로, 허가사항을 직접 참조하세요.
- **약물 상호작용**: 총 100건이 확인되었고, 그중 20건을 검토했습니다.
  - **Major**: Fentanyl, Adalimumab
  - **Moderate**: Zidovudine, Paclitaxel, Isotretinoin, Abemaciclib, Acalabrutinib, Acarbose, Acebutolol, Acetazolamide, Codeine, Dihydrocodeine, Ibuprofen, Ketorolac, Nifedipine 등
  - **Minor**: Dolutegravir, Lidocaine, Formoterol

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 점액성 탈모증에 대한 임상시험과 문헌이 없어 근거 수준이 L5(모델 예측만 존재)입니다.
- 높은 예측 점수만으로는 진행을 판단할 수 없습니다.

**진행하려면 필요한 것:**
- 점액성 탈모증에서 Dexamethasone 또는 다른 코르티코스테로이드의 효과를 다룬 증례·관찰연구·임상시험 확인
- Dexamethasone의 작용 기전(MOA) 데이터 확보
- 허가사항의 경고·금기 정보 확보
- 투여 경로(국소 또는 전신) 적합성 검토
- 전신 투여 시 약물 상호작용 관리 계획 수립

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

