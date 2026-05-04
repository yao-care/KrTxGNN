---
layout: default
title: Ampicillin Sodium
parent: 僅模型預測 (L5)
nav_order: 70
evidence_level: L5
indication_count: 0
---

# Ampicillin Sodium
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

Evidence Pack을 분석했습니다. `predicted_indications`가 빈 배열이고 주요 데이터가 누락되어 있어, 평가 불가 사유를 명시하는 보고서를 작성합니다.

---

# Ampicillin Sodium: 평가 불가 — 예측 적응증 데이터 없음

## 한 문장 요약

Ampicillin Sodium은 페니실린계 광역항생제로, 세균 감염 치료에 사용되는 약물입니다.
이번 Evidence Pack에는 TxGNN 모델의 예측 적응증 데이터가 포함되지 않았으며,
한국 허가 이력 및 안전성 정보도 확인되지 않아 **약물 재창출 평가를 진행할 수 없습니다.**

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | 없음 (TxGNN 예측 결과 미포함) |
| TxGNN 예측 점수 | 없음 |
| 근거 수준 | 평가 불가 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증 데이터가 없고, 기존 적응증·작용 기전(MOA)·안전성 데이터가 모두 누락되어 있어 재창출 후보로서의 타당성을 판단할 수 없습니다.

**진행하려면 필요한 것:**
- TxGNN 파이프라인 재실행 및 `predicted_indications` 데이터 확보 *(Blocking)*
- DrugBank API를 통한 DrugBank ID, 작용 기전(MOA), 기존 적응증 조회 *(High)*
- 한국 허가 데이터 (MFDS/식약처) 수집 — 현재 허가건수 0건으로 해외 허가 자료로 대체 필요 *(Medium)*
- 안전성 데이터 보완 — 경고, 금기, 약물 상호작용 *(Medium)*

---

> **Data Gaps 요약 (Evidence Pack DG001–DG002)**
>
> | ID | 항목 | 심각도 | 해결 방법 |
> |----|------|--------|----------|
> | DG001 | 허가사항 경고/금기 | Blocking | MFDS 허가사항 PDF 다운로드 및 파싱 |
> | DG002 | 작용 기전 (MOA) | High | DrugBank API 조회 |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

