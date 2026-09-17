---
layout: default
title: Cefoperazone
parent: 높은 근거 (L1-L2)
nav_order: 182
evidence_level: L2
indication_count: 10
---

# Cefoperazone
{: .fs-9 }

근거 수준: **L2** | 예측 적응증: **10** 건
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

# Cefoperazone: 항균 치료제에서 폐렴 적응증 근거 재확인으로

> **참고**: TxGNN이 제시한 예측 적응증 후보는 총 10건입니다. 1순위(경화성 담관염, sclerosing cholangitis)를 포함해 6건은 근거 수준 L5(임상시험·문헌 전무)이며, 평가 근거(`repurposing_rationale.mechanistic_link`) 자체가 "기전 관련성 없음", "KG 잡음(noise)으로 판단"이라고 명시하고 있어 보고서의 주 후보로 부적합합니다. 이에 반해 **폐렴(Pneumonia, 3순위)**은 임상시험 2건·문헌 20편이 확보되어 있고 근거 수준 L2, 권장 단계 S3(Proceed with Guardrails)로 유일하게 실질적 근거를 갖춘 후보이므로, 본 보고서는 이를 중심으로 작성합니다.

## 한 문장 요약

Cefoperazone은 그람음성균을 포함한 광범위 항균 스펙트럼을 가진 3세대 세팔로스포린계 항생제입니다. TxGNN 모델이 예측한 다수 후보 중 실제 근거가 확인되는 적응증은 **폐렴(Pneumonia)**이며, 현재 **임상시험 2건**과 **문헌 20편**이 이를 뒷받침합니다. 다만 이는 완전히 새로운 질환으로의 "재창출"이라기보다, 기존 항균 기전이 적용되는 적응증(원내획득폐렴 등)에 대한 근거 재확인에 가깝습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 명시적 허가 기록 없음 (광범위 항생제로 그람음성균 감염 치료에 사용되는 약리학적 배경) |
| 예측 신규 적응증 | 폐렴 (Pneumonia) |
| TxGNN 예측 점수 | 99.93% |
| 근거 수준 | L2 |
| 한국 시판 현황 | ✗ 미판매 (허가 0건) |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 확보되지 않았습니다([Data Gap], DG002). 다만 각 예측 후보의 근거 서술에 따르면, Cefoperazone은 세균 세포벽 합성을 억제(penicillin-binding proteins 결합)하는 3세대 세팔로스포린으로, 녹농균을 포함한 다수의 그람음성균 및 일부 그람양성균에 광범위 살균 활성을 가집니다.

폐렴은 이러한 항균 스펙트럼이 직접 적용되는 핵심 영역입니다. 원내획득폐렴(HAP)·인공호흡기관련폐렴(VAP)의 주요 원인균(폐렴막대균, 아시네토박터균 등)에 대해 Cefoperazone/Sulbactam 병용이 다수 비교임상시험에서 평가되었으며, 이는 "신규 적응증 발굴"이라기보다 **기존 항균 적응증 범위 내 근거를 확인**하는 성격입니다.

