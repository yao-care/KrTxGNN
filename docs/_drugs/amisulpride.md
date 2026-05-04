---
layout: default
title: Amisulpride
parent: 僅模型預測 (L5)
nav_order: 60
evidence_level: L5
indication_count: 0
---

# Amisulpride
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

# Amisulpride: 예측 적응증 없음 — 평가 보류

## 한 문장 요약

Amisulpride(DrugBank ID: DB06288)는 현재 대만 미허가 약물로, 이번 Evidence Pack에 TxGNN 예측 적응증 결과가 포함되어 있지 않습니다. 작용 기전(MOA)과 허가 경고문·금기사항 데이터도 모두 누락되어 있어, 재창출 가능성 평가를 진행하기 위한 최소 요건이 충족되지 않았습니다. 핵심 데이터 보완 후 재평가가 필요합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | 예측 결과 없음 |
| TxGNN 예측 점수 | — |
| 근거 수준 | 평가 불가 |
| 시판 현황 | ✗ 미허가 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 데이터 갭 현황

이 Evidence Pack은 평가 진행에 필요한 핵심 항목이 누락되어 있습니다.

| 갭 ID | 항목 | 심각도 | 영향 | 해소 방법 |
|-------|------|--------|------|-----------|
| DG001 | 허가 경고문 / 금기사항 | **Blocking** | 안전성 초평가 불가 | 허가 기관 PDF 파싱 |
| DG002 | 작용 기전 (MOA) | **High** | 기전 관련성 분석 불가 | DrugBank API 조회 |
| — | TxGNN 예측 적응증 | **Critical** | 재창출 대상 없음 | 예측 파이프라인 재실행 |
| — | 원래 허가 적응증 | **High** | 기준선 설정 불가 | 허가 기관 자료 수집 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증이 존재하지 않으며, 작용 기전(MOA)·안전성 데이터가 모두 누락되어 현 시점에서는 재창출 가능성 평가를 수행할 수 없습니다.

**진행하려면 필요한 것:**
- TxGNN 예측 파이프라인 재실행 및 예측 결과 포함 여부 확인
- DrugBank API를 통한 MOA 및 약물 카테고리 데이터 수집
- 해당 의약품 허가 기관(TFDA 등) 자료를 통한 경고문·금기사항 확인
- 원래 허가 적응증 데이터 수집
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

