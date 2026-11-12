---
noindex: true
sitemap: false
layout: default
title: Amiodarone Hydrochloride
parent: 모델 예측만 (L5)
nav_order: 61
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Amiodarone Hydrochloride
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

## Amiodarone Hydrochloride: 데이터 부족 — 평가 보류
{: .text-alpha }

---

## 한 문장 요약

Amiodarone Hydrochloride는 DrugBank에서 약물 존재가 확인되었으나, 이번 Evidence Pack에는 기존 적응증·작용 기전·안전성 정보가 모두 수집되지 않았습니다.
TxGNN 모델의 예측 적응증이 **0건**으로, 재창출 후보로서의 기전 관련성 분석을 진행할 수 없습니다.
핵심 데이터 보완 후 재평가가 필요하며, 현재 단계에서는 **Hold** 결정을 권장합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | TxGNN 예측 없음 |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | 해당 없음 (예측 부재) |
| 한국 시판 현황 | 시판 중 (유효 허가 3건 / 전체 3건) |
| 허가증 수 | 3건 (유효 3건) |
| 권장 결정 | Hold |

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증이 없고, 기존 적응증·작용 기전(MOA)·안전성 데이터가 모두 미수집 상태입니다. 현재 단계에서 재창출 평가를 진행하기 어렵습니다.

<!-- review:begin kr-lic-20261105-amiodarone_hydrochloride-1 -->

> **검토 정정 (2026-11-05)**: 원래 문장: “한국 내 허가 이력도 없어 현재 단계에서 재창출 평가를 진행하기 어렵습니다.” 삭제: 허가가 취소되었거나 허가·시판되지 않는다고 했으나, 성분 기준으로 다시 맞춘 2026-11-05 기준 식품의약품안전처(nedrug) 허가 자료와 맞지 않습니다. 이 약의 허가는 3건(유효 3건)이며, 현재 수치는 빠른 개요와 「한국 시판 정보」의 표에 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261105-amiodarone_hydrochloride-1 -->

**진행하려면 필요한 것:**
- MFDS(식품의약품안전처) 허가 데이터 수집 및 기존 적응증 확인
- DrugBank API를 통한 DrugBank ID 및 MOA 확보 (DG002 해소)
- 허가사항 PDF 파싱을 통한 경고·금기 정보 수집 (DG001 해소, Blocking)
- 위 데이터 보완 후 TxGNN 예측 재실행

---

> **참고:** DrugBank 쿼리(2026-03-27)에서 1건의 결과가 확인되었으나, `drugbank_id` 및 MOA 등 구조화된 데이터가 Evidence Pack에 반영되지 않았습니다. 파이프라인 상의 매핑 실패 여부를 점검하시기 바랍니다.

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-05 | 삭제: “한국 내 허가 이력도 없어” | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

