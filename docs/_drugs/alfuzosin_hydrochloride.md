---
noindex: true
sitemap: false
layout: default
title: Alfuzosin Hydrochloride
parent: 모델 예측만 (L5)
nav_order: 38
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Alfuzosin Hydrochloride
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

## Alfuzosin Hydrochloride: 평가 보류 — 필수 데이터 누락
{: .text-alpha }

---

## 한 문장 요약

Alfuzosin Hydrochloride는 알파-1 차단제 계열로 알려진 약물이나, 이번 Evidence Pack에는 기존 적응증 및 TxGNN 예측 신규 적응증 데이터가 모두 포함되어 있지 않습니다.
작용 기전(MOA)과 안전성 정보(경고·금기)가 누락된 상태로, 현 단계에서는 정식 약물 재창출 평가를 수행할 수 없습니다.

<!-- review:begin kr-lic-20261105-alfuzosin_hydrochloride-1 -->

> **검토 정정 (2026-11-05)**: 원래 문장: “한국 내 허가 이력이 없으며, 작용 기전(MOA)과 안전성 정보(경고·금기)가 누락된 상태로, 현 단계에서는 정식 약물 재창출 평가를 수행할 수 없습니다.” 삭제: 허가가 취소되었거나 허가·시판되지 않는다고 했으나, 성분 기준으로 다시 맞춘 2026-11-05 기준 식품의약품안전처(nedrug) 허가 자료와 맞지 않습니다. 이 약의 허가는 19건(유효 16건)이며, 현재 수치는 빠른 개요와 「한국 시판 정보」의 표에 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261105-alfuzosin_hydrochloride-1 -->

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | 데이터 없음 (TxGNN 예측 미제공) |
| TxGNN 예측 점수 | — |
| 근거 수준 | L5 (예측 결과 없음, 실증 연구 미확인) |
| 한국 시판 현황 | 시판 중 (유효 허가 16건 / 전체 19건) |
| 허가증 수 | 19건 (유효 16건) |
| 권장 결정 | **Hold** |

---

## 이 예측이 타당한 이유는?

현재 Evidence Pack에 작용 기전(MOA) 데이터가 포함되어 있지 않습니다. DrugBank 조회는 성공(1건 반환)하였으나, DrugBank ID 및 MOA 정보가 최종 데이터셋에 반영되지 않아 기전 분석이 불가능합니다.

TxGNN 모델이 이 약물에 대한 신규 적응증 예측을 제공하지 않았으므로, 기존 적응증과 신규 적응증 간 연관성 분석 역시 현 단계에서는 수행할 수 없습니다.

<!-- review:begin kr-lic-20261105-alfuzosin_hydrochloride-2 -->

> **검토 정정 (2026-11-05)**: 원래 문장: “현재 한국 내 허가된 제품이 없습니다.” 삭제: 성분 기준으로 다시 맞춘 2026-11-05 기준 식품의약품안전처(nedrug) 허가 자료와 맞지 않습니다. 이 약의 허가는 19건(유효 16건)이며, 현재 수치는 빠른 개요와 「한국 시판 정보」의 표에 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261105-alfuzosin_hydrochloride-2 -->

---

## 한국 시판 정보

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증이 없고, 안전성 정보(경고·금기) 및 작용 기전(MOA) 데이터가 모두 누락되어 있어 재창출 평가의 핵심 요소가 갖춰지지 않은 상태입니다.

**진행하려면 필요한 것:**
- DrugBank API를 통해 DrugBank ID 및 MOA 데이터 확보 (`DG002`, 우선순위: High)
- TFDA 또는 관련 국가 허가사항 PDF에서 경고·금기 정보 추출 (`DG001`, 우선순위: Blocking)
- DrugBank 조회 결과(query\_log ID 2, result\_count: 1)를 Evidence Pack 약물 섹션에 반영
- TxGNN 파이프라인 재실행하여 예측 적응증 생성
- 한국 MFDS 데이터베이스에서 Alfuzosin 관련 허가 현황 추가 확인

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-05 | 삭제: “한국 내 허가 이력이 없으며” | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |
| 2026-11-05 | 삭제: “현재 한국 내 허가된 제품이 없습니다” | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

