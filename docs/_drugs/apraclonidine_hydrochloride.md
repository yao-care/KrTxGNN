---
noindex: true
sitemap: false
layout: default
title: Apraclonidine Hydrochloride
parent: 모델 예측만 (L5)
nav_order: 79
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Apraclonidine Hydrochloride
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

Evidence Pack을 분석한 결과:

- `predicted_indications`: 비어 있음 (TxGNN 예측 없음)
- `original_indications`: 비어 있음
- `original_moa`: `[Data Gap]` → 표시 금지
- `safety`: 전부 `[Data Gap]` → 대체 문구 사용
- 항종양약 해당 없음 → 세포독성 섹션 생략

<!-- review:begin kr-lic-20261105-apraclonidine_hydrochloride-1 -->

> **검토 정정 (2026-11-05)**: 원래 문장: “`taiwan_regulatory.licenses`: 0건 → 시판 정보 섹션 생략 / `safety`: 전부 `[Data Gap]` → 대체 문구 사용” 삭제: 대만 TFDA에 관한 템플릿 잔여 문구로, 이 한국 페이지와 관련이 없습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261105-apraclonidine_hydrochloride-1 -->

---

## Apraclonidine Hydrochloride: 재창출 평가 불가 — 데이터 보완 후 재실행 필요
{: .text-alpha }

## 한 문장 요약

Apraclonidine Hydrochloride에 대해 Evidence Pack을 수신하였으나, 기존 적응증 및 작용 기전(MOA) 데이터가 확보되지 않은 상태입니다.
TxGNN 모델의 **예측 결과가 생성되지 않았으며**, **현 시점에서 재창출 후보 평가를 진행할 수 없습니다.**
DrugBank ID 확인 및 규제 기관 자료 보완 후 파이프라인 재실행이 필요합니다.

<!-- review:begin kr-lic-20261105-apraclonidine_hydrochloride-2 -->

> **검토 정정 (2026-11-05)**: 원래 문장: “TxGNN 모델의 **예측 결과가 생성되지 않았으며**, 시판 허가 기록도 없어 **현 시점에서 재창출 후보 평가를 진행할 수 없습니다.**” 삭제: 허가 건수나 상태가 성분 기준으로 다시 맞춘 2026-11-05 기준 식품의약품안전처(nedrug) 허가 자료와 맞지 않습니다. 이 약의 허가는 1건(유효 1건)이며, 현재 수치는 빠른 개요와 「한국 시판 정보」의 표에 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261105-apraclonidine_hydrochloride-2 -->

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | Evidence Pack에 미포함 |
| 예측 신규 적응증 | 예측 결과 없음 |
| TxGNN 예측 점수 | — |
| 근거 수준 | L5 (예측 없음) |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | **Hold** |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 결과가 생성되지 않았고, 기존 적응증·작용 기전(MOA)·안전성 데이터가 모두 누락되어 재창출 후보 평가를 수행할 수 없습니다. 현지 규제 맥락 역시 확인이 불가능합니다.

<!-- review:begin kr-lic-20261105-apraclonidine_hydrochloride-3 -->

> **검토 정정 (2026-11-05)**: 원래 문장: “시판 허가 기록도 없어 현지 규제 맥락 역시 확인이 불가능합니다.” 삭제: 허가 건수나 상태가 성분 기준으로 다시 맞춘 2026-11-05 기준 식품의약품안전처(nedrug) 허가 자료와 맞지 않습니다. 이 약의 허가는 1건(유효 1건)이며, 현재 수치는 빠른 개요와 「한국 시판 정보」의 표에 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261105-apraclonidine_hydrochloride-3 -->

**진행하려면 필요한 것:**
- DrugBank ID 및 작용 기전(MOA) 확보 (DrugBank API 조회)
- 원래 허가 적응증 정보 확보 (FDA, EMA 또는 TFDA 자료 참조)
- 안전성 정보 추출 (허가사항 PDF 다운로드 및 파싱 — DG001 해소)
- 위 데이터 보완 후 TxGNN 예측 파이프라인 재실행

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-05 | 삭제: “`taiwan_regulatory.licenses`: 0건 → 시판 정보 섹션 생략” | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |
| 2026-11-05 | 삭제: “시판 허가 기록도 없어” | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |
| 2026-11-05 | 삭제: “시판 허가 기록도 없어” | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

