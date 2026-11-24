---
layout: default
title: Codeine
parent: 모델 예측만 (L5)
nav_order: 232
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
description: "Codeine: 예측 신규 적응증 비강 질환 (Nasal Cavity Disease) (근거 수준 L5). 기존 적응증: (정제) 1. 19세 이상 성인 1) 기관지염, 폐렴, 인두염, 후두염, 기관지천식, 기타 호흡기 질환에…"
monitor_inn: "codeine"
predicted_indications: ["nasal cavity disease", "trigeminal autonomic cephalalgia", "allergic urticaria"]
---

# Codeine
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

## Codeine: 통증·기침 완화에서 비강 질환으로
{: .text-alpha }

## 한 문장 요약

Codeine(코데인)은 오피오이드 계열 약물로, 한국에서 인산코데인 단일제로 허가되어 시판되고 있습니다. TxGNN 모델은 **비강 질환(Nasal Cavity Disease)**에 효과가 있을 수 있다고 예측하지만, 이를 지지하는 임상시험은 **0건**이며 문헌은 **1건**(치료 효과가 아닌 이물 관련 증례 보고)뿐입니다. 따라서 실질적인 근거 없이 모델 예측에만 의존한 상태입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | (정제) 1. 19세 이상 성인 1) 기관지염, 폐렴, 인두염, 후두염, 기관지천식, 기타 호흡기 질환에 동반되는 기침의 진정 2) 통증의 완화 2. 13세 이상 ∼ 18세 이하의 소아 아세트아미노펜이나 이부프로펜과 같은 다른 진통제로 경감되지 않은 염증에 의한 급성 중등도 통증의 완화 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199403297/EE)) |
| 예측 신규 적응증 | 비강 질환 (Nasal Cavity Disease) |
| TxGNN 예측 점수 | 0.9993 |
| 근거 수준 | L5 (모델 예측만 있고 치료 효과를 보여주는 연구 없음) |
| 한국 시판 현황 | 시판 중 (유효 허가 8건 / 전체 11건) |
| 허가증 수 | 11건 (유효 8건) |
| 권장 결정 | Hold |

> 참고: 데이터 상 이 예측의 근거 수준은 L4로 표기되어 있으나, 유일한 문헌이 치료 효과나 기전 연구가 아닌 부작용성 증례 보고이므로 본 보고서에서는 판정 규칙에 따라 L5로 평가했습니다.

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Codeine 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “코데인 황산염은 뮤-오피오이드 수용체에 비교적 선택적인 오피오이드 작용제이나, 모르핀보다 훨씬 약한 친화력을 갖는다. 코데인의 진통 특성은 모르핀으로의 전환에서 비롯되는 것으로 추정되어 왔으나, 정확한 진통 작용 기전은 아직 알려져 있지 않다.” 영어 원문: "Codeine sulfate is an opioid agonist relatively selective for the mu-opioid receptor, but with a much weaker affinity than morphine. The analgesic properties of codeine have been speculated to come from its conversion to morphine, although the exact mechanism of analgesic action remains unknown." ([DailyMed: codeine sulfate prescribing information, Lannett Company, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5819bdf7-300e-45b8-8f3a-447b53656293), 버전 2026-01-16; 확인일 2026-11-19). 알려진 정보에 따르면 codeine은 mu-오피오이드 수용체 작용을 통해 진해 및 경도 진통 효과를 나타내는 약물입니다. 그러나 이것은 증상 완화에 해당하며, 비강 질환 자체를 치료하는 기전은 확인되지 않았습니다.

