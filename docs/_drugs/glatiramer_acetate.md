---
layout: default
title: Glatiramer Acetate
parent: 僅模型預測 (L5)
nav_order: 266
evidence_level: L5
indication_count: 0
---

# Glatiramer Acetate
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

Evidence Pack을 분석합니다. `predicted_indications`가 완전히 비어 있고, 기존 적응증·MOA·안전성 데이터도 모두 부재한 상태입니다. 데이터 갭을 정직하게 반영한 보고서를 생성합니다.

---

# Glatiramer Acetate: 재창출 평가 보류 — 예측 적응증 데이터 없음

## 한 문장 요약

Glatiramer Acetate는 이번 Evidence Pack에서 기존 적응증 및 TxGNN 예측 신규 적응증 데이터가 모두 부재하여 정식 재창출 평가를 진행할 수 없습니다.
DrugBank 조회는 성공(결과 1건)하였으나, 예측 적응증 목록(`predicted_indications`)이 비어 있어 어떠한 후보 적응증도 도출되지 않았습니다.
데이터 갭(DG001, DG002) 해소 후 재평가가 필요합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | 데이터 없음 |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | 평가 불가 (예측 결과 없음) |
| 한국 시판 현황 | 미시판 (허가 0건) |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
`predicted_indications` 목록이 비어 있어 재창출 후보 자체가 존재하지 않으며, 기존 적응증·MOA·경고/금기 등 핵심 약물 정보도 모두 누락되어 있어 안전성·기전 분석이 불가능한 상태입니다.

**진행하려면 필요한 것:**
- **[최우선]** TxGNN 예측 파이프라인 재실행 → `predicted_indications` 목록 확보
- **[Blocking — DG001]** TFDA/MFDS 허가사항 PDF 다운로드 및 파싱 → 경고·금기 데이터 보완
- **[High — DG002]** DrugBank API 조회 결과를 `drug.original_moa` 및 `drug.original_indications`에 반영 (DrugBank 쿼리 성공(1건) 확인됨 — 파싱 단계 점검 필요)
- 한국 MFDS 시판 여부 재확인 (현재 허가 0건)

---

> **⚠️ 면책 고지:** 본 보고서는 연구 참고 목적으로만 작성되었으며, 의료 조언을 구성하지 않습니다. 재창출 후보는 임상 검증 후에만 적용될 수 있습니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

