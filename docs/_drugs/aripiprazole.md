---
layout: default
title: Aripiprazole
parent: 모델 예측만 (L5)
nav_order: 85
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Aripiprazole: 예측 신규 적응증 주요 우울장애 (major affective disorder) (근거 수준 L5). 기존 적응증: 허가 적응증 본문이 링크 형태로만 제공되어 확인 불가 (허가사항 참조 필요)"
monitor_inn: "ARIPIPRAZOLE"
predicted_indications: ["gaze palsy, familial horizontal, with progressive scoliosis", "asperger syndrome, susceptibility to", "Phelan-McDermid syndrome", "amelocerebrohypohidrotic syndrome", "distal 17p13.3 microdeletion syndrome", "trichotillomania", "Malan overgrowth syndrome", "retinal dystrophy with or without extraocular anomalies", "hydranencephaly (disease)"]
---

# Aripiprazole
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

# Aripiprazole: 허가 적응증에서 주요 우울장애(Major Affective Disorder)로

## 한 문장 요약

Aripiprazole은 D2/5-HT1A 부분 작용제이자 5-HT2A 길항제로, 한국에서 20건의 허가증이 유효하게 시판되고 있는 비정형 항정신병약입니다. TxGNN 모델은 **주요 우울장애(Major Affective Disorder)**에 효과가 있을 수 있다고 예측하며, 현재 **35건의 임상시험**과 **19편의 문헌**이 이 방향을 지지합니다. 특히 항우울제 보조요법(치료저항성 우울증)에서 근거가 가장 강합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 링크 형태로만 제공되어 확인 불가 (허가사항 참조 필요) |
| 예측 신규 적응증 | 주요 우울장애 (major affective disorder) |
| TxGNN 예측 점수 | 99.62% |
| 근거 수준 | L1 (완료된 Phase 3 RCT 다수) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 이 보고서용 데이터에 포함되어 있지 않습니다. 알려진 약리 정보에 따르면 aripiprazole은 D2/5-HT1A 부분 작용제이자 5-HT2A 길항제입니다. 도파민과 세로토닌 신호 조절은 항우울제 보조 효과와 양극성 장애에서의 기분 안정화에 대한 타당한 근거가 됩니다.

근거는 항우울제에 불충분하게 반응한 주요 우울장애에 대한 보조요법에서 가장 강합니다. 위약 대조 Phase 3 시험이 여러 건 완료되었고, 대규모 비교 효과 시험(VAST-D)과 다수의 메타분석이 있습니다.

