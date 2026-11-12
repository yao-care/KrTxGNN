---
noindex: true
sitemap: false
layout: default
title: Azacitidine
parent: 모델 예측만 (L5)
nav_order: 111
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Azacitidine
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

Evidence Pack에 예측 적응증이 없고 핵심 데이터가 모두 미수집 상태입니다. 규칙에 따라 데이터가 없는 섹션은 전부 생략하고, 현황을 정확히 반영한 보고서를 작성합니다.

---

## Azacitidine: 평가 보류 — 예측 적응증 미수집
{: .text-alpha }

## 한 문장 요약

Azacitidine(DrugBank ID: DB00928)은 이번 Evidence Pack에는 기존 적응증과 TxGNN 예측 적응증이 포함되어 있지 않습니다. 작용 기전(MOA), 경고·금기 등 핵심 안전성 데이터도 미수집 상태로, 약물 재창출 가능성 평가를 위해서는 추가 데이터 수집이 선행되어야 합니다.

<!-- review:begin kr-lic-20261105-azacitidine-1 -->

> **검토 정정 (2026-11-05)**: 원래 문장: “Azacitidine(DrugBank ID: DB00928)은 현재 한국 내 허가 이력이 없으며, 이번 Evidence Pack에는 기존 적응증과 TxGNN 예측 적응증이 포함되어 있지 않습니다.” 삭제: 허가가 취소되었거나 허가·시판되지 않는다고 했으나, 성분 기준으로 다시 맞춘 2026-11-05 기준 식품의약품안전처(nedrug) 허가 자료와 맞지 않습니다. 이 약의 허가는 6건(유효 6건)이며, 현재 수치는 빠른 개요와 「한국 시판 정보」의 표에 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261105-azacitidine-1 -->

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 |
| 예측 신규 적응증 | 없음 (TxGNN 예측 미실행) |
| TxGNN 예측 점수 | — |
| 근거 수준 | L5 이하 (예측 결과 없음) |
| 한국 시판 현황 | 시판 중 (유효 허가 6건 / 전체 6건) |
| 허가증 수 | 6건 (유효 6건) |
| 권장 결정 | Hold |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증이 없고, 기존 적응증·작용 기전·안전성 데이터가 모두 수집되지 않아 현 단계에서 재창출 평가를 진행할 수 없습니다.

**진행하려면 필요한 것:**
- 기존 허가 적응증 데이터 수집 (DrugBank 조회)
- 작용 기전(MOA) 데이터 수집 → DG002: DrugBank API 조회
- 안전성 데이터(경고·금기) 수집 → DG001: 허가사항 PDF 파싱 (Blocking)
- TxGNN 모델 예측 실행
- 약물 상호작용(DDI) 재조회

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-05 | 삭제: “현재 한국 내 허가 이력이 없으며” | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

