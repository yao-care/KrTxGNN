---
noindex: true
sitemap: false
layout: default
title: Arotinolol Hydrochloride
parent: 모델 예측만 (L5)
nav_order: 88
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Arotinolol Hydrochloride
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

## Arotinolol Hydrochloride: 예측 적응증 데이터 없음 — 평가 보류
{: .text-alpha }

---

## 한 문장 요약

Arotinolol Hydrochloride는 베타차단·알파차단 계열 약물로 알려져 있으나, 현재 수신된 Evidence Pack에는 TxGNN 예측 적응증이 포함되어 있지 않습니다.
작용 기전(MOA)과 허가 경고·금기 데이터 모두 누락되어 있어 약물 재창출 가능성을 정식 평가하기 위한 추가 데이터 확보가 선행되어야 합니다.

<!-- review:begin kr-lic-20261105-arotinolol_hydrochloride-1 -->

> **검토 정정 (2026-11-05)**: 원래 문장: “한국 내 시판 기록도 없으며, 작용 기전(MOA)과 허가 경고·금기 데이터 모두 누락되어 있어 약물 재창출 가능성을 정식 평가하기 위한 추가 데이터 확보가 선행되어야 합니다.” 삭제: 성분 기준으로 다시 맞춘 2026-11-05 기준 식품의약품안전처(nedrug) 허가 자료와 맞지 않습니다. 이 약의 허가는 4건(유효 4건)이며, 현재 수치는 빠른 개요와 「한국 시판 정보」의 표에 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261105-arotinolol_hydrochloride-1 -->

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 |
| 예측 신규 적응증 | 예측 결과 없음 |
| TxGNN 예측 점수 | — |
| 근거 수준 | L5 (예측 미실행) |
| 한국 시판 현황 | 시판 중 (유효 허가 4건 / 전체 4건) |
| 허가증 수 | 4건 (유효 4건) |
| 권장 결정 | Hold |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 결과(`predicted_indications`)가 없고, 기존 허가 적응증·MOA·안전성 데이터 모두 확보되지 않아 재창출 타당성을 판단할 수 없습니다.

**진행하려면 필요한 것:**
- TxGNN 예측 파이프라인 실행 결과 수신 (`predicted_indications` 배열 채움)
- 작용 기전(MOA) 데이터 — DrugBank API 조회 (DG002, High)
- 허가 경고 및 금기 사항 — MFDS/TFDA 공식 허가사항 PDF 파싱 (DG001, Blocking)
- 기존 허가 적응증 확인 — 국내외 약품 DB 대조

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-05 | 삭제: “한국 내 시판 기록도 없으며” | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

