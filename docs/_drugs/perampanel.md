---
layout: default
title: Perampanel
parent: 모델 예측만 (L5)
nav_order: 544
evidence_level: L5
indication_count: 10
---

# Perampanel
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

# Perampanel: 뇌전증(국소발작·전신발작)에서 시각유발 뇌전증(Visual Epilepsy)으로

## 한 문장 요약

Perampanel은 선택적 비경쟁적 AMPA 수용체 길항제로, 해외(미국·EU·일본 등 35개국 이상)에서 국소발작(부분발작) 및 원발성 전신 강직-간대발작 치료에 사용되어 온 항뇌전증제입니다. 다만 국내(한국)에는 아직 허가된 제품이 없습니다.
TxGNN 모델은 **시각유발 뇌전증(Visual Epilepsy)**에 효과가 있을 수 있다고 예측(점수 99.92%)하지만, 현재 확보된 **3건의 임상시험**과 **20편의 문헌**은 모두 일반 뇌전증에 대한 것으로 이 특정 아형(시각 자극 유발 발작)을 직접 검증한 근거는 없습니다. 같은 Evidence Pack에는 총 10건의 TxGNN 예측 적응증이 함께 스코어링되어 있으며, 그중 **뇌전증 중첩증(Status Epilepticus)**이 가장 구체적이고 강한 근거(L2, Proceed with Guardrails)를 보유하고 있습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 국소(부분)발작 및 원발성 전신 강직-간대발작 — 해외 승인 항뇌전증제, 국내 미허가 (문헌 근거 기반) |
| 예측 신규 적응증 | 시각유발 뇌전증 (Visual Epilepsy) |
| TxGNN 예측 점수 | 99.92% |
| 근거 수준 | L4 (독자 평가 — 원 데이터는 미채점 상태였음, 아래 설명 참조) |
| 한국 시판 현황 | ❌ 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Research Question |

> ※ Evidence Pack 내 이 후보의 `scoring` 필드는 "pending"(미채점) 상태였습니다. 아래 임상시험·문헌이 모두 시각유발 뇌전증에 특이적이지 않고 일반 뇌전증 근거인 점을 근거로, 동일 Pack 내 유사 패턴(예: reading seizures, L4/Research Question)에 맞춰 본 보고서에서 독자적으로 L4·Research Question으로 판정했습니다.

---

## 이 예측이 타당한 이유는?

구조화된 MOA 필드는 데이터 갭(DG002, High)으로 비어 있지만, 수집된 문헌들은 일관되게 perampanel의 작용 기전을 설명하고 있습니다. Perampanel은 시냅스 후막의 AMPA(α-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid) 수용체를 선택적·비경쟁적으로 차단하여 글루타메이트 매개 흥분성 신경전달을 억제하는 최초의 항뇌전증제입니다(PMID 21635236, 24559052). 이 기전은 특정 발작 유형에 국한되지 않는 광범위 항발작(broad-spectrum) 작용으로 알려져 있습니다.

시각 자극에 의해 유발되는 반사성 뇌전증(reflex epilepsy)은 대뇌 피질의 과흥분성(cortical hyperexcitability)이 핵심 병태생리로 지목되는데, 이는 AMPA 수용체 과활성화와 기전적으로 연결됩니다. 실제로 같은 Pack 내 다른 반사성 뇌전증 후보인 청각유발발작(audiogenic seizures)의 경우 GEPR(유전적 뇌전증 유발 쥐) 동물모델에서 perampanel이 청각 자극 유발 발작을 억제한다는 직접 증거가 있어(L3), 이론적으로는 시각유발 뇌전증에도 유사한 확장 적용이 가능할 수 있습니다.

