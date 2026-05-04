---
layout: default
title: Aripiprazole Monohydrate
parent: 僅模型預測 (L5)
nav_order: 84
evidence_level: L5
indication_count: 0
---

# Aripiprazole Monohydrate
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

# Aripiprazole Monohydrate: 평가 데이터 부족으로 보류

## 한 문장 요약

Aripiprazole Monohydrate에 대한 약물 재창출 평가가 요청되었으나, TxGNN 예측 적응증 및 기존 적응증 데이터가 모두 누락되어 있습니다.
현재 한국 내 허가 이력이 없으며, 안전성 정보(경고·금기·약물 상호작용) 역시 확인되지 않습니다.
필수 데이터 확보 후 재평가가 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | 데이터 없음 |
| TxGNN 예측 점수 | — |
| 근거 수준 | — |
| 한국 시판 현황 | ✗ 미허가 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증이 존재하지 않고, 기존 적응증·MOA·안전성 데이터가 모두 누락되어 있어 재창출 가능성을 평가할 수 없습니다.

**진행하려면 필요한 것:**
- TFDA 허가 경고·금기 정보 수집 — DG001 (Blocking): 안전성 초평가 진입 전 필수
- DrugBank ID 확인 및 MOA(작용 기전) 데이터 수집 — DG002 (High): 기전 연관성 분석에 필요
- TxGNN 예측 파이프라인 재실행으로 적응증 후보 생성 (현재 `predicted_indications: []`)
- 예측 결과 확보 후 임상시험·문헌 증거 수집 재진행
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

