---
layout: default
title: Arotinolol Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 86
evidence_level: L5
indication_count: 0
---

# Arotinolol Hydrochloride
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

# Arotinolol Hydrochloride: 예측 적응증 데이터 없음 — 평가 보류

---

## 한 문장 요약

Arotinolol Hydrochloride는 베타차단·알파차단 계열 약물로 알려져 있으나, 현재 수신된 Evidence Pack에는 TxGNN 예측 적응증이 포함되어 있지 않습니다.
한국 내 시판 기록도 없으며, 작용 기전(MOA)과 허가 경고·금기 데이터 모두 누락되어 있어 약물 재창출 가능성을 정식 평가하기 위한 추가 데이터 확보가 선행되어야 합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 |
| 예측 신규 적응증 | 예측 결과 없음 |
| TxGNN 예측 점수 | — |
| 근거 수준 | L5 (예측 미실행) |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 결과(`predicted_indications`)가 없고, 기존 허가 적응증·MOA·안전성 데이터 모두 확보되지 않아 재창출 타당성을 판단할 수 없습니다.

**진행하려면 필요한 것:**
- TxGNN 예측 파이프라인 실행 결과 수신 (`predicted_indications` 배열 채움)
- 작용 기전(MOA) 데이터 — DrugBank API 조회 (DG002, High)
- 허가 경고 및 금기 사항 — MFDS/TFDA 공식 허가사항 PDF 파싱 (DG001, Blocking)
- 기존 허가 적응증 확인 — 국내외 약품 DB 대조
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