반면 1순위(경화성 담관염), 4·5순위(희귀 유전성 증후군), 6순위(통풍), 9·10순위(중이염, IgG4 관련 경화성 담관염)는 자가면역·유전 질환 또는 항생제 기전과 무관한 질환으로, 근거 텍스트에서도 "기전 관련성 없음", "지식그래프 잡음"으로 명시되어 있어 제외했습니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01280461](https://clinicaltrials.gov/study/NCT01280461) | Phase 3 (등록상 N/A) | 상태 불명 | 142 | Cefoperazone/Sulbactam vs Cefepime, 원내획득폐렴(HAP) 및 의료관련폐렴(HCAP) 치료 효능·안전성 비교 무작위 공개표지 시험. 관련성 등급 A(직접 증거). |
| [NCT02060149](https://clinicaltrials.gov/study/NCT02060149) | Phase 1/2 | 상태 불명 | 90 | 광범위약제내성 아시네토박터균 폐렴에서 Cefoperazone-Sulbactam+Minocycline 병용요법 중 알칼리 용액 분무 병용 효과 평가. 관련성 등급 C(간접 증거, 주 개입약물 아님). |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [34168466](https://pubmed.ncbi.nlm.nih.gov/34168466/) | 2021 | RCT (Tier 1) | Infection and Drug Resistance | Cefoperazone-Sulbactam vs Piperacillin-Tazobactam, HAP/VAP 치료 효능 비교 |
| [31138577](https://pubmed.ncbi.nlm.nih.gov/31138577/) | 2019 | RCT (Tier 1) | Antimicrob Agents Chemother | Cefoperazone-Sulbactam vs Cefepime, HAP/HCAP 비열등성 무작위 시험 |
| [6456894](https://pubmed.ncbi.nlm.nih.gov/6456894/) | 1981 | RCT (Tier 2) | Drugs | 폐렴 15례·신우신염 15례 대상 초기 임상시험, 전 균주 감수성 확인 |
| [1643821](https://pubmed.ncbi.nlm.nih.gov/1643821/) | 1992 | RCT | Diagn Microbiol Infect Dis | Cefoperazone vs Ceftriaxone 단독요법, 원내폐렴 비교(치료 성공률 80% vs 70%) |
| [34871744](https://pubmed.ncbi.nlm.nih.gov/34871744/) | 2022 | 비교연구 | Int J Antimicrob Agents | 고령 환자 폐렴에서 Cefoperazone-Sulbactam vs Piperacillin-Tazobactam 효과 비교 |
| [24726664](https://pubmed.ncbi.nlm.nih.gov/24726664/) | 2014 | Cohort (Tier 2) | Int J Infect Dis | 카바페넴내성 아시네토박터균 원내폐렴 후향분석 및 Cefoperazone/Sulbactam in vitro 효과 |
| [29319497](https://pubmed.ncbi.nlm.nih.gov/29319497/) | 2018 | 비교연구 | Int J Clin Pharmacol Ther | 광범위약제내성 아시네토박터균 VAP에서 고용량 Cefoperazone-Sulbactam+Tigecycline 병용 효과 |
| [17120738](https://pubmed.ncbi.nlm.nih.gov/17120738/) | 2006 | 비교연구 | J Huazhong Univ Sci Technol | 지역사회획득폐렴에서 Moxifloxacin vs Cefoperazone+Azithromycin 효능·안전성 비교 |
| [6391668](https://pubmed.ncbi.nlm.nih.gov/6391668/) | 1984 | 다기관 임상시험 | Clinical Therapeutics | 일본·한국·대만 476례 대상 Cefoperazone 호흡기감염 다기관 시험, 폐렴 78.9% 만족 반응 |
| [2671141](https://pubmed.ncbi.nlm.nih.gov/2671141/) | 1989 | Review (Tier 3) | Infect Dis Clin North Am | 3세대 세팔로스포린 계열 개관, Cefoperazone의 항균 스펙트럼 기술 |

※ PMID [35685727](https://pubmed.ncbi.nlm.nih.gov/35685727/)은 이후 철회(Retraction, PMID [38125170](https://pubmed.ncbi.nlm.nih.gov/38125170/))되어 근거 목록에서 제외했습니다.

---

## 한국 시판 정보

현재 이 지역에 허가된 Cefoperazone 제품이 없습니다 (시판 현황: 미판매, 허가 0건). 신규 진입 시 별도의 허가 절차와 현지 안전성 자료 확보가 필요합니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (주요 경고·금기·약물상호작용 자료 미확보 — DG001, Blocking 등급)

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
Cefoperazone-Sulbactam의 원내획득폐렴/인공호흡기관련폐렴 치료 효능을 뒷받침하는 Phase 3급 무작위 대조시험(RCT Tier 1) 2건을 포함해 총 10편 이상의 비교임상 근거가 확보되어 있습니다. 다만 이는 신규 적응증이 아닌 기존 항균 기전의 적용 범위 확인이며, 현재 이 지역에서 미판매 상태이고 안전성 라벨 정보가 Blocking 수준으로 결여되어 있어 즉시 진행보다는 안전장치를 갖춘 진행이 적절합니다.

**진행하려면 필요한 것:**
- TFDA(또는 현지 규제기관) 공식 허가사항의 경고·금기 정보 확보 (DG001, Blocking)
- DrugBank 등에서 상세 작용기전(MOA) 데이터 확보 (DG002)
- 약물상호작용(DDI) 자료 보강 (현재 조회 결과 없음)
- 신규 허가 신청 시 요구되는 현지 임상/안전성 자료 검토

**참고(2차 후보):** 기관지염(Bronchitis, L2/S2, Research Question)과 수막구균 감염(L3/S1, Research Question)도 제한적이나마 실질 근거를 가진 후보로 확인되며, 향후 추가 조사 가치가 있습니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

