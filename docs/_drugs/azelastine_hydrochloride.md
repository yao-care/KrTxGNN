---
layout: default
title: Azelastine Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 112
evidence_level: L5
indication_count: 0
---

# Azelastine Hydrochloride
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

# Azelastine Hydrochloride: 평가 불가 — 예측 데이터 미확보

## 한 문장 요약

Azelastine Hydrochloride는 Evidence Pack 기준으로 허가 이력이 없으며, 현재 TxGNN 예측 적응증 데이터가 전혀 포함되어 있지 않습니다. 작용 기전(MOA) 및 안전성 데이터도 확보되지 않아, 현 시점에서는 체계적인 약물 재창출 평가를 진행할 수 없는 상태입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 이력 없음 (허가증 0건) |
| 예측 신규 적응증 | TxGNN 예측 결과 없음 |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미허가 (未上市) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증이 없고, 시판 허가 이력이 없으며, 안전성·기전 데이터가 모두 미확보 상태입니다. Evidence Pack이 실질적인 재창출 후보 평가를 수행하기에 충분하지 않습니다.

**진행하려면 필요한 것:**
- TxGNN 모델 예측 실행 및 `predicted_indications` 결과 반영
- DrugBank API를 통한 작용 기전(MOA) 및 DrugBank ID 확보 (`DG002` 해소)
- TFDA/MFDS 仿單 기반 경고·금기 정보 수집 (`DG001` 해소, Blocking 항목)
- 임상시험 및 문헌 증거 수집 후 근거 수준 재판정
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

