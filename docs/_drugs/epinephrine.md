---
layout: default
title: Epinephrine
parent: 높은 근거 (L1-L2)
nav_order: 292
evidence_level: L2
indication_count: 4
---

# Epinephrine
{: .fs-9 }

근거 수준: **L2** | 예측 적응증: **4** 건
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

# Epinephrine: 아나필락시스에서 폐쇄성 폐질환으로

## 한 문장 요약

Epinephrine(에피네프린)은 아나필락시스(과민성 쇼크) 등 응급 상황에 사용되어 온 비선택적 α/β 아드레날린 수용체 작용제입니다.
TxGNN 모델은 **폐쇄성 폐질환(Obstructive Lung Disease)**에도 효과가 있을 수 있다고 예측하며(예측 점수 99.71%),
전체 50건의 임상시험과 20편의 문헌 중 직접 관련성이 높은 **10건의 임상시험**과 **10편의 문헌**이 이 방향(기관지 확장/점막 부종 완화)을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 아나필락시스 등 응급 적응증 (국내 허가 자료 없음 — 미상판 약물) |
| 예측 신규 적응증 | 폐쇄성 폐질환 (Obstructive Lung Disease) |
| TxGNN 예측 점수 | 99.71% |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미상판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

**참고 — 이번 Evidence Pack은 4개 예측 적응증을 포함합니다.** 아래는 전체 후보 비교이며, 본 보고서는 근거 수준이 가장 높은 1순위(폐쇄성 폐질환)를 중심으로 상세히 다룹니다.

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 | 권장 결정 |
|------|-----------|-----------|----------|----------|
| 1 | 폐쇄성 폐질환 | 99.71% | L2 | Proceed with Guardrails |
| 2 | 식품 유발 운동유발성 아나필락시스 (FDEIA) | 99.57% | L3 | Proceed with Guardrails |
| 3 | Rienhoff 증후군 | 99.57% | L5 | Hold |
| 4 | 호흡기 기형 | 99.56% | L4 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터(MOA)는 데이터베이스상 [Data Gap]으로 표시되어 있습니다. 다만 Epinephrine은 약리학적으로 잘 알려진 비선택적 α/β 아드레날린 수용체 작용제이며, β2 수용체 작용을 통한 기관지 평활근 이완과 α1 수용체 작용을 통한 점막 혈관수축(부종 감소)이 핵심 기전입니다.

이는 기도 폐쇄성 질환(천식, 세기관지염, 크룹)의 급성 악화 시 나타나는 기관지 경련과 점막 부종을 동시에 완화할 수 있는 고전적인 생리 기전으로, 완전히 새로운 가설이라기보다는 흡입형/분무형(nebulized) Epinephrine이 이미 응급실 임상 실무에서 세기관지염·크룹 치료에 널리 사용되어 온 적응증 확장에 가깝습니다. 다만 "폐쇄성 폐질환(obstructive lung disease)"이라는 포괄적 질병 분류에 대한 공식 승인 표지가 없을 뿐입니다.

