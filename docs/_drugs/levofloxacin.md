---
layout: default
title: Levofloxacin
parent: 모델 예측만 (L5)
nav_order: 473
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Levofloxacin: 예측 신규 적응증 점상 상피성 각결막염 (Punctate Epithelial Keratoconjunctivitis) (근거 수준 L5). 기존 적응증: 데이터에서 확인되지 않음 (허가 적응증 본문 없이 허가 문서 링크만 제공됨)"
monitor_inn: "Levofloxacin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder"]
---

# Levofloxacin
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

## Levofloxacin: 세균 감염증에서 점상 상피성 각결막염으로
{: .text-alpha }

## 한 문장 요약

Levofloxacin은 광범위 플루오로퀴놀론계 항균제로, 한국에서 세균 감염 치료에 사용되고 있습니다.
TxGNN 모델은 **점상 상피성 각결막염(Punctate Epithelial Keratoconjunctivitis)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 지지하는 **임상시험은 0건**이고 **문헌은 1편(집단 발생 보고)**뿐이며 효능을 보여 주는 근거는 아닙니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터에서 확인되지 않음 (허가 적응증 본문 없이 허가 문서 링크만 제공됨) |
| 예측 신규 적응증 | 점상 상피성 각결막염 (Punctate Epithelial Keratoconjunctivitis) |
| TxGNN 예측 점수 | 0.9992 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Levofloxacin은 DNA gyrase와 topoisomerase IV를 억제하는 플루오로퀴놀론계 항균제이며, 점안액 제형은 세균성 결막염에 사용됩니다. 이 점이 안구 표면 감염과의 유일한 연결고리입니다.

그러나 점상 상피성 각결막염은 바이러스(아데노바이러스 등)나 미포자충이 원인인 경우가 많고, 플루오로퀴놀론은 이들 병원체에 대한 확립된 활성이 없습니다. 이번에 연결된 문헌도 대만 수영장 수질 오염과 관련된 미포자충 각결막염 집단 발생 보고이며, Levofloxacin의 이점을 보여 주지 않습니다. 따라서 높은 예측 점수는 모델 예측일 뿐, 기전적·임상적 뒷받침은 부족합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | 집단 발생 보고 | American Journal of Ophthalmology | 대만 수영장 수질 오염과 관련된 미포자충 각결막염 집단 발생 보고. Levofloxacin의 효과는 제시되지 않음 |

## 한국 시판 정보

허가증 20건이 모두 유효하며, 단일 성분 제제입니다. 허가 적응증은 본문이 아닌 허가 문서 링크로만 제공되어 요약할 수 없습니다. 주요 5건은 다음과 같습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199400461 | 제일크라비트정 | 필름코팅정 | 허가 문서 참조 |
| 199800676 | 크라비트주 | 주사제(바이알) | 허가 문서 참조 |
| 200600109 | 크라비트정500밀리그람 | 필름코팅정 | 허가 문서 참조 |
| 200400034 | 레포신주 | 주사제(바이알) | 허가 문서 참조 |
| 201308471 | 카바스타점안액(레보플록사신수화물) | 점안액 | 허가 문서 참조 |

한국에는 점안액 제형(카바스타점안액 등)도 허가되어 있으나, 적응증 본문을 확인할 수 없어 각결막염 관련 여부는 허가사항에서 확인해야 합니다.

## 안전성 고려사항

- **약물 상호작용**: 데이터가 확인된 상호작용은 100건입니다. 이 중 주요(Major) 등급은 다음과 같습니다.
  - Tramadol
  - Hydrocortisone
- 중등도(Moderate) 등급에는 Abiraterone, Acarbose, Famotidine, Formoterol, Ketorolac, Ibuprofen, Metformin, Pioglitazone 등이 포함됩니다.

그 밖의 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
임상시험이 없고 문헌도 집단 발생 보고 1편뿐이며, 원인 병원체(바이러스·미포자충)에 대한 Levofloxacin의 활성도 확립되어 있지 않습니다. 높은 TxGNN 점수만으로는 진행 근거가 되지 않습니다.

**진행하려면 필요한 것:**
- 한국 허가 적응증 본문 확보 (기존 적응증 확인 및 점안액 허가 범위 검토)
- 점상 상피성 각결막염의 원인별(세균성 여부) 효능을 평가한 임상 또는 전임상 근거
- 허가사항의 경고·금기 정보 확인
- 작용 기전 데이터 보완

---

**참고 (다른 예측 적응증):** 데이터에는 순위 7위 **단클론 감마글로불린병증**과 9위 **패혈성 페스트**도 있습니다. 전자는 다발성 골수종에서 예방적 Levofloxacin을 평가한 3상 RCT(TEAMM)가 있으나 감염 예방 목적이며 MGUS로 확대 해석할 수 없습니다. 후자는 주로 동물 실험 근거이며 결과가 엇갈립니다. 이 두 질환은 별도 평가를 권고합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

