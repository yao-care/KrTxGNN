---
layout: default
title: Clonidine
parent: 僅模型預測 (L5)
nav_order: 181
evidence_level: L5
indication_count: 10
---

# Clonidine
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

# Clonidine: 고혈압에서 주의력결핍 과잉행동장애 (주의력결핍형)으로

## 한 문장 요약

Clonidine은 중추 α2 아드레날린 수용체 작용제로, 고혈압 치료에 광범위하게 사용되어 온 약물입니다.
TxGNN 모델은 **주의력결핍 과잉행동장애 주의력결핍형 (ADHD Inattentive Type)**에 효과가 있을 수 있다고 예측하며,
순수 주의력결핍형에 특화된 임상시험은 아직 없으나 ADHD 전반을 대상으로 한 **다수의 완료된 Phase 3 RCT**와 **체계적 문헌고찰**이 이 방향을 간접 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 허가 데이터 없음 (고혈압 치료에 글로벌 광범위 사용) |
| 예측 신규 적응증 | 주의력결핍 과잉행동장애 주의력결핍형 (ADHD Inattentive Type) |
| TxGNN 예측 점수 | 99.9997% |
| 근거 수준 | L3 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Clonidine은 전전두엽 피질(Prefrontal Cortex, PFC)의 α2A 아드레날린 수용체를 선택적으로 활성화하는 비자극성(non-stimulant) 약물입니다. 이 기전을 통해 작업 기억(working memory)과 억제 조절(inhibitory control) 기능을 강화하고, 청반(locus coeruleus)의 과도한 노르에피네프린 방출을 억제하여 충동성과 과잉행동 증상을 완화합니다. 미국 FDA는 Clonidine 서방형 제제(Kapvay®)를 2010년 6~17세 ADHD 환자 치료제로 승인한 바 있습니다.

ADHD 주의력결핍형(ADHD-I)은 과잉행동·충동형(ADHD-HI) 및 혼합형(ADHD-C)과 동일한 전전두엽 노르에피네프린 조절 이상을 핵심 병리로 공유합니다. 따라서 Clonidine의 α2A 수용체 조절 기전은 주의력 결핍 증상 개선에도 이론적으로 적용 가능합니다. 실제로 ADHD 전반을 대상으로 한 복수의 Phase 3 RCT(NCT00031395, NCT00641329, NCT00556959)가 Clonidine의 ADHD 증상 개선 효능을 입증하였으며, 2018년 The Lancet Psychiatry 네트워크 메타분석(PMID 30097390)도 이를 지지합니다.

다만 현재까지 발표된 임상시험 대부분은 혼합형 또는 과잉행동형을 주 대상으로 설계되었으며, 순수 주의력결핍형만을 독립적으로 연구한 RCT는 부재합니다. 이 점이 ADHD 전반(Rank 2, L1)과 달리 본 예측(Rank 1)의 근거 수준이 L3에 머무는 이유이며, 진행 시 하위그룹 분석 또는 독립 시험 설계가 필요합니다.

---

## 임상시험 근거

현재 "주의력결핍 과잉행동장애 주의력결핍형"에 특화된 등록 임상시험이 없습니다.

