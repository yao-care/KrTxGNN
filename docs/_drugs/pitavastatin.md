---
layout: default
title: Pitavastatin
parent: 모델 예측만 (L5)
nav_order: 607
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Pitavastatin: 예측 신규 적응증 폐지된 용어로 분류된 가족성 복합 고지혈증 / 고지단백혈증 (근거 수준 L5). 기존 적응증: 확인 불가 (허가 적응증이 PDF 링크로만 제공됨)"
monitor_inn: "Pitavastatin"
predicted_indications: ["homozygous familial hypercholesterolemia", "hyperlipoproteinemia", "familial hypercholesterolemia", "cholesterol-ester transfer protein deficiency", "hypercholesterolemia, autosomal dominant", "hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency", "HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Pitavastatin
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

# Pitavastatin: 이상지질혈증에서 고지단백혈증(HIV 환자의 심혈관 예방 포함)으로

## 한 문장 요약

Pitavastatin은 HMG-CoA 환원효소 억제제(스타틴)로, 한국에서 20건의 단일 성분 허가를 받아 시판 중입니다. 다만 허가 적응증 원문은 이번 자료에 텍스트로 포함되어 있지 않습니다.
TxGNN 모델은 상위 예측 질환으로 **고지단백혈증(Hyperlipoproteinemia)**을 제시하며, 이 질환에는 **9건의 임상시험**과 **17편의 문헌**이 연결되어 있습니다.
다만 이 예측은 기존 지질강하 적응증과 거의 겹쳐 진정한 재창출이라기보다 허가 범위 내 사용에 가깝습니다. 실질적인 신규 방향은 **HIV 환자의 심혈관질환 예방**(REPRIEVE 시험)입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 적응증이 PDF 링크로만 제공됨) |
| 예측 신규 적응증 | 폐지된 용어로 분류된 가족성 복합 고지혈증 (obsolete familial combined hyperlipidemia, 1순위) / 고지단백혈증 (3순위, 근거 가장 충실) |
| TxGNN 예측 점수 | 1순위 99.998% (고지단백혈증은 99.995%) |
| 근거 수준 | 1순위 L5 / 고지단백혈증 L1 / HIV 감염증 L1 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 (모두 유효, 단일 성분) |
| 권장 결정 | 1순위: Hold / 고지단백혈증·HIV 심혈관 예방: Proceed with Guardrails |

> 참고: 1순위 예측은 폐지된 질환 용어이며 임상시험과 문헌이 전혀 없습니다. 아래에서는 근거가 있는 3순위(고지단백혈증)를 중심으로 정리하고, 근거가 가장 뚜렷한 HIV 관련 예측(9순위)을 함께 다룹니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Pitavastatin은 스타틴 계열로, HMG-CoA 환원효소를 억제해 LDL 콜레스테롤과 apoB 함유 지단백을 낮춥니다. 한국에서는 단일제 외에 ezetimibe 복합제(타바로젯), fenofibrate 복합제(타바페노, 리바페논 등)도 허가되어 있어 지질 이상 치료에 널리 쓰이는 약물임을 알 수 있습니다.

고지단백혈증은 이 약의 기본 작용과 정확히 맞닿아 있습니다. 따라서 이 예측은 신규 적응증이라기보다 기존 지질강하 사용과 같은 영역입니다. 다양한 임상시험과 문헌이 효능과 안전성을 뒷받침합니다.

반면 다른 예측 중에는 기전상 근거가 약한 것이 많습니다. 호모접합 가족성 고콜레스테롤혈증은 LDL 수용체 기능이 거의 없어 스타틴 반응이 제한적입니다. CETP 결핍은 HDL이 높은 상태라 LDL 강하 치료가 필요하지 않습니다. LPL 관련 복합 고지혈증은 중성지방 제거 장애가 원인이라 스타틴의 효과가 작습니다. 희귀 신경발달장애는 기전적 연결고리를 찾을 수 없습니다.

HIV 예측은 HIV 자체의 치료가 아니라, 만성 염증과 항레트로바이러스제로 높아진 심혈관 위험을 낮추는 것입니다. REPRIEVE 시험(NEJM 2023)에서 Pitavastatin이 HIV 환자의 주요 심혈관 사건을 약 35% 줄였습니다. 이는 지질강하와 항염증 작용(다면 효과)이 함께 작용한 결과로 해석됩니다. Pitavastatin은 CYP450 의존 대사가 적어 항레트로바이러스제와의 상호작용 면에서도 유리합니다.

## 임상시험 근거

