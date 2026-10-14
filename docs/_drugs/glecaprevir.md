---
layout: default
title: Glecaprevir
parent: 모델 예측만 (L5)
nav_order: 379
evidence_level: L5
indication_count: 10
---

# Glecaprevir
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

# Glecaprevir: C형 간염에서 HIV 감염으로 (모델 예측)

## 한 문장 요약

Glecaprevir는 pibrentasvir와 복합제로 사용되는 HCV NS3/4A 프로테아제 억제제로, 한국에서 C형 간염 치료제로 허가되어 시판 중입니다.
TxGNN 모델은 **HIV 감염(HIV infectious disease)**에 효과가 있을 수 있다고 예측하지만, 관련 임상시험 7건과 문헌 20편은 모두 **HIV 동반감염 환자에서의 C형 간염 치료**를 다룬 것으로, HIV 자체에 대한 효능 근거는 아닙니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | C형 간염 (허가증에는 적응증 본문 대신 허가 문서 링크만 기재되어 있음) |
| 예측 신규 적응증 | HIV 감염 (HIV infectious disease) |
| TxGNN 예측 점수 | 99.87% |
| 근거 수준 | L4 (HIV 자체에 대한 직접 근거 없음, 실질적으로는 모델 예측 수준) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 glecaprevir는 HCV의 NS3/4A 프로테아제를 억제하는 직접작용 항바이러스제(DAA)로, pibrentasvir(NS5A 억제제)와 복합제로 사용됩니다.

HIV는 레트로바이러스로 역전사를 통해 복제하며, HCV NS3/4A와 같은 프로테아제 표적에 대한 직접적인 항HIV 활성은 확립되어 있지 않습니다. 높은 TxGNN 점수는 바이러스 프로테아제 간 유사성이나 지식 그래프상의 근접성을 반영했을 가능성이 큽니다.

