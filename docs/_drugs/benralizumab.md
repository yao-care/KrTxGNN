---
layout: default
title: Benralizumab
parent: 僅模型預測 (L5)
nav_order: 131
evidence_level: L5
indication_count: 5
---

# Benralizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Benralizumab: 중증 호산구성 천식에서 피부염으로

---

## 한 문장 요약

Benralizumab은 IL-5Rα를 표적으로 하는 인간화 단클론항체로, 원래 중증 호산구성 천식 치료에 국제 허가를 받았으나 한국에서는 현재 미시판 상태입니다.
TxGNN 모델은 **피부염(Dermatitis)**을 근거 기반 우선 예측 적응증으로 제시하며,
**4건의 임상시험**과 **19편의 문헌**이 이 방향을 탐색하였으나, Phase 2 RCT에서 아토피 피부염 전체 집단 대상 효과는 확인되지 않아 세부 아형 선택이 핵심 과제입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 중증 호산구성 천식 (국제 승인; 한국 허가 정보 없음) |
| 예측 신규 적응증 | 피부염 (Dermatitis) |
| TxGNN 예측 점수 | 99.16% |
| 근거 수준 | L2 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold (아토피 피부염) / Research Question (DRESS 아형) |

> **참고**: TxGNN 1순위 예측은 면역성 혈소판감소증(Thrombocytopenia due to immune destruction, 99.34%)이나, 임상시험·문헌 근거가 전무(L5, Hold)합니다. 본 보고서는 근거가 가장 풍부한 피부염(2순위)을 중심으로 서술합니다. 1순위 예측에 대한 기전 분석은 "결론 및 다음 단계" 섹션을 참조하세요.

---

## 이 예측이 타당한 이유는?

Benralizumab은 IL-5Rα(인터류킨-5 수용체 알파)에 결합하는 인간화 단클론항체입니다. NK 세포를 통한 ADCC(항체 의존성 세포 매개 세포독성) 기전으로 호산구(Eosinophil) 및 호염기구(Basophil)를 혈중과 조직에서 거의 완전히 고갈시킵니다. 작용 기전 상세 데이터는 현재 데이터 갭(DG002)으로, DrugBank API 조회를 통한 보완이 권장됩니다.

아토피 피부염(Atopic Dermatitis, AD)은 Th2 면역 반응이 주도하는 만성 염증성 피부 질환으로, 조직 내 호산구 증가 및 심한 가려움증이 주요 특징입니다. Benralizumab이 AD 피부 병변 내 IL-5Rα 발현 세포를 효과적으로 고갈시킨다는 점은 기전적으로 타당하며(PMID 40781582 확인), 이는 Phase 1/2 탐색 연구의 이론적 근거가 되었습니다.

