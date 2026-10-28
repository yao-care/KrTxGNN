---
layout: default
title: Propylene Glycol
parent: 모델 예측만 (L5)
nav_order: 634
evidence_level: L5
indication_count: 10
monitor_inn: "PROPYLENE GLYCOL"
predicted_indications: ["bronchitis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "cortical cataract", "nuclear senile cataract", "senile cataract", "diabetic cataract", "craniostenosis cataract", "tetanic cataract", "mature cataract"]
last_modified_at: 2026-10-28
description: "Propylene Glycol: 예측 신규 적응증 기관지염 (근거 수준 L5). 기존 적응증: 확인 불가 (허가 적응증 항목에 문서 링크만 있고 본문이 없음)"
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

## Propylene Glycol: 점안액 성분에서 기관지염으로
{: .text-alpha }

## 한 문장 요약

Propylene Glycol은 한국에서 점안액(수출용) 3개 제품의 성분으로 허가되어 있습니다. 다만 허가 적응증의 구체적인 내용은 이번 데이터에 포함되어 있지 않습니다.
TxGNN 모델은 **기관지염(bronchitis)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 다룬 임상시험은 없습니다. 문헌 3편도 치료 효과가 아닌 전자담배 에어로졸의 기도 자극 가능성 등을 다루고 있어 근거가 매우 약합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 적응증 항목에 문서 링크만 있고 본문이 없음) |
| 예측 신규 적응증 | 기관지염 |
| TxGNN 예측 점수 | 0.9990 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 3건 (모두 단일 성분, 유효) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. Propylene Glycol은 점안액 제품(수출용)의 성분으로 허가되어 있으나, 허가 적응증 본문을 확인할 수 없어 기존 적응증과 기관지염 사이의 기전적 연관성을 설명하기 어렵습니다.

제시된 문헌은 오히려 반대 방향의 신호를 보여줍니다. Propylene Glycol은 전자담배 액상의 구성 성분으로, 흡입된 에어로졸이 기도 자극이나 천식 악화와 연관될 수 있다고 보고됩니다. 따라서 높은 TxGNN 점수는 치료 신호라기보다 TxGNN 모델(딥러닝)이 관련 질환 사이에서 학습한 유사성을 반영했을 가능성이 크며, 생물학적 근거는 아닙니다. 세 번째 문헌(퀘르세틴, 마우스 COPD 모델)은 Propylene Glycol을 치료제로 다루지 않습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [26408554](https://pubmed.ncbi.nlm.nih.gov/26408554/) | 2015 | Review | Am J Physiol Lung Cell Mol Physiol | 만성 전자담배 사용이 폐질환(만성 기관지염 포함 COPD)을 일으킬 수 있는지 검토 |
| [28983782](https://pubmed.ncbi.nlm.nih.gov/28983782/) | 2017 | Review | Curr Allergy Asthma Rep | 전자담배 구성 성분과 에어로졸의 기도 자극 물질 및 천식과의 잠재적 연관성 |
| [20920189](https://pubmed.ncbi.nlm.nih.gov/20920189/) | 2010 | 전임상(동물) | Respir Res | 엘라스타제/LPS 노출 마우스에서 퀘르세틴이 MMP 발현을 조절해 질병 진행을 억제 (Propylene Glycol 무관) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202001451 | 울트라릴리프점안액(수출용) | 점안제 | 본문 정보 없음 |
| 201505058 | 발란스피이지점안액(프로필렌글리콜)(수출용) | 점안액 | 본문 정보 없음 |
| 201500588 | 밸런스루브리컨트점안액(수출용) | 점안제 | 본문 정보 없음 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
기관지염을 직접 다룬 임상시험이나 치료 효과 문헌이 없어 근거 수준은 L5입니다. 제시된 문헌은 오히려 흡입 시 기도 자극 가능성을 시사하므로, 높은 예측 점수만으로 진행하기는 어렵습니다.

**진행하려면 필요한 것:**
- 한국 허가 적응증 본문 및 허가사항(경고·금기) 확인
- 작용 기전(MOA) 데이터 확보
- 기관지염에서 Propylene Glycol의 치료 효과를 직접 평가한 연구
- 흡입 경로의 안전성 검토 (현재 허가 제형은 모두 점안제)

---

**참고: 다른 예측 적응증**

동일한 약물에 대해 다음 질환도 예측되었으나, 모두 Hold 판정입니다.

- **당뇨망막병증(diabetic retinopathy, 점수 0.9968)**: 직접 연구가 없어 근거 수준은 L5로 판단합니다. 제시된 임상시험(NCT07090044)은 주사 후 통증을 비교한 시험이며, 문헌 중 임상 연구(PMID 39006273)는 별개 화합물인 propylene glycol mannate sulfate를 다룹니다.
- **중증 비증식성 당뇨망막병증, 백내장 계열(피질, 핵, 노인성, 당뇨, 성숙 등)**: 임상시험과 문헌이 없거나 제형 개발 연구(부형제 사용)에 한정되어 모델 예측만 있는 수준(L5)입니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

