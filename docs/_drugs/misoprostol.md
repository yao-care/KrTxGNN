---
layout: default
title: Misoprostol
parent: 모델 예측만 (L5)
nav_order: 521
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Misoprostol: 예측 신규 적응증 무월경 (Amenorrhea) (근거 수준 L5). 기존 적응증: 허가 적응증 본문은 확인되지 않음 (허가증 문서 링크만 제공됨)"
monitor_inn: "MISOPROSTOL"
predicted_indications: ["amenorrhea (disease)", "atypical coarctation of aorta"]
---

# Misoprostol
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **2** 건
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

## Misoprostol: 소화성 궤양 계열 약물에서 무월경으로
{: .text-alpha }

## 한 문장 요약

Misoprostol은 프로스타글란딘 E1(PGE1) 유사체로, 한국에서 단일제 정제로 허가되어 시판 중입니다. TxGNN 모델은 **무월경(amenorrhea)**에 효과가 있을 수 있다고 예측하지만, 이를 직접 뒷받침하는 임상시험은 **0건**이며 **7편의 문헌**도 대부분 임신 중절 관련 내용이라 근거가 간접적입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문은 확인되지 않음 (허가증 문서 링크만 제공됨) |
| 예측 신규 적응증 | 무월경 (Amenorrhea) |
| TxGNN 예측 점수 | 0.9964 |
| 근거 수준 | L5 (임상시험 없음, 기전적 연관성만 존재) |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 2건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Misoprostol은 프로스타글란딘 E1 유사체로, 자궁경부 숙화와 자궁 수축을 유도합니다. 이론적으로는 무월경이 조기 임신이나 잔류 임신 조직 때문일 때 자궁 내용물 배출이나 월경성 출혈 회복에 도움이 될 수 있습니다.

다만 검색된 문헌은 저용량 mifepristone과 misoprostol 병용 임신 중절, 계류유산 관리 등에 관한 것이며, 무월경 자체를 치료한 연구가 아닙니다. 여기서 무월경은 임신 등 다른 원인의 증상일 뿐이므로 연관성은 간접적입니다. 시상하부, 뇌하수체, 난소, 구조적 원인에 의한 원발성·속발성 무월경에 효과가 있다는 근거도 없습니다. 높은 TxGNN 점수는 임신·자궁 출혈 관련 네트워크 맥락의 영향일 가능성이 크며, 임상 데이터로 뒷받침되지 않습니다.

두 번째 예측 질환인 비전형 대동맥 축착(atypical coarctation of aorta)은 점수 0.9930이나 임상시험과 문헌이 모두 없습니다. PGE1 제제(alprostadil)가 신생아 동맥관 의존성 선천 심질환에서 동맥관 개존에 쓰이므로 계열 수준의 이론적 연관성은 있습니다. 그러나 misoprostol은 경구·점막 투여제이고, 자궁수축 작용과 최기형성 위험(혈관 파괴 결손 포함)이 있어 이 용도로 적합하지 않습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | RCT (코호트로 분류) | Reprod Sci | 무월경 35일 이하 초기 임신 744명에서 저용량 mifepristone + 자가 투여 misoprostol의 초조기 약물 유산 효능·안전성·수용성 평가 |
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | RCT (코호트로 분류) | Reprod Sci | 2,500명을 대상으로 mifepristone 50~150 mg 후 misoprostol 200 µg 투여, 초조기 임신 종결 용량 탐색 |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | 코호트 | Hum Reprod | 예상 월경 전 저용량 mifepristone + misoprostol로 비임신 상태 유지·회복 효능 평가 |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | 코호트 | J Obstet Gynaecol Res | 자가 투여 저용량 mifepristone + misoprostol의 조기 임신 종결 안전성·효능 |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Review | BMJ | 계류유산 및 무배아 임신의 약물 관리 (초록 없음) |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Review | J Obstet Gynaecol Can | 비정상 자궁출혈 관리에서 자궁내막 소작술 (무월경과 직접 관련 낮음) |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Review (증례) | Cureus | 임신성 급성 지방간 증례, 무월경은 임신 증상으로 언급됨 |

위 문헌들은 모두 무월경을 치료 대상으로 평가한 것이 아니라, 임신 관련 상황에서 무월경이 언급된 것입니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199903836 | 알소벤정100마이크로그람(미소프로스톨) | 하늘색 육각형 정제 | 허가증 문서 참조 |
| 199603160 | 알소벤정200마이크로그램(미소프로스톨) | 백색 육각형 정제 | 허가증 문서 참조 |

두 제품 모두 유니메드제약(주)의 단일제이며 유효한 허가 상태입니다.

## 안전성 고려사항

- **약물 상호작용**: 총 100건의 상호작용이 조회되었으며, 주요 항목은 다음과 같습니다.
  - **Major**: Dinoprostone(국소) — 같은 프로스타글란딘 계열로 병용 시 주의가 필요합니다.
  - **Moderate**: 마그네슘 함유 제제(Magnesium oxide, Magaldrate, Magnesium carbonate, Magnesium hydroxide), Quinapril
  - **Minor**: Sodium citrate, Aluminum hydroxide, Calcium carbonate, Sodium bicarbonate, Naproxen
  - 그 외 Goserelin, Cyclosporine, Valsartan, Ramipril, Lorazepam 등은 등급이 불명입니다.
- **지식그래프 기반 금기 관련 질환** (허가 문서가 아닌 TxGNN 지식그래프 기준): 고혈압, 간부전·간질환, 담낭질환, 울혈성 심부전, 염증성 장질환, 천식, 약물 남용·의존, 혈액응고 질환, 뇌졸중·뇌혈관 질환, 심근경색, 관상동맥 혈전증, 혈색소병증, 빈혈, 약물 유발 간손상, 심혈관 질환, 활동성 소화성 궤양, 비감염성 수막염
- 허가사항의 경고 및 금기는 확인되지 않았으므로 허가증 문서를 직접 확인해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
무월경 예측은 임상시험이 없고, 문헌도 임신 중절 맥락에 한정되어 무월경 자체의 치료 효과를 지지하지 않습니다. 높은 TxGNN 점수에도 불구하고 근거 수준은 L4에 그칩니다. 대동맥 축착 예측은 근거가 전혀 없고(L5) 최기형성 위험 때문에 부적합합니다.

**진행하려면 필요한 것:**
- 한국 허가증 문서(199903836, 199603160)에서 허가 적응증, 경고, 금기 확보
- 상세한 작용 기전(MOA) 데이터 (DrugBank 조회)
- 비임신성 원인(시상하부·뇌하수체·난소·구조적)의 무월경에서 misoprostol 효과를 평가한 임상 또는 전임상 연구
- 임신 가능 연령 여성에 대한 자궁수축·최기형성 위험 평가와 안전성 관리 계획
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

