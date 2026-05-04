---
layout: default
title: Anagrelide Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 72
evidence_level: L5
indication_count: 0
---

# Anagrelide Hydrochloride
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

# ANAGRELIDE HYDROCHLORIDE: 평가 보류 — TxGNN 예측 미생성

---

## 한 문장 요약

ANAGRELIDE HYDROCHLORIDE는 이번 Evidence Pack에서 기존 적응증 및 작용 기전 데이터가 확인되지 않았습니다.
TxGNN 모델의 신규 적응증 예측이 아직 생성되지 않아 재창출 후보를 평가할 수 없는 상태입니다.
필수 데이터 수집 완료 후 보고서 재발행이 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (데이터 없음) |
| 예측 신규 적응증 | 없음 (TxGNN 예측 미생성) |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | L5 (예측 미생성, 평가 불가) |
| 시판 현황 | 미상시 (未上市) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 신규 적응증 예측이 생성되지 않았으며, 기존 적응증·작용 기전·안전성 정보가 모두 누락되어 있어 재창출 평가를 진행할 수 없습니다.

**진행하려면 필요한 것:**
- TxGNN 예측 실행 (`predicted_indications` 생성)
- DrugBank API 조회를 통한 MOA 및 기존 적응증 확인 (query_log에 DrugBank 조회 성공 기록 존재 — 결과 파싱 필요)
- 허가 기관(TFDA/MFDS) 허가 정보 수집 (경고, 금기, 세포독성 분류 포함)
- `data_gaps` DG001(경고/금기, Blocking), DG002(MOA, High) 순서로 우선 해소
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

