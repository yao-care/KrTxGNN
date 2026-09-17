---
layout: default
title: Fluvastatin
parent: 높은 근거 (L1-L2)
nav_order: 336
evidence_level: L1
indication_count: 10
---

# Fluvastatin
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

# Fluvastatin: 고콜레스테롤혈증에서 고지질단백혈증(Hyperlipoproteinemia)으로

## 한 문장 요약

Fluvastatin은 HMG-CoA 환원효소를 억제하는 스타틴 계열 약물로, 원래 고콜레스테롤혈증(고지혈증) 치료에 사용되어 왔습니다.
TxGNN 모델은 **고지질단백혈증(Hyperlipoproteinemia)**에도 효과가 있을 것으로 예측하며, 현재 **5건의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다.
다만 예측 근거 자체가 밝히듯, 이는 스타틴 계열 약물의 핵심(표준) 적응증과 사실상 동일한 영역이어서 완전히 새로운 재창출이라기보다 기존 효능의 재확인에 가깝습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (한국 허가 정보 미확보, 미출시) |
| 예측 신규 적응증 | 고지질단백혈증 (Hyperlipoproteinemia) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L1 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

DrugBank 기준 상세 MOA 데이터는 아직 확보되지 않았습니다(Data Gap). 다만 예측 근거 자료에 따르면, Fluvastatin은 HMG-CoA 환원효소를 억제하여 간에서 LDL/VLDL 콜레스테롤 합성을 저하시키는 것으로 알려져 있으며, 이는 스타틴 계열 약물의 표준 작용 기전입니다.

고지질단백혈증은 LDL·VLDL 등 지단백 이상을 특징으로 하는 질환군으로, 스타틴의 콜레스테롤 합성 억제 기전이 그대로 적용되는 영역입니다. 실제로 아래 근거들을 보면 Fluvastatin은 이미 다양한 고지혈증 아형(혼합형, 가족성 등)에서 반복적으로 연구되어 왔습니다.

단, 예측 근거 자체에 "이는 스타틴 계열 약물의 핵심 적응증이지 새로운 재창출 영역이 아니다"라는 평가가 명시되어 있어, 이번 예측은 진정한 의미의 '신규 적응증 발굴'보다는 이미 확립된 약효 영역의 재확인 성격이 강하다는 점에 유의해야 합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00726362](https://clinicaltrials.gov/study/NCT00726362) | N/A | 완료 | 3270 | 로수바스타틴·아토르바스타틴·심바스타틴·로바스타틴·프라바스타틴·플루바스타틴 등 시판 스타틴의 실제 임상에서의 고지혈증 치료 효과를 비교한 대규모 관찰 연구 (Grade A: fluvastatin 직접 포함) |
| [NCT01634906](https://clinicaltrials.gov/study/NCT01634906) | N/A | 완료 | 55 | 스타틴 중단 후 적혈구 결합 apolipoprotein B(ery-apoB) 변화 평가, 스타틴 계열 공통 기전과 직접 관련 (Grade B) |
| [NCT00532311](https://clinicaltrials.gov/study/NCT00532311) | Phase 3 | 중단 | 411 | 스쿠알렌 합성효소 억제제(lapaquistat acetate)와 스타틴 병용 시 콜레스테롤 강하 효과 평가 — fluvastatin 자체 시험은 아니며 동일 기전 계열 참고용 (Grade C) |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | 완료 | 18 | 소아·청소년 동형접합 가족성 고콜레스테롤혈증에서 alirocumab 평가 — fluvastatin 직접 근거 아님 (Grade C) |
| [NCT04608474](https://clinicaltrials.gov/study/NCT04608474) | Phase 4 | 불명 | 120 | 신장이식 환자 대상 evolocumab(PCSK9 억제제) 지질관리 연구 — fluvastatin 직접 근거 아님 (Grade C) |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [10856536](https://pubmed.ncbi.nlm.nih.gov/10856536/) | 2000 | RCT | Atherosclerosis | 혼합형 고지혈증 환자에서 fluvastatin+bezafibrate 병용요법의 효능·안전성 평가 (FACT study, n=333) |
| [11219479](https://pubmed.ncbi.nlm.nih.gov/11219479/) | 2001 | RCT | Clinical Therapeutics | 원발성 고콜레스테롤혈증에서 fluvastatin 서방형(ER) vs 속방형(IR) 제형 효능·내약성 비교 |
| [15598476](https://pubmed.ncbi.nlm.nih.gov/15598476/) | 2004 | RCT | Clinical Therapeutics | 혼합형 고지혈증·제2형 당뇨·관상동맥질환 환자에서 fluvastatin+fenofibrate 병용 vs fluvastatin 단독요법 12개월 비교 |
| [8157036](https://pubmed.ncbi.nlm.nih.gov/8157036/) | 1993 | RCT | Eur J Clin Pharmacol | 가족성 고콜레스테롤혈증 환자에서 고용량 fluvastatin의 효능·안전성 이중맹검 연구 (n=52) |
| [8967021](https://pubmed.ncbi.nlm.nih.gov/8967021/) | 1996 | 연구 | Vnitrni lekarstvi | 고지질단백혈증(hyperlipoproteinemia) 치료에서 fluvastatin의 초기 임상 경험 |
| [10067240](https://pubmed.ncbi.nlm.nih.gov/10067240/) | 1998 | Cohort | Terapevticheskii arkhiv | 원발성 고지질단백혈증에서 simvastatin과 fluvastatin의 지질 강하 효과 변동성 비교 |
| [7604789](https://pubmed.ncbi.nlm.nih.gov/7604789/) | 1995 | Cohort | Am J Cardiol | 중국인 고콜레스테롤혈증 환자에서 fluvastatin의 지질 프로파일·아포지단백 효과 |
| [9271817](https://pubmed.ncbi.nlm.nih.gov/9271817/) | 1997 | 연구 | Thrombosis Research | Type IIA/IIB 고지혈증 및 급성 심근경색 환자에서 fluvastatin과 조직인자 경로억제제(TFPI) 관계 |
| [17062478](https://pubmed.ncbi.nlm.nih.gov/17062478/) | 2006 | 연구 | Acta Paediatrica | 이형접합 가족성 고콜레스테롤혈증 소아·청소년에서 fluvastatin 효능·안전성 |
| [11347136](https://pubmed.ncbi.nlm.nih.gov/11347136/) | 2001 | Review | Nihon Rinsho | Fluvastatin 전반에 대한 일본어 종설 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
고지질단백혈증에 대한 근거 수준은 L1로, 대규모 실사용 비교 연구(NCT00726362, n=3270)와 다수의 fluvastatin 직접 RCT(가족성/혼합형 고지혈증 등)가 이를 뒷받침합니다. 다만 예측 근거 자체가 밝히듯 이는 스타틴의 기존 핵심 적응증과 사실상 동일하여, '신규 재창출'이라기보다 기존 효능의 확인에 가깝습니다.

**진행하려면 필요한 것:**
- TFDA(현지 규제기관) 앞표시 경고·금기사항 확보 (DG001, Blocking — 안전성 초기평가 진입에 필수)
- DrugBank 기반 상세 MOA 데이터 확보 (DG002)
- 한국(현지) 시판 및 허가 현황 확인 — 현재 미출시로 등록 정보 부재
- DDI(약물상호작용) 데이터 확보 — 현재 조회 결과 없음
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

