---
layout: default
title: Risperidone
parent: 높은 근거 (L1-L2)
nav_order: 606
evidence_level: L1
indication_count: 6
---

# Risperidone
{: .fs-9 }

근거 수준: **L1** | 예측 적응증: **6** 건
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

# Risperidone: 조현병·양극성 조증에서 정동장애(치료저항성 우울증 보조요법)로

## 한 문장 요약

> Risperidone은 임상시험 근거상 조현병 및 양극성 조증 치료에 사용되어 온 비정형 항정신병제입니다.
> TxGNN 모델은 이번 Evidence Pack에서 총 6개 적응증을 예측했는데, 이 중 **정동장애(Major Affective Disorder)**가
> 가장 강력한 실증 근거를 보였습니다 — 현재 **36건의 임상시험**(다수의 완료된 Phase 3 RCT 포함)과
> **20편의 문헌**(체계적 문헌고찰·메타분석 다수)이 이 방향을 지지합니다.
> 나머지 5개 예측(안구운동마비 증후군, 아스퍼거 증후군 감수성 등 희귀 유전질환)은
> TxGNN 점수는 높지만 실제 근거가 없거나(L5) 기전적 타당성이 낮아 모두 보류(Hold) 판정되었으며 본 보고서에서는 다루지 않습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 조현병 및 양극성 조증 (임상시험 자료 기반 확인, 국내 허가 자료는 없음) |
| 예측 신규 적응증 | 정동장애 / 치료저항성 우울증 보조요법 (Major Affective Disorder) |
| TxGNN 예측 점수 | 99.11% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

공식 DrugBank 작용기전(MOA) 데이터는 아직 확보되지 않았습니다(Data Gap, 심각도: High). 다만 Evidence Pack에 포함된 임상시험·근거 자료에 따르면, Risperidone은 D2 도파민 수용체와 5-HT2A 세로토닌 수용체를 동시에 길항하는 제2세대(비정형) 항정신병약물로 알려져 있습니다.

이 기전은 이미 조현병뿐 아니라 양극성 조증의 핵심 치료 기전으로 확립되어 있으며, 여러 대규모 Phase 3 RCT에서 소아·성인 양극성장애의 급성 조증 및 유지요법에 대한 단독/병용 효능이 입증되었습니다. 나아가 세로토닌-도파민 이중 조절 특성 때문에 치료저항성 주요우울장애(TRD)에서 SSRI/SNRI에 대한 증강요법(augmentation)으로도 폭넓게 연구되어 왔습니다.

