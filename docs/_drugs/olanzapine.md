---
layout: default
title: Olanzapine
parent: 모델 예측만 (L5)
nav_order: 560
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Olanzapine: 예측 신규 적응증 영아 양성 발작성 사경 (Benign paroxysmal torticollis of infancy) (근거 수준 L5). 기존 적응증: 1. 조현병 2. 양극성장애 - 양극성장애 1형과 관련된 조증 및 혼재삽화의 치료 - 올란자핀 투여로…"
monitor_inn: "OLANZAPINE"
predicted_indications: ["benign paroxysmal torticollis of infancy", "agoraphobia"]
---

# Olanzapine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **2** 건
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

## Olanzapine: 정신과 질환에서 영아 양성 발작성 사경으로
{: .text-alpha }

## 한 문장 요약

Olanzapine은 한국에서 허가된 비정형 항정신병 약물입니다(허가 건수와 상태는 빠른 개요 참조). TxGNN 모델은 예측 점수가 가장 높은 **영아 양성 발작성 사경(Benign paroxysmal torticollis of infancy)**을 1순위로 예측했지만, 이 예측을 지지하는 임상시험과 문헌은 없습니다. 반면 2순위인 **광장공포증(Agoraphobia)**은 **6편의 문헌**(임상시험 0건)이 간접적으로 뒷받침하여, 이 보고서는 광장공포증을 중심으로 평가합니다.

<!-- review:begin kr-lic-20261124c-olanzapine-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “Olanzapine은 한국에서 단일 성분제로 20건이 허가된 비정형 항정신병 약물입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 단일·복합 표기와 건수를 본문에 고정해 쓰지 않고, 매주 갱신되는 허가 자료를 반영하는 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 2026-11-25에 식품의약품안전처 품목허가 상세 자료(2026-03)의 주성분명으로 품목별로 다시 확인한 결과, 이 자료에 수록된 허가 품목은 모두 단일 성분 제제입니다. 이 자료에는 허가의 일부만 수록되어 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-olanzapine-1 -->

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 조현병 2. 양극성장애 - 양극성장애 1형과 관련된 조증 및 혼재삽화의 치료 - 올란자핀 투여로 조증삽화에 반응을 보인 환자들에 있어서 양극성 장애의 재발방지 - 양극성장애 1형과 관련된 우울삽화의 급성 치료 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201507969/EE)) |
| 예측 신규 적응증 (1순위) | 영아 양성 발작성 사경 (Benign paroxysmal torticollis of infancy) |
| TxGNN 예측 점수 (1순위) | 0.9954 |
| 근거 수준 (1순위) | L5 |
| 권장 결정 (1순위) | Hold |
| 주요 검토 대상 (2순위) | 광장공포증 (Agoraphobia), 예측 점수 0.9947, 근거 수준 L3, 권장 결정 Research Question |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |

> 1순위 예측은 근거가 전혀 없어 보류하며, 이하 임상시험·문헌 근거는 근거가 있는 2순위(광장공포증)를 기준으로 정리합니다.

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Olanzapine 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “기재된 적응증에서 올란자핀의 작용기전은 명확하지 않다. 그러나 조현병에서 올란자핀의 효능은 도파민 및 세로토닌 제2형(5HT 2 ) 길항 작용의 조합을 통해 매개될 수 있다.” 영어 원문: "The mechanism of action of olanzapine, in the listed indications, is unclear. However, the efficacy of olanzapine in schizophrenia could be mediated through a combination of dopamine and serotonin type 2 (5HT 2 ) antagonism." ([DailyMed: Weltruza (olanzapine) prescribing information, Teva Pharmaceuticals USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a23e99c7-fb76-46d2-95af-e03d5a4d1f2c), 버전 2026-10-26; 확인일 2026-11-19). 알려진 정보에 따르면 Olanzapine은 도파민 D2 및 세로토닌 5-HT2A/5-HT2C 수용체를 차단하는 비정형 항정신병 약물입니다. 이 수용체 차단 작용이 불안 회로에 영향을 줄 수 있어, 기전상 불안 관련 질환에도 적용 가능할 수 있습니다.

**광장공포증(2순위):** 공황장애는 광장공포증과 함께 나타나는 경우가 많습니다. SSRI에 반응하지 않는 공황장애 환자에게 Olanzapine을 추가하는 방식이 소규모 연구에서 검토되었습니다. 다만 광장공포증 자체를 대상으로 한 연구는 없고, 근거는 모두 공황장애에 관한 것입니다. 또한 대사 이상과 진정 작용 같은 부작용이 있고 1차 치료 옵션(SSRI, SNRI, 인지행동치료)이 이미 있어 사용에 제약이 있습니다.

**영아 양성 발작성 사경(1순위):** 편두통 스펙트럼 및 이온채널 이상(예: CACNA1A)과 관련된 드물고 저절로 호전되는 소아 질환입니다. Olanzapine의 수용체 차단 작용과 이 질환 사이에 확립된 연관성은 없습니다. 양성 경과를 보이는 영아에게 항정신병약을 쓰는 것은 위험 대비 이익 측면에서 큰 우려가 있습니다.

**기분부전장애(3순위):** Olanzapine은 우울증에서 보조 요법(예: fluoxetine 병용)으로 사용되며, 5-HT2C 차단을 통한 전전두엽 도파민·노르에피네프린 탈억제가 근거로 제시됩니다. 다만 근거는 항정신병약 계열 전체에 대한 간접 근거입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

