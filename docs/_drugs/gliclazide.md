---
layout: default
title: Gliclazide
parent: 僅模型預測 (L5)
nav_order: 269
evidence_level: L5
indication_count: 0
---

# Gliclazide
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

이 Evidence Pack은 `predicted_indications`가 비어 있고 대부분의 필드가 데이터 결함 상태입니다. 금지 사항(빈 섹션 생략, [Data Gap] 출력 금지)을 준수하여 채울 수 있는 섹션만 기재합니다.

---

# GLICLAZIDE: 예측 신규 적응증 없음 — 데이터 보완 후 재평가 필요

## 한 문장 요약

GLICLAZIDE(DrugBank ID: DB01120)는 설포닐우레아 계열의 경구 혈당강하제로 알려진 약물입니다.
현재 Evidence Pack에 TxGNN 예측 신규 적응증 결과가 존재하지 않으며, 한국 시판 허가 기록·작용 기전·안전성 데이터 모두 수집되지 않아 **재창출 평가를 개시할 수 있는 최소 요건을 충족하지 못한 상태**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 수집 데이터 없음 (한국 미허가) |
| 예측 신규 적응증 | 수집 데이터 없음 |
| TxGNN 예측 점수 | — |
| 근거 수준 | L5 (예측 결과 없음) |
| 한국 시판 현황 | 미상시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 데이터 결함 현황

Evidence Pack 생성 시 확인된 미수집 항목입니다. 아래 결함이 해소되기 전까지 평가를 진행할 수 없습니다.

| 결함 ID | 항목 | 심각도 | 영향 | 해소 방법 |
|---------|------|--------|------|-----------|
| DG001 | 한국 허가 경고·금기 정보 | **Blocking** | 안전성 초평가 불가 | MFDS 의약품통합정보시스템에서 허가사항 PDF 다운로드 |
| DG002 | 작용 기전 (MOA) | High | 기전 관련성 분석 불가 | DrugBank API 재조회 |
| —      | TxGNN 예측 적응증 | Blocking | 재창출 평가 자체 불가 | TxGNN 파이프라인 재실행 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 결과가 없고, 작용 기전·한국 허가 안전성 데이터(경고·금기·DDI)가 모두 미수집 상태로, 재창출 가능성 평가의 기초 요건을 갖추지 못했습니다.

**진행하려면 필요한 것:**
- **[최우선]** TxGNN 예측 파이프라인 재실행 → `predicted_indications` 결과 확보
- DrugBank API 재조회 → MOA, 원래 적응증(original_indications) 보완
- MFDS 허가정보 시스템 조회 → 경고·금기·DDI 데이터 수집
- 위 데이터 확보 후 Evidence Pack v5로 재생성하여 본 보고서 재작성
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

