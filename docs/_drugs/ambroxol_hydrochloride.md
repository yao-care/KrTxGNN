---
noindex: true
sitemap: false
layout: default
title: Ambroxol Hydrochloride
parent: 모델 예측만 (L5)
nav_order: 54
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Ambroxol Hydrochloride
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

## AMBROXOL HYDROCHLORIDE: 재창출 평가 불가 — 데이터 미흡으로 Hold 권고
{: .text-alpha }

## 한 문장 요약

AMBROXOL HYDROCHLORIDE는 기존 적응증을 확인할 수 없습니다.
TxGNN 예측 파이프라인이 이 약물에 대한 신규 적응증을 생성하지 못했으며,
작용 기전(MOA)·안전성·규제 데이터가 모두 수집되지 않아 현 단계에서는 평가를 진행할 수 없습니다.

<!-- review:begin kr-lic-20261105-ambroxol_hydrochloride-1 -->

> **검토 정정 (2026-11-05)**: 원래 문장: “AMBROXOL HYDROCHLORIDE는 대만 허가 이력이 없어 기존 적응증을 확인할 수 없습니다.” 삭제: 대만 TFDA에 관한 템플릿 잔여 문구로, 이 한국 페이지와 관련이 없습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261105-ambroxol_hydrochloride-1 -->

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 |
| 예측 신규 적응증 | 없음 (TxGNN 예측 미생성) |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | L5 이하 (예측조차 없음) |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | **Hold** |

---

## 이 예측이 타당한 이유는?

TxGNN 모델이 이 약물에 대한 예측 결과를 생성하지 않았습니다.
이는 약물이 지식 그래프(KG) 내에 노드로 존재하지 않거나, DrugBank ID 매핑이 실패하여 예측 파이프라인에 진입하지 못했을 가능성이 높습니다.

쿼리 로그에서 DrugBank 검색은 성공(result_count: 1)하였으나, DrugBank ID가 Evidence Pack에 포함되지 않았습니다.
이 불일치를 해결하지 않으면 기전 분석 및 재창출 가능성 평가를 수행할 수 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 결과가 없고, 작용 기전·안전성 데이터가 모두 부재하여 재창출 가능성을 평가할 최소한의 근거조차 확보되지 않았습니다.

<!-- review:begin kr-lic-20261105-ambroxol_hydrochloride-2 -->

> **검토 정정 (2026-11-05)**: 원래 문장: “TxGNN 예측 결과가 없고, 대만 허가 이력·작용 기전·안전성 데이터가 모두 부재하여 재창출 가능성을 평가할 최소한의 근거조차 확보되지 않았습니다.” 삭제: 대만 TFDA에 관한 템플릿 잔여 문구로, 이 한국 페이지와 관련이 없습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261105-ambroxol_hydrochloride-2 -->

**진행하려면 필요한 것:**

- **[Blocking]** DrugBank ID 확인 — DrugBank API 재쿼리 후 `drugbank_id` 필드 보완
- **[Blocking]** TxGNN KG 내 노드 존재 여부 확인 — `data/external/drugbank_vocab.csv` 대조
- **[High]** 작용 기전(MOA) 수집 — DrugBank 약물 프로파일 파싱
- DrugBank ID 확보 후 Evidence Pack을 v5로 재생성하여 재평가 진행

<!-- review:begin kr-lic-20261105-ambroxol_hydrochloride-3 -->

> **검토 정정 (2026-11-05)**: 원래 문장: “**[High]** 대만 허가 현황 재확인 — TFDA 데이터베이스에서 "AMBROXOL" 성분명으로 재검색 (조회 시 `AMBROXOL`과 `AMBROXOL HYDROCHLORIDE` 두 형태 모두 시도) / DrugBank ID 확보 후 Evidence Pack을 v5로 재생성하여 재평가 진행” 삭제: 대만 TFDA에 관한 템플릿 잔여 문구로, 이 한국 페이지와 관련이 없습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261105-ambroxol_hydrochloride-3 -->

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-05 | 삭제: “대만 허가 이력이 없어” | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |
| 2026-11-05 | 삭제: “대만 허가 이력·” | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |
| 2026-11-05 | 삭제: “**[High]** 대만 허가 현황 재확인 — TFDA 데이터베이스에서 "AMBROXOL" 성분명으로 재검색 (조회 시 `AMBROXOL`과 `AMBROXOL HYDROCHLORIDE` 두 형태 모두 시도)” | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

