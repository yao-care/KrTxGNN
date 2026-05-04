---
layout: default
title: Rokitamycin
parent: 僅模型預測 (L5)
nav_order: 287
evidence_level: L5
indication_count: 0
---

# Rokitamycin
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

이 skill은 파이프라인 기술 작업용으로, 현재 보고서 생성 작업에는 해당되지 않습니다. Evidence Pack을 분석하여 보고서를 작성합니다.

---

Evidence Pack 핵심 파악:

- **predicted_indications**: 빈 배열 → TxGNN 예측 결과 없음
- **original_indications**: 빈 배열 → 기존 적응증 데이터 없음
- **taiwan_regulatory**: 미상시, 0건
- **safety**: 전체 [Data Gap]
- **original_moa**: [Data Gap]

---

# Rokitamycin: 예측 데이터 부재로 평가 보류

## 한 문장 요약

Rokitamycin(DB13409)은 DrugBank에 등재된 약물이나, 현재 Evidence Pack에 기존 적응증과 TxGNN 예측 적응증이 모두 존재하지 않습니다. 한국 내 허가 이력이 없고 작용 기전·안전성 데이터도 미확보 상태로, 약물 재창출 가능성을 평가하기 위한 최소 데이터 요건이 충족되지 않았습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | 데이터 없음 (TxGNN 예측 미실행 또는 결과 없음) |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | 평가 불가 (L5 미만 — 모델 예측 자체 부재) |
| 한국 시판 현황 | 미상시 (허가 이력 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 이 예측이 타당한 이유는?

현재 TxGNN 모델의 예측 결과가 없으며, 작용 기전(MOA) 정보도 확보되지 않은 상태입니다. 약물의 약리학적 특성과 기존 적응증이 모두 부재하므로, 신규 적응증과의 기전적 연관성 분석을 수행할 수 없습니다.

DrugBank(DB13409) 기록은 존재하나, 현재 Evidence Pack에 포함된 DrugBank 쿼리 결과에 MOA 정보가 누락되어 있어 추가 조회가 필요합니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증, 기존 적응증, 작용 기전, 안전성 정보가 모두 부재하여 약물 재창출 후보로서의 가능성을 평가할 수 없습니다. 핵심 데이터가 확보된 이후 재평가가 필요합니다.

**진행하려면 필요한 것:**
- DrugBank API 재쿼리를 통한 MOA·적응증·안전성 데이터 확보 (DG002 해소)
- TxGNN 예측 파이프라인 실행 및 `predicted_indications` 생성
- MFDS 또는 기타 국가 규제기관 허가 데이터 확인 (한국 시판 여부)
- 경고·금기·약물 상호작용 정보 수집 (DG001 해소)
- 임상시험(ClinicalTrials.gov, CRIS) 및 PubMed 증거 수집

---

> **참고:** 이 보고서는 Evidence Pack v4 (2026-04-20 기준) 데이터를 기반으로 작성되었습니다. Rokitamycin(DB13409)에 대한 필수 데이터가 확보되는 즉시 보고서를 갱신하시기 바랍니다.
>
> 본 보고서는 연구 참고용이며, 의료 조언을 구성하지 않습니다. 약물 재창출 후보는 임상 검증 이후에만 적용 가능합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

