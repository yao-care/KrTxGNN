---
layout: default
title: Iloprost
parent: 모델 예측만 (L5)
nav_order: 415
evidence_level: L5
indication_count: 4
monitor_inn: "ILOPROST"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "pulmonary arteriovenous malformation (disease)", "diffuse alopecia areata"]
last_modified_at: 2026-11-15
description: "Iloprost: 예측 신규 적응증 단순 두피 박모증 (hypotrichosis simplex of the scalp) (근거 수준 L5). 기존 적응증: NYHA Ⅲ,Ⅳ에 해당하는 폐동맥고혈압(WHO GroupⅠ)환자의 운동능력 및 증상 개선"
---

# Iloprost
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **4** 건
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

## Iloprost: 프로스타사이클린 유사체 → 단순 두피 박모증 (hypotrichosis simplex of the scalp)
{: .text-alpha }

## 한 문장 요약

Iloprost는 프로스타사이클린 계열의 혈관확장 및 항혈소판 작용 약물입니다.
TxGNN 모델은 **단순 두피 박모증(hypotrichosis simplex of the scalp)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 **임상시험은 0건**, **문헌도 0편**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | NYHA Ⅲ,Ⅳ에 해당하는 폐동맥고혈압(WHO GroupⅠ)환자의 운동능력 및 증상 개선 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200801539/EE)) |
| 예측 신규 적응증 | 단순 두피 박모증 (hypotrichosis simplex of the scalp) |
| TxGNN 예측 점수 | 0.9945 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Iloprost 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “일로프로스트는 프로스타사이클린 PGI 2의 합성 유사체이다. 일로프로스트는 혈관확장제이며 혈소판 응집을 억제한다.” 영어 원문: "Iloprost is a synthetic analog of prostacyclin PGI 2. Iloprost is a vasodilator and inhibits platelet aggregation." ([DailyMed: Aurlumyn (iloprost) prescribing information, BTG International Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=34036fc0-6832-d066-e063-6394a90a18a4), 버전 2026-08-13; 확인일 2026-11-19). 알려진 정보에 따르면 Iloprost는 프로스타사이클린 유사체로 혈관확장과 혈소판 응집 억제 작용을 가집니다. 이로 인해 두피 미세순환에 영향을 줄 가능성은 생각해 볼 수 있으나, 이는 어디까지나 추정입니다.

이번에 정리된 자료에서는 이 예측을 뒷받침하는 기전적 연결 고리가 확인되지 않았습니다. TxGNN 점수는 매우 높지만 임상시험과 문헌이 모두 없어, 임상적 검증이 없는 모델 예측 단계입니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200801539 | 벤타비스흡입액(일로프로스트) | 무색투명한 액이 무색 앰플에 든 흡입용 액제 | 적응증 텍스트가 기재되어 있지 않음 |

## 안전성 고려사항

- **약물 상호작용**: 조회된 상호작용은 총 100건이며, 이 중 주요 항목은 다음과 같습니다.
  - 중등도: Epinephrine, Acetylsalicylic acid(아스피린), Canagliflozin, Dapagliflozin, Empagliflozin, Ertugliflozin, 흡입 속효성 인슐린, Mannitol, Ephedrine, Fenfluramine, Dexfenfluramine, Glycerin, Papaverine, Sibutramine
  - 등급 미상: Calcitriol, Pantoprazole, Morphine, Metformin, Omeprazole

허가사항상의 경고 및 금기는 이번 자료에서 확인되지 않았으므로, 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 예측 점수는 높지만 이를 직접 뒷받침하는 임상시험과 문헌이 없고, 기전적 연결 고리도 확인되지 않아 근거 수준이 L5(모델 예측만 존재)에 머뭅니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기) 확보 및 안전성 검토
- 상세한 약물 작용 기전(MOA) 데이터
- 두피 박모증에 대한 전임상 또는 임상 연구 근거
- 시판 상태(유효/취소) 확인

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Aurlumyn (iloprost) prescribing information, BTG International Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=34036fc0-6832-d066-e063-6394a90a18a4) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

