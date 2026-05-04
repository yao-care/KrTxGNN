---
layout: default
title: Glipizide
parent: 僅模型預測 (L5)
nav_order: 271
evidence_level: L5
indication_count: 0
---

# Glipizide
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

# Glipizide (DB01067): 평가 보류 — 핵심 데이터 미수집

## 한 문장 요약

Glipizide(DrugBank ID: DB01067)는 현재 한국 미시판 약물로, 본 Evidence Pack에 기존 적응증·TxGNN 예측 적응증·안전성 정보가 모두 포함되어 있지 않습니다.
작용 기전(MOA)을 포함한 핵심 항목이 수집되지 않아 재창출 가능성 평가를 진행할 수 없는 상태입니다.
**데이터 수집 완료 후 재평가**가 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | 예측 결과 없음 |
| TxGNN 예측 점수 | — |
| 근거 수준 | 평가 불가 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 누락 데이터 현황

정식 평가를 차단하는 데이터 격차는 다음과 같습니다.

| ID | 누락 항목 | 심각도 | 영향 | 해결 방안 |
|----|-----------|--------|------|-----------|
| DG001 | 허가사항 경고 및 금기 (MFDS 仿單) | **Blocking** | 안전성 초평가 불가 | MFDS 공식 사이트에서 PDF 다운로드 및 파싱 |
| DG002 | 작용 기전 (MOA) | **High** | 기전 연관성 분석 불가 | DrugBank API 조회 |

> DG001이 **Blocking** 등급이므로, 이 항목이 해소되기 전까지 이후 모든 평가 단계를 시작할 수 없습니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증이 없고, 기존 적응증·작용 기전·안전성 정보 모두 수집되지 않아 재창출 후보로서의 타당성을 판단할 근거가 없습니다. 현 시점에서는 보고서 작성 자체가 불가합니다.

**진행하려면 필요한 것:**
- MFDS 허가사항 PDF 수집 및 파싱 → 경고·금기 추출 (DG001 해소)
- DrugBank API를 통한 MOA 데이터 확보 (DG002 해소)
- TxGNN 모델을 통한 신규 적응증 예측 실행 (`predicted_indications` 생성)
- 기존 허가 적응증 확인 및 `original_indications` 입력
- 위 데이터 보완 후 Evidence Pack v5 재생성 및 보고서 재실행
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

