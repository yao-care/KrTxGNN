---
layout: default
title: Bedaquiline Fumarate
parent: 모델 예측만 (L5)
nav_order: 128
evidence_level: L5
indication_count: 0
---

# Bedaquiline Fumarate
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **0** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 약사 평가 보고서

</div>

Evidence Pack을 분석하겠습니다. `predicted_indications`가 비어 있고 주요 데이터 항목들이 수집되지 않은 상태임을 확인했습니다. 수집된 데이터 범위 내에서 보고서를 작성합니다.

---

# Bedaquiline Fumarate: 예측 신규 적응증 미결정 — 데이터 수집 필요

## 한 문장 요약

Bedaquiline Fumarate는 약물 재창출 평가 파이프라인에 진입한 약물이나, 현재 원래 적응증·작용 기전(MOA)·안전성 정보가 모두 수집되지 않은 상태입니다.
TxGNN 예측 결과가 존재하지 않아 신규 적응증 후보를 특정할 수 없으며, 기반 데이터 확보 후 재평가가 선행되어야 합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | 예측 결과 없음 |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | 평가 불가 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 결과가 생성되지 않았고, 약물 기본 정보(원래 적응증, DrugBank ID, MOA)와 안전성 데이터(경고·금기·DDI) 모두 미수집 상태이므로 재창출 가능성을 평가할 수 없습니다.

**진행하려면 필요한 것:**

- **[DG001 — Blocking]** 규제기관 허가사항(TFDA 또는 FDA/EMA 동등 문서)에서 원래 적응증 및 안전성 정보(경고·금기·이상반응) 수집
- **[DG002 — High]** DrugBank API 조회를 통해 DrugBank ID 및 작용 기전(MOA) 확인
- DrugBank ID 확정 후 TxGNN 예측 파이프라인 재실행하여 신규 적응증 후보 도출
- 예측 결과 도출 이후 ClinicalTrials.gov(임상시험) 및 PubMed(문헌) 증거 수집 실시
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

