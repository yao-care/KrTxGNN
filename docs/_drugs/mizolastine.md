---
layout: default
title: Mizolastine
parent: 모델 예측만 (L5)
nav_order: 524
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Mizolastine: 예측 신규 적응증 급성 간헐성 포르피린증 (Acute Intermittent Porphyria) (근거 수준 L5). 기존 적응증: 허가 적응증 텍스트가 링크로만 제공되어 구체적인 내용을 확인할 수 없음 (항히스타민제로 분류)"
monitor_inn: "MIZOLASTINE"
predicted_indications: ["acute intermittent porphyria", "psychogenic movement disorders", "lingual-facial-buccal dyskinesia", "chronic tic disorder", "benign shuddering attacks", "extrapyramidal and movement disease", "primary orthostatic tremor", "tremor-nystagmus-duodenal ulcer syndrome", "benign paroxysmal tonic upgaze of childhood with ataxia", "carbamoyl phosphate synthetase I deficiency disease"]
---

# Mizolastine
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

# Mizolastine: 알레르기 질환에서 급성 간헐성 포르피린증으로

## 한 문장 요약

Mizolastine은 2세대 H1 수용체 길항제(항히스타민제)로, 한국에서 단일제로 허가되어 시판되고 있습니다.
TxGNN 모델은 **급성 간헐성 포르피린증(Acute Intermittent Porphyria)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 지지하는 **임상시험은 0건, 문헌도 0편**입니다.
따라서 이 예측은 모델 계산에만 근거한 가설 수준입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 텍스트가 링크로만 제공되어 구체적인 내용을 확인할 수 없음 (항히스타민제로 분류) |
| 예측 신규 적응증 | 급성 간헐성 포르피린증 (Acute Intermittent Porphyria) |
| TxGNN 예측 점수 | 99.76% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Mizolastine은 H1 수용체(HRH1)를 표적으로 하는 2세대 항히스타민제이며, 알레르기 질환 치료제로 세계 여러 나라에서 사용됩니다. 미국에서는 승인되지 않았습니다.

급성 간헐성 포르피린증은 헤me 생합성 경로의 포르포빌리노겐 탈아미노효소 결핍으로 생기는 대사 질환입니다. H1 수용체 차단과 이 경로 사이에 확립된 기전적 연결고리는 확인되지 않습니다. 항히스타민제는 일반적으로 이 질환의 관리에 사용되지 않으며, 포르피린증 환자에서 Mizolastine의 안전성(포르피린 생성 유발 가능성)도 평가된 적이 없습니다.

따라서 높은 TxGNN 점수는 지식 그래프상의 근접성을 반영한 계산상 예측일 뿐이며, 약리학적 타당성은 현재 뒷받침되지 않습니다. 같은 약물의 다른 상위 예측들(정신인성 운동장애, 만성 틱 장애, 원발성 기립성 진전 등)도 모두 근거가 없는 L5 수준입니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200001929 | 부광미졸렌정10밀리그램(미졸라스틴) | 흰색의 장방형 필름코팅정 | 허가사항 문서 링크로만 제공됨 (MFDS 허가정보 참조) |

## 안전성 고려사항

- **약물 상호작용**: 약리학 데이터상 H1 수용체(HRH1)를 표적으로 하는 길항제로 확인되었습니다. 약물-약물 상호작용 항목은 별도로 보고된 것이 없습니다.

그 외 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
급성 간헐성 포르피린증에 대한 예측은 모델 점수에만 의존하며, 임상시험과 문헌이 전혀 없고 기전적 연결고리도 불분명합니다. 또한 포르피린증 환자에서의 안전성이 평가되지 않아 현 단계에서 진행하기는 어렵습니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기 포함)의 확보 및 분석 (MFDS 허가 문서)
- 상세한 약물 작용 기전(MOA) 데이터 확보
- 포르피린증 환자에서의 포르피린 생성 가능성 등 안전성 평가
- H1 수용체 길항과 헴 생합성 경로 사이의 연관성을 뒷받침하는 전임상 또는 문헌 근거
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