> **참고**: ADHD 전반(Rank 2)에 해당하는 Clonidine 임상시험 중 관련성 높은 주요 8건을 아래에 제시합니다. ADHD-I는 ADHD의 하위 분류이므로 이들 근거가 간접적으로 적용될 수 있습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00031395](https://clinicaltrials.gov/study/NCT00031395) | Phase 3 | 완료 | 122 | 7~12세 ADHD 아동에서 Clonidine 단독 및 메틸페니데이트 병용 안전성·효능 직접 평가 (핵심 독립 시험) |
| [NCT00641329](https://clinicaltrials.gov/study/NCT00641329) | Phase 3 | 완료 | 198 | CLONICEL® (서방형) + 정신자극제 병용 대 정신자극제 단독 비교 RCT; add-on 효과 입증 |
| [NCT00556959](https://clinicaltrials.gov/study/NCT00556959) | Phase 3 | 완료 | 236 | CLONICEL® 서방형 용량-반응 평가; 가장 큰 규모의 위약대조 Phase 3 시험 |
| [NCT01439126](https://clinicaltrials.gov/study/NCT01439126) | Phase 4 | 완료 | 135 | KAPVAY™ 서방형 40주 장기 효능·안전성 확인; 무작위 투약 중단(withdrawal) 설계로 유지 효과 검증 |
| [NCT00723190](https://clinicaltrials.gov/study/NCT00723190) | Phase 3 | 완료 | 303 | CLONICEL 12개월 개방표지 장기 안전성 연구; 단독 및 자극제 병용 모두 평가, 최대 규모 |
| [NCT00414921](https://clinicaltrials.gov/study/NCT00414921) | Phase 2 | 완료 | 30 | 4~6세 학령전 아동 대상 Clonidine + 메틸페니데이트 탐색 연구 |
| [NCT07044609](https://clinicaltrials.gov/study/NCT07044609) | Phase 4 | 모집 예정 | 162 | Onyda™ XR의 ADHD+ODD 아동(6~12세) 대상 이중맹검 위약대조 시험 (2025~2026 예정) |
| [NCT05916339](https://clinicaltrials.gov/study/NCT05916339) | Phase 4 | 모집 중 | 500 | 자폐스펙트럼+ADHD 아동의 약물 비교효과 연구 (SMART 설계); α2 작용제 군 포함 |

---

## 문헌 근거

현재 "주의력결핍 과잉행동장애 주의력결핍형"에 특화된 직접 문헌이 없습니다.

> **참고**: ADHD 전반을 대상으로 한 고품질 문헌 중 Clonidine과 직접 관련된 상위 10편을 제시합니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [30097390](https://pubmed.ncbi.nlm.nih.gov/30097390/) | 2018 | Network Meta-Analysis | The Lancet Psychiatry | 아동·청소년·성인 ADHD 약물 비교 효능·내약성 체계적 분석; Clonidine 포함된 최대 규모 NMA |
| [37166701](https://pubmed.ncbi.nlm.nih.gov/37166701/) | 2023 | Systematic Review | CNS Drugs | 성인 ADHD의 비자극제(Clonidine 포함) 체계적 고찰 및 메타분석 |
| [39760346](https://pubmed.ncbi.nlm.nih.gov/39760346/) | 2025 | Review | Pediatric Annals | 소아·청소년 비자극제 ADHD 치료 최신 검토; Clonidine을 자극제 대안으로 명시 |
| [28391425](https://pubmed.ncbi.nlm.nih.gov/28391425/) | 2017 | Systematic Review | Paediatric Drugs | ADHD 소아 수면장애 치료 약물 안전성·효능 체계적 검토; Clonidine의 수면 개선 효과 포함 |
| [34174276](https://pubmed.ncbi.nlm.nih.gov/34174276/) | 2022 | Review | Pharmacology & Therapeutics | 아동·청소년 ADHD 근거기반 약리치료 종합 검토 |
| [35507282](https://pubmed.ncbi.nlm.nih.gov/35507282/) | 2022 | Review | Curr Topics Behav Neurosci | ADHD 현행 약리치료 총괄; Clonidine을 FDA 승인 비자극제로 기술 |
| [28700715](https://pubmed.ncbi.nlm.nih.gov/28700715/) | 2017 | Network Meta-Analysis | PLoS ONE | 아동·청소년 ADHD 약리·비약리 치료 비교 체계적 검토 |
| [40203844](https://pubmed.ncbi.nlm.nih.gov/40203844/) | 2025 | Network Meta-Analysis | The Lancet Psychiatry | ADHD 치료 약물의 심혈관 안전성 비교; Clonidine의 혈역학적 영향(혈압·맥박) 정량 평가 |
| [41164104](https://pubmed.ncbi.nlm.nih.gov/41164104/) | 2025 | Review | Australian Prescriber | 아동·청소년 ADHD 약물 관리 최신 임상 가이드 |
| [26601963](https://pubmed.ncbi.nlm.nih.gov/26601963/) | 2016 | Review | Current Pharmaceutical Design | ADHD 약물 작용기전 및 부작용 종합 검토; Clonidine의 α2 기전 기술 |

---

## 한국 시판 정보

현재 한국에서 Clonidine에 대한 허가 기록이 없습니다 (허가증 수: 0건).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
Clonidine 서방형은 미국 FDA에서 이미 ADHD(6~17세) 치료제로 승인된 비자극제이며, 다수의 완료된 Phase 3 RCT와 고품질 체계적 문헌고찰이 ADHD 전반에 대한 효능을 지지합니다. 주의력결핍형(ADHD-I)은 ADHD의 하위 분류로 동일한 전전두엽 노르에피네프린 조절 이상이라는 핵심 병리를 공유하므로, 기존 근거의 외삽 가능성이 높습니다.

**진행하려면 필요한 것:**
- 한국 식품의약품안전처(MFDS) 허가 신청을 위한 규제 전략 수립 (미국 Kapvay® 허가 자료 활용 가능)
- 작용 기전(MOA) 상세 데이터 보완 (DrugBank API 조회 권장, DG002 해소)
- 한국 허가사항 및 경고·금기 문구 확인 (MFDS 또는 FDA 허가 문서 검토, DG001 해소)
- ADHD 주의력결핍형만을 대상으로 한 하위그룹 분석 또는 독립 임상시험 설계 검토
- 심혈관 안전성 모니터링 계획 수립 (혈압 저하, 서맥 등 α2 작용제 계열 주요 이상반응 관리)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

