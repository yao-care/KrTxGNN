---
layout: default
title: Barnidipine Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 123
evidence_level: L5
indication_count: 0
---

# Barnidipine Hydrochloride
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

Evidence Pack를 분석했습니다. `predicted_indications`가 빈 배열이고 DrugBank ID 미매핑, 허가 데이터 전무 등 핵심 데이터 격차가 확인됩니다. 아래에 가용 데이터 기반으로 보고서를 생성합니다.

---

# Barnidipine Hydrochloride: TxGNN 예측 없음 — 재창출 평가 불가

## 한 문장 요약

Barnidipine Hydrochloride는 현재 이 Evidence Pack에 기존 적응증 정보가 포함되어 있지 않으며, 한국 내 허가 이력도 확인되지 않습니다.
TxGNN 모델의 신규 적응증 예측 결과가 존재하지 않아 약물 재창출 가능성 분석을 수행할 수 없습니다.
DrugBank 조회는 성공(1건)하였으나 ID 매핑이 누락된 상태로, 파이프라인 재실행 전 수동 검증이 선행되어야 합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 |
| 예측 신규 적응증 | 없음 (TxGNN 예측 결과 부재) |
| TxGNN 예측 점수 | N/A |
| 근거 수준 | 평가 불가 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 결과가 없고 기존 적응증·작용 기전·안전성 정보 모두 부재하여 약물 재창출 평가를 수행할 수 없습니다. 아래 데이터 격차를 해소한 후 파이프라인을 재실행해야 정식 평가가 가능합니다.

**진행하려면 필요한 것:**

- **DrugBank ID 수동 확인**: DrugBank 조회는 성공(1건)했으나 `drugbank_id` 필드가 `null`로 매핑되지 않음 → DrugBank 웹사이트에서 "barnidipine" 직접 검색 후 ID 기입
- **작용 기전(MOA) 보완**: DrugBank API에서 `mechanism_of_action` 필드 추출 (조회 성공 이력 있음)
- **기존 적응증 데이터 확보**: MFDS 의약품통합정보시스템 또는 DrugBank `indication` 필드에서 확인
- **안전성 데이터 확보**: MFDS 허가사항 PDF 또는 DrugBank `toxicity` / `warnings` 필드 파싱
- **TxGNN KG·DL 예측 재실행**: DrugBank ID 확인 후 `run_kg_prediction.py` 및 `txgnn_model.py` 재수행
- **DDI 재조회**: DrugBank ID 확보 후 재검색 권장 (현재 drug name 기반 조회 실패)

> **참고**: Evidence Pack 메타데이터의 `data_gaps`에 DG001(TFDA 허가 경고·금기, Blocking) 및 DG002(MOA, High) 가 등록되어 있습니다. 특히 DG001은 안전성 초평가 진입을 차단하는 `Blocking` 등급으로, 우선 해소가 필요합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

