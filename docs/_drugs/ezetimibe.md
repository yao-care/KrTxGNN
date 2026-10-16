---
layout: default
title: Ezetimibe
parent: 높은 근거 (L1-L2)
nav_order: 336
evidence_level: L1
indication_count: 4
last_modified_at: 2026-10-15
description: "Ezetimibe: 예측 신규 적응증 고지단백혈증 (Hyperlipoproteinemia) (근거 수준 L1). 기존 적응증: 허가 적응증 원문은 문서 링크로만 제공되어 확인되지 않음 (일차 고콜레스테롤혈증 및 혼합형 고지질혈증으로 추정)"
---

# Ezetimibe
{: .fs-9 }

근거 수준: **L1** | 예측 적응증: **4** 건
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

# Ezetimibe: 고콜레스테롤혈증에서 고지단백혈증으로

## 한 문장 요약

Ezetimibe는 장내 콜레스테롤 흡수를 억제하는 약물로, 원래 고콜레스테롤혈증 및 고지질혈증 치료에 사용되어 왔습니다.
TxGNN 모델은 **고지단백혈증(hyperlipoproteinemia)**에 효과가 있을 수 있다고 예측하며, 이번 보고서에 수집된 자료 기준으로 **40건의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다.
다만 이 예측은 기존 적응증과 사실상 같은 범주이므로 엄밀한 의미의 재창출 후보는 아닙니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 원문은 문서 링크로만 제공되어 확인되지 않음 (일차 고콜레스테롤혈증 및 혼합형 고지질혈증으로 추정) |
| 예측 신규 적응증 | 고지단백혈증 (Hyperlipoproteinemia) |
| TxGNN 예측 점수 | 99.63% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 |
| 권장 결정 | Proceed with Guardrails |

> 참고: 이 보고서의 다른 예측 적응증 중 가장 근거가 두터운 것은 고지단백혈증(1순위)과 가족성 고콜레스테롤혈증(2순위)입니다. 3~4순위(CYP7A1 결핍 고콜레스테롤혈증, CETP 결핍)는 근거 수준 L5, 권장 결정 Hold입니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 수집되지 않았습니다. 알려진 정보에 따르면 ezetimibe는 소장 상피의 NPC1L1 단백질을 통한 콜레스테롤 흡수를 억제하여 LDL 콜레스테롤(LDL-C)을 낮춥니다. 이는 고지단백혈증/고지질혈증의 병태와 직접 연결됩니다.

다만 이 예측은 약물의 기존 허가 적응증(일차 고콜레스테롤혈증, 혼합형 고지질혈증)과 사실상 일치합니다. 따라서 TxGNN 점수가 높은 것은 이미 알려진 기전과 승인된 용도를 반영한 결과로 보는 것이 타당하며, 새로운 용도를 발견했다는 의미는 아닙니다.

## 임상시험 근거

