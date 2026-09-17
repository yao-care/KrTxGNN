---
layout: default
title: Omalizumab
parent: 중등도 근거 (L3-L4)
nav_order: 519
evidence_level: L4
indication_count: 10
---

# Omalizumab
{: .fs-9 }

근거 수준: **L4** | 예측 적응증: **10** 건
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

# Omalizumab: 알레르기성 천식에서 기관지염으로

## 한 문장 요약

Omalizumab은 IgE를 표적으로 하는 재조합 인간화 단클론항체로, 국제적으로 알레르기성 천식·만성 특발성 두드러기 치료에 승인되어 사용되어 왔습니다(단, 한국 허가 자료는 현재 확인되지 않음).
TxGNN 모델은 **기관지염(Bronchitis)**에도 효과가 있을 수 있다고 예측했으나, 현재 근거는 대부분 천식 환자를 대상으로 한 연구이며 기관지염 자체를 검증한 임상시험은 **2건**, 관련 문헌은 **8편**에 그쳐 근거 수준이 낮습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 허가 자료 없음 (해외 자료 기준: 알레르기성 천식, IgE 매개 질환) |
| 예측 신규 적응증 | 기관지염 (Bronchitis) |
| TxGNN 예측 점수 | 99.9992% (rank 72) |
| 근거 수준 | L4 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

공식 DrugBank 자료에서 상세한 작용기전(MOA) 정보가 현재 확인되지 않습니다(자료 공백, 안전성 초기 평가에도 영향). 다만 근거 자료들을 종합하면, Omalizumab은 유리(free) IgE에 결합하여 비만세포·호염기구 표면의 고친화성 IgE 수용체(FcεRI) 발현을 하향조절함으로써 제2형(Th2) 알레르기 염증 반응을 억제하는 것으로 알려져 있습니다.

기관지염, 특히 호산구성 기관지염(eosinophilic bronchitis)은 알레르기성 기도 염증과 병태생리학적으로 관련이 있어, 동일한 항IgE 기전이 이론적으로 적용될 가능성이 있습니다. 실제로 등록된 임상시험 중 하나(NCT02049294)는 천식을 동반한 지속성 호산구성 기관지염 환자를 대상으로 스테로이드 절감 효과를 평가한 바 있습니다.

다만 확보된 근거 대부분은 기관지염이 아닌 천식 환자를 대상으로 한 연구이며, "chronic bronchitis"라는 용어도 천식-COPD 중복증후군(ACO)의 공존 질환으로 언급되는 데 그쳐, 기관지염 자체를 1차 목표로 설계된 검증적 임상시험은 부족한 상태입니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | 완료 | 11 | 천식 동반 지속성 호산구성 기관지염 환자에서 Omalizumab 병용 시 프레드니손 감량 효과 평가(무작위, 이중맹검, 위약대조) |
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Phase 2b | 완료 | 382 | 만성 자발성 두드러기(CSU) 대상 용량탐색 시험 — 기관지염 전용 적응증 아님, 참고 목적으로만 관련 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | Cohort | Postepy Dermatol Alergol | 중년·고령 중증 알레르기 천식-COPD 중복(overlap) 환자에서 생물학적 치료 유용성 |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Review | Masui | 기관지 천식/만성 기관지염 환자의 수술 전 관리, Omalizumab 언급 |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Expert Opinion | Expert Opin Pharmacother | 흡연 관련 기도질환(만성 기관지염, 폐기종 등)을 동반한 천식 관리의 난제 |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Case report | J Investig Allergol Clin Immunol | 기관지 열성형술 후 발생한 희귀 플라스틱 기관지염 사례(IgE 기전과 직접 관련 없음) |
| [21163396](https://pubmed.ncbi.nlm.nih.gov/21163396/) | 2010 | Review | Rev Mal Respir | 성인 천식 악화의 정의·병태생리·치료 고찰 |
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Review | Clin Rev Allergy Immunol | Omalizumab의 천식 승인 및 시판 후 경험 |
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | Pooled analysis | Curr Med Res Opin | 소아 알레르기 천식 환자에서 Omalizumab의 안전성·내약성 |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | Review | Allergol Immunopathol | 소아과 영역 단클론항체 사용(예방·치료) 개괄 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> ⚠ 한국 식약처(또는 TFDA) 공식 경고·금기 자료가 확보되지 않아(DG001, Blocking) 초기 안전성 평가(S1) 진행이 불가능한 상태입니다. 약물 상호작용(DDI) 자료도 조회되지 않았습니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
현재 근거는 대부분 천식 환자를 대상으로 한 연구이며, 기관지염을 1차 목표로 설계된 검증적 임상시험은 1건(NCT02049294, N=11)에 불과합니다. 근거 수준이 L4(전임상/기전 수준)에 그치고, 공식 안전성 자료(경고·금기)가 전혀 확보되지 않아 초기 안전성 평가(S1) 진입 자체가 불가능한 상태입니다.

**진행하려면 필요한 것:**
- TFDA/한국 식약처 공식 허가사항(경고·금기사항) 확보 — Blocking 항목(DG001)
- DrugBank 등 공식 MOA 자료 확보(DG002)
- 기관지염(특히 호산구성 기관지염)을 1차 목표(primary endpoint)로 설계한 전향적 검증 임상시험
- 한국 내 허가·시판 현황 확인(현재 0건, 미시판)

> 참고: 동일 Evidence Pack 내 예측 적응증 중 **알레르기성 천식(allergic asthma)**은 근거 수준 L1(Phase 3 RCT 다수, "Proceed with Guardrails" 권고)로 가장 강한 근거를 보유하고 있어, 이 약물의 재평가/재창출 우선순위 검토 시 별도로 함께 고려할 가치가 있습니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

