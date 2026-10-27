---
layout: default
title: Propylene Glycol
parent: 모델 예측만 (L5)
nav_order: 634
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Propylene Glycol: 예측 신규 적응증 기관지염 (Bronchitis) (근거 수준 L5). 기존 적응증: 허가 적응증 본문 없음 (허가 문서 링크만 제공됨)"
monitor_inn: "PROPYLENE GLYCOL"
predicted_indications: ["bronchitis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "cortical cataract", "nuclear senile cataract", "senile cataract", "diabetic cataract", "mature cataract", "immature cataract", "craniostenosis cataract"]
---

# Propylene Glycol
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

## Propylene Glycol: 점안제 첨가제·보습제에서 기관지염으로
{: .text-alpha }

## 한 문장 요약

Propylene glycol은 한국에서 점안액(수출용) 제품에 사용되는 성분입니다. TxGNN 모델은 **기관지염(bronchitis)**에 효과가 있을 수 있다고 예측하지만, 이 예측을 지지하는 임상시험은 **0건**이며 관련 문헌 3편도 치료 효과가 아니라 전자담배 에어로졸의 기도 자극 가능성이나 다른 주제를 다룹니다. 따라서 모델 점수가 높아도 실제 근거는 매우 약합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문 없음 (허가 문서 링크만 제공됨) |
| 예측 신규 적응증 | 기관지염 (Bronchitis) |
| TxGNN 예측 점수 | 99.90% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 3건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. Propylene glycol은 의약품 첨가제와 전자담배 에어로졸의 구성 성분으로 널리 알려져 있으며, 한국에서는 점안액 제품(안구 건조 완화 목적으로 추정되나 허가 적응증 본문은 확인되지 않음)에 사용됩니다.

기관지염에 대한 치료 기전은 데이터상 뒷받침되지 않습니다. 검색된 문헌은 흡입된 propylene glycol 에어로졸이 기도 자극이나 폐 질환 악화와 연관될 수 있다는 내용으로, 오히려 치료 효과와 반대 방향의 우려를 시사합니다. 높은 TxGNN 점수는 지식 그래프상의 인위적 연관일 가능성이 큽니다.

참고로 다른 예측 질환(당뇨망막병증, 백내장 등)도 안과 질환이지만, 이 역시 직접적인 근거가 없습니다. 당뇨망막병증 관련 문헌 중 propylene glycol mannate sulfate(PGMS) 연구는 propylene glycol과 다른 화합물에 대한 것이므로 이 약물의 근거로 볼 수 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [26408554](https://pubmed.ncbi.nlm.nih.gov/26408554/) | 2015 | Review | Am J Physiol Lung Cell Mol Physiol | 전자담배 장기 사용이 폐 질환을 유발할 수 있는지 검토. 치료 효과에 대한 내용 아님 |
| [28983782](https://pubmed.ncbi.nlm.nih.gov/28983782/) | 2017 | Review | Curr Allergy Asthma Rep | 전자담배 성분과 천식의 연관성 검토. 기도 자극 물질 및 독성 우려 |
| [20920189](https://pubmed.ncbi.nlm.nih.gov/20920189/) | 2010 | 전임상(동물) | Respir Res | 쿼세틴이 COPD 마우스 모델에서 염증과 폐 기능을 개선. propylene glycol과 직접 관련 없음 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202001451 | 울트라릴리프점안액(수출용) | 점안제 (무색 투명한 액) | 적응증 본문 미확인 (허가 문서 링크만 제공) |
| 201505058 | 발란스피이지점안액(프로필렌글리콜)(수출용) | 점안액 (흰색~미백색) | 적응증 본문 미확인 (허가 문서 링크만 제공) |
| 201500588 | 밸런스루브리컨트점안액(수출용) | 점안제 (불투명한 용액) | 적응증 본문 미확인 (허가 문서 링크만 제공) |

## 결론 및 다음 단계

**결정: Hold**

**사유:**
기관지염에 대한 임상시험이 없고, 문헌도 치료 효과를 지지하지 않으며 오히려 흡입 시 기도 자극 우려를 시사합니다. 허가 제품도 모두 점안제(수출용)여서 호흡기 투여 경로와도 맞지 않습니다.

**진행하려면 필요한 것:**
- 허가사항의 경고·금기 및 적응증 본문 확보 (현재 확인되지 않아 안전성 검토 불가)
- 작용 기전 데이터 확보
- 기관지염에서 propylene glycol 자체의 치료 효과를 보여주는 전임상 또는 임상 근거
- 흡입 투여 시 안전성 평가 및 투여 경로 적합성 검토
- 안과 질환 예측(당뇨망막병증, 백내장 등)을 검토할 경우, PGMS 등 다른 화합물 문헌과 구분된 직접 근거
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

