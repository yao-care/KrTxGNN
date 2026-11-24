---
layout: default
title: Mesalazine
parent: 모델 예측만 (L5)
nav_order: 505
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
description: "Mesalazine: 예측 신규 적응증 선천성 저모발증 동반 연소성 황반 이영양증 (congenital hypotrichosis with juvenile macul… (근거 수준 L5). 기존 적응증: 1. 주효능 효과 궤양성 대장염의 급성발병치료 및 재발방지, 크론병의 급성발병치료"
monitor_inn: "MESALAZINE"
predicted_indications: ["congenital hypotrichosis with juvenile macular dystrophy", "osteoarthritis", "rheumatoid arthritis", "seborrheic keratosis", "vulvar inverted follicular keratosis", "pseudoachondroplasia"]
---

# Mesalazine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **6** 건
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

## Mesalazine: 염증성 장질환에서 선천성 저모발증 동반 연소성 황반 이영양증으로
{: .text-alpha }

## 한 문장 요약

Mesalazine(5-ASA)은 한국에서 허가를 보유한 항염증제입니다(허가 건수와 상태는 빠른 개요 참조).
TxGNN 모델은 **선천성 저모발증 동반 연소성 황반 이영양증(congenital hypotrichosis with juvenile macular dystrophy)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다. 예측은 모델 점수에만 근거하고 있습니다.

<!-- review:begin kr-lic-20261124c-mesalazine-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “Mesalazine(5-ASA)은 한국에서 14건의 허가를 보유한 단일제 성분의 항염증제입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 이 사이트 자료의 성분란에는 일치한 성분만 기록되어 허가 품목별 단일 성분·복합 성분 여부를 확인할 수 없으므로, 단일·복합 표기를 빼고 건수는 쓰지 않고 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-mesalazine-1 -->

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 주효능 효과 궤양성 대장염의 급성발병치료 및 재발방지, 크론병의 급성발병치료 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201201615/EE)) |
| 예측 신규 적응증 | 선천성 저모발증 동반 연소성 황반 이영양증 (congenital hypotrichosis with juvenile macular dystrophy) |
| TxGNN 예측 점수 | 0.9965 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 14건 / 전체 14건) |
| 허가증 수 | 14건 (유효 14건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Mesalazine 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “메살라민의 작용 기전은 완전히 밝혀지지 않았으나, 결장 상피세포에 국소 항염 효과를 나타내는 것으로 보인다. 궤양성 대장염 환자에서는 사이클로옥시게나제 경로와 리폭시게나제 경로 모두를 통한 아라키돈산 대사체의 점막 생성이 증가되어 있으며, 메살라민은 결장에서 사이클로옥시게나제를 차단하고 프로스타글란딘 생성을 억제함으로써 염증을 감소시킬 가능성이 있다.” 영어 원문: "The mechanism of action of mesalamine is not fully understood, but it appears to have a topical anti-inflammatory effect on the colonic epithelial cells. Mucosal production of arachidonic acid metabolites, both through the cyclooxygenase and lipoxygenase pathways, is increased in patients with ulcerative colitis, and it is possible that mesalamine diminishes inflammation by blocking cyclooxygenase and inhibiting prostaglandin production in the colon." ([DailyMed: Lialda (mesalamine) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3098a080-be86-4265-9818-7fc4beab77b7), 버전 2026-10-26; 확인일 2026-11-19). 알려진 정보에 따르면 Mesalazine은 장관 염증 치료에 쓰이는 5-아미노살리실산 계열 약물이며, COX/LOX 억제, PPAR-gamma 활성화, NF-kB 조절 등 항염증 작용이 보고되어 있습니다.

그러나 이 질환은 CDH3 유전자 이상과 관련된 희귀 유전성 질환으로, Mesalazine의 항염증 작용과의 기전적 연결고리는 제공된 데이터에서 확인되지 않습니다. 예측 점수는 매우 높지만 TxGNN 모델(딥러닝)이 산출한 값으로, 모델이 관련 질환 간에 학습한 유사성을 반영할 수 있을 뿐 생물학적 근거는 아닙니다.

참고로 다른 예측 후보 중에서는 류마티스 관절염(L4)이 상대적으로 많은 문헌을 갖고 있으나, 이는 주로 sulfasalazine 관련 문헌이며 항류마티스 효과는 5-ASA보다 sulfapyridine 성분에 기인하는 것으로 보여 Mesalazine 단독과의 연관성은 간접적입니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201201615 | 대한뉴팜메살라민정250밀리그램(수출용) | 황색의 원형 장용성 필름코팅정 | 대한뉴팜(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201201615/EE) | 유효 |
| 199903215 | 메진정500mg(메살라진)(수출용) | 황색의 장방형 장용성 필름코팅정 | (주)휴온스 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199903215/EE) | 유효 |
| 200307868 | 아사콜관장액4그람/100밀리리터(메살라진) | 흰색 불투명한 폴리에틸렌 용기에 들어있는 갈색현탁액 | (주)대웅제약 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200307868/EE) | 유효 |
| 200307870 | 아사콜좌약500밀리그람(메살라진) | 회갈색의 방추형 좌약 | (주)대웅제약 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200307870/EE) | 유효 |
| 201001891 | 메자반트엑스엘장용정1200밀리그램(메살라진) | 적갈색 타원형의 서방형 장용필름코팅정제 | 한국다케다제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201001891/EE) | 유효 |

위 표는 허가 14건 중 5건입니다.

<!-- licenses:end -->

## 안전성 고려사항

- **약물 상호작용**: 데이터에서 조회된 상호작용 100건 중 일부를 확인했습니다. 중대(Major) 수준으로는 Cidofovir, 보툴리눔 신경독소 A/B 면역글로불린이 있습니다. 중등도(Moderate) 수준으로는 Ketorolac, Ibuprofen, Celecoxib 등 NSAID, Amphotericin B, Amikacin, Cisplatin 등 신독성 약물, Azathioprine 등이 있습니다.
- **지식 그래프 기반 금기 관련 질환**: 신장 질환, 간 질환, 담낭 질환, 호중구감소증, 무과립구증, 빈혈, 간질성 신염, 지질성 신증, 유문 협착증 등이 연결되어 있습니다. 이는 허가 문서의 금기 사항이 아니라 지식 그래프의 연결 정보이므로 허가사항 확인이 필요합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
임상시험과 문헌이 전혀 없고 기전적 연결고리도 확인되지 않아, 높은 TxGNN 점수(0.9965)만으로는 진행 근거가 부족합니다. 허가사항의 경고·금기 정보도 확보되지 않았습니다.

**진행하려면 필요한 것:**
- Mesalazine의 작용 기전(MOA) 데이터 확보 (DrugBank 조회)
- MFDS 허가사항(경고·금기·적응증 텍스트) 확보 및 분석
- CDH3 관련 질환과 Mesalazine 사이의 기전적 연관성에 대한 전임상 근거
- 우선순위 재검토: 근거가 상대적으로 많은 류마티스 관절염 등 다른 예측 후보 평가 고려

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Lialda (mesalamine) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3098a080-be86-4265-9818-7fc4beab77b7) |
| 2026-11-24 | 단일·복합 표기: “Mesalazine(5-ASA)은 한국에서 14건의 허가를 보유한 단일제…” → 확인할 수 없는 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

