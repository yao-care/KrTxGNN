---
layout: default
title: Fluticasone
parent: 모델 예측만 (L5)
nav_order: 362
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
description: "Fluticasone: 예측 신규 적응증 편두통 (migraine disorder) (근거 수준 L5). 기존 적응증: 1. 기관지 천식 1) 성인 : 다음 경우에 있어서의 천식의 예방적 치료 (1) 경증 천식(PEF 80%…"
monitor_inn: "fluticasone"
predicted_indications: ["migraine disorder", "Prinzmetal angina", "migraine with brainstem aura"]
---

# Fluticasone
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

## Fluticasone: 허가 적응증 정보 미확인 상태에서 편두통으로
{: .text-alpha }

## 한 문장 요약

Fluticasone은 흡입제 및 비강 분무제로 한국에서 시판 중인 글루코코르티코이드 계열 약물입니다. 허가 적응증 본문은 이 보고서에 사용된 데이터에 포함되어 있지 않습니다.
TxGNN 모델은 **편두통(migraine disorder)**에 효과가 있을 수 있다고 예측하지만, 현재 **임상시험은 0건**이고 연결된 문헌 **1편**도 효능이 아닌 이상반응을 다룬 리뷰입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 기관지 천식 1) 성인 : 다음 경우에 있어서의 천식의 예방적 치료 (1) 경증 천식(PEF 80% 초과) 일상생활 속에서 간헐적으로 기관지확장제 투여가 필요한 환자 (2) 중등도 천식(PEF 60∼80%) 정기적인 천식치료를 필요로 하는 경우 현행 예방적 치료나 기관지확장제… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200307778/EE)) |
| 예측 신규 적응증 | 편두통 (migraine disorder) |
| TxGNN 예측 점수 | 0.9920 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 14건 / 전체 14건) |
| 허가증 수 | 14건 (유효 14건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Fluticasone 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “플루티카손프로피오네이트는 항염증 활성을 가진 합성 삼불화 코르티코스테로이드이다. 플루티카손프로피오네이트는 시험관 내에서 인간 글루코코르티코이드 수용체에 대해 덱사메타손의 18배, 베클로메타손디프로피오네이트의 활성 대사체인 베클로메타손-17-모노프로피오네이트(BMP)의 거의 2배, 부데소니드의 3배 이상에 해당하는 결합 친화도를 나타내는 것으로 확인되었다.” 영어 원문: "Fluticasone propionate is a synthetic trifluorinated corticosteroid with anti-inflammatory activity. Fluticasone propionate has been shown in vitro to exhibit a binding affinity for the human glucocorticoid receptor that is 18 times that of dexamethasone, almost twice that of beclomethasone-17-monopropionate (BMP), the active metabolite of beclomethasone dipropionate, and over 3 times that of budesonide." ([DailyMed: Xhance (fluticasone propionate) prescribing information, Paratek Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=44fcea33-8cfa-3a5c-e063-6394a90aafb2), 버전 2026-10-23; 확인일 2026-11-19). 알려진 정보에 따르면 fluticasone은 흡입 또는 비강 투여하는 국소 글루코코르티코이드로, 항염증 작용을 나타냅니다. 한국에서는 단일제(fluticasone propionate, fluticasone furoate)와 복합제 계열 제품으로 허가되어 있습니다.

편두통에는 신경인성 염증이 관여하는 것으로 알려져 있어, 항염증 약물이 이론적으로 연결될 수는 있습니다. 그러나 이는 추측 수준이며, 이 보고서의 데이터에서 직접 뒷받침되지 않습니다.

게다가 흡입제나 비강 분무제는 전신 노출이 낮아 중추신경계 효과를 기대하기 어렵습니다. 유일하게 연결된 문헌(PMID 18681087)도 비강 코르티코스테로이드 사용 중 발생한 신경정신계 이상반응을 분석한 것으로, 치료 효과의 근거가 아닙니다.

참고로 TxGNN 상위 예측에는 **변이형 협심증**(0.9919)과 **뇌간 조짐 편두통**(0.9909)도 있으나, 둘 다 임상시험과 문헌이 없는 계산 예측입니다. 뇌간 조짐 편두통의 점수는 TxGNN 모델(딥러닝)에서 나온 것이며, 상위 질환인 편두통과 관련된 질환 사이에서 모델이 학습한 유사성을 반영했을 가능성이 있을 뿐 생물학적 근거는 아닙니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [18681087](https://pubmed.ncbi.nlm.nih.gov/18681087/) | 2008 | Review | Annals of Allergy, Asthma & Immunology | WHO 국제 약물감시 프로그램 자료에서 비강 코르티코스테로이드 사용 중 신경정신계 이상반응 사례가 집중적으로 보고됨. 효능이 아닌 안전성 관련 문헌 |

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 한국 시판 정보

허가 적응증 본문은 확인되지 않아 제품명, 제형 및 제조사를 기재합니다. (주요 5건)

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 200307778 | 후릭소타이드주니어에보할러50마이크로그램(플루티카손프로피오네이트(미분화)) | 흰색-미백색의 현탁액이 흡입량 조절밸브가 달린 금속통에 든 흡입 에어로솔… | (주)글락소스미스클라인 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200307778/EE) | 유효 |
| 199604660 | 후릭소타이드디스커스100마이크로그램(플루티카손프로피오네이트(미분화)) | 흰색 또는 유백색의 분말이 담겨져 있고, 남아있는 복용량의 수를 나타내는… | (주)글락소스미스클라인 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199604660/EE) | 유효 |
| 201606837 | 아뉴이티100엘립타(플루티카손푸로에이트(미분화)) | 흰색가루가 충진된 블리스터가 규칙적으로 분포되어 있는 1개의 스트립이 플… | (주)글락소스미스클라인 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201606837/EE) | 유효 |
| 200805432 | 아바미스나잘스프레이(미분화플루티카손푸로에이트) | 흰색의 균질한 현탁액이 연한 파랑색의 레바와 뚜껑마개가 장착된 유리병에… | (주)글락소스미스클라인 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200805432/EE) | 유효 |
| 201309960 | 플루티폼흡입제250μg/10μg | 흡입량 조절밸브가 달린 알루미늄 용기 속에 흰색 내지 미백색의 현탁액이… | 한국먼디파마(유) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201309960/EE) | 유효 |

