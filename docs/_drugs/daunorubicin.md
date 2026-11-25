---
layout: default
title: Daunorubicin
parent: 모델 예측만 (L5)
nav_order: 254
evidence_level: L5
indication_count: 10
monitor_inn: "Daunorubicin"
predicted_indications: ["Hodgkins lymphoma", "vertebral anomalies and variable endocrine and T-cell dysfunction", "ganglioneuroblastoma (disease)", "neuroblastoma", "ALK-positive large B-cell lymphoma", "adenosarcoma", "retroperitoneal neoplasm", "small cell lung carcinoma", "primary pulmonary lymphoma", "pulmonary blastoma"]
last_modified_at: 2026-11-24
description: "Daunorubicin: 예측 신규 적응증 호지킨 림프종 (근거 수준 L5). 기존 적응증: 급성 백혈병(만성 골수성 백혈병의 급성 전환 포함)"
---

# Daunorubicin
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

## Daunorubicin: 허가 적응증 정보 확인 불가 상태에서 호지킨 림프종으로
{: .text-alpha }

## 한 문장 요약

Daunorubicin은 안트라사이클린 계열의 항암제로, 한국에서 주사제 허가증이 확인됩니다(허가 건수와 상태는 빠른 개요 참조). 다만 허가 적응증 본문은 이번 자료에 담기지 않았습니다.
TxGNN 모델은 **호지킨 림프종(Hodgkin's lymphoma)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 다룬 임상시험이나 문헌은 확인되지 않았습니다. 현재 근거는 모델 예측 수준입니다.

<!-- review:begin kr-lic-20261124c-daunorubicin-2 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “Daunorubicin은 안트라사이클린 계열의 항암제로, 한국에서 단일 성분 주사제 3건의 허가증이 확인됩니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 단일·복합 표기와 건수를 본문에 고정해 쓰지 않고, 매주 갱신되는 허가 자료를 반영하는 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 2026-11-25에 식품의약품안전처 품목허가 상세 자료(2026-03)의 주성분명으로 품목별로 다시 확인한 결과, 이 자료에 수록된 허가 품목에는 단일 성분 제제와 복합 성분 제제가 함께 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-daunorubicin-2 -->

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 급성 백혈병(만성 골수성 백혈병의 급성 전환 포함) ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202400632/EE)) |
| 예측 신규 적응증 | 호지킨 림프종 |
| TxGNN 예측 점수 | 0.9981 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 4건 / 전체 4건) |
| 허가증 수 | 4건 (유효 4건) |
| 권장 결정 | Hold |

근거 수준을 L5로 판정한 이유는 다음과 같습니다. 호지킨 림프종 항목의 임상시험 2건은 비호지킨 림프종 또는 급성 B림프모구성 백혈병을 다룹니다. 문헌 중 호지킨 림프종을 언급한 자료는 안트라사이클린 전반을 다룬 리뷰와 혈액종양 총설이며, daunorubicin의 호지킨 림프종 효능을 직접 연구한 자료는 없습니다.

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Daunorubicin 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “다우노루비신은 제안된 여러 작용기전을 통해 항유사분열 및 세포독성 활성을 나타낸다. 다우노루비신은 염기쌍 사이에 삽입되어 DNA와 복합체를 형성한다. 다우노루비신은 DNA-topoisomerase II 복합체를 안정화하여 topoisomerase II가 촉매하는 결찰-재결찰 반응 중 재결찰 단계를 저해함으로써 topoisomerase II 활성을 억제한다.” 영어 원문: "Daunorubicin has antimitotic and cytotoxic activity through a number of proposed mechanisms of action. Daunorubicin forms complexes with DNA by intercalation between base pairs. It inhibits topoisomerase II activity by stabilizing the DNA-topoisomerase II complex, preventing the religation portion of the ligation-religation reaction that topoisomerase II catalyzes." ([DailyMed: daunorubicin hydrochloride prescribing information, Meitheal Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ff6b9bd4-8a9f-400f-a0b9-70e25fa8a28f), 버전 2025-05-21; 확인일 2026-11-19). 일반적으로 daunorubicin은 DNA에 삽입(intercalation)되고 topoisomerase II를 억제하는 안트라사이클린으로 알려져 있습니다. 이 기전은 호지킨 림프종의 표준 요법인 ABVD에 포함된 doxorubicin과 같은 계열의 것입니다.

