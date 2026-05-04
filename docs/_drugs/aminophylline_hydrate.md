---
layout: default
title: Aminophylline Hydrate
parent: 僅模型預測 (L5)
nav_order: 58
evidence_level: L5
indication_count: 0
---

# Aminophylline Hydrate
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

# AMINOPHYLLINE HYDRATE: 평가 불가 — 핵심 데이터 부재

## 한 문장 요약

AMINOPHYLLINE HYDRATE는 Xanthine 계열 기관지 확장제로, 기존에 천식 및 만성 폐쇄성 폐질환(COPD) 치료에 사용되어 왔습니다.
그러나 이번 Evidence Pack에는 **TxGNN 예측 결과가 포함되어 있지 않으며**, 한국 허가 이력 및 안전성 데이터도 존재하지 않아 정식 재창출 평가를 진행할 수 없습니다.
현재 상태에서는 **Hold** 결정이 권장되며, 아래 기재된 데이터 보완 후 재평가가 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (허가 이력 부재) |
| 예측 신규 적응증 | 없음 (TxGNN 예측 결과 미포함) |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | L5 (모델 예측 없음, 실제 연구 미확인) |
| 한국 시판 현황 | 미상 (한국 허가 현황 미포함) |
| 허가증 수 | 0건 (데이터 부재) |
| 권장 결정 | **Hold** |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 결과가 포함되어 있지 않으며, 허가 정보·MOA·안전성 데이터 등 평가에 필수적인 핵심 항목이 모두 누락되어 있어 재창출 가능성 평가 자체가 불가능합니다.

**진행하려면 필요한 것:**
- **TxGNN 예측 재실행**: `predicted_indications` 결과 생성 (현재 빈 배열)
- **DrugBank 데이터 보완**: DrugBank ID 확인 및 MOA, 적응증, 독성 데이터 수집 (`query_log` 상 DrugBank 조회 성공(1건) 기록이 있으나 결과 미반영 — 재확인 필요)
- **규제 데이터 수집**: 한국 MFDS 허가 현황 조회 (aminophylline hydrate 제품 포함 여부 확인)
- **안전성 데이터 확보**: 허가사항 PDF 수집 및 경고·금기 항목 파싱
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

