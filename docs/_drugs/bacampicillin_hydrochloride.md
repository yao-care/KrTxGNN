---
layout: default
title: Bacampicillin Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 117
evidence_level: L5
indication_count: 0
---

# Bacampicillin Hydrochloride
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

# Bacampicillin Hydrochloride: 예측 적응증 없음 — 평가 보류

## 한 문장 요약

Bacampicillin Hydrochloride는 페니실린계 항생제 Ampicillin의 전구약물(prodrug)로, 세균 감염 치료에 사용되는 것으로 알려져 있습니다.
그러나 이번 Evidence Pack에는 **TxGNN 예측 결과가 존재하지 않으며**, 대만(한국) 시판 이력도 없어 재창출 분석을 진행하기 위한 기본 데이터가 충족되지 않습니다.
현재 확보된 근거로는 재창출 방향성을 평가할 수 없습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (Evidence Pack에 미기재) |
| 예측 신규 적응증 | 없음 (TxGNN 예측 결과 없음) |
| TxGNN 예측 점수 | 없음 |
| 근거 수준 | L5 (모델 예측 없음, 실제 연구 미확인) |
| 한국 시판 현황 | 미상시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증이 존재하지 않아 재창출 가능성을 평가할 수 없으며, 해당 약물은 시판 이력이 없어 규제 정보도 확보되어 있지 않습니다. 아래 데이터 확보 없이는 평가를 진행하기 어렵습니다.

**진행하려면 필요한 것:**
- **[필수]** TxGNN 파이프라인에서 Bacampicillin Hydrochloride의 DrugBank ID 매핑 확인 및 예측 재실행 (`drugbank_id`가 `null`이므로 KG 예측 미수행된 가능성 있음)
- **[필수]** DrugBank API를 통해 작용 기전(MOA) 및 원래 적응증 정보 수집
- **[권장]** TFDA/MFDS 허가사항 PDF를 다운로드하여 경고 및 금기 항목 파싱
- **[참고]** 시판이 없는 약물의 경우, PubMed 및 ClinicalTrials.gov에서 직접 문헌/시험 검색 후 수동 Evidence Pack 보완 필요
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

