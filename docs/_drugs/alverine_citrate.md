---
layout: default
title: Alverine Citrate
parent: 僅模型預測 (L5)
nav_order: 49
evidence_level: L5
indication_count: 0
---

# Alverine Citrate
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

# ALVERINE CITRATE: 재창출 평가 보류 — 핵심 데이터 부재

## 한 문장 요약

ALVERINE CITRATE는 현재 허가 이력이 없어 기존 적응증을 확인할 수 없습니다.
이번 Evidence Pack에는 TxGNN 예측 적응증이 포함되어 있지 않아, 신규 재창출 가능성 평가를 진행할 수 없습니다.
작용 기전, 안전성, 허가 데이터를 보완한 후 재평가가 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 미확인 (허가 데이터 없음) |
| 예측 신규 적응증 | 없음 (TxGNN 예측 부재) |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | L5 — 예측 없음, 실제 근거 없음 |
| 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 데이터 수집 현황

이번 조회에서 확인된 내용은 다음과 같습니다.

| 조회 일자 | 출처 | 결과 | 비고 |
|---------|------|------|------|
| 2026-03-27 | DrugBank | 성공 (1건 반환) | DrugBank ID가 Evidence Pack에 기록되지 않음 — 파싱 오류 가능성 |
| 2026-03-27 | DDI (약물상호작용) | 결과 없음 | — |

> **주의**: DrugBank 조회는 성공으로 기록되었으나 `drugbank_id` 필드가 비어 있습니다. Evidence Pack 생성 과정에서 파싱 단계에 문제가 있을 수 있으므로 원시 조회 결과를 직접 확인할 것을 권장합니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 데이터가 없고 원래 적응증·작용 기전·안전성 정보가 모두 부재하여, 재창출 후보 타당성을 평가할 수 있는 최소 요건이 충족되지 않습니다.

**진행하려면 필요한 것:**
- DrugBank 원시 조회 결과 재확인 및 `drugbank_id` 파싱 수정 (조회는 이미 성공한 상태)
- DrugBank에서 작용 기전(MOA), 적응증, 안전성(경고·금기) 정보 추출
- 관련 규제기관(MFDS, TFDA, EMA 등)에서 허가 여부 및 원래 적응증 확인
- DrugBank ID 확보 후 TxGNN 예측 파이프라인 재실행
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