다만 시각유발 뇌전증을 **직접** 대상으로 한 임상시험이나 문헌은 확인되지 않았습니다. 아래 근거는 모두 일반 뇌전증(부분발작, 전신발작, 소아 뇌전증 등)에 대한 것이며, 시각/광과민성 자극 유발 발작에 특이적인 데이터는 아닙니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03780907](https://clinicaltrials.gov/study/NCT03780907) | Phase 2 | 완료 | 18 | 난치성 부분/전신발작 환자 대상 E2007(perampanel) 내약성·안전성·약동학 평가 |
| [NCT02900755](https://clinicaltrials.gov/study/NCT02900755) | Phase 4 | 완료 | 30 | 뇌전증 환자에서 perampanel이 인지기능 및 뇌파(EEG)에 미치는 영향 평가 |
| [NCT03653741](https://clinicaltrials.gov/study/NCT03653741) | Phase 4 | 완료 | 12 | Perampanel이 EEG, 체성감각/뇌간청각/**시각유발전위(VEP)** 등 신경생리검사 결과에 미치는 영향 평가 (건강한 지원자 대상, 시각유발 뇌전증 치료 효과 검증은 아님) |

> 시각유발 뇌전증(광과민성 발작 등)을 직접 치료 대상으로 설계된 시험은 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [36206645](https://pubmed.ncbi.nlm.nih.gov/36206645/) | 2022 | 체계적 문헌고찰·메타분석 (RCT) | Seizure | Perampanel의 뇌전증 치료 효과·안전성에 대한 RCT 메타분석 |
| [36878742](https://pubmed.ncbi.nlm.nih.gov/36878742/) | 2023 | 체계적 문헌고찰·메타분석 | Brain & Development | 소아·청소년 뇌전증에서 perampanel의 효과·내약성·안전성 |
| [24559052](https://pubmed.ncbi.nlm.nih.gov/24559052/) | 2014 | 개발 리뷰 | Expert Opin Drug Discov | Perampanel의 발견 및 개발 과정, AMPA 길항 기전 최초 기술 |
| [36150304](https://pubmed.ncbi.nlm.nih.gov/36150304/) | 2022 | 임상시험+실사용 근거 리뷰 | Epilepsy & Behavior | Perampanel 단독요법의 임상시험 및 실사용 데이터 종합 |
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | 진료지침 | Neurology | 미국신경학회(AAN)/미국뇌전증학회 신규 발병 뇌전증 치료 가이드라인 |
| [25878177](https://pubmed.ncbi.nlm.nih.gov/25878177/) | 2015 | Phase 3 통합분석 | Neurology | 효소유도 항뇌전증제 병용 시 perampanel의 효과·안전성 (3건 Phase III 통합) |
| [26111428](https://pubmed.ncbi.nlm.nih.gov/26111428/) | 2015 | 리뷰 (PK/PD) | Expert Opin Drug Metab Toxicol | 부분발작 뇌전증에서 perampanel의 약동학·약력학 평가 |
| [41043235](https://pubmed.ncbi.nlm.nih.gov/41043235/) | 2025 | 전향적 다기관 연구 | Epilepsy & Behavior | Perampanel이 발작 및 수면의 질에 미치는 영향 |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | 체계적 문헌고찰·네트워크 메타분석 | Journal of Neurology | 특발성 전신뇌전증에서 항발작제 비교 |
| [37684052](https://pubmed.ncbi.nlm.nih.gov/37684052/) | 2023 | 리뷰 | BMJ | 임신·수유 중 뇌전증 관리 (perampanel 포함 항발작제 안전성) |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (TFDA 첨부문서상 경고·금기 정보는 데이터 갭 DG001로 분류되어 있으며, Blocking 등급으로 S1 안전성 초평가 진입 전 반드시 보완이 필요합니다.)

---

## 부록: TxGNN 예측 적응증 후보 전체 비교 (총 10건)

같은 Evidence Pack에는 시각유발 뇌전증 외에도 9건의 예측 적응증이 함께 채점되어 있습니다. 의사결정 시 아래 비교표를 함께 고려하는 것을 권장합니다.

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 | 결정 단계 | 권장 결정 | 비고 |
|------|-----------|-----------|----------|----------|----------|------|
| 1 | 시각유발 뇌전증 (Visual Epilepsy) | 99.92% | L4* | S1* | Research Question* | 일반 뇌전증 근거만 존재, 특이적 데이터 없음 |
| 2 | 사고유발발작 (Thinking Seizures) | 99.86% | pending | pending | pending | 미채점 |
| 3 | 섭식유발발작 (Eating Seizures) | 99.86% | L4 | S0 | Hold | 오히려 식욕 저하 부작용 사례 보고, 반대 방향 근거 |
| 4 | 경악유발 뇌전증 (Startle Epilepsy) | 99.86% | L5 | S0 | Hold | 간접 유전학 연구만 존재, 기전 연관성 불명확 |
| **5** | **청각유발발작 (Audiogenic Seizures)** | 99.86% | **L3** | **S1** | **Research Question** | GEPR 동물모델에서 직접적 억제 효과 확인 |
| 6 | 배뇨유발발작 (Micturition-induced Seizures) | 99.86% | pending | pending | pending | 미채점, 일반 뇌전증 근거만 존재 |
| 7 | 성적흥분유발발작 (Orgasm-induced Seizures) | 99.86% | L5 | S0 | Hold | 임상시험·문헌 전무, TxGNN 위양성 가능성 |
| 8 | 읽기유발발작 (Reading Seizures) | 99.83% | L4 | S1 | Research Question | 일반 근거만 존재 (본 보고서 rank 1과 유사 패턴) |
| 9 | 베타-케토티올라제 결핍증 (Beta-ketothiolase Deficiency) | 99.79% | L5 | S0 | Hold | 대사질환-AMPA 기전 연관성 없음, 근거 전무 |
| **10** | **뇌전증 중첩증 (Status Epilepticus)** | 99.77% | **L2** | **S2** | **Proceed with Guardrails** | Phase 2~4 특이적 시험 3건 + 체계적 문헌고찰(Tier1) 포함, 실사용 코호트 다수. **가장 강력한 후보** |

\* rank 1(시각유발 뇌전증)의 근거수준·단계·권장 결정은 원 데이터가 "pending"이었던 것을 본 보고서에서 유사 사례(rank 8)에 근거해 자체 판정한 값입니다.

---

## 결론 및 다음 단계

**결정: Research Question (시각유발 뇌전증) / 별도로 Status Epilepticus는 Proceed with Guardrails 검토 권장**

**사유:**
- 시각유발 뇌전증은 TxGNN 점수가 가장 높지만(99.92%), 이를 직접 뒷받침하는 임상시험·문헌이 없어 현재로서는 가설 단계(Research Question)입니다. AMPA 길항 기전과 반사성 뇌전증 병태생리 간 이론적 연결성은 있으나, 청각유발발작처럼 동물모델 수준의 직접 증거조차 없습니다.
- 반면 같은 Pack 내 뇌전증 중첩증(Status Epilepticus)은 질환 특이적 Phase 2~4 임상시험 3건, 체계적 문헌고찰(Tier 1), 다수 코호트 연구를 갖추고 있어 실질적으로 가장 진행 가능성이 높은 후보입니다.

**진행하려면 필요한 것:**
- **DG001 (Blocking)** 해소: TFDA 첨부문서 경고·금기사항 확보 — S1 안전성 초평가 진입의 전제조건
- **DG002 (High)** 해소: DrugBank API를 통한 구조화된 MOA 데이터 확보
- 시각유발/광과민성 뇌전증 환자를 대상으로 한 전향적 관찰연구 또는 최소한 photic stimulation 동물모델 데이터 확보
- 국내 미출시 상태이므로, 반려동물... 아닌 재창출 개발 시 별도의 국내 허가 경로(신약 또는 신규 적응증 추가) 검토 필요
- 향후 자원 배분 시 시각유발 뇌전증보다 근거 수준이 높은 뇌전증 중첩증(rank 10) 트랙을 우선 검토 권장
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

