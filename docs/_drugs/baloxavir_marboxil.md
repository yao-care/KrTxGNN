---
layout: default
title: Baloxavir Marboxil
parent: 僅模型預測 (L5)
nav_order: 120
evidence_level: L5
indication_count: 0
---

# Baloxavir Marboxil
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

# Baloxavir Marboxil: 재창출 평가 불가 — 핵심 데이터 보완 필요

---

## 한 문장 요약

Baloxavir Marboxil(DrugBank: DB13997)은 현재 한국 시판 기록이 없으며, Evidence Pack에는 기존 적응증 정보와 TxGNN 재창출 예측 결과가 모두 포함되어 있지 않습니다. 작용 기전(MOA), 안전성 경고, 허가 적응증 등 평가에 필수적인 핵심 데이터가 미확보된 상태로, 데이터 보완 후 재평가가 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (한국 허가 기록 없음) |
| 예측 신규 적응증 | 없음 (TxGNN 예측 결과 미산출) |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | L5 (예측 결과 없음, 평가 불가) |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 현재 평가 가능 여부

이 Evidence Pack(v4, 기준일: 2026-04-19)은 DrugBank 조회에는 성공하였으나, 재창출 평가에 필수적인 세 가지 데이터가 모두 누락되어 있습니다.

**누락 데이터 및 영향:**

| 데이터 | 심각도 | 영향 |
|--------|--------|------|
| 작용 기전 (MOA) | 높음 | 기전 관련성 분석 불가 |
| 허가사항 경고/금기 | 차단 (Blocking) | 안전성 초평가 진행 불가 |
| TxGNN 예측 적응증 | 차단 (Blocking) | 재창출 후보 없음, 보고서 핵심 섹션 작성 불가 |

현재 `predicted_indications` 배열이 비어 있어 임상시험 근거, 문헌 근거, 예측 타당성 섹션을 작성할 수 없습니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증이 산출되지 않았고, 안전성·MOA 등 평가 필수 데이터가 미확보 상태입니다. 데이터 보완 없이 재창출 평가를 진행할 수 없습니다.

**진행하려면 필요한 것:**

- **[DG001 — Blocking]** 식품의약품안전처(MFDS) 허가사항 PDF 수집 및 경고·금기 정보 파싱
- **[DG002 — High]** DrugBank API를 통한 MOA 데이터 확보 (DB13997)
- 한국 또는 주요국(미국 FDA, 일본 PMDA, 유럽 EMA) 허가 적응증 수집으로 `original_indications` 보완
- 위 데이터 확보 후 TxGNN 예측 파이프라인 재실행으로 `predicted_indications` 산출
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

