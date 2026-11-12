---
noindex: true
sitemap: false
layout: default
title: Atosiban Acetate
parent: 모델 예측만 (L5)
nav_order: 100
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Atosiban Acetate
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

Evidence Pack을 분석했습니다. 이 케이스는 예측 적응증·기존 적응증·MOA·안전성 데이터가 모두 부재한 최소 데이터 상태입니다. 프롬프트 규칙(빈 섹션 생략, [Data Gap] 출력 금지)에 따라 보고서를 작성합니다.

---

## ATOSIBAN ACETATE: 평가 불가 — 필수 데이터 부재
{: .text-alpha }

## 한 문장 요약

TxGNN 모델은 이 약물에 대한 재창출 적응증을 예측하지 못했고,
작용 기전(MOA)·안전성 정보가 모두 확보되지 않아 **근거 기반 평가 진행이 불가능한 상태**입니다.

<!-- review:begin kr-lic-20261031-atosiban_acetate-1 -->

> **검토 정정 (2026-10-31)**: 원래 문장: “ATOSIBAN ACETATE는 현재 한국 허가 이력이 없으며 시판되지 않는 약물입니다. / TxGNN 모델은 이 약물에 대한 재창출 적응증을 예측하지 못했고,” 삭제: 허가가 취소되었거나 허가·시판되지 않는다고 했으나, 성분 기준으로 다시 맞춘 2026-10-31 기준 식품의약품안전처(nedrug) 허가 자료와 맞지 않습니다. 이 약의 허가는 4건(유효 3건)이며, 현재 수치는 빠른 개요와 「한국 시판 정보」의 표에 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261031-atosiban_acetate-1 -->

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 한국 시판 현황 | 시판 중 (유효 허가 3건 / 전체 4건) |
| 허가증 수 | 4건 (유효 3건) |
| TxGNN 예측 적응증 | 없음 |
| 근거 수준 | 해당 없음 |
| 권장 결정 | **Hold** |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 결과가 없으며, 작용 기전·허가 정보·안전성 데이터가 모두 부재합니다. 현 상태에서는 재창출 가능성을 평가할 수 없습니다.

**진행하려면 필요한 것:**
- DrugBank API를 통한 DrugBank ID 및 MOA 확보 (DG002 — 우선순위: High)
- 한국 식약처(MFDS) 허가 이력 재확인
- TxGNN 모델에서 이 약물에 대한 예측 결과 재실행 여부 검토
- 경고 및 금기 등 안전성 정보 수집 (DG001 — 우선순위: Blocking)

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-10-31 | 삭제: “ATOSIBAN ACETATE는 현재 한국 허가 이력이 없으며 시판되지 않는 약물입니다” | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

