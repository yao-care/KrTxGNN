---
layout: default
title: Atovaquone
parent: 僅模型預測 (L5)
nav_order: 99
evidence_level: L5
indication_count: 0
---

# Atovaquone
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

# Atovaquone: 예측 결과 없음 — 데이터 보완 후 재평가 필요

---

## 한 문장 요약

Atovaquone(아토바쿠온)은 DrugBank ID DB01117로 등록된 항감염제입니다.
이번 Evidence Pack에는 TxGNN 예측 결과, 작용 기전(MOA), 원래 적응증, 안전성 데이터가 모두 포함되어 있지 않습니다.
현 시점에서는 재창출 가능성을 평가할 수 없으며, 아래 누락 데이터를 보완한 후 재평가가 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | Evidence Pack에 미포함 |
| 예측 신규 적응증 | TxGNN 예측 없음 |
| TxGNN 예측 점수 | — |
| 근거 수준 | L5 (실제 연구 확인 불가) |
| 시판 현황 | 미시판 (허가 0건) |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 시판 정보

현재 허가된 제품이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 결과가 없으며 작용 기전·안전성 데이터가 모두 누락되어, 재창출 후보로서의 타당성을 판단할 근거가 없습니다.

**진행하려면 필요한 것:**
- TxGNN 모델 실행 및 예측 결과 수집 (predicted_indications 보완)
- 작용 기전(MOA) 데이터 확보 — DrugBank API 조회 (DG002)
- 원래 적응증(original_indications) 확인 — DrugBank 또는 허가사항 참조
- 안전성 데이터 확보 — 허가사항 PDF 파싱 (DG001)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