따라서 기전상 호지킨 림프종에 적용될 가능성은 있습니다. 그러나 이는 계열 수준의 추론입니다. 제공된 임상시험과 문헌에서 daunorubicin 자체의 호지킨 림프종 효능은 확인되지 않았습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00002471](https://clinicaltrials.gov/study/NCT00002471) | Phase 2 | 완료 | 정보 없음 | 고위험 비림프모구성 림프종 및 급성 B림프모구성 백혈병, 재발성 비호지킨 림프종에 대한 집중 단기 병용화학요법 시험. 호지킨 림프종 대상 여부와 daunorubicin의 역할은 확인 불가 |
| [NCT00002691](https://clinicaltrials.gov/study/NCT00002691) | Phase 2 | 완료 | 정보 없음 | 소아·청소년 진행성 비호지킨 림프종 LSA5 프로토콜. 호지킨 림프종과 다른 질환이라 간접 근거에 그침 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [30231396](https://pubmed.ncbi.nlm.nih.gov/30231396/) | 2018 | Review | ASCO Educational Book | 안트라사이클린(daunorubicin 포함)이 소아 호지킨 림프종 등의 요법의 근간이며, 심장독성이 임상 사용의 제약이라는 내용 |
| [14584273](https://pubmed.ncbi.nlm.nih.gov/14584273/) | 2003 | 총설 | Gan to Kagaku Ryoho | 진행성 호지킨 림프종의 1차 요법은 ABVD라는 내용. daunorubicin 자체의 효능 자료는 아님 |
| [10410671](https://pubmed.ncbi.nlm.nih.gov/10410671/) | 1999 | 총설 | Gan to Kagaku Ryoho | 혈액종양 치료 개요. 진행성 호지킨 림프종 표준요법 언급 |
| [17610809](https://pubmed.ncbi.nlm.nih.gov/17610809/) | 2007 | 체계적 문헌고찰 | Health Technol Assess | 소아 암 환자의 안트라사이클린 심장독성에 대한 심장보호 방법 평가 |
| [9387047](https://pubmed.ncbi.nlm.nih.gov/9387047/) | 1997 | 임상시험 | Invest New Drugs | 재발·불응성 림프종 19명에 리포좀 daunorubicin 투여. 고용량군에서 완전반응 1명, 부분반응 일부 관찰 (비호지킨 림프종 중심) |
| [11699226](https://pubmed.ncbi.nlm.nih.gov/11699226/) | 2001 | 임상시험 | Leuk Lymphoma | 예후 불량 비호지킨 림프종에서 리포좀 daunorubicin 병용요법(COP-X) 시행. 평가 가능 32명 중 81% 반응 |

위 문헌은 대부분 비호지킨 림프종이나 안트라사이클린 일반을 다룹니다. 호지킨 림프종에서 daunorubicin 효능을 직접 입증한 문헌은 없습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 202400632 | 다우노신주20밀리그램(다우노루비신염산염) | 빨간색의 동결건조분말이 무색투명한 바이알에 든 주사제(첨부용제 : 무색의… | 한국유나이티드제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202400632/EE) | 유효 |
| 201309135 | 주사용다우노마이신20밀리그램(다우노루비신염산염)(수출용) | 빨간색의 결정 또는 가루가 든 무색투명한 바이알 | 동아에스티(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201309135/EE) | 유효 |
| 199801567 | 다우노신주(다우노루비신염산염)(수출용) | 적색의 동결건조분말이 든 바이알(첨부용제 : 투명한 용액이 든 앰플 또는… | 한국유나이티드제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199801567/EE) | 유효 |

위 표는 허가 4건 중 3건입니다.

<!-- licenses:end -->

허가증 목록은 위 표에 있습니다. 이 중 2건은 수출용입니다. 허가 상태는 빠른 개요와 위 표에 있습니다.

<!-- review:begin kr-lic-20261124b-daunorubicin-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “시판 현황은 취소 여부 정보가 없어 확인할 수 없습니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 허가 상태(유효·취소)는 자료에 있으며 빠른 개요와 표에 표시됩니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124b-daunorubicin-1 -->

<!-- review:begin kr-lic-20261124c-daunorubicin-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “허가증 3건은 모두 단일 성분이며 유효 상태입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 단일·복합 표기와 건수를 본문에 고정해 쓰지 않고, 매주 갱신되는 허가 자료를 반영하는 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 2026-11-25에 식품의약품안전처 품목허가 상세 자료(2026-03)의 주성분명으로 품목별로 다시 확인한 결과, 이 자료에 수록된 허가 품목에는 단일 성분 제제와 복합 성분 제제가 함께 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-daunorubicin-1 -->

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (안트라사이클린 계열) |
| 골수억제 위험 | 고 (일반적으로 안트라사이클린 계열의 주요 독성) |
| 구토 유발성 등급 | 중 |
| 모니터링 항목 | CBC (분류 포함), 간·신기능, 심기능 (누적 용량에 따른 심장독성) |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

허가사항의 경고 및 주의사항을 참조하세요. 위 내용은 약물 계열의 일반 지식에 근거하며, 이번 자료에는 독성 데이터가 포함되어 있지 않습니다.

## 안전성 고려사항

**약물 상호작용**: 상호작용 100건이 조회되었으며, 아래는 일부입니다.
- **Major**: Cisapride, Dolasetron, Papaverine, Deferiprone, Macimorelin
- **Moderate**: Famotidine, Loperamide, Clarithromycin, Ondansetron, Granisetron, Palonosetron, Levofloxacin, Eliglustat, Rolapitant, Palifermin 등
- **Minor**: Metronidazole

주요 경고와 금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
호지킨 림프종에 대한 TxGNN 점수는 높지만, daunorubicin의 호지킨 림프종 효능을 직접 연구한 임상시험이나 문헌이 없어 근거가 모델 예측 수준(L5)에 머뭅니다. 허가 적응증과 안전성 정보도 확인되지 않은 상태입니다.

**진행하려면 필요한 것:**
- 식약처 허가사항(첨부문서)에서 허가 적응증, 경고, 금기 확보
- 작용 기전 데이터 확보 (DrugBank 등)
- 호지킨 림프종에서 daunorubicin을 직접 평가한 임상시험 또는 문헌 탐색
- NCT00002471의 대상 집단과 daunorubicin 포함 여부 확인
- 한국 시판 및 허가 유지 여부 확인

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: daunorubicin hydrochloride prescribing information, Meitheal Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ff6b9bd4-8a9f-400f-a0b9-70e25fa8a28f) |
| 2026-11-24 | 허가 상태: “시판 현황은 취소 여부 정보가 없어 확인할 수 없습니다.” → 자료 기준으로 수정 | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |
| 2026-11-24 | 단일·복합 표기: “허가증 3건은 모두 단일 성분이며 유효 상태입니다.” → 고정된 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 (2026-11-25 수정, 이전 판은 기록에 보존) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |
| 2026-11-24 | 단일·복합 표기: “Daunorubicin은 안트라사이클린 계열의 항암제로, 한국에서 단일 …” → 고정된 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 (2026-11-25 수정, 이전 판은 기록에 보존) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

