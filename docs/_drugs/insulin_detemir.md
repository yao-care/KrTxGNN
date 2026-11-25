---
layout: default
title: Insulin Detemir
parent: 모델 예측만 (L5)
nav_order: 425
evidence_level: L5
indication_count: 9
monitor_inn: "INSULIN DETEMIR"
predicted_indications: ["autoimmune oophoritis", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "focal stiff limb syndrome", "classic stiff person syndrome", "pancreatic agenesis", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy"]
last_modified_at: 2026-11-24
description: "Insulin Detemir: 예측 신규 적응증 자가면역성 난소염 (autoimmune oophoritis) (근거 수준 L5). 기존 적응증: 만 1세 이상의 소아와 청소년 및 성인에서의 당뇨병 치료"
---

# Insulin Detemir
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **9** 건
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

## Insulin detemir: 지속형 인슐린 유사체(기저 인슐린) → 자가면역성 난소염 (autoimmune oophoritis)
{: .text-alpha }

## 한 문장 요약

Insulin detemir는 지속형 기저 인슐린 유사체로, 한국에서 허가증이 확인됩니다(허가 건수와 상태는 빠른 개요 참조).
TxGNN 모델은 **자가면역성 난소염(autoimmune oophoritis)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 다룬 **임상시험과 문헌은 각각 0건**입니다.
현재로서는 모델 예측만 있는 단계입니다.

<!-- review:begin kr-lic-20261124c-insulin_detemir-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “Insulin detemir는 지속형 기저 인슐린 유사체로, 한국에서 단일 성분 허가증 1건이 확인됩니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 단일·복합 표기와 건수를 본문에 고정해 쓰지 않고, 매주 갱신되는 허가 자료를 반영하는 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 2026-11-25에 식품의약품안전처 품목허가 상세 자료(2026-03)의 주성분명으로 품목별로 다시 확인한 결과, 이 자료에 수록된 허가 품목은 모두 단일 성분 제제입니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-insulin_detemir-1 -->

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 만 1세 이상의 소아와 청소년 및 성인에서의 당뇨병 치료 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200603934/EE)) |
| 예측 신규 적응증 | 자가면역성 난소염 (autoimmune oophoritis) |
| TxGNN 예측 점수 | 0.9967 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Insulin Detemir 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “LEVEMIR를 포함한 인슐린의 주된 작용은 포도당 대사의 조절이다. 인슐린과 그 유사체는 특히 골격근 및 지방에 의한 말초 포도당 흡수를 촉진하고 간의 포도당 생성을 억제함으로써 혈당을 낮춘다.” 영어 원문: "The primary activity of insulin, including LEVEMIR, is regulation of glucose metabolism. Insulins and its analogs lower blood glucose by stimulating peripheral glucose uptake, especially by skeletal muscle and fat, and by inhibiting hepatic glucose production." ([DailyMed: Levemir (insulin detemir) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=82192527-99aa-4b53-8ce9-9173668d309c), 버전 2024-10-09; 확인일 2026-11-19). 작용 기전은 출처와 함께 위에 인용되어 있습니다 ([DailyMed](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=82192527-99aa-4b53-8ce9-9173668d309c)).

이 약과 자가면역성 난소염 사이에는 뚜렷한 기전적 연결이 확인되지 않습니다. 예측 점수는 자가면역성 내분비 질환 간의 네트워크 연관성을 반영한 계산상의 결과일 가능성이 있습니다. 인슐린 수용체 작용이 난소의 자가면역을 치료한다는 근거는 알려져 있지 않습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 200603934 | 레버미어플렉스펜주100단위/밀리리터 | 무색 투명한 액이 든 용량조절이 가능한 펜모양의 프리필드 주사제 | 노보노디스크제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200603934/EE) | 유효 |

<!-- licenses:end -->

## 안전성 고려사항

- **약물 상호작용**: 조회된 상호작용은 총 100건이며, 그중 일부는 다음과 같습니다.
  - 중등도: phenylephrine, acebutolol, acetazolamide, formoterol, pseudoephedrine, doxycycline, epinephrine, ethinylestradiol, hydrocortisone, albiglutide, salbutamol, ethanol, hydrochlorothiazide, alogliptin, metformin, pioglitazone, estradiol, alpelisib
  - 경미: hydrocortisone (외용), alclometasone (외용)

허가사항의 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
이 질환을 직접 다룬 임상시험이나 문헌이 없고, 기전적 연결도 불분명하여 근거 수준은 L5(모델 예측만 있음)입니다. 현재 단계에서 재창출을 진행할 근거가 부족합니다.

**진행하려면 필요한 것:**
- 자가면역성 난소염에서 인슐린 수용체 신호 또는 insulin detemir의 역할을 뒷받침하는 전임상 또는 기전 연구
- 상세한 약물 작용 기전(MOA) 데이터
- 허가사항(경고, 금기)의 확보 및 분석
- 한국 시판 상태(취소 여부) 확인

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Levemir (insulin detemir) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=82192527-99aa-4b53-8ce9-9173668d309c) |
| 2026-11-20 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 (2026-11-20 수정, 이전 판은 기록에 보존) | [DailyMed: Levemir (insulin detemir) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=82192527-99aa-4b53-8ce9-9173668d309c) |
| 2026-11-24 | 단일·복합 표기: “Insulin detemir는 지속형 기저 인슐린 유사체로, 한국에서 단…” → 고정된 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 (2026-11-25 수정, 이전 판은 기록에 보존) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