고지단백혈증(3순위) 관련 시험입니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01386853](https://clinicaltrials.gov/study/NCT01386853) | Phase 3 | 불명 | 200 | 고위험 고콜레스테롤혈증 환자에서 Pitavastatin vs Atorvastatin 12주 비열등성 시험 (이중맹검) |
| [NCT01256476](https://clinicaltrials.gov/study/NCT01256476) | Phase 4 | 완료 | 328 | 원발성 고지혈증·혼합형 이상지질혈증에서 Pitavastatin 4 mg vs Pravastatin 40 mg (이중맹검) |
| [NCT01166633](https://clinicaltrials.gov/study/NCT01166633) | Phase 4 | 완료 | 200 | 경증~중등도 간 손상 동반 고콜레스테롤혈증에서 Pitavastatin vs Atorvastatin 용량 적정 (공개 라벨) |
| [NCT02056847](https://clinicaltrials.gov/study/NCT02056847) | Phase 4 | 완료 | 313 | 공복혈당장애 동반 고지혈증에서 Pitavastatin 2 mg vs 4 mg의 HbA1c 변화 비교 |
| [NCT00711919](https://clinicaltrials.gov/study/NCT00711919) | 해당 없음 | 불명 | 300 | 고지혈증과 경동맥 내중막 비후 환자에서 집중 지질강하 요법의 동맥경화 퇴행 효과 |
| [NCT01695954](https://clinicaltrials.gov/study/NCT01695954) | Phase 1 | 완료 | 34 | Efavirenz, darunavir/ritonavir와의 약동학적 상호작용 |
| [NCT02634034](https://clinicaltrials.gov/study/NCT02634034) | Phase 1 | 완료 | 18 | 서방형(CR)과 속방형(IR) Pitavastatin의 약동학·안전성 비교 (건강인) |
| [NCT01764178](https://clinicaltrials.gov/study/NCT01764178) | Phase 1 | 완료 | 52 | Pitavastatin+Valsartan 병용투여와 복합제의 약동학 비교 |
| [NCT01406431](https://clinicaltrials.gov/study/NCT01406431) | Phase 1 | 완료 | 48 | 위와 동일 설계의 약동학 비교 시험 |

HIV 예측(9순위) 관련 시험입니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT06317051](https://clinicaltrials.gov/study/NCT06317051) | Phase 3/4 | 진행 중 (모집 종료) | 300 | 대사 위험이 높은 HIV 환자에서 dapagliflozin 추가 및 rosuvastatin/ezetimibe vs Pitavastatin 요인 설계 시험 |

가족성 고콜레스테롤혈증(5순위)과 상염색체 우성 고콜레스테롤혈증(7순위)에 연결된 NCT01890967(Phase 2, 527명)은 다른 약물(LY3015014)의 시험이므로 Pitavastatin의 직접 근거가 아닙니다.

## 문헌 근거

고지단백혈증(3순위)에 연결된 문헌 중 관련성이 높은 것입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [25891210](https://pubmed.ncbi.nlm.nih.gov/25891210/) | 2016 | 임상시험 | J Atheroscler Thromb | 일본 남아 이형접합 가족성 고콜레스테롤혈증에서 Pitavastatin의 효능·안전성 |
| [29187694](https://pubmed.ncbi.nlm.nih.gov/29187694/) | 2018 | 임상시험 | J Atheroscler Thromb | 일본과 유럽의 소아·청소년 가족성 고콜레스테롤혈증에서 효능·안전성 비교 |
| [23672789](https://pubmed.ncbi.nlm.nih.gov/23672789/) | 2013 | 비교 임상연구 | J Cardiol | 이상지질혈증 및 관상동맥질환에서 Pitavastatin vs Atorvastatin의 HDL-C·아디포넥틴 상승 효과 비교 (COMPACT-CAD) |
| [17957184](https://pubmed.ncbi.nlm.nih.gov/17957184/) | 2008 | 교차 연구 | Clin Pharmacol Ther | 이형접합 FH 19명에서 Pitavastatin과 Atorvastatin이 LDL-C를 비슷하게 감소(약 -43% vs -41%), 혈장 CoQ10 비교 |
| [12048134](https://pubmed.ncbi.nlm.nih.gov/12048134/) | 2002 | 장기 임상연구 | Atherosclerosis | 이형접합 FH 25명 최대 104주 투여, 총콜레스테롤 약 31% 감소 |
| [21951922](https://pubmed.ncbi.nlm.nih.gov/21951922/) | 2011 | 공개 라벨 파일럿 | Hepatol Res | 이상지질혈증 동반 NASH에서 Pitavastatin의 효능 |
| [12822207](https://pubmed.ncbi.nlm.nih.gov/12822207/) | 2003 | Review | Therapie | 신규 지질강하제 전망 |

HIV 예측(9순위)에 연결된 핵심 문헌입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [37486775](https://pubmed.ncbi.nlm.nih.gov/37486775/) | 2023 | RCT (Phase 3, REPRIEVE) | N Engl J Med | HIV 감염인의 심혈관질환 1차 예방에서 Pitavastatin 효과 |
| [38381407](https://pubmed.ncbi.nlm.nih.gov/38381407/) | 2024 | RCT 하위연구 | JAMA Cardiol | Pitavastatin이 주요 심혈관 사건을 35% 감소시켰고, 관상동맥 플라크와 염증 바이오마커 변화를 분석 |
| [40482662](https://pubmed.ncbi.nlm.nih.gov/40482662/) | 2025 | RCT 2차 분석 | Lancet HIV | 항레트로바이러스제 사용과 주요 심혈관 사건의 연관성 |
| [39661372](https://pubmed.ncbi.nlm.nih.gov/39661372/) | 2025 | RCT 2차 분석 | JAMA Cardiol | 프로콜라겐 경로와 플라크 안정화 |
| [38294226](https://pubmed.ncbi.nlm.nih.gov/38294226/) | 2025 | Review | Cardiol Rev | HIV 환자의 심혈관질환 예방에서 Pitavastatin 고찰 |
| [28416195](https://pubmed.ncbi.nlm.nih.gov/28416195/) | 2017 | RCT (Phase 4) | Lancet HIV | HIV 감염 이상지질혈증에서 Pitavastatin vs Pravastatin (INTREPID) |

호모접합 가족성 고콜레스테롤혈증(2순위)에는 직접 근거가 없습니다. 연결된 문헌은 HIV 이상지질혈증 RCT(INTREPID)와 상염색체 열성 고콜레스테롤혈증 증례 보고(39532566)뿐이며, 둘 다 해당 질환의 직접 근거가 아닙니다.

## 한국 시판 정보

허가 적응증은 이번 자료에 PDF 링크 형태로만 제공되어 텍스트로 요약할 수 없습니다. 아래는 대표 허가 5건입니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201500067 | 피타바스정 4밀리그램 (초당약품공업) | 필름코팅정 | 허가사항 참조 |
| 202301672 | 타바로젯정 2/10밀리그램 (대원제약) | 필름코팅정 | 허가사항 참조 |
| 202600585 | 타바페노서방정 (팜젠사이언스) | 서방성 필름코팅정 | 허가사항 참조 |
| 201208724 | 피타듀스정 2밀리그램 (한림제약) | 필름코팅정 | 허가사항 참조 |
| 202201915 | 로바로우정 4밀리그램 (한국휴텍스제약) | 필름코팅정 | 허가사항 참조 |

전체 20건은 모두 유효하며 취소된 허가는 없습니다. 이 중 2건은 수출용입니다.

## 안전성 고려사항

- **약물 상호작용**: 총 86건이 확인되었습니다. 주요 항목은 다음과 같습니다.
  - **Major**: Erythromycin
  - **Moderate**: Rosuvastatin, Simvastatin, Cobicistat, Eltrombopag, Metronidazole, Tinidazole, Chloroquine, Hydroxychloroquine, Disulfiram, Dapsone, Zafirlukast, Chloramphenicol, Naltrexone, Eluxadoline, Ethanol 등
  - **Minor**: Warfarin, Dicoumarol
- **모니터링 권고 (근거 분석 기반)**: 근병증과 간 효소 상승을 감시해야 합니다. cyclosporine, gemfibrozil 등은 금기이거나 제한됩니다. HIV 환자에서는 혈당 모니터링, 근육 증상, 부스터 포함 항레트로바이러스 요법(ritonavir/darunavir 등)과의 상호작용을 확인해야 합니다.

주요 경고와 금기 등 허가사항 기반 정보는 이번 자료에 포함되지 않았습니다. 상세 내용은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: 고지단백혈증 및 HIV 환자 심혈관 예방은 Proceed with Guardrails, 그 외 예측(1순위 포함)은 Hold**

**사유:**
고지단백혈증은 Phase 3와 Phase 4 비교 시험이 있으나 기존 지질강하 적응증과 사실상 같아 재창출로서의 신규성은 낮습니다. HIV 환자의 심혈관 예방은 대규모 Phase 3 RCT(REPRIEVE)가 효과를 입증해 가장 의미 있는 확장 방향입니다. 1순위(폐지된 질환 용어), LPL 관련, CETP 결핍, CYP7A1 결핍, 신경발달장애 예측은 시험과 문헌이 없고 기전도 약해 보류가 적절합니다. 호모접합 FH는 기전상 제한적이고 직접 근거가 없습니다.

**진행하려면 필요한 것:**
- 허가 적응증 원문과 경고·금기 정보 확보 (허가증 PDF 파싱)
- 작용 기전(MOA) 데이터 보완
- 한국 허가 범위에서 HIV 환자 심혈관 예방 사용의 적응증 확대 필요 여부 검토
- HIV 환자 적용 시 항레트로바이러스제 상호작용과 혈당·근육 모니터링 계획 수립
- 폐지된 질환 용어를 현행 분류 체계의 질환으로 대응시켜 재평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

