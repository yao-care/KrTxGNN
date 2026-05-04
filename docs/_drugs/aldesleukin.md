---
layout: default
title: Aldesleukin
parent: 僅模型預測 (L5)
nav_order: 33
evidence_level: L5
indication_count: 0
---

# Aldesleukin
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

# Aldesleukin: 예측 적응증 없음 — 평가 보류

## 한 문장 요약

Aldesleukin(DB00041)은 DrugBank에 등재된 약물로, DrugBank 쿼리는 성공적으로 완료되었습니다.
그러나 이번 Evidence Pack에는 기존 적응증 정보, TxGNN 예측 신규 적응증, 작용 기전(MOA) 데이터가 모두 수록되어 있지 않습니다.
현재 상태로는 약물 재창출 타당성 평가를 진행할 수 없으며, 추가 데이터 수집이 선행되어야 합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | 데이터 없음 |
| TxGNN 예측 점수 | 데이터 없음 |
| 근거 수준 | L5 이하 (예측 결과 없음) |
| 한국 시판 현황 | 미등록 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 Evidence Pack에 작용 기전(MOA) 및 기존 적응증 데이터가 포함되어 있지 않아 기전 기반 분석을 수행할 수 없습니다.

DrugBank 쿼리(DB00041)는 성공적으로 실행되었으나(result_count: 1), MOA 항목은 이번 Evidence Pack에 반영되지 않았습니다. TxGNN 예측도 실행되지 않아 신규 적응증 후보가 없는 상태입니다.

추후 DrugBank API를 통해 MOA를 확인한 뒤 TxGNN 예측을 실행하면 기전 기반 분석이 가능해질 것입니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 적응증 데이터가 전무하고, 기존 적응증·작용 기전·안전성 정보 모두 누락된 상태입니다. Evidence Pack 필수 항목이 충족되지 않아 약물 재창출 평가를 진행할 수 없습니다.

**진행하려면 필요한 것:**
- **TxGNN 예측 실행**: 약물-질병 적합성 예측 점수 산출 (최우선)
- **MOA 데이터 수집**: DrugBank API 조회 (DB00041, severity: High)
- **기존 적응증 확인**: 한국 외 국가(미국 FDA, EMA 등) 허가 현황 조회
- **안전성 정보 확인**: 식품의약품안전처 허가사항 또는 해외 허가사항 PDF 분석 (severity: Blocking)
- **DDI 데이터 확인**: 약물 상호작용 쿼리 재실행 (현재 not_found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

