---
layout: default
title: Carvedilol
parent: 모델 예측만 (L5)
nav_order: 186
evidence_level: L5
indication_count: 4
monitor_inn: "CARVEDILOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
last_modified_at: 2026-10-31
description: "Carvedilol: 예측 신규 적응증 악성 고혈압성 신질환 (malignant hypertensive renal disease) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201905581/EE"
---

# Carvedilol
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

## Carvedilol: 알파/베타 차단제 → 악성 고혈압성 신질환 (malignant hypertensive renal disease)
{: .text-alpha }

## 한 문장 요약

Carvedilol은 알파-1/베타 차단 작용을 가진 약물입니다. TxGNN 모델은 **악성 고혈압성 신질환(malignant hypertensive renal disease)**에 효과가 있을 수 있다고 예측하며, 예측 점수는 0.9955입니다. 이 예측을 직접 뒷받침하는 임상시험과 문헌은 **0건**이어서 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201905581/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200701226/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201805248/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200100858/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201200186/EE;  |
| 예측 신규 적응증 | 악성 고혈압성 신질환 (malignant hypertensive renal disease) |
| TxGNN 예측 점수 | 0.9955 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 20건 (목록은 일부일 수 있음) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 이 보고서를 위해 수집된 데이터에는 상세한 작용 기전 정보가 없습니다. 알려진 약리 특성상 carvedilol은 알파-1 및 베타 수용체를 함께 차단하므로, 이론적으로는 혈압을 낮추어 고혈압에 의한 신장 손상을 줄일 가능성이 있습니다.

다만 이는 이론적 추정일 뿐입니다. 이 예측을 지지하는 임상시험이나 문헌이 제공되지 않았습니다. 악성 고혈압은 임상적 응급 상황이며, 보통 용량 조절이 쉬운 정맥 주사제로 관리합니다. 따라서 경구 베타 차단제가 이 상황에 적합한지는 불확실합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

유효 허가가 20건 확인되었으며, 아래는 그중 일부입니다. 허가 적응증은 각 허가사항 문서에서 확인할 수 있습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201905581 | 카베씨티정25mg | 흰색의 원형 정제 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201905581/EE) 참조 |
| 200701226 | 카베날정12.5밀리그램 | 적갈색의 원형 정제 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200701226/EE) 참조 |
| 201805248 | 카르베타정25밀리그램 | 흰색의 원형 정제 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201805248/EE) 참조 |
| 200100858 | 알보젠카베디롤정25밀리그램 | 흰색의 원형정제 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200100858/EE) 참조 |
| 201404426 | 카르베롤서방캡슐32밀리그램 | 속방성 및 서방성 과립이 들어있는 경질캡슐제 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201404426/EE) 참조 |

## 안전성 고려사항

- **약물 상호작용**: 수집된 상호작용 100건 중 일부를 아래에 정리했습니다.
  - 주요(Major): Epinephrine
  - 중등도(Moderate): Hydrocortisone, Hyoscyamine, Bupropion, Triamcinolone, Morphine, Atropine, Dexamethasone, Lorcaserin, Betamethasone, Budesonide, Canagliflozin, Acetohexamide, 칼슘 제제(Calcium Phosphate, Calcium acetate, Calcium carbonate, Calcium citrate)
  - 경미(Minor): Acetylsalicylic acid, Aluminum hydroxide, Attapulgite

경고 및 금기 등 그 밖의 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 예측 점수는 높지만 임상시험과 문헌이 없어 근거 수준이 L5(모델 예측만 있음)입니다.
- 악성 고혈압은 정맥 주사제로 관리하는 응급 상황이어서 경구 베타 차단제의 적합성도 불확실합니다.

**진행하려면 필요한 것:**
- 이 질환에서의 carvedilol 효과를 직접 평가한 임상 또는 전임상 연구
- 상세한 작용 기전(MOA) 데이터
- 허가사항(경고·금기) 원문 확인 및 안전성 검토
- 악성 고혈압 상황에서의 투여 경로·용량 적합성에 대한 전문가 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

