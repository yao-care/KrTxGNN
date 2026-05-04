---
layout: default
title: Amiloride Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 55
evidence_level: L5
indication_count: 0
---

# Amiloride Hydrochloride
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

Evidence Pack을 분석합니다. `predicted_indications`가 비어 있고 대부분 데이터가 미수집 상태임을 확인했습니다. 표준 보고서 형식을 최대한 준수하되, 실제 데이터에 맞게 조정하여 작성합니다.

---

# Amiloride Hydrochloride: 예측 적응증 데이터 없음 — 재평가 필요

## 한 문장 요약

Amiloride Hydrochloride는 포타슘 보존성 이뇨제 계열 약물로, DrugBank 조회는 성공적으로 완료되었으나 이번 Evidence Pack에 TxGNN 예측 적응증 정보가 포함되지 않아 정식 재창출 평가를 진행할 수 없습니다. 대만 내 시판 허가 이력이 없으며, 작용 기전(MOA) 및 안전성 데이터 모두 미수집 상태입니다. 재평가를 위해서는 TFDA 仿單 수집 및 TxGNN 예측 재실행이 선행되어야 합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | 예측 데이터 없음 |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | L5 (모델 예측 없음, 실제 연구 데이터 미수집) |
| 대만 시판 현황 | 미상시 (未上市) |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. DrugBank 조회는 성공적으로 완료되었으나(쿼리 로그 #2, 결과 1건), Evidence Pack에 MOA 정보가 포함되지 않았습니다.

예측 적응증이 존재하지 않아 기존 적응증과 신규 적응증 간의 기전 관련성 분석을 진행할 수 없습니다. 기전 분석을 수행하려면 DrugBank API에서 직접 MOA 및 약리 분류 데이터를 수집해야 합니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

*(예측 적응증 데이터가 확보되면 해당 적응증 기준으로 재조회 필요)*

---

## 문헌 근거

현재 관련 문헌이 없습니다.

*(예측 적응증 데이터가 확보되면 해당 적응증 기준으로 재조회 필요)*

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

*(TFDA 仿單 PDF 미수집 상태 — Data Gap DG001: Blocking 수준. DDI 조회 결과 없음)*

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증 데이터가 없어 재창출 타당성 평가 자체를 진행할 수 없습니다. 작용 기전(MOA), 안전성 경고/금기, 대만 허가 이력 모두 미수집 상태로, 최소 데이터 요건이 충족되지 않습니다.

**진행하려면 필요한 것:**
- **[Blocking]** TFDA 仿單 수집 — TFDA 공식 사이트에서 PDF 다운로드 후 경고/금기 파싱
- **[High]** DrugBank API를 통한 MOA, 약리 분류, 독성 데이터 수집 (`drugbank_id` 확인 필요)
- **[High]** TxGNN 모델 재실행 — `predicted_indications` 데이터 생성
- **[Medium]** DDI 데이터베이스 재조회 — 현재 `not_found` 상태로 확인 필요
- **[참고]** Amiloride는 국제적으로 고혈압·부종 적응증으로 허가된 약물이나, 대만 내 허가 이력이 없으므로 규제 경로 별도 검토 필요
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

