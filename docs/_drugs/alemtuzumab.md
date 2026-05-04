---
layout: default
title: Alemtuzumab
parent: 僅模型預測 (L5)
nav_order: 34
evidence_level: L5
indication_count: 0
---

# Alemtuzumab
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

txgnn-pipeline 스킬은 파이프라인 운영 관련이며, 이 보고서 작성 작업에는 직접 적용되지 않습니다. Evidence Pack을 분석하여 지정된 형식으로 보고서를 작성합니다.

---

**Evidence Pack 분석:**
- `predicted_indications`: 빈 배열 → TxGNN 예측 없음
- `original_indications`: 빈 배열, MOA: [Data Gap]
- `taiwan_regulatory`: 미시판, 0건
- `safety`: 전체 [Data Gap]
- Data Gap DG001 (Blocking): 허가사항 경고/금기 미수집
- Data Gap DG002 (High): MOA 미수집

---

# Alemtuzumab: 예측 적응증 없음 — 데이터 보완 후 재평가 필요

## 한 문장 요약

Alemtuzumab(DrugBank ID: DB00087)은 현재 한국 미시판 의약품으로, 이번 Evidence Pack에는 TxGNN 예측 적응증이 포함되어 있지 않습니다. 작용 기전(MOA), 안전성 경고·금기 데이터가 모두 누락된 상태이며, 이로 인해 표준 재창출 평가 절차를 진행할 수 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (허가 이력 없음) |
| 예측 신규 적응증 | 예측 없음 |
| TxGNN 예측 점수 | N/A |
| 근거 수준 | 평가 불가 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

## 이 예측이 타당한 이유는?

현재 Evidence Pack의 `predicted_indications` 배열이 비어 있어 TxGNN 예측 결과가 존재하지 않습니다. 따라서 기전 관련성 분석, 기존 적응증과의 연관성 검토, 새로운 적응증으로의 전용 가능성 평가를 수행할 수 없습니다.

작용 기전(MOA) 데이터 역시 누락(DG002, High severity)되어 있어, 설령 예측 결과가 있더라도 기전 근거를 제시하기 어려운 상황입니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> ⚠️ **차단 데이터 갭(DG001 — Blocking):** 한국 허가사항의 경고 및 금기 정보가 아직 수집되지 않았습니다. 이 항목이 해소될 때까지 안전성 초기 평가(S1)를 진행할 수 없습니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증이 없고, 작용 기전(MOA)과 안전성 정보가 모두 누락되어 있어 재창출 후보로서의 타당성을 판단할 수 없습니다. 데이터 보완 없이는 다음 평가 단계로 진행할 수 없습니다.

**진행하려면 필요한 것:**
- **[Blocking]** 한국 허가사항 경고·금기 수집 — 식품의약품안전처(MFDS) 허가사항 PDF 다운로드 및 파싱
- **[High]** 작용 기전(MOA) 데이터 보완 — DrugBank API를 통해 DB00087 조회
- TxGNN 예측 파이프라인 재실행 및 `predicted_indications` 생성
- 예측 결과 생성 후 임상시험·문헌 증거 수집 재개
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

