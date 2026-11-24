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
last_modified_at: 2026-11-24
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

Amlodipine Besylate는 칼슘 채널 차단제 계열의 약물로, 국내에서 단일제와 복합제 형태로 널리 시판되고 있습니다. TxGNN 모델은 **뇌간 경색(brain stem infarction)**에 효과가 있을 수 있다고 예측합니다. 다만 이 예측을 직접 뒷받침하는 임상시험과 문헌은 **0건**이어서, 현재는 모델 예측 단계입니다.

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

미국 FDA가 승인한 Amlodipine Besylate 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “암로디핀은 디히드로피리딘계 칼슘 길항제(칼슘 이온 길항제 또는 서통로 차단제)로서, 혈관 평활근 및 심근으로의 칼슘 이온의 막횡단 유입을 억제한다. 실험 자료에 따르면 암로디핀은 디히드로피리딘 결합 부위와 비디히드로피리딘 결합 부위 모두에 결합하는 것으로 시사된다.” 영어 원문: "Amlodipine is a dihydropyridine calcium antagonist (calcium ion antagonist or slow-channel blocker) that inhibits the transmembrane influx of calcium ions into vascular smooth muscle and cardiac muscle. Experimental data suggest that amlodipine binds to both dihydropyridine and nondihydropyridine binding sites." ([DailyMed: Sdamlo (amlodipine) prescribing information, Pangea Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=886a7f97-60a4-4206-a6c7-5206069ed487), 버전 2026-09-28; 확인일 2026-11-19). 알려진 정보에 따르면 Amlodipine은 혈관 평활근의 칼슘 유입을 차단하는 칼슘 채널 차단제입니다. 이 혈압 강하 작용은 뇌졸중 2차 예방에 기여할 가능성이 있습니다.

그러나 이번에 수집된 자료에는 뇌간 경색에서 Amlodipine을 검증한 연구가 없습니다. 예측 점수가 높은 것은 다른 뇌혈관 질환과의 연관성이 반영된 결과로 보이며, 뇌간 경색에 특화된 기전적 근거는 확인되지 않았습니다. 따라서 이 예측은 가설 수준으로 보아야 합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

주요 허가 5건입니다. 허가 적응증의 상세 내용은 각 허가사항 문서를 참조하세요.

<!-- review:begin kr-lic-20261124c-amlodipine_besylate-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “단일 성분 제품 중 주요 허가 5건입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 이 사이트 자료의 성분란에는 일치한 성분만 기록되어 허가 품목별 단일 성분·복합 성분 여부를 확인할 수 없으므로, 단일·복합 표기를 빼고 건수는 쓰지 않고 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-amlodipine_besylate-1 -->

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201400501 | 디아딘정(암로디핀베실산염) | 흰색의 팔각형 나정 | 에스피씨(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201400501/EE) | 유효 |
| 201804866 | 로바스크정(암로디핀베실산염) | 흰색의 팔각형 정제 | (주)인트로바이오파마 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201804866/EE) | 유효 |
| 201505922 | 암로베실정5mg(암로디핀베실산염) | 흰색의 팔각형 나정 | 화일약품(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201505922/EE) | 유효 |
| 201500483 | 휴온스암로디핀정5mg(암로디핀베실산염) | 흰색의 팔각형 정제 | (주)휴온스 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201500483/EE) | 유효 |
| 201603362 | 에이디핀정(암로디핀베실산염) | 흰색의 팔각형 정제 | 아이큐어(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201603362/EE) | 유효 |

위 표는 허가 최소 20건 중 5건입니다.

<!-- licenses:end -->

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
뇌간 경색에 대해 모델 예측만 있고, 이를 직접 검증한 임상시험이나 문헌이 없습니다(L5). 기전 데이터와 허가사항 기반 안전성 정보도 확보되지 않아 다음 단계로 진행하기 어렵습니다.

**진행하려면 필요한 것:**
- 뇌간 경색을 직접 다룬 임상시험 또는 문헌 근거
- 상세한 약물 작용 기전(MOA) 데이터
- 허가사항(경고, 금기)의 안전성 정보 확인
- 뇌졸중 환경에서의 혈압 목표와 저혈압 위험을 검토하는 안전성 계획

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Sdamlo (amlodipine) prescribing information, Pangea Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=886a7f97-60a4-4206-a6c7-5206069ed487) |
| 2026-11-24 | 단일·복합 표기: “단일 성분 제품 중 주요 허가 5건입니다.” → 확인할 수 없는 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

