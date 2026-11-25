---
layout: default
title: Donepezil
parent: 모델 예측만 (L5)
nav_order: 287
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-24
description: "Donepezil: 예측 신규 적응증 심인성 운동장애 (Psychogenic Movement Disorders) (근거 수준 L5). 기존 적응증: 알츠하이머형 치매증상의 치료"
monitor_inn: "DONEPEZIL"
predicted_indications: ["psychogenic movement disorders", "chronic tic disorder", "primary orthostatic tremor", "benign shuddering attacks", "extrapyramidal and movement disease", "tremor-nystagmus-duodenal ulcer syndrome", "benign paroxysmal tonic upgaze of childhood with ataxia", "lingual-facial-buccal dyskinesia"]
---

# Donepezil
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

## Donepezil: 알츠하이머형 치매에서 심인성 운동장애로
{: .text-alpha }

## 한 문장 요약

Donepezil은 아세틸콜린에스테라제 억제제로, 한국에서 허가되어 시판 중입니다(허가 건수와 상태는 빠른 개요 참조). 다만 허가 적응증 원문은 이 보고서용으로 수집된 데이터에 텍스트로 포함되지 않았습니다.
TxGNN 모델은 **심인성 운동장애(Psychogenic Movement Disorders)**에 효과가 있을 수 있다고 예측하지만(점수 0.9923), 이 질환을 직접 뒷받침하는 **임상시험은 0건**, **문헌도 0편**입니다.
따라서 예측은 모델 수준에 머물러 있으며, 같은 운동 질환 범주에서는 만성 틱 장애(문헌 5편), 추체외로 및 운동 질환(문헌 4편), 설-안면-협부 이상운동증(문헌 20편)이 상대적으로 더 많은 근거를 갖고 있습니다.

<!-- review:begin kr-lic-20261124c-donepezil-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “Donepezil은 아세틸콜린에스테라제 억제제로, 한국에서 20건의 단일제 허가증이 유효하며 시판 중입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 단일·복합 표기와 건수를 본문에 고정해 쓰지 않고, 매주 갱신되는 허가 자료를 반영하는 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 2026-11-25에 식품의약품안전처 품목허가 상세 자료(2026-03)의 주성분명으로 품목별로 다시 확인한 결과, 이 자료에 수록된 허가 품목은 모두 단일 성분 제제입니다. 이 자료에는 허가의 일부만 수록되어 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-donepezil-1 -->

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 알츠하이머형 치매증상의 치료 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201405368/EE)) |
| 예측 신규 적응증 | 심인성 운동장애 (Psychogenic Movement Disorders) |
| TxGNN 예측 점수 | 0.9923 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Donepezil 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “알츠하이머병의 인지 징후 및 증상의 발병기전에 관한 현재의 이론은 그 중 일부를 콜린성 신경전달의 결핍에 기인한 것으로 본다. 도네페질염산염은 콜린성 기능을 증강시킴으로써 치료 효과를 나타내는 것으로 추정된다.” 영어 원문: "Current theories on the pathogenesis of the cognitive signs and symptoms of Alzheimer’s disease attribute some of them to a deficiency of cholinergic neurotransmission. Donepezil hydrochloride is postulated to exert its therapeutic effect by enhancing cholinergic function." ([DailyMed: Aricept (donepezil hydrochloride) prescribing information, Eisai Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e451e1-e4d7-4439-a675-c5457ba20975), 버전 2021-12-30; 확인일 2026-11-19). 알려진 정보에 따르면 donepezil은 아세틸콜린에스테라제를 억제하여 뇌 내 콜린성 신호를 강화하는 약물입니다. 콜린성 신호는 기저핵 등 운동 조절 회로와 관련이 있어 운동 질환에 대한 접근 자체는 생각해 볼 수 있습니다.

