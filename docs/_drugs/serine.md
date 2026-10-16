---
layout: default
title: Serine
parent: 모델 예측만 (L5)
nav_order: 690
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Serine: 예측 신규 적응증 가족성 내장 근병증 (Familial Visceral Myopathy) (근거 수준 L5). 기존 적응증: 확인 불가 (허가 문서 링크만 확보되어 적응증 본문 미확인)"
monitor_inn: "Serine"
predicted_indications: ["familial visceral myopathy", "intestinal obstruction", "unclassified intestinal pseudoobstruction", "myopathic intestinal pseudoobstruction", "neuronal intestinal dysplasia, type B", "angle-closure glaucoma", "intestinal pseudoobstruction, neuronal, chronic idiopathic, X-linked", "exercise-induced malignant hyperthermia", "aqueous misdirection", "traumatic glaucoma"]
---

# Serine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 약사 평가 보고서

</div>

# Serine: 허가 적응증 정보 미확인에서 가족성 내장 근병증으로

## 한 문장 요약

Serine(세린)은 아미노산 성분으로 한국에서 수액 주사제와 연질캡슐 형태로 허가되어 시판 중이나, 현재 확보된 자료에서는 허가 적응증 문구를 확인할 수 없었습니다.
TxGNN 모델은 **가족성 내장 근병증(Familial Visceral Myopathy)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다.
따라서 현재는 모델 예측만 존재하는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 문서 링크만 확보되어 적응증 본문 미확인) |
| 예측 신규 적응증 | 가족성 내장 근병증 (Familial Visceral Myopathy) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 3건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. Serine은 아미노산으로 영양 수액 제제 등에 사용되는 성분이지만, 허가 적응증 본문이 확보되지 않아 기존 적응증과 신규 적응증 사이의 연관성을 평가할 수 없습니다.

가족성 내장 근병증은 소화관 평활근 기능 이상(예: ACTG2 관련 근병증)으로 발생하는 희귀 질환입니다. 그러나 이 질환과 세린 보충 사이의 기전적 연결고리는 현재 자료로 확인되지 않습니다. 이 예측은 지식 그래프상의 네트워크 근접성에서 비롯된 것일 가능성이 있으며, 검증된 기전으로 보기는 어렵습니다.

같은 방식으로 예측된 다른 질환(장폐색, 만성 가성장폐색, 신경성 장 이형성증, 폐쇄각 녹내장 등)도 모두 L5 수준입니다. 장폐색과 폐쇄각 녹내장에 대해 검색된 문헌은 대부분 "serine"이라는 용어(세린 단백분해효소 PRSS56, STK11 세린/트레오닌 키나제 등)에 따른 키워드 일치로 보이며, 아미노산 세린의 치료 효과를 다룬 연구가 아닙니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200607037 | 헤로셀연질캡슐(수출용) | 연질캡슐 | 허가 문서 참조 |
| 199201368 | 이노엔10%후라바솔주 | 수액 주사제 | 허가 문서 참조 |
| 199201373 | 이노엔8.5%후라바솔주 | 수액 주사제 | 허가 문서 참조 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 매우 높지만 임상시험과 문헌 근거가 없고(L5), 작용 기전과 허가 적응증 정보도 확보되지 않아 타당성을 판단할 수 없습니다. 안전성 데이터 역시 확인되지 않아 안전성 선별 단계로 진행할 수 없습니다.

**진행하려면 필요한 것:**
- 식약처(MFDS) 허가사항 문서에서 적응증, 경고, 금기 정보 확보
- 작용 기전(MOA) 데이터 확보 (예: DrugBank 조회)
- 가족성 내장 근병증과 세린 대사 사이의 기전적 연관성에 대한 문헌 조사
- 키워드 일치로 인한 무관한 문헌을 제외한 재검색
- 투여 경로(경구/정맥) 적합성 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

