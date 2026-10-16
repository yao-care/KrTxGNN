---
layout: default
title: Taurolidine
parent: 모델 예측만 (L5)
nav_order: 718
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Taurolidine: 예측 신규 적응증 당뇨병성 백내장 (Diabetic Cataract) (근거 수준 L5). 기존 적응증: 허가 문서 링크만 확인되며, 적응증 본문은 이번 데이터에 포함되지 않음"
monitor_inn: "Taurolidine"
predicted_indications: ["diabetic cataract", "cortical cataract", "nuclear senile cataract", "mature cataract", "tetanic cataract", "immature cataract", "diabetes mellitus type 2 associated cataract", "craniostenosis cataract", "diabetic retinopathy", "senile cataract"]
---

# Taurolidine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 약사 평가 보고서

</div>

# Taurolidine: 감염 관련 용도에서 당뇨병성 백내장으로

## 한 문장 요약

Taurolidine(타우롤리딘)은 국내에서 주사용 액제로 허가·시판 중인 약물입니다. TxGNN 모델은 **당뇨병성 백내장(Diabetic Cataract)**에 효과가 있을 수 있다고 예측하지만, 이 방향을 지지하는 **임상시험은 0건**, **문헌도 0편**입니다. 현재는 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 문서 링크만 확인되며, 적응증 본문은 이번 데이터에 포함되지 않음 |
| 예측 신규 적응증 | 당뇨병성 백내장 (Diabetic Cataract) |
| TxGNN 예측 점수 | 98.94% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. Taurolidine은 타우린에서 유래한 메틸올 전달 물질로, 항균 및 내독소 중화 활성이 알려져 있습니다. 그러나 이 활성이 수정체 혼탁이나 당뇨병성 백내장의 폴리올 경로·산화 스트레스 기전과 연결된다는 근거는 확립되어 있지 않습니다.

TxGNN의 상위 예측 10건 중 대부분이 백내장 하위 유형(피질성, 핵성 노인성, 성숙, 미성숙 등)이며 점수가 거의 같습니다(98.8~98.9%). 이는 약물 고유의 신호라기보다 질환 간 그래프 유사성에 따른 결과일 가능성이 있습니다. 당뇨병성 망막병증(98.86%)에 대해서는 전임상 종양학 연구에서 보고된 항염증·항혈관신생 효과가 연결고리가 될 수 있다는 추측이 있으나, 이번 데이터로 뒷받침되지 않으며 전임상 검증이 선행되어야 합니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202501709 | 유케이타우로키트2%주 (타우로리딘) | 무색투명한 병에 든 무색 또는 담황색의 투명한 액제 | 허가 문서 참조 ([MFDS 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202501709/EE)) |
| 198700927 | 삼진타우로린주사2% (타우로리딘) | 무색투명한 병에 든 무색 또는 담황색의 투명한 액제 | 허가 문서 참조 ([MFDS 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198700927/EE)) |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
당뇨병성 백내장 예측은 TxGNN 점수(98.94%)만 있고 임상시험과 문헌이 모두 없어 근거 수준이 L5입니다. 작용 기전 데이터가 없고 안과 투여 경로의 적합성도 확인되지 않았습니다.

**진행하려면 필요한 것:**
- 허가 문서(MFDS 첨부문서)에서 기존 적응증, 경고 및 금기 정보 확보
- DrugBank 등에서 작용 기전(MOA) 데이터 보완
- 수정체 혼탁 및 당뇨병성 백내장 모델에서의 전임상 검증
- 안과 투여 경로(현재 허가 제형은 주사용 액제)의 적합성과 안전성 평가
- 백내장 하위 유형 간 점수 유사성이 그래프 구조에 의한 것인지 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

