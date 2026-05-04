---
layout: default
title: Atropine Sulfate
parent: 僅模型預測 (L5)
nav_order: 102
evidence_level: L5
indication_count: 0
---

# Atropine Sulfate
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

# ATROPINE SULFATE: TxGNN 예측 적응증 없음 — 약물 재창출 평가 보류

---

## 한 문장 요약

Atropine Sulfate는 무스카린 수용체 길항제(항콜린성 약물)로, 서맥·유기인산 중독 해독·수술 전 처치 등에 사용되어 온 약물입니다.
이번 Evidence Pack에는 **TxGNN 예측 적응증이 생성되지 않았으며**, 한국 허가 이력 및 안전성 데이터 또한 수집되지 않아 정식 약물 재창출 평가를 진행할 수 없습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (한국 허가 이력 없음) |
| 예측 신규 적응증 | 없음 (TxGNN 예측 결과 미생성) |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | L5 (모델 예측 부재, 실제 연구 근거 없음) |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 데이터 현황

이번 Evidence Pack에는 약물 재창출 평가의 핵심 데이터 두 가지가 누락되어 있습니다.

첫째, **DrugBank ID가 확인되지 않았습니다.** DrugBank 조회는 성공(result_count: 1)으로 기록되었으나 `drugbank_id` 필드가 비어 있습니다. TxGNN 예측 파이프라인은 DrugBank ID를 기반으로 지식 그래프 탐색을 수행하므로, ID 매핑 실패 시 예측 후보가 생성되지 않습니다.

둘째, **작용 기전(MOA) 데이터가 수집되지 않았습니다.** Atropine Sulfate는 무스카린성 아세틸콜린 수용체의 경쟁적 길항제로 알려진 약물이지만, 기전 기반 적용 가능성 분석을 위한 구조화된 MOA 데이터가 없습니다.

한국 허가 데이터 부재(미출시)와 맞물려, 현재 상태로는 약물 재창출 후보 타당성을 평가할 근거가 충분하지 않습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증이 생성되지 않았고, 한국 허가 데이터 및 안전성 정보 모두 확인되지 않아 약물 재창출 평가를 진행할 수 없습니다.

**진행하려면 필요한 것:**
- DrugBank ID 확보 및 매핑 재시도 (`DB` 식별자 확인 후 TxGNN 예측 파이프라인 재실행)
- DrugBank API에서 MOA, 약물 분류, 독성 데이터 조회
- 한국 식약처(MFDS) 허가 데이터베이스에서 ATROPINE SULFATE 허가 현황 확인
- 허가사항 PDF 다운로드 및 파싱을 통해 경고·금기 정보 수집 (Data Gap DG001 해소)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

