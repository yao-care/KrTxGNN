---
layout: default
title: Azacitidine
parent: 僅模型預測 (L5)
nav_order: 109
evidence_level: L5
indication_count: 0
---

# Azacitidine
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

Evidence Pack에 예측 적응증이 없고 핵심 데이터가 모두 미수집 상태입니다. 규칙에 따라 데이터가 없는 섹션은 전부 생략하고, 현황을 정확히 반영한 보고서를 작성합니다.

---

# Azacitidine: 평가 보류 — 예측 적응증 미수집

## 한 문장 요약

Azacitidine(DrugBank ID: DB00928)은 현재 한국 내 허가 이력이 없으며, 이번 Evidence Pack에는 기존 적응증과 TxGNN 예측 적응증이 포함되어 있지 않습니다. 작용 기전(MOA), 경고·금기 등 핵심 안전성 데이터도 미수집 상태로, 약물 재창출 가능성 평가를 위해서는 추가 데이터 수집이 선행되어야 합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 |
| 예측 신규 적응증 | 없음 (TxGNN 예측 미실행) |
| TxGNN 예측 점수 | — |
| 근거 수준 | L5 이하 (예측 결과 없음) |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증이 없고, 기존 적응증·작용 기전·안전성 데이터가 모두 수집되지 않아 현 단계에서 재창출 평가를 진행할 수 없습니다.

**진행하려면 필요한 것:**
- 기존 허가 적응증 데이터 수집 (DrugBank 조회)
- 작용 기전(MOA) 데이터 수집 → DG002: DrugBank API 조회
- 안전성 데이터(경고·금기) 수집 → DG001: 허가사항 PDF 파싱 (Blocking)
- TxGNN 모델 예측 실행
- 약물 상호작용(DDI) 재조회
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