실제로 Epinephrine 흡입 에어로졸(E004, HFA-MDI 제형)에 대한 별도의 임상 개발 프로그램이 존재하며, 이는 TxGNN 예측이 임상 현실과 상당 부분 부합함을 뒷받침합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01143051](https://clinicaltrials.gov/study/NCT01143051) | Phase 1/2 | 완료 | 24 | Epinephrine Inhalation Aerosol(E004, HFA-MDI)의 약동학·안전성 평가 |
| [NCT01737892](https://clinicaltrials.gov/study/NCT01737892) | Phase 1/2 | 종료 | 21 | 중수소 표지 epinephrine-d3로 E004의 약동학 정밀 평가 |
| [NCT01476904](https://clinicaltrials.gov/study/NCT01476904) | Phase 3 | 완료 | 208 | 천식 환자 대상 E004(epinephrine 흡입) vs 위약 6개월 안전성 연구 |
| [NCT01737905](https://clinicaltrials.gov/study/NCT01737905) | Phase 3 | 완료 | 28 | 4-11세 소아 천식 환자에서 E004 단회 투여 유효성·안전성 |
| [NCT04207840](https://clinicaltrials.gov/study/NCT04207840) | Phase 4 | 완료 | 28 | Primatene Mist 흡입 vs Epinephrine 근육주사 vs ProAir 전신 노출 비교 |
| [NCT01705964](https://clinicaltrials.gov/study/NCT01705964) | Phase 4 | 완료 | 49 | 소아 중증 천식 악화에서 근육주사 epinephrine의 보조요법 효과 |
| [NCT00817466](https://clinicaltrials.gov/study/NCT00817466) | Phase 4 | 불명 | 500 | 영유아 급성 세기관지염 최적 흡입치료 비교(분무 epinephrine 포함) |
| [NCT02586961](https://clinicaltrials.gov/study/NCT02586961) | Phase 2/3 | 종료 | 195 | 소아 세기관지염에서 분무 adrenaline + 경구 betamethasone 병용 |
| [NCT02585531](https://clinicaltrials.gov/study/NCT02585531) | Phase 2 | 불명 | 100 | 소아 세기관지염에서 Epinephrine, dexamethasone, 고장식염수 비교 |
| [NCT00114478](https://clinicaltrials.gov/study/NCT00114478) | N/A | 불명 | 600 | 세기관지염에서 Epinephrine과 Albuterol의 효과 비교 RCT |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [34593615](https://pubmed.ncbi.nlm.nih.gov/34593615/) | 2022 | Review | Thorax | 급성 천식에서 Epinephrine과 선택적 β2 작용제 비교 체계적 문헌고찰·메타분석 |
| [21678340](https://pubmed.ncbi.nlm.nih.gov/21678340/) | 2011 | Review (Cochrane) | Cochrane Database Syst Rev | 세기관지염에서 Epinephrine의 효과에 대한 체계적 고찰 |
| [14974006](https://pubmed.ncbi.nlm.nih.gov/14974006/) | 2004 | Review (Cochrane) | Cochrane Database Syst Rev | 세기관지염 관리에서 기관지확장제(Epinephrine 포함)의 초기 근거 검토 |
| [30488718](https://pubmed.ncbi.nlm.nih.gov/30488718/) | 2019 | Review | Expert Rev Respir Med | 소아 세기관지염 치료전략 중 라세믹 epinephrine의 역할 검토 |
| [19135584](https://pubmed.ncbi.nlm.nih.gov/19135584/) | 2009 | Review | Pediatr Clin North Am | 급성 세기관지염·크룹에서 분무 adrenaline의 증상 완화 효과 |
| [21486501](https://pubmed.ncbi.nlm.nih.gov/21486501/) | 2011 | Review | BMJ Clinical Evidence | 세기관지염의 호발 시기·치료 개관 |
| [19450362](https://pubmed.ncbi.nlm.nih.gov/19450362/) | 2007 | Review | BMJ Clinical Evidence | 세기관지염의 역학 및 치료 개관 (구판) |
| [6417212](https://pubmed.ncbi.nlm.nih.gov/6417212/) | 1983 | Review | J Allergy Clin Immunol | 소아 천식의 기도 폐쇄 병태생리 개관 |
| [6107058](https://pubmed.ncbi.nlm.nih.gov/6107058/) | 1980 | Review | Anaesth Intensive Care | 교감신경흥분성 아민(Epinephrine 포함)의 임상 선택 기준 |
| [6777857](https://pubmed.ncbi.nlm.nih.gov/6777857/) | 1980 | Cohort | Scand J Clin Lab Invest | 만성 폐쇄성 폐질환 환자의 혈중 노르아드레날린 농도와 혈역학 상관관계 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> ⚠ 참고: TFDA(대만 식약처 상당) 수준의 공식 경고문·금기 정보 확보가 **Blocking 등급 데이터 갭**으로 분류되어 있어, 현재로서는 S1 안전성 초기 평가 자체가 불가능한 상태입니다.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
분무·흡입형 Epinephrine이 세기관지염·천식 악화 치료에 사용된 다수의 Phase 1-4 임상시험과 Cochrane 체계적 고찰이 존재하여, "폐쇄성 폐질환" 적응증 확장의 기전적·임상적 타당성은 L2 수준으로 뒷받침됩니다. 다만 국내(한국) 미상판 상태이며 안전성 라벨 정보가 전무하여, 가드레일 없이 바로 진행하기는 이릅니다.

**진행하려면 필요한 것:**
- TFDA(또는 해당국 식약처) 공식 허가사항 PDF 확보 및 경고/금기 정보 파싱 (Blocking, 최우선)
- DrugBank API를 통한 공식 작용기전(MOA) 데이터 보강
- 국내 시판 여부 및 제형별 투여경로 확인 (현재 총 허가 0건)
- FDEIA(2순위) 적응증은 이미 승인된 아나필락시스 적응증의 직접 연장으로, 임상시험 설계상 윤리적 제약이 있어 실제 진행 시 RCT 대신 관찰연구·레지스트리 활용 검토 필요
- Rienhoff 증후군(3순위)·호흡기 기형(4순위)은 근거 부재 또는 기전 불일치로 현시점 Hold 유지 권장
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

