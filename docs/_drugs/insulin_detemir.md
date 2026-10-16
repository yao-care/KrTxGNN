---
layout: default
title: Insulin Detemir
parent: 모델 예측만 (L5)
nav_order: 425
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Insulin Detemir: 예측 신규 적응증 제1형 당뇨병 (type 1 diabetes mellitus) (근거 수준 L5). 기존 적응증: 허가 적응증 원문은 링크로만 제공되어 구체적 문구를 확인할 수 없음 (당뇨병 치료제로 시판)"
monitor_inn: "INSULIN DETEMIR"
predicted_indications: ["type 1 diabetes mellitus", "autoimmune oophoritis", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "classic stiff person syndrome", "focal stiff limb syndrome", "pancreatic agenesis", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy"]
---

# Insulin Detemir
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

# Insulin Detemir: 제1형 당뇨병에서 제1형 당뇨병으로 (기존 적응증 재확인)

## 한 문장 요약

Insulin detemir는 지속형 기저 인슐린 유사체로, 한국에서 당뇨병 치료제로 허가되어 시판 중입니다.
TxGNN 모델이 1순위로 예측한 **제1형 당뇨병(type 1 diabetes mellitus)**은 이 약의 기존 용도와 사실상 같아서 새로운 재창출 발견으로 보기 어렵고, 기존 적응증을 재확인하는 결과입니다.
이 방향을 **임상시험 40건**과 **문헌 20편**이 뒷받침합니다. 나머지 예측 질환(2~10위)은 근거가 거의 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 원문은 링크로만 제공되어 구체적 문구를 확인할 수 없음 (당뇨병 치료제로 시판) |
| 예측 신규 적응증 | 제1형 당뇨병 (type 1 diabetes mellitus) |
| TxGNN 예측 점수 | 99.77% |
| 근거 수준 | L1 (완료된 Phase 3 RCT 다수) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 다만 문헌에 따르면 insulin detemir는 14-탄소 지방산(myristic acid)을 결합한 가용성 지속형 인슐린 유사체입니다. 피하 주사 후 알부민에 가역적으로 결합하여 흡수가 느려지고, 최대 24시간 지속되는 혈당 강하 효과를 냅니다. 인슐린 수용체에 작용해 부족한 내인성 인슐린을 보충합니다.

제1형 당뇨병은 인슐린이 절대적으로 부족한 질환이므로, 기저 인슐린 보충은 기전상 가장 직접적인 치료입니다. 이 예측은 새로운 용도 발견이 아니라 기존 용도의 재확인이라고 보는 것이 정확합니다.

2~10위 예측 질환(자가면역 난소염, opsismodysplasia, 티아민 반응성 이상 증후군, 강직인간증후군, 췌장 무발생, 국소 지방이영양증 등)은 임상시험이나 문헌이 없습니다. 대부분 당뇨병 동반증이나 유전자 경로 연관성에서 나온 계산상 예측으로 보입니다. 이 중 췌장 무발생은 신생아 인슐린 결핍성 당뇨병이어서 기전상 타당하나, 제1형 당뇨병에서의 외삽에 그칩니다. 약물 유발 국소 지방이영양증은 주사 인슐린이 오히려 원인이 될 수 있어 치료 신호로 보기 어렵습니다.

## 임상시험 근거

관련성이 높은 시험 10건을 표시합니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00595374](https://clinicaltrials.gov/study/NCT00595374) | Phase 3 | 완료 | 114 | 성인 제1형 당뇨병에서 detemir+aspart와 NPH+aspart의 혈당 조절 비교 |
| [NCT00447382](https://clinicaltrials.gov/study/NCT00447382) | Phase 3 | 완료 | 330 | 기존 공정과 신규 공정(NN729) detemir의 12개월 이중맹검 안전성·효능 비교 |
| [NCT00312156](https://clinicaltrials.gov/study/NCT00312156) | Phase 3 | 완료 | 347 | 소아·청소년 제1형 당뇨병에서 detemir와 NPH 비교 |
| [NCT00184639](https://clinicaltrials.gov/study/NCT00184639) | Phase 3 | 완료 | 71 | 소아·청소년·청년에서 detemir와 Semilente MC 비교 (32주) |
| [NCT00117780](https://clinicaltrials.gov/study/NCT00117780) | Phase 4 | 완료 | 520 | detemir 하루 1회 vs 2회 투여의 효능·안전성 비교 |
| [NCT01542463](https://clinicaltrials.gov/study/NCT01542463) | 해당 없음 | 완료 | 4,464 | 제1형·제2형 당뇨병에서 Levemir의 안전성, 혈당 조절, 체중 관찰 연구 |
| [NCT00322257](https://clinicaltrials.gov/study/NCT00322257) | Phase 3 | 중단 | 596 | 흡입 식사 인슐린 vs 주사 aspart (두 군 모두 detemir 병용). detemir 자체 평가는 아님 |
| [NCT01440439](https://clinicaltrials.gov/study/NCT01440439) | Phase 4 | 불명 | 30 | 운동 중 detemir와 glargine의 혈당 조절 비교 |
| [NCT00670683](https://clinicaltrials.gov/study/NCT00670683) | 해당 없음 | 완료 | 797 | 한국에서 Levemir FlexPen의 단기·장기 안전성과 효능을 보는 관찰 연구 |
| [NCT00313742](https://clinicaltrials.gov/study/NCT00313742) | Phase 4 | 완료 | 51 | 운동 시 detemir, glargine, NPH의 혈당 감소 비교 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | 임신한 제1형 당뇨병 여성에서 degludec와 detemir의 비열등성 비교 (EXPECT) |
| [33662147](https://pubmed.ncbi.nlm.nih.gov/33662147/) | 2021 | 체계적 문헌고찰 | Cochrane Database Syst Rev | 제1형 당뇨병에서 (초)지속형 인슐린 유사체의 합병증·저혈당 영향 |
| [21878861](https://pubmed.ncbi.nlm.nih.gov/21878861/) | 2011 | 메타분석 | Pol Arch Med Wewn | 제1형 당뇨병에서 detemir와 NPH 비교 |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | 네트워크 메타분석 | Value Health | 성인 제1형 당뇨병 기저 인슐린 요법의 상대적 효능·안전성 |
| [23243636](https://pubmed.ncbi.nlm.nih.gov/23243636/) | 2012 | 체계적 문헌고찰 | Drugs Today | 소아·청소년 제1형 당뇨병에서의 인슐린 유사체 |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | 메타분석 | Clin Ther | degludec와 glargine·detemir의 효능 및 내약성 비교 |
| [17326333](https://pubmed.ncbi.nlm.nih.gov/17326333/) | 2006 | Review | Vasc Health Risk Manag | 제1형·제2형 당뇨병에서 detemir, 특히 야간 저혈당 위험 감소 |
| [15516157](https://pubmed.ncbi.nlm.nih.gov/15516157/) | 2004 | Review | Drugs | detemir는 NPH보다 예측 가능하고 일관된 혈당 강하 효과 |
| [20539842](https://pubmed.ncbi.nlm.nih.gov/20539842/) | 2010 | Review | Vasc Health Risk Manag | detemir 중심의 제1형·제2형 당뇨병 치료 업데이트 |
| [17881330](https://pubmed.ncbi.nlm.nih.gov/17881330/) | 2007 | Review | Endocrinol Metab Clin North Am | 집중 당뇨병 치료와 체중, detemir의 체중 증가 감소 가능성 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200603934 | 레버미어플렉스펜주100단위/밀리리터 (노보노디스크제약) | 용량 조절이 가능한 펜 모양의 프리필드 주사제 | 허가 적응증 원문은 링크로만 제공되어 구체적 내용을 확인할 수 없음 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 확인되었으며, 대부분 중등도(Moderate)입니다. 대표 항목은 다음과 같습니다.
  - 다른 혈당강하제: metformin, pioglitazone, alogliptin, albiglutide
  - 교감신경 작용제: epinephrine, salbutamol, formoterol, pseudoephedrine, phenylephrine
  - 기타: acebutolol(베타차단제), hydrochlorothiazide, acetazolamide, ethinylestradiol, estradiol, hydrocortisone, doxycycline, ethanol, alpelisib
  - 경미한 수준(Minor): 국소 hydrocortisone, 국소 alclometasone

경고와 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
제1형 당뇨병에는 완료된 Phase 3 RCT가 여러 건 있고 체계적 문헌고찰도 풍부해 근거는 충분합니다. 다만 이것은 이미 시판 중인 용도의 재확인이므로 새로운 재창출 성과로 해석해서는 안 됩니다. 2~10위 예측 질환은 근거가 없어 보류(Hold) 수준이며, 췌장 무발생만 추가 연구 질문으로 남습니다.

**진행하려면 필요한 것:**
- 허가사항 원문(적응증, 경고, 금기)을 확보하고 확인
- 작용 기전(MOA) 데이터 보완 (DrugBank 등)
- 재창출 가치를 평가하려면 제1형 당뇨병 외의 질환(예: 췌장 무발생)에 대한 별도 검토
- 병용 시 저혈당 위험이 있으므로 다른 혈당강하제와의 상호작용 모니터링 계획 수립
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

