---
noindex: true
sitemap: false
layout: default
title: Glipizide
parent: 모델 예측만 (L5)
nav_order: 383
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Glipizide
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **0** 건
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

## Glipizide (DB01067): 평가 보류 — 핵심 데이터 미수집
{: .text-alpha }

## 한 문장 요약

Glipizide(DrugBank ID: DB01067)는 본 Evidence Pack에 기존 적응증·TxGNN 예측 적응증·안전성 정보가 모두 포함되어 있지 않습니다.
작용 기전(MOA)을 포함한 핵심 항목이 수집되지 않아 재창출 가능성 평가를 진행할 수 없는 상태입니다.
**데이터 수집 완료 후 재평가**가 필요합니다.

<!-- review:begin kr-lic-20261031-glipizide-1 -->

> **검토 정정 (2026-10-31)**: 원래 문장: “Glipizide(DrugBank ID: DB01067)는 현재 한국 미시판 약물로, 본 Evidence Pack에 기존 적응증·TxGNN 예측 적응증·안전성 정보가 모두 포함되어 있지 않습니다.” 삭제: 허가가 취소되었거나 허가·시판되지 않는다고 했으나, 성분 기준으로 다시 맞춘 2026-10-31 기준 식품의약품안전처(nedrug) 허가 자료와 맞지 않습니다. 이 약의 허가는 1건(유효 1건)이며, 현재 수치는 빠른 개요와 「한국 시판 정보」의 표에 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261031-glipizide-1 -->

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | 예측 결과 없음 |
| TxGNN 예측 점수 | — |
| 근거 수준 | 평가 불가 |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

---

## 누락 데이터 현황

정식 평가를 차단하는 데이터 격차는 다음과 같습니다.

| ID | 누락 항목 | 심각도 | 영향 | 해결 방안 |
|----|-----------|--------|------|-----------|
| DG001 | 허가사항 경고 및 금기 (MFDS 仿單) | **Blocking** | 안전성 초평가 불가 | MFDS 공식 사이트에서 PDF 다운로드 및 파싱 |
| DG002 | 작용 기전 (MOA) | **High** | 기전 연관성 분석 불가 | DrugBank API 조회 |

> DG001이 **Blocking** 등급이므로, 이 항목이 해소되기 전까지 이후 모든 평가 단계를 시작할 수 없습니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증이 없고, 기존 적응증·작용 기전·안전성 정보 모두 수집되지 않아 재창출 후보로서의 타당성을 판단할 근거가 없습니다. 현 시점에서는 보고서 작성 자체가 불가합니다.

**진행하려면 필요한 것:**
- MFDS 허가사항 PDF 수집 및 파싱 → 경고·금기 추출 (DG001 해소)
- DrugBank API를 통한 MOA 데이터 확보 (DG002 해소)
- TxGNN 모델을 통한 신규 적응증 예측 실행 (`predicted_indications` 생성)
- 기존 허가 적응증 확인 및 `original_indications` 입력
- 위 데이터 보완 후 Evidence Pack v5 재생성 및 보고서 재실행

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-10-31 | 삭제: “현재 한국 미시판 약물로” | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

