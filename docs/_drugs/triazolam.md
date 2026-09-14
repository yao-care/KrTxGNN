---
layout: default
title: Triazolam
parent: 僅模型預測 (L5)
nav_order: 702
evidence_level: L5
indication_count: 1
---

# Triazolam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Triazolam: 벤조디아제핀계 수면진정제에서 불면증(수면 개시·유지 장애)으로

## 한 문장 요약

Triazolam(DrugBank DB00897)은 벤조디아제핀 계열 진정수면제로 알려져 있으나, 이번 Evidence Pack에는 공식 원 적응증·작용기전(MOA) 데이터가 확보되지 않았습니다.
TxGNN 모델은 **불면증(Sleep disorder, initiating and maintaining sleep)**에 효과가 있을 것으로 예측하며(예측 점수 99.72%),
현재 등록된 임상시험은 없으나 **21편의 문헌**(가이드라인·체계적 문헌고찰·네트워크 메타분석 포함)이 벤조디아제핀 계열 수면제로서의 효능·안전성을 뒷받침합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 자료 없음 (한국 미허가, DrugBank 원 적응증 데이터 결측 — MOA도 High 등급 Data Gap) |
| 예측 신규 적응증 | 불면증 — 수면 개시 및 유지 장애 (Sleep disorder, initiating and maintaining sleep) |
| TxGNN 예측 점수 | 99.72% |
| 근거 수준 | L3 (완료된 임상시험 없음, 체계적 문헌고찰·네트워크 메타분석 등 관찰/종합근거 존재) |
| 한국 시판 현황 | ✗ 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용기전(MOA) 데이터는 확보되지 않았습니다(Blocking/High 등급 Data Gap). 다만 문헌 근거에서 반복적으로 확인되듯, Triazolam은 짧은 반감기를 가진 벤조디아제핀 계열 수면제(hypnotic)로, GABA-A 수용체의 벤조디아제핀 결합 부위에 작용하는 것으로 널리 알려져 있는 약물군에 속합니다(예: PMID 1319429, PMID 19682231).

TxGNN이 예측한 신규 적응증인 "불면증(수면 개시·유지 장애)"은 이 약물군의 전형적인 임상 활용 영역과 직접적으로 일치합니다. 실제로 수집된 21편의 문헌 대부분이 불면증 약물치료 가이드라인 및 벤조디아제핀 계열 약물(특히 triazolam)의 효능·안전성을 다루고 있어, 예측의 기전적 타당성을 뒷받침합니다. 다만 이는 "신규" 적응증이라기보다 이미 잘 알려진 약물 분류의 전형적 용도에 가까우므로, 한국 내 정식 허가 여부와는 별개로 해석할 필요가 있습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [9161660](https://pubmed.ncbi.nlm.nih.gov/9161660/) | 1997 | Review | The Annals of Pharmacotherapy | Zolpidem과 Triazolam의 효능·안전성 비교 문헌고찰 |
| [1319429](https://pubmed.ncbi.nlm.nih.gov/1319429/) | 1992 | Review | J Clin Psychiatry | Triazolam·Temazepam 등 벤조디아제핀 수면제의 약리학적 특성 정리 |
| [19682231](https://pubmed.ncbi.nlm.nih.gov/19682231/) | 2010 | Original study | J Sleep Research | Triazolam·Zolpidem이 수면 의존적 운동학습에 미치는 역행성 효과 연구 |
| [2567741](https://pubmed.ncbi.nlm.nih.gov/2567741/) | 1989 | Review | J Clin Psychopharmacology | Triazolam 등 단기작용 벤조디아제핀 중단 시 반동성 불면증(rebound insomnia) 비평 |
| [33249496](https://pubmed.ncbi.nlm.nih.gov/33249496/) | 2021 | Network meta-analysis | Sleep | 고령자 불면증 치료제(수면진정제 포함)의 효능·안전성 비교 네트워크 메타분석 |
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | Clinical guideline | J Clin Sleep Medicine | AASM 성인 만성 불면증 약물치료 임상진료지침 |
| [40110890](https://pubmed.ncbi.nlm.nih.gov/40110890/) | 2025 | Systematic review/meta-analysis of RCTs | Psychiatry Clin Neurosci | 불면 동반 주요우울장애에서 수면제 병용요법의 효능·안전성 메타분석 |
| [30058034](https://pubmed.ncbi.nlm.nih.gov/30058034/) | 2018 | Review | Drugs & Aging | 고령 불면증 환자 약물치료 권고사항 |
| [27751669](https://pubmed.ncbi.nlm.nih.gov/27751669/) | 2016 | Review | Clinical Therapeutics | 고령자 대상 수면제의 안전성·효능 문헌고찰 |
| [39932761](https://pubmed.ncbi.nlm.nih.gov/39932761/) | 2025 | Review | Minerva Medica | 불면증 장애의 정의·역학·치료 개관 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
안전성 관련 핵심 자료(주요 경고, 금기, DDI)가 전부 결측 상태이며, 특히 허가사항/경고 정보 결측(DG001)은 Blocking 등급으로 S1 안전성 초기평가 자체가 불가능합니다. 또한 한국 내 허가증이 0건으로, 이는 기존 허가 약물의 적응증 확장이 아니라 신규 허가 절차가 필요한 상황이라 리스크 프로파일이 다릅니다.

**진행하려면 필요한 것:**
- 한국 식약처(MFDS) 허가사항·경고·금기 정보 확보 (DG001 해결, Blocking)
- DrugBank 등에서 작용기전(MOA) 데이터 확보 (DG002 해결)
- DDI(약물상호작용) 데이터베이스 재조회
- 한국 내 임상시험 등록 현황 및 벤조디아제핀 계열 약물 규제 동향 조사
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

