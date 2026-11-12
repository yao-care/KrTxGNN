---
noindex: true
sitemap: false
layout: default
title: Aripiprazole Monohydrate
parent: 모델 예측만 (L5)
nav_order: 86
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Aripiprazole Monohydrate
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

## Aripiprazole Monohydrate: 평가 데이터 부족으로 보류
{: .text-alpha }

## 한 문장 요약

Aripiprazole Monohydrate에 대한 약물 재창출 평가가 요청되었으나, TxGNN 예측 적응증 및 기존 적응증 데이터가 모두 누락되어 있습니다.
안전성 정보(경고·금기·약물 상호작용) 역시 확인되지 않습니다.
필수 데이터 확보 후 재평가가 필요합니다.

<!-- review:begin kr-lic-20261105-aripiprazole_monohydrate-1 -->

> **검토 정정 (2026-11-05)**: 원래 문장: “현재 한국 내 허가 이력이 없으며, 안전성 정보(경고·금기·약물 상호작용) 역시 확인되지 않습니다.” 삭제: 허가가 취소되었거나 허가·시판되지 않는다고 했으나, 성분 기준으로 다시 맞춘 2026-11-05 기준 식품의약품안전처(nedrug) 허가 자료와 맞지 않습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261105-aripiprazole_monohydrate-1 -->

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | 데이터 없음 |
| TxGNN 예측 점수 | — |
| 근거 수준 | — |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 19건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증이 존재하지 않고, 기존 적응증·MOA·안전성 데이터가 모두 누락되어 있어 재창출 가능성을 평가할 수 없습니다.

**진행하려면 필요한 것:**
- TFDA 허가 경고·금기 정보 수집 — DG001 (Blocking): 안전성 초평가 진입 전 필수
- DrugBank ID 확인 및 MOA(작용 기전) 데이터 수집 — DG002 (High): 기전 연관성 분석에 필요
- TxGNN 예측 파이프라인 재실행으로 적응증 후보 생성 (현재 `predicted_indications: []`)
- 예측 결과 확보 후 임상시험·문헌 증거 수집 재진행

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-05 | 삭제: “현재 한국 내 허가 이력이 없으며” | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