**그러나 핵심 임상 시그널은 부정적입니다.** AD의 핵심 구동 축은 IL-4/IL-13(Dupilumab의 표적)이며, 호산구는 이 경로의 하류 효과 세포에 불과합니다. HILLIER Phase 2 RCT(NCT04605094, n=194)는 조기 종료되며 중등-중증 AD에서 유의미한 임상 효과가 없음을 확인했습니다(PMID 37178404, 38695680). 반면, **DRESS(Drug Reaction with Eosinophilia and Systemic Symptoms, 약물 반응 동반 호산구 증가 및 전신 증상)**는 호산구가 직접 병리 역할을 하는 아형으로, 기전 적합도가 현저히 높습니다. 해당 아형을 대상으로 한 별도 Phase 2 연구(NCT06734884)가 계획되어 있습니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04605094](https://clinicaltrials.gov/study/NCT04605094) | Phase 2 | 조기 종료 | 194 | 중등-중증 AD에서 Benralizumab vs. 위약 16주 비교 — **핵심 부정적 결과**: 유의미한 증상 개선 없음 (PMID 37178404, 38695680) |
| [NCT06734884](https://clinicaltrials.gov/study/NCT06734884) | Phase 2 | 모집 예정 | 96 | DRESS 환자에서 Benralizumab 효능·안전성 평가 (2025.01 시작, 2029.09 완료 예정) — 호산구 구동 아형으로 기전 적합도 높음 |
| [NCT03563066](https://clinicaltrials.gov/study/NCT03563066) | Phase 2 | 완료 | 20 | AD에서 호산구·호염기구·ILC2에 대한 기전 탐색 연구 (2018~2021) — 피부 내 IL-5Rα 발현 세포 고갈 확인, HILLIER 대형 시험의 전임상 근거 제공 |
| [NCT04126499](https://clinicaltrials.gov/study/NCT04126499) | N/A | 완료 | 28 | 스페인 개별 접근 프로그램 내 중증 호산구성 천식 환자 Benralizumab 후향 관찰 — 실세계 안전성 참고 데이터 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [37178404](https://pubmed.ncbi.nlm.nih.gov/37178404/) | 2023 | Phase 2 RCT (1차 결과) | JEADV | **핵심**: HILLIER 시험 — 중등-중증 AD에서 Benralizumab 무효 확인, 조기 종료 |
| [38695680](https://pubmed.ncbi.nlm.nih.gov/38695680/) | 2024 | Phase 2 RCT (전문) | Immunotherapy | HILLIER 시험 평이 언어 전문 요약 — 동일 부정적 결과 재확인 |
| [40781582](https://pubmed.ncbi.nlm.nih.gov/40781582/) | 2025 | 기전/중개 연구 | Clin Transl Allergy | AD 피부 병변에서 IL-5Rα 발현 세포 고갈 확인 — 생물학적 효과 증명, 그러나 임상 개선 미동반 |
| [39234416](https://pubmed.ncbi.nlm.nih.gov/39234416/) | 2024 | 기전 연구 | J Allergy Clin Immunol Global | AD 환자 피내 알레르겐 유발 모델에서 Benralizumab의 피부 염증 억제 효과 평가 |
| [36270814](https://pubmed.ncbi.nlm.nih.gov/36270814/) | 2023 | 이상반응 증례 | Therapie | Benralizumab 유발 간질성 육아종성 피부염 증례 보고 — 피부과 역설적 이상반응 신호 |
| [38035014](https://pubmed.ncbi.nlm.nih.gov/38035014/) | 2023 | 약물 감시 | Front Pharmacol | FAERS 기반 항제2형 면역 단클론항체(Benralizumab 포함)의 기생충 감염 안전 신호 분석 |
| [37201737](https://pubmed.ncbi.nlm.nih.gov/37201737/) | 2023 | 검토 | Pharmacol Ther | 알레르기 질환에서 IL-5/IL-5R 길항제 및 병리적 Th2 세포 표적 치료제 총론 |
| [36355314](https://pubmed.ncbi.nlm.nih.gov/36355314/) | 2023 | 검토 | Dermatol Ther | AD 동반 질환 관리를 위한 Dupilumab과 타 단클론항체(Benralizumab 포함) 병용 안전성 |
| [36411004](https://pubmed.ncbi.nlm.nih.gov/36411004/) | 2023 | 안전성 검토 | Immunol Allergy Clin North Am | 임신·수유 중 biologics(Benralizumab 포함) 7종 사용 안전성 — 적응증 확장 시 특수 집단 고려 필요 |
| [35987486](https://pubmed.ncbi.nlm.nih.gov/35987486/) | 2022 | 안전성 검토 | J Allergy Clin Immunol Pract | FDA 승인 아토피 질환 biologics 7종의 임신 중 모체·태아 결과 체계적 검토 |

---

## 한국 시판 정보

현재 Benralizumab의 한국 MFDS 허가 이력이 확인되지 않습니다 (허가증 0건, 시판 현황: 미시판).

> Benralizumab(상품명 **Fasenra®**)은 미국 FDA(2017년), 유럽 EMA(2018년), 일본 PMDA 등에서 **중증 호산구성 천식** 적응증으로 승인되어 있습니다. 한국 MFDS 공식 허가 여부는 MFDS 의약품통합정보시스템(nedrug.mfds.go.kr)을 통한 별도 확인이 필요합니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

문헌에서 확인된 주요 안전 신호:
- **기생충 감염 위험**: FAERS 데이터 분석(PMID 38035014)에서 Benralizumab 사용 시 helminth(기생충) 감염 안전 신호 확인. 기생충 감염 위험 지역 환자에서 투여 전 스크리닝 고려 필요
- **약물 유발 피부 반응**: 간질성 육아종성 피부염 증례 보고(PMID 36270814) — 피부과 재창출 연구 설계 시 역설적 피부 이상반응 모니터링 항목으로 포함 필요

---

## 결론 및 다음 단계

**결정: Hold (아토피 피부염) / Research Question (DRESS 아형)**

**사유:**
아토피 피부염에 대해서는 Phase 2 RCT(HILLIER, n=194)가 조기 종료되며 임상적 효과가 없음이 확인된 상태입니다. IL-5/호산구 축이 AD 전체 집단의 핵심 구동 기전이 아님이 임상적으로 결론났습니다. 그러나 호산구가 직접 병리 역할을 하는 **DRESS 아형**은 기전 적합도가 높고 미충족 의료 수요가 존재하여, NCT06734884 시험 결과를 지켜볼 탐색 가치가 있습니다.

**TxGNN 1순위 예측(면역성 혈소판감소증) 요약:** ITP의 주요 병리는 IgG 자가항체 및 T세포 매개 면역 이상이며, IL-5/호산구 축은 핵심 구동 기전이 아닙니다. 임상시험·문헌 근거가 전무(L5)하여 현 단계에서는 Hold를 권장합니다.

**진행하려면 필요한 것:**
- MFDS 의약품통합정보시스템에서 Benralizumab(Fasenra®) 한국 허가 현황 공식 확인 및 허가사항 경고·금기 데이터 확보 (DG001 해소)
- DrugBank API를 통한 작용 기전(MOA) 상세 데이터 보완 (DG002 해소)
- NCT06734884(DRESS 대상 Phase 2) 진행 상황 모니터링 — 2025년 시작 예정, 1차 결과 시 즉시 재평가
- DRESS 아형 환자에서 호산구 감소 대리 지표와 임상 결과 간 상관관계 데이터 수집
- 한국 환자 집단 내 기생충 감염 위험도를 고려한 환자 선별 기준 및 안전성 모니터링 계획 수립
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

