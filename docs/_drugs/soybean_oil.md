---
layout: default
title: Soybean Oil
parent: 모델 예측만 (L5)
nav_order: 701
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Soybean Oil: 예측 신규 적응증 무월경 (Amenorrhea) (근거 수준 L5). 기존 적응증: 비경구 영양요법을 필요로 하는 환자(경구 혹은 위장관 영양공급이 불가능, 불충분 또는 제한되는…"
monitor_inn: "SOYBEAN OIL"
predicted_indications: ["amenorrhea (disease)"]
---

# Soybean Oil
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **1** 건
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

## Soybean Oil: 기존 허가 적응증에서 무월경(Amenorrhea)으로
{: .text-alpha }

## 한 문장 요약

Soybean Oil(대두유)은 한국에서 수액용 유화 주사제(테트라프리피드주)의 성분으로 허가되어 시판 중이나, 허가 적응증 본문은 이번에 정리된 데이터에서 확인되지 않았습니다.
TxGNN 모델은 **무월경(Amenorrhea)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 **임상시험은 0건**, **문헌도 0편**으로 모델 예측 외의 근거가 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 비경구 영양요법을 필요로 하는 환자(경구 혹은 위장관 영양공급이 불가능, 불충분 또는 제한되는 경우)에게에너지와 필수지방산 및 오메가-3 지방산의 공급 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202106173/EE)) |
| 예측 신규 적응증 | 무월경 (Amenorrhea) |
| TxGNN 예측 점수 | 0.9961 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 13건 / 전체 13건) |
| 허가증 수 | 13건 (유효 13건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Soybean Oil 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “정맥 투여된 Nutrilipid 20%는 생물학적으로 이용 가능한 칼로리 및 필수 지방산 공급원을 제공한다. 지방산은 에너지 생성을 위한 중요한 기질로 작용한다. 지방산 대사로부터 유래하는 에너지 생성의 가장 일반적인 작용 기전은 베타 산화이다.” 영어 원문: "Nutrilipid 20% administered intravenously provides biologically utilizable source of calories and essential fatty acids. Fatty acids serve as an important substrate for energy production. The most common mechanism of action for energy production derived from fatty acid metabolism is beta oxidation." ([DailyMed: Nutrilipid I.V. Fat Emulsion (soybean oil) prescribing information, B. Braun Medical Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=193290b1-a0a1-4054-a22a-de5c9e7a8b73), 버전 2026-07-10; 확인일 2026-11-19). 알려진 정보에 따르면 대두유는 비경구 영양 유화액 등에서 지질과 열량, 필수지방산, 식물성 스테롤을 공급하는 성분입니다.

가능한 가설은 두 가지입니다. 첫째, 에너지 부족이나 기능성 시상하부 무월경처럼 영양·에너지 결핍이 원인인 경우 지질 보충이 도움이 될 수 있습니다. 둘째, 식물성 스테롤의 에스트로겐 유사 작용이 시상하부-뇌하수체-난소 축에 영향을 줄 가능성도 있습니다.

다만 두 가설 모두 이번 보고서에 정리된 데이터로 확인되지 않았습니다. 무월경은 시상하부, 뇌하수체, 난소, 해부학적 원인 등 원인이 다양하여, 이번 예측을 특정 병인에 대응시킬 수 없습니다. 기존 적응증과의 유사성 평가도 아직 이루어지지 않았습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 202106173 | 테트라프리피드주 | 수액용 플라스틱 용기에 들어있는 유백색의 균질한 유화액 | 대한약품공업(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202106173/EE) | 유효 |

위 표는 허가 13건 중 1건입니다.

<!-- licenses:end -->

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. 약물 상호작용 조회에서도 확인된 항목이 없었습니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
근거는 TxGNN의 높은 예측 점수(0.9961)뿐이며, 임상시험과 문헌이 모두 없어 근거 수준이 L5입니다. 작용 기전과 허가 안전성 정보도 확인되지 않아 현 단계에서는 진행을 권고하기 어렵습니다.

**진행하려면 필요한 것:**
- 허가 문서(MFDS 첨부문서)에서 적응증, 경고, 금기 정보 확보 (안전성 검토의 선결 조건)
- DrugBank 등에서 작용 기전 데이터 확보
- 무월경 관련 임상시험 및 문헌 탐색 (특히 에너지 결핍성 무월경 대상)
- 무월경의 세부 병인별로 기전 가설 검증
- 투여 경로 적합성 평가: 현재 제품은 정맥 수액 제제이므로, 무월경 치료에 적합한지 검토 필요

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Nutrilipid I.V. Fat Emulsion (soybean oil) prescribing information, B. Braun Medical Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=193290b1-a0a1-4054-a22a-de5c9e7a8b73) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

