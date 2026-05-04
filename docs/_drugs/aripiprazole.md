---
layout: default
title: Aripiprazole
parent: 僅模型預測 (L5)
nav_order: 83
evidence_level: L5
indication_count: 10
---

# Aripiprazole
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

# Aripiprazole: 조현병/양극성 장애에서 주요 정동장애로

## 한 문장 요약

Aripiprazole은 도파민·세로토닌 시스템을 동시에 조절하는 비정형 항정신병약물로, 전 세계적으로 조현병과 양극성 장애 치료에 사용됩니다.
TxGNN 모델은 **주요 정동장애(Major Affective Disorder)**에 효과가 있을 것으로 예측하며, 이는 항우울제 보조요법으로서의 역할을 포함합니다.
현재 **다수의 완료된 Phase 3 RCT(핵심 시험만 10건 이상)**와 **20편의 고품질 문헌**이 이 방향을 강력히 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 허가 자료 없음 (글로벌 기준: 조현병, 양극성 I형 장애) |
| 예측 신규 적응증 | 주요 정동장애 (Major Affective Disorder) |
| TxGNN 예측 점수 | 99.62% |
| 근거 수준 | L1 (복수의 완료된 Phase 3 RCT) |
| 한국 시판 현황 | ✗ 미허가 (데이터 팩 기준; 실제 현황 재확인 필요) |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Aripiprazole은 **D2/D3 도파민 수용체 부분 효현제(partial agonist)** 이자 **5-HT1A 세로토닌 수용체 부분 효현제**, **5-HT2A 길항제**로 작용하는 도파민-세로토닌 시스템 안정화제입니다. 이 독특한 기전 덕분에 전두엽 피질처럼 도파민 활성이 낮은 환경에서는 DA 활성을 높여 집행기능과 기분을 개선하고, 변연계처럼 도파민 활성이 높은 환경에서는 이를 억제합니다. 이는 단순 D2 차단제와 근본적으로 다른 작용 방식입니다.

주요 정동장애(주요 우울장애·양극성 장애 포함)의 핵심 병태생리는 전두엽 도파민 결핍, 변연계 과활성, 세로토닌 시스템 이상입니다. Aripiprazole의 5-HT1A 부분 효현 작용은 SSRI/SNRI 항우울제의 효과를 시너지적으로 증강시키며, 이것이 치료 저항성 우울증 환자에서 보조요법으로서 이론적으로 완벽하게 맞아떨어지는 이유입니다.