임상 자료는 HIV/HCV 동반감염 환자에서 HCV를 치료하는 것을 뒷받침합니다. 이는 이미 허가된 사용 범위이며, HIV 치료를 위한 재창출이 아닙니다. 따라서 이 예측은 기전상 타당성이 낮다고 판단됩니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02738138](https://clinicaltrials.gov/study/NCT02738138) | Phase 3 | 완료 | 153 | HCV/HIV-1 동반감염 성인에서 glecaprevir/pibrentasvir의 효능·안전성 (EXPEDITION-2). 평가변수는 HCV SVR |
| [NCT03235349](https://clinicaltrials.gov/study/NCT03235349) | Phase 3 | 완료 | 160 | 대상성 간경변이 있는 아시아 성인 HCV 환자(HIV 동반감염 포함 가능). 표적은 HCV |
| [NCT03222583](https://clinicaltrials.gov/study/NCT03222583) | Phase 3 | 완료 | 546 | 간경변 없는 아시아 성인 HCV 환자(HIV 동반감염 포함 가능). 항HIV 효능 근거 없음 |
| [NCT02634008](https://clinicaltrials.gov/study/NCT02634008) | Phase 3 | 완료 | 83 | 최근 감염된 HCV(HIV 동반 여부 무관)에서 paritaprevir 기반 등 다른 요법 파일럿 |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | 완료 | 87 | HIV/HCV 환자에서 HCV 완치 후 심혈관 위험 평가. HIV 치료가 아닌 HCV 완치 결과 평가 |
| [NCT04042740](https://clinicaltrials.gov/study/NCT04042740) | Phase 2 | 완료 | 45 | 급성 HCV(HIV-1 동반 포함)에서 4주 glecaprevir/pibrentasvir 요법 (PURGE-C) |
| [NCT07040319](https://clinicaltrials.gov/study/NCT07040319) | Phase 1/2 | 모집 중 | 30 | 임신 중 HCV 여성(HIV 동반 포함)에서 PK 및 안전성. HIV가 아닌 HCV 대상 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [37671831](https://pubmed.ncbi.nlm.nih.gov/37671831/) | 2023 | Cohort | J Antimicrob Chemother | 실제 진료 환경의 HIV/HCV 동반감염 환자에서 G/P의 SVR 반응 평가 |
| [39697370](https://pubmed.ncbi.nlm.nih.gov/39697370/) | 2024 | 실사용 연구 | Clin Exp Hepatol | bictegravir/emtricitabine/TAF 투여 중인 HIV/HCV 환자에서 G/P의 효과·안전성 |
| [31504702](https://pubmed.ncbi.nlm.nih.gov/31504702/) | 2020 | 약물상호작용 연구 | J Infect Dis | G/P와 HIV 항레트로바이러스제 병용 시 약물상호작용 |
| [31284039](https://pubmed.ncbi.nlm.nih.gov/31284039/) | 2019 | 체계적 문헌고찰·메타분석 | Int J Antimicrob Agents | 13개 연구 3,082명에서 HCV 전체 SVR12 97.8% |
| [41297677](https://pubmed.ncbi.nlm.nih.gov/41297677/) | 2026 | 단일군 시험 | J Hepatol | 급성 HCV 성인에서 8주 G/P의 효능·안전성 |
| [30499343](https://pubmed.ncbi.nlm.nih.gov/30499343/) | 2019 | Review | Future Microbiol | 만성 HCV에서 G/P 개관 |
| [29595065](https://pubmed.ncbi.nlm.nih.gov/29595065/) | 2018 | Review | Expert Opin Pharmacother | HCV 프로테아제 억제제 치료 개관 |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Review | Clin Pharmacokinet | HCV 치료제의 약동학·약력학 고려사항 |

이 문헌들은 모두 HCV 치료 또는 HIV/HCV 동반감염 환자의 HCV 치료를 다루며, HIV 자체에 대한 항바이러스 효과를 보고한 문헌은 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201800200 | 마비렛정 (한국애브비) | 분홍색의 양면이 볼록한 장방형 필름코팅정 | 허가 문서 링크로만 제공되어 적응증 본문 확인 불가 |

## 안전성 고려사항

- **약물 상호작용**: 총 57건이 확인되었으며, 주요 항목은 다음과 같습니다.
  - **Major**: rosuvastatin, simvastatin, edoxaban
  - **Moderate**: dexamethasone, esomeprazole, omeprazole, apixaban, betrixaban, cobicistat, deferasirox, metreleptin, naldemedine, lusutrombopag, revefenacin, griseofulvin, troglitazone
  - **Minor**: fidaxomicin, naloxegol, prucalopride, indacaterol
- **참고**: HCV 직접작용 항바이러스제 투여 시 HBV 동반감염 환자에서 HBV 재활성화 위험이 알려져 있습니다. 이는 안전성 고려사항이며 치료 효과가 아닙니다.

경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
HIV 관련 임상시험은 모두 HIV/HCV 동반감염 환자의 HCV 치료를 평가한 것으로, 이미 허가된 사용 범위입니다. HIV 자체에 대한 항바이러스 활성 근거는 없으며 기전상 연결고리도 불충분하므로, 높은 TxGNN 점수만으로 재창출을 진행하기는 어렵습니다.

**진행하려면 필요한 것:**
- HIV 복제에 대한 glecaprevir의 in vitro 항바이러스 활성 자료
- 상세한 작용 기전(MOA) 데이터 확보
- 허가사항(경고·금기) 원문 확인 및 안전성 검토
- 허가 적응증 본문 확인

**참고 (다른 예측 적응증):** B형 간염, A형 간염, E형 간염, 동물 바이러스성 간염, 심ian/고양이 면역결핍 관련 질환, 옴스크 출혈열, 키야사누르 산림병, 희귀 신경발달장애 등 나머지 예측 적응증도 모두 Hold입니다. A형 간염에 연결된 임상시험은 실제로는 HCV 시험이며, 진드기 매개 플라비바이러스 질환은 NS3 프로테아제 보존성에 근거한 추측일 뿐 실증 근거가 없습니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

