---
layout: default
title: Argatroban
parent: 僅模型預測 (L5)
nav_order: 81
evidence_level: L5
indication_count: 0
---

# Argatroban
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

# Argatroban: 항혈전 치료제 — 예측 적응증 없음

## 한 문장 요약

Argatroban은 직접 트롬빈 억제제(Direct Thrombin Inhibitor) 계열의 항혈전 약물입니다.
이번 Evidence Pack에는 TxGNN 모델의 예측 적응증이 포함되어 있지 않아 **신규 적응증 재창출 평가를 수행할 수 없습니다.**
현재 한국 내 미상시 상태이며, 안전성 및 작용 기전 데이터 모두 수집되지 않아 추가 데이터 보충이 선행되어야 합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (허가 이력 없음) |
| 예측 신규 적응증 | 예측 결과 없음 |
| TxGNN 예측 점수 | — |
| 근거 수준 | L5 (모델 예측 없음, 평가 불가) |
| 한국 시판 현황 | 미상시 (허가 이력 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 Evidence Pack에 작용 기전(MOA) 데이터가 포함되어 있지 않습니다.

알려진 약리학 정보에 따르면, Argatroban은 **직접 트롬빈 억제제(Direct Thrombin Inhibitor)** 로서 트롬빈의 활성 부위에 가역적으로 결합하여 혈전 형성을 억제합니다. 주요 임상 적용 분야는 헤파린 유도 혈소판감소증(HIT, Heparin-Induced Thrombocytopenia) 및 관련 혈전증 치료로 알려져 있습니다.

그러나 이번 Evidence Pack에는 **TxGNN 예측 결과(`predicted_indications`)가 없어** 기전 기반의 재창출 적응증 분석을 수행할 수 없습니다. 재창출 평가를 위해서는 예측 파이프라인 재실행이 필요합니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 결과가 없고, 작용 기전·안전성·허가 이력 등 핵심 데이터 모두 수집되지 않아 재창출 가능성을 평가할 근거가 전무합니다.

**진행하려면 필요한 것:**

- **[필수] TxGNN 예측 재실행** — `predicted_indications` 데이터 생성
- **[필수] DrugBank API 조회** — 작용 기전(MOA), 약물 카테고리, 독성 정보 보충 (DG002 해소)
- **[필수] MFDS/TFDA 허가 자료 확인** — 경고, 금기 사항 등 안전성 데이터 수집 (DG001 해소)
- **[권장] 한국 MFDS 등록 현황 재조회** — 미상시 상태 재확인 및 국내 허가 가능성 검토
- **[권장] ClinicalTrials.gov / CRIS / ICTRP 검색** — Argatroban 관련 기존 임상 근거 사전 수집
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

