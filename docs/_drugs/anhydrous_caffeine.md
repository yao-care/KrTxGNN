---
layout: default
title: Anhydrous Caffeine
parent: 僅模型預測 (L5)
nav_order: 74
evidence_level: L5
indication_count: 0
---

# Anhydrous Caffeine
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

TxGNN 파이프라인 스킬은 데이터 파이프라인 관리용으로, 이 보고서 생성 태스크에는 적용되지 않습니다. 시스템 프롬프트의 보고서 형식 지침에 따라 바로 작성합니다.

---

# Anhydrous Caffeine: 기존 적응증 미확인 / 예측 적응증 없음

## 한 문장 요약

Anhydrous Caffeine은 현재 한국에 허가 이력이 없으며, DrugBank ID와 작용 기전 모두 확인되지 않은 약물입니다.
TxGNN 모델이 어떠한 신규 적응증도 예측하지 않았으며, 뒷받침하는 임상시험 및 문헌 근거 또한 수집되지 않았습니다.
데이터 부재로 인해 약물 재창출 가능성을 정식 평가할 수 없는 상태입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인되지 않음 |
| 예측 신규 적응증 | 없음 (TxGNN 예측 미생성) |
| TxGNN 예측 점수 | N/A |
| 근거 수준 | 평가 불가 (예측 없음) |
| 한국 시판 현황 | ✗ 미상장 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 모델이 신규 적응증을 예측하지 않았고, 약물 식별 정보(DrugBank ID)와 작용 기전(MOA)이 모두 누락되어 있어 재창출 가능성 평가가 불가능합니다.

**진행하려면 필요한 것:**
- DrugBank ID 확인 (DrugBank API 조회)
- 작용 기전(MOA) 데이터 수집
- 주요 규제기관(한국 MFDS 등) 기준 원래 허가 적응증 확인
- TFDA 仿單 또는 동등 허가사항의 경고·금기 안전성 정보 확보
- 올바른 DrugBank ID를 사용하여 TxGNN 예측 재실행
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

