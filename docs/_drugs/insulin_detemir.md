---
layout: default
title: Insulin Detemir
parent: 높은 근거 (L1-L2)
nav_order: 396
evidence_level: L1
indication_count: 10
---

# Insulin Detemir
{: .fs-9 }

근거 수준: **L1** | 예측 적응증: **10** 건
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

# Insulin Detemir: 적응증 데이터 공백 상태에서 "제1형 당뇨병"으로 (사실상 기존 적응증 재확인)

## 한 문장 요약

Insulin Detemir(DB01307)는 장시간형 인슐린 유사체로, 본 Evidence Pack에는 기존 승인 적응증 데이터가 공백(Data Gap)으로 표시되어 있습니다. TxGNN 모델은 **제1형 당뇨병(Type 1 Diabetes Mellitus)**에 효과가 있을 것으로 예측(점수 99.77%)하며, 임상시험 50건 조회·문헌 19편 조회 중 다수가 이를 지지합니다. 다만 이 예측은 데이터 자체에 명시된 것처럼 **인슐린 제제의 기존·핵심 적응증을 재확인한 것**이며, 진정한 의미의 "노약재창출(drug repurposing)" 후보는 아닙니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (허가증 0건, 미출시로 approved_indication_text 확인 불가) |
| 예측 신규 적응증 | 제1형 당뇨병 (Type 1 Diabetes Mellitus) |
| TxGNN 예측 점수 | 99.77% |
| 근거 수준 | L1 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 Data Gap으로 표시되어 있습니다. 다만 수집된 문헌 근거(PMID 15516157, 15691219 등)에 따르면, insulin detemir는 14-carbon 지방산이 결합된 가용성 장시간형 인간 인슐린 유사체로, 알부민에 가역적으로 결합하여 흡수가 지연되고 최대 24시간까지 지속적인 혈당 강하 효과를 나타냅니다. 이는 제1형·제2형 당뇨병 환자의 기저 인슐린 요법으로 널리 사용되는 기전입니다.

**중요한 주의점**: 본 Evidence Pack의 `repurposing_rationale`에 명시된 바와 같이, insulin detemir는 제1형 당뇨병 환자에게 부족한 인슐린을 직접 보충하는 약물이며, 이는 약물의 핵심·기존 작용이지 "노약재창출"로 볼 수 없습니다. `original_indications`가 공백으로 표시된 것은 실제 적응증이 없어서가 아니라 데이터 수집 단계의 공백(Data Gap)으로 판단됩니다.

