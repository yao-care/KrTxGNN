---
layout: default
title: Givosiran Sodium
parent: 僅模型預測 (L5)
nav_order: 265
evidence_level: L5
indication_count: 0
---

# Givosiran Sodium
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

txgnn-pipeline 스킬은 파이프라인 운영 지침이며, Evidence Pack 보고서 작성은 시스템 프롬프트 규칙을 따릅니다. 이제 Evidence Pack을 분석하여 보고서를 작성합니다.

---

**Evidence Pack 분석 결과:**

| 항목 | 값 | 비고 |
|------|-----|------|
| `drug.inn` | GIVOSIRAN SODIUM | ✓ |
| `drug.original_indications` | `[]` | 비어 있음 |
| `drug.original_moa` | `[Data Gap]` | 누락 |
| `predicted_indications` | `[]` | **예측 결과 없음** |
| `taiwan_regulatory.market_status` | `未上市` | 미시판 |
| `taiwan_regulatory.total_licenses` | `0` | |
| `safety.*` | 전부 `[Data Gap]` | 누락 |
| 데이터 갭 | DG001 (Blocking), DG002 (High) | |

`predicted_indications`가 빈 배열이므로 표준 재창출 평가 보고서 형식 적용 불가. 가용 데이터 기반으로 최대한 작성하고, 진행 불가 항목은 규칙에 따라 생략합니다.

---

# GIVOSIRAN SODIUM: 핵심 데이터 부재로 평가 보류

## 한 문장 요약

GIVOSIRAN SODIUM은 DrugBank 조회에서 1건이 확인되었으나, 기존 적응증·작용 기전·안전성 정보가 모두 수집되지 않은 상태입니다.
TxGNN 모델의 신규 적응증 예측이 아직 수행되지 않아 약물 재창출 평가를 진행할 수 없으며,
Blocking 수준 데이터 갭(DG001)이 해소될 때까지 **모든 평가 단계가 보류**됩니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | 없음 (TxGNN 예측 미수행) |
| TxGNN 예측 점수 | 없음 |
| 근거 수준 | L5 미만 (예측 데이터 부재) |
| 대만 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 모델 예측 결과가 존재하지 않고, 기존 적응증·작용 기전·허가사항 경고·금기 등 평가에 필수적인 핵심 데이터가 모두 누락되어 있습니다. Blocking 수준 데이터 갭(DG001)이 해소되지 않는 한 S1 안전성 초평가를 포함한 모든 후속 단계 진행이 불가합니다.

**진행하려면 필요한 것:**

| 갭 ID | 심각도 | 누락 항목 | 해소 방법 |
|-------|--------|-----------|----------|
| DG001 | **Blocking** | TFDA 허가사항 경고·금기 | TFDA 官網에서 仿單 PDF 다운로드 후 파싱 |
| DG002 | High | 작용 기전 (MOA) | DrugBank API 조회 (`drugbank_id` 수동 확인 필요) |
| — | Critical | TxGNN 예측 결과 | `scripts/run_kg_prediction.py` 실행 후 Evidence Pack 재생성 |
| — | High | 기존 적응증 | DrugBank 또는 TFDA 허가사항에서 확인 |
| — | Medium | 안전성 정보 (DDI) | DDI 데이터베이스 재조회 (현재 `not_found`) |

> **참고:** `query_log` 기준 DrugBank 조회는 성공(result\_count = 1)했으나 `drugbank_id`가 null로 기록되어 있습니다. 수동으로 매핑 결과를 확인하여 DrugBank ID를 확정한 뒤 MOA 및 안전성 데이터를 재수집하십시오.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

