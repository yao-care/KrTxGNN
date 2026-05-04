---
layout: default
title: Amiodarone Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 59
evidence_level: L5
indication_count: 0
---

# Amiodarone Hydrochloride
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

# Amiodarone Hydrochloride: 데이터 부족 — 평가 보류

---

## 한 문장 요약

Amiodarone Hydrochloride는 DrugBank에서 약물 존재가 확인되었으나, 이번 Evidence Pack에는 기존 적응증·작용 기전·안전성 정보가 모두 수집되지 않았습니다.
TxGNN 모델의 예측 적응증이 **0건**으로, 재창출 후보로서의 기전 관련성 분석을 진행할 수 없습니다.
핵심 데이터 보완 후 재평가가 필요하며, 현재 단계에서는 **Hold** 결정을 권장합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | TxGNN 예측 없음 |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | 해당 없음 (예측 부재) |
| 한국 시판 현황 | 미시판 (허가 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증이 없고, 기존 적응증·작용 기전(MOA)·안전성 데이터가 모두 미수집 상태입니다. 한국 내 허가 이력도 없어 현재 단계에서 재창출 평가를 진행하기 어렵습니다.

**진행하려면 필요한 것:**
- MFDS(식품의약품안전처) 허가 데이터 수집 및 기존 적응증 확인
- DrugBank API를 통한 DrugBank ID 및 MOA 확보 (DG002 해소)
- 허가사항 PDF 파싱을 통한 경고·금기 정보 수집 (DG001 해소, Blocking)
- 위 데이터 보완 후 TxGNN 예측 재실행

---

> **참고:** DrugBank 쿼리(2026-03-27)에서 1건의 결과가 확인되었으나, `drugbank_id` 및 MOA 등 구조화된 데이터가 Evidence Pack에 반영되지 않았습니다. 파이프라인 상의 매핑 실패 여부를 점검하시기 바랍니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

