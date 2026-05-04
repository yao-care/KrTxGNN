---
layout: default
title: Bazedoxifene Acetate
parent: 僅模型預測 (L5)
nav_order: 125
evidence_level: L5
indication_count: 0
---

# Bazedoxifene Acetate
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

`txgnn-pipeline` 스킬을 확인했습니다. 해당 스킬은 파이프라인 관리용이며, 이 작업(Evidence Pack → 보고서 생성)에 직접 적용되는 지침은 없습니다. Evidence Pack을 분석하여 보고서를 작성합니다.

---

**Evidence Pack 분석 결과:**

| 항목 | 상태 |
|---|---|
| predicted_indications | **빈 배열** — 예측 미생성 |
| original_indications | 빈 배열 |
| original_moa | [Data Gap] |
| taiwan_regulatory.licenses | 빈 배열 (미시판) |
| safety | 전 항목 [Data Gap] |

> 예측 후보가 없으므로 임상시험·문헌·시판정보·세포독성 섹션은 모두 생략됩니다.

---

# Bazedoxifene Acetate: 예측 데이터 없음 — 평가 보류

## 한 문장 요약

Bazedoxifene Acetate는 DrugBank에서 약물로 확인되었으나, 현재 시판 허가 이력이 없는 약물입니다.
TxGNN 파이프라인에서 신규 적응증 예측이 생성되지 않았으며,
작용 기전·안전성 정보 등 핵심 데이터가 누락되어 본격적인 재창출 평가를 진행할 수 없습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | 없음 (예측 미생성) |
| TxGNN 예측 점수 | N/A |
| 근거 수준 | L5 (예측 없음) |
| 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, Bazedoxifene Acetate는 **선택적 에스트로겐 수용체 조절제(SERM)** 계열의 약물로, 해외에서는 폐경 후 골다공증 치료제(Viviant®, Conbriza®) 또는 복합제(Duavee® — bazedoxifene + 결합형 에스트로겐) 형태로 허가된 바 있습니다.

그러나 Evidence Pack 내 DrugBank 조회 결과(result_count: 1)에도 불구하고 DrugBank ID 및 MOA 정보가 파이프라인에 반영되지 않았습니다. 예측된 신규 적응증이 없어 기전상 연관성 분석을 수행할 수 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측된 신규 적응증이 없고, 작용 기전(MOA)·안전성 정보(경고, 금기) 등 핵심 데이터가 누락되어 재창출 평가를 진행할 수 없습니다.

**진행하려면 필요한 것:**
- DrugBank API 재조회 → DrugBank ID 및 MOA 확보
- 원래 허가 적응증 데이터 확보 (해외 허가기관: EMA, FDA, PMDA)
- 안전성 정보 수집 — 경고·금기 항목 (TFDA/관할 허가기관 仿單/SmPC 다운로드)
- TxGNN 파이프라인 재실행하여 예측 후보 생성 (현재 `candidate_id: TW-UNKNOWN-multi` 상태)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

