---
noindex: true
sitemap: false
layout: default
title: Apalutamide
parent: 모델 예측만 (L5)
nav_order: 77
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Apalutamide
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **0** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 약사 평가 보고서

</div>

Evidence Pack을 분석했습니다. `predicted_indications`가 비어 있고 대부분의 필드에 데이터가 없는 미완성 팩이므로, 해당 섹션을 생략하고 확보된 데이터만으로 보고서를 작성합니다.

---

## APALUTAMIDE: 예측 적응증 데이터 수집 필요
{: .text-alpha }

## 한 문장 요약

APALUTAMIDE(DrugBank ID: DB11901)는 이번 Evidence Pack에는 TxGNN 예측 적응증 결과가 포함되어 있지 않습니다.
작용 기전(MOA), 원래 적응증, 안전성 데이터 등 핵심 항목이 모두 수집되지 않아 재창출 분석을 진행할 수 없는 상태이며, 데이터 보완 후 재평가가 필요합니다.

<!-- review:begin kr-lic-20261105-apalutamide-1 -->

> **검토 정정 (2026-11-05)**: 원래 문장: “APALUTAMIDE(DrugBank ID: DB11901)는 현재 한국 미허가 약물로, 이번 Evidence Pack에는 TxGNN 예측 적응증 결과가 포함되어 있지 않습니다.” 삭제: 성분 기준으로 다시 맞춘 2026-11-05 기준 식품의약품안전처(nedrug) 허가 자료와 맞지 않습니다. 이 약의 허가는 1건(유효 1건)이며, 현재 수치는 빠른 개요와 「한국 시판 정보」의 표에 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261105-apalutamide-1 -->

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | 데이터 없음 |
| TxGNN 예측 점수 | 데이터 없음 |
| 근거 수준 | — (예측 결과 미생성) |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | **Hold** |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증 목록(`predicted_indications`)이 비어 있어 재창출 후보 질환이 특정되지 않았습니다. 작용 기전, 원래 적응증, 안전성 데이터도 모두 확보되지 않아 분석을 진행할 수 없습니다.

**진행하려면 필요한 것:**

| 우선순위 | 항목 | 조치 방법 |
|---------|------|---------|
| 🔴 Blocking | TxGNN 예측 실행 (`predicted_indications` 생성) | `scripts/run_kg_prediction.py` 실행 후 Evidence Pack 재생성 |
| 🔴 Blocking | 규제기관 허가 데이터 확보 | 식약처(MFDS) 의약품 허가 데이터베이스 조회 |
| 🟠 High | 작용 기전 (MOA) 확보 | DrugBank API 조회 (`/drugs/DB11901`) |
| 🟠 High | 원래 적응증 텍스트 확보 | DrugBank categories 및 국내외 허가 정보 참조 |
| 🟡 Medium | 안전성 정보 (경고·금기·DDI) 확보 | 허가 주의사항(SPC) PDF 다운로드 후 파싱 |

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-05 | 삭제: “현재 한국 미허가 약물로” | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

