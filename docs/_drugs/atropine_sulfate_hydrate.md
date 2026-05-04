---
layout: default
title: Atropine Sulfate Hydrate
parent: 僅模型預測 (L5)
nav_order: 103
evidence_level: L5
indication_count: 0
---

# Atropine Sulfate Hydrate
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

# Atropine Sulfate Hydrate: 평가 불가 — TxGNN 예측 데이터 없음

## 한 문장 요약

Atropine Sulfate Hydrate는 항콜린성 약물 계열로 알려진 성분이나, 이번 Evidence Pack에는 기존 적응증 및 TxGNN 예측 결과가 모두 포함되어 있지 않습니다.
한국 내 허가 이력이 전무하고, 작용 기전(MOA)·경고·금기 등 핵심 데이터가 누락되어 있어 **현재 상태로는 약물 재창출 평가를 진행할 수 없습니다.**
데이터 수집 완료 후 파이프라인 재실행이 선행되어야 합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | 데이터 없음 (TxGNN 예측 미생성) |
| TxGNN 예측 점수 | — |
| 근거 수준 | L5 (실제 연구 없음, 모델 예측조차 없음) |
| 한국 시판 현황 | 미허가 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

이번 Evidence Pack에는 TxGNN 예측 결과(`predicted_indications`)가 포함되어 있지 않아 기전 연관성 분석을 수행할 수 없습니다. 해당 약물이 한국 의약품 데이터베이스에 등록되어 있지 않아 TxGNN 파이프라인이 DrugBank ID 매핑 단계를 통과하지 못했을 가능성이 높습니다.

작용 기전(MOA) 데이터 역시 누락(`[Data Gap]`)되어 있습니다. 조회 로그(query_log)를 보면 DrugBank 쿼리는 성공(`result_status: success`, `result_count: 1`)으로 기록되어 있으나 `drugbank_id`가 최종적으로 채워지지 않았습니다. 이 불일치를 먼저 해소해야 MOA 및 안전성 분석이 가능합니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 결과가 없고, 한국 내 허가 이력이 없으며, MOA·경고·금기 등 평가에 필수적인 데이터가 모두 누락되어 있어 재창출 가능성을 판단할 근거가 전혀 없습니다.

**진행하려면 필요한 것:**

- **[DG002 해소]** DrugBank API 재조회를 통해 `drugbank_id` 및 MOA 데이터 확보 (query_log에 성공 기록이 있으나 ID 미수집 — 원인 규명 필요)
- **[DG001 해소]** 한국 MFDS 또는 해외 규제기관(FDA, EMA 등) 허가사항에서 경고·금기 데이터 수집
- **TxGNN 파이프라인 재실행** — DrugBank ID 확보 후 예측 재실행하여 `predicted_indications` 생성
- **기존 적응증 정의** — 허가사항 기반으로 `original_indications` 필드 보완 후 재평가 의뢰
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

