---
layout: default
title: Amoxicillin Sodium
parent: 僅模型預測 (L5)
nav_order: 67
evidence_level: L5
indication_count: 0
---

# Amoxicillin Sodium
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

Evidence Pack을 분석합니다. `predicted_indications`가 비어 있고 허가 데이터·안전성 정보 모두 수집되지 않은 극단적 데이터 부족 케이스입니다. 규칙에 따라 빈 섹션은 생략하고, `[Data Gap]`은 출력하지 않으며, 실제 데이터만으로 보고서를 작성합니다.

---

# AMOXICILLIN SODIUM: 예측 적응증 없음 — 평가 보류

## 한 문장 요약

AMOXICILLIN SODIUM은 베타-락탐계 광역 스펙트럼 항생제로 알려진 약물입니다.
현재 Evidence Pack에는 **TxGNN 예측 적응증이 존재하지 않으며**, 허가 데이터·임상시험·문헌·안전성 정보 모두 수집되지 않았습니다.
최소한의 분석 근거가 확보되지 않아 정식 재창출 평가를 진행할 수 없습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 수집된 허가 데이터 없음 |
| 예측 신규 적응증 | TxGNN 예측 없음 |
| TxGNN 예측 점수 | — |
| 근거 수준 | L5 이하 (모델 예측조차 없음) |
| 시판 현황 | 미시판 (허가 이력 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 결과가 없고, 허가 데이터·안전성 정보·임상 근거 모두 수집되지 않아 재창출 후보로서의 타당성을 판단할 수 없습니다.

**진행하려면 필요한 것:**
- **DrugBank ID 확인** — `AMOXICILLIN SODIUM`의 DrugBank 매핑 성공(query_log #2에서 result_count=1) 결과를 파이프라인에 반영하여 `drugbank_id` 필드 채우기
- **TxGNN 예측 재실행** — DrugBank ID 확보 후 KG 예측 및 DL 예측 재실행하여 `predicted_indications` 생성
- **MOA 데이터 수집** — DrugBank API에서 작용 기전 조회 (Data Gap DG002 해소)
- **안전성 데이터 수집** — MFDS 또는 국내 허가 현황 확인, 주요 경고·금기·DDI 수집 (Data Gap DG001 해소)
- **적응증 데이터 확인** — `original_indications` 배열이 비어 있으므로 허가사항 원문에서 기존 적응증 추출 필요

> ⚠️ **참고**: `query_log #2` (DrugBank 조회)에서 `result_count: 1`이 반환되었으나 `drugbank_id`가 `null`로 남아 있습니다. 파이프라인 매핑 단계에서 오류가 발생했을 가능성이 있으므로 먼저 이 부분을 점검하시기 바랍니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

