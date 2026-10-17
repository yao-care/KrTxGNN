---
layout: default
title: Vitamin A
parent: 모델 예측만 (L5)
nav_order: 786
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Vitamin A: 예측 신규 적응증 선천성 프로트롬빈 결핍증 (congenital prothrombin deficiency) (근거 수준 L5). 기존 적응증: 육체피로 및 체력 저하 시 비타민 A·D·E·B군·C 보급, 눈의 건조감 완화, 야맹증, 피부염·구내염 증상 완화 등"
monitor_inn: "Vitamin A"
predicted_indications: ["congenital prothrombin deficiency", "biotin metabolic disease", "non-syndromic esophageal malformation", "injury", "cell proliferation disorder", "florid cemento-osseous dysplasia", "segmental odontomaxillary dysplasia", "perinatal disease", "disease by subcellular system affected", "radiation or chemically induced disorder"]
---

# Vitamin A
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

# Vitamin A: 비타민 보급·야맹증 등에서 선천성 프로트롬빈 결핍증으로

## 한 문장 요약

Vitamin A는 원래 비타민 보급, 눈의 건조감 완화, 야맹증 등에 사용되는 지용성 비타민입니다.
TxGNN 모델은 **선천성 프로트롬빈 결핍증(congenital prothrombin deficiency)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다. 따라서 이 예측은 모델 점수에만 근거한 가설 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 육체피로 및 체력 저하 시 비타민 A·D·E·B군·C 보급, 눈의 건조감 완화, 야맹증, 피부염·구내염 증상 완화 등 |
| 예측 신규 적응증 | 선천성 프로트롬빈 결핍증 (congenital prothrombin deficiency) |
| TxGNN 예측 점수 | 99.97% (전체 순위 996위) |
| 근거 수준 | L5 (모델 예측만 있음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Vitamin A는 시각 회로, 상피세포 분화, 면역 기능에 관여하는 필수 영양소입니다. 국내에서는 다른 비타민과 함께 영양 보급 목적의 제품으로 허가되어 있습니다.

그러나 신규 적응증과의 기전적 연관성은 약합니다. 프로트롬빈(응고인자 II) 합성은 **비타민 K 의존적 감마-카르복실화**에 의존하며, Vitamin A가 이 과정에 관여한다는 근거는 알려져 있지 않습니다. 선천성 프로트롬빈 결핍증은 유전적 원인으로 생기는 응고인자 결핍입니다. 따라서 이 높은 점수는 비타민·영양소 계열 약물이 지식 그래프에서 서로 가까운 이웃으로 연결되어 나온 결과일 가능성이 큽니다. 현 시점에서 치료적 타당성을 뒷받침하는 근거는 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200100244 | 비나폴로엑스트라연질캡슐 ((주)유유제약) | 연질캡슐 | 이 약은 육체피로, 임신ㆍ수유기, 병중ㆍ병후(병을 앓는 동안이나 회복 후)의 체력 저하 시, 발육기, 노년기의 비타민 A, D, E, B1, B2, B6, C의 보급과 눈의 건조감의 완화... |

## 안전성 고려사항

허가사항의 경고 및 금기 정보는 이번 보고서에 반영하지 못했으므로 허가사항을 직접 확인하세요. 아래는 다른 출처에서 확인된 참고 정보입니다.

- **지식 그래프 기반 금기 질환 (허가 문서가 아닌 모델 데이터)**: 신장 질환, 간 질환, 담낭 질환, 소화성 궤양, 유육종증, 고칼슘혈증, 신석회증, 신장결석, 염증성 장질환(궤양성 대장염 포함), 용혈성 빈혈, 겸상적혈구빈혈, 윌슨병, 유전성 혈색소침착증, 비타민 과다증 등이 연결되어 있습니다.
- **약물 상호작용**: 총 68건이 확인되었습니다. 주요(Major) 등급은 다음과 같습니다.
  - 레티노이드 계열: Isotretinoin, Acitretin, Tretinoin
  - 테트라사이클린 계열: Doxycycline, Minocycline, Tetracycline, Oxytetracycline, Demeclocycline, Omadacycline, Eravacycline, Sarecycline
- **중등도(Moderate) 상호작용**: Bexarotene, 담즙산 결합제(Cholestyramine, Colesevelam, Colestipol), Sevelamer, Selpercatinib
- **경미(Minor) 상호작용**: Orlistat

## 결론 및 다음 단계

**결정: Hold**

**사유:**
선천성 프로트롬빈 결핍증에 대해서는 임상시험과 문헌이 모두 없고 근거 수준이 L5입니다. 프로트롬빈 합성은 비타민 K에 의존하므로 Vitamin A의 기전적 연결 고리도 불분명합니다. 모델 점수가 매우 높아도 이 방향의 개발을 정당화하기에는 부족합니다.

**진행하려면 필요한 것:**
- Vitamin A와 프로트롬빈 합성·응고 경로 사이의 기전적 연관성을 뒷받침하는 전임상 근거
- 허가사항의 경고·금기 정보 확보 및 안전성 검토 (간독성, 과다복용, 임신 시 催奇形性 위험 포함)
- 작용 기전(MOA) 데이터 보완
- 이 약의 다른 예측 후보 중에는 근거가 더 풍부한 것이 있습니다. 예를 들어 '주산기 질환'(저체중 출생아의 기관지폐이형성증 예방 관련 Cochrane 체계적 문헌고찰)이 있어, 우선순위 재검토를 권고합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

