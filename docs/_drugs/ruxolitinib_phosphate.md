---
noindex: true
sitemap: false
layout: default
title: Ruxolitinib Phosphate
parent: 모델 예측만 (L5)
nav_order: 677
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Ruxolitinib Phosphate
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

Evidence Pack을 분석했습니다. `predicted_indications`가 비어 있고 핵심 데이터가 대부분 누락된 특수 케이스입니다. 아래에 가용 데이터 기반 보고서를 작성합니다.

---

## Ruxolitinib Phosphate: 예측 적응증 없음 — 데이터 보강 후 재평가 필요
{: .text-alpha }

## 한 문장 요약

Ruxolitinib Phosphate는 이번 Evidence Pack에 기존 적응증 정보가 포함되어 있지 않으며, TxGNN 모델의 신규 적응증 예측 결과도 없습니다. 작용 기전(MOA)과 안전성 데이터가 모두 확보되지 않아 재창출 타당성 평가가 불가능한 상태입니다.

<!-- review:begin kr-lic-20261031-ruxolitinib_phosphate-1 -->

> **검토 정정 (2026-10-31)**: 원래 문장: “한국에서 현재 **미시판 상태**로 허가 내역이 없고, 작용 기전(MOA)과 안전성 데이터가 모두 확보되지 않아 재창출 타당성 평가가 불가능한 상태입니다.” 삭제: 허가가 취소되었거나 허가·시판되지 않는다고 했으나, 성분 기준으로 다시 맞춘 2026-10-31 기준 식품의약품안전처(nedrug) 허가 자료와 맞지 않습니다. 이 약의 허가는 4건(유효 4건)이며, 현재 수치는 빠른 개요와 「한국 시판 정보」의 표에 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261031-ruxolitinib_phosphate-1 -->

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 |
| 예측 신규 적응증 | 예측 결과 없음 |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | 해당 없음 (예측 결과 미포함) |
| 한국 시판 현황 | 시판 중 (유효 허가 4건 / 전체 4건) |
| 허가증 수 | 4건 (유효 4건) |
| 권장 결정 | **Hold** |

## 누락 데이터 현황

이번 Evidence Pack에는 재창출 평가에 필수적인 핵심 데이터가 다음과 같이 누락되어 있습니다:

| ID | 항목 | 심각도 | 영향 | 보완 방법 |
|----|------|--------|------|----------|
| DG001 | 허가 경고 / 금기 사항 | 차단 (Blocking) | 안전성 초평가 불가 | 허가 기관 공식 사이트에서 의약품 설명서 PDF 다운로드 후 파싱 |
| DG002 | 작용 기전 (MOA) | 높음 (High) | 기전 연관성 분석 불가 | DrugBank API 조회 |

> **참고:** `query_log`에 따르면 DrugBank 조회는 **성공**(result\_count: 1)하였으나, `drugbank_id` 필드에 값이 입력되지 않았습니다. DrugBank ID 추출 및 기재가 필요합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증 데이터가 없어 재창출 후보로서의 잠재력을 평가할 수 없으며, 작용 기전·안전성 경고·금기 등 핵심 데이터가 모두 누락되어 있습니다.

**진행하려면 필요한 것:**
- TxGNN 파이프라인 재실행 후 `predicted_indications` 결과 추가
- DrugBank 조회 결과(성공 확인됨)에서 `drugbank_id` 및 MOA 데이터 추출
- 허가 기관 의약품 설명서 파싱을 통한 경고/금기 항목 수집
- 기존 적응증(`original_indications`) 데이터 보완

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-10-31 | 삭제: “한국에서 현재 **미시판 상태**로 허가 내역이 없고” | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

