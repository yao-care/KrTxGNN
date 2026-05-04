---
layout: default
title: Alpha-Tocopherol Acetate
parent: 僅模型預測 (L5)
nav_order: 44
evidence_level: L5
indication_count: 10
---

# Alpha-Tocopherol Acetate
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

# Alpha-Tocopherol Acetate: 비타민 E 보충제에서 당뇨병성 망막병증으로

## 한 문장 요약

Alpha-Tocopherol Acetate(비타민 E 아세테이트)는 지용성 항산화제로, 세포막 지질 과산화 방지 및 비타민 E 결핍 예방에 활용됩니다. TxGNN 모델은 **10가지 새로운 적응증**을 예측했으며, 그 중 **당뇨병성 망막병증(Diabetic Retinopathy)**이 **2건의 임상시험**과 **20편의 문헌**으로 가장 강력한 근거를 보유합니다. 피질성 백내장(9편 문헌, L3)과 당뇨병성 백내장(11편 문헌, L4)도 추가 연구 가치가 있는 후보로 확인됩니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 없음 (항산화 보충제로 활용) |
| 최우선 예측 적응증 | 당뇨병성 망막병증 (Diabetic Retinopathy) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L2 |
| 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 전체 예측 적응증 요약

본 보고서는 10개 적응증에 대한 다적응증(Multi-Indication) 평가입니다. 이하 본문은 근거가 가장 충분한 **당뇨병성 망막병증**을 중심으로 작성됩니다.

| 순위 | 적응증 | TxGNN 점수 | 근거 수준 | 임상시험 | 문헌 | 권장 결정 |
|:----:|--------|:---------:|:-------:|:------:|:----:|:-------:|
| 1 | Drug-Induced Osteoporosis | 99.994% | L5 | 0 | 0 | Hold |
| 2 | Diabetic Cataract | 99.993% | L4 | 0 | 11 | Research Question |
| 3 | Craniostenosis Cataract | 99.992% | L5 | 0 | 0 | Hold |
| 4 | Mature Cataract | 99.992% | L5 | 0 | 0 | Hold |
| 5 | Immature Cataract | 99.992% | L4 | 0 | 1 | Research Question |
| 6 | T2DM-Associated Cataract | 99.992% | L5 | 0 | 0 | Hold |
| 7 | Tetanic Cataract | 99.992% | L5 | 0 | 0 | Hold |
| 8 | Nuclear Senile Cataract | 99.991% | L5 | 0 | 0 | Hold |
| 9 | Cortical Cataract | 99.991% | L3 | 0 | 9 | Research Question |
| **10** | **Diabetic Retinopathy** | **99.991%** | **L2** | **2** | **20** | **Proceed with Guardrails** |

> **Hold 사유 요약**: 크라니오스테노시스 백내장(유전/발달 기전), 성숙 백내장(항산화 개입 시기 초과), T2DM 관련 백내장(독립 근거 없음), 파상풍성 백내장(전해질 기전, 산화 스트레스 비관련), 핵성 노인성 백내장(갈색화 기전 중심, 산화 관련성 낮음)은 기전적 타당성 및 근거 부재로 Hold 판정됩니다.

---

## 이 예측이 타당한 이유는?

Alpha-Tocopherol Acetate는 비타민 E의 안정화된 에스테르 형태로, 체내에서 가수분해 후 활성형인 알파-토코페롤로 전환됩니다. 알파-토코페롤은 세포막의 지질 이중층에 특이적으로 분포하는 지용성 항산화제로, 자유 라디칼 연쇄 반응을 차단하고 지질 과산화를 억제하는 것이 핵심 작용입니다. DrugBank MOA 데이터는 현재 미확보 상태이나(DG002), 광범위한 문헌을 통해 항산화 기전이 잘 정립되어 있습니다.

당뇨병성 망막병증의 발병 핵심은 **고혈당 유발 산화 스트레스**입니다. 지속적인 고혈당은 다이아실글리세롤(DAG) 축적을 통해 단백질 키나아제 C(PKC)를 과활성화시키고, 망막 혈관 기능 장애 및 주위세포(pericyte) 소실을 거쳐 최종적으로 신생혈관 형성과 시력 손상으로 이어집니다. Alpha-Tocopherol은 ① PKC 과활성화 억제를 통한 망막 혈류 정상화(PMID 9523029), ② 적혈구막 지질 과산화 스트레스 감소 및 혈액 점도 개선(PMID 9609359), ③ 미토콘드리아 기능 보호를 통한 망막 혈관내피세포 세포자멸사 억제라는 세 가지 독립적 경로를 통해 이 병인 과정에 직접 개입합니다.

