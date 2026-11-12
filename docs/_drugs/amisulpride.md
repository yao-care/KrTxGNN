---
noindex: true
sitemap: false
layout: default
title: Amisulpride
parent: 모델 예측만 (L5)
nav_order: 62
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Amisulpride
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

## Amisulpride: 예측 적응증 없음 — 평가 보류
{: .text-alpha }

## 한 문장 요약

Amisulpride(DrugBank ID: DB06288)는 이번 Evidence Pack에 TxGNN 예측 적응증 결과가 포함되어 있지 않습니다. 작용 기전(MOA)과 허가 경고문·금기사항 데이터도 모두 누락되어 있어, 재창출 가능성 평가를 진행하기 위한 최소 요건이 충족되지 않았습니다. 핵심 데이터 보완 후 재평가가 필요합니다.

<!-- review:begin kr-lic-20261105-amisulpride-1 -->

> **검토 정정 (2026-11-05)**: 원래 문장: “Amisulpride(DrugBank ID: DB06288)는 현재 대만 미허가 약물로, 이번 Evidence Pack에 TxGNN 예측 적응증 결과가 포함되어 있지 않습니다.” 삭제: 대만 TFDA에 관한 템플릿 잔여 문구로, 이 한국 페이지와 관련이 없습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261105-amisulpride-1 -->

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | 예측 결과 없음 |
| TxGNN 예측 점수 | — |
| 근거 수준 | 평가 불가 |
| 한국 시판 현황 | 시판 중 (유효 허가 10건 / 전체 10건) |
| 허가증 수 | 10건 (유효 10건) |
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

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-05 | 삭제: “현재 대만 미허가 약물로” | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