다만 기존 적응증과 작용 기전 항목이 확인되지 않았으므로, 허가사항에서 실제 허가 적응증을 확인한 뒤에야 진정한 재창출인지 판단할 수 있습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00095823](https://clinicaltrials.gov/study/NCT00095823) | Phase 3 | 완료 | 1200 | 항우울제 보조요법 aripiprazole의 14주 이중맹검 위약대조 효능·안전성 시험 |
| [NCT00095758](https://clinicaltrials.gov/study/NCT00095758) | Phase 3 | 완료 | 1151 | 주요 우울장애에서 보조 aripiprazole의 14주 이중맹검 위약대조 시험 |
| [NCT00876343](https://clinicaltrials.gov/study/NCT00876343) | Phase 3 | 완료 | 586 | SSRI/SNRI 병용 보조 aripiprazole 대 위약 비교 시험 |
| [NCT00105196](https://clinicaltrials.gov/study/NCT00105196) | Phase 3 | 완료 | 349 | 항우울제 불완전 반응 환자에서 보조 aripiprazole의 14주 위약대조 시험 |
| [NCT00683852](https://clinicaltrials.gov/study/NCT00683852) | Phase 3 | 완료 | 225 | 감량된 용량의 aripiprazole 보조요법 위약대조 시험 |
| [NCT01421342](https://clinicaltrials.gov/study/NCT01421342) | Phase 3 | 완료 | 1522 | VAST-D: aripiprazole 보조 vs bupropion 보조 vs bupropion 전환 비교 |
| [NCT00095745](https://clinicaltrials.gov/study/NCT00095745) | Phase 3 | 완료 | 1002 | 보조 aripiprazole의 52주 장기 공개 안전성·내약성 시험 |
| [NCT01111539](https://clinicaltrials.gov/study/NCT01111539) | Phase 3 | 조기 종료 | 211 | Aripiprazole/escitalopram 병용요법 이중맹검 시험 (조기 종료로 근거 비중 제한) |
| [NCT00882362](https://clinicaltrials.gov/study/NCT00882362) | Phase 3 | 완료 | 155 | SSRI/SNRI 병용 보조 aripiprazole 장기 투여 안전성·효능 |
| [NCT00080314](https://clinicaltrials.gov/study/NCT00080314) | Phase 3 | 완료 | 400 | 양극성 우울 에피소드에서 aripiprazole 대 위약 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [42090141](https://pubmed.ncbi.nlm.nih.gov/42090141/) | 2026 | 체계적 문헌고찰/네트워크 메타분석 | JAMA Psychiatry | 주요 우울장애 보조 비정형 항정신병약의 효능·안전성 비교 (FDA는 5종 승인) |
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | 체계적 문헌고찰/네트워크 메타분석 | J Affect Disord | 치료저항성 우울증 보강 요법의 효능과 중단율 비교 |
| [35861202](https://pubmed.ncbi.nlm.nih.gov/35861202/) | 2023 | 체계적 문헌고찰/메타분석 | J Psychopharmacol | 초기 치료저항성 우울증의 보강·병용 치료 근거 평가 |
| [34238049](https://pubmed.ncbi.nlm.nih.gov/34238049/) | 2021 | 체계적 문헌고찰/메타분석 | J Psychopharmacol | 항우울제+SGA vs 에스케타민 vs 리튬 병용요법의 효능·내약성 비교 |
| [39739012](https://pubmed.ncbi.nlm.nih.gov/39739012/) | 2025 | 체계적 문헌고찰/네트워크 메타분석 | Neuropsychopharmacology | 치료저항성 우울증 치료법의 상대적 효과 비교 |
| [36855876](https://pubmed.ncbi.nlm.nih.gov/36855876/) | 2023 | Review | Am J Psychiatry | 치료저항성 우울증에서 항정신병약의 위치 |
| [37149344](https://pubmed.ncbi.nlm.nih.gov/37149344/) | 2023 | Review | Psychiatr Clin North Am | 비정형 항정신병약은 가장 많이 연구된 보강제이며 aripiprazole 등이 포함됨 |
| [37815563](https://pubmed.ncbi.nlm.nih.gov/37815563/) | 2023 | Review | JAMA | 양극성 장애의 진단과 치료 |
| [42283956](https://pubmed.ncbi.nlm.nih.gov/42283956/) | 2026 | 네트워크 메타분석 | Adv Ther | 우울장애 보조요법으로 승인된 비정형 항정신병약 간 비교 |
| [25963405](https://pubmed.ncbi.nlm.nih.gov/25963405/) | 2016 | 리뷰 | Asia Pac Psychiatry | 비정형 항정신병약은 항정신병 용량 이하에서 항우울 효과를 보임 |

참고: PMID 38669232(aripiprazole/bupropion 메타분석)는 철회된 논문이므로 근거로 사용하지 않았습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200202888 | 아빌리파이정5밀리그램 | 정제 | 허가사항 참조 |
| 200202889 | 아빌리파이정10밀리그램 | 정제 | 허가사항 참조 |
| 201309520 | 아빌리파이오디정10밀리그램 | 구강붕해정 | 허가사항 참조 |
| 202500429 | 아빌리파이아심투파이주사960밀리그램 | 서방형 주사제 | 허가사항 참조 |
| 201102477 | 아리피졸정10밀리그램 | 정제 | 허가사항 참조 |

전체 20건 중 주요 허가 5건만 표시했습니다. 수출용 허가(종근당, 신풍제약)도 포함되어 있습니다.

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 일부를 아래에 정리했습니다.
  - **Major**: Bupropion
  - **Moderate**: 혈당강하제(Acarbose, Metformin, Pioglitazone, Canagliflozin, Alogliptin, Albiglutide, Acetohexamide, Chlorpropamide), Epinephrine, 항콜린제(Atropine, Hyoscyamine, Clidinium), Clarithromycin, Cimetidine, Famotidine, Cisapride, Aprepitant, Loperamide, Clotrimazole
- **지식그래프 기반 금기 관련 질환**(허가문서가 아닌 TxGNN 지식그래프 기준): 기립저혈압, 간질, 고혈당·당뇨병·당뇨병성 케톤산증, 호중구감소증·무과립구증·백혈구감소증, 고지혈증, 비만, 심근경색·관상동맥질환, 심장 전도 질환, 급성 심정지, 신경이완제 악성 증후군, 뇌혈관 질환 등
- 이 약은 병용 시 충동·강박 행동(예: 발모광 사례 보고)을 유발할 수 있다는 보고가 있습니다.

허가사항의 경고·금기 항목은 이번 데이터에서 확인되지 않았으므로, 허가사항 원문을 반드시 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
항우울제 보조요법으로서 완료된 위약대조 Phase 3 시험이 다수 있고 대규모 비교 시험과 여러 메타분석이 뒷받침하여 근거 수준은 L1입니다. 다만 허가 적응증과 작용 기전 데이터가 확인되지 않았고, 안전성 관련 허가 정보가 없어 조건부 진행이 적절합니다.

**진행하려면 필요한 것:**
- MFDS 허가사항 PDF를 내려받아 허가 적응증, 경고, 금기 확인 (현재 차단성 데이터 공백)
- DrugBank에서 작용 기전(MOA) 데이터 확보
- 허가 적응증에 우울증 보조요법이 이미 포함되는지 확인하여 진정한 재창출 여부 판정
- 대사·심혈관 위험, 호중구감소증, 기립저혈압 등 지식그래프 금기 질환에 대한 모니터링 계획 수립
- Bupropion 등 주요 상호작용 약물의 병용 관리 지침 마련
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

