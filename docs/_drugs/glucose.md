---
layout: default
title: Glucose
parent: 모델 예측만 (L5)
nav_order: 356
evidence_level: L5
indication_count: 0
---

# Glucose
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **0** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 약사 평가 보고서

</div>

`txgnn-pipeline` 스킬은 파이프라인 운영 관련 안내이며, 이 작업(Evidence Pack → 보고서 생성)은 시스템 프롬프트의 보고서 양식이 전면 적용됩니다. Evidence Pack을 분석 후 보고서를 생성합니다.

---

**Evidence Pack 분석 결과:**

| 항목 | 상태 |
|------|------|
| `drug.inn` | GLUCOSE |
| `drug.drugbank_id` | null |
| `drug.original_indications` | 비어 있음 |
| `drug.original_moa` | [Data Gap] |
| `predicted_indications` | **비어 있음 (예측 결과 없음)** |
| `taiwan_regulatory.market_status` | Not marketed |
| `taiwan_regulatory.total_licenses` | 0건 |
| `safety.*` | 전 항목 [Data Gap] |

---

# GLUCOSE: 약물 재창출 평가 불가 — 예측 적응증 없음

## 한 문장 요약

GLUCOSE(포도당)는 DrugBank 조회에서 인식되었으나, 이번 평가 주기에서 TxGNN 모델이 유효한 재창출 적응증을 예측하지 못하였습니다.
허가 이력이 없고 안전성 데이터도 확보되지 않아, 현 단계에서 약물 재창출 평가를 진행할 수 없습니다.
데이터 격차(DG001, DG002)를 우선 해소한 뒤 재평가가 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 이력 없음 |
| 예측 신규 적응증 | 예측 결과 없음 |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | N/A |
| 시판 현황 | ✗ 미시판 (Not marketed) |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증이 없고 허가 데이터 및 안전성 정보도 전무하여, 재창출 평가를 위한 최소한의 근거가 확보되지 않은 상태입니다.

**진행하려면 필요한 것:**
- **[DG001 — Blocking]** 허가사항(仿單) 입수: 공식 기관 사이트에서 PDF 다운로드 후 경고·금기 항목 파싱
- **[DG002 — High]** 작용 기전(MOA) 확보: DrugBank API 재조회 또는 DrugBank 페이지 수동 확인
- DrugBank ID 확인: DrugBank 조회(`query_log` id=2)에서 1건이 반환되었으나 `drugbank_id`가 기록되지 않음 — ID 값 저장 필요
- 위 항목 확보 후 TxGNN 예측 파이프라인 재실행 및 Evidence Pack v5 재생성
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

