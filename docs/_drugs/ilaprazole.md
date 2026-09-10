---
layout: default
title: Ilaprazole
parent: 僅模型預測 (L5)
nav_order: 386
evidence_level: L5
indication_count: 5
---

# Ilaprazole
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

# ILAPRAZOLE: 미시판(개발단계)에서 활동성 소화성궤양으로

## 한 문장 요약

Ilaprazole은 제3세대 질소펌프억제제(PPI) 계열 약물로, 중국·한국 등에서 진행된 자체 임상개발 프로그램을 통해 원래부터 소화성궤양(특히 십이지장궤양) 치료를 목표로 개발되었으나, 현재 대만(taiwan_regulatory 기준) 내 허가·시판 이력은 없습니다. TxGNN 모델은 **활동성 소화성궤양(Active Peptic Ulcer Disease)**에 대한 효과를 예측하며, 이는 **5건의 임상시험(완료 4건 포함)**과 **6편의 문헌**으로 뒷받침됩니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 자료 없음 (현지 허가 이력 없음, 원개발 적응증은 십이지장궤양·소화성궤양으로 추정) |
| 예측 신규 적응증 | 활동성 소화성궤양 (Active Peptic Ulcer Disease) |
| TxGNN 예측 점수 | 99.89% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✗ 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

DrugBank의 공식 작용기전(MOA) 데이터는 현재 확보되지 않았습니다(Data Gap, High severity). 다만 근거팩 내 예측 근거(rationale)에 따르면 ilaprazole은 위벽세포의 H+/K+-ATPase를 억제하는 제3세대 PPI로, omeprazole·rabeprazole·esomeprazole과 동일한 기전을 공유합니다.

활동성 소화성궤양은 애초에 ilaprazole의 임상개발 프로그램(중국 다기관 Phase 2/3 시험군)의 원 표적 적응증이었습니다. 즉 이번 예측은 완전히 새로운 치료영역 발굴이라기보다, 약물이 이미 확립한 핵심 적응증을 현지(대만) 시장 진입 관점에서 재확인하는 성격이 강합니다. 다만 대만 내 허가·시판 실적이 전무하므로, 이는 "재창출"이라기보다 "미허가 약물의 시장 진입 타당성 검토"에 가깝습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00953381](https://clinicaltrials.gov/study/NCT00953381) | Phase 2 | 완료 | 235 | 급성 십이지장궤양에서 ilaprazole 3용량군(5/10/20mg) vs omeprazole 20mg, 4주 궤양치유율이 1차 평가변수 |
| [NCT02847455](https://clinicaltrials.gov/study/NCT02847455) | Phase 2/3 | 완료 | 408 | 급성 십이지장궤양에서 ilaprazole(5/10mg) vs rabeprazole 10mg, 4주 궤양치유율 비교 |
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | 완료 | 323 | H. pylori 양성 위/십이지장궤양 환자 대상 ilaprazole vs pantoprazole 3제요법 7일 제균효과 비교 |
| [NCT06284876](https://clinicaltrials.gov/study/NCT06284876) | Phase 3 | 모집 중 | 416 | NSAID 연관 소화성궤양 예방에서 ilaprazole 10mg의 비열등성 평가(24주 시점, 결과 미도출) |
| [NCT00952978](https://clinicaltrials.gov/study/NCT00952978) | Phase 3 | 완료 | 496 | 급성 십이지장궤양에서 ilaprazole 10mg vs omeprazole 20mg 대규모 3상 시험, 4주 궤양치유율 비교 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [19434360](https://pubmed.ncbi.nlm.nih.gov/19434360/) | 2009 | RCT | Journal of Gastroenterology | 위·십이지장궤양에서 ilaprazole과 omeprazole의 궤양치유 효과 비교 병행군 RCT |
| [20679904](https://pubmed.ncbi.nlm.nih.gov/20679904/) | 2011 | RCT | Journal of Clinical Gastroenterology | 십이지장궤양 치료에서 신규 PPI ilaprazole과 omeprazole 비교, 용량-반응 관계 규명 |
| [22070512](https://pubmed.ncbi.nlm.nih.gov/22070512/) | 2012 | RCT | Curr Med Res Opin | 십이지장궤양 3상 RCT, ilaprazole 10mg vs omeprazole 20mg, CYP2C19 대사와의 관계 분석 |
| [27605258](https://pubmed.ncbi.nlm.nih.gov/27605258/) | 2016 | RCT | Clinical Drug Investigation | 역류성식도염(산 관련 질환) 치료에서 ilaprazole 다기관 활성대조 RCT |
| [30789856](https://pubmed.ncbi.nlm.nih.gov/30789856/) | 2019 | RCT | Journal of Clinical Gastroenterology | 십이지장궤양 치료에서 ilaprazole과 rabeprazole 비교, 용량-효과 관계 탐색 |
| [24801687](https://pubmed.ncbi.nlm.nih.gov/24801687/) | 2014 | Animal Study | Digestive Diseases and Sciences | 랫드 모델에서 정맥주사 ilaprazole이 경구제형보다 위병변에 더 강력한 보호효과(전임상) |

## 한국 시판 정보

현재 대만(현지 규제기관) 내 허가받은 제품이 없습니다 (시판 현황: 미출시, 허가증 0건).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> ⚠️ 참고: 근거팩에 명시된 데이터 갭(DG001, Blocking) 상 TFDA 수준의 경고·금기 정보 미확보로 안전성 초평가(S1) 자체가 진행되지 못한 상태입니다. 아래 결론의 "진행 조건"을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
활동성 소화성궤양에 대해 완료된 Phase 2/3 RCT 다수(근거 수준 L1)가 ilaprazole의 유효성을 뒷받침하며, 이는 약물의 원 개발 적응증과 기전적으로 완전히 일치합니다. 다만 현지 허가·시판 이력이 전무하고, 안전성 데이터(경고/금기/DDI)가 아직 확보되지 않아 무조건적 진행은 불가하며 안전장치(Guardrails)를 전제로 한 진행이 타당합니다.

**진행하려면 필요한 것:**
- TFDA(현지 식약처) 수준 허가사항 경고·금기 정보 확보 (DG001, Blocking — 안전성 초평가 S1 진입의 선행 조건)
- 공식 DrugBank MOA 데이터 확보 (DG002, High)
- 약물상호작용(DDI) 프로파일 조사 (현재 not_found 상태)
- 미시판 상태이므로 현지 규제기관 대상 허가 신청 또는 가교시험 필요 여부 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

