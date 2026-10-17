---
layout: default
title: Lactic Acid
parent: 모델 예측만 (L5)
nav_order: 453
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Lactic Acid: 예측 신규 적응증 비정형 대동맥 협착증 (atypical coarctation of aorta) (근거 수준 L5). 기존 적응증: 확인 불가 (허가 적응증 텍스트가 문서 링크로만 제공됨)"
monitor_inn: "Lactic acid"
predicted_indications: ["atypical coarctation of aorta", "aortic malformation", "non-syndromic esophageal malformation", "amenorrhea (disease)", "dry eye syndrome", "esophageal disease", "double outlet right ventricle with atrioventricular septal defect, pulmonary stenosis, heterotaxy", "excretory apparatus of the lacrimal system anomaly", "eye disease", "cauda equina syndrome"]
---

# Lactic Acid
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

# Lactic acid: 기존 적응증 불명에서 비정형 대동맥 협착증(예측)으로

## 한 문장 요약

Lactic acid(젖산)는 한국에서 연속신대체요법(CRRT)용 액상제제인 헤모졸비제로액의 성분으로 허가되어 있으나, 허가 적응증의 구체적인 텍스트는 확인되지 않았습니다.
TxGNN 모델은 **비정형 대동맥 협착증(atypical coarctation of aorta)**에 효과가 있을 수 있다고 예측하지만, 이 예측을 지지하는 **임상시험은 0건**, **직접 관련 문헌도 없습니다.**
상위 10개 예측 전체가 근거 수준 L4~L5로, 현재로서는 모델 예측 단계에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 적응증 텍스트가 문서 링크로만 제공됨) |
| 예측 신규 적응증 | 비정형 대동맥 협착증 (atypical coarctation of aorta) |
| TxGNN 예측 점수 | 99.59% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 젖산은 체내에서 생성되는 내인성 대사산물이며, 한국에서는 헤모졸비제로액이라는 액상제제의 성분으로 허가되어 있습니다.

비정형 대동맥 협착증은 선천성 구조 이상입니다. 저분자 대사산물이 이런 구조적 결함을 교정한다고 보기는 어렵습니다. 이번 예측은 지식 그래프의 연결 구조에서 생긴 인공적 결과일 가능성이 높으며, 기전상 연결고리는 확인되지 않았습니다.

참고로 2순위 이하 예측(대동맥 기형, 식도 기형, 무월경, 안구건조증, 식도 질환 등)도 검토했지만 타당한 기전은 확인되지 않았습니다. 일부 문헌은 젖산이 오히려 질환을 악화시킬 수 있다고 시사합니다. 예를 들어 젖산이 VEGF 발현을 높여 맥락막 신생혈관을 촉진한다는 전임상 연구가 있고, 식도 편평세포암에서 항PD-1 효과를 저해한다는 보고도 있습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

1순위 예측(비정형 대동맥 협착증)에 대한 문헌은 없습니다. 아래는 2순위 예측인 대동맥 기형에서 검색된 문헌 중 일부입니다. 모두 젖산 치료 효과를 직접 검증한 연구는 아닙니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [23791497](https://pubmed.ncbi.nlm.nih.gov/23791497/) | 2013 | RCT | J Cardiothorac Vasc Anesth | 소아 심장수술 중 복합 한외여과 전략 평가 (젖산 중재 아님) |
| [3367436](https://pubmed.ncbi.nlm.nih.gov/3367436/) | 1988 | 전임상 | J Vasc Surg | 토끼 대동맥 협착 전후 대동맥벽의 호흡·해당과정과 동맥경화 감수성 |
| [25157439](https://pubmed.ncbi.nlm.nih.gov/25157439/) | 2015 | 전임상 | Catheter Cardiovasc Interv | 폴리젖산(PLLA) 생분해 스텐트의 토끼 하행대동맥 중기 결과 (소재 연구) |
| [31714687](https://pubmed.ncbi.nlm.nih.gov/31714687/) | 2020 | 증례군 | Catheter Cardiovasc Interv | PLLA 소재 생분해 심방중격결손 폐쇄 기구의 첫 인체 적용 |
| [32382764](https://pubmed.ncbi.nlm.nih.gov/32382764/) | 2020 | 증례 | Pediatr Cardiol | PLLA 흡수성 미세판을 이용한 선천성 심장질환 영아의 기관지연화증 치료 (기구 소재) |

이 문헌들은 젖산을 치료제로 쓴 근거가 아니라, 젖산이 수술 중 지표로 쓰였거나 폴리젖산이 기구 소재로 쓰인 키워드 일치 결과입니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200209451 | 헤모졸비제로액 | 투명한 Polyolefin 백에 들어있는 무색투명한 액상제제 | 허가 문서 링크로만 제공되어 적응증 요약 불가 |

제조사는 밴티브코리아주식회사입니다.

## 안전성 고려사항

- **약물 상호작용**: 총 17건이 확인되었으며, 모두 DDInter 기준입니다.
  - 중등도(Moderate):
    - 테트라사이클린계: Doxycycline, Tetracycline, Minocycline, Demeclocycline, Oxytetracycline
    - 살리실산계: Acetylsalicylic acid, Salicylic acid (sodium)
    - 에페드린계: Ephedrine, Ephedrine (nasal), Pseudoephedrine
  - 경미(Minor):
    - 설포닐우레아계: Chlorpropamide, Tolazamide, Glipizide, Glyburide, Acetohexamide, Tolbutamide
    - 기타: Methotrexate

허가사항의 경고 및 금기는 이번 자료에서 확보되지 않았으므로 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 점수는 99.59%로 높지만 임상시험과 직접 관련 문헌이 없고, 구조적 선천 기형을 대사산물로 치료한다는 기전도 성립하기 어렵습니다. 상위 10개 예측 모두 보류가 적절하며, 일부는 젖산이 해로울 수 있다는 방향의 문헌을 포함합니다.

**진행하려면 필요한 것:**
- 허가 적응증 텍스트 확보 (허가증 PDF 내려받아 분석)
- 약물 작용 기전(MOA) 데이터 확보
- 허가사항의 경고·금기 정보 확보 (안전성 1차 선별에 필요)
- 젖산이 예측 질환에 치료적 역할을 한다는 기전적 근거 정립
- 근거가 상대적으로 있는 안구 질환·식도 질환 등은 젖산의 작용 방향(유익/유해)을 먼저 규명
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

