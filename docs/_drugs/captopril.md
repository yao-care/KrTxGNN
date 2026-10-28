---
layout: default
title: Captopril
parent: 모델 예측만 (L5)
nav_order: 179
evidence_level: L5
indication_count: 3
monitor_inn: "CAPTOPRIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism"]
last_modified_at: 2026-10-27
description: "Captopril: 예측 신규 적응증 악성 고혈압성 신질환 (malignant hypertensive renal disease) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198600630/EE"
---

# Captopril
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

## Captopril: ACE 억제제 → 악성 고혈압성 신질환 (malignant hypertensive renal disease)
{: .text-alpha }

## 한 문장 요약

Captopril은 안지오텐신 전환효소(ACE)를 억제하는 약물입니다. TxGNN 모델은 이 약이 **악성 고혈압성 신질환(malignant hypertensive renal disease)**에 효과가 있을 수 있다고 예측합니다. 다만 이 질환을 직접 다룬 **임상시험은 0건**이고, 확인된 문헌 1편은 진단 목적의 증례 보고라서 치료 근거로 보기 어렵습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198600630/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199500320/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200804337/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199703532/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201504524/EE;  |
| 예측 신규 적응증 | 악성 고혈압성 신질환 (malignant hypertensive renal disease) |
| TxGNN 예측 점수 | 0.9928 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 12건 (모두 단일 성분 제제) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

이 보고서용으로 수집한 데이터에는 상세한 작용 기전 정보가 없습니다. Captopril은 ACE 억제제로 알려져 있으며, ACE를 억제하면 안지오텐신 II 생성이 줄어 혈관 수축과 혈압 상승이 완화됩니다.

악성 고혈압과 그에 따른 신장 손상은 레닌-안지오텐신계(RAS)의 과활성과 관련이 깊습니다. 그래서 RAS를 차단하는 ACE 억제제가 기전상 적용될 가능성이 있습니다.

다만 이는 기전에 근거한 가설 수준입니다. 이 질환에서 captopril의 치료 효과를 보여주는 임상 데이터는 현재 확인되지 않았습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [28902735](https://pubmed.ncbi.nlm.nih.gov/28902735/) | 2017 | 증례 보고 | Clinical Nuclear Medicine | captopril 신장 스캔(renography) 양성이었으나 신동맥 협착은 없었고 거대한 혐색소 신세포암이 확인됨. 신장 절제 후 레닌 의존성 고혈압이 호전됨. 진단 목적의 보고이며 치료 효과를 입증하지 않음 |

## 한국 시판 정보

유효 허가는 12건이며 모두 단일 성분 제제입니다. 아래는 주요 5건이고, 대부분 수출용 제품으로 표시되어 있습니다. 허가 적응증은 문서 링크만 기록되어 있어 이 표에 싣지 않았습니다.

| 허가번호 | 제품명 | 제형 | 제조사 |
|---------|------|------|--------|
| 198600630 | 카프릴정12.5밀리그람 | 흰색 원형 정제 | (주)보령 |
| 199500320 | 일동캅토프릴정12.5밀리그람(수출용) | 백색 원형 정제 | 일동제약(주) |
| 200804337 | 파마캅토프릴정25밀리그람(수출용) | 백색 사각형 정제 | (주)한국파마 |
| 199703532 | 케토닐정(수출용) | 백색 원형 정제 | 대한뉴팜(주) |
| 201504524 | 카모투스정(수출용) | 흰색~미백색 사각형 정제 | 경진제약(주) |

## 안전성 고려사항

허가사항의 경고·금기 정보는 이 보고서용 데이터에서 확인하지 못했습니다. 상세 내용은 허가사항을 참조하세요.

**약물 상호작용**: 총 100건이 조사되었습니다. 주요 항목은 다음과 같습니다.
- 중등도: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide(코르티코스테로이드 계열)
- 중등도: metformin, alogliptin, canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, exenatide, acetohexamide, chlorpropamide(당뇨병 치료제)
- 중등도: bupropion, morphine, acetylsalicylic acid, dronabinol
- 경미: aluminum hydroxide, calcium carbonate

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 예측 점수는 높지만(0.9928), 이 질환을 직접 연구한 임상시험이나 문헌이 없어 근거 수준은 L5입니다. 유일한 문헌은 진단 목적의 증례 보고입니다.

**진행하려면 필요한 것:**
- 악성 고혈압성 신질환에서 captopril의 치료 효과를 평가한 임상 또는 전임상 연구
- 허가사항의 경고·금기 정보 확보 (현재 확인되지 않음)
- 작용 기전(MOA) 상세 데이터 보완
- 신기능 저하 환자에서의 안전성 및 모니터링 계획
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