나머지 예측 적응증(자가면역 난소염, 골격 이형성증, 티아민 반응성 증후군, Stiff Person 증후군, 지방위축증 등)은 대부분 근거 수준 L4~L5로, 임상시험·문헌이 전무하며 일부(약물 유발 국소 지방위축증 등)는 오히려 **인슐린 주사가 원인 질환**인 역방향 관계로 파악되어 치료 후보로 부적절합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01486940](https://clinicaltrials.gov/study/NCT01486940) | Phase 3 | 완료 | 598 | 제1형 당뇨병 기저-볼루스 요법에서 detemir+aspart vs NPH+human soluble insulin 비교 |
| [NCT03220425](https://clinicaltrials.gov/study/NCT03220425) | Phase 3 | 완료 | 752 | 제1형 당뇨병 기저-볼루스 요법에서 detemir(2400 nmol/mL) vs NPH 효능·안전성 비교 |
| [NCT01513473](https://clinicaltrials.gov/study/NCT01513473) | Phase 3 | 완료 | 350 | 소아·청소년 제1형 당뇨병에서 degludec vs detemir 26주+26주 연장 효능·안전성 비교(BEGIN Young 1) |
| [NCT00447382](https://clinicaltrials.gov/study/NCT00447382) | Phase 3 | 완료 | 330 | 제1형 당뇨병 기저-볼루스 요법에서 신규/기존 생산공정 detemir 간 12개월 안전성 비교 |
| [NCT01798706](https://clinicaltrials.gov/study/NCT01798706) | Phase 3 | 완료 | 350 | 고령 제2형 당뇨병 환자에서 lixisenatide 24주 이중맹검 위약대조 효능·안전성 평가 |
| [NCT01709929](https://clinicaltrials.gov/study/NCT01709929) | Phase 3 | 완료 | 2287 | 제1형·제2형 당뇨병 환자 대상 insulin detemir 대규모 안전성 평가 |
| [NCT01831765](https://clinicaltrials.gov/study/NCT01831765) | Phase 3 | 완료 | 1290 | 제1형 당뇨병 성인에서 detemir 병용 하 FIAsp vs insulin aspart 효능·안전성 비교 |
| [NCT00474045](https://clinicaltrials.gov/study/NCT00474045) | Phase 3 | 완료 | 470 | 제1형 당뇨병 임신 여성에서 detemir+aspart vs NPH+aspart 혈당조절·안전성 비교 |
| [NCT00095082](https://clinicaltrials.gov/study/NCT00095082) | Phase 3 | 완료 | 447 | 제1형 당뇨병에서 detemir+aspart vs glargine+aspart 안전성·유효성 비교 |
| [NCT00487240](https://clinicaltrials.gov/study/NCT00487240) | Phase 3 | 완료 | 387 | 제1형 당뇨병 기저-볼루스 요법에서 insulin lispro protamine suspension vs detemir 비교 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | 제1형 당뇨병 임신 여성에서 degludec vs detemir(+aspart) 비열등성 무작위대조시험(EXPECT) |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Review(네트워크 메타분석) | Value in Health | 성인 제1형 당뇨병 기저 인슐린 요법의 상대적 효능·안전성 체계적 문헌고찰 |
| [21878861](https://pubmed.ncbi.nlm.nih.gov/21878861/) | 2011 | 체계적 문헌고찰/메타분석 | Pol Arch Med Wewn | 제1형 당뇨병에서 detemir vs NPH 혈당조절 효과 비교 |
| [15516157](https://pubmed.ncbi.nlm.nih.gov/15516157/) | 2004 | Review | Drugs | Insulin detemir의 제1형·제2형 당뇨병 관리에서의 역할 개관 |
| [15691219](https://pubmed.ncbi.nlm.nih.gov/15691219/) | 2005 | Review | BioDrugs | Insulin detemir 약리학적 특성 및 임상적 활용 스포트라이트 |
| [23110609](https://pubmed.ncbi.nlm.nih.gov/23110609/) | 2012 | Review | Drugs | Insulin detemir의 당뇨병 관리 전반 재검토 |
| [20539842](https://pubmed.ncbi.nlm.nih.gov/20539842/) | 2010 | Review | Vasc Health Risk Manag | 제1형·제2형 당뇨병 치료 업데이트, detemir 중심 |
| [17326333](https://pubmed.ncbi.nlm.nih.gov/17326333/) | 2006 | Review | Vasc Health Risk Manag | 제1형·제2형 당뇨병에서 insulin detemir 치료 |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Review | Lancet Diabetes Endocrinol | 임신 중 제1형 당뇨병 관리(생활습관·약물·신기술) 최신 지견 |
| [18454569](https://pubmed.ncbi.nlm.nih.gov/18454569/) | 2008 | Review | Paediatr Drugs | 소아·청소년 제1형 당뇨병에서 인슐린 유사체 제제 개관 |

## 한국 시판 정보

현재 한국에 등재된 허가 정보가 없습니다(허가증 0건, 미출시 상태).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (주요 경고, 금기, DDI 모두 데이터 공백이며, DDI 조회 결과도 "찾을 수 없음"으로 확인됨)

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 최상위 예측 적응증(제1형 당뇨병)은 인슐린 제제의 **기존·핵심 적응증을 재확인**한 것으로, 데이터 자체에 이 점이 명시되어 있어 진정한 노약재창출 후보로 볼 수 없습니다.
- 나머지 9개 예측 적응증은 근거 수준 L4~L5로 임상·문헌 근거가 전무하며, 일부는 기전상 방향이 반대(지방위축증은 인슐린의 부작용이지 치료 대상이 아님)입니다.
- TFDA(현지 규제기관) 수준의 경고·금기 정보(DG001)가 **Blocking** 등급 공백이라 S1 안전성 초기 평가 자체가 불가능하며, 한국 내 허가증도 0건(미출시)입니다.

**진행하려면 필요한 것:**
- DG001: 규제기관 등재 첨부문서(경고/금기) 확보 — S1 안전성 초평 진입 필수
- DG002: DrugBank API를 통한 정식 MOA 데이터 확보
- `original_indications` 공백 원인 확인 — 데이터 수집 오류인지, 실제 미등재 상태인지 재검증
- 진정한 신규 적응증 후보를 찾으려면 rank 1(제1형 당뇨병)을 제외하고 rank 7 이하(췌장무형성증 등)처럼 기전적으로 의미 있으나 근거가 부족한 후보에 대해 전임상/기전 연구 우선 확보 필요
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

