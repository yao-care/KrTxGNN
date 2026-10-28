---
layout: default
title: Nadolol
parent: 모델 예측만 (L5)
nav_order: 535
evidence_level: L5
indication_count: 4
monitor_inn: "NADOLOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
last_modified_at: 2026-10-28
description: "Nadolol: 예측 신규 적응증 악성 고혈압성 신장질환 (malignant hypertensive renal disease) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201604248/EE"
---

# Nadolol
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **4** 건
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

## Nadolol: 비선택적 베타차단제 → 악성 고혈압성 신장질환 (malignant hypertensive renal disease)
{: .text-alpha }

## 한 문장 요약

Nadolol은 비선택적 베타아드레날린 차단제 계열의 약물입니다. TxGNN 모델은 **악성 고혈압성 신장질환(malignant hypertensive renal disease)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 **임상시험은 0건, 문헌도 0편**으로 모델 예측 단계에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201604248/EE |
| 예측 신규 적응증 | 악성 고혈압성 신장질환 (malignant hypertensive renal disease) |
| TxGNN 예측 점수 | 0.9959 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 nadolol은 베타 수용체를 차단하여 심박수와 혈압을 낮추는 약물입니다. 이 혈압 강하 작용과 레닌-안지오텐신 축 억제를 통해 고혈압성 신장 손상을 줄일 가능성이 이론적으로 제기됩니다.

다만 이 예측은 근거가 독립적이지 않습니다. 같은 계열의 신혈관성 질환 항목과 거의 같은 점수(약 0.9959)를 보여, 서로 밀접하게 관련된 질환 분류에서 비롯된 신호일 가능성이 큽니다. 또한 nadolol은 신장으로 배설되므로 신장 기능이 저하된 환자에게는 용량 조절이 필요하며, 이는 추가적인 안전성 고려 사항입니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201604248 | 나도가드정40밀리그램(나도롤) | 흰색의 장방형 정제 | 허가 적응증 텍스트가 기재되어 있지 않음 |

## 안전성 고려사항

- **약물 상호작용**: 이번 보고서에 편집된 자료에서 총 100건의 상호작용이 확인되었으며, 그중 주요 항목은 다음과 같습니다.
  - 주의 필요(Major): Epinephrine
  - 중등도(Moderate): Hydrocortisone, Methscopolamine, Hyoscyamine, Bupropion, Triamcinolone, Morphine, Atropine, Dexamethasone, Betamethasone, Budesonide, Cimetidine, Canagliflozin, Dapagliflozin, Chlorpropamide 등
  - 경미(Minor): Acetylsalicylic acid, Clarithromycin, Magnesium oxide
- 허가사항의 경고 및 금기 정보는 이번 자료에 없으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
악성 고혈압성 신장질환에 대한 임상시험과 문헌이 전혀 없고 모델 예측 점수만 있어 근거 수준이 L5입니다. 인접 질환 항목과 점수가 동일하여 독립적인 신호로 보기도 어렵습니다.

**진행하려면 필요한 것:**
- 해당 질환에서 nadolol 또는 베타차단제를 직접 평가한 임상 및 전임상 연구
- 허가사항(경고, 금기)의 확보 및 분석
- 상세한 작용 기전(MOA) 데이터
- 신장 기능 저하 환자에 대한 용량 및 안전성 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

