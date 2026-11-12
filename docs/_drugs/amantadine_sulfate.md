---
noindex: true
sitemap: false
layout: default
title: Amantadine Sulfate
parent: 모델 예측만 (L5)
nav_order: 52
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Amantadine Sulfate
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

## AMANTADINE SULFATE: 약물 재창출 평가 보류
{: .text-alpha }

## 한 문장 요약

AMANTADINE SULFATE는 이번 Evidence Pack에는 TxGNN 예측 적응증 데이터가 포함되지 않아 정상적인 약물 재창출 평가를 진행할 수 없습니다. 예측 파이프라인이 완료되지 않았으며, 작용 기전(MOA)·안전성·기존 적응증 데이터가 모두 누락된 상태입니다. 평가를 재개하려면 DrugBank 데이터 추출 및 예측 파이프라인 재실행이 선행되어야 합니다.

<!-- review:begin kr-lic-20261105-amantadine_sulfate-1 -->

> **검토 정정 (2026-11-05)**: 원래 문장: “AMANTADINE SULFATE는 현재 한국 내 허가 기록이 없는 약물로, 이번 Evidence Pack에는 TxGNN 예측 적응증 데이터가 포함되지 않아 정상적인 약물 재창출 평가를 진행할 수 없습니다.” 삭제: 성분 기준으로 다시 맞춘 2026-11-05 기준 식품의약품안전처(nedrug) 허가 자료와 맞지 않습니다. 이 약의 허가는 3건(유효 2건)이며, 현재 수치는 빠른 개요와 「한국 시판 정보」의 표에 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261105-amantadine_sulfate-1 -->

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 |
| 예측 신규 적응증 | 없음 (예측 결과 미생성) |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 3건) |
| 허가증 수 | 3건 (유효 2건) |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 Evidence Pack에 `predicted_indications` 데이터가 없어 기전 관련성 분석을 수행할 수 없습니다.

DrugBank 쿼리(query_log ID #2)는 1건의 결과를 반환하는 데 성공했으나, 해당 내용이 Evidence Pack에 반영되지 않았습니다. `drugbank_id`도 확인되지 않은 상태입니다. MOA 및 DrugBank 기본 정보를 확보한 뒤 분석을 재개해야 합니다.

<!-- review:begin kr-lic-20261105-amantadine_sulfate-2 -->

> **검토 정정 (2026-11-05)**: 원래 문장: “현재 AMANTADINE SULFATE의 한국 허가 기록이 없습니다 (총 0건).” 삭제: 허가 건수나 상태가 성분 기준으로 다시 맞춘 2026-11-05 기준 식품의약품안전처(nedrug) 허가 자료와 맞지 않습니다. 이 약의 허가는 3건(유효 2건)이며, 현재 수치는 빠른 개요와 「한국 시판 정보」의 표에 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261105-amantadine_sulfate-2 -->

---

## 한국 시판 정보

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 적응증 데이터가 없고, 작용 기전·안전성·기존 적응증 정보가 모두 누락되어 있어 약물 재창출 평가를 진행할 수 없는 상태입니다.

**진행하려면 필요한 것:**
- DrugBank API에서 MOA·DrugBank ID·기본 약물 정보 추출 (쿼리 성공 확인됨, 데이터 파싱 필요)
- TxGNN 예측 파이프라인 재실행하여 `predicted_indications` 확보
- 기존 적응증(`original_indications`) 보충 — DrugBank 또는 해당 허가 기관 허가사항 참조
- 허가 기관 허가사항 PDF 다운로드 및 주요 경고·금기 추출 (DG001, Blocking 수준 데이터 갭 해소)

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-05 | 삭제: “현재 한국 내 허가 기록이 없는 약물로” | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |
| 2026-11-05 | 삭제: “현재 AMANTADINE SULFATE의 한국 허가 기록이 없습니다 (총 0건)” | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

