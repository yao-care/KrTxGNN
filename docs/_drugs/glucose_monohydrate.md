---
layout: default
title: Glucose Monohydrate
parent: 僅模型預測 (L5)
nav_order: 273
evidence_level: L5
indication_count: 0
---

# Glucose Monohydrate
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

# GLUCOSE MONOHYDRATE: 데이터 부족으로 평가 불가

## 한 문장 요약

GLUCOSE MONOHYDRATE(포도당 일수화물)는 일반적으로 수액제 등에 사용되는 기본 영양 성분이나, 이번 Evidence Pack에는 허가 적응증, 예측 신규 적응증, 안전성 정보가 모두 수집되지 않았습니다.
TxGNN 모델이 예측한 신규 적응증이 없으며, 임상시험 및 문헌 근거도 확인되지 않아 **약물 재창출 평가를 진행할 수 없습니다.**

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 데이터 없음) |
| 예측 신규 적응증 | 없음 (TxGNN 예측 결과 없음) |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | L5 미만 (예측 결과 자체 없음) |
| 한국 시판 현황 | 미상 (대만 기준 미상시) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 모델이 이 약물에 대한 신규 적응증을 예측하지 못했으며, 허가 데이터·안전성 정보·임상 근거 모두 수집되지 않아 재창출 가능성을 평가할 수 없습니다.

**진행하려면 필요한 것:**

- **DrugBank ID 확보**: GLUCOSE MONOHYDRATE의 공식 DrugBank 등록 여부 확인 (포도당은 DB00174 등으로 등록되어 있을 수 있음)
- **INN 정규화**: "GLUCOSE MONOHYDRATE"가 "Dextrose" 또는 "Glucose"로 TxGNN 지식 그래프에 등록되어 있는지 확인 후 재쿼리 필요
- **허가사항 수집**: 식약처(MFDS) 의약품통합정보시스템에서 관련 허가 정보 조회
- **TxGNN 재실행**: 정규화된 INN으로 KG 예측 및 DL 예측 재실행
- **안전성 정보 보완**: DrugBank API를 통해 MOA, 경고, 금기 데이터 수집

> ⚠️ **참고**: GLUCOSE MONOHYDRATE는 수액·영양 보충 목적으로 광범위하게 사용되는 물질로, 재창출 연구 대상으로서의 적합성 자체도 검토가 필요합니다. 약물 식별자(INN/DrugBank ID)가 시스템에 올바르게 등록되었는지 먼저 확인하세요.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

