---
layout: default
title: Axicabtagene Ciloleucel
parent: 僅模型預測 (L5)
nav_order: 107
evidence_level: L5
indication_count: 0
---

# Axicabtagene Ciloleucel
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

# AXICABTAGENE CILOLEUCEL: TxGNN 예측 없음 — 평가 보류

---

## 한 문장 요약

Axicabtagene ciloleucel(DB13915)은 현재 한국에 시판되지 않은 약물입니다.
이번 Evidence Pack에는 **TxGNN 예측 적응증이 없으며**, 작용 기전·안전성 데이터도 모두 누락되어 있어 표준 약물 재창출 평가를 수행할 수 없습니다.
데이터 보완 후 재평가가 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (Evidence Pack에 데이터 없음) |
| 예측 신규 적응증 | 없음 (TxGNN 예측 결과 미수신) |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | L5 이하 (예측 자체 없음) |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 데이터 공백 현황

이번 Evidence Pack에서 표준 평가에 필요한 핵심 항목이 다음과 같이 누락되어 있습니다.

| 공백 ID | 누락 항목 | 심각도 | 평가에 미치는 영향 | 보완 방법 |
|---------|----------|--------|-----------------|---------|
| DG001 | 허가 경고 / 금기사항 | Blocking | 안전성 초평가 불가 | TFDA 공식 사이트에서 仿單 PDF 다운로드 후 파싱 |
| DG002 | 작용 기전 (MOA) | High | 기전 연관성 분석 불가 | DrugBank API 조회 |
| — | TxGNN 예측 적응증 | Blocking | 재창출 평가 자체 불가 | TxGNN 파이프라인 재실행 및 예측 결과 확인 |
| — | 기존 적응증 (original_indications) | High | 비교 기준 부재 | DrugBank / MFDS 데이터 보완 |

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증 배열이 비어 있고, 안전성·MOA·기존 적응증 데이터가 모두 누락되어 표준 약물 재창출 평가 진행이 불가합니다.

**진행하려면 필요한 것:**
- TxGNN 파이프라인을 재실행하여 `predicted_indications` 결과 생성
- DrugBank API를 통해 작용 기전(MOA) 및 기존 적응증 데이터 확보
- TFDA 仿單 PDF 파싱을 통해 허가 경고·금기사항 수집
- 한국 MFDS(의약품통합정보시스템)에서 허가 현황 재확인
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

