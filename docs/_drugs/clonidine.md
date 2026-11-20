---
layout: default
title: Clonidine
parent: 모델 예측만 (L5)
nav_order: 229
evidence_level: L5
indication_count: 10
monitor_inn: "Clonidine"
predicted_indications: ["faciodigitogenital syndrome", "specific developmental disorder", "chondromyxoid fibroma", "trichotillomania", "Tourette syndrome", "obesity disorder", "hypervitaminosis", "proximal 16p11.2 microdeletion syndrome", "migraine disorder", "manic bipolar affective disorder"]
last_modified_at: 2026-11-15
description: "Clonidine: 예측 신규 적응증 안면지생식기 증후군 (faciodigitogenital syndrome) (근거 수준 L5). 기존 적응증: 6 ~ 17 세 소아 및 청소년의 주의력결핍과잉행동장애 (ADHD) 치료 진단은 DSM-IV 기준 또는…"
---

# Clonidine
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

## Clonidine: 알파-2 아드레날린 작용제 → 안면지생식기 증후군 (faciodigitogenital syndrome)
{: .text-alpha }

## 한 문장 요약

Clonidine은 중추 알파-2 아드레날린 수용체 작용제 계열의 약물입니다.
TxGNN 모델은 **안면지생식기 증후군(faciodigitogenital syndrome)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 **임상시험은 0건**, **문헌도 0편**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 6 ~ 17 세 소아 및 청소년의 주의력결핍과잉행동장애 (ADHD) 치료 진단은 DSM-IV 기준 또는 ICD-10 가이드라인에 따라 실시해야 한다. ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201302802/EE)) |
| 예측 신규 적응증 | 안면지생식기 증후군 (faciodigitogenital syndrome) |
| TxGNN 예측 점수 | 1.0000 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Clonidine 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “클로니딘은 뇌간의 알파-아드레날린 수용체를 자극한다. 이 작용으로 중추신경계로부터의 교감신경 유출이 감소하고, 말초 저항, 신혈관 저항, 심박수 및 혈압이 감소한다.” 영어 원문: "Clonidine stimulates alpha-adrenoreceptors in the brain stem. This action results in reduced sympathetic outflow from the central nervous system and in decreases in peripheral resistance, renal vascular resistance, heart rate, and blood pressure." ([DailyMed: Qlonilik (clonidine hydrochloride) prescribing information, CMP Pharma, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=826de1dc-378e-4c90-86d1-e33f7a4248cd), 버전 2026-08-12; 확인일 2026-11-19). Clonidine은 알파-2 아드레날린 작용을 통해 중추 교감신경 출력을 낮추는 약물로 알려져 있습니다.

그러나 안면지생식기 증후군은 드문 유전성 발달 질환이며, 알파-2 아드레날린 작용이 이 질환과 연결된다는 기전적 근거는 확인되지 않았습니다. 예측 점수는 매우 높지만 이는 모델 기반 예측일 뿐이며, 이를 뒷받침하는 임상시험이나 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201302802 | 켑베이서방정0.1밀리그램(클로니딘염산염) | 흰색의 양면이 볼록한 원형 정제 | 적응증 본문 미기재 (링크만 제공) |

## 안전성 고려사항

- **약물 상호작용**: DDI 조회 결과 총 100건이 확인되었으며, 이 중 일부는 중등도(Moderate) 수준입니다. 대표적으로 hydrocortisone, bupropion, triamcinolone, morphine, dexamethasone, betamethasone, budesonide 등이 있고, 혈당 관련 약물(canagliflozin, dapagliflozin, empagliflozin, glimepiride, glipizide, glyburide, 인슐린 제제 등)도 포함됩니다.

그 외 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
안면지생식기 증후군에 대한 임상시험과 문헌이 전혀 없고 기전적 연결고리도 확인되지 않아, 근거 수준은 L5(모델 예측만 존재)입니다.

**진행하려면 필요한 것:**
- 안면지생식기 증후군과 알파-2 아드레날린 경로 사이의 기전적 연관성 검토
- 이 질환에 대한 전임상 또는 임상 근거 확보
- 허가사항의 경고·금기 정보 확보 및 작용 기전 데이터 보완

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Qlonilik (clonidine hydrochloride) prescribing information, CMP Pharma, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=826de1dc-378e-4c90-86d1-e33f7a4248cd) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

