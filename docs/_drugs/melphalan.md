---
layout: default
title: Melphalan
parent: 모델 예측만 (L5)
nav_order: 500
evidence_level: L5
indication_count: 5
monitor_inn: "Melphalan"
predicted_indications: ["rectum mucinous adenocarcinoma", "colon mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma", "cervical mucinous adenocarcinoma", "endometrial mucinous adenocarcinoma"]
last_modified_at: 2026-11-24
description: "Melphalan: 예측 신규 적응증 직장 점액성 선암 (근거 수준 L5). 기존 적응증: 1. 다발성골수종 2. 난소선암 3. 진행성유방암 4. 진성적혈구증가증 (주사제) 다발성골수종"
---

# Melphalan
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

## Melphalan: 허가 적응증에서 직장 점액성 선암으로
{: .text-alpha }

## 한 문장 요약

Melphalan은 한국에서 주사제와 정제 허가를 보유한 알킬화 항종양제입니다(허가 건수와 상태는 빠른 개요 참조). 다만 이번 데이터에서는 허가 적응증의 구체적인 문구를 확인할 수 없었습니다.
TxGNN 모델은 **직장 점액성 선암(rectum mucinous adenocarcinoma)**에 효과가 있을 수 있다고 예측합니다.
그러나 현재 이 예측을 직접 뒷받침하는 **임상시험은 0건, 문헌도 0건**이며, 모델 예측 점수만 있는 상태입니다.

<!-- review:begin kr-lic-20261124c-melphalan-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “Melphalan은 한국에서 3건의 단일 성분 허가(주사제 2건, 정제 1건)를 보유한 알킬화 항종양제입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 단일·복합 표기와 건수를 본문에 고정해 쓰지 않고, 매주 갱신되는 허가 자료를 반영하는 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 2026-11-25에 식품의약품안전처 품목허가 상세 자료(2026-03)의 주성분명으로 품목별로 다시 확인한 결과, 이 자료에 수록된 허가 품목은 모두 단일 성분 제제입니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-melphalan-1 -->

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 다발성골수종 2. 난소선암 3. 진행성유방암 4. 진성적혈구증가증 (주사제) 다발성골수종 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200307781/EE)) |
| 예측 신규 적응증 | 직장 점액성 선암 |
| TxGNN 예측 점수 | 0.9938 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 3건) |
| 허가증 수 | 3건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Melphalan 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “Melphalan은 bischloroethylamine 계열의 알킬화제이다. 그 결과, 이 약물의 세포독성은 아마도 구아닌의 N 7 위치에 결합함으로써 일어나는 DNA와의 가닥 간 교차결합의 정도와 관련이 있는 것으로 보인다.” 영어 원문: "Melphalan is an alkylating agent of the bischloroethylamine type. As a result, its cytotoxicity appears to be related to the extent of its interstrand cross-linking with DNA, probably by binding at the N 7 position of guanine." ([DailyMed: Evomela (melphalan) prescribing information, Acrotech Biopharma Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=69f55869-dc11-408e-8fc7-47634269a52c), 버전 2026-09-15; 확인일 2026-11-19). 일반적으로 melphalan은 이중 기능성 질소 머스타드 계열의 알킬화제로, DNA 가닥 간 교차결합을 형성해 증식하는 세포를 억제하는 것으로 알려져 있습니다. 이 기전은 선암 세포에도 이론적으로 작용할 수 있습니다.

그러나 이 연관성은 검증되지 않았습니다. 직장 점액성 선암과 melphalan을 직접 연결하는 시험이나 문헌이 제공되지 않았고, 근거는 TxGNN 점수(0.9938)뿐입니다. 또한 점액성 조직형은 일반적으로 화학요법에 대한 반응이 떨어지는 경향이 있어, 세포독성이라는 일반적 근거만으로는 기대 효과가 강하다고 보기 어렵습니다.

같은 모델이 예측한 다른 후보도 근거 수준이 동일합니다(모두 L5, Hold).

| 순위 | 예측 질환 | TxGNN 점수 |
|------|----------|-----------|
| 2 | 결장 점액성 선암 | 0.9936 |
| 3 | 담낭 점액성 선암 | 0.9929 |
| 4 | 자궁경부 점액성 선암 | 0.9927 |
| 5 | 자궁내막 점액성 선암 | 0.9926 |

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 202106448 | 멜스팔주50밀리그램(멜팔란염산염) | 1) 주성분 바이알 : 흰색 또는 연한노란색의 동결건조 분말이 무색투명한… | 위너마크팜 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202106448/EE) | 유효기간만료 |
| 202000405 | 메그발주50밀리그램(멜팔란염산염) | 1) 주성분 바이알 : 흰색 내지 연한노란색의 동결건조 분말이 무색투명한… | (주)에이스파마 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202000405/EE) | 유효 |
| 200307781 | 알케란정(멜팔란) | 흰색-회백색의 양면이 볼록한 원형 필름코팅정 | 삼일제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200307781/EE) | 유효 |

<!-- licenses:end -->

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (알킬화제, 질소 머스타드 계열) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 (일반적으로 CBC, 간·신기능 확인) |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

## 안전성 고려사항

- **약물 상호작용**: 이번 조회에서 총 100건이 확인되었으며, 그중 일부를 아래에 정리합니다.
  - 중등도: Amphotericin B 및 그 지질 제제(지질 복합체, 콜레스테릴 설페이트, 리포좀형)
  - 경미: Cimetidine, Levofloxacin, 황산아연, 글루콘산아연
  - 등급 미상: Lansoprazole, Omeprazole, Pantoprazole, Famotidine, Metformin, Prednisone, Simvastatin 등

주요 경고와 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
직장 점액성 선암에 대한 임상시험과 문헌이 없고 TxGNN 예측 점수만 있어 근거 수준이 L5입니다. 작용 기전과 허가 적응증 문구도 확인되지 않아 현 단계에서 진행할 근거가 부족합니다.

**진행하려면 필요한 것:**
- 허가 문서(첨부문서)의 경고·금기·적응증 확인 (현재 안전성 검토를 진행할 수 없는 상태)
- 상세한 작용 기전(MOA) 데이터 확보
- 직장·결장 점액성 선암에 대한 전임상 또는 임상 근거 탐색
- 점액성 조직형의 화학요법 저항성을 고려한 기존 표준요법 대비 이점 검토
- 투여 경로(주사/경구) 적합성 평가

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Evomela (melphalan) prescribing information, Acrotech Biopharma Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=69f55869-dc11-408e-8fc7-47634269a52c) |
| 2026-11-24 | 단일·복합 표기: “Melphalan은 한국에서 3건의 단일 성분 허가(주사제 2건, 정제 …” → 고정된 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 (2026-11-25 수정, 이전 판은 기록에 보존) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

