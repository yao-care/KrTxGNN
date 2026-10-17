---
layout: default
title: Clonidine
parent: 모델 예측만 (L5)
nav_order: 229
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Clonidine: 예측 신규 적응증 ADHD, 부주의형 (attention deficit hyperactivity disorder… (근거 수준 L5). 기존 적응증: 허가사항 원문 링크만 제공되어 확인 불가 (허가사항 참조 필요)"
monitor_inn: "Clonidine"
predicted_indications: ["faciodigitogenital syndrome", "chondromyxoid fibroma", "trichotillomania", "Tourette syndrome", "obesity disorder", "hypervitaminosis", "proximal 16p11.2 microdeletion syndrome"]
---

# Clonidine
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

# Clonidine: 고혈압에서 주의력결핍 과잉행동장애(ADHD)로

## 한 문장 요약

Clonidine은 알파-2 아드레날린 작용제로, 한국에서는 서방정 제품(켑베이서방정)으로 허가되어 시판 중입니다.
TxGNN 모델은 **주의력결핍 과잉행동장애(ADHD)**에 효과가 있을 수 있다고 예측하며, 현재 **9건의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다.

> 참고: 허가증에 기재된 기존 적응증은 텍스트가 아닌 링크 형태로만 제공되어 구체적인 적응증 내용은 확인되지 않았습니다. 제목의 "고혈압"은 clonidine의 일반적인 약리 분류에 근거한 것이며, 허가 적응증은 허가사항으로 확인이 필요합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가사항 원문 링크만 제공되어 확인 불가 (허가사항 참조 필요) |
| 예측 신규 적응증 | ADHD, 부주의형 (attention deficit hyperactivity disorder, inattentive type) |
| TxGNN 예측 점수 | 99.9997% |
| 근거 수준 | 부주의형 하위 유형 자체는 L5 (상위 질환인 ADHD는 L1) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | 부주의형: Hold / ADHD(전체): Proceed with Guardrails |

> 1순위 예측인 부주의형 ADHD는 직접 연구가 검색되지 않았습니다. 이 보고서는 근거가 가장 충실한 2순위 예측 **ADHD(전체, TxGNN 99.9996%)**를 중심으로 근거를 정리합니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 수집되지 않았습니다. 알려진 정보에 따르면 clonidine은 알파-2 아드레날린 수용체 작용제입니다. 시냅스후 알파-2A 수용체를 통해 전전두엽 피질의 신경망 조절을 강화하고, 청반(locus coeruleus)의 노르아드레날린 활성을 낮추는 것으로 알려져 있습니다.

이러한 기전은 주의력, 충동성, 과잉행동 조절과 직접 관련됩니다. 서방형 clonidine은 이미 비자극제 ADHD 치료제로 확립되어 있으며, 단독요법과 자극제 병용요법에서 여러 Phase 3 시험이 수행되었습니다. 부주의형은 ADHD의 하위 유형이므로 기전상 적용 가능성은 있으나, 이 하위 유형만을 대상으로 한 시험이나 문헌은 확인되지 않았습니다.

## 임상시험 근거

(ADHD 전체 대상, 관련성 높은 순)

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00556959](https://clinicaltrials.gov/study/NCT00556959) | Phase 3 | 완료 | 236 | 소아·청소년 ADHD에서 서방형 clonidine vs 위약 용량-반응 효능·안전성 평가 |
| [NCT00641329](https://clinicaltrials.gov/study/NCT00641329) | Phase 3 | 완료 | 198 | 자극제 병용(add-on) 시 서방형 clonidine의 효능·안전성 |
| [NCT00031395](https://clinicaltrials.gov/study/NCT00031395) | Phase 3 | 완료 | 122 | 7~12세 ADHD에서 clonidine 단독 또는 methylphenidate 병용 효능·안전성(CAT) |
| [NCT01439126](https://clinicaltrials.gov/study/NCT01439126) | Phase 4 | 완료 | 135 | 40주 무작위 중단 시험으로 장기 효능 유지 평가 |
| [NCT00723190](https://clinicaltrials.gov/study/NCT00723190) | Phase 3 | 완료 | 303 | 12개월 공개 라벨 장기 안전성 평가 |
| [NCT00414921](https://clinicaltrials.gov/study/NCT00414921) | Phase 2 | 완료 | 30 | 4~6세 미취학 아동에서 clonidine과 methylphenidate 단독·병용 평가 |
| [NCT07044609](https://clinicaltrials.gov/study/NCT07044609) | Phase 4 | 모집 예정 | 162 | ADHD와 적대적 반항장애 동반 아동에서 서방형 clonidine 위약대조 시험 |
| [NCT00152750](https://clinicaltrials.gov/study/NCT00152750) | Phase 4 | 불명 | 32 | 틱장애·ADHD 동반 아동의 공격성에 대한 야간 clonidine 효과 |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | 해당 없음 | 모집 중 | 5000 | 소아 대상 연구 미진 약물의 약동학·안전성(ADHD 특이적 아님) |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [30097390](https://pubmed.ncbi.nlm.nih.gov/30097390/) | 2018 | 네트워크 메타분석 | Lancet Psychiatry | 소아·청소년·성인 ADHD 약물의 비교 효능·내약성 |
| [37166701](https://pubmed.ncbi.nlm.nih.gov/37166701/) | 2023 | 체계적 문헌고찰 | CNS Drugs | 성인 ADHD에서 비자극제의 단독·보조요법 평가 |
| [28700715](https://pubmed.ncbi.nlm.nih.gov/28700715/) | 2017 | 네트워크 메타분석 | PLoS One | 소아·청소년 ADHD의 약물·비약물 치료 비교 |
| [25886655](https://pubmed.ncbi.nlm.nih.gov/25886655/) | 2015 | 체계적 문헌고찰·메타분석 | Can J Psychiatry | 알파-2 작용제 등의 반항·공격 행동 약물 치료 평가 |
| [29944175](https://pubmed.ncbi.nlm.nih.gov/29944175/) | 2018 | 체계적 문헌고찰 | Cochrane Database Syst Rev | 틱장애 동반 ADHD 아동의 약물 치료 |
| [40203844](https://pubmed.ncbi.nlm.nih.gov/40203844/) | 2025 | 네트워크 메타분석 | Lancet Psychiatry | ADHD 약물의 심혈관 안전성 비교 |
| [34174276](https://pubmed.ncbi.nlm.nih.gov/34174276/) | 2022 | 문헌고찰 | Pharmacol Ther | 소아·청소년 ADHD의 근거 기반 약물 치료 |
| [35697393](https://pubmed.ncbi.nlm.nih.gov/35697393/) | 2022 | 문헌고찰 | Child Adolesc Psychiatr Clin N Am | 승인·오프라벨 비자극제의 기전, 효능, 안전성 |
| [35507282](https://pubmed.ncbi.nlm.nih.gov/35507282/) | 2022 | 문헌고찰 | Curr Top Behav Neurosci | 자극제와 비자극제(clonidine 포함)가 ADHD 증상에 효과적 |
| [38771653](https://pubmed.ncbi.nlm.nih.gov/38771653/) | 2024 | 문헌고찰 | Expert Opin Pharmacother | 자극제 이후의 ADHD 약물 치료 최신 동향 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201302802 | 켑베이서방정0.1밀리그램(클로니딘염산염) | 서방정 (흰색 양면 볼록 원형 정제) | 허가사항 원문 참조 (제공된 데이터에 적응증 텍스트 없음) |

제조사는 에이치케이이노엔(주)입니다.

## 안전성 고려사항

- **약물 상호작용**: 데이터베이스에서 100건의 상호작용이 확인되었으며, 제시된 항목은 모두 중등도(Moderate) 수준입니다.
  - 코르티코스테로이드: hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide
  - 혈당강하제: canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, glimepiride, glipizide, glyburide, chlorpropamide, acetohexamide, 인슐린 제제
  - 기타: bupropion, morphine, dronabinol
- **투여 시 유의사항(근거 기반)**: 혈압과 심박수 모니터링, 진정 작용 관찰, 갑작스러운 중단 시 반동성 고혈압 위험에 따른 점진적 감량이 필요합니다.

경고 및 금기 세부 내용은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: 부주의형 ADHD는 Hold / ADHD 전체는 Proceed with Guardrails**

**사유:**
1순위 예측인 부주의형 ADHD는 직접 시험과 문헌이 없어 모델 예측만 있는 상태(L5)입니다. 반면 ADHD 전체는 완료된 Phase 3 시험 4건(NCT00556959, NCT00641329, NCT00031395, NCT00723190)과 메타분석이 뒷받침하여 근거 수준 L1에 해당하며, 서방형 clonidine은 이미 확립된 비자극제 치료 옵션입니다.

**진행하려면 필요한 것:**
- 켑베이서방정의 허가 적응증 확인 (허가사항 원문 확보). 한국 허가 적응증에 ADHD가 포함되는지 확인이 필요합니다.
- 허가사항의 경고·금기 정보 확보 (현재 안전성 스크리닝 진행에 차단 요인)
- 작용 기전 데이터 보완 (DrugBank 조회)
- 부주의형 하위 유형에 대한 직접 근거 확인
- 혈압·심박수 모니터링, 진정 관찰, 점진적 감량 등 안전 관리 계획 수립

### 참고: 기타 예측 적응증

| 순위 | 질환 | 점수 | 근거 수준 | 권장 |
|------|------|------|----------|------|
| 7 | 뚜렛 증후군 | 99.98% | L1 (가이드라인·메타분석 기반, 전용 Phase 3 시험은 없음) | Proceed with Guardrails |
| 8 | 비만 | 99.91% | L3 | 연구 과제 (비만 관련 고혈압 연구 후보 수준) |
| 4 | 특정 발달장애 | 99.999% | L4 | Hold |
| 6 | 발모광 | 99.99% | L5 | Hold |
| 3, 5, 9, 10 | 안면지생식기 증후군, 연골점액양섬유종, 비타민과다증, 16p11.2 미세결실 증후군 | 99.85~99.999% | L5 | Hold (근거 없음, 그래프 기반 예측 가능성) |
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

