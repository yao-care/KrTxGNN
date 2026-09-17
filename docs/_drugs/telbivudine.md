---
layout: default
title: Telbivudine
parent: 중등도 근거 (L3-L4)
nav_order: 661
evidence_level: L4
indication_count: 10
---

# Telbivudine
{: .fs-9 }

근거 수준: **L4** | 예측 적응증: **10** 건
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

Using report-generation instructions directly (no additional skill needed — this is a structured content-authoring task per the provided prompt spec).

---

# Telbivudine: 적응증 미상에서 만성 C형 간염 바이러스 감염으로

## 한 문장 요약

Telbivudine(DrugBank ID: DB01265)은 한국에 허가된 제품이 없어 기존 적응증 정보가 확인되지 않는 약물입니다. TxGNN 모델은 **만성 C형 간염 바이러스 감염(Chronic Hepatitis C Virus Infection)**에 효과가 있을 수 있다고 예측했으나(예측 점수 99.96%), **10건의 임상시험**과 **10편의 문헌**을 검토한 결과 대부분이 실제로는 B형 간염(HBV) 관련 연구이며, 이 예측을 직접 지지하는 근거는 확인되지 않았습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (한국 허가 정보 미제공) |
| 예측 신규 적응증 | 만성 C형 간염 바이러스 감염 (Chronic Hepatitis C Virus Infection) |
| TxGNN 예측 점수 | 99.96% (rank 1,381) |
| 근거 수준 | L4 |
| 한국 시판 현황 | 미출시 (한국 내 허가 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

작용 기전(MOA) 데이터는 현재 제공되지 않았습니다. 다만 확보된 임상·문헌 근거를 종합하면, Telbivudine은 L-티미딘 뉴클레오사이드 유사체로 인산화 후 **B형 간염 바이러스(HBV) DNA 중합효소(역전사효소)**를 경쟁적으로 억제하고 사슬 종결을 유도하는 약물입니다.

반면 C형 간염 바이러스(HCV)는 RNA 바이러스로 **NS5B RNA 의존성 RNA 중합효소**를 이용해 복제하며, 두 효소는 구조와 기질 특이성이 달라 Telbivudine이 HCV 복제를 억제한다는 기전적 근거는 보고된 바 없습니다.

근거팩에 포함된 임상시험·문헌은 대부분 "B형 및 C형 간염"을 함께 다루는 종설(review)이거나, HBV 환자를 대상으로 한 시험이 "hepatitis"라는 공통 키워드로 인해 이 적응증에 연결된 사례입니다. 즉, TxGNN의 높은 예측 점수는 지식 그래프 상의 위상적 유사성(topological similarity)에서 비롯된 것으로 보이며, 직접적인 항HCV 약리 근거는 확인되지 않았습니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00805675](https://clinicaltrials.gov/study/NCT00805675) | Phase 3 | 완료 | 83 | Telbivudine+Tenofovir 병용 vs 각각 단독요법의 HBV DNA 동태 비교(HBeAg 양성 대상성 만성B형간염 대상, C등급: HBV 시험이 HCV로 오분류) |
| [NCT01925820](https://clinicaltrials.gov/study/NCT01925820) | Phase 4 | 불명 | 540 | Pegasys+Entecavir vs Entecavir vs Pegasys, HBeAg 음성 만성B형간염 비교 연구 |
| [NCT00142298](https://clinicaltrials.gov/study/NCT00142298) | Phase 3 | 완료 | 1869 | Idenix 후원 telbivudine 임상시험 참여자 대상 개방표지 확장연구(만성B형간염) |
| [NCT03181607](https://clinicaltrials.gov/study/NCT03181607) | N/A | 불명 | 300 | 고HBV DNA 부하 임산부에서 TDF/telbivudine을 이용한 모자수직감염(MTCT) 예방 |
| [NCT00412529](https://clinicaltrials.gov/study/NCT00412529) | Phase 3 | 완료 | 44 | Telbivudine vs Entecavir, HBeAg양성 대상성 만성B형간염에서 HBV DNA 동태 비교 |
| [NCT00810524](https://clinicaltrials.gov/study/NCT00810524) | Phase 4 | 불명 | 600 | 만성HBV감염 환자 대상 항바이러스 치료의 장기 예후 영향 평가 |
| [NCT02956850](https://clinicaltrials.gov/study/NCT02956850) | Phase 1 | 완료 | 160 | RO7020531의 안전성·PK/PD 평가(건강인 및 만성B형간염 환자 대상) |
| [NCT02058108](https://clinicaltrials.gov/study/NCT02058108) | Phase 3 | 중단 | 53 | 소아·청소년 만성B형간염에서 telbivudine 경구용액/정제 효능·안전성 평가(C등급: HBV 시험 오분류) |
| [NCT01083251](https://clinicaltrials.gov/study/NCT01083251) | N/A | 불명 | 120 | 만성HBV감염자에서 비타민D 보충이 Peg-IFNα2a 또는 telbivudine 단독요법에 미치는 부가효과 |
| [NCT05466071](https://clinicaltrials.gov/study/NCT05466071) | N/A | 불명 | 200 | 고HBV DNA 부하 임산부에서 TAF의 모자수직감염 예방 효능·안전성 평가 |

> 위 10건 모두 실제로는 HBV(B형 간염) 대상 시험으로, HCV(C형 간염)에 대한 직접적인 유효성 데이터는 포함되어 있지 않습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [19344237](https://pubmed.ncbi.nlm.nih.gov/19344237/) | 2009 | Review | Expert Rev Anti Infect Ther | 만성 B형·C형간염 관리에 대한 종설(초록 없음) |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wien Med Wochenschr | 만성 B형·C형간염의 현재 치료 및 향후 치료전망 |
| [25233195](https://pubmed.ncbi.nlm.nih.gov/25233195/) | 2014 | Review | J Perinatol | 임신 중 B형·C형간염 리뷰 및 모자수직감염(MTCT) 감소 권고 |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | B형·C형간염 항바이러스제 및 신기능에 미치는 영향 |
| [28845882](https://pubmed.ncbi.nlm.nih.gov/28845882/) | 2018 | Cohort | J Viral Hepat | HCV DAA 치료 전후 HBV 재활성화 및 간 이상반응 발생률(미국 재향군인 코호트) |
| [18330099](https://pubmed.ncbi.nlm.nih.gov/18330099/) | 2007 | Guideline | Acta Gastroenterol Belg | 만성B형간염 관리 벨기에 가이드라인(2007) |
| [18340426](https://pubmed.ncbi.nlm.nih.gov/18340426/) | 2008 | Review | Der Internist | 만성B형·C형간염 항바이러스치료 최신 자료 및 독일 권고안 |
| [23697556](https://pubmed.ncbi.nlm.nih.gov/23697556/) | 2013 | Clinical study | J Interferon Cytokine Res | Telbivudine 치료 중 HBeAg 혈청전환과 혈청 IL-37 농도 상관관계 |
| [21964179](https://pubmed.ncbi.nlm.nih.gov/21964179/) | 2011 | Review | Mayo Clin Proc | HIV 이외 바이러스(헤르페스·간염·인플루엔자)에 대한 항바이러스제 총설 |
| [21999649](https://pubmed.ncbi.nlm.nih.gov/21999649/) | 2011 | Review | Paediatric Drugs | 소아 만성 간질환 관리(1부): 치료 가능 질환 중심 |

> 상기 문헌은 대부분 B형·C형간염을 함께 다루는 종설로, telbivudine의 HCV에 대한 직접적 항바이러스 효능을 보고한 연구는 없습니다.

---

## 한국 시판 정보

현재 한국에 허가된 Telbivudine 제품이 없습니다(허가증 0건, 미출시).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 근거 수준 L4로, 확인 가능한 임상시험·문헌이 대부분 HBV(B형 간염) 관련 연구이며 HCV(C형 간염)에 대한 직접적 유효성 데이터가 없습니다.
- Telbivudine의 작용 표적(HBV DNA 중합효소)과 HCV 복제 효소(NS5B RNA 의존성 RNA 중합효소)가 상이하여 기전적 타당성도 부족합니다.

**진행하려면 필요한 것:**
- Telbivudine의 항HCV in vitro/in vivo 활성 데이터 (현재 전무)
- 작용기전(MOA) 상세 자료 확보 — DrugBank API 조회 필요 (DG002)
- 한국 허가사항(경고·금기) 확보 — 안전성 초기평가(S1) 진입을 위한 필수 선결 조건, 현재 Blocking 상태 (DG001)

**참고 — 동일 근거팩 내 대안 후보:**
같은 근거팩의 2순위 후보인 **만성 B형간염(Hepatitis B virus infection)**은 근거 수준 **L1**, 완료된 대규모 Phase 3 RCT([NCT00142298](https://clinicaltrials.gov/study/NCT00142298), n=1,869 등) 다수를 보유하고 있으며 **"Proceed with Guardrails"** 권고를 받았습니다. 다만 이는 telbivudine의 이미 알려진 작용 영역(HBV DNA 중합효소 억제)과 일치하는 결과로, 진정한 신규 재창출 후보라기보다 모델이 기존 지식을 재확인한 사례로 해석하는 것이 타당합니다. 신규 적응증 발굴이 목적이라면 해당 후보보다는 별도의 낮은 순위 예측(예: HIV, 대사질환 등)에 대한 추가 검증이 필요합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