즉 "정동장애"로의 확장은 완전히 새로운 가설이라기보다, 이미 임상에서 광범위하게 활용되고 여러 국가에서 부분적으로 허가·가이드라인화된 사용 패턴을 TxGNN이 지식그래프상에서 재확인한 결과에 가깝습니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00107939](https://clinicaltrials.gov/study/NCT00107939) | Phase 3 | 완료 | 453 | Licarbazepine 부가요법 vs 위약, risperidone 등 비정형 항정신병제 병용 하 양극성 조증 치료 |
| [NCT00095134](https://clinicaltrials.gov/study/NCT00095134) | Phase 3 | 완료 | 630 | 항우울제 반응 불충분 주요우울장애에서 risperidone 부가요법 vs 위약, 이중맹검 |
| [NCT00391222](https://clinicaltrials.gov/study/NCT00391222) | Phase 3 | 완료 | 585 | 양극성 I 장애 기분삽화 재발 방지에서 risperidone 지속형 주사제(LAI) vs 위약 |
| [NCT00057681](https://clinicaltrials.gov/study/NCT00057681) | Phase 3 | 완료 | 379 | TEAM 연구: 소아·청소년 조증에서 lithium/valproate/risperidone 비교 |
| [NCT00044681](https://clinicaltrials.gov/study/NCT00044681) | Phase 3 | 완료 | 258 | 치료저항성 단극성 우울증에서 SSRI + risperidone 증강요법 장기 유지 효과 |
| [NCT01888107](https://clinicaltrials.gov/study/NCT01888107) | Phase 3 | 완료 | 347 | 조현병·조현정동장애에서 risperidone LAI 임상반응 유지 |
| [NCT00277654](https://clinicaltrials.gov/study/NCT00277654) | Phase 3 | 완료 | 111 | 불안 동반 양극성장애 외래환자에서 risperidone 단독요법 vs 위약 |
| [NCT00176202](https://clinicaltrials.gov/study/NCT00176202) | Phase 3 | 완료 | 65 | 소아 양극성장애에서 risperidone vs divalproex sodium, MRI 회로 분석 병행 |
| [NCT00221403](https://clinicaltrials.gov/study/NCT00221403) | Phase 3 | 완료 | 46 | 3–7세 양극성장애 소아에서 valproate·risperidone 위약대조 시험 |
| [NCT01282632](https://clinicaltrials.gov/study/NCT01282632) | Phase 1/2 | 완료 | 42 | 치료저항성 우울증에서 risperidone vs olanzapine, SSRI 부가요법 이중맹검 예비시험 |

*(위 10건 외 총 36건의 관련 임상시험이 등록되어 있으며, 다수가 소아·청소년 양극성장애 및 치료저항성 우울증 영역입니다.)*

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [17975181](https://pubmed.ncbi.nlm.nih.gov/17975181/) | 2007 | RCT | Annals of Internal Medicine | 치료저항성 주요우울장애에서 risperidone 무작위 대조 시험 |
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | 체계적 문헌고찰/네트워크 메타분석 | J Affect Disord | 치료저항성 우울증 증강요법제 간 효능·중단율 비교 |
| [35861202](https://pubmed.ncbi.nlm.nih.gov/35861202/) | 2023 | 체계적 문헌고찰/메타분석 | J Psychopharmacol | 초기단계 치료저항성 우울증 부가/병용요법 효능 종합분석 |
| [34238049](https://pubmed.ncbi.nlm.nih.gov/34238049/) | 2021 | 메타분석 | J Psychopharmacol | 항우울제+2세대 항정신병제 vs esketamine vs lithium 병용요법 비교 |
| [35510505](https://pubmed.ncbi.nlm.nih.gov/35510505/) | 2023 | 체계적 문헌고찰 | Psychological Medicine | 성인 주요우울장애에서 항정신병제 단독/부가요법 효능·내약성 |
| [21154393](https://pubmed.ncbi.nlm.nih.gov/21154393/) | 2010 | Cochrane 리뷰 | Cochrane Database Syst Rev | 주요우울장애·기분부전증에서 2세대 항정신병제 효과 |
| [24919175](https://pubmed.ncbi.nlm.nih.gov/24919175/) | 2014 | 메타분석 | Braz J Med Biol Res | 17개 시험·3,807명 대상 비정형 항정신병제 항우울제 증강요법 메타분석 |
| [25295435](https://pubmed.ncbi.nlm.nih.gov/25295435/) | 2014 | 전국 인구기반 코호트 | J Clin Psychiatry | Aripiprazole/olanzapine/quetiapine/risperidone 증강요법 실제 효과 비교 |
| [7545159](https://pubmed.ncbi.nlm.nih.gov/7545159/) | 1995 | 임상연구 | J Clin Psychiatry | Risperidone의 정동질환·강박장애 치료 가능성에 대한 초기 임상 관찰 |
| [21189367](https://pubmed.ncbi.nlm.nih.gov/21189367/) | 2011 | 문헌고찰 | Annals of Pharmacotherapy | 주요우울장애 증강치료로서 risperidone 효능·안전성 리뷰 |

*(총 20편의 관련 문헌이 확인되었습니다.)*

---

## 한국 시판 정보

현재 한국에서 Risperidone의 허가·시판 이력이 이 Evidence Pack에는 확인되지 않습니다(허가증 0건, 미시판 상태).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (TFDA/식약처 라벨상 경고·금기·상호작용 데이터는 아직 확보되지 않은 Blocking 등급 Data Gap입니다.)

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
- 정동장애(양극성 조증, 치료저항성 우울증 증강요법) 방향은 다수의 완료된 Phase 3 RCT와 체계적 문헌고찰/메타분석으로 뒷받침되는 L1 수준 근거를 갖추고 있어, 순수 모델 예측을 넘어선 실질적 임상 활용 근거가 존재합니다.
- 다만 이 약물은 국내(한국) 시판 이력이 없고, 안전성 라벨(경고/금기)과 공식 MOA 자료가 아직 확보되지 않아(Blocking/High Data Gap) 즉시 진행보다는 안전장치를 두고 진행해야 합니다.

**진행하려면 필요한 것:**
- 식약처(MFDS) 라벨상 경고·금기사항 확보 (DG001, Blocking — S1 안전성 초평가 진입 전제조건)
- DrugBank 공식 작용기전(MOA) 데이터 확보 (DG002, High)
- 한국 내 허가/시판 전략 수립 (현재 미시판 상태이므로 정동장애 적응증 확대 이전에 기본 허가 경로 검토 필요)
- 정동장애 적응증에 대해 이미 허가한 해외 규제기관 라벨(예: 조증 부가요법 승인국)과의 비교 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

