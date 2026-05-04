---
layout: default
title: Artesunate
parent: 僅模型預測 (L5)
nav_order: 89
evidence_level: L5
indication_count: 0
---

# Artesunate
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

# Artesunate: 데이터 보완 필요 — 예측 생성 전 단계

---

## 한 문장 요약

Artesunate는 아르테미시닌(Artemisinin) 유도체 계열의 항말라리아 약물입니다.
이번 Evidence Pack에는 **TxGNN 예측 적응증이 포함되어 있지 않으며**, 한국 허가 이력도 없어
현재 상태로는 재창출 가능성 평가를 진행할 수 없습니다.
**2건의 Blocking/High 데이터 갭**이 해소되어야 다음 단계로 진행이 가능합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (Evidence Pack 내 기재 없음) |
| 예측 신규 적응증 | 없음 — TxGNN 예측 미수행 또는 미포함 |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | L5 (모델 예측 없음, 실제 연구 미확인) |
| 한국 시판 현황 | 미상장 (허가 이력 0건) |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, Artesunate는 아르테미시닌 반합성 유도체로, 중증 말라리아 치료에 사용되는 약물입니다. 그러나 본 Evidence Pack의 `original_moa` 항목은 데이터 갭 상태이며, 기전 관련성 분석을 진행하기 어렵습니다.

TxGNN 모델의 예측 결과(`predicted_indications`)가 비어 있어, 현재로서는 재창출 신규 적응증을 도출하거나 기전적 타당성을 검토할 수 없습니다. Evidence Pack `meta.inputs_received`에는 DrugBank만 포함되어 있고, TFDA 데이터 및 MOA 정보는 미수신 상태입니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

*(predicted_indications 데이터가 없어 신규 적응증 기준의 근거 검색이 수행되지 않았습니다.)*

---

## 문헌 근거

현재 관련 문헌이 없습니다.

*(predicted_indications 데이터가 없어 신규 적응증 기준의 문헌 검색이 수행되지 않았습니다.)*

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 결과가 Evidence Pack에 포함되어 있지 않으며, 한국 허가 이력이 없고, MOA 및 안전성 데이터 모두 미확보 상태입니다. 핵심 평가 데이터가 없는 상황에서 재창출 검토를 진행하는 것은 부적절합니다.

**진행하려면 필요한 것:**

| 우선순위 | 항목 | 조치 방법 | 심각도 |
|---------|------|----------|--------|
| 1 | TxGNN 예측 실행 (`predicted_indications`) | KG/DL 예측 파이프라인 재실행 | Blocking |
| 2 | TFDA 허가 경고 및 금기 데이터 | TFDA 공식 사이트에서 PDF 다운로드 후 파싱 | Blocking |
| 3 | 작용 기전 (MOA) | DrugBank API 조회 | High |
| 4 | 한국 시판 현황 재확인 | MFDS 허가 DB 조회 (nedrug.mfds.go.kr) | Medium |

---

> **참고**: 본 보고서는 연구 목적으로만 제공되며 의료 조언을 구성하지 않습니다. 약물 재창출 후보는 임상 검증을 거쳐야 합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

