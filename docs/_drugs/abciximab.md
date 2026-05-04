---
layout: default
title: Abciximab
parent: 僅模型預測 (L5)
nav_order: 13
evidence_level: L5
indication_count: 0
---

# Abciximab
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

Evidence Pack을 분석한 결과, `predicted_indications`가 빈 배열이고 `original_indications`도 미수록, 안전성 데이터도 모두 공백입니다. 작성 규칙에 따라 빈 섹션은 생략하고, 실제 데이터가 있는 항목만 포함한 보고서를 작성합니다.

---

# Abciximab: 예측 적응증 없음 — 데이터 보완 필요

## 한 문장 요약

Abciximab(DrugBank ID: DB00054)은 한국에 허가된 이력이 없는 약물로, 이번 Evidence Pack에는 기존 적응증 및 TxGNN 예측 적응증 데이터가 모두 포함되어 있지 않습니다. DrugBank 조회는 성공하였으나 작용 기전(MOA)을 포함한 핵심 정보가 수록되지 않았으며, 현재 상태에서는 재창출 가능성 평가를 완료할 수 없습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 미수록 (Evidence Pack 누락) |
| 예측 신규 적응증 | 예측 결과 없음 |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | 평가 불가 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 한국 시판 정보

현재 한국에 Abciximab 성분으로 등록된 허가증이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증이 없고, 기존 적응증·작용 기전(MOA)·안전성 데이터가 모두 누락되어 있어 재창출 가능성을 평가하기 위한 최소 요건을 충족하지 못합니다.

**진행하려면 필요한 것:**
- TxGNN 예측 파이프라인 실행 및 `predicted_indications` 데이터 생성
- DrugBank API에서 기존 적응증·작용 기전(MOA) 보완 (DG002, High)
- 한국 허가사항(경고, 금기) 확인 — 현재 미시판이므로 원산지국 허가사항(ReoPro 미국/유럽 SmPC) 대체 적용 검토 (DG001, Blocking)
- 위 데이터 수집 후 Evidence Pack v5 이상으로 재생성하여 본 평가 재개
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