이번 데이터에서 비강 질환과 연결되는 유일한 문헌은 오피오이드(코데인과 아편 혼합물)가 포함된 이물 주위에 비석(rhinolith)이 형성된 증례입니다. 이는 치료 효과가 아니라 우발적·이상 사례에 가깝습니다. 따라서 TxGNN의 매우 높은 점수(0.9993)는 임상적·기전적 근거로 뒷받침되지 않습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | 증례 보고 | Ear, Nose, & Throat Journal | 코데인과 아편 혼합물을 나일론으로 싼 이물 주위에 형성된 일측성 비석(rhinolith)의 드문 증례. 국소마취하에 제거했으며, 치료 효과를 보여주는 연구가 아님 |

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 199403297 | 명문인산코데인정 | 흰색의 원형정제 | 명문제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199403297/EE) | 유효 |
| 200308509 | 데코인정(코데인인산염수화물) | 흰색~황색의 원형 정제 | 성원애드콕제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200308509/EE) | 유효 |
| 199907257 | 코노펜캡슐 | 백색의 과립 또는 분말이 충진되어 있는 상부 적색, 하부 백색의 경질캡슐… | 하나제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199907257/EE) | 유효 |
| 199704636 | 비씨인산코데인정 | 흰색 내지 담황색의 원형 정제 | (주)비씨월드제약 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199704636/EE) | 유효 |
| 199806858 | 구주인산코데인정 | 백색 내지 황색을 띤 원형 정제 | 구주제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199806858/EE) | 유효 |

위 표는 허가 11건 중 5건입니다.

<!-- licenses:end -->

위 표 외의 단일제는 일성코데인정(수출용)과 하나인산코데인정이며, 이 밖에 복합제(마이폴캡슐)와 취하된 허가도 있습니다. 허가 건수와 상태는 빠른 개요와 위 표에 있습니다.

<!-- review:begin kr-lic-20261112-codeine-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “전체 7건 중 5건만 표시했습니다. 나머지는 일성코데인정(수출용)과 하나인산코데인정입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-09 데이터) 기준으로 수정했습니다: 허가 11건 중 단일제 7건, 복합제 1건(마이폴캡슐), 취하 3건. 최신 수치는 빠른 개요에 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261112-codeine-1 -->

## 안전성 고려사항

- **약물 상호작용**: 총 449건이 확인되었으며, 주요(Major) 등급은 다음과 같습니다.
  - Alvimopan
  - Bupropion
  - 그 외 중등도(Moderate) 상호작용으로 Atropine, Cimetidine, Dexamethasone, Loperamide, Glycopyrronium, Hyoscyamine 등 항콜린제·위장관 운동 관련 약물이 다수 포함됩니다.
- **지식 그래프상 금기 관련 질환**(허가 문구가 아닌 TxGNN 지식 그래프 기반): 고혈압, 간부전·간질환, 간질, 만성폐쇄성폐질환(COPD), 불안장애, 불면증, 포르피린증, 신장질환, 췌장염, 담낭질환, 혈소판감소증, 갑상선기능저하증, 소화성궤양, 염증성 장질환, 정신병적 장애, 위염 등이 해당됩니다.
- 예측 후보 관련 참고: 소아에서의 호흡억제 및 CYP2D6 초고속 대사자 위험이 사용을 제한할 수 있습니다.

허가사항의 경고 및 금기 본문은 이번 데이터에 포함되어 있지 않으므로 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
비강 질환에 대한 임상시험이 없고, 유일한 문헌도 치료 효과가 아닌 이물 관련 증례입니다. 코데인에는 비강 질환을 치료하는 확립된 기전이 없어, 높은 모델 점수만으로는 진행하기 어렵습니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기·효능효과) 원문 확보 및 파싱
- DrugBank 등에서 상세 작용 기전(MOA) 데이터 확보
- 비강 질환에서 코데인의 치료적 효과를 지지하는 전임상·임상 근거
- 안전성 선별(S1) 단계 진행을 위한 안전성 데이터 보완

---

### 참고: 다른 예측 적응증 (순위 2~4)

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 | 평가 |
|------|-----------|-----------|------|------|
| 3 | 삼차자율신경두통 | 0.9943 | 소아 군발두통 증례군, 코카인 오남용 증례 (치료 효과 근거 없음) | Hold. 군발두통에서 오피오이드는 일반적으로 권장되지 않음 |
| 4 | 알레르기성 두드러기 | 0.9937 | 문헌 다수이나 코데인이 두드러기를 유발·악화시키는 내용 | 방향상 부적합. 코데인은 비만세포 히스타민 유리제로 증상을 악화시킬 수 있음 |

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-24 | 허가 건수: “전체 7건” → 단일제·복합제·취하 허가 구분(건수는 빠른 개요와 위 표) | 정정 (2026-11-24 수정, 이전 판은 기록에 보존) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: codeine sulfate prescribing information, Lannett Company, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5819bdf7-300e-45b8-8f3a-447b53656293) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

