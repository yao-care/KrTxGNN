---
layout: default
title: Agalsidase Beta
parent: 僅模型預測 (L5)
nav_order: 28
evidence_level: L5
indication_count: 0
---

# Agalsidase Beta
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

# Agalsidase Beta: 예측 적응증 없음 — 평가 보류 (Evidence Pack 불완전)

## 한 문장 요약

Agalsidase Beta(DB00103)는 현재 대만에 시판 허가 이력이 없으며, 이번 Evidence Pack에는 기존 적응증·작용 기전(MOA)·안전성 정보·TxGNN 예측 결과가 모두 누락되어 있습니다.
데이터 공백이 평가의 모든 핵심 항목에 걸쳐 있어, 이 상태로는 약물 재창출 후보로서의 타당성을 판단할 수 없습니다.
데이터 보완 후 Evidence Pack을 재구성하고 평가를 다시 시작해야 합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | 예측 없음 |
| TxGNN 예측 점수 | N/A |
| 근거 수준 | 평가 불가 |
| 대만 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
`predicted_indications` 배열이 비어 있어 TxGNN이 재창출 후보 적응증을 반환하지 않았습니다. 기존 적응증·MOA·안전성 데이터도 모두 누락되어 있어, 현 시점에서 재창출 가능성을 평가할 근거가 전혀 없습니다.

**진행하려면 필요한 것:**

- **[필수] TxGNN 예측 파이프라인 재실행** — DrugBank ID `DB00103`이 KG(knowledge graph)에 정상 매핑되는지 확인 후 예측 재수행
- **[필수] 작용 기전(MOA) 수집** — DrugBank API의 `mechanism-of-action` 필드 조회 (DG002 해소)
- **[필수] 기존 적응증 확인** — DrugBank `indication` 필드, PubMed, 또는 FDA 라벨을 통해 허가 적응증 확인
- **[권고] 안전성 데이터 수집** — TFDA 또는 EMA 허가 정보에서 경고·금기 항목 파싱 (DG001 해소)
- **[참고] 대만 허가 조회** — 현재 대만 시판 기록이 0건이므로, 글로벌 허가 현황(FDA·EMA)을 별도로 조회하여 규제 맥락 보완

---

> **참고:** Evidence Pack v4 기준으로 DrugBank 쿼리(`result_status: success`)는 성공하였으나, 해당 데이터가 파이프라인에 반영되지 않았습니다. `DB00103` 파싱 로직 및 필드 매핑을 우선 점검하십시오.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

