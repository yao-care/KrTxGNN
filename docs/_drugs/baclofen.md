---
layout: default
title: Baclofen
parent: 僅模型預測 (L5)
nav_order: 119
evidence_level: L5
indication_count: 2
---

# Baclofen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Baclofen: 근육 경직에서 주의력결핍 과잉행동장애·니코틴 의존증으로

---

## 한 문장 요약

Baclofen은 GABA-B 수용체 작용제로, 전 세계적으로 근육 경직(Spasticity) 치료에 사용되는 약물입니다 (단, 한국 미허가). TxGNN 모델은 **주의력결핍 과잉행동장애(ADHD)** (예측 점수 99.32%)와 **니코틴 의존증(Nicotine Dependence)** (예측 점수 99.19%) 두 가지 새로운 적응증에 효과가 있을 수 있다고 예측하며, ADHD에 대해서는 **10편의 문헌**, 니코틴 의존증에 대해서는 **3건의 임상시험**과 **20편의 문헌**이 이를 뒷받침합니다.

---

## 빠른 개요

### 예측 적응증 1: 주의력결핍 과잉행동장애 (ADHD)

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 미허가 약물 (해외: 근육 경직 치료) |
| 예측 신규 적응증 | 주의력결핍 과잉행동장애 (ADHD) |
| TxGNN 예측 점수 | 99.32% |
| 근거 수준 | L4 (전임상·기전 연구) |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

### 예측 적응증 2: 니코틴 의존증 (Nicotine Dependence)

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 미허가 약물 (해외: 근육 경직 치료) |
| 예측 신규 적응증 | 니코틴 의존증 (Nicotine Dependence) |
| TxGNN 예측 점수 | 99.19% |
| 근거 수준 | L2 (Phase 2 임상시험 완료) |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

**공통 기전: GABA-B 수용체 작용**

Baclofen은 GABA-B 수용체의 선택적 작용제입니다. GABA-B 수용체 활성화는 중추신경계 전반에 걸쳐 억제성 신경전달을 강화하며, 도파민·노르에피네프린·글루타메이트 등 여러 신경전달물질 시스템과 교차 상호작용합니다. 이 공통된 기전적 기반이 ADHD와 니코틴 의존증 두 적응증 모두에 대한 재창출 가능성을 이론적으로 뒷받침합니다. 다만, 상세 작용 기전(MOA) 데이터는 현재 확인되지 않아 아래 설명은 문헌 및 동물 연구 기반의 추론입니다.

**주의력결핍 과잉행동장애(ADHD)와의 연관성**

GABA-B 수용체 활성화는 전전두엽 피질 및 중뇌변연계에서 도파민·노르에피네프린 분비를 조절하여, 이론적으로 충동 조절 및 주의력 조절 기능에 영향을 미칠 수 있습니다. 자발성 고혈압 쥐(SHR) 동물 모델—ADHD의 대용 모델로 널리 사용—에서 GABA 작용제가 피질·해마 EEG 패턴을 변화시킨다는 보고가 있습니다. 그러나 이 기전적 연결은 여전히 추론 단계이며, 인체를 대상으로 한 직접 임상 데이터가 전무합니다.

**니코틴 의존증과의 연관성**

Baclofen은 복측 피개 영역(VTA)에서 측좌핵(NAc)으로의 도파민 투사를 억제하여 니코틴의 보상 효과를 직접적으로 감소시킵니다. 동시에 시냅스 전 GABA-B 수용체를 통한 글루타메이트 분비 감소로, 니코틴 관련 단서(cue)에 의한 갈망과 재발 행동을 억제합니다. 이 기전은 알코올·코카인·오피오이드 의존 치료에서도 공통적으로 연구되어 있어 범용성이 높으며, 쥐 자가 투약(self-administration) 및 재발(reinstatement) 모델에서 반복 검증되었습니다.

---

## 임상시험 근거

### 예측 적응증 1: 주의력결핍 과잉행동장애 (ADHD)

현재 관련 임상시험 등록이 없습니다.

