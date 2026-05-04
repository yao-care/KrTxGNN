---
layout: default
title: Azelnidipine
parent: 僅模型預測 (L5)
nav_order: 113
evidence_level: L5
indication_count: 0
---

# Azelnidipine
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

Evidence Pack를 분석합니다. 핵심 상황:

- `predicted_indications: []` — TxGNN 예측 결과 없음
- `taiwan_regulatory.market_status: "未上市"` — 미허가
- `original_moa: "[Data Gap]"` — MOA 없음
- 안전성 데이터 전체 부재

---

# AZELNIDIPINE: 예측 데이터 부족으로 평가 보류

## 한 문장 요약

AZELNIDIPINE(DB09230)은 현재 한국 미허가 약물로, 이번 평가에 필요한 기초 데이터가 수집되지 않았습니다.
TxGNN 모델의 신규 적응증 예측 결과가 생성되지 않았으며, 작용 기전(MOA) 및 안전성 데이터도 확인되지 않아
현 시점에서 정식 재창출 평가를 진행할 수 없습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인되지 않음 |
| 예측 신규 적응증 | 없음 (TxGNN 예측 결과 미생성) |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | L5 (예측 결과 없음) |
| 한국 시판 현황 | 미허가 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 AZELNIDIPINE에 대한 TxGNN 예측 결과가 없어 재창출 후보 적응증을 특정할 수 없습니다.
작용 기전(MOA) 데이터도 확보되지 않아 기전 기반의 유사 적응증 추론 또한 불가능합니다.

한국 식약처(MFDS) 허가 이력이 없고 DrugBank 외 추가 입력 데이터도 없는 상태로, 예측 파이프라인이 실행되었더라도 입력 품질의 한계로 결과 신뢰도를 보장하기 어렵습니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 결과가 존재하지 않으며, 평가에 필요한 MOA·안전성·규제 데이터가 모두 공백 상태입니다. 추가 데이터 수집 없이는 재창출 타당성 판단이 불가능합니다.

**진행하려면 필요한 것:**
- TxGNN 예측 파이프라인 재실행 및 `predicted_indications` 결과 생성 여부 확인
- DrugBank API를 통한 MOA 데이터 수집 (`DG002` 해소)
- 일본 PMDA 또는 기타 규제 기관 허가사항 참조로 원래 적응증 확인
- MFDS 또는 해외 허가 문서에서 안전성 정보(경고, 금기, 약물상호작용) 수집 (`DG001` 해소)
- 데이터 보완 후 Evidence Pack v5 재생성 및 평가 재개
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

