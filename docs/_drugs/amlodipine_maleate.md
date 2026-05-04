---
layout: default
title: Amlodipine Maleate
parent: 僅模型預測 (L5)
nav_order: 63
evidence_level: L5
indication_count: 0
---

# Amlodipine Maleate
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

# AMLODIPINE MALEATE: 평가 보류 — 예측 적응증 데이터 없음

---

## 한 문장 요약

AMLODIPINE MALEATE는 암로디핀의 말레산염 형태로, TxGNN 재창출 파이프라인에 입력되었습니다.
그러나 현재 **예측된 신규 적응증이 존재하지 않으며**, 한국 시판 허가 이력 및 안전성 데이터 역시 확보되지 않아
본 Evidence Pack만으로는 약물 재창출 평가를 진행할 수 없는 상태입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인된 허가 적응증 없음 |
| 예측 신규 적응증 | 없음 (예측 결과 미생성) |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 결과(`predicted_indications`)가 비어 있어 재창출 후보 적응증 자체가 없으며, 작용 기전(MOA)·안전성 경고·금기 데이터가 모두 누락되어 있어 어떠한 평가 단계도 진행할 수 없습니다.

**진행하려면 필요한 것:**
- TxGNN 예측 결과(`predicted_indications`) 재실행 및 확보 — DrugBank ID 매핑 성공 여부 선확인 필요
- DrugBank API를 통한 DrugBank ID 및 작용 기전(MOA) 조회 (`query_log` ID 2는 `success`이나 `drugbank_id`가 여전히 `null` — 매핑 결과 검토 필요)
- MFDS 또는 TFDA 허가 데이터에서 적응증 및 안전성 정보(경고·금기) 수집
- Evidence Pack 재생성 후 v5 보고서 재발행
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

