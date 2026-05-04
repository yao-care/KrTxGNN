---
layout: default
title: Articaine Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 90
evidence_level: L5
indication_count: 0
---

# Articaine Hydrochloride
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

# ARTICAINE HYDROCHLORIDE: 예측 불가 — 입력 데이터 부족

## 한 문장 요약

ARTICAINE HYDROCHLORIDE는 아미드계 국소마취제로 치과 마취에 널리 사용되는 약물입니다.
그러나 이번 Evidence Pack에는 **TxGNN 예측 결과가 없으며**, 한국(대만) 허가 이력도 존재하지 않아
재창출 후보로서의 타당성을 평가할 수 없는 상태입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (허가 이력 없음) |
| 예측 신규 적응증 | TxGNN 예측 결과 없음 |
| TxGNN 예측 점수 | — |
| 근거 수준 | 해당 없음 (예측 결과 없음) |
| 한국 시판 현황 | 미상시 |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 결과(`predicted_indications`)가 비어 있고, 약물의 DrugBank ID · 작용 기전 · 기존 허가 적응증 모두 확인되지 않아 재창출 가능성을 평가할 근거가 전무합니다.

**진행하려면 필요한 것:**

- **[최우선]** TxGNN 예측 파이프라인 재실행 — `ARTICAINE HYDROCHLORIDE`가 지식 그래프에 존재하는지 확인
- **[높음]** DrugBank ID 확보 후 작용 기전(MOA) 데이터 수집 (`DB09091` 또는 동일 성분 ID 검토)
- **[높음]** 한국 MFDS 또는 대만 TFDA 허가 현황 재조회 — 치과용 마취제 카테고리 별도 분류 여부 확인
- **[중간]** 허가사항 PDF 다운로드 및 경고·금기 항목 파싱 (DG001 해소)
- 위 데이터 확보 후 Evidence Pack v5 재생성 및 보고서 재발행
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

