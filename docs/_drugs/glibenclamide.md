---
layout: default
title: Glibenclamide
parent: 僅模型預測 (L5)
nav_order: 268
evidence_level: L5
indication_count: 0
---

# Glibenclamide
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

주어진 Evidence Pack을 분석합니다. `predicted_indications`가 비어 있고 핵심 데이터가 누락된 특수 케이스로, 빈 섹션은 모두 생략하고 보고서를 작성합니다.

---

# Glibenclamide: 평가 보류 — TxGNN 예측 데이터 없음

## 한 문장 요약

Glibenclamide는 설포닐우레아(Sulfonylurea) 계열의 경구 혈당강하제로, 제2형 당뇨병 치료에 사용되는 약물입니다.
이번 Evidence Pack에는 TxGNN 모델의 예측 적응증 데이터가 생성되지 않았으며, 작용 기전·경고/금기사항 등 핵심 정보도 수록되어 있지 않습니다.
현재 상태로는 약물 재창출 평가를 진행할 수 없으며, 데이터 격차 해소 후 재평가가 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 제2형 당뇨병 (Evidence Pack 미수록, 공지된 사실 기반) |
| 예측 신규 적응증 | 없음 (TxGNN 예측 결과 미생성) |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | L5 (예측 결과 없음) |
| 대만 시판 현황 | 미허가 (未上市) |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
이번 Evidence Pack에 TxGNN 예측 적응증 데이터(`predicted_indications`)가 포함되어 있지 않아 재창출 평가 자체를 진행할 수 없습니다. 대만 허가 이력도 없고 작용 기전·안전성 데이터도 누락된 상태로, 현재 근거로는 의사결정을 내리기 어렵습니다.

**진행하려면 필요한 것:**

- **[우선순위 1 — Blocking]** TxGNN 모델 예측 파이프라인 재실행 → `predicted_indications` 데이터 생성
- **[우선순위 2 — Blocking]** 허가사항(仿單) PDF 수집 및 경고/금기사항 파싱 (DG001 해소)
- **[우선순위 3 — High]** DrugBank API 조회를 통한 작용 기전(MOA) 확보 (DG002 해소)
- 원래 적응증 목록(`original_indications`) 및 DrugBank ID 수록
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

