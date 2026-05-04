---
layout: default
title: Alfentanil Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 36
evidence_level: L5
indication_count: 0
---

# Alfentanil Hydrochloride
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

# Alfentanil Hydrochloride: 재창출 후보 평가 불가 (데이터 부족)

## 한 문장 요약

Alfentanil Hydrochloride는 단시간 작용형 합성 오피오이드 계열 약물로, 마취 유도 및 유지에 사용되는 것으로 알려져 있습니다.
이번 평가에서 TxGNN 모델이 생성한 **예측 적응증이 없으며**, 한국 시판 이력도 존재하지 않아 재창출 가능성을 평가할 수 있는 근거가 충분하지 않습니다.
현재 상태에서는 **Hold** 결정이 권장됩니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 이력 없음) |
| 예측 신규 적응증 | 없음 (TxGNN 예측 결과 없음) |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | L5 (모델 예측조차 없음) |
| 한국 시판 현황 | 미상시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증이 전혀 생성되지 않았고, 한국 허가 이력이 없으며, 작용 기전(MOA)·경고·금기 등 핵심 안전성 데이터가 모두 누락되어 있습니다. 재창출 가능성 평가를 진행할 최소한의 데이터 기반이 갖춰지지 않은 상태입니다.

**진행하려면 필요한 것:**

- **DrugBank 연동 보완**: DrugBank API 재조회를 통해 DrugBank ID, MOA, 카테고리, 독성 데이터 확보 (`DG002`)
- **허가사항 PDF 확보**: TFDA 또는 국내 허가 기관 공식 사이트에서 첨부문서(仿單) 다운로드 후 경고·금기 파싱 (`DG001`)
- **TxGNN 예측 재실행**: DrugBank ID 확보 후 KG 및 DL 예측 파이프라인 재실행하여 후보 적응증 도출
- **시판 현황 재확인**: 식품의약품안전처(MFDS) 의약품통합정보시스템에서 alfentanil 관련 수입 허가 여부 재조회
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

