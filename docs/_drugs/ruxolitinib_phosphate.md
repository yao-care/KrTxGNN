---
layout: default
title: Ruxolitinib Phosphate
parent: 僅模型預測 (L5)
nav_order: 299
evidence_level: L5
indication_count: 0
---

# Ruxolitinib Phosphate
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

Evidence Pack을 분석했습니다. `predicted_indications`가 비어 있고 핵심 데이터가 대부분 누락된 특수 케이스입니다. 아래에 가용 데이터 기반 보고서를 작성합니다.

---

# Ruxolitinib Phosphate: 예측 적응증 없음 — 데이터 보강 후 재평가 필요

## 한 문장 요약

Ruxolitinib Phosphate는 이번 Evidence Pack에 기존 적응증 정보가 포함되어 있지 않으며, TxGNN 모델의 신규 적응증 예측 결과도 없습니다. 한국에서 현재 **미시판 상태**로 허가 내역이 없고, 작용 기전(MOA)과 안전성 데이터가 모두 확보되지 않아 재창출 타당성 평가가 불가능한 상태입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 |
| 예측 신규 적응증 | 예측 결과 없음 |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | 해당 없음 (예측 결과 미포함) |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

## 누락 데이터 현황

이번 Evidence Pack에는 재창출 평가에 필수적인 핵심 데이터가 다음과 같이 누락되어 있습니다:

| ID | 항목 | 심각도 | 영향 | 보완 방법 |
|----|------|--------|------|----------|
| DG001 | 허가 경고 / 금기 사항 | 차단 (Blocking) | 안전성 초평가 불가 | 허가 기관 공식 사이트에서 의약품 설명서 PDF 다운로드 후 파싱 |
| DG002 | 작용 기전 (MOA) | 높음 (High) | 기전 연관성 분석 불가 | DrugBank API 조회 |

> **참고:** `query_log`에 따르면 DrugBank 조회는 **성공**(result\_count: 1)하였으나, `drugbank_id` 필드에 값이 입력되지 않았습니다. DrugBank ID 추출 및 기재가 필요합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증 데이터가 없어 재창출 후보로서의 잠재력을 평가할 수 없으며, 작용 기전·안전성 경고·금기 등 핵심 데이터가 모두 누락되어 있습니다.

**진행하려면 필요한 것:**
- TxGNN 파이프라인 재실행 후 `predicted_indications` 결과 추가
- DrugBank 조회 결과(성공 확인됨)에서 `drugbank_id` 및 MOA 데이터 추출
- 허가 기관 의약품 설명서 파싱을 통한 경고/금기 항목 수집
- 기존 적응증(`original_indications`) 데이터 보완
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

