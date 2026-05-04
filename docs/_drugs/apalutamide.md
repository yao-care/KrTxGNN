---
layout: default
title: Apalutamide
parent: 僅模型預測 (L5)
nav_order: 75
evidence_level: L5
indication_count: 0
---

# Apalutamide
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

Evidence Pack을 분석했습니다. `predicted_indications`가 비어 있고 대부분의 필드에 데이터가 없는 미완성 팩이므로, 해당 섹션을 생략하고 확보된 데이터만으로 보고서를 작성합니다.

---

# APALUTAMIDE: 예측 적응증 데이터 수집 필요

## 한 문장 요약

APALUTAMIDE(DrugBank ID: DB11901)는 현재 한국 미허가 약물로, 이번 Evidence Pack에는 TxGNN 예측 적응증 결과가 포함되어 있지 않습니다.
작용 기전(MOA), 원래 적응증, 안전성 데이터 등 핵심 항목이 모두 수집되지 않아 재창출 분석을 진행할 수 없는 상태이며, 데이터 보완 후 재평가가 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | 데이터 없음 |
| TxGNN 예측 점수 | 데이터 없음 |
| 근거 수준 | — (예측 결과 미생성) |
| 한국 시판 현황 | ✗ 미허가·미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증 목록(`predicted_indications`)이 비어 있어 재창출 후보 질환이 특정되지 않았습니다. 작용 기전, 원래 적응증, 안전성 데이터도 모두 확보되지 않아 분석을 진행할 수 없습니다.

**진행하려면 필요한 것:**

| 우선순위 | 항목 | 조치 방법 |
|---------|------|---------|
| 🔴 Blocking | TxGNN 예측 실행 (`predicted_indications` 생성) | `scripts/run_kg_prediction.py` 실행 후 Evidence Pack 재생성 |
| 🔴 Blocking | 규제기관 허가 데이터 확보 | 식약처(MFDS) 의약품 허가 데이터베이스 조회 |
| 🟠 High | 작용 기전 (MOA) 확보 | DrugBank API 조회 (`/drugs/DB11901`) |
| 🟠 High | 원래 적응증 텍스트 확보 | DrugBank categories 및 국내외 허가 정보 참조 |
| 🟡 Medium | 안전성 정보 (경고·금기·DDI) 확보 | 허가 주의사항(SPC) PDF 다운로드 후 파싱 |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

