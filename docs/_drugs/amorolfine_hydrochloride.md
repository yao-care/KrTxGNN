---
layout: default
title: Amorolfine Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 65
evidence_level: L5
indication_count: 0
---

# Amorolfine Hydrochloride
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

Evidence Pack을 분석합니다. `predicted_indications`가 비어 있고, 기존 적응증 및 MOA 데이터도 부재한 극히 제한적인 데이터셋임을 확인했습니다. 가용 데이터 기반으로 보고서를 작성합니다.

---

# Amorolfine Hydrochloride: 예측 신규 적응증 없음

## 한 문장 요약

Amorolfine Hydrochloride는 현재 한국에 허가 이력이 없는 약물입니다.
TxGNN 파이프라인에서 DrugBank 조회는 1건 성공했으나, DrugBank ID·작용 기전·기존 적응증이 Evidence Pack에 기록되지 않아 예측이 생성되지 않았습니다.
데이터 공백이 다수 존재하여 재창출 평가를 현 시점에서 수행할 수 없습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 기록 없음 |
| 예측 신규 적응증 | 예측 없음 |
| TxGNN 예측 점수 | — |
| 근거 수준 | L5 (예측 미생성) |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 파이프라인 현황

| 조회 항목 | 상태 | 비고 |
|----------|------|------|
| DrugBank 조회 | ✓ 성공 (1건) | DrugBank ID가 Evidence Pack에 미기록 |
| DDI 조회 | 결과 없음 | — |
| TxGNN 예측 | 미생성 | 입력 데이터(DrugBank ID, MOA) 누락으로 인한 파이프라인 미실행 |
| 한국 허가 데이터 | 없음 | 미시판 약물 |
| 작용 기전 (MOA) | 없음 | DrugBank 데이터 연계 필요 |
| 임상시험 / 문헌 | 없음 | 예측 없으므로 수집 미진행 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측이 생성되지 않았고, 약물의 핵심 기본 정보(DrugBank ID, MOA, 기존 적응증)가 확보되지 않아 재창출 평가의 어떤 단계도 수행할 수 없습니다.

**진행하려면 필요한 것:**
- DrugBank ID 확보 → Evidence Pack의 `drugbank_id` 필드 보완
- 작용 기전(MOA) 수집 → DrugBank API 또는 문헌 검색
- 기존 적응증 확정 → TFDA·EMA·FDA 허가 데이터 조회
- TxGNN 파이프라인 재실행 → 위 3개 항목 보완 후 재처리
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

