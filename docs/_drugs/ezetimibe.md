---
layout: default
title: Ezetimibe
parent: 僅模型預測 (L5)
nav_order: 312
evidence_level: L5
indication_count: 4
---

# Ezetimibe
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Ezetimibe: 적응증 자료 미비 상태에서 고지단백혈증(Hyperlipoproteinemia)으로

## 한 문장 요약

Ezetimibe는 소장 NPC1L1 수용체를 억제해 콜레스테롤 흡수를 차단하는 약물이지만, 이번 평가 팩에는 원 적응증과 작용기전(MOA) 등록 정보가 남아 있지 않습니다. TxGNN 모델은 **고지단백혈증(Hyperlipoproteinemia)**에 대해 **99.63%**의 예측 점수를 부여했으며, 현재 **50건의 임상시험**과 **19편의 문헌**이 이를 뒷받침합니다. 다만 근거 자체는 ezetimibe가 이미 널리 쓰이는 콜레스테롤 저하 용도와 겹쳐 있어, 엄밀한 의미의 '노 드럭-뉴 유즈'보다는 기존 약효 범주의 재확인에 가깝다는 점에 유의해야 합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 등록된 자료 없음 (원 적응증·한국 허가증 정보 부재) |
| 예측 신규 적응증 | 고지단백혈증 (Hyperlipoproteinemia) |
| TxGNN 예측 점수 | 99.63% |
| 근거 수준 | L1 |
| 한국 시판 현황 | 미상장 (시판되지 않음) |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

DrugBank 기반 공식 MOA 필드는 현재 등록되어 있지 않습니다. 다만 예측 근거 데이터에 따르면, Ezetimibe는 소장 융모 상피 자락막의 **NPC1L1 수송단백질**을 억제하여 식이·담즙 유래 콜레스테롤의 장내 흡수를 차단하고, 이를 통해 LDL-C 및 apoB 수치를 낮추는 것으로 알려져 있습니다. 이 기전은 고지단백혈증 치료와 직접적으로 대응됩니다.

