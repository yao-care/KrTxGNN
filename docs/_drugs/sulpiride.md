---
layout: default
title: Sulpiride
parent: 모델 예측만 (L5)
nav_order: 652
evidence_level: L5
indication_count: 9
---

# Sulpiride
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **9** 건
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

# SULPIRIDE: 정신과·소화기 질환에서 망막 이상형성증으로

## 한 문장 요약

Sulpiride는 선택적 D2/D3 도파민 수용체 길항제로, 정신과(항정신병) 및 소화기과(위장관 운동 촉진·제토)에서 사용되어 온 약물입니다. TxGNN 모델은 **망막 이상형성증(Retinal Dystrophy with or without Extraocular Anomalies)**에 효과가 있을 수 있다고 예측했지만, 관련 임상시험은 전혀 없고 문헌 15편도 약물과 직접적인 연관성이 확인되지 않아 근거 수준이 매우 낮습니다(L5).

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정신과(항정신병)·소화기과(위장관 운동 촉진) — 한국 허가 정보 없음 |
| 예측 신규 적응증 | 망막 이상형성증 (Retinal Dystrophy with or without Extraocular Anomalies) |
| TxGNN 예측 점수 | 99.95% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미상시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 DrugBank의 상세한 작용 기전(MOA) 데이터는 확보되지 않았습니다(High 등급 데이터 갭). 다만 알려진 정보에 따르면 Sulpiride는 선택적 D2/D3 도파민 수용체 길항제 계열 약물로, 정신과에서 항정신병제로, 소화기과에서 위장관 운동 촉진 및 제토 목적으로 사용되어 왔습니다.

그러나 이번 예측 대상인 망막 이상형성증(선천성 망막·안외 이상 질환군)은 발생학적 구조 이상에 기인하는 질환으로, 현재까지 도파민 수용체 길항 기전과의 직접적인 연관성은 보고된 바 없습니다. TxGNN이 제시한 순위 2~9위의 후보 적응증(수두무뇌증, 선천성 대뇌피질 형성이상 증후군, CMT1G, X-연관 근시, 당화이상 질환, 비정형 글라이신 뇌병증 등) 역시 모두 희귀 유전질환으로, 도파민 경로와의 생물학적 연결고리가 확인되지 않았고 실증 근거도 전무합니다. 전체적으로 이번 후보는 지식그래프 임베딩 유사도에 기반한 순수 모델 예측이며, 기전적 타당성은 낮습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

아래는 망막 이상형성증(rank 1) 예측과 연관 검색된 문헌으로, 대부분 안과 일반 질환 리뷰·증례이며 **Sulpiride를 직접 다루는 문헌은 없습니다**.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review/Case | Semin Ultrasound CT MR | 안와 감염(부비동염 속발 봉와직염) 병기 및 임상양상 리뷰 |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Semin Neurol | 복시(diplopia) 진단 접근법 리뷰 |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klin Monatsbl Augenheilkd | 선천성 안검하수의 병태생리 및 검사 리뷰 |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan J Ophthalmol | 수정체 모양 선천성 기형 리뷰 |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case Report | Am J Ophthalmol | 편측성 잠안구증(cryptophthalmia) 증례 |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case Report | J Neuroophthalmol | 선천성 활차-동안신경 연합운동 증례 |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Doc Ophthalmol | Wagner-Stickler 증후군 복합체 리뷰 |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatr Radiol | 소아 안와 병변(안과적 병리) 영상 리뷰 |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Case Report | Optom Vis Sci | 선천성 안외근 섬유증 관련 변이형 산개 증례 |
| [19064847](https://pubmed.ncbi.nlm.nih.gov/19064847/) | 2008 | Review | Arch Ophthalmol | 안와 동정맥 기형 임상 특징 및 치료 리뷰 |

---

## 한국 시판 정보

이 약물은 현재 한국에 등록된 허가 정보가 없습니다(미상시판, 허가증 0건).

---

## 안전성 고려사항

TFDA 수준의 경고·금기 정보 및 약물상호작용 데이터는 현재 확보되지 않았습니다(Blocking 등급 데이터 갭 — 안전성 초기 평가 단계 진입 불가). 안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 근거 수준이 L5(모델 예측만 존재)로, 관련 임상시험이 전혀 없고 문헌 증거도 약물과 직접 연관되지 않습니다.
- 안전성 정보(경고, 금기, DDI)가 전면 결측된 Blocking 데이터 갭이 있어 안전성 초기 평가(S1) 자체가 불가능합니다.
- 한국 내 허가·시판 이력이 없어 규제 경로 확인이 필요합니다.
- 순위 2~9위 후보 적응증도 모두 희귀 유전질환이며 임상·문헌 근거가 전무해 기전적 타당성이 낮습니다.

**진행하려면 필요한 것:**
- TFDA(또는 원산지 규제기관) 공식 첨부문서 확보 및 파싱 (DG001, Blocking)
- DrugBank API를 통한 상세 작용 기전(MOA) 데이터 보완 (DG002, High)
- 망막 이상형성증에 대한 전임상/기전 연구 확보 — 현재 도파민 경로와의 연결고리 부재
- 대체 후보 적응증에 대한 우선순위 재평가 필요 (전체 후보군 근거 수준 일괄 L5)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

