---
noindex: true
sitemap: false
layout: default
title: Axicabtagene Ciloleucel
parent: 모델 예측만 (L5)
nav_order: 109
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Axicabtagene Ciloleucel
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

## AXICABTAGENE CILOLEUCEL: TxGNN 예측 없음 — 평가 보류
{: .text-alpha }

---

## 한 문장 요약

이번 Evidence Pack에는 **TxGNN 예측 적응증이 없으며**, 작용 기전·안전성 데이터도 모두 누락되어 있어 표준 약물 재창출 평가를 수행할 수 없습니다.
데이터 보완 후 재평가가 필요합니다.

<!-- review:begin kr-lic-20261031-axicabtagene_ciloleucel-1 -->

> **검토 정정 (2026-10-31)**: 원래 문장: “Axicabtagene ciloleucel(DB13915)은 현재 한국에 시판되지 않은 약물입니다. / 이번 Evidence Pack에는 **TxGNN 예측 적응증이 없으며**, 작용 기전·안전성 데이터도 모두 누락되어 있어 표준 약물 재창출 평가를 수행할 수 없습니다.” 삭제: 허가가 취소되었거나 허가·시판되지 않는다고 했으나, 성분 기준으로 다시 맞춘 2026-10-31 기준 식품의약품안전처(nedrug) 허가 자료와 맞지 않습니다. 이 약의 허가는 1건(유효 1건)이며, 현재 수치는 빠른 개요와 「한국 시판 정보」의 표에 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261031-axicabtagene_ciloleucel-1 -->

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (Evidence Pack에 데이터 없음) |
| 예측 신규 적응증 | 없음 (TxGNN 예측 결과 미수신) |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | L5 이하 (예측 자체 없음) |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
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

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-10-31 | 삭제: “Axicabtagene ciloleucel(DB13915)은 현재 한국에 시판되지 않은 약물입니다” | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

