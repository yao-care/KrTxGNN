---
layout: default
title: Romosozumab
parent: 僅模型預測 (L5)
nav_order: 289
evidence_level: L5
indication_count: 0
---

# Romosozumab
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

# Romosozumab (DB11866): 증거 팩 불완전 — 재평가 필요

## 한 문장 요약

Romosozumab은 골 형성 촉진 기전의 단클론항체 계열 약물로, DrugBank (DB11866) 조회는 성공했습니다.
그러나 이번 증거 팩에는 **TxGNN 신규 적응증 예측 결과가 포함되지 않았으며**, 한국 허가 정보·안전성 데이터도 모두 누락되어 있습니다.
현재 상태로는 재창출 가능성 평가를 진행할 수 없어, **데이터 보완 후 재평가**가 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (증거 팩 미기재) |
| 예측 신규 적응증 | 해당 없음 (TxGNN 예측 미생성) |
| TxGNN 예측 점수 | N/A |
| 근거 수준 | L5 (예측 없음) |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 데이터 공백 현황

이번 증거 팩은 핵심 항목 전반에 걸쳐 데이터가 누락되어 있습니다.

| 항목 | ID | 상태 | 심각도 | 비고 |
|------|----|------|--------|------|
| TxGNN 예측 결과 | — | 미생성 | 치명적 | `predicted_indications` 배열 비어 있음 |
| 한국 허가 경고/금기 | DG001 | 미확인 | Blocking | 평가 진입 불가 |
| 작용 기전 (MOA) | DG002 | 미확인 | High | 기전 연관성 분석 불가 |
| 약물 상호작용 (DDI) | — | 조회 실패 | 중간 | `not_found` (2026-03-27 조회) |

> DrugBank 조회(2026-03-27)는 성공(1건)했으나, TxGNN 예측 파이프라인 결과가 증거 팩에 포함되지 않았습니다.
> 예측 파이프라인 재실행 또는 Evidence Pack 재생성이 필요합니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증이 없어 재창출 가능성을 평가할 수 없습니다. 허가 안전성 정보(DG001)와 MOA(DG002) 공백도 초기 스크리닝 진입을 막고 있습니다. 아래 항목을 보완한 후 증거 팩을 재생성해야 합니다.

**진행하려면 필요한 것:**

- **[필수]** TxGNN 예측 파이프라인 재실행 — DrugBank ID `DB11866` 기반 KG + DL 예측
- **[필수]** 한국 MFDS 허가 현황 확인 ([nedrug.mfds.go.kr](https://nedrug.mfds.go.kr)) — DG001 해소
- **[필수]** 한국 허가 의약품 설명서(仿單) 경고·금기 항목 추출 — DG001 해소
- **[권장]** DrugBank API 재조회로 MOA 데이터 보완 — DG002 해소
- **[권장]** DDI 조회 재시도 (이전 조회 결과: `not_found`)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

