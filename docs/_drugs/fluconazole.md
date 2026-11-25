---
layout: default
title: Fluconazole
parent: 모델 예측만 (L5)
nav_order: 352
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Fluconazole: 예측 신규 적응증 점상 상피성 각결막염 (Punctate Epithelial Keratoconjunctivitis) (근거 수준 L5). 기존 적응증: 허가 적응증 본문은 이번 데이터에 포함되지 않음 (허가사항 참조)"
monitor_inn: "FLUCONAZOLE"
predicted_indications: ["punctate epithelial keratoconjunctivitis"]
---

# Fluconazole
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

## Fluconazole: 진균 감염에서 점상 상피성 각결막염으로
{: .text-alpha }

## 한 문장 요약

Fluconazole은 트리아졸 계열 항진균제로, 한국에서 진균 감염 치료에 사용되고 있습니다.
TxGNN 모델은 **점상 상피성 각결막염(Punctate Epithelial Keratoconjunctivitis)**에 효과가 있을 수 있다고 예측합니다.
다만 이 예측을 지지하는 **임상시험은 0건**, **문헌도 0편**이어서 현재는 모델 예측만 있는 상태입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문은 이번 데이터에 포함되지 않음 (허가사항 참조) |
| 예측 신규 적응증 | 점상 상피성 각결막염 (Punctate Epithelial Keratoconjunctivitis) |
| TxGNN 예측 점수 | 0.9924 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Fluconazole 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “플루코나졸은 진균의 시토크롬 P450 의존성 효소인 라노스테롤 14-α-탈메틸효소의 고도로 선택적인 억제제이다. 이 효소는 라노스테롤을 에르고스테롤로 전환하는 기능을 한다. 그에 따른 정상 스테롤의 소실은 진균 내 14-α-메틸 스테롤의 축적과 상관관계가 있으며, 플루코나졸의 정진균 활성의 원인일 수 있다.” 영어 원문: "Fluconazole is a highly selective inhibitor of fungal cytochrome P450 dependent enzyme lanosterol 14-α-demethylase. This enzyme functions to convert lanosterol to ergosterol. The subsequent loss of normal sterols correlates with the accumulation of 14-α-methyl sterols in fungi and may be responsible for the fungistatic activity of fluconazole." ([DailyMed: Diflucan (fluconazole) prescribing information, Roerig](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f694c617-3383-416c-91b6-b94fda371204), 버전 2026-04-02; 확인일 2026-11-19). 알려진 정보에 따르면 fluconazole은 트리아졸 계열 항진균제로, 진균의 lanosterol 14-alpha-demethylase(CYP51)를 억제해 에르고스테롤 합성을 차단합니다.

점상 상피성 각결막염은 대개 바이러스(예: 아데노바이러스), 안구건조, 약물 독성 등 비진균성 원인과 관련됩니다. 이런 경우 항진균제를 쓸 기전적 근거가 뚜렷하지 않습니다. 진균성 원인이나 이차 감염 성분이 있다면 연결 고리가 될 수 있지만, 이는 추정에 불과합니다.

따라서 높은 예측 점수는 TxGNN 모델(딥러닝)에서 나온 것이며, 모델이 관련 질환 사이에서 학습한 유사성을 반영했을 수 있을 뿐 생물학적 근거는 아닙니다. 기전 연관성은 현재 가설 수준입니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 200400359 | 한올플루코나졸캡슐 | 백색 내지 유백색의 분말을 함유하는 상부-청록색, 하부-미백색의 경질캡슐… | 한올바이오파마(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200400359/EE) | 유효 |
| 201400853 | 플루졸캡슐(플루코나졸) | 흰색의 분말이 든 상부 파란색, 하부 흰색의 경질캡슐제 | 알리코제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201400853/EE) | 유효 |
| 200403937 | 푸졸캡슐(플루코나졸)(수출명:NewfuconacCap.) | 백색분말이 충진된 상부 담청색, 하부 백색의 캡슐제 | 대한뉴팜(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200403937/EE) | 유효 |
| 201300893 | 푸로날캡슐(플루코나졸) | 백색 분말이 충진된 상부 청색, 하부 백색의 경질캡슐 | 삼성제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201300893/EE) | 유효 |
| 200202782 | 플로졸캡슐(플루코나졸) | 흰색의 분말이 든 상부 파란색, 하부 흰색의 경질캡슐제 | 알보젠코리아(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200202782/EE) | 유효 |

위 표는 허가 최소 20건 중 5건입니다.

<!-- licenses:end -->

허가 건수와 상태는 빠른 개요와 위 표에 있습니다. 위 표는 주요 5건만 나열한 것입니다.

<!-- review:begin kr-lic-20261124c-fluconazole-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “전체 20건이 모두 단일 성분 제제로 유효하며, 취소된 허가는 없습니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 단일·복합 표기와 건수를 본문에 고정해 쓰지 않고, 매주 갱신되는 허가 자료를 반영하는 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 2026-11-25에 식품의약품안전처 품목허가 상세 자료(2026-03)의 주성분명으로 품목별로 다시 확인한 결과, 이 자료에 수록된 허가 품목은 모두 단일 성분 제제입니다. 이 자료에는 허가의 일부만 수록되어 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-fluconazole-1 -->

## 안전성 고려사항

- **지식 그래프상 금기 관련 질환**: QT 연장 증후군, 가족성 QT 연장 증후군, 신장 질환, 요관농양, 간 질환, 담낭 질환 (허가사항 문구가 아니라 지식 그래프의 약물-질환 금기 관계에서 가져온 정보)
- **약물 상호작용**: 총 100건이 확인되었으며, 일부는 다음과 같습니다.
  - **주요(Major)**: Chlorpropamide
  - **중등도(Moderate)**: Famotidine, Rabeprazole, Omeprazole, Dexlansoprazole, Hydrocortisone, Dexamethasone, Betamethasone, Triamcinolone, Budesonide, Loperamide, Aprepitant, Bisacodyl, Saxagliptin
  - **경미(Minor)**: Amphotericin B, Clarithromycin

허가사항의 경고 및 금기 항목은 별도로 확인해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 매우 높지만 임상시험과 문헌이 전혀 없고(근거 수준 L5), 비진균성이 많은 질환 특성상 기전적 근거도 약합니다. 현재 단계에서 진행을 권장하기 어렵습니다.

**진행하려면 필요한 것:**
- 점상 상피성 각결막염에서 진균 원인이나 이차 진균 감염이 관여하는지 확인하는 기전 및 문헌 검토
- 작용 기전(MOA) 데이터 보완
- 허가사항의 경고·금기 및 허가 적응증 확인
- 안과 투여 경로(국소 점안 등) 적합성 평가. 현재 한국 허가 제형은 경구 캡슐과 정제뿐입니다.
- 관련 임상시험이나 전임상 연구 근거 확보

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Diflucan (fluconazole) prescribing information, Roerig](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f694c617-3383-416c-91b6-b94fda371204) |
| 2026-11-24 | 단일·복합 표기: “전체 20건이 모두 단일 성분 제제로 유효하며, 취소된 허가는 없습니다.” → 고정된 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 (2026-11-25 수정, 이전 판은 기록에 보존) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

