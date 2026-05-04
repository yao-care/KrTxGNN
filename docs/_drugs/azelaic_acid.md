---
layout: default
title: Azelaic Acid
parent: 僅模型預測 (L5)
nav_order: 111
evidence_level: L5
indication_count: 0
---

# Azelaic Acid
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

이 스킬은 CLI 보고서 출력용이라 현재 작업에 적용되지 않습니다. Evidence Pack 기반 약물 재창출 평가 보고서를 바로 작성하겠습니다.

---

# Azelaic Acid: 재창출 후보 평가 불가 (데이터 부족)

## 한 문장 요약

Azelaic Acid(아젤라산, DB00548)는 한국 내 허가 이력이 없으며, 이번 Evidence Pack에는 원래 적응증 정보가 포함되어 있지 않습니다.
TxGNN 모델의 신규 적응증 예측 결과가 도출되지 않았으며, 작용 기전·안전성 데이터 모두 미확보 상태로, 현재로서는 재창출 타당성을 평가할 수 없습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (한국 미허가) |
| 예측 신규 적응증 | TxGNN 예측 결과 없음 |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | 해당 없음 (예측 데이터 없음) |
| 한국 시판 현황 | ✗ 미상시 |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 파이프라인에서 이 약물에 대한 재창출 후보 적응증이 도출되지 않았으며, 작용 기전(MOA)·안전성 데이터·한국 내 허가 정보가 모두 미확보 상태입니다. 평가에 필요한 최소 근거가 없어 진행이 불가합니다.

**진행하려면 필요한 것:**
- **[DG002 해소]** DrugBank API 조회를 통한 MOA(작용 기전) 데이터 확보
- **[DG001 해소]** MFDS(식품의약품안전처) 또는 TFDA 허가 데이터베이스에서 경고·금기 등 안전성 정보 수집
- TxGNN 파이프라인에서 DB00548 수동 입력 여부 확인 및 예측 재실행
- 한국 외 허가국(예: 미국 FDA, EMA) 적응증 정보를 보조 참고 자료로 확보하여 원래 적응증 기반 재창출 방향 탐색
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

