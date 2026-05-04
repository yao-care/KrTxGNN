---
layout: default
title: Acamprosate Calcium
parent: 僅模型預測 (L5)
nav_order: 15
evidence_level: L5
indication_count: 0
---

# Acamprosate Calcium
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

# ACAMPROSATE CALCIUM: 평가 보류 — TxGNN 예측 데이터 부재

## 한 문장 요약

ACAMPROSATE CALCIUM은 현재 대만 시장에 미등록된 약물입니다.
이번 Evidence Pack에는 TxGNN 예측 적응증 결과가 포함되어 있지 않으며,
작용 기전·안전성·허가 데이터도 미확보 상태로 약물 재창출 평가를 완료할 수 없습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | 없음 (TxGNN 예측 미실행) |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | L5 (모델 예측 없음, 실제 연구 확인 불가) |
| 대만 시판 현황 | 미상市 (허가증 0건) |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
`predicted_indications` 배열이 비어 있어 TxGNN이 제안한 신규 적응증이 없으며, 작용 기전(MOA)·허가 데이터·안전성 경고·금기가 모두 미확보 상태입니다. 재창출 타당성을 판단할 근거 자체가 없습니다.

**진행하려면 필요한 것:**

- **TxGNN 예측 실행**: 해당 약물에 대해 KG + DL 예측 파이프라인을 재실행하여 후보 적응증 목록 확보
- **DrugBank 데이터 통합**: query_log에 DrugBank 조회 성공(result_count: 1) 기록이 있으나 결과가 Evidence Pack에 누락됨 — DrugBank ID·MOA·카테고리 추출 필요
- **허가 현황 확인**: 대만 미상市이지만 글로벌(미국 FDA, EMA, 일본 PMDA 등) 허가 여부 확인 필요
- **안전성 정보 확보**: TFDA 또는 글로벌 허가 기관 공식 라벨에서 경고·금기 내용 파싱
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

