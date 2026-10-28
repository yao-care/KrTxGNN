---
layout: default
title: Mepolizumab
parent: 모델 예측만 (L5)
nav_order: 502
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Mepolizumab: 예측 신규 적응증 면역 파괴에 의한 혈소판감소증 (thrombocytopenia due to immune destruction) (근거 수준 L4). 기존 적응증: 허가 적응증 본문은 허가증 링크로만 제공되어 확인되지 않음 (허가사항 참조)"
monitor_inn: "MEPOLIZUMAB"
predicted_indications: ["thrombocytopenia due to immune destruction", "primary release disorder of platelets", "pseudo-von Willebrand disease", "autoimmune thrombocytopenic", "Glanzmann thrombasthenia"]
---

# Mepolizumab
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

## Mepolizumab: 허가 적응증에서 면역 파괴에 의한 혈소판감소증으로
{: .text-alpha }

## 한 문장 요약

Mepolizumab은 항 IL-5 단클론항체로, 한국에서 누칼라(Nucala) 제품으로 허가되어 시판 중입니다.
TxGNN 모델은 **면역 파괴에 의한 혈소판감소증(thrombocytopenia due to immune destruction)**에 효과가 있을 수 있다고 예측하지만, 현재 임상시험은 **0건**이며 직접 관련된 문헌은 **1편(증례 보고)**에 그칩니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문은 허가증 링크로만 제공되어 확인되지 않음 (허가사항 참조) |
| 예측 신규 적응증 | 면역 파괴에 의한 혈소판감소증 (thrombocytopenia due to immune destruction) |
| TxGNN 예측 점수 | 0.9966 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 2건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 없습니다. 다만 mepolizumab은 IL-5를 차단하여 호酸球(호산구)를 감소시키는 항체로 알려져 있으며, 이 분석에서는 호산구 매개 면역 이상이 있는 경우에 한해 연관성을 고려할 수 있습니다.

신규 적응증과의 연관성은 제한적입니다. 면역성 혈소판감소증이 호산구증가증과 동반되는 경우에만 기전상 가능성이 있습니다. 반면 호산구가 없는 원발성 면역성 혈소판감소증에서 IL-5 차단이 효과가 있다는 근거는 없습니다.

참고로 유일한 문헌(PMID 28648630)은 스테로이드 불응성 호산구증가성 면역 이상이 mepolizumab과 병용 요법으로 호전된 증례 보고입니다. 병용 치료가 있었으므로 mepolizumab 단독 효과로 해석할 수 없습니다. 0.9966이라는 높은 점수는 컴퓨터 예측일 뿐, 임상시험 데이터로 뒷받침되지 않습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [28648630](https://pubmed.ncbi.nlm.nih.gov/28648630/) | 2018 | 증례 보고 | Blood Cells Mol Dis | 스테로이드 불응성 호산구증가성 면역 이상이 mepolizumab 투여 후 해소되고 혼합형 혈栓성 미세혈관병증도 호전됨 (병용 치료로 단독 효과 판단 불가) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201601746 | 누칼라주(메폴리주맙, 유전자재조합) | 동결건조 분말 주사제 (용해 후 투여) | 허가증 원문 링크 참조 |
| 202500679 | 누칼라오토인젝터주(메폴리주맙) | 오토인젝터 장착 프리필드시린지 주사제 | 허가증 원문 링크 참조 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
면역성 혈소판감소증에 대한 임상시험이 없고, 유일한 문헌은 병용 치료가 포함된 증례 보고입니다. 높은 TxGNN 점수 외에 이를 뒷받침할 근거가 부족합니다.

**진행하려면 필요한 것:**
- 허가 적응증 및 경고·금기 정보 확보 (허가증 PDF 확인)
- 작용 기전 데이터 보완
- 호산구증가증이 동반된 면역성 혈소판감소증 하위군에 대한 추가 문헌 조사 및 전임상/임상 근거
- 호산구 비의존성 혈소판감소증에 대한 기전적 타당성 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