다만 중요한 유의점이 있습니다: 이 예측은 Ezetimibe가 이미 널리 승인·처방되고 있는 콜레스테롤 저하 용도 범주에 해당하며, 전형적인 '노 드럭-뉴 유즈(약물 재창출)' 사례로 보기 어렵습니다. 입력 데이터의 `original_indications`가 비어 있고 `original_moa`도 자료 결손으로 표시되어 있어, 이번 평가는 원 적응증과의 비교 없이 현재 보유한 근거만으로 독립적으로 수행되었습니다. 따라서 본 결과는 재창출 후보라기보다 기존 약효 범주에 대한 근거 재확인으로 해석하는 것이 더 정확합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00704444](https://clinicaltrials.gov/study/NCT00704444) | N/A | 완료 | 11,332 | Zetia(에제티미브) 10mg의 일본 대규모 시판후 관찰연구, 12주간 단독·병용요법의 안전성·유효성 확인 |
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Phase 3 | 완료 | 611 | Ezetimibe/Simvastatin과 Fenofibrate 병용요법의 혼합형 고지혈증 콜레스테롤 저하 효과 평가 |
| [NCT00655265](https://clinicaltrials.gov/study/NCT00655265) | Phase 4 | 완료 | 86 | 스타틴+에제티미브 병용 중인 가족성 고콜레스테롤혈증 환자에 Colesevelam 추가투여 시 LDL-C 추가 저하 효과 평가 |
| [NCT00092560](https://clinicaltrials.gov/study/NCT00092560) | Phase 3 | 완료 | 587 | Fenofibrate와 Ezetimibe 병용투여의 혼합형 고지혈증 치료 효과·안전성 평가 |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Phase 3 | 완료 | 576 | Fenofibrate+Ezetimibe 병용요법, 혼합형 고지혈증 대상 반복 검증 시험 |
| [NCT00349284](https://clinicaltrials.gov/study/NCT00349284) | Phase 3 | 완료 | 181 | Fenofibrate 145mg, Ezetimibe 10mg 단독 및 병용요법 비교, Type IIb 이상지질혈증·대사증후군 동반 환자 대상 |
| [NCT00271817](https://clinicaltrials.gov/study/NCT00271817) | Phase 3 | 완료 | 1,220 | Ezetimibe/Simvastatin과 나이아신 서방정 병용투여, Type IIa/IIb 고지혈증 환자 대상 유효성·안전성 평가 |
| [NCT00203476](https://clinicaltrials.gov/study/NCT00203476) | Phase 4 | 완료 | 30 | 스타틴 최대내약용량에 Ezetimibe·나이아신·콜레스티폴을 추가한 보조요법 간 LDL 저하 효과 비교 |
| [NCT00753883](https://clinicaltrials.gov/study/NCT00753883) | Phase 4 | 완료 | 40 | Ezetimibe 단독요법과 스타틴 단독요법의 고콜레스테롤혈증 치료 효과 비교 |
| [NCT00705211](https://clinicaltrials.gov/study/NCT00705211) | N/A | 완료 | 1,794 | Zetia(에제티미브) 10mg의 일본 52주 장기 시판후 사용성적조사 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | RCT | Lancet | Obicetrapib·Ezetimibe 고정용량복합제(TANDEM)의 LDL-C 저하 효능 평가 3상 RCT |
| [37762244](https://pubmed.ncbi.nlm.nih.gov/37762244/) | 2023 | Review | Int J Mol Sci | 식후 고지혈증의 병태생리, 진단, 죽상경화 기전 및 치료법 종합 리뷰 |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Review | Mol Med Rep | 고지혈증 표적 치료제 최신 연구 동향 리뷰 |
| [35593194](https://pubmed.ncbi.nlm.nih.gov/35593194/) | 2022 | Review | J Cardiovasc Pharmacol Ther | PCSK9 억제제 종합 리뷰, 스타틴·에제티미브 불충분 반응군 치료전략 논의 |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Review | Cardiology Clinics | 가족성 고콜레스테롤혈증 개관: 스타틴, 에제티미브 등 LDL-C 저하 치료 옵션 정리 |
| [34480646](https://pubmed.ncbi.nlm.nih.gov/34480646/) | 2021 | Review | Curr Cardiol Rep | 가족성 고콜레스테롤혈증의 전세계적 질병 부담과 관리전략 리뷰 |
| [29219151](https://pubmed.ncbi.nlm.nih.gov/29219151/) | 2017 | Review | Nat Rev Dis Primers | 가족성 고콜레스테롤혈증 병태·진단·치료 종합 개관 |
| [23956253](https://pubmed.ncbi.nlm.nih.gov/23956253/) | 2013 | Review | Eur Heart J | 유럽동맥경화학회 가족성 고콜레스테롤혈증 과소진단·과소치료 합의문 |
| [30702994](https://pubmed.ncbi.nlm.nih.gov/30702994/) | 2019 | Review | Circulation Research | 콜레스테롤 저하제(PCSK9 포함) 전반 리뷰 |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Review | J Am Coll Cardiol | LDL-C·ApoB 감소를 위한 신규·차세대 치료제 리뷰 |

## 한국 시판 정보

현재 한국에 등록된 Ezetimibe 허가 제품이 없습니다 (미상장, 허가증 0건).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
고지단백혈증에 대한 근거 수준은 L1(50건 임상시험, 다수의 Phase 3 RCT 포함)로 매우 높으나, 이 예측이 Ezetimibe의 기존 콜레스테롤 저하 용도와 실질적으로 겹친다는 점에서 '신규 재창출'로서의 가치는 제한적입니다. 또한 한국 라벨 경고·금기(DG001, Blocking 등급)와 공식 MOA(DG002) 정보가 없어 안전성 초기 평가(S1) 단계에 아직 진입할 수 없는 상태입니다.

**진행하려면 필요한 것:**
- MFDS(식약처) 원본 허가 라벨의 경고·금기사항 확보 (DG001, Blocking — 안전성 평가 진입 필수조건)
- DrugBank API를 통한 공식 MOA 데이터 확보 (DG002)
- 한국 내 실제 허가·시판 현황 재확인 (현재 데이터상 미상장으로 표기됨)
- 예측이 기존 승인 용도와 중복되는지 여부를 원 적응증 자료 확보 후 재검증
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

