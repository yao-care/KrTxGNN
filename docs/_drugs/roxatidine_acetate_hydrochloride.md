---
layout: default
title: Roxatidine Acetate Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 294
evidence_level: L5
indication_count: 0
---

# Roxatidine Acetate Hydrochloride
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

# Roxatidine Acetate Hydrochloride: 파이프라인 재실행 필요

## 한 문장 요약

Roxatidine Acetate Hydrochloride는 H2 수용체 길항제 계열의 약물로, 위궤양·소화성 궤양 등 위산 과다 관련 질환 치료에 사용됩니다.
현재 Evidence Pack에는 **TxGNN 예측 적응증이 없으며**, DrugBank ID 미확인으로 인해 예측 파이프라인이 완료되지 않은 상태입니다.
작용 기전·안전성·시판 현황 모두 데이터 공백 상태이므로 추가 조치 없이는 평가를 진행할 수 없습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (허가 정보 미수집) |
| 예측 신규 적응증 | **없음** — TxGNN 예측 결과 미생성 |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | **L5** (모델 예측조차 없음) |
| 시판 현황 | 미상장 (허가증 0건) |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 이 예측이 타당한 이유는?

Roxatidine Acetate Hydrochloride는 H2 수용체를 선택적으로 차단하여 위산 분비를 억제하는 기전으로 알려진 약물입니다. 일본(상품명 Altat)을 비롯한 일부 아시아 국가에서 위·십이지장궤양 치료제로 허가된 이력이 있습니다.

그러나 본 Evidence Pack에서는 DrugBank ID가 확인되지 않아 TxGNN 지식 그래프 예측 파이프라인이 해당 약물을 처리하지 못했습니다. 예측 결과(`predicted_indications`)가 빈 배열로 반환되었기 때문에 신규 적응증 가능성을 현재 시점에서 평가할 수 없습니다.

MOA 상세 데이터도 수집되지 않아 기전 연관성 분석 역시 불가합니다. 알려진 H2 길항제 계열의 특성을 참고하되, DrugBank 연동이 완료된 후 공식 데이터에 기반한 재분석이 필요합니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
DrugBank ID 미확인으로 TxGNN 예측이 생성되지 않았으며, 작용 기전·경고·금기 등 모든 주요 평가 항목에 데이터 공백이 존재합니다. 현재 상태로는 재창출 가능성 판단이 불가합니다.

**진행하려면 필요한 것:**

- **[긴급]** DrugBank ID 확인: `ROXATIDINE ACETATE HYDROCHLORIDE` → DrugBank 직접 검색 후 `drug.drugbank_id` 업데이트
- **[긴급]** DrugBank ID 확인 후 TxGNN 예측 파이프라인 재실행 (`scripts/run_kg_prediction.py`)
- **[높음]** 작용 기전(MOA) 수집: DrugBank API 또는 문헌 검색
- **[높음]** 허가사항 수집: 주요국(일본 PMDA 등) 제품 정보 조회 후 경고·금기 항목 입력
- **[중간]** 한국 내 시판 현황 재확인: MFDS 허가 DB 검색 (`nedrug.mfds.go.kr`)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

