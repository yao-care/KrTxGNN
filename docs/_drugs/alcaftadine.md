---
layout: default
title: Alcaftadine
parent: 僅模型預測 (L5)
nav_order: 32
evidence_level: L5
indication_count: 0
---

# Alcaftadine
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

해당 스킬은 파이프라인 관리용이므로 본 보고서 생성에는 직접 적용되지 않습니다. Evidence Pack을 분석하여 보고서를 작성합니다.

**분석 결과:**
- `predicted_indications: []` → TxGNN 예측 후보 없음
- `original_indications: []`, `original_moa: "[Data Gap]"` → 기본 약물 정보 부재
- `taiwan_regulatory.market_status: "未上市"` → 한국 미시판
- `safety` 전체 [Data Gap]

예측 적응증이 없으므로 보고서 구조를 해당 상황에 맞게 조정하겠습니다.

---

# Alcaftadine: 재창출 후보 미생성 — 추가 데이터 필요

## 한 문장 요약

Alcaftadine(DB06766)은 현재 한국 미시판 약물로, 이번 TxGNN 파이프라인 실행에서 신규 적응증 후보가 생성되지 않았습니다. 작용 기전(MOA) 정보와 한국 허가 데이터가 모두 부재하여 재창출 타당성 평가를 진행할 수 없는 상태이며, 파이프라인 원인 파악 및 핵심 데이터 보완이 선행되어야 합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 |
| 예측 신규 적응증 | 없음 (TxGNN 후보 미생성) |
| TxGNN 예측 점수 | N/A |
| 근거 수준 | N/A |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 파이프라인 실행 현황

이번 Evidence Pack에서 `predicted_indications` 목록이 비어 있습니다. Query Log에 따르면 DrugBank 조회는 성공(결과 1건)했으나, DDI 데이터베이스에서는 해당 약물이 확인되지 않았습니다.

| 조회 항목 | 조회일 | 상태 | 비고 |
|-----------|--------|------|------|
| DDI | 2026-03-27 | 미발견 | —  |
| DrugBank | 2026-03-27 | 성공 (1건) | — |

DrugBank 매핑은 성공했음에도 예측 후보가 생성되지 않은 원인으로는 다음을 고려할 수 있습니다:

- 지식 그래프(KG) 내 해당 약물 노드의 연결 엣지 부족
- 예측 점수 임계값(threshold) 미달
- 질병 매핑 단계에서 적응증 후보 탈락
- 파이프라인 실행 오류

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 파이프라인이 Alcaftadine에 대한 신규 적응증 후보를 생성하지 못했고, 작용 기전(MOA) 및 기존 적응증 정보가 모두 부재하여 재창출 타당성의 기초 평가조차 수행할 수 없습니다.

**진행하려면 필요한 것:**

- **파이프라인 점검**: Alcaftadine이 KG 예측 단계에서 왜 후보를 생성하지 못했는지 원인 파악 (DrugBank ID → KG 노드 매핑 확인, 점수 분포 확인)
- **MOA 데이터 확보**: DrugBank API에서 작용 기전(mechanism of action) 조회 (DG002 해소)
- **기존 적응증 확인**: DrugBank 또는 공개 문헌을 통해 승인된 적응증 확인
- **한국 허가 현황 확인**: 식약처(MFDS) 의약품 통합정보시스템(nedrug.mfds.go.kr) 조회
- **안전성 데이터 확보**: 허가된 국가(예: 미국 FDA)의 의약품 설명서(PI) 검토 (DG001 해소)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

