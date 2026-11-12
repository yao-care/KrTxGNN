---
noindex: true
sitemap: false
layout: default
title: Bacampicillin Hydrochloride
parent: 모델 예측만 (L5)
nav_order: 119
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Bacampicillin Hydrochloride
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

## Bacampicillin Hydrochloride: 예측 적응증 없음 — 평가 보류
{: .text-alpha }

## 한 문장 요약

Bacampicillin Hydrochloride는 페니실린계 항생제 Ampicillin의 전구약물(prodrug)로, 세균 감염 치료에 사용되는 것으로 알려져 있습니다.
그러나 이번 Evidence Pack에는 **TxGNN 예측 결과가 존재하지 않으며**, 재창출 분석을 진행하기 위한 기본 데이터가 충족되지 않습니다.
현재 확보된 근거로는 재창출 방향성을 평가할 수 없습니다.

<!-- review:begin kr-lic-20261105-bacampicillin_hydrochloride-1 -->

> **검토 정정 (2026-11-05)**: 원래 문장: “그러나 이번 Evidence Pack에는 **TxGNN 예측 결과가 존재하지 않으며**, 대만(한국) 시판 이력도 없어 재창출 분석을 진행하기 위한 기본 데이터가 충족되지 않습니다.” 삭제: 대만 TFDA에 관한 템플릿 잔여 문구로, 이 한국 페이지와 관련이 없습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261105-bacampicillin_hydrochloride-1 -->

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (Evidence Pack에 미기재) |
| 예측 신규 적응증 | 없음 (TxGNN 예측 결과 없음) |
| TxGNN 예측 점수 | 없음 |
| 근거 수준 | L5 (모델 예측 없음, 실제 연구 미확인) |
| 한국 시판 현황 | 허가되었으나 미시판 (수출용 허가만 유효: 1건 / 전체 2건) |
| 허가증 수 | 2건 (국내 0건 · 유효 0건 / 수출용 2건 · 유효 1건) |
| 권장 결정 | Hold |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증이 존재하지 않아 재창출 가능성을 평가할 수 없으며, 해당 약물은 규제 정보도 확보되어 있지 않습니다. 아래 데이터 확보 없이는 평가를 진행하기 어렵습니다.

<!-- review:begin kr-lic-20261105-bacampicillin_hydrochloride-2 -->

> **검토 정정 (2026-11-05)**: 원래 문장: “TxGNN 예측 적응증이 존재하지 않아 재창출 가능성을 평가할 수 없으며, 해당 약물은 시판 이력이 없어 규제 정보도 확보되어 있지 않습니다.” 삭제: 허가가 취소되었거나 허가·시판되지 않는다고 했으나, 성분 기준으로 다시 맞춘 2026-11-05 기준 식품의약품안전처(nedrug) 허가 자료와 맞지 않습니다. 이 약의 허가는 2건(유효 1건)이며, 현재 수치는 빠른 개요와 「한국 시판 정보」의 표에 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261105-bacampicillin_hydrochloride-2 -->

**진행하려면 필요한 것:**
- **[필수]** TxGNN 파이프라인에서 Bacampicillin Hydrochloride의 DrugBank ID 매핑 확인 및 예측 재실행 (`drugbank_id`가 `null`이므로 KG 예측 미수행된 가능성 있음)
- **[필수]** DrugBank API를 통해 작용 기전(MOA) 및 원래 적응증 정보 수집
- **[권장]** TFDA/MFDS 허가사항 PDF를 다운로드하여 경고 및 금기 항목 파싱
- **[참고]** 시판이 없는 약물의 경우, PubMed 및 ClinicalTrials.gov에서 직접 문헌/시험 검색 후 수동 Evidence Pack 보완 필요

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-05 | 삭제: “대만(한국) 시판 이력도 없어” | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |
| 2026-11-05 | 삭제: “시판 이력이 없어” | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

