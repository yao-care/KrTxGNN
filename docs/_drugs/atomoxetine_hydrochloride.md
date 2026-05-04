---
layout: default
title: Atomoxetine Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 94
evidence_level: L5
indication_count: 0
---

# Atomoxetine Hydrochloride
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

# Atomoxetine Hydrochloride: ADHD 치료제 — TxGNN 예측 후보 없음

## 한 문장 요약

Atomoxetine Hydrochloride는 선택적 노르에피네프린 재흡수 억제제(SNRI)로, 주의력결핍 과잉행동장애(ADHD) 치료에 사용되는 비자극성 약물입니다.
이번 분석 주기에서 TxGNN 모델은 **재창출 예측 후보를 생성하지 못했으며**, 작용 기전(MOA) 및 안전성 데이터가 모두 미수집 상태입니다.
현재 시판 허가 실적 또한 없어 독립적인 근거 평가가 불가능합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 미비 (허가 기록 없음) |
| 예측 신규 적응증 | 없음 (예측 미생성) |
| TxGNN 예측 점수 | — |
| 근거 수준 | L5 이하 — 예측 자체 없음 |
| 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 수집되지 않았습니다. Evidence Pack의 `original_moa` 필드가 비어 있으며, DrugBank 조회는 실행되었으나 MOA 정보가 패키지에 포함되지 않았습니다.

Atomoxetine은 일반적으로 시냅스 전 노르에피네프린 운반체(NET)를 선택적으로 차단하여 전전두엽 피질의 노르에피네프린 농도를 높이는 것으로 알려져 있습니다. 그러나 이 정보는 Evidence Pack 외부의 일반 약리학 지식에 근거한 것으로, 본 보고서의 근거로 사용하기 위해서는 DrugBank API를 통한 정식 데이터 수집이 선행되어야 합니다.

**TxGNN 예측 자체가 생성되지 않았으므로** 기전-적응증 연관성 분석은 이번 주기에서 수행할 수 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> **참고**: 경고·금기·약물상호작용(DDI) 데이터가 모두 수집되지 않았습니다. DDI 조회 결과 `not_found`(0건)이며, TFDA 仿單 경고/금기 수집이 차단 수준(Blocking) 데이터 갭으로 분류되어 있습니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 후보가 생성되지 않았고, 작용 기전·안전성·시판 허가 데이터가 모두 미비하여 재창출 타당성을 평가할 근거가 존재하지 않습니다.

**진행하려면 필요한 것:**

- **[Blocking]** TFDA 仿單 PDF 다운로드 및 경고·금기 항목 파싱 (`DG001`)
- **[High]** DrugBank API를 통한 MOA 데이터 수집 (`DG002`)
- TxGNN 파이프라인 재실행 — `predicted_indications` 배열이 비어 있는 원인 진단 필요
- 시판국 허가 데이터 확보 (한국 MFDS, 미국 FDA, 일본 PMDA 등)
- DDI 조회 재시도 (현재 `not_found` — 쿼리 방식 또는 데이터 소스 점검)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

