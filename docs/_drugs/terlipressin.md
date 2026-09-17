---
layout: default
title: Terlipressin
parent: 모델 예측만 (L5)
nav_order: 671
evidence_level: L5
indication_count: 10
---

# Terlipressin
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

# Terlipressin: 식도정맥류출혈(해외 근거)에서 폐고혈압으로

## 한 문장 요약

Terlipressin은 바소프레신 유사체(V1 수용체 작용제)로, 해외 임상시험 근거상 주로 **식도정맥류출혈**과 **간신증후군** 치료에 사용되어 왔습니다(한국 내 정식 허가 적응증 아님). TxGNN 모델은 여러 후보 중 **폐고혈압(Pulmonary Hypertension)**, 특히 간경변 관련 **문맥성 폐고혈압(portopulmonary hypertension)**에서 가장 실증 가능한 신호를 보이며, 현재 **4건의 임상시험**(모두 폐고혈압이 주 평가지표는 아님)과 **20편의 문헌**(코호트 연구·증례 보고 다수 포함)이 이 방향을 간접적으로 뒷받침합니다.

> ⚠️ 이 약물은 한국에 **미상시(미허가)** 상태이며, 허가사항 경고/금기 정보가 확보되지 않아 안전성 초기평가(S1) 자체가 불가능한 차단(Blocking) 데이터 공백이 존재합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (한국 미허가) — 해외 임상시험 근거상 식도정맥류출혈·간신증후군에 주로 사용 |
| 예측 신규 적응증 | 폐고혈압 (Pulmonary Hypertension, 특히 문맥성 폐고혈압) |
| TxGNN 예측 점수 | 99.56% (rank 7,777 / score 0.9956) |
| 근거 수준 | L3 (관찰 연구 다수, RCT 없음) |
| 한국 시판 현황 | 미상시 (시판되지 않음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 확보되지 않았습니다. 다만 제공된 임상시험 근거 자료에 따르면 Terlipressin은 **바소프레신 유사체**로서 V1 수용체에 작용해 내장혈관을 수축시키는 약물이며, 이를 통해 식도정맥류출혈 시 문맥압을 낮추는 목적으로 사용되어 왔습니다.

간경변 환자는 흔히 전신 과역동(hyperdynamic) 순환 상태를 동반하며, 이것이 **문맥성 폐고혈압(portopulmonary hypertension)**의 병태생리와 연결됩니다. Terlipressin의 내장혈관 수축 작용이 이 과역동 상태를 완화시켜 간접적으로 폐혈류역학을 개선한다는 코호트 연구 결과가 다수 존재합니다(Kalambokis 등, 2008/2012). 다만 이는 **직접적인 폐혈관 확장/수축 기전이 아니라 전신 순환 개선을 통한 간접 효과**이며, 신생아 지속성 폐고혈압(PPHN)에서의 사용례는 구제요법(rescue therapy) 성격의 증례 보고 수준에 머물러 있습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03584087](https://clinicaltrials.gov/study/NCT03584087) | Phase 4 | 완료 | 74 | 내시경 정맥류 결찰술 후 급성 정맥류 출혈에서의 Terlipressin 효능 평가. 폐고혈압은 평가지표 아님 (관련성 C등급) |
| [NCT06027970](https://clinicaltrials.gov/study/NCT06027970) | Phase 3 | 불명 | 165 | 급성 정맥류 출혈에서 지속주입 Terlipressin 요법 평가. 폐고혈압 평가지표 아님 (관련성 C등급) |
| [NCT06256432](https://clinicaltrials.gov/study/NCT06256432) | Phase 2 | 모집 중 | 54 | 간신증후군에서 Ambrisentan(타 약물) 평가 — Terlipressin 자체 시험 아님, 환자군만 중첩 (관련성 C등급) |
| [NCT05315557](https://clinicaltrials.gov/study/NCT05315557) | 미해당 | 불명 | 100 | 패혈성 쇼크를 동반한 중증 간경변 환자에서 Vasopressin vs Terlipressin 2차 승압제 비교. 전신 혈류역학 중심 (관련성 C등급) |

**주의:** 폐고혈압을 1차 평가지표로 삼은 임상시험은 현재 등록되어 있지 않습니다. 위 4건은 모두 간경변/정맥류출혈 맥락에서의 간접 관련 시험입니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [22893473](https://pubmed.ncbi.nlm.nih.gov/22893473/) | 2012 | Cohort | Hepatobiliary Pancreat Dis Int | 정맥류출혈 또는 간신증후군을 동반한 폐고혈압 간경변 환자 7명에서 Terlipressin 2mg 투여 후 폐혈관저항 감소 확인 |
| [21733953](https://pubmed.ncbi.nlm.nih.gov/21733953/) | 2012 | Cohort | Angiology | 심초음파로 평가한 간경변 환자에서 Terlipressin이 폐고혈압군에서 폐혈관저항을 선택적으로 낮춤 |
| [18280605](https://pubmed.ncbi.nlm.nih.gov/18280605/) | 2008 | 미분류 | J Hepatology | 1주간 Terlipressin 투여 후 문맥성 폐고혈압 환자의 폐동맥압이 유의하게 개선된 증례 |
| [15259082](https://pubmed.ncbi.nlm.nih.gov/15259082/) | 2004 | 미분류 | World J Gastroenterol | 심초음파로 간경변 환자의 수축기 폐동맥압에 대한 Terlipressin 효과 평가 |
| [19624374](https://pubmed.ncbi.nlm.nih.gov/19624374/) | 2009 | 미분류 | Paediatric Anaesthesia | 선천성 횡격막탈장(CDH) 환아의 중증 폐고혈압 관리에서 Terlipressin의 역할 |
| [23128058](https://pubmed.ncbi.nlm.nih.gov/23128058/) | 2012 | 미분류 | J Perinatology | 패혈증 저체온요법 신생아에서 Terlipressin의 폐동맥압 영향 (심초음파 평가) |
| [30971593](https://pubmed.ncbi.nlm.nih.gov/30971593/) | 2019 | 미분류 | Ann Cardiac Anaesth | 폐고혈압 심장수술 환자에서 밀리논 유발 전신 저혈압 예방: Terlipressin vs Norepinephrine |
| [34179513](https://pubmed.ncbi.nlm.nih.gov/34179513/) | 2021 | Review | BMJ Paediatr Open | 미숙아 저혈압/지속성 폐고혈압에서 Vasopressin·Terlipressin 효능·안전성 체계적 문헌고찰 프로토콜 |
| [32999121](https://pubmed.ncbi.nlm.nih.gov/32999121/) | 2020 | Case Report | Indian Pediatrics | 미숙아의 지속성 폐고혈압 및 난치성 쇼크에서 Terlipressin 구제요법 |
| [21292065](https://pubmed.ncbi.nlm.nih.gov/21292065/) | 2011 | Case Report | J Pediatr Surg | 선천성 횡격막탈장 신생아의 난치성 폐고혈압에서 Terlipressin 구제요법 |

## 기타 예측 후보에 대한 참고

TxGNN 점수 상위 후보 중 **개방각 녹내장(open-angle glaucoma), 유전성 녹내장, 척추후만증 심질환, 내사시, 갑상선기능항진증, 두통, 삼차자율신경두통** 등은 모두 **L5(모델 예측만 존재, 실제 연구 없음)** 수준이며, 근거 자료상 임상시험·문헌이 전혀 없거나(0건) 있어도 해당 적응증과 무관한 시험뿐입니다. Rationale 텍스트 자체도 "기전 방향 불명확", "지식그래프 잡음(noise)으로 추정" 등으로 명시하고 있어, 본 보고서는 유일하게 실증 가능한 **폐고혈압** 후보를 중심으로 작성했습니다.

## 안전성 고려사항

- 이 약물은 **한국에서 허가되지 않은 상태**이므로 국내 허가사항(경고, 금기, 상호작용) 정보가 존재하지 않습니다.
- **[DG001, Blocking]** TFDA/한국 식약처 수준의 경고·금기 정보 결측으로 인해 안전성 초기평가(S1) 단계 진입이 불가능합니다.
- 약물상호작용(DDI) 조회 결과 "not_found" — 등록된 상호작용 데이터가 없습니다.
- 해외 허가국(예: EU EMA, 미국 FDA)의 공식 라벨 정보를 별도로 확인해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
문맥성 폐고혈압에 대해서는 소규모 코호트 연구와 증례 보고 수준의 기전적 타당성(L3)이 존재하지만, 이 약물은 한국 미허가 상태이며 허가 경고/금기 정보 결측이라는 **차단(Blocking) 데이터 공백**이 있어 안전성 초기평가조차 진행할 수 없습니다. RCT 수준의 직접 근거도 부재합니다.

**진행하려면 필요한 것:**
- 해외(FDA/EMA) 허가사항의 경고·금기·부작용 정보 확보
- DrugBank API를 통한 정확한 작용기전(MOA) 데이터 확인
- 한국 내 도입/허가 가능성에 대한 규제 검토
- 문맥성 폐고혈압을 1차 평가지표로 하는 전향적 임상시험(Phase 2 이상) 설계 필요성 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

