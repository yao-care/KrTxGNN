---
layout: default
title: Amiloride Hydrochloride
parent: 모델 예측만 (L5)
nav_order: 57
evidence_level: L5
indication_count: 5
drugbank_id: DB00594
monitor_inn: "Amiloride"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-11-17
description: "Amiloride Hydrochloride: 예측 신규 적응증 악성 고혈압성 신질환 (malignant hypertensive renal disease) (근거 수준 L5). 기존 적응증: MFDS 허가사항(PDF) 참조"
---

# Amiloride Hydrochloride
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **5** 건
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

## Amiloride Hydrochloride: 악성 고혈압성 신질환 (malignant hypertensive renal disease)
{: .text-alpha }

## 한 문장 요약

아미로라이드 염산염은 원위세뇨관의 상피성 나트륨 채널(ENaC)을 차단하는 칼륨보존 이뇨제입니다.
TxGNN 모델은 **악성 고혈압성 신질환 (malignant hypertensive renal disease)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 다룬 **임상시험은 0건, 문헌도 0편**이어서 모델 예측 단계에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198100103/EE) |
| 예측 신규 적응증 | 악성 고혈압성 신질환 (malignant hypertensive renal disease) |
| TxGNN 예측 점수 | 0.9982 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 수집되지 않았습니다. 알려진 정보에 따르면 아미로라이드는 원위세뇨관의 ENaC를 차단해 나트륨 재흡수를 줄이는 칼륨보존 이뇨제이며, 혈압을 낮추는 효과도 있습니다. 따라서 혈압과 체액량 조절이라는 측면에서 기전상 적용 가능성을 생각해 볼 수 있습니다.

그러나 이 연결고리는 일반적인 약리 특성에서 추정한 것입니다. 이 질환에 대한 임상시험이나 문헌은 확인되지 않았고, 매우 높은 예측 점수(0.9982)도 모델 계산 결과일 뿐 임상적 근거가 아닙니다.

안전성 측면의 우려도 큽니다. 악성 고혈압성 신질환은 급성이며 위험도가 높은 상태입니다. 신기능 저하가 동반되는 환자에게 칼륨보존 약물을 쓰면 고칼륨혈증 위험이 커질 수 있어, 이 적응증에서는 특히 신중한 검토가 필요합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 198100103 | 아미로정(염산아미로라이드) | 미황색의 원형정제 | [허가사항 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198100103/EE) |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
이 질환을 직접 연구한 임상시험과 문헌이 없어 근거 수준이 L5(모델 예측만 있음)입니다. 또한 급성·고위험 상태에서 신기능 저하와 고칼륨혈증 위험이 있는 칼륨보존 이뇨제를 쓰는 것이므로, 현 단계에서 진행하기는 어렵습니다.

**진행하려면 필요한 것:**
- 악성 고혈압성 신질환에서 아미로라이드의 효과를 직접 평가한 전임상 또는 임상 근거
- 허가사항(경고, 금기)의 확보 및 분석, 특히 신기능 저하와 고칼륨혈증 관련 항목
- 상세 작용 기전 데이터 확보
- 신기능 저하 환자의 혈청 칼륨 모니터링을 포함한 안전성 관리 계획

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-05 | 삭제: “대만 내 시판 허가 이력이 없으며” | 보고서가 다시 생성되어 이 문장이 없음(2026-11-16: 2026년 11월 16일 보고서가 새 예측(DrugBank ID로 찾은 TxGNN 예측)으로 다시 생성되어 이 문장이 더 이상 없음; 원래: 정정) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |
| 2026-11-05 | 삭제: “대만 허가 이력” | 보고서가 다시 생성되어 이 문장이 없음(2026-11-16: 2026년 11월 16일 보고서가 새 예측(DrugBank ID로 찾은 TxGNN 예측)으로 다시 생성되어 이 문장이 더 이상 없음; 원래: 정정) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |
| 2026-11-05 | 삭제: “**[참고]** Amiloride는 국제적으로 고혈압·부종 적응증으로 허가된 약물이나, 대만 내 허가 이력이 없으므로 규제 경로 별도 검토 필요” | 보고서가 다시 생성되어 이 문장이 없음(2026-11-16: 2026년 11월 16일 보고서가 새 예측(DrugBank ID로 찾은 TxGNN 예측)으로 다시 생성되어 이 문장이 더 이상 없음; 원래: 정정) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

