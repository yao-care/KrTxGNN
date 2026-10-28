---
layout: default
title: Artemether
parent: 모델 예측만 (L5)
nav_order: 90
evidence_level: L5
indication_count: 8
monitor_inn: "ARTEMETHER"
predicted_indications: ["acquired angioedema", "angioedema", "hereditary angioedema", "nephrogenic syndrome of inappropriate antidiuresis", "acute contagious conjunctivitis", "scleroderma (disease)", "conjunctivitis", "renin-angiotensin-aldosterone system-blocker-induced angioedema"]
last_modified_at: 2026-10-27
description: "Artemether: 예측 신규 적응증 후천성 혈관부종 (acquired angioedema) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202401012/EE"
---

# Artemether
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

## Artemether: 아르테미시닌 계열 약물 → 후천성 혈관부종 (acquired angioedema)
{: .text-alpha }

## 한 문장 요약

Artemether는 아르테미시닌 계열 약물로, 국내에는 수출용 정제 2건의 허가가 등록되어 있습니다.
TxGNN 모델은 **후천성 혈관부종(acquired angioedema)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 **임상시험과 문헌은 한 건도 없습니다**.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202401012/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202401013/EE |
| 예측 신규 적응증 | 후천성 혈관부종 (acquired angioedema) |
| TxGNN 예측 점수 | 0.9990 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 2건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 이번 평가에 사용한 데이터에서는 Artemether와 후천성 혈관부종 사이의 뚜렷한 기전적 연결고리를 확인하지 못했습니다.

혈관부종은 브래디키닌 또는 보체 경로와 관련되어 있으나, 이는 Artemether의 알려진 표적이 아닙니다. 0.9990이라는 높은 예측 점수는 네트워크 기반의 계산 결과일 뿐이며, 이를 뒷받침하는 임상시험이나 문헌이 없습니다. 따라서 이 예측은 가설 단계로 보아야 합니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202401012 | 루마트-이정(수출용) | 황색의 원형정제 | 허가 문서 링크만 확인되며 적응증 본문은 기재되어 있지 않음 |
| 202401013 | 루마트정(수출용) | 황색의 장방형정제 | 허가 문서 링크만 확인되며 적응증 본문은 기재되어 있지 않음 |

두 허가 모두 단일 성분 제품이며 유효 상태입니다.

## 안전성 고려사항

- **약물 상호작용**: 총 95건이 확인되었으며, 주요 항목은 다음과 같습니다.
  - 중대(Major): Clarithromycin, Cobicistat, Amprenavir, Apalutamide, Atazanavir, Boceprevir
  - 중등도(Moderate): Dexamethasone, Miconazole, Troglitazone, Deferasirox, Bosentan, Brigatinib 등

허가사항의 경고 및 금기 정보는 이번 데이터에 포함되지 않았으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
후천성 혈관부종에 대한 임상시험과 문헌이 없고 기전적 연결고리도 확인되지 않아, 근거는 모델 예측뿐인 L5 수준입니다.

**진행하려면 필요한 것:**
- 후천성 혈관부종과 Artemether의 연관성을 다룬 전임상 또는 기전 연구
- 작용 기전(MOA) 데이터 확보
- 허가사항의 경고·금기 정보 확보 및 안전성 검토
- 약물 상호작용(특히 중대 등급 항목)에 대한 위험 평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