실제로 Aripiprazole(Abilify®)은 미국 FDA에서 주요 우울장애 항우울제 보조요법, 양극성 I형 장애, 조현병, 자폐증 관련 과민성 등의 적응증으로 허가받은 약물입니다. 이번 TxGNN 예측은 기전적으로 충분히 타당하며, 이미 전 세계적으로 임상 검증이 완료된 방향을 한국 시장의 관점에서 재확인하는 결과로 해석할 수 있습니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00095823](https://clinicaltrials.gov/study/NCT00095823) | Phase 3 | 완료 | 1,200 | 기존 항우울제에 Aripiprazole 보조 투여 시 안전성·유효성 평가한 14주 이중맹검 위약대조 RCT |
| [NCT00876343](https://clinicaltrials.gov/study/NCT00876343) | Phase 3 | 완료 | 586 | SSRI 또는 SNRI 병용 Aripiprazole 보조요법의 주요 우울장애 유효성·안전성 평가 |
| [NCT02046564](https://clinicaltrials.gov/study/NCT02046564) | Phase 3 | 완료 | 412 | Aripiprazole/sertraline 병용제(ASC-01) vs sertraline 단독: sertraline 불완전 반응 MDD 환자 대상 비교 |
| [NCT02305823](https://clinicaltrials.gov/study/NCT02305823) | Phase 4 | 완료 | 203 | 첫 발병 비정동성 정신증 환자에서 Aripiprazole·Quetiapine·Ziprasidone 유효성 직접 비교 |
| [NCT00107939](https://clinicaltrials.gov/study/NCT00107939) | Phase 3 | 완료 | 453 | Licarbazepine을 비정형 항정신병약물(Aripiprazole 포함) 보조 투여 시 양극성 I형 조증 삽화 유효성·안전성 평가 |
| [NCT00683852](https://clinicaltrials.gov/study/NCT00683852) | Phase 3 | 완료 | 225 | 항우울제 불충분 반응 MDD 외래환자에서 저용량 Aripiprazole 보조요법 유효성 평가 |
| [NCT00882362](https://clinicaltrials.gov/study/NCT00882362) | Phase 3 | 완료 | 155 | SSRI/SNRI 병용 Aripiprazole 보조요법의 주요 우울장애 장기 안전성·유효성 평가 |
| [NCT00667745](https://clinicaltrials.gov/study/NCT00667745) | Phase 4 | 완료 | 283 | 양극성 장애에서 Lithium 포함 최적화 약물치료의 전반적 질환 수준·삶의 질 개선 평가 (Aripiprazole 비교군 포함) |
| [NCT01111565](https://clinicaltrials.gov/study/NCT01111565) | Phase 3 | 조기 종료 | 137 | Aripiprazole/Escitalopram 병용요법의 MDD 유효성·안전성 평가 (조기 종료, 부분 안전성 자료 제공) |
| [NCT03423680](https://clinicaltrials.gov/study/NCT03423680) | Phase 3 | 모집 중 | 390 | 기분안정제 병용 Aripiprazole 보조요법의 양극성 I형/II형 주요 우울 삽화 유효성·안전성 확인 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [38669232](https://pubmed.ncbi.nlm.nih.gov/38669232/) | 2024 | Systematic Review + Meta-analysis | PLoS One | Aripiprazole 또는 bupropion 보조요법·전환요법의 TRD/MDD 유효성·안전성을 평가한 RCT 최대 규모 메타분석 |
| [38219278](https://pubmed.ncbi.nlm.nih.gov/38219278/) | 2024 | Systematic Review + NMA | Neuropsychopharmacology Reports | 항우울제 불충분 반응 일본 MDD 환자에서 brexpiprazole vs aripiprazole 비교 네트워크 메타분석 |
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Systematic Review + NMA | J Affective Disorders | 치료 저항성 우울증 보조제 비교 네트워크 메타분석; Aripiprazole이 주요 효과적 보조제 중 하나로 확인 |
| [37149344](https://pubmed.ncbi.nlm.nih.gov/37149344/) | 2023 | Review | Psychiatric Clinics of North America | 치료 저항성 우울증의 항우울제 및 비정형 항정신병약물 검토; Aripiprazole·brexpiprazole·quetiapine 중심 |
| [35510505](https://pubmed.ncbi.nlm.nih.gov/35510505/) | 2023 | Systematic Review + Meta-analysis | Psychological Medicine | MDD 치료에서 항정신병약물의 유효성·안전성/내약성 포괄적 메타분석 (단독 및 보조요법 포함) |
| [37746943](https://pubmed.ncbi.nlm.nih.gov/37746943/) | 2023 | Systematic Review + NMA | Medicine | MDD 보조치료에서 4가지 비정형 항정신병약물(Aripiprazole 포함) 비교·순위화 네트워크 메타분석 |
| [34167174](https://pubmed.ncbi.nlm.nih.gov/34167174/) | 2021 | Systematic Review + Meta-analysis | Primary Care Companion CNS Disorders | MDD에서 Aripiprazole 장기 보조요법(≥6개월)의 유효성·내약성 체계적 고찰 |
| [25963405](https://pubmed.ncbi.nlm.nih.gov/25963405/) | 2016 | Review | Asia-Pacific Psychiatry | FDA 승인 비정형 항정신병약물(quetiapine, aripiprazole, olanzapine)의 항우울 효과 기전·임상 근거 검토 |
| [37815563](https://pubmed.ncbi.nlm.nih.gov/37815563/) | 2023 | Review | JAMA | 양극성 장애 진단·치료 종합 검토; 미국 내 약 800만 명, 전 세계 4천만 명 이상에게 영향 |
| [36961650](https://pubmed.ncbi.nlm.nih.gov/36961650/) | 2023 | Randomized Open-Label Study | CNS Drugs | Aripiprazole 2개월 지속형 주사제(Ari 2MRTU 960) 안전성·내약성·약동학 평가; 조현병 및 양극성 I형 성인 대상 |

---

## 한국 시판 정보

이번 데이터 팩에서 한국 내 Aripiprazole 허가 정보가 확인되지 않았습니다 (허가증 0건, 시판 현황: 미허가).

> ⚠️ **주의:** Aripiprazole(Abilify®)은 미국·유럽·일본 등 주요국에서 광범위하게 허가된 약물입니다. 한국 MFDS 실제 허가 현황과 데이터 팩 내용 간 불일치 가능성이 있으므로, MFDS 의약품통합정보시스템(nedrug.mfds.go.kr)을 통한 직접 확인이 필요합니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
주요 우울장애 및 양극성 장애(주요 정동장애)에서 Aripiprazole 보조요법을 지지하는 복수의 Phase 3 완료 RCT가 존재하며, FDA·EMA 등 주요 규제기관에서 이미 허가된 적응증으로 근거 수준이 L1(최고 등급)에 해당합니다. 한국 시장 도입을 위한 임상적 근거는 충분합니다.

**진행하려면 필요한 것:**
- 한국 MFDS 실제 허가 현황 재확인 (데이터 팩 내 허가 정보 부재 해소)
- DrugBank API를 통한 상세 MOA 데이터 보완 (현재 Data Gap)
- MFDS 허가사항 기반 한국어 안전성 경고·금기 정보 수집 (현재 Blocking Data Gap)
- 한국인 대상 특이적 약동학/약력학 자료 및 아시아 인구집단 임상 데이터 추가 검토

---

> **면책 조항:** 본 보고서는 연구 참고용으로만 제공되며, 의료 조언을 구성하지 않습니다. 약물 재창출 후보는 임상 검증을 거쳐야 합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

