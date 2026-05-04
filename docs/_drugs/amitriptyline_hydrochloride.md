---
layout: default
title: Amitriptyline Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 61
evidence_level: L5
indication_count: 0
---

# Amitriptyline Hydrochloride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Amitriptyline Hydrochloride: 예측 적응증 없음 — 데이터 불충분으로 평가 불가

---

## 한 문장 요약

Amitriptyline Hydrochloride에 대한 이번 Evidence Pack은 핵심 데이터가 모두 누락되어 있어 약물 재창출 평가를 진행할 수 없습니다. TxGNN 모델의 예측 적응증 결과가 포함되지 않았고, 기존 적응증·작용 기전·안전성 정보도 부재하여 현 시점에서의 평가는 **보류(Hold)** 가 불가피합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 |
| 예측 신규 적응증 | 정보 없음 (predicted_indications 비어 있음) |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | 해당 없음 (예측 결과 자체가 없음) |
| 시판 현황 | 미시판 (허가 0건) |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증이 전혀 포함되지 않아 재창출 후보 자체가 존재하지 않으며, 기존 적응증·작용 기전·안전성 데이터도 모두 누락되어 있어 보고서의 어떠한 분석 섹션도 생성할 수 없습니다.

**진행하려면 필요한 것:**

| 우선순위 | 항목 | 조치 |
|---------|------|------|
| 🔴 Blocking | TxGNN 예측 결과 | `predicted_indications` 배열이 비어 있음. DrugBank ID를 확인하고 예측 파이프라인을 재실행해야 함 |
| 🔴 Blocking | 허가 정보 / 안전성 경고 · 금기 | 공식 허가 데이터 소스에서 仿單 PDF 수집 및 파싱 필요 |
| 🟠 High | 작용 기전 (MOA) | DrugBank API 조회 (query_log에 따르면 drugbank 조회는 성공했으나 결과가 반영되지 않음 — 후처리 확인 필요) |
| 🟡 Medium | DrugBank ID | `drugbank_id` 값이 null. INN 기반 DrugBank 매핑 재시도 필요 |

> **참고:** query_log에 따르면 DrugBank 조회(`source: "drugbank"`)는 `result_status: "success"`, `result_count: 1`로 성공했음에도 불구하고 Evidence Pack에 MOA 및 DrugBank ID가 반영되지 않았습니다. 데이터 파이프라인의 파싱 또는 필드 매핑 로직을 점검하세요.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