### 예측 적응증 2: 니코틴 의존증 (Nicotine Dependence)

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01821560](https://clinicaltrials.gov/study/NCT01821560) | Phase 2 | 완료 | 44 | 흡연자에서 fMRI를 활용하여 흡연 단서 노출 시 Baclofen의 뇌 기능·행동 반응 평가; 도파민 관련 유전자 다형성 분석 포함. 현재 존재하는 가장 신뢰도 높은 임상 데이터 |
| [NCT00257894](https://clinicaltrials.gov/study/NCT00257894) | Phase 2 | 조기 종료 | 41 | 중등~중증 흡연자에서 Baclofen의 흡연 충동·금단 증상·강화 효과 감소 여부 평가. 41명 모집 후 조기 종료; 부분 데이터 존재 가능성, 종료 원인 미확인 |
| [NCT01228994](https://clinicaltrials.gov/study/NCT01228994) | Phase 2 | 조기 종료 | 6 | 니코틴 의존의 GABAergic 가설 직접 검증; Baclofen의 금연 효능 위약 비교 평가. 6명 모집 후 조기 종료, 결론 도출 불가 |

---

## 문헌 근거

### 예측 적응증 1: 주의력결핍 과잉행동장애 (ADHD)

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|------|------|------|---------|
| [10342599](https://pubmed.ncbi.nlm.nih.gov/10342599/) | 1999 | Clinical Review | J Child Neurology | 450명 틱/Tourette 환자에 Baclofen·보툴리눔 독소 A형 치료; Yale 전체 틱 중증도 척도로 증상 평가 |
| [21300040](https://pubmed.ncbi.nlm.nih.gov/21300040/) | 2011 | Animal Study | Brain Research | SHR 모델(ADHD 대용)에서 GABA 작용제를 포함한 신경전달물질 작용제의 피질·해마 EEG 효과 분석 |
| [24062084](https://pubmed.ncbi.nlm.nih.gov/24062084/) | 2014 | Animal Study | Psychopharmacology | 복측 해마의 α2A 수용체 자극이 충동적 의사결정 감소에 기여; ADHD 관련 신경회로 탐색 |
| [24496320](https://pubmed.ncbi.nlm.nih.gov/24496320/) | 2014 | Animal Study | Neuropsychopharmacology | 전측 대상 피질·기저외측 편도체가 인지적 노력 의사결정에 미치는 역할 규명; ADHD·우울·조현병 관련 |
| [24103016](https://pubmed.ncbi.nlm.nih.gov/24103016/) | 2013 | Animal Study | Eur J Neuroscience | 습상핵 기능이 쥐의 사회적 놀이 행동에 필수적; 모노아민계 신경전달 조절과의 연관성 |
| [35345730](https://pubmed.ncbi.nlm.nih.gov/35345730/) | 2022 | Systematic Review | Cureus | Tourette 증후군 틱 치료에서 행동 중재, 항정신병약, 알파 효능제 효능 비교 평가; ADHD 동반 질환 포함 |
| [24295630](https://pubmed.ncbi.nlm.nih.gov/24295630/) | 2013 | Review | Int Rev Neurobiology | Tourette 증후군 신흥 치료 전략 검토; ADHD·강박장애 동반 증상 관리 포함 |
| [26366961](https://pubmed.ncbi.nlm.nih.gov/26366961/) | 2015 | Narrative Review | Clinical Neuropharmacology | 자폐 스펙트럼 장애 아동·청소년에서 기분 안정제 사용 현황; 주의력 결핍 동반 증상 포함 |
| [11393328](https://pubmed.ncbi.nlm.nih.gov/11393328/) | 2001 | Clinical Review | Paediatric Drugs | Tourette 증후군 임상 특성 및 관리 전략; ADHD 동반 질환 및 1차 약물 선택 기준 |
| [30122296](https://pubmed.ncbi.nlm.nih.gov/30122296/) | 2019 | Clinical Commentary | L'Encephale | 성인 ADHD에서 메틸페니데이트 허가 외 처방의 감독 체계 사례; 정신과 허가 외 처방 현황 |

### 예측 적응증 2: 니코틴 의존증 (Nicotine Dependence)

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|------|------|------|---------|
| [25868070](https://pubmed.ncbi.nlm.nih.gov/25868070/) | 2015 | Conference Abstract (Clinical) | Neuropsychopharmacology | 알코올·니코틴 동반 의존 치료에 Baclofen의 이중맹검 위약 대조 무작위 임상시험 결과 발표 |
| [24553576](https://pubmed.ncbi.nlm.nih.gov/24553576/) | 2014 | Animal Study | Psychopharmacology | 쥐에서 Baclofen이 니코틴 보상 특성 및 금단 증상 발현을 유의하게 감쇠시킴 확인 |
| [19250803](https://pubmed.ncbi.nlm.nih.gov/19250803/) | 2009 | Animal Study | Eur Neuropsychopharmacology | 소거/재발 모델에서 Baclofen이 약물 유발 니코틴 추구 행동 재발 및 조건 장소 선호 억제 |
| [18682277](https://pubmed.ncbi.nlm.nih.gov/18682277/) | 2008 | Animal Study | Neuroscience Letters | 쥐에서 Baclofen의 니코틴 유발 조건 장소 선호 및 변별 자극 효과에 대한 선택적 감쇠 평가 |
| [23500668](https://pubmed.ncbi.nlm.nih.gov/23500668/) | 2013 | Animal Study | Progress Neuro-Psychopharmacology | Baclofen이 니코틴 금단 증후군 발현 예방 및 α4β2 니코틴 수용체 밀도 변화 억제 확인 |
| [38555115](https://pubmed.ncbi.nlm.nih.gov/38555115/) | 2024 | Review (Drug Repurposing) | Int Rev Neurobiology | 알코올 사용 장애 약물 재창출 종합 검토; 프랑스·유럽의 Baclofen 승인 현황 및 임상 근거 포함 |
| [24971600](https://pubmed.ncbi.nlm.nih.gov/24971600/) | 2015 | Review | Neuropharmacology | GABA-B 수용체 양성 알로스테릭 조절제의 물질 사용 장애 치료 잠재성; Baclofen 대비 장점 비교 |
| [17338593](https://pubmed.ncbi.nlm.nih.gov/17338593/) | 2007 | Review | CNS Drugs | 이중 물질 남용·의존에 대한 약물 치료 전략; 니코틴·알코올 동반 의존에서 Baclofen 검토 |
| [29250815](https://pubmed.ncbi.nlm.nih.gov/29250815/) | 2018 | Review | Pharmacotherapy | 금연 약물 치료 현황 및 신흥 접근법; 현행 치료의 한계와 Baclofen의 보조 역할 검토 |
| [24654737](https://pubmed.ncbi.nlm.nih.gov/24654737/) | 2014 | Review | Expert Opin Emerging Drugs | 니코틴 의존 치료 신약 2014년 업데이트; 기전·임상 근거 기반 Baclofen 포함 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

### 예측 적응증 1: 주의력결핍 과잉행동장애 (ADHD)

**결정: Hold**

**사유:**
ADHD에 대한 Baclofen의 등록 임상시험이 전무하며, 현재 가용 문헌은 대부분 SHR 동물 모델을 이용한 EEG 연구이거나 Tourette 증후군 관련 간접 문헌으로 구성되어 있습니다. 기전적 연결이 추론 단계에 머물러 있어 직접 임상 근거 생산이 선행되어야 합니다.

**진행하려면 필요한 것:**
- ADHD 동물 모델에서 Baclofen의 직접적 행동 효과를 검증한 표적 전임상 연구
- 소규모 탐색적 임상 연구(Phase 1b/2a) 설계를 위한 프로토콜 개발
- 상세 MOA 데이터 확보 (DrugBank API 조회 필요)
- 한국 내 임상시험을 위한 규제 전략 수립 (미허가 약물 대상)

---

### 예측 적응증 2: 니코틴 의존증 (Nicotine Dependence)

**결정: Proceed with Guardrails**

**사유:**
1건의 완료된 Phase 2 임상시험(NCT01821560, n=44)과 다수의 동물 연구가 Baclofen의 니코틴 의존 치료 가능성을 지지합니다. GABA-B 수용체를 통한 도파민·글루타메이트 조절 기전은 동물 연구에서 반복 검증되었으며, Baclofen은 프랑스·유럽에서 알코올 사용 장애 치료에 이미 허가되어 광범위한 임상 안전성 축적 데이터가 존재합니다.

**진행하려면 필요한 것:**
- NCT01821560 완료 시험의 발표 결과 전문 검토 (fMRI 및 금연율 결과 포함)
- 조기 종료된 두 시험(NCT00257894, NCT01228994)의 종료 사유 확인 (안전성 문제 vs. 운영상 이유 구별)
- 최적 용량 범위 설정을 위한 용량-반응 데이터 확보
- 한국 내 임상시험 가능성 검토 및 규제 당국(식약처) 사전 협의 계획 수립
- 허가사항 기반 상세 안전성 프로파일 문서화 (TFDA 仿單 또는 유사 승인 국가 허가서 확보)

---

> **⚠️ 면책 고지:** 본 보고서는 연구 참고 목적으로만 작성되었으며, 의료 처방 또는 치료 결정을 위한 근거로 사용될 수 없습니다. 모든 재창출 후보는 임상 검증을 거쳐야 하며, 본 예측 결과의 임상 적용은 관련 법령 및 규제 당국의 허가 절차를 반드시 준수해야 합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

