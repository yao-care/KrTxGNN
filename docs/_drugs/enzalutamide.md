---
layout: default
title: Enzalutamide
parent: 모델 예측만 (L5)
nav_order: 313
evidence_level: L5
indication_count: 5
monitor_inn: "ENZALUTAMIDE"
predicted_indications: ["prostate leiomyoma", "Brenner tumor", "fibroma of prostate", "benign reproductive system neoplasm", "benign prostate phyllodes tumor"]
last_modified_at: 2026-10-28
description: "Enzalutamide: 예측 신규 적응증 전립선 평활근종 (prostate leiomyoma) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202600225/EE"
---

# Enzalutamide
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **5** 건
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

## Enzalutamide: 안드로겐 수용체 억제제 → 전립선 평활근종 (prostate leiomyoma)
{: .text-alpha }

## 한 문장 요약

Enzalutamide는 안드로겐 수용체를 표적으로 하는 약물로, 한국에서 단일제 허가를 받아 사용되고 있습니다.
TxGNN 모델은 **전립선 평활근종(prostate leiomyoma)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다.
따라서 이 예측은 모델 계산에만 근거한 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202600225/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202500452/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202402841/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202402842/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201307883/EE;  |
| 예측 신규 적응증 | 전립선 평활근종 (prostate leiomyoma) |
| TxGNN 예측 점수 | 0.9957 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 7건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 다만 enzalutamide는 안드로겐 수용체(AR) 신호를 억제하는 계열의 약물로 알려져 있습니다. 전립선 기질 조직에서 AR 신호가 어떤 역할을 할 수 있다는 가설이 가능합니다.

전립선 평활근종은 전립선의 양성 중간엽 종양입니다. AR 억제와의 연결은 어디까지나 추측 수준이며, 이 예측은 전립선암과의 근접성 때문에 높은 점수를 받았을 가능성이 큽니다. 이를 지지하는 임상시험이나 문헌은 확인되지 않았습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202600225 | 엔잘엑스연질캡슐40밀리그램 | 연질캡슐 | 허가 적응증 텍스트 없음 |
| 202500452 | 아나미드연질캡슐40밀리그램 | 연질캡슐 | 허가 적응증 텍스트 없음 |
| 202402841 | 엑스탄디정80밀리그램 | 필름코팅정 | 허가 적응증 텍스트 없음 |
| 202402842 | 엑스탄디정40밀리그램 | 필름코팅정 | 허가 적응증 텍스트 없음 |
| 201307883 | 엑스탄디연질캡슐40mg | 연질캡슐 | 허가 적응증 텍스트 없음 |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (호르몬 계열, 안드로겐 수용체 억제) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **약물 상호작용**: 이번 조회에서 총 100건이 확인되었으며, 그중 일부 주요 항목은 다음과 같습니다.
  - 주요(Major) 등급: bupropion, dolasetron, eliglustat
  - 중등도(Moderate) 등급: famotidine, rabeprazole, omeprazole, hydrocortisone, dexamethasone, clarithromycin, aprepitant, loperamide, saxagliptin, linagliptin, empagliflozin 등

경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
전립선 평활근종에 대해 직접 연구한 임상시험이나 문헌이 없으며, 예측은 모델 계산에만 근거합니다. 기전적 연결도 추측 수준입니다.

**진행하려면 필요한 것:**
- 전립선 평활근종에서 안드로겐 수용체 발현과 의존성을 확인하는 전임상 또는 병리 연구
- 작용 기전(MOA) 상세 데이터 보완
- 허가사항(경고·금기) 확인 및 안전성 검토
- 질환의 희귀성을 고려한 임상 근거 확보 가능성 평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

