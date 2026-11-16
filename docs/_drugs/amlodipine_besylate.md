---
layout: default
title: Amlodipine Besylate
parent: 모델 예측만 (L5)
nav_order: 64
evidence_level: L5
indication_count: 9
drugbank_id: DB00381
monitor_inn: "Amlodipine"
predicted_indications: ["brain stem infarction", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "cerebral artery occlusion", "Braddock syndrome", "MRI defined brain infarct", "ABri amyloidosis", "intracerebral hemorrhage"]
last_modified_at: 2026-11-16
description: "Amlodipine Besylate: 예측 신규 적응증 뇌간 경색 (brain stem infarction) (근거 수준 L5). 기존 적응증: MFDS 허가사항(PDF) 참조"
---

# Amlodipine Besylate
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

## Amlodipine Besylate: 뇌간 경색 (brain stem infarction)
{: .text-alpha }

## 한 문장 요약

Amlodipine besylate는 디히드로피리딘계 칼슘 채널 차단제로, 한국에서 단일 성분 제제와 복합제로 널리 시판되고 있습니다. TxGNN 모델은 **뇌간 경색(brain stem infarction)**에 효과가 있을 수 있다고 예측합니다. 다만 이 질환을 직접 다룬 **임상시험은 0건, 문헌도 0건**이어서 현재는 모델 예측 단계입니다.

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

현재 상세한 작용 기전 데이터가 없습니다. 알려진 약리학적 분류를 근거로 보면, amlodipine은 L-type 칼슘 채널을 차단하는 디히드로피리딘계 약물입니다. 혈관 평활근을 이완시켜 혈압을 낮춥니다.

혈압 조절은 뇌졸중 예방의 핵심 요소이므로, 혈관 확장과 혈압 강하를 통한 간접적인 연결고리는 생각해 볼 수 있습니다. 하지만 이는 항고혈압제 전반에 해당하는 일반적인 추론입니다. 뇌간 경색에 특이적으로 이점이 있다고 뒷받침하는 임상시험이나 문헌은 이번에 확인되지 않았습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

단일 성분 제제 중 유효 상태인 주요 허가 5건입니다. 허가 적응증 원문은 각 허가사항 문서에서 확인해야 합니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201400501 | 디아딘정 | 흰색의 팔각형 나정 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201400501/EE) 참조 |
| 201804866 | 로바스크정 | 흰색의 팔각형 정제 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201804866/EE) 참조 |
| 201505922 | 암로베실정5mg | 흰색의 팔각형 나정 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201505922/EE) 참조 |
| 201500483 | 휴온스암로디핀정5mg | 흰색의 팔각형 정제 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201500483/EE) 참조 |
| 201505007 | 노바스틴정5밀리그램 | 흰색의 팔각형 정제 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201505007/EE) 참조 |

확인된 허가증 20건 중 19건이 유효하고 1건이 취소 상태입니다. 전체 허가 건수는 최소 20건이며, 위 목록은 일부일 수 있습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
뇌간 경색에 대한 직접적인 임상시험과 문헌이 없고 모델 예측만 있어 근거 수준이 L5입니다. 작용 기전 데이터와 허가사항의 안전성 정보도 아직 확보되지 않았습니다.

**진행하려면 필요한 것:**
- 뇌간 경색(또는 후방 순환계 뇌경색)을 직접 대상으로 한 임상시험 및 문헌 확보
- 작용 기전 데이터 보완 (예: DrugBank 조회)
- 허가사항의 경고, 금기, 약물 상호작용 정보 확보 및 분석
- 뇌졸중 환자에서 혈압 강하 시 뇌관류 저하 위험에 대한 안전성 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