수집된 시험 중 관련성이 높은 대표 10건입니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01984424](https://clinicaltrials.gov/study/NCT01984424) | Phase 3 | 완료 | 511 | 스타틴 불내성 고콜레스테롤혈증에서 evolocumab vs ezetimibe 비교 (ezetimibe는 대조군) |
| [NCT03847506](https://clinicaltrials.gov/study/NCT03847506) | Phase 4 | 완료 | 127 | 본태성 고혈압 및 고지질혈증에서 ezetimibe/rosuvastatin 병용 효능·안전성 |
| [NCT00753883](https://clinicaltrials.gov/study/NCT00753883) | Phase 4 | 완료 | 40 | 고콜레스테롤혈증에서 ezetimibe 단독 vs 스타틴의 지질 강하 효과 비교 (소규모, 공개 label) |
| [NCT00092833](https://clinicaltrials.gov/study/NCT00092833) | Phase 3 | 종료 | 49 | 동형접합 가족성 고콜레스테롤혈증/시토스테롤혈증에서 ezetimibe 10 mg 치료 사용 연구 |
| [NCT00705211](https://clinicaltrials.gov/study/NCT00705211) | N/A | 완료 | 1,794 | 일본 Zetia 52주 시판 후 장기 조사 (관찰연구) |
| [NCT00271817](https://clinicaltrials.gov/study/NCT00271817) | Phase 3 | 완료 | 1,220 | IIa/IIb형 고지질혈증에서 ezetimibe/simvastatin과 niacin 병용 |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Phase 3 | 완료 | 576 | 혼합형 고지질혈증에서 fenofibrate + ezetimibe 병용 |
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Phase 3 | 완료 | 611 | 혼합형 고지질혈증에서 ezetimibe/simvastatin + fenofibrate 병용 |
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | 완료 | 720 | ENHANCE: 이형접합 가족성 고콜레스테롤혈증에서 ezetimibe + simvastatin vs simvastatin 단독의 경동맥 동맥경화 진행 |
| [NCT06005597](https://clinicaltrials.gov/study/NCT06005597) | Phase 3 | 완료 | 407 | obicetrapib 10 mg + ezetimibe 10 mg 고정용량 복합제 vs 위약 |

가족성 고콜레스테롤혈증(2순위 예측)에 대해서는 ezetimibe를 직접 평가한 Phase 3 시험 [NCT03884452](https://clinicaltrials.gov/study/NCT03884452)(n=50), [NCT03885921](https://clinicaltrials.gov/study/NCT03885921)(n=44, 장기 안전성), [NCT00867165](https://clinicaltrials.gov/study/NCT00867165)(소아, 위약 대조, n=138)가 있습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | RCT | JAMA | 이형접합 가족성 고콜레스테롤혈증에서 경구 PCSK9 억제제 enlicitide의 효능·안전성 |
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | RCT (Phase 3) | Lancet | obicetrapib + ezetimibe 고정용량 복합제의 LDL-C 감소 (TANDEM) |
| [25282519](https://pubmed.ncbi.nlm.nih.gov/25282519/) | 2015 | RCT | Lancet | 이형접합 가족성 고콜레스테롤혈증에서 evolocumab의 LDL-C 감소 (RUTHERFORD-2) |
| [37850379](https://pubmed.ncbi.nlm.nih.gov/37850379/) | 2024 | RCT | Circulation | 동형접합 가족성 고콜레스테롤혈증에서 inclisiran (ORION-5) |
| [35101175](https://pubmed.ncbi.nlm.nih.gov/35101175/) | 2022 | 코호트 | Lancet | 동형접합 가족성 고콜레스테롤혈증의 전 세계 임상 경험 |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Review | J Am Coll Cardiol | 스타틴·ezetimibe·PCSK9 억제제 기반의 신규 LDL-C 강하 요법 |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Review | Mol Med Rep | 고지질혈증 표적 약물의 연구 동향 |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Review | Cardiol Clin | 가족성 고콜레스테롤혈증: ezetimibe를 포함한 LDL-C 강하 치료 개관 |
| [23956253](https://pubmed.ncbi.nlm.nih.gov/23956253/) | 2013 | 합의문 | Eur Heart J | 가족성 고콜레스테롤혈증의 과소진단·과소치료와 선별·치료 지침 |
| [14727947](https://pubmed.ncbi.nlm.nih.gov/14727947/) | 2003 | Review | Am J Cardiovasc Drugs | Ezetimibe 약리 및 임상 효능 개관 |

참고로 위 문헌 중 다수는 ezetimibe가 아닌 다른 약물(PCSK9 억제제 등)의 시험이거나 질환 개관이며, ezetimibe 자체의 효능을 직접 입증하는 문헌은 제한적입니다.

## 한국 시판 정보

20건의 허가가 모두 유효하며, 대부분 스타틴(로수바스타틴, 아토르바스타틴, 심바스타틴 등)과의 복합제입니다. 허가 적응증 원문은 문서 링크로만 제공되어 요약하지 못했습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201701413 | 에제스롤정 (에제티미브 단일) | 흰색 내지 거의 흰색의 장방형 정제 | 허가증 원문 참조 |
| 201500366 | 아토젯정 10/80mg (한국오가논) | 필름코팅정 | 허가증 원문 참조 |
| 201007235 | 이지심바정 10/10mg (에제티미브+심바스타틴) | 정제 | 허가증 원문 참조 |
| 201606048 | 슈바젯정 10/20mg (에제티미브+로수바스타틴) | 필름코팅정 | 허가증 원문 참조 |
| 202402807 | 암로젯정 10/5/10mg (암로디핀+로수바스타틴+에제티미브) | 필름코팅정 | 허가증 원문 참조 |

## 안전성 고려사항

허가사항의 경고·금기 정보는 이번 수집 자료에 포함되지 않았으므로 안전성 정보는 허가사항을 참조하세요.

- **지식그래프 기반 금기 관련 질환** (허가 문서가 아닌 약물-질환 관계 데이터 기준): 췌장염, 간질환, 담낭질환, 근병증, 근육질환, 골격근질환, 가족성 주기성 마비, 약물 남용/의존, 횡문근융해증, 결절성 근막염
- **약물 상호작용** (총 100건 조회 중 중등도 4건): chenodeoxycholic acid, eluxadoline, rosuvastatin, simvastatin. 그 외 calcitriol, pantoprazole, glimepiride, metformin, omeprazole 등은 등급이 불명확합니다.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
고지단백혈증에 대해 완료된 Phase 3 시험이 다수 있고 한국에서 20건이 시판 중이므로 근거 수준은 L1입니다. 다만 이는 사실상 기존 적응증이므로 새로운 재창출이라기보다 기존 용도의 확인에 해당합니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기) 원문 확인: 현재 허가 문서 내용이 수집되지 않았음
- 작용 기전(MOA) 데이터 보완
- 가족성 고콜레스테롤혈증 등은 전문의 관리하에 스타틴 또는 PCSK9 억제제, bempedoic acid와의 병용 전략 검토
- 스타틴 병용 시 근병증·간기능 모니터링 계획 수립
- 3~4순위 예측(CYP7A1 결핍, CETP 결핍)은 근거가 전임상 1건 수준이거나 치료적 근거가 불분명하여 Hold 유지
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

