---
layout: default
title: Acipimox
parent: 僅模型預測 (L5)
nav_order: 21
evidence_level: L5
indication_count: 0
---

# Acipimox
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

# ACIPIMOX: 데이터 부족으로 평가 불가 — 보완 필요

## 한 문장 요약

ACIPIMOX(DB09055)는 Evidence Pack에 기존 적응증 및 TxGNN 예측 결과가 포함되어 있지 않아 약물 재창출 평가를 진행할 수 없는 상태입니다.
현재 한국(대만) 시판 이력도 없으며, 작용 기전·안전성 데이터 모두 수집되지 않아 **평가 자체가 Blocking 상태**입니다.
아래 섹션은 수집된 데이터 범위 내에서만 작성되었습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | 예측 결과 없음 |
| TxGNN 예측 점수 | — |
| 근거 수준 | L5 (모델 예측 없음, 실제 연구 확인 불가) |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 없습니다. DrugBank ID(DB09055)는 확인되었으나, TFDA(대만 식약처) 및 DrugBank API로부터 MOA 정보가 수집되지 않았습니다.

`predicted_indications` 배열이 비어 있어 TxGNN 모델이 이 약물에 대한 재창출 후보 적응증을 반환하지 않았습니다. 이는 지식 그래프 내 약물 노드 연결 부족, 또는 DrugBank 매핑 미완성으로 인한 것일 수 있습니다.

기전 연관성 분석 및 신규 적응증 타당성 검토는 MOA 데이터와 TxGNN 예측 결과가 보완된 이후에 진행 가능합니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 결과가 없고 작용 기전·안전성 데이터 모두 미수집 상태입니다. 현재 상태에서는 재창출 후보 평가를 위한 최소 근거가 확보되지 않았습니다.

**진행하려면 필요한 것:**

| 우선순위 | 항목 | 조치 방법 |
|---------|------|---------|
| Blocking | TFDA 허가사항(경고·금기) 수집 | TFDA 공식 사이트에서 仿單 PDF 다운로드 후 파싱 |
| High | 작용 기전(MOA) 확보 | DrugBank API 재조회 또는 PubMed 문헌 검색 |
| High | TxGNN 예측 재실행 | DrugBank 매핑 완성 후 `run_kg_prediction.py` 재실행 |
| Medium | PubMed 문헌 수동 검색 | ACIPIMOX + 적응증 키워드 조합으로 문헌 탐색 |

> **참고**: ACIPIMOX가 지식 그래프에 정상 연결되어 있는지 `data/external/drugbank_vocab.csv`에서 DB09055 존재 여부를 먼저 확인하세요.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

