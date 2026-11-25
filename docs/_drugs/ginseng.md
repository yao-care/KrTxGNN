---
layout: default
title: Ginseng
parent: 모델 예측만 (L5)
nav_order: 375
evidence_level: L5
indication_count: 10
monitor_inn: "Ginseng"
predicted_indications: ["drug-induced osteoporosis", "acne (disease)", "severe nonproliferative diabetic retinopathy", "hemorrhagic disease of newborn", "nuclear senile cataract", "cortical cataract", "diabetic retinopathy", "amenorrhea (disease)", "tetanic cataract", "diabetes mellitus type 2 associated cataract"]
last_modified_at: 2026-11-25
description: "Ginseng: 예측 신규 적응증 약물유발 골다공증 (근거 수준 L5). 기존 적응증: 병후 체력저하, 피로권태, 식욕감퇴(식욕부진), 도한(盜汗, 야간에 자 는 동안 땀이 나지만 느끼지 못하고…"
---

# Ginseng
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

## Ginseng: 허가 적응증 정보 미확인 상태에서 약물유발 골다공증으로
{: .text-alpha }

## 한 문장 요약

인삼(Ginseng)은 한국에서 십전대보탕, 인삼패독산 등 한약 복합 처방의 구성 성분으로 허가를 받은 생약입니다. TxGNN 모델은 **약물유발 골다공증(drug-induced osteoporosis)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 다룬 임상시험과 문헌은 **0건**입니다. 따라서 근거 수준은 모델 예측에 그치는 L5입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 병후 체력저하, 피로권태, 식욕감퇴(식욕부진), 도한(盜汗, 야간에 자 는 동안 땀이 나지만 느끼지 못하고 깨어나면 땀이 그치는 증상), 손발이 차가움, 빈혈 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/197900047/EE)) |
| 예측 신규 적응증 | 약물유발 골다공증 |
| TxGNN 예측 점수 | 0.9995 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 18건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 인삼의 주성분인 진세노사이드가 일반적인 골 생물학에서 조골세포와 파골세포 활동에 영향을 줄 수 있다는 가설은 있으나, 이번에 수집된 데이터에서는 이를 뒷받침하는 근거가 확인되지 않았습니다.

기존 적응증과 신규 적응증 사이의 연관성도 평가되지 않은 상태입니다. 예측 점수는 TxGNN 모델(딥러닝)에서 나온 값이며, 모델이 관련 질환 사이에서 학습한 유사성을 반영할 수 있을 뿐 생물학적 근거는 아닙니다. 약인성 골다공증에 대한 효과는 가설 단계입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

허가가 여러 건 확인되었으며(허가 건수와 상태는 빠른 개요 참조), 전체 목록의 일부일 수 있습니다. 모두 한약 복합 처방 제품으로 보이므로, 이 허가 정보를 인삼 단일 성분의 허가 현황으로 해석해서는 안 됩니다. 허가 적응증 칸에는 본문 대신 문서 링크만 수록되어 있어 적응증 내용은 확인할 수 없습니다. 아래는 주요 5건입니다.

<!-- review:begin kr-lic-20261125c-ginseng-1 -->

> **검토 정정 (2026-11-25)**: 원래 문장: “허가 20건이 확인되었으며, 전체 목록의 일부일 수 있습니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-25 데이터) 기준으로 수정했습니다: 이 페이지의 자료는 허가의 일부만 수록하고 있어(빠른 개요에 「최소 …건」으로 표시), 본문에 쓴 건수가 전체 건수가 아닙니다. 건수는 쓰지 않고 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261125c-ginseng-1 -->

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 197900047 | 데시텐과립(십전대보탕) | 흑갈색의 과립제. | (유)한풍제약 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/197900047/EE) | 유효 |
| 200004501 | 패감산과립(인삼패독산) | 회갈색의 과립 | 한솔신약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200004501/EE) | 유효 |
| 200005653 | 경방이중탕엑스과립 | 황갈색의 과립제 | 경방신약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200005653/EE) | 유효 |
| 200404344 | 가쁘레엑스과립(인삼패독산) | 담갈색의 과립제 | 경방신약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200404344/EE) | 유효 |
| 202401570 | 진삼소음액 | 흑갈색의 액제 | 메딕스제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202401570/EE) | 취하 |

위 표는 허가 최소 20건 중 5건입니다.

<!-- licenses:end -->

## 안전성 고려사항

- **약물 상호작용**: 데이터에 83건의 상호작용이 기록되어 있으며, 표시된 항목은 모두 중등도(Moderate)입니다. 주로 혈당 강하제와의 상호작용입니다.
  - 경구 혈당강하제: acarbose, metformin, pioglitazone, glimepiride, chlorpropamide
  - DPP-4 억제제: alogliptin, linagliptin
  - SGLT2 억제제: canagliflozin, dapagliflozin, empagliflozin
  - GLP-1 계열: albiglutide, dulaglutide, semaglutide, lixisenatide
  - 인슐린: aspart, degludec, detemir, glargine, glulisine
  - 기타: acetylsalicylic acid(아스피린)
- 병용 시 혈당 변화를 주의해서 관찰해야 하는 것으로 해석됩니다.

경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
약물유발 골다공증에 대한 예측은 모델 점수만 있을 뿐 임상시험과 문헌이 전혀 없어 근거 수준이 L5입니다. 작용 기전과 허가 적응증 본문, 안전성 정보(경고·금기)도 확보되지 않아 현 단계에서는 진행하기 어렵습니다.

**진행하려면 필요한 것:**
- 허가 문서(MFDS 첨부문서)에서 적응증, 경고, 금기 정보 확보
- 인삼 및 진세노사이드의 작용 기전 데이터 확보
- 골다공증 관련 전임상·임상 문헌 탐색
- 혈당강하제 등 병용 약물과의 상호작용 검토

## 참고: 다른 예측 적응증

이번 보고서는 1순위 예측을 중심으로 작성했습니다. 이번 데이터에서 다른 예측 질환 중 문헌이 가장 많은 것은 당뇨병성 망막병증(문헌 20편)이며, 대부분 동물·세포·컴퓨터 기반 연구입니다. 이 질환을 직접 다룬 2026년 전향적 무작위 이중맹검 임상시험(PMID 42395017)이 보고되었지만, 설계와 규모는 전문 확인이 필요합니다. 별도 평가를 고려할 수 있습니다.

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-25 | 허가 건수: “허가 20건이 확인되었으며, 전체 목록의 일부일 수 있습니다.” → 건수를 쓰지 않도록 수정(건수는 빠른 개요와 표) | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

