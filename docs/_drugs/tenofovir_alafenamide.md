---
layout: default
title: Tenofovir Alafenamide
parent: 모델 예측만 (L5)
nav_order: 725
evidence_level: L5
indication_count: 3
monitor_inn: "TENOFOVIR ALAFENAMIDE"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-11-24
description: "Tenofovir Alafenamide: 예측 신규 적응증 고양이 후천성 면역결핍 증후군 (근거 수준 L5). 기존 적응증: 성인의 만성 B형 간염 치료"
---

# Tenofovir Alafenamide
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

## Tenofovir Alafenamide: 허가 적응증에서 고양이 후천성 면역결핍 증후군으로
{: .text-alpha }

## 한 문장 요약

Tenofovir alafenamide는 한국에서 허가된 뉴클레오타이드 역전사효소 억제제입니다(허가 건수와 상태는 빠른 개요 참조). TxGNN 모델은 **고양이 후천성 면역결핍 증후군(Feline Acquired Immunodeficiency Syndrome)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 다룬 임상시험과 문헌은 **0건**입니다. 따라서 이 예측은 모델 점수와 기전적 추정에만 의존하는 단계입니다.

<!-- review:begin kr-lic-20261124c-tenofovir_alafenamide-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “Tenofovir alafenamide는 한국에서 단일 성분 제제 8건이 허가된 뉴클레오타이드 역전사효소 억제제입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 이 사이트 자료의 성분란에는 일치한 성분만 기록되어 허가 품목별 단일 성분·복합 성분 여부를 확인할 수 없으므로, 단일·복합 표기를 빼고 건수는 쓰지 않고 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-tenofovir_alafenamide-1 -->

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 성인의 만성 B형 간염 치료 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202300039/EE)) |
| 예측 신규 적응증 | 고양이 후천성 면역결핍 증후군 |
| TxGNN 예측 점수 | 0.9989 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 8건 / 전체 8건) |
| 허가증 수 | 8건 (유효 8건) |
| 권장 결정 | Hold |

> 근거 수준 참고: 이 질환 자체를 직접 연구한 임상시험이나 문헌이 없으므로 규칙상 L5로 판정했습니다.

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Tenofovir Alafenamide 처방 정보(Prescribing Information)의 “Mechanism of Action” 및 “Microbiology” 항목에 따르면(비공식 번역): “테노포비르 알라페나미드는 B형 간염 바이러스에 대한 항바이러스제이다. […] 테노포비르 알라페나미드는 테노포비르(2'-데옥시아데노신 일인산 유사체)의 포스포아미데이트 전구약물이다. 지용성 세포 투과성 화합물인 테노포비르 알라페나미드는 수동 확산 및 간 흡수 수송체인 OATP1B1과 OATP1B3에 의해 일차 간세포 내로 들어간다.” 영어 원문: "Tenofovir alafenamide is an antiviral drug against the hepatitis B virus. […] Tenofovir alafenamide is a phosphonamidate prodrug of tenofovir (2'-deoxyadenosine monophosphate analog). Tenofovir alafenamide as a lipophilic cell-permeant compound enters primary hepatocytes by passive diffusion and by the hepatic uptake transporters OATP1B1 and OATP1B3." ([DailyMed: Vemlidy (tenofovir alafenamide) prescribing information, Gilead Sciences, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=72e6b33c-0351-4070-9172-eeaa186c01d2), 버전 2025-07-14; 확인일 2026-11-19). 알려진 정보에 따르면 tenofovir alafenamide는 tenofovir의 프로드럭으로, 활성 대사체(tenofovir diphosphate)가 역전사효소를 억제하는 뉴클레오타이드 유사체입니다. 이 약은 HIV 및 HBV 감염 치료에 사용됩니다.

고양이 면역결핍 바이러스(FIV)는 HIV와 유사한 렌티바이러스로, 복제에 역전사효소를 이용합니다. 그래서 기전상 효과 가능성은 있습니다. 다만 이 데이터에는 FIV에 대한 임상시험이나 문헌이 없습니다.

TxGNN의 높은 점수는 HIV 관련 질환 노드와의 유사성을 반영했을 가능성이 큽니다. 기전에 근거한 간접 추정일 뿐 직접 근거는 아닙니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 202300039 | 테카비어디정(테노포비르알라페나미드) | 노란색의 원형 필름코팅정 | 제일약품(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202300039/EE) | 유효 |
| 202204504 | 베믈리아정(테노포비르알라페나미드시트르산염) | 노란색의 원형 필름코팅정 | 동아에스티(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202204504/EE) | 유효 |
| 202300190 | 테노포벨에이정(테노포비르알라페나미드숙신산염) | 한 면에 "CKD", 다른 한 면에 "25"가 음각된 노란색의 원형 필름… | (주)종근당 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202300190/EE) | 유효 |

위 표는 허가 8건 중 3건입니다.

<!-- licenses:end -->

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
고양이 후천성 면역결핍 증후군에 대한 임상시험과 문헌이 없고, 높은 TxGNN 점수는 모델 예측일 뿐입니다. 허가사항의 경고·금기 정보도 확보되지 않아 안전성 검토를 진행할 수 없습니다.

**진행하려면 필요한 것:**
- 식약처 허가사항(경고·금기·적응증 원문) 확보
- 상세한 약물 작용 기전(MOA) 데이터 보완
- FIV에 대한 전임상 또는 수의학 연구 근거 탐색
- 사람 대상 약물의 동물(고양이) 적용 가능성에 대한 별도의 수의학적·규제적 검토

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Vemlidy (tenofovir alafenamide) prescribing information, Gilead Sciences, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=72e6b33c-0351-4070-9172-eeaa186c01d2) |
| 2026-11-24 | 단일·복합 표기: “Tenofovir alafenamide는 한국에서 단일 성분 제제 8건이…” → 확인할 수 없는 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