그러나 심인성 운동장애는 기능성(functional) 기원의 질환이어서, 콜린성 기전이 직접 관여한다는 근거는 뚜렷하지 않습니다. 이번 예측 점수는 TxGNN 모델(딥러닝)에서 나온 것으로, 모델이 관련 질환 사이에서 학습한 유사성을 반영했을 수 있으며 생물학적 근거를 뜻하지는 않습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201405368 | 뉴페질구강붕해필름10mg(도네페질염산염) | 연한 노란색의 직사각형 구강붕해필름 | (주)씨엘팜 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201405368/EE) | 유효 |
| 200708819 | 도네트정10밀리그램(도네페질염산염) | 황색의 원형 필름코팅정제 | 하나제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200708819/EE) | 유효 |
| 201307375 | 아리셉트정23밀리그램(도네페질염산염) | 빨간색의 양면이 볼록한 원형 필름코팅정 | (주)한독 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201307375/EE) | 유효 |
| 202107340 | 도네리온패취87.5밀리그램(도네페질) | 흰색 내지 미백색의 지지체와 엠보싱 처리된 모서리가 둥근 사각형의 피복체… | (주)셀트리온 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202107340/EE) | 유효 |
| 201506131 | 아리셉트구강용해필름5밀리그램(도네페질염산염) | 흰색의 구강용해필름 | 한국에자이(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201506131/EE) | 유효 |

위 표는 허가 최소 20건 중 5건입니다.

<!-- licenses:end -->

구강붕해필름, 구강용해필름, 패취 등 다양한 제형이 허가되어 있습니다. 위 표는 주요 5건만 기재했으며, 수출용 허가(아이큐어도네페질패취25, 아셉정10mg)도 포함됩니다.

## 안전성 고려사항

- **약물 상호작용**: 확인된 상호작용 100건 중 일부를 보면 다음과 같습니다.
  - **주요(Major)**: Bupropion
  - **중등도(Moderate)**: 항콜린제 및 위장관 약물(Hyoscyamine, Atropine, Glycopyrronium, Clidinium, Dicyclomine), H2 차단제(Famotidine, Ranitidine, Cimetidine), Loperamide, Dexamethasone, Metronidazole, Dolasetron 등
  - **경미(Minor)**: Aprepitant, 아스피린, Lorcaserin, Clarithromycin 등
- **지식 그래프상 금기 관련 질환**: 간질, 천식, 방광 경부 폐쇄, 활동성 소화성 궤양, 동기능부전증후군, 房室차단 등. 허가 문서의 문구가 아니라 모델 지식 그래프의 정보이므로 허가사항에서 확인이 필요합니다.
- **운동 증상 관련 신호**: 추체외로 및 운동 질환 분야 문헌(2025년 체계적 문헌고찰)에서 콜린에스테라제 억제제가 운동 장애를 유발하거나 악화시킬 수 있다는 안전성 신호가 보고되었습니다. 운동 질환을 대상으로 한 재창출에서 중요한 고려 사항입니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
심인성 운동장애에 대해서는 모델 예측 점수만 높을 뿐 임상시험과 문헌이 전혀 없고(L5), 기능성 질환에서 콜린성 기전의 직접적 타당성도 확인되지 않습니다. 콜린에스테라제 억제제가 오히려 운동 증상을 유발할 수 있다는 보고도 있어 우선순위를 높일 근거가 부족합니다.

**진행하려면 필요한 것:**
- 허가사항(경고, 금기, 허가 적응증) 원문 확보: 현재 허가증 PDF 내용이 수집되지 않아 안전성 1차 검토를 진행할 수 없습니다.
- DrugBank에서 작용 기전(MOA) 데이터 보완
- 심인성 운동장애에 대한 문헌 및 임상시험 재검색
- 같은 예측 목록 중 근거가 더 있는 만성 틱 장애(근거 수준 L4, 소규모 소아 연구와 증례 보고 및 전임상 데이터)나 설-안면-협부 이상운동증(L4, Cochrane 체계적 문헌고찰 포함)을 우선 후보로 검토. 단, 두 경우 모두 대조군이 있는 근거는 부족하며 donepezil에 특이적인 효능이 확립되지 않았습니다.

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Aricept (donepezil hydrochloride) prescribing information, Eisai Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e451e1-e4d7-4439-a675-c5457ba20975) |
| 2026-11-24 | 단일·복합 표기: “Donepezil은 아세틸콜린에스테라제 억제제로, 한국에서 20건의 단일…” → 고정된 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 (2026-11-25 수정, 이전 판은 기록에 보존) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

