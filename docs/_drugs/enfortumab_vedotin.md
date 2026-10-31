---
layout: default
title: Enfortumab Vedotin
parent: 모델 예측만 (L5)
nav_order: 309
evidence_level: L5
indication_count: 9
monitor_inn: "Enfortumab vedotin"
predicted_indications: ["leprosy", "multiple endocrine neoplasia", "cytomegalovirus infection", "candidiasis", "cerebral infarction", "HIV infectious disease", "homozygous familial hypercholesterolemia", "malignant catarrh", "infectious bovine rhinotracheitis"]
last_modified_at: 2026-10-31
description: "Enfortumab Vedotin: 예측 신규 적응증 나병 (leprosy) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202300822/EE"
---

# Enfortumab Vedotin
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

## Enfortumab vedotin: Nectin-4 표적 항체-약물 접합체 → 나병 (leprosy)
{: .text-alpha }

## 한 문장 요약

Enfortumab vedotin은 Nectin-4를 표적으로 하는 항체-약물 접합체(ADC)로, 미세소관 억제제 MMAE를 종양 세포에 전달하는 항암제입니다.
TxGNN 모델은 **나병(leprosy)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험과 문헌은 0건**입니다.
이 예측은 컴퓨터 모델 결과일 뿐이며, 현재로서는 근거가 매우 부족합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202300822/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202300823/EE |
| 예측 신규 적응증 | 나병 (leprosy) |
| TxGNN 예측 점수 | 0.9953 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 2건) |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 충분하지 않습니다. 알려진 정보에 따르면 이 약은 Nectin-4를 표적으로 하는 ADC이며, 미세소관 억제제인 MMAE를 Nectin-4 발현 종양 세포에 전달합니다.

이 기전과 나병(*Mycobacterium leprae* 감염) 사이를 연결하는 근거는 이번에 수집된 데이터에서 확인되지 않습니다. 세포독성 항암 기전이 항미생물 효과로 이어진다는 자료도 없습니다.

따라서 높은 예측 점수는 계산상의 결과일 뿐이며, 기전상 타당성은 현재 입증되지 않았습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202300822 | 파드셉주20밀리그램(엔포투맙베도틴) | 동결건조 분말 주사제 | 허가 문서 링크만 제공됨 |
| 202300823 | 파드셉주30밀리그램(엔포투맙베도틴) | 동결건조 분말 주사제 | 허가 문서 링크만 제공됨 |

---

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (항체-약물 접합체, 미세소관 억제제 MMAE 탑재) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

---

## 안전성 고려사항

- **약물 상호작용**: 데이터에서 100건이 확인되었으며, 대부분 중등도(Moderate)입니다. 주요 항목은 다음과 같습니다.
  - 중대(Major): Clarithromycin
  - 중등도: Aprepitant, Metformin, Pioglitazone, Glimepiride, Glipizide, Glyburide, Dapagliflozin, Empagliflozin 등 (혈당강하제 계열이 다수)

그 외 경고 및 금기 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 나병에 대한 임상시험과 문헌이 전혀 없고, 기전적 연결고리도 확인되지 않아 근거 수준은 L5(모델 예측만 존재)입니다.
- 세포독성 항암제를 감염병에 적용할 근거가 없으므로 현 단계에서 진행하기 어렵습니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기·적응증) 원문 확보 및 분석
- 상세한 작용 기전(MOA) 데이터 보충
- 나병과의 기전적 연관성을 보여주는 전임상 연구 또는 문헌
- 안전성 검토(세포독성 항암제의 감염 위험 등)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

