---
layout: default
title: Ranibizumab
parent: 僅模型預測 (L5)
nav_order: 591
evidence_level: L5
indication_count: 10
---

# Ranibizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Ranibizumab: 당뇨병성 황반부종에서 중증 비증식성 당뇨병성 망막병증으로

## 한 문장 요약

Ranibizumab은 항혈관내피성장인자(VEGF) 억제제로, 당뇨병성 황반부종(DME) 등 안과 신생혈관 질환 치료에 사용되어 온 생물학적 제제입니다.
TxGNN 모델은 **중증 비증식성 당뇨병성 망막병증(Severe Nonproliferative Diabetic Retinopathy)**에도 효과가 있을 것으로 예측하며,
현재 **6건의 임상시험**과 **19편의 문헌**이 이 방향을 지지합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 당뇨병성 황반부종(DME) 등 안과 신생혈관 질환 (국내 허가 정보 없음) |
| 예측 신규 적응증 | 중증 비증식성 당뇨병성 망막병증 (Severe Nonproliferative Diabetic Retinopathy) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L1 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 확보되지 않았습니다(DrugBank 조회 필요). 다만 근거 자료에 포함된 임상적 맥락에서 확인되는 바에 따르면, Ranibizumab은 VEGF(혈관내피성장인자)를 표적으로 하는 항체 단편(anti-VEGF) 제제이며, 당뇨병성 황반부종(DME) 치료의 근간이 되는 RIDE/RISE, DRCR Protocol I 등 대규모 임상시험을 통해 이미 효능이 입증되어 있습니다.

VEGF는 당뇨병성 망막병증(DR)이 비증식기에서 증식기로 진행하는 핵심 동인으로, VEGF를 억제하면 미세혈관 누출과 신생혈관 형성을 억제할 수 있습니다. 즉 기존 적응증(DME)과 예측 신규 적응증(중증 NPDR)은 동일한 질환 스펙트럼의 서로 다른 진행 단계로, 기전상 동일한 약리학적 근거를 공유합니다.

실제로 Port Delivery System(PDS)을 이용한 Ranibizumab의 Phase 3 시험(NCT04503551, Pavilion 연구)이 황반부종이 없는 중증 NPDR 환자를 대상으로 진행 중이며, 이는 TxGNN 예측의 타당성을 뒷받침합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04503551](https://clinicaltrials.gov/study/NCT04503551) | Phase 3 | 진행 중(모집 종료) | 174 | 황반부종 없는 DR 환자에서 Port Delivery System(PDS)과 대조군 비교, 완료 예정 2026-03 |
| [NCT00444600](https://clinicaltrials.gov/study/NCT00444600) | Phase 3 | 완료 | 691 | 레이저 단독 vs 트리암시놀론+레이저 vs Ranibizumab+레이저 vs Ranibizumab 단독 비교(DME) |
| [NCT02634333](https://clinicaltrials.gov/study/NCT02634333) | Phase 3 | 완료 | 399 | 고위험 DR에서 항-VEGF 치료로 시력 위협 합병증 예방 효과 확인 |
| [NCT03452657](https://clinicaltrials.gov/study/NCT03452657) | Phase 3 | 불명(업데이트 중단) | 118 | 고위험 DR 예방 목적 Ranibizumab vs 위약주사 비교 |
| [NCT02834663](https://clinicaltrials.gov/study/NCT02834663) | Phase 4 | 완료 | 25 | 단일기관 소규모 연구, NPDR+DME에서 미세동맥류 및 무관류 망막 면적 변화 관찰 |
| [NCT05222633](https://clinicaltrials.gov/study/NCT05222633) | N/A | 불명 | 1000 | 실제 임상현장에서 항-VEGF 치료의 시력·해부학적 효과 관찰(주로 습성 AMD 대상) |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | RCT | JAMA Ophthalmology | Pavilion 연구: 황반부종 없는 NPDR에서 PDS-Ranibizumab vs 관찰군 비교 |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | Cohort(RIDE/RISE 사후분석) | Clin Ophthalmol | RIDE/RISE 시험에서 조기 DR 개선 예측인자 분석 |
| [33966556](https://pubmed.ncbi.nlm.nih.gov/33966556/) | 2021 | Review | Expert Opin Biol Ther | Ranibizumab의 DR 치료 효능에 대한 종합 리뷰 |
| [36774994](https://pubmed.ncbi.nlm.nih.gov/36774994/) | 2023 | Cohort(메타분석) | Ophthalmology Retina | 기저 DR 중증도와 DME 소실 시간의 관계(Phase 3 데이터 메타분석) |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2024 | Review(체계적 문헌고찰) | Health Technol Assess | 항-VEGF vs 레이저 광응고술의 DR 치료 효과 비교 |
| [35417296](https://pubmed.ncbi.nlm.nih.gov/35417296/) | 2022 | Cohort | Ophthalmic Surg Lasers Imaging Retina | RIDE/RISE 미치료 반대안(fellow eye)의 DR 자연 경과 분석 |
| [40347224](https://pubmed.ncbi.nlm.nih.gov/40347224/) | 2025 | Review(체계적 문헌고찰+경제성 분석) | Health Technol Assess | 항-VEGF vs 레이저 광응고술 DR 치료의 비용효과 분석 |
| [30234859](https://pubmed.ncbi.nlm.nih.gov/30234859/) | 2018 | 관찰 연구 | Retina | DRCR Protocol I 5년 추적: Ranibizumab 치료 시 DR 중증도 변화 |
| [28448655](https://pubmed.ncbi.nlm.nih.gov/28448655/) | 2017 | RCT 사후분석 | JAMA Ophthalmology | Aflibercept/Bevacizumab/Ranibizumab 비교 시 2년간 DR 변화 분석 |
| [20964459](https://pubmed.ncbi.nlm.nih.gov/20964459/) | 2010 | Review | Drugs | DR 및 DME 관리에 대한 현재 접근법 종합 리뷰 |

## 안전성 고려사항

안전성 정보(경고, 금기, 약물상호작용)가 아직 확보되지 않았습니다. 국내 미출시 상태로 관련 허가사항이 없으며, 규제기관(TFDA/식약처) 원문 라벨 확보가 필요합니다.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
DME에 대한 Ranibizumab의 효능을 입증한 다수의 완료된 Phase 3 RCT(NCT00444600, NCT02634333)와, 중증 NPDR을 직접 표적으로 한 진행 중인 Phase 3 시험(NCT04503551, Pavilion)이 존재하여 근거 수준 L1에 해당합니다. VEGF가 DR 진행의 핵심 기전이라는 점도 강력한 생물학적 타당성을 제공합니다. 다만 국내 미출시 상태이며 안전성/허가 정보가 부재하여 즉시 진행(Go) 판정은 유보합니다.

**진행하려면 필요한 것:**
- 국내(한국) 허가 현황 확보 — 현재 미출시, 허가증 0건
- TFDA/식약처 원문 허가사항(경고·금기·상호작용) 확보 — Blocking 등급 데이터 갭
- DrugBank API를 통한 상세 작용기전(MOA) 데이터 보완
- NCT04503551(Pavilion Phase 3, 완료 예정 2026-03) 최종 결과 확인
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

