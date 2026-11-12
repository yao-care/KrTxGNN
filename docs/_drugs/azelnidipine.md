---
noindex: true
sitemap: false
layout: default
title: Azelnidipine
parent: 모델 예측만 (L5)
nav_order: 115
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Azelnidipine
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

Evidence Pack를 분석합니다. 핵심 상황:

- `predicted_indications: []` — TxGNN 예측 결과 없음
- `original_moa: "[Data Gap]"` — MOA 없음
- 안전성 데이터 전체 부재

<!-- review:begin kr-lic-20261031-azelnidipine-1 -->

> **검토 정정 (2026-10-31)**: 원래 문장: “`taiwan_regulatory.market_status: "Not marketed"` — 미허가 / `original_moa: "[Data Gap]"` — MOA 없음” 삭제: 대만 TFDA에 관한 템플릿 잔여 문구로, 이 한국 페이지와 관련이 없습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261031-azelnidipine-1 -->

---

## AZELNIDIPINE: 예측 데이터 부족으로 평가 보류
{: .text-alpha }

## 한 문장 요약

AZELNIDIPINE(DB09230)은 이번 평가에 필요한 기초 데이터가 수집되지 않았습니다.
TxGNN 모델의 신규 적응증 예측 결과가 생성되지 않았으며, 작용 기전(MOA) 및 안전성 데이터도 확인되지 않아
현 시점에서 정식 재창출 평가를 진행할 수 없습니다.

<!-- review:begin kr-lic-20261105-azelnidipine-2 -->

> **검토 정정 (2026-11-05)**: 원래 문장: “AZELNIDIPINE(DB09230)은 현재 한국 미허가 약물로, 이번 평가에 필요한 기초 데이터가 수집되지 않았습니다.” 삭제: 성분 기준으로 다시 맞춘 2026-11-05 기준 식품의약품안전처(nedrug) 허가 자료와 맞지 않습니다. 이 약의 허가는 10건(유효 10건)이며, 현재 수치는 빠른 개요와 「한국 시판 정보」의 표에 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261105-azelnidipine-2 -->

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인되지 않음 |
| 예측 신규 적응증 | 없음 (TxGNN 예측 결과 미생성) |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | L5 (예측 결과 없음) |
| 한국 시판 현황 | 시판 중 (유효 허가 10건 / 전체 10건) |
| 허가증 수 | 10건 (유효 10건) |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 AZELNIDIPINE에 대한 TxGNN 예측 결과가 없어 재창출 후보 적응증을 특정할 수 없습니다.
작용 기전(MOA) 데이터도 확보되지 않아 기전 기반의 유사 적응증 추론 또한 불가능합니다.

DrugBank 외 추가 입력 데이터도 없는 상태로, 예측 파이프라인이 실행되었더라도 입력 품질의 한계로 결과 신뢰도를 보장하기 어렵습니다.

<!-- review:begin kr-lic-20261105-azelnidipine-3 -->

> **검토 정정 (2026-11-05)**: 원래 문장: “한국 식약처(MFDS) 허가 이력이 없고 DrugBank 외 추가 입력 데이터도 없는 상태로, 예측 파이프라인이 실행되었더라도 입력 품질의 한계로 결과 신뢰도를 보장하기 어렵습니다.” 삭제: 허가가 취소되었거나 허가·시판되지 않는다고 했으나, 성분 기준으로 다시 맞춘 2026-11-05 기준 식품의약품안전처(nedrug) 허가 자료와 맞지 않습니다. 이 약의 허가는 10건(유효 10건)이며, 현재 수치는 빠른 개요와 「한국 시판 정보」의 표에 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261105-azelnidipine-3 -->

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 결과가 존재하지 않으며, 평가에 필요한 MOA·안전성·규제 데이터가 모두 공백 상태입니다. 추가 데이터 수집 없이는 재창출 타당성 판단이 불가능합니다.

**진행하려면 필요한 것:**
- TxGNN 예측 파이프라인 재실행 및 `predicted_indications` 결과 생성 여부 확인
- DrugBank API를 통한 MOA 데이터 수집 (`DG002` 해소)
- 일본 PMDA 또는 기타 규제 기관 허가사항 참조로 원래 적응증 확인
- MFDS 또는 해외 허가 문서에서 안전성 정보(경고, 금기, 약물상호작용) 수집 (`DG001` 해소)
- 데이터 보완 후 Evidence Pack v5 재생성 및 평가 재개

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-10-31 | 삭제: “`taiwan_regulatory.market_status: "Not marketed"` — 미허가” | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |
| 2026-11-05 | 삭제: “현재 한국 미허가 약물로” | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |
| 2026-11-05 | 삭제: “한국 식약처(MFDS) 허가 이력이 없고” | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

