---
layout: default
title: Finasteride
parent: 중등도 근거 (L3-L4)
nav_order: 324
evidence_level: L4
indication_count: 6
---

# Finasteride
{: .fs-9 }

근거 수준: **L4** | 예측 적응증: **6** 건
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

# Finasteride: 원 적응증 정보 미비에서 다모증(Hypertrichosis)으로

## 한 문장 요약

Finasteride는 본 Evidence Pack 내에 원 적응증·작용기전(MOA) 데이터가 등록되어 있지 않으며(High severity Data Gap), 국내에는 허가된 제품이 없습니다(미시판). TxGNN 모델은 6개 후보 적응증을 제시했으나 대부분 기전적 근거와 실증 자료가 전혀 없는 낮은 신뢰도(L5)의 노이즈성 예측으로 평가되며, 그중 유일하게 실제 임상시험 1건과 문헌 4편이 확인된 **다모증(Hypertrichosis)**만이 L4 수준의 최소한의 근거를 갖추고 있습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (원 적응증·MOA 모두 Data Gap, High severity) |
| 예측 신규 적응증 | 다모증 (Hypertrichosis, disease) |
| TxGNN 예측 점수 | 99.99% (rank 355) |
| 근거 수준 | L4 |
| 한국 시판 현황 | 미시판 (허가증 0건) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다(원 적응증·MOA 모두 [Data Gap], DG002·High severity). 다만 Evidence Pack에 포함된 후보별 기전 논증(repurposing_rationale) 텍스트에는 finasteride가 5α-reductase를 억제하여 테스토스테론의 DHT 전환을 감소시키는 항안드로겐 기전을 가진다는 점이 공통적으로 언급되어 있으며, 이는 안드로겐 의존성 모발 성장을 "억제"하는 방향(예: 남성형 탈모 치료)에 가깝습니다.

**후보 스크리닝 참고**: TxGNN이 가장 높은 점수(99.99%, rank 307)로 제시한 1순위 후보 "Ambras type hypertrichosis universalis congenita"는 염색체 재배열 등 비안드로겐성 유전 질환으로, finasteride 기전과 병태생리학적 연결고리가 없고 임상시험·문헌이 전혀 없어(L5) 지식그래프 이웃 노드로 인한 통계적 노이즈로 판단됩니다. 3~6순위 후보(치주질환 관련 기형, Dandy-Walker 증후군, 모발간 구조이상, 가족성 속눈썹비대증) 역시 기전적 연결이 없고 직접 증거가 전무합니다. 이에 실제 임상시험·문헌이 확인되는 2순위 후보 **다모증(Hypertrichosis)**을 이 보고서의 주 평가 대상으로 선정했습니다.

다모증과 남성형 탈모는 모두 모낭 성장 조절 이상이라는 공통 축을 가지지만, 방향성이 반대(모발 과다 성장 vs 억제)라는 점에서 기전상 직접적 치료 효과보다는 "안드로겐 의존성 모발 이상"이라는 넓은 범주에서의 간접적 연관 가능성에 그칩니다. 현재 문헌은 이 방향성에 대한 직접적 임상 데이터를 제공하지 않습니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04293822](https://clinicaltrials.gov/study/NCT04293822) | Phase 4 | 불명(Unknown) | 60 | 국소 Cetirizine gel vs Minoxidil 5% gel의 남성형 탈모(안드로겐성 탈모) 치료 비교. Finasteride는 시험 약물로 사용되지 않았으며 적응증도 다모증이 아님 — TxGNN 질환 노드 근접성에 의한 간접 연결(관련성 등급 C) |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [10330884](https://pubmed.ncbi.nlm.nih.gov/10330884/) | 1999 | Review | Therapeutische Umschau | 안드로겐성 탈모·다모증·조모증 치료의 새로운 접근법 개관, 경구 치료제(finasteride 계열 포함) 언급 |
| [12223963](https://pubmed.ncbi.nlm.nih.gov/12223963/) | 2002 | Review | Annales de dermatologie et de venereologie | 성인 다모증은 비안드로겐 의존 부위의 모발 증가로, 호르몬 검사가 불필요함을 설명(조모증과 대비); 원인은 약인성·대사성·영양성·부종양성 등 |
| [12942187](https://pubmed.ncbi.nlm.nih.gov/12942187/) | 2003 | Review | Der Hautarzt | 남성형 탈모 치료에서의 finasteride 도입과 다모증·조모증에 대한 레이저 제모 기술 소개 |
| [12444520](https://pubmed.ncbi.nlm.nih.gov/12444520/) | 2002 | Review | Der Hautarzt | 모발 손실/성장 평가를 위한 디지털 분석 도구(TrichoScan) 소개, 치료 반응 모니터링 방법론 |

---

## 한국 시판 정보

국내에 허가된 제품이 없습니다 (미시판, 허가증 0건).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (주요 경고·금기·DDI 모두 조회 결과 없음, TFDA 수준 경고/금기 자료는 Blocking 등급 Data Gap으로 S1 안전성 초평가 진입 불가 상태)

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
다모증 후보는 6개 예측 중 유일하게 최소한의 실증 자료(문헌 4편)를 갖추었으나, 모두 finasteride를 직접 다루지 않는 리뷰 논문이며 관련 임상시험 1건도 관련성 등급 C(간접 연결)에 불과합니다. 기전상 방향성(모발 억제 vs 다모증의 모발 과다)도 상충되어 직접적 근거가 부족합니다.

**진행하려면 필요한 것:**
- 작용기전(MOA) 데이터 확보 (DrugBank API 재조회, High severity Data Gap)
- 국내 허가사항 경고/금기 자료 확보 — TFDA(현지 규제기관) 원문 PDF 파싱 필요 (Blocking Data Gap, S1 안전성 초평가 진입 전제조건)
- Finasteride-다모증 관계에 대한 직접적 전임상/기전 연구
- 나머지 4개 후보(Ambras 다모증, 치주 기형 증후군, Dandy-Walker 증후군, 모발간 구조이상)는 기전적 타당성과 실증 자료가 전무하여 별도 조치 없이 Hold 유지 권장
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

