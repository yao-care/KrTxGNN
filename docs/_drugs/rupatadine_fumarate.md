---
layout: default
title: Rupatadine Fumarate
parent: 僅模型預測 (L5)
nav_order: 298
evidence_level: L5
indication_count: 0
---

# Rupatadine Fumarate
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

# Rupatadine Fumarate: 평가 데이터 부족으로 결론 보류

## 한 문장 요약

Rupatadine Fumarate는 약물 재창출 후보로 조회되었으나, 이번 Evidence Pack에는 TxGNN 예측 적응증 결과가 포함되어 있지 않습니다. 현재 예측 데이터, 작용 기전(MOA), 안전성 정보가 모두 누락되어 있어 정식 재창출 평가를 진행할 수 없으며, 핵심 데이터 보충 후 재평가가 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | 없음 (TxGNN 예측 결과 미수신) |
| TxGNN 예측 점수 | 산출 불가 |
| 근거 수준 | 평가 불가 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증이 존재하지 않아 재창출 방향성 자체를 설정할 수 없으며, 작용 기전 및 안전성 데이터도 모두 부재하여 후보 타당성을 판단할 근거가 전혀 없습니다.

**진행하려면 필요한 것:**

- **[최우선]** TxGNN 예측 파이프라인 재실행 — `repurposing_candidates.csv`에 Rupatadine Fumarate 포함 여부 확인 및 DrugBank ID 매핑 점검
- **[DG001 해소]** 규제 기관 허가 자료 수집 — MFDS(식약처) 의약품 허가 데이터베이스에서 허가 현황 및 경고/금기 사항 확인
- **[DG002 해소]** DrugBank API 조회 — Rupatadine Fumarate의 DrugBank ID 확보 후 MOA, 안전성, 약물 상호작용 데이터 수집
- 허가 데이터 수집 이후 Evidence Pack 재생성 및 본 보고서 업데이트
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

