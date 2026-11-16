---
layout: default
title: Alverine Citrate
parent: 모델 예측만 (L5)
nav_order: 51
evidence_level: L5
indication_count: 9
drugbank_id: DB01616
monitor_inn: "Alverine"
predicted_indications: ["dysthymic disorder", "neurotic disorder", "anxiety disorder", "migraine disorder", "neurotic depression", "melancholia", "benign paroxysmal torticollis of infancy", "agoraphobia", "congenital isolated adrenocorticotropic hormone deficiency (disease)"]
last_modified_at: 2026-11-16
description: "Alverine Citrate: 예측 신규 적응증 기분부전장애 (dysthymic disorder) (근거 수준 L5). 기존 적응증: MFDS 허가사항(PDF) 참조"
---

# Alverine Citrate
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **9** 건
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

## Alverine Citrate: 기분부전장애 (dysthymic disorder)
{: .text-alpha }

## 한 문장 요약

Alverine Citrate는 평활근 이완 작용을 가진 약물로, 한국에서 여러 제품으로 허가되어 있습니다.
TxGNN 모델은 **기분부전장애(dysthymic disorder)**에 효과가 있을 수 있다고 예측하지만, 이 예측을 직접 뒷받침하는 임상시험이나 문헌은 현재 없습니다.
따라서 현 단계에서는 모델 예측만 존재하는 상태입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201602428/EE); [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200403769/EE); [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200502681/EE); [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201501570/EE); [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202107582/EE);  |
| 예측 신규 적응증 | 기분부전장애 (dysthymic disorder) |
| TxGNN 예측 점수 | 0.9983 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 10건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 이 보고서를 위해 수집된 자료에서는 알베린이 5-HT1A 수용체 길항 작용을 가진 평활근 이완제로 설명됩니다. 세로토닌 계통은 기분 장애의 병태생리와 관련되어 있어, 기분부전장애와의 연관성을 생각해 볼 수는 있습니다.

다만 이는 가설 수준입니다. 기분부전장애에 대해 알베린을 직접 평가한 임상시험이나 문헌은 확인되지 않았습니다. 관련 우울 장애를 다룬 컴퓨터 기반 재창출 연구가 있으나, 이는 기분부전장애 자체를 직접 연구한 것이 아니므로 근거로 인정하지 않았습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

아래는 단일 성분 허가 중 현재 유효한 주요 5건입니다. 허가 적응증 텍스트는 문서 링크 형태로만 제공되어 요약하지 않았습니다. 전체 허가 목록은 일부만 포함되었을 수 있습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201602428 | 레바스판연질캡슐(수출용) | 연질캡슐 | 허가 문서 참조 |
| 200403769 | 알베신정(수출용) | 정제 | 허가 문서 참조 |
| 200502681 | 알모론연질캡슐(수출용) | 연질캡슐 | 허가 문서 참조 |
| 202107582 | 스파스모날캡슐 | 경질캡슐 | 허가 문서 참조 |
| 200501660 | 알베릭스연질캡슐 | 연질캡슐 | 허가 문서 참조 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
기분부전장애에 대한 TxGNN 점수는 높지만(0.9983), 이 질환을 직접 다룬 임상시험이나 문헌이 없어 근거 수준은 L5입니다. 안전성 및 작용 기전 데이터도 부족합니다.

**진행하려면 필요한 것:**
- 기분부전장애에서 알베린의 효과를 직접 평가한 전임상 또는 임상 연구
- 상세한 작용 기전(MOA) 데이터 확보
- 허가사항의 경고, 금기 및 약물 상호작용 정보 확인
- 정신과 적응증 투여 시 용량, 안전성 및 이상반응 평가 계획

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-05 | 삭제: “현재 허가 이력이 없어” | 보고서가 다시 생성되어 이 문장이 없음(2026-11-16: 2026년 11월 16일 보고서가 새 예측(DrugBank ID로 찾은 TxGNN 예측)으로 다시 생성되어 이 문장이 더 이상 없음; 원래: 정정) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

