---
layout: default
title: Tenofovir Disoproxil
parent: 모델 예측만 (L5)
nav_order: 667
evidence_level: L5
indication_count: 4
---

# Tenofovir Disoproxil
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **4** 건
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

# Tenofovir Disoproxil: 기존 적응증 정보 없음에서 SIV 감염(전임상 근거)으로

## 한 문장 요약

Tenofovir Disoproxil(DB00300)은 본 Evidence Pack에 원 적응증 및 작용기전(MOA) 자료가 등록되어 있지 않습니다. TxGNN 모델은 **원숭이면역결핍바이러스(SIV) 감염**에 효과가 있을 것으로 예측(점수 99.95%)했으나, 이는 인간이 아닌 영장류 동물 질환이며, 현재 **관련 임상시험 2건(모두 저관련성 판정)**과 **문헌 20편(대부분 원숭이 전임상 모델)**이 확인됩니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 자료 없음 (원 적응증·허가 정보 미제공) |
| 예측 신규 적응증 | 원숭이면역결핍바이러스 감염 (Simian Immunodeficiency Virus Infection) |
| TxGNN 예측 점수 | 99.95% |
| 근거 수준 | L4 (전임상 동물모델 연구 중심, 직접 관련 임상시험 없음) |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용기전(MOA) 데이터는 확보되지 않았습니다(Data Gap, 심각도 High).

다만 근거 자료의 기전 연관성(repurposing_rationale) 설명에 따르면, Tenofovir는 반전사효소억제제(reverse transcriptase inhibitor) 계열이며, SIV는 HIV-1과 동일한 렌티바이러스(Lentivirus) 속(屬)으로 반전사효소 구조가 고도로 보존되어 있습니다. 이 때문에 붉은털원숭이(macaque) 모델에서 tenofovir 및 그 유도체(TAF 등)의 항SIV/SHIV 활성이 수십 년간 반복적으로 확인되어 왔습니다.

다만 중요한 한계가 있습니다: 이 근거들은 SIV 감염 자체(동물 질환)를 인간 적응증으로 삼기 위한 것이 아니라, **인간 HIV 노출 전 예방요법(PrEP) 전략을 뒷받침하기 위한 전임상 동물실험 자료**입니다. 따라서 이 예측을 그대로 "인간 대상 SIV 치료 적응증"으로 해석하는 것은 타당하지 않으며, 실질적 함의는 "tenofovir 기반 PrEP/치료 전략의 기전적 타당성"에 국한됩니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | NA | 철회됨 | 0 | Raltegravir의 HIV 붕괴동역학 연구로, tenofovir와 무관하며 SIV 모델을 참고 언급만 함 — KG 오매칭, 관련성 낮음(Grade C) |
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | 불명 | 12 | Vedolizumab+ART 병용요법을 통한 바이러스 관해 연구로, tenofovir 특이적 근거가 아님 — 관련성 낮음(Grade C) |

두 시험 모두 실제 연구약물이 tenofovir가 아니며, 이 적응증에 대한 직접적 근거로 사용하기 어렵습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [20874040](https://pubmed.ncbi.nlm.nih.gov/20874040/) | 2010 | RCT | Pharmacotherapy | 전신 노출 전 예방요법(PrEP)으로서 tenofovir 기반 요법의 인체 적용 근거 개관 |
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | Cohort(동물모델) | Nature Communications | 조기 치료 개시 및 초장기 지속형 항바이러스제 병용으로 SHIV 관해 유도 |
| [38134382](https://pubmed.ncbi.nlm.nih.gov/38134382/) | 2024 | Cohort(동물모델) | J Infect Dis | TAF/Elvitegravir 질내 삽입형 제제의 노출 후 SHIV 방어 효과 |
| [31597776](https://pubmed.ncbi.nlm.nih.gov/31597776/) | 2019 | Cohort(동물모델) | J Virol | ART 조기 개시 후 SIV 잔존 바이러스 게놈의 완전성 평가 |
| [31362305](https://pubmed.ncbi.nlm.nih.gov/31362305/) | 2019 | Cohort(동물모델) | J Infect Dis | 경구 TAF/FTC 병용 또는 TAF 단독의 질내 SHIV 감염 예방 효능 |
| [36477356](https://pubmed.ncbi.nlm.nih.gov/36477356/) | 2022 | Cohort(동물모델) | JCI Insight | 저삼투압 직장관장형 tenofovir 제제의 SHIV 감염 예방 효과 |
| [29788316](https://pubmed.ncbi.nlm.nih.gov/29788316/) | 2018 | Cohort(동물모델) | J Infect Dis | 질내 투여 FTC/TFV 젤의 반복 직장 SHIV 노출 방어 효과 |
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Cohort(동물모델) | J Infect Dis | 경구 FTC/TAF 병용 화학예방요법의 직장 SHIV 감염 방어 |
| [26743846](https://pubmed.ncbi.nlm.nih.gov/26743846/) | 2016 | Cohort(동물모델) | J Infect Dis | 성병 동반감염(클라미디아·트리코모나스) 상황에서 FTC/TDF의 질내 SHIV 예방 효과 |
| [23633402](https://pubmed.ncbi.nlm.nih.gov/23633402/) | 2013 | Cohort(동물모델) | J Infect Dis | K65R 내성 변이 SHIV에 대한 FTC/TDF 예방 효능 |

문헌 근거 대부분이 원숭이(macaque) 전임상 모델 연구이며, 인간 대상 SIV 치료를 직접 다룬 문헌은 없습니다(SIV는 인간에게 발생하지 않는 동물 질환).

---

## 한국 시판 정보

현재 한국 내 허가 제품이 없습니다(허가증 0건, 미출시).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> 참고: TFDA(식약처) 수준의 경고·금기 정보 부재는 심각도 **Blocking**(DG001)으로 분류되어 있어, 안전성 초기 평가(S1) 단계 진입이 현재 불가능합니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 예측된 1순위 적응증(SIV 감염)은 인간이 아닌 영장류 동물 질환으로, 실제 인간 치료 적응증으로 직접 전환할 수 없습니다.
- 제시된 임상시험 2건은 모두 tenofovir와 무관한 약물(raltegravir, vedolizumab)을 다루며 관련성 Grade C(낮음)로 판정되어, 실질적 임상 근거로 인정하기 어렵습니다.
- 문헌 근거는 기전적으로 타당하나 전임상 동물모델 수준(L4)에 머물러 있어, 인간 임상 개발 단계로 진행하기에는 근거가 부족합니다.
- 2·3순위 예측(고양이 면역결핍증후군, 신경발달장애)은 각각 수의학 적응증 또는 근거 전무(L5)로 확인되어 KG 노이즈로 판단되며, 4순위(폐기된 질병 용어) 역시 조사 가치가 없습니다.

**진행하려면 필요한 것:**
- DrugBank API를 통한 정식 MOA 데이터 확보 (DG002)
- 식약처(또는 TFDA) 허가사항 PDF 확보 및 경고·금기 파싱 (DG001, Blocking — S1 진입 필수 선행조건)
- 이 예측을 "SIV 치료"가 아닌 "HIV PrEP/치료 전략의 기전적 타당성 근거"로 재해석할지에 대한 연구 방향 재정의
- 실제 인간 적응증(HIV 감염 등) 관점에서 재쿼리하여 임상적으로 의미 있는 예측 재도출 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