위 표는 허가 14건 중 5건입니다.

<!-- licenses:end -->

이 외에 트렐리지엘립타, 렐바엘립타, 플루티폼 등의 유효 허가가 더 있습니다. 허가 건수와 상태는 빠른 개요와 위 표에 있습니다.

<!-- review:begin kr-lic-20261124b-fluticasone-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “이 외에 트렐리지엘립타, 렐바엘립타, 플루티폼 등을 포함해 총 13건의 유효 허가가 있습니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 허가 건수가 자료와 맞지 않아, 건수를 쓰지 않고 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124b-fluticasone-1 -->

## 안전성 고려사항

- **약물 상호작용**: 데이터에 총 474건의 상호작용이 있습니다. 주요 항목은 다음과 같습니다.
  - **Clarithromycin**: Major
  - **Aprepitant**: Moderate
  - **Insulin human (흡입, 속효성)**: Moderate
  - 그 외 prednisone, triamcinolone 등 다수는 등급 미확인(Unknown)입니다.

경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 점수는 높지만 임상시험이 없고, 유일한 문헌은 효능이 아닌 이상반응을 다룹니다. 기전적 근거도 추측 수준이며 흡입·비강 투여의 낮은 전신 노출은 중추신경계 효과의 타당성을 떨어뜨립니다.

**진행하려면 필요한 것:**
- MFDS 허가사항 문서에서 적응증, 경고, 금기 확인 (안전성 검토의 선행 조건)
- DrugBank 등에서 상세한 작용 기전(MOA) 데이터 확보
- 편두통에 대한 전임상 또는 관찰 연구 등 직접 근거 탐색
- 편두통 치료에 적합한 투여 경로와 전신 노출 수준 검토 (현재 투여 경로 호환성 평가 미완료)

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Xhance (fluticasone propionate) prescribing information, Paratek Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=44fcea33-8cfa-3a5c-e063-6394a90aafb2) |
| 2026-11-24 | 허가 건수: “이 외에 트렐리지엘립타, 렐바엘립타, 플루티폼 등을 포함해 총 13건의 유효 허가가 있…” → 자료 기준으로 수정(건수는 빠른 개요와 표) | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

