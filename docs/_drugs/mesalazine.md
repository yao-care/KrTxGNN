---
layout: default
title: Mesalazine
parent: 僅模型預測 (L5)
nav_order: 469
evidence_level: L5
indication_count: 7
---

# Mesalazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Mesalazine: 궤양성대장염에서 골관절염으로

## 한 문장 요약

Mesalazine(5-ASA)은 궤양성대장염 등 염증성 장질환에 쓰이는 항염증제입니다.
TxGNN 모델은 **골관절염(Osteoarthritis)**에도 효과가 있을 수 있다고 예측하며,
현재 임상시험 등록은 없지만 **Nature Communications 게재 전임상 기전 연구를 포함한 3편의 문헌**이 이 방향의 생물학적 타당성을 뒷받침합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (한국 미출시, DrugBank 원 적응증 데이터 없음 — 문헌상 통상 용도는 궤양성대장염) |
| 예측 신규 적응증 | 골관절염 (Osteoarthritis) |
| TxGNN 예측 점수 | 99.63% |
| 근거 수준 | L4 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용기전(MOA) 데이터는 확보되지 않았습니다(DrugBank 조회 결과 Data Gap). 다만 문헌에 따르면 mesalazine(5-ASA)은 궤양성대장염 치료에 쓰이는 항염증제로 알려져 있습니다.

주목할 점은, 최근 연구(PMID 38310093, *Nature Communications*, 2024)가 5-ASA 자체(대사물인 sulfapyridine이 아니라)가 연골세포의 OSCAR 수용체에 결합해 PPARγ 경로를 활성화함으로써 파골세포 유사 분화와 연골 파괴를 억제한다는 새로운 기전을 직접 규명했다는 것입니다. 이는 TxGNN이 지식그래프상의 유사성만으로 예측한 것이 아니라, 실제 분자 수준의 기전 증거가 뒷받침된다는 의미입니다.

추가로 1991년 in vitro 연구(PMID 1673814)는 활막 조직에서 5-ASA가 프로스타글란딘·류코트리엔 분비를 억제함을 보여, 관절 염증 억제 가능성에 대한 오래된 방증도 존재합니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [38310093](https://pubmed.ncbi.nlm.nih.gov/38310093/) | 2024 | 전임상 기전 연구 | Nature Communications | 5-ASA가 OSCAR-PPARγ 축을 통해 연골 파괴 및 골관절염 진행을 억제함을 규명 |
| [38491514](https://pubmed.ncbi.nlm.nih.gov/38491514/) | 2024 | 생물정보학/전산 표적 발굴 | Journal of Translational Medicine | 이종 발현 데이터와 약물-표적 상호작용을 결합해 OA 치료 표적 후보를 발굴 |
| [1673814](https://pubmed.ncbi.nlm.nih.gov/1673814/) | 1991 | 시험관내(인체 조직) 연구 | Wiener klinische Wochenschrift | 인체 활막 조직에서 5-ASA 등이 프로스타글란딘·류코트리엔 분비를 억제함을 확인 |

---

## 한국 시판 정보

현재 한국 내 허가 정보가 없습니다 (미출시).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.
※ 참고: TFDA 등 공식 규제기관의 경고·금기 정보 및 DDI 자료가 확보되지 않아, 안전성 초기 평가(S1) 진행이 현재 차단된 상태입니다.

---

## 참고: 검토했으나 제외한 후보

TxGNN 예측 점수 1위였던 "congenital hypotrichosis with juvenile macular dystrophy"는 CDH3 유전자 돌연변이에 의한 유전질환으로, 근거 팩 자체가 "지식그래프 잡음(기전 비연관)"으로 판정하여 제외했습니다. 류마티스 관절염(3위, L3)도 검토했으나, 기존 문헌들이 sulfasalazine의 RA 효능이 5-ASA가 아닌 대사물 sulfapyridine에서 기인할 가능성을 제기하고 있어(PMID 2860942 등) 약물 귀속이 불명확해 골관절염보다 근거 신뢰도가 낮다고 판단했습니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
근거 수준이 L4(전임상·시험관 연구)에 그치고 실제 임상시험이 전무하며, 약물이 한국에 미출시 상태입니다. 또한 규제기관 경고/금기 정보 확보 실패(Blocking 등급 Data Gap)로 안전성 초기 평가(S1)조차 진행할 수 없습니다.

**진행하려면 필요한 것:**
- TFDA/한국 식약처 공식 첨부문서에서 경고·금기 정보 확보 (Blocking, 최우선)
- DrugBank 등에서 정식 MOA 데이터 확보
- 5-ASA의 OA 동물모델 in vivo 효능 데이터 축적 및 향후 임상시험 등록 모니터링
- 한국 내 mesalazine 제품 허가·유통 현황 재확인
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

