---
layout: default
title: Ambroxol Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 52
evidence_level: L5
indication_count: 0
---

# Ambroxol Hydrochloride
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

# AMBROXOL HYDROCHLORIDE: 재창출 평가 불가 — 데이터 미흡으로 Hold 권고

## 한 문장 요약

AMBROXOL HYDROCHLORIDE는 대만 허가 이력이 없어 기존 적응증을 확인할 수 없습니다.
TxGNN 예측 파이프라인이 이 약물에 대한 신규 적응증을 생성하지 못했으며,
작용 기전(MOA)·안전성·규제 데이터가 모두 수집되지 않아 현 단계에서는 평가를 진행할 수 없습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (대만 허가 이력 없음) |
| 예측 신규 적응증 | 없음 (TxGNN 예측 미생성) |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | L5 이하 (예측조차 없음) |
| 대만 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 이 예측이 타당한 이유는?

TxGNN 모델이 이 약물에 대한 예측 결과를 생성하지 않았습니다.
이는 약물이 지식 그래프(KG) 내에 노드로 존재하지 않거나, DrugBank ID 매핑이 실패하여 예측 파이프라인에 진입하지 못했을 가능성이 높습니다.

쿼리 로그에서 DrugBank 검색은 성공(result_count: 1)하였으나, DrugBank ID가 Evidence Pack에 포함되지 않았습니다.
이 불일치를 해결하지 않으면 기전 분석 및 재창출 가능성 평가를 수행할 수 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 결과가 없고, 대만 허가 이력·작용 기전·안전성 데이터가 모두 부재하여 재창출 가능성을 평가할 최소한의 근거조차 확보되지 않았습니다.

**진행하려면 필요한 것:**

- **[Blocking]** DrugBank ID 확인 — DrugBank API 재쿼리 후 `drugbank_id` 필드 보완
- **[Blocking]** TxGNN KG 내 노드 존재 여부 확인 — `data/external/drugbank_vocab.csv` 대조
- **[High]** 작용 기전(MOA) 수집 — DrugBank 약물 프로파일 파싱
- **[High]** 대만 허가 현황 재확인 — TFDA 데이터베이스에서 "AMBROXOL" 성분명으로 재검색 (조회 시 `AMBROXOL`과 `AMBROXOL HYDROCHLORIDE` 두 형태 모두 시도)
- DrugBank ID 확보 후 Evidence Pack을 v5로 재생성하여 재평가 진행
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

