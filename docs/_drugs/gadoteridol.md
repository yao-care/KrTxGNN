---
layout: default
title: Gadoteridol
parent: 모델 예측만 (L5)
nav_order: 341
evidence_level: L5
indication_count: 10
---

# Gadoteridol
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

# Gadoteridol: MRI 조영제에서 골관절염 감수성(Osteoarthritis Susceptibility)으로

## 한 문장 요약

Gadoteridol은 치료제가 아닌 **MRI 조영제**(마크로사이클릭 비이온성 gadolinium 화합물)로, 현재 한국에는 허가된 제품이 없습니다. TxGNN 모델은 **골관절염 감수성(Osteoarthritis Susceptibility)**에 연관성이 있다고 예측했으나, 이 예측을 뒷받침하는 임상시험이나 문헌은 **0건**이며, 근거 수준도 최하위(L5)입니다. 관련 상위 예측들(골관절염, 류마티스 관절염 등)의 문헌도 대부분 "조영제를 이용한 영상 진단" 연구일 뿐, 치료적 개입 근거가 아닙니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 — Gadoteridol은 치료 적응증이 아닌 **MRI 조영제**로 사용됨 (근거팩 내 명시) |
| 예측 신규 적응증 | 골관절염 감수성 (Osteoarthritis Susceptibility) |
| TxGNN 예측 점수 | 98.90% |
| 근거 수준 | L5 (모델 예측만 있음, 실제 연구 없음) |
| 한국 시판 현황 | 미출시 (허가 제품 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

작용 기전(MOA) 데이터는 확보되지 않았습니다(Data Gap). 다만 근거팩에 포함된 분석에 따르면, Gadoteridol은 **진단용 MRI 조영제**이며 치료적 약리 기전 자체가 없는 물질입니다.

1순위 예측인 "골관절염 감수성"에는 지지하는 임상시험이나 문헌이 전혀 없으며, 이는 TxGNN 지식그래프상의 순수 통계적 연관 점수에 불과합니다.

2~3순위인 골관절염·류마티스 관절염 예측에는 문헌이 다수 존재하지만, 내용을 보면 모두 **"조영제를 이용해 관절 연골·활막염을 영상으로 평가"**하는 진단/방법론 연구입니다(예: dGEMRIC, 이중조영 CT, LGE-MRI). 즉 TxGNN이 포착한 높은 점수는 "이 약물이 해당 질환의 치료에 효과적"이라서가 아니라, **"이 약물이 해당 질환을 진단하는 논문에 자주 등장한다"**는 공출현(co-occurrence) 패턴을 학습한 결과로 판단됩니다. 심부전(rank 8) 예측도 동일하게 LGE 심장 MRI 예후 평가 문헌에서 비롯된 것으로, 치료적 연관성을 뒷받침하지 않습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

`predicted_indications[0]` (골관절염 감수성)에 대한 직접 문헌은 없습니다.

참고로 근접 예측인 "골관절염"(rank 2)에는 12편의 문헌이 있으나, 아래와 같이 전부 **영상 진단/방법론 연구**이며 치료 효능 연구가 아닙니다:

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [32525582](https://pubmed.ncbi.nlm.nih.gov/32525582/) | 2020 | Method/Imaging | J Orthop Res | 이중 에너지 CT로 연골 내 조영제(gadoteridol 등) 분포 정량 |
| [37593815](https://pubmed.ncbi.nlm.nih.gov/37593815/) | 2024 | Method/Imaging | J Orthop Res | 삼중 조영 CT로 무릎 관절 연골 생체역학 평가 |
| [39622931](https://pubmed.ncbi.nlm.nih.gov/39622931/) | 2024 | Method/Imaging | Sci Rep | 광자계수 CT 이중조영 기법으로 연골 생체역학 정량 |
| [33692379](https://pubmed.ncbi.nlm.nih.gov/33692379/) | 2021 | Method/Imaging | Sci Rep | 광자계수 CT로 관절 연골 상태 평가 |
| [30816584](https://pubmed.ncbi.nlm.nih.gov/30816584/) | 2019 | Cadaveric/Imaging | J Orthop Res | 전신 CT 이중조영 기법으로 연골 프로테오글리칸/수분 함량 영상화 |
| [31576504](https://pubmed.ncbi.nlm.nih.gov/31576504/) | 2020 | Method/Imaging | Ann Biomed Eng | 삼중 조영 CT로 연골 조성 및 분할 동시 평가 |
| [31535728](https://pubmed.ncbi.nlm.nih.gov/31535728/) | 2020 | Ex vivo/Imaging | J Orthop Res | 싱크로트론 마이크로CT로 이중조영 기법 검증 |
| [32767676](https://pubmed.ncbi.nlm.nih.gov/32767676/) | 2021 | In vitro/Diffusion | J Orthop Res | 연골 구성성분이 양이온/비이온 조영제 확산에 미치는 영향 |
| [31068614](https://pubmed.ncbi.nlm.nih.gov/31068614/) | 2019 | In vitro/Analytical | Sci Rep | 싱크로트론 마이크로CT로 조영제 정량 |
| [27161058](https://pubmed.ncbi.nlm.nih.gov/27161058/) | 2016 | Cohort/Imaging | Eur J Radiol | 조영증강 MRI 활막염과 무릎 골관절염 통증의 연관성 |
| [21305156](https://pubmed.ncbi.nlm.nih.gov/21305156/) | 2009 | pending | Metallomics | 조영제 사용 후 뼈 조직 내 gadolinium 축적 관찰 |
| [16271300](https://pubmed.ncbi.nlm.nih.gov/16271300/) | 2006 | pending | Osteoarthritis Cartilage | gadolinium 프로브와 마이크로CT로 연골 프로테오글리칸 영상화 |

> 위 문헌들은 참고용으로 제시하며, 골관절염 **치료** 근거로는 사용할 수 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (주요 경고·금기·상호작용 데이터 미확보, MFDS 라벨 확인 필요 — Blocking 등급 데이터 갭)

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 1순위 예측(골관절염 감수성)은 임상시험·문헌 근거가 전무하며 순수 그래프 통계 점수(L5)에 불과합니다.
- Gadoteridol은 진단용 MRI 조영제로, 치료적 작용 기전이 없어 "재창출" 프레임 자체가 적용되기 어려운 후보입니다.
- 근접 예측들의 문헌은 모두 영상 진단/방법론 연구이며, TxGNN이 "질환-조영제 공출현"을 "치료 연관성"으로 오인했을 가능성이 높습니다.

**진행하려면 필요한 것:**
- MFDS(식약처) 허가사항 및 경고·금기 정보 확보 (현재 Blocking 데이터 갭)
- DrugBank 기반 정확한 MOA 데이터 확보
- 이 후보는 "치료제 재창출"이 아닌 "진단 영상 활용 확대" 관점으로 재분류할지 여부를 우선 결정 필요
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

