---
layout: default
title: Amlodipine Maleate
parent: 모델 예측만 (L5)
nav_order: 65
evidence_level: L5
indication_count: 9
drugbank_id: DB00381
monitor_inn: "Amlodipine"
predicted_indications: ["brain stem infarction", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "cerebral artery occlusion", "Braddock syndrome", "MRI defined brain infarct", "ABri amyloidosis", "intracerebral hemorrhage"]
last_modified_at: 2026-11-17
description: "Amlodipine Maleate: 예측 신규 적응증 뇌간 경색 (brain stem infarction) (근거 수준 L5). 기존 적응증: MFDS 허가사항(PDF) 참조"
---

# Amlodipine Maleate
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

## Amlodipine Maleate: 뇌간 경색 (brain stem infarction)
{: .text-alpha }

## 한 문장 요약

Amlodipine Maleate(암로디핀 말레산염)는 디히드로피리딘계 칼슘채널차단제로, 혈압을 낮추는 작용을 합니다.
TxGNN 모델은 **뇌간 경색(brain stem infarction)**에 효과가 있을 수 있다고 예측하지만, 이번에 수집한 데이터에는 이 질환을 직접 다룬 **임상시험 0건, 문헌 0건**으로 모델 예측만 있는 상태입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201805227/EE); [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201406182/EE); [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201400501/EE); [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200807530/EE); [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201804866/EE);  |
| 예측 신규 적응증 | 뇌간 경색 (brain stem infarction) |
| TxGNN 예측 점수 | 0.9994 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 19건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 확보되지 않았습니다. 알려진 정보에 따르면 암로디핀은 L형 칼슘채널을 차단해 혈관 평활근을 이완시키고 혈압을 낮추는 디히드로피리딘계 약물입니다.

혈압 강하는 뇌졸중 이차 예방의 핵심 전략입니다. 이 점에서 뇌간 경색과 같은 허혈성 뇌혈관 질환에서도 기전상 적용 가능성을 생각해 볼 수 있습니다.

다만 이는 일반적인 약리 기전에 근거한 추정입니다. 뇌간 경색 환자를 대상으로 암로디핀을 평가한 시험이나 문헌은 수집되지 않았습니다. 따라서 이 예측은 가설 수준입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

수집된 허가증 20건 중 19건이 유효하고 1건이 취하·취소 상태입니다. 전체 허가증은 최소 20건이며, 아래는 단일 성분 제품 중 주요 5건입니다.

| 허가번호 | 제품명 | 제형 | 제조사 | 상태 |
|---------|------|------|------|------|
| 201400501 | 디아딘정 | 흰색의 팔각형 나정 | 에스피씨(주) | 유효 |
| 201804866 | 로바스크정 | 흰색의 팔각형 정제 | (주)인트로바이오파마 | 유효 |
| 201505922 | 암로베실정5mg | 흰색의 팔각형 나정 | 화일약품(주) | 유효 |
| 201500483 | 휴온스암로디핀정5mg | 흰색의 팔각형 정제 | (주)휴온스 | 유효 |
| 201900838 | 노바스크정2.5밀리그램 | 납작한 마름모꼴의 흰색 정제 | 비아트리스코리아(주) | 유효 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 점수는 높지만 뇌간 경색을 직접 다룬 임상시험이나 문헌이 없어 근거 수준이 L5(모델 예측만 있음)입니다. 현 단계에서는 진행을 판단할 근거가 부족합니다.

**진행하려면 필요한 것:**
- 뇌간 경색(또는 후방순환계 뇌경색)에서 암로디핀을 평가한 임상·전임상 연구 확인
- 식약처 허가사항(경고·금기) 확보 및 안전성 검토
- 작용 기전(MOA) 데이터 보완 및 기전적 연관성 분석
- 허혈성 뇌졸중 환자에서의 저혈압·뇌관류 저하 위험 평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