광장공포증 관련 문헌입니다 (연구 설계 및 직접 관련성 순).

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [16415705](https://pubmed.ncbi.nlm.nih.gov/16415705/) | 2006 | 공개 라벨 시험 | J Clin Psychopharmacol | SSRI 저항성 공황장애(광장공포증 동반 여부 무관) 성인 31명에게 Olanzapine 5 mg/일을 12주간 추가 투여한 시험 |
| [15470803](https://pubmed.ncbi.nlm.nih.gov/15470803/) | 2004 | 증례 보고 | Pharmacopsychiatry | Olanzapine과 paroxetine 병용 후 공황장애가 완전 관해된 1례 |
| [10739446](https://pubmed.ncbi.nlm.nih.gov/10739446/) | 2000 | 증례 보고 | Am J Psychiatry | Olanzapine과 공황 발작에 관한 증례 보고 |
| [26635099](https://pubmed.ncbi.nlm.nih.gov/26635099/) | 2016 | 체계적 문헌고찰 | Expert Opin Pharmacother | 치료 저항성 공황장애 치료 현황. 환자 약 1/3은 치료 후에도 공황 발작이 지속됨 |
| [40946318](https://pubmed.ncbi.nlm.nih.gov/40946318/) | 2026 | 체계적 문헌고찰 | Psychother Psychosom | 치료 저항성 불안장애의 약물·정신요법·신경자극 치료 옵션 종합 검토 |
| [25012437](https://pubmed.ncbi.nlm.nih.gov/25012437/) | 2014 | 코호트 | J Affect Disord | 동반 불안장애(광장공포증 포함)가 양극성 장애 I형 24개월 임상 경과에 미치는 영향 |

## 한국 시판 정보

허가증 20건 중 주요 5건입니다. 허가 적응증은 허가 문서 링크만 확인되어 본문은 기재하지 못했습니다.

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201507969 | 테바올란자핀정15밀리그램 | 연한 파란색의 양면이 볼록한 타원형 필름코팅정제 | (주)한독테바 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201507969/EE) | 유효 |
| 201006443 | 에이프렉사정5밀리그램(올란자핀) | 흰색의 원형 필름코팅정 | 에이치케이이노엔(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201006443/EE) | 유효 |
| 200903065 | 산도스올란자핀정10밀리그램 | 흰색의 원형 필름코팅 정제 | 삼일제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200903065/EE) | 유효 |
| 201101853 | 올자핀정10밀리그램(올란자핀) | 흰색의 원형 필름코팅정 | 동화약품(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201101853/EE) | 유효 |
| 202400668 | 자이프렉사정5밀리그램(올란자핀) | 필름코팅된 백색의 원형정제 | (주)보령 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202400668/EE) | 유효 |

위 표는 허가 최소 20건 중 5건입니다.

<!-- licenses:end -->

## 안전성 고려사항

허가사항의 경고·금기 정보는 확인되지 않았으므로 허가사항을 참조하세요.

- **지식 그래프상 금기 관련 질환:** 간부전·간질환·간경변, 당뇨병·고혈당·당뇨병성 케톤산증, 고지혈증·고중성지방혈증, 비만, 호중구감소증·무과립구증, 기립성 저혈압, 뇌졸중·뇌경색, 심근경색, 간질(뇌전증), 양성 전립선 비대증, 유방암 등이 연관되어 있습니다. 이는 허가 문구가 아니라 지식 그래프 기반 정보이므로 참고용입니다.
- **약물 상호작용:** 조회된 상호작용은 100건이며, 그중 **중대(Major)** 수준은 다음과 같습니다.
  - Bupropion
  - Morphine
  - Potassium citrate
- 그 밖에 Acarbose, Famotidine, Epinephrine, Metformin, Clarithromycin, Atropine, 여러 당뇨병 치료제 등 **중등도(Moderate)** 상호작용이 다수 확인되었습니다.

## 결론 및 다음 단계

**결정: 1순위(영아 양성 발작성 사경) Hold / 2순위(광장공포증)·3순위(기분부전장애) Research Question 단계**

**사유:**
- 1순위 예측은 TxGNN 모델(딥러닝)의 점수만 있고(이 점수는 모델이 관련 질환 사이에서 학습한 유사성을 반영할 수 있으며, 생물학적 근거는 아닙니다) 임상시험과 문헌이 없으며, 영아에게 항정신병약을 쓰는 위험 대비 이익 우려가 커서 보류합니다.
- 광장공포증은 공황장애 증강 요법에 대한 소규모 공개 라벨 시험과 증례 보고만 있어 연구 질문 단계(L3)입니다.

**진행하려면 필요한 것:**
- 허가사항(MFDS)의 경고·금기 정보 확보 (현재 안전성 심사를 진행할 수 없는 차단 수준의 데이터 공백)
- 상세한 작용 기전(MOA) 데이터 확보 (DrugBank 조회)
- 광장공포증 또는 공황장애에서 Olanzapine 증강 요법의 무작위 대조 시험 및 임상시험 등록 근거
- 대사 및 진정 관련 부작용을 고려한 위험·이익 평가와 1차 치료(SSRI, SNRI, 인지행동치료)와의 비교
- 기분부전장애에 대해서는 해당 질환에 특화된 근거

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Weltruza (olanzapine) prescribing information, Teva Pharmaceuticals USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a23e99c7-fb76-46d2-95af-e03d5a4d1f2c) |
| 2026-11-24 | 단일·복합 표기: “Olanzapine은 한국에서 단일 성분제로 20건이 허가된 비정형 항정…” → 고정된 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 (2026-11-25 수정, 이전 판은 기록에 보존) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