임상적 타당성은 두 건의 완료된 시험으로 뒷받침됩니다. Phase 3 시험(NCT03702374, n=132, 12개월)은 다양한 병기의 당뇨병성 망막병증 환자에서 조합 항산화 요법의 효과를 검증했으며, Phase 2 시험(NCT04071977, n=40)은 증식성 망막병증 환자의 안구 내 국소 산화 스트레스 생물지표를 직접 측정했습니다. 두 시험 모두 Alpha-Tocopherol을 포함한 조합 요법으로 설계되어 단일 성분 기여도 분리가 필요하나, 기전 검증의 측면에서 중요한 임상 근거를 제공합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|:--------:|---------|
| [NCT03702374](https://clinicaltrials.gov/study/NCT03702374) | Phase 3 | 완료 | 132 | 중등도~증식성 당뇨병성 망막병증 환자에서 조합 항산화 요법(Alpha-Tocopherol 포함) 12개월 투여가 산화 스트레스 및 미토콘드리아 기능 장애 지표에 미치는 영향 평가; 위약 대조, 다병기 설계 |
| [NCT04071977](https://clinicaltrials.gov/study/NCT04071977) | Phase 2 | 완료 | 40 | 증식성 당뇨병성 망막병증으로 유리체 절제술 예정 환자에서 2개월 조합 항산화 요법이 방수 및 유리체 내 국소 산화 스트레스 생물지표 수준에 미치는 효과; Phase 3의 기전 전임상 근거 제공 |

---

## 문헌 근거

### 당뇨병성 망막병증 (Diabetic Retinopathy)

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|:---:|------|------|---------|
| [19900709](https://pubmed.ncbi.nlm.nih.gov/19900709/) | 2010 | Systematic Review | Ophthalmology | 당뇨병성 망막병증과 비타민 E·C·마그네슘 섭취/혈중 농도의 연관성 체계적 고찰; 항산화제의 병인적 개입 가능성 검토 |
| [12882944](https://pubmed.ncbi.nlm.nih.gov/12882944/) | 2003 | Cross-sectional | Am J Epidemiology | NHANES III(n=998, 2형 당뇨): 혈청 알파-토코페롤 수준 저하와 망막병증 유병률 증가의 연관성; 대규모 국가 표본 |
| [9609359](https://pubmed.ncbi.nlm.nih.gov/9609359/) | 1998 | Clinical Study | Diabetic Medicine | T2DM 망막병증 환자(n=13)에서 알파-토코페롤 니코티네이트 3개월 투여 후 혈액 점도 및 적혈구막 지질 과산화 유의하게 감소 |
| [8407170](https://pubmed.ncbi.nlm.nih.gov/8407170/) | 1993 | Observational | Int J Vitamin Nutr Res | IDDM 환자(n=60)에서 망막병증·신증 동반 시 혈장 알파-토코페롤 농도 유의하게 감소; 미세혈관 합병증과의 직접 연관성 |
| [9695797](https://pubmed.ncbi.nlm.nih.gov/9695797/) | 1998 | Mechanistic Review | Prog Retinal Eye Res | 알도오스 환원효소 경로 및 자유 라디칼 기전과 당뇨 합병증의 연결고리; Alpha-Tocopherol 기전적 개입 지점 제시 |
| [16842139](https://pubmed.ncbi.nlm.nih.gov/16842139/) | 2006 | Narrative Review | Curr Vascular Pharmacol | 당뇨 혈관 합병증(망막병증 포함) 발병에서 산화 스트레스, 고혈당 단백 당화, 내피 기능 장애의 복합적 역할 고찰 |
| [9523029](https://pubmed.ncbi.nlm.nih.gov/9523029/) | 1998 | Animal Study | BioFactors | 당뇨 쥐에서 d-알파-토코페롤이 PKC 과활성화 및 DAG 수준을 억제하고 비정상 망막 혈류를 정상화 (핵심 기전 연구) |
| [11473058](https://pubmed.ncbi.nlm.nih.gov/11473058/) | 2001 | Animal Study | Diabetes | 당뇨 및 갈락토스혈증 쥐에서 비타민 C+E 조합 장기 투여가 망막병증 초기 혈관 변화(무세포 모세혈관, 주위세포 소실) 억제 |
| [35715832](https://pubmed.ncbi.nlm.nih.gov/35715832/) | 2022 | Animal Study | Int J Retina Vitreous | 당뇨 모델 쥐(alloxan 유발)에서 레티놀+알파-토코페롤 투여가 광수용체 및 망막 신경절세포 세포자멸사를 유의하게 억제 |
| [14703729](https://pubmed.ncbi.nlm.nih.gov/14703729/) | 2003 | Animal Study | Free Radical Research | 당뇨 쥐 망막에서 NF-κB 산화 전사 인자 과활성화 확인; 다중 항산화제 식이가 NF-κB를 억제하고 망막병증 발생 지연 |

---

### 피질성 백내장 (Cortical Cataract) — L3 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|:---:|------|------|---------|
| [9527321](https://pubmed.ncbi.nlm.nih.gov/9527321/) | 1997 | RCT | Acta Ophthalmol Scand | ATBC Study 이차 종점: 핀란드 남성 흡연자에서 알파-토코페롤 장기 보충과 노인성 백내장 유병률·중증도 관련성 분석 |
| [8363468](https://pubmed.ncbi.nlm.nih.gov/8363468/) | 1993 | RCT | Arch Ophthalmol | Linxian 영양 개입 RCT(n=3,249): 비타민/미네랄 보충이 노인성 백내장(피질성 포함) 발생 위험에 미치는 영향 |
| [8512984](https://pubmed.ncbi.nlm.nih.gov/8512984/) | 1993 | Prospective Cohort | Epidemiology | Baltimore 노화 종단 연구(n=660): 혈장 알파-토코페롤 높을수록 피질성 백내장 위험 감소 경향; 핵성과 분리 분석 |
| [7843899](https://pubmed.ncbi.nlm.nih.gov/7843899/) | 1995 | Cross-sectional | Invest Ophthalmol Vis Sci | 혈청 토코페롤 수준과 핵성/피질성 혼탁 중증도 간 역방향 관련성; 피질성 백내장에서 특히 유의한 결과 |
| [10749028](https://pubmed.ncbi.nlm.nih.gov/10749028/) | 1999 | Clinical Study | Ann Nutr Metab | 미성숙 노인성 백내장(피질성 n=25, 핵성 n=25)에서 비타민 E 30일 투여 후 GSH↑, MDA↓, 수정체 내 비타민 E 농도↑ |
| [10550792](https://pubmed.ncbi.nlm.nih.gov/10550792/) | 1999 | Human Tissue Study | Current Eye Research | 인체 백내장 수정체 층별(외피질/상피 vs. 내피질/핵) 알파-토코페롤 농도 차이 확인; 분포 특성이 피질성 보호와 일치 |
| [21620831](https://pubmed.ncbi.nlm.nih.gov/21620831/) | 2011 | Animal Study | Exp Eye Res | 쥐 UV 유발 피질성 백내장 모델에서 알파-토코페롤의 명확한 용량-반응 보호 관계(5~100 IU/day) 확립 |

---

### 당뇨병성 백내장 (Diabetic Cataract) — L4 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|:---:|------|------|---------|
| [9799882](https://pubmed.ncbi.nlm.nih.gov/9799882/) | 1998 | RCT | J Epidemiol Community Health | ATBC Study 이차 분석: 핀란드 남성 흡연자에서 알파-토코페롤 보충이 백내장 수술 발생률에 유의한 영향 없음 (부정적 결과 포함, 편향 주의) |
| [1486302](https://pubmed.ncbi.nlm.nih.gov/1486302/) | 1992 | Case-control | BMJ | 혈청 알파-토코페롤·베타카로틴·레티놀·셀레늄 농도와 말기 백내장 위험의 역방향 연관성 |
| [9695797](https://pubmed.ncbi.nlm.nih.gov/9695797/) | 1998 | Mechanistic Review | Prog Retinal Eye Res | 알도오스 환원효소 경로를 통한 당뇨 합병증(당뇨 백내장 포함) 발생 기전; Alpha-Tocopherol이 직접 개입하기 어려운 경로도 포함 |
| [2629605](https://pubmed.ncbi.nlm.nih.gov/2629605/) | 1989 | Animal Study | Ann NY Acad Sci | 당뇨 쥐 피질성 백내장 모델에서 비타민 E 아세테이트·숙시네이트의 백내장 형성 및 감마-크리스탈린 누출 억제 |
| [12919321](https://pubmed.ncbi.nlm.nih.gov/12919321/) | 2003 | In Vitro | Eur J Biochem | LDL의 포도당 당화/당산화 과정과 당뇨 합병증(백내장 포함) 발생 기전; 산화적 경로의 역할 재확인 |

---

### 미성숙 백내장 (Immature Cataract) — L4 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|:---:|------|------|---------|
| [10749028](https://pubmed.ncbi.nlm.nih.gov/10749028/) | 1999 | Clinical Study | Ann Nutr Metab | 미성숙 노인성 백내장 환자(n=50)에서 비타민 E 30일 투여 후 산화 스트레스 지표 및 수정체 내 비타민 E 농도 개선; 현재 유일한 직접 인체 연구 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails (당뇨병성 망막병증)**

**사유:**
Phase 3 완료 임상시험(NCT03702374, n=132)을 포함한 2건의 완료된 임상시험과 20편의 문헌이 당뇨병성 망막병증에 대한 기전적 타당성을 뒷받침합니다. PKC 억제, 망막 혈류 개선, 미토콘드리아 보호라는 다중 독립 경로가 확립되어 있고, 오랜 기간 사용된 보충제로서 일반적 안전성 프로파일이 잘 알려져 있어 L2 근거 수준으로 평가됩니다.

**진행하려면 필요한 것:**
- Alpha-Tocopherol **단독 투여** 효과를 평가하는 무작위 대조 임상시험 설계 (조합 요법 내 단일 성분 기여도 분리 필수)
- 구체적인 작용 기전(MOA) 데이터 확보를 위한 DrugBank API 재조회 (DG002 해결)
- TFDA 허가 경고/금기 정보 취득 및 안전성 평가 완료 (DG001 해결)
- 당뇨병성 망막병증 병기별(비증식성·증식성) 최적 투여 용량·기간·경로 설정
- 피질성 백내장 및 당뇨병성 백내장에 대한 독립 연구 질문 수립 (별도 탐색 단계 권장)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

