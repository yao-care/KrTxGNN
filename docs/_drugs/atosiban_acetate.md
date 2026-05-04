---
layout: default
title: Atosiban Acetate
parent: 僅模型預測 (L5)
nav_order: 98
evidence_level: L5
indication_count: 0
---

# Atosiban Acetate
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

Evidence Pack을 분석했습니다. 이 케이스는 예측 적응증·기존 적응증·MOA·안전성 데이터가 모두 부재한 최소 데이터 상태입니다. 프롬프트 규칙(빈 섹션 생략, [Data Gap] 출력 금지)에 따라 보고서를 작성합니다.

---

# ATOSIBAN ACETATE: 평가 불가 — 필수 데이터 부재

## 한 문장 요약

ATOSIBAN ACETATE는 현재 한국 허가 이력이 없으며 시판되지 않는 약물입니다.
TxGNN 모델은 이 약물에 대한 재창출 적응증을 예측하지 못했고,
작용 기전(MOA)·안전성 정보가 모두 확보되지 않아 **근거 기반 평가 진행이 불가능한 상태**입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 한국 시판 현황 | ✗ 미등록 |
| 허가증 수 | 0건 |
| TxGNN 예측 적응증 | 없음 |
| 근거 수준 | 해당 없음 |
| 권장 결정 | **Hold** |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 결과가 없으며, 작용 기전·허가 정보·안전성 데이터가 모두 부재합니다. 현 상태에서는 재창출 가능성을 평가할 수 없습니다.

**진행하려면 필요한 것:**
- DrugBank API를 통한 DrugBank ID 및 MOA 확보 (DG002 — 우선순위: High)
- 한국 식약처(MFDS) 허가 이력 재확인
- TxGNN 모델에서 이 약물에 대한 예측 결과 재실행 여부 검토
- 경고 및 금기 등 안전성 정보 수집 (DG001 — 우선순위: Blocking)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

