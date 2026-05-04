---
layout: default
title: Belotecan
parent: 僅模型預測 (L5)
nav_order: 130
evidence_level: L5
indication_count: 0
---

# Belotecan
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

# Belotecan (DB12459): 예측 데이터 부족 — 평가 보류

## 한 문장 요약

Belotecan은 DrugBank(DB12459)에 등재된 약물로, 기존 적응증 및 작용 기전 데이터가 이번 Evidence Pack에 포함되어 있지 않습니다.
TxGNN 예측 결과(`predicted_indications`)가 생성되지 않아 재창출 후보 적응증 분석이 불가능하며,
안전성·규제 정보 역시 대부분 누락되어 있어 전체적인 평가를 위한 추가 데이터 수집이 선행되어야 합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | 예측 결과 없음 |
| TxGNN 예측 점수 | — |
| 근거 수준 | L5 (모델 예측 미생성) |
| 시판 현황 | 미허가 (Taiwan 기준) |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 데이터 현황

이번 Evidence Pack 수집 과정에서 확인된 데이터 격차는 다음과 같습니다.

| 항목 | 상태 | 중요도 | 비고 |
|------|------|--------|------|
| TxGNN 예측 결과 | 미생성 | 致命的 | 재창출 평가의 핵심 입력값 |
| 원래 적응증 | 누락 | 높음 | DrugBank API 추가 조회 필요 |
| 작용 기전 (MOA) | 누락 | 높음 | 기전 연관성 분석 불가 |
| 안전성 (경고/금기) | 누락 | 차단 | DDI 조회 결과 없음 |
| 규제 허가 정보 | 없음 | 중간 | Taiwan 0건, 국내 MFDS 조회 필요 |

> DrugBank 조회는 성공(1건 반환)하였으나, MOA·적응증 등 세부 내용이 Evidence Pack에 반영되지 않아 재확인이 필요합니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
`predicted_indications` 배열이 비어 있어 TxGNN이 예측한 재창출 후보 적응증이 없고, 원래 적응증·작용 기전·안전성 데이터도 모두 누락되어 있어 약물 재창출 가능성을 체계적으로 평가할 수 없습니다.

**진행하려면 필요한 것:**

- **[필수]** TxGNN 예측 파이프라인 재실행 → `predicted_indications` 생성
- **[필수]** DrugBank API 재조회 → MOA, 원래 적응증, 약물 카테고리 확보
- **[필수]** 한국 MFDS 허가 정보 조회 → Belotecan은 국내에서 소세포폐암·난소암 적응증으로 허가된 이력이 있을 수 있음 (CamtoHex 상품명 확인 필요)
- **[권장]** 안전성 정보 수집 → MFDS 또는 한국 허가 仿單 PDF 파싱
- **[권장]** DDI 데이터베이스 재조회 → 현재 `not_found` 상태, 다른 소스 시도 필요
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

