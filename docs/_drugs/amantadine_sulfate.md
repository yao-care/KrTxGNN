---
layout: default
title: Amantadine Sulfate
parent: 모델 예측만 (L5)
nav_order: 52
evidence_level: L5
indication_count: 4
drugbank_id: DB00915
monitor_inn: "Amantadine"
predicted_indications: ["Rasmussen subacute encephalitis", "transaldolase deficiency", "myelitis", "PLA2G6-associated neurodegeneration"]
last_modified_at: 2026-11-16
description: "Amantadine Sulfate: 예측 신규 적응증 라스무센 아급성 뇌염 (Rasmussen subacute encephalitis) (근거 수준 L5). 기존 적응증: MFDS 허가사항(PDF) 참조"
---

# Amantadine Sulfate
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **4** 건
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

## Amantadine Sulfate: 라스무센 아급성 뇌염 (Rasmussen subacute encephalitis)
{: .text-alpha }

## 한 문장 요약

아만타딘황산염(Amantadine Sulfate)은 한국에서 단일 성분 제제로 허가되어 시판 중인 약물입니다.
TxGNN 모델은 **라스무센 아급성 뇌염(Rasmussen subacute encephalitis)**에 효과가 있을 수 있다고 예측합니다.
다만 이 질환을 직접 다룬 임상시험과 문헌은 **0건**이어서, 현재는 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200510972/EE); [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198701132/EE) |
| 예측 신규 적응증 | 라스무센 아급성 뇌염 (Rasmussen subacute encephalitis) |
| TxGNN 예측 점수 | 0.9948 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 3건) |
| 허가증 수 | 3건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없어 기전에 근거한 분석에는 한계가 있습니다.

다만 아만타딘이 NMDA 수용체 길항 작용을 가진다는 점에서 가설을 세워 볼 수 있습니다. 이 작용은 면역 매개성 뇌염과 간질성 뇌병증에서 글루타메이트 매개 흥분독성을 줄일 수 있다는 추론입니다. 그러나 이 가설을 뒷받침하는 임상시험이나 문헌은 이번에 수집된 자료에 없습니다.

따라서 이 예측은 모델 점수에만 근거한 탐색적 가설이며, 기존 약물과 이 질환의 연관성도 아직 검토되지 않았습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 상태 |
|---------|------|------|------|
| 200510972 | 피케이멜즈인퓨전주(아만타딘황산염) | 수액용 주사제 | 유효 |
| 198701132 | 피케이멜즈정(아만타딘황산염) | 필름코팅 정제 | 유효 |
| 200704626 | 아만타정(아만타딘황산염) | 필름코팅 정제 | 취소 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
라스무센 아급성 뇌염을 직접 다룬 임상시험과 문헌이 없고, 근거 수준은 L5(모델 예측만 있음)입니다. 작용 기전 및 안전성 데이터도 확보되지 않아 현재로서는 진행을 권고하기 어렵습니다.

**진행하려면 필요한 것:**
- 허가사항(첨부문서)의 경고 및 금기 정보 확보
- 아만타딘의 작용 기전 데이터 확보
- 라스무센 아급성 뇌염에서의 아만타딘 관련 전임상 연구, 증례 보고, 임상시험 탐색
- NMDA 수용체 길항을 통한 가설을 검증할 수 있는 기전 연구
- 주사제와 경구제 중 어떤 제형이 적합한지에 대한 투여 경로 검토

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-05 | 삭제: “현재 한국 내 허가 기록이 없는 약물로” | 보고서가 다시 생성되어 이 문장이 없음(2026-11-16: 2026년 11월 16일 보고서가 새 예측(DrugBank ID로 찾은 TxGNN 예측)으로 다시 생성되어 이 문장이 더 이상 없음; 원래: 정정) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |
| 2026-11-05 | 삭제: “현재 AMANTADINE SULFATE의 한국 허가 기록이 없습니다 (총 0건)” | 보고서가 다시 생성되어 이 문장이 없음(2026-11-16: 2026년 11월 16일 보고서가 새 예측(DrugBank ID로 찾은 TxGNN 예측)으로 다시 생성되어 이 문장이 더 이상 없음; 원래: 정정) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

