---
layout: default
title: Cefamandole Nafate
parent: 모델 예측만 (L5)
nav_order: 187
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Cefamandole Nafate: 예측 신규 적응증 혈색소병증 (hemoglobinopathy) (근거 수준 L5). 기존 적응증: 허가 적응증 본문이 확보되지 않았습니다. 세팔로스포린계 항생제로서 세균 감염증 치료에 사용됩니다"
monitor_inn: "Cefamandole nafate"
predicted_indications: ["hemoglobinopathy", "myocardial infarction", "posteroinferior myocardial infarction", "posterolateral myocardial infarction", "septal myocardial infarction", "partial deletion of the short arm of chromosome 16", "Prinzmetal angina", "beta-thalassemia with other manifestations", "hemolytic anemia due to glucophosphate isomerase deficiency", "pyruvate kinase deficiency of red cells"]
---

# Cefamandole Nafate
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

# Cefamandole nafate: 세균 감염증에서 혈색소병증으로

## 한 문장 요약

Cefamandole nafate는 2세대 세팔로스포린계 항생제로, 한국에서 주사제로 허가되어 시판되고 있습니다.
TxGNN 모델은 **혈색소병증(hemoglobinopathy)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 지지하는 **임상시험은 0건**, **문헌도 0편**입니다.
모델 예측만 존재하는 단계이며, 약리학적 근거도 확인되지 않았습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 확보되지 않았습니다. 세팔로스포린계 항생제로서 세균 감염증 치료에 사용됩니다. |
| 예측 신규 적응증 | 혈색소병증 (hemoglobinopathy) |
| TxGNN 예측 점수 | 99.65% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Cefamandole nafate는 세균 세포벽 합성을 억제하는 2세대 세팔로스포린계 항생제입니다.

혈색소병증은 글로빈 사슬의 결함으로 발생하는 질환입니다. 항생제가 글로빈 유전자 발현, 적혈구 생성, 철 대사에 영향을 준다는 알려진 근거는 없습니다. 따라서 기전상 연결고리는 확립되어 있지 않습니다.

TxGNN 점수(99.65%)는 지식 그래프 기반 예측일 뿐입니다. 상위 예측 질환에는 심근경색의 해부학적 하위 유형(후하벽, 후측벽, 중격)이 여럿 포함되어 있는데, 이는 독립적인 근거가 아니라 질환 분류 체계상 인접 관계가 중복 반영된 신호일 가능성이 높습니다. 16번 염색체 단완 부분 결실 같은 예측도 그래프 구조에서 비롯된 인공적 결과일 가능성이 있습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 198800285 | 만세프주1그램(세파만돌나페이트) | 흰색 분말이 충진된 무색투명한 바이알제 (주사제) | 허가사항 문서 참조 |
| 198900736 | 영진세파만돌나페이트주1그람(수출용) | 용시 용해하여 사용하는 백색 분말 주사제 | 허가사항 문서 참조 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

참고로, 이번 예측 후보 중 심근경색과 관련해서는 Cefamandole이 가진 N-메틸티오테트라졸(NMTT) 측쇄가 저프로트롬빈혈증 및 출혈 위험과 연관된다고 알려져 있어, 급성 관상동맥 상황에서는 이점이 아니라 안전성 우려가 됩니다. 또한 세팔로스포린은 드물게 면역성 용혈을 일으킬 수 있어, 용혈성 빈혈 계열 질환에서는 위험 요인이 될 수 있습니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
혈색소병증 예측은 TxGNN 점수에만 의존하며, 임상시험과 문헌이 전혀 없고 기전상 연결고리도 확인되지 않습니다. 같은 약물의 다른 상위 예측(심근경색 계열, 적혈구 효소 결핍증 등)도 마찬가지로 근거가 없고, 일부는 약물 자체의 안전성 우려와 상충합니다.

**진행하려면 필요한 것:**
- 허가사항 PDF에서 적응증, 경고, 금기 정보를 확보
- DrugBank에서 작용 기전(MOA) 데이터 확보
- 혈색소병증과 이 약물을 연결하는 전임상 또는 기전 연구 근거
- 임상시험 및 문헌 검색을 통한 독립적 근거 확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

