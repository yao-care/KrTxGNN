---
layout: default
title: Atorvastatin Calcium
parent: 僅模型預測 (L5)
nav_order: 95
evidence_level: L5
indication_count: 0
---

# Atorvastatin Calcium
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

# Atorvastatin Calcium: 데이터 미완성으로 평가 보류

## 한 문장 요약

Atorvastatin Calcium은 스타틴 계열 약물로 알려져 있으나, 이번 Evidence Pack에는 허가 적응증, TxGNN 예측 결과, 안전성 정보가 모두 포함되어 있지 않습니다. 파이프라인 식별 오류(`candidate_id: TW-UNKNOWN-multi`)로 인해 약물 데이터가 정상적으로 수집되지 않았으며, 의미 있는 약물 재창출 평가를 진행할 수 없는 상태입니다. 차단 수준 데이터 오류(DG001: Blocking) 해소 후 재처리가 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 데이터 없음 |
| 예측 신규 적응증 | 없음 (TxGNN 예측 결과 없음) |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | L5 (예측 결과 없음, 지지 연구 없음) |
| 한국 시판 현황 | 미시판 (未上市) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
이번 Evidence Pack은 `candidate_id: TW-UNKNOWN-multi`로, 파이프라인 단계에서 약물 식별에 실패하였습니다. TxGNN 예측 결과, 허가 데이터, 안전성 정보가 모두 누락되어 있어 약물 재창출 평가를 수행할 근거가 없습니다.

**진행하려면 필요한 것:**

- **[DG001 — Blocking]** TFDA/MFDS 허가사항(仿單) PDF 수집 및 파싱 → 경고·금기 데이터 확보
- **[DG002 — High]** DrugBank API로 `drugbank_id` 및 MOA 데이터 재조회
- 약물명 정규화 재실행: `ATORVASTATIN CALCIUM` → `Atorvastatin` INN 매핑 확인 후 KG 예측 파이프라인 재처리
- TxGNN 예측 파이프라인 재실행 후 `predicted_indications` 정상 생성 여부 확인

> **참고**: Atorvastatin Calcium은 국제적으로 광범위하게 시판 중인 스타틴 계열 약물(Lipitor 등)입니다. `시판 현황: 未上市`, `허가증 수: 0`은 파이프라인 내 약물명 매핑 오류일 가능성이 높습니다. 데이터 재처리 시 매핑 로직을 우선 점검하세요.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

