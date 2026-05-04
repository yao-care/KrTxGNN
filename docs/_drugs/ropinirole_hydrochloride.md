---
layout: default
title: Ropinirole Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 291
evidence_level: L5
indication_count: 0
---

# Ropinirole Hydrochloride
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

# Ropinirole Hydrochloride: 재창출 평가 불가 (데이터 부족)

## 한 문장 요약

Ropinirole Hydrochloride는 현재 한국에 허가 이력이 없는 약물입니다.
이번 Evidence Pack에는 TxGNN 예측 적응증 데이터가 포함되어 있지 않으며,
작용 기전 및 안전성 정보 역시 수집되지 않아 신규 적응증 평가를 진행할 수 없습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (한국 허가 이력 없음) |
| 예측 신규 적응증 | 없음 (예측 데이터 미수집) |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | 평가 불가 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

예측 적응증 데이터(`predicted_indications`)가 존재하지 않아 기전 연관성 분석을 수행할 수 없습니다.

작용 기전(MOA) 데이터 또한 수집되지 않았습니다. DrugBank 조회는 성공(`result_status: success`)으로 기록되어 있으나, 결과값이 Evidence Pack에 반영되지 않아 기전 기반 재창출 가능성을 평가할 수 없습니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 적응증 데이터, 작용 기전, 안전성 정보 등 핵심 평가 항목이 모두 누락되어 있어 현재 단계에서는 평가를 진행할 수 없습니다.

**진행하려면 필요한 것:**
- TxGNN 예측 파이프라인 재실행 (`predicted_indications` 생성 필요)
- DrugBank 조회 결과 Evidence Pack 반영 (조회 성공 기록이 있으나 MOA 미포함)
- 원내 또는 해외 허가사항 확보 (작용 기전, 경고, 금기 포함)
- 한국 MFDS 미허가 약물이므로, 해외(미국 FDA, EMA 등) 허가사항 기준으로 안전성 초평가 수행
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

