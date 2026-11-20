---
layout: default
title: Isotretinoin
parent: 모델 예측만 (L5)
nav_order: 442
evidence_level: L5
indication_count: 1
monitor_inn: "ISOTRETINOIN"
predicted_indications: ["malignant hypertensive renal disease"]
last_modified_at: 2026-11-20
description: "Isotretinoin: 예측 신규 적응증 악성 고혈압성 신장질환 (malignant hypertensive renal disease) (근거 수준 L5). 기존 적응증: 다른 치료법으로 잘 치료되지 않는 중증의 결절성-낭포성 여드름(좌창), 특히 체간 병변이 관련된 낭포성…"
---

# Isotretinoin
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

## Isotretinoin: 레티노이드 (비타민 A 유도체) → 악성 고혈압성 신장질환 (malignant hypertensive renal disease)
{: .text-alpha }

## 한 문장 요약

Isotretinoin은 경구 연질캡슐 등으로 국내에 허가된 레티노이드 계열 약물입니다.
TxGNN 모델은 **악성 고혈압성 신장질환(malignant hypertensive renal disease)**에 효과가 있을 수 있다고 예측하지만, 현재 이 방향을 직접 지지하는 **임상시험은 0건, 문헌도 0편**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 다른 치료법으로 잘 치료되지 않는 중증의 결절성-낭포성 여드름(좌창), 특히 체간 병변이 관련된 낭포성 및접촉성 여드름 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201306920/EE)) |
| 예측 신규 적응증 | 악성 고혈압성 신장질환 (malignant hypertensive renal disease) |
| TxGNN 예측 점수 | 0.9901 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 19건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Isotretinoin 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “전신 항생제를 포함한 기존 치료에 반응하지 않는, 직경 5 mm 이상의 다발성 염증성 결절을 가진 12세 이상의 비임신 환자에서 중증 난치성 결절성 여드름 치료 시 Zenatane의 정확한 작용기전은 알려져 있지 않다. 레티노이드인 이소트레티노인은 피지선 기능과 각질화를 억제한다.” 영어 원문: "The exact mechanism of action of Zenatane in the treatment of severe recalcitrant nodular acne in nonpregnant patients 12 years of age and older with multiple inflammatory nodules with a diameter of 5 mm or greater who are unresponsive to conventional therapy, including systemic antibiotics is unknown. Isotretinoin, a retinoid, inhibits sebaceous gland function and keratinization." ([DailyMed: Zenatane (isotretinoin) prescribing information, Dr. Reddy's Laboratories Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=27b3cf26-f22e-5b70-1c24-009933b7c6ee), 버전 2026-09-20; 확인일 2026-11-19). 따라서 Isotretinoin의 기전을 근거로 한 직접적인 연관성 분석은 할 수 없습니다.

레티노이드는 신장 손상 전임상 모델에서 단백뇨 감소 및 항섬유화 효과가 연구된 바 있습니다. 다만 이는 간접적인 정보이며, Isotretinoin이나 악성 고혈압성 신장병증에 특정된 것은 아닙니다.

이번 예측 점수(0.9901)는 매우 높지만, 같은 계열의 인접 질환 예측(악성 신혈관성 고혈압)과 동일한 점수를 보입니다. 두 예측이 독립적이지 않고 같은 모델 내 유사한 영역에서 나왔을 가능성이 있습니다. 현재 자료는 계산상의 가설 수준에 머뭅니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

주요 허가 5건입니다. 전체 20건 중 일부이며, 목록은 부분 기록일 수 있습니다. 허가 적응증 텍스트는 링크 형태로만 기록되어 있어 세부 내용은 각 허가 문서를 참조해야 합니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201306920 | 이소레인연질캡슐20mg (수출용) | 연질캡슐 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201306920/EE) |
| 200904074 | 이티에스연질캡슐10밀리그램 (수출용) | 연질캡슐 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200904074/EE) |
| 200102110 | 이소트렌연질캡슐 | 연질캡슐 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200102110/EE) |
| 201508411 | 우리큐탄연질캡슐 | 연질캡슐 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201508411/EE) |
| 201503563 | 트렉마이겔 (수출용) | 겔 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201503563/EE) |

## 안전성 고려사항

허가사항의 경고 및 금기 정보는 이 보고서의 데이터에 포함되어 있지 않아, 안전성 정보는 허가사항을 참조하세요.

- **약물 상호작용**: 총 98건이 기록되어 있습니다. 주요(Major) 등급은 다음과 같습니다.
  - Doxycycline, Minocycline, Tetracycline (테트라사이클린계 항생제)
  - Vitamin A
- **중등도(Moderate) 상호작용**: 코르티코스테로이드(Betamethasone, Budesonide, Dexamethasone, Hydrocortisone, Prednisolone, Prednisone, Triamcinolone), Warfarin, Dicoumarol, Ethanol, Naltrexone, Nitisinone, Fostamatinib, Ivacaftor, Lumacaftor 등
- 이상지질혈증, 간 영향, 기형 유발성 등 알려진 위험은 중증 질환자이자 여러 약물을 복용하는 이 환자군에서 특히 주의가 필요합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 예측 점수는 높지만 직접 뒷받침하는 임상시험이나 문헌이 없어 근거 수준이 L5(모델 예측만 있음)입니다. 또한 안전성 및 기전 데이터가 부족합니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기) 자료 확보: 식약처 허가 문서 PDF 내려받기 및 분석
- 작용 기전(MOA) 데이터 보완
- 악성 고혈압성 신장질환에 대한 전임상 또는 임상 연구 근거 확인
- 중증 신장질환 환자에서의 안전성 평가 계획

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Zenatane (isotretinoin) prescribing information, Dr. Reddy's Laboratories Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=27b3cf26-f22e-5b70-1c24-009933b7c6ee) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

