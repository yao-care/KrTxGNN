---
layout: default
title: Mannitol
parent: 모델 예측만 (L5)
nav_order: 494
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Mannitol: 예측 신규 적응증 신인성 항이뇨호르몬 부적절 분비 증후군 (nephrogenic syndrome of inappropriate antidiur… (근거 수준 L5). 기존 적응증: 허가증에 적응증 원문 대신 링크만 제공되어 구체적인 내용을 확인할 수 없음 (허가사항 참조)"
monitor_inn: "Mannitol"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "congestive heart failure", "acute pulmonary heart disease", "exercise-induced malignant hyperthermia", "malignant hyperthermia, susceptibility to", "familial periodic paralysis", "hypokalemic periodic paralysis", "congenital multicore myopathy with external ophthalmoplegia", "moderate multiminicore disease with hand involvement", "pseudotumor cerebri"]
---

# Mannitol
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

# Mannitol: 수액·삼투압 이뇨제에서 저나트륨혈증 관련 질환(신인성 항이뇨 부적절 증후군)으로

## 한 문장 요약

Mannitol은 삼투성 이뇨제로, 한국에서 주사액과 흡입용 캡슐 형태로 허가되어 시판 중입니다.
TxGNN 모델은 **신인성 항이뇨호르몬 부적절 분비 증후군(nephrogenic syndrome of inappropriate antidiuresis)**에 효과가 있을 수 있다고 예측하지만, 현재 **임상시험은 0건**이고 직접 관련된 **문헌은 1편(일반 리뷰)**에 그칩니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에 적응증 원문 대신 링크만 제공되어 구체적인 내용을 확인할 수 없음 (허가사항 참조) |
| 예측 신규 적응증 | 신인성 항이뇨호르몬 부적절 분비 증후군 (nephrogenic syndrome of inappropriate antidiuresis) |
| TxGNN 예측 점수 | 99.97% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 8건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Mannitol은 삼투성 이뇨제로, 삼투압 이뇨를 일으켜 수분 배설에 영향을 줄 수 있습니다. 이 점 때문에 모델이 수분 대사 이상 질환과 연결했을 가능성이 있습니다.

그러나 이 질환은 AVPR2(V2 수용체) 기능획득 돌연변이로 수분이 부적절하게 저류되어 발생합니다. 이 경우 삼투성 이뇨는 오히려 나트륨 손실과 저나트륨혈증을 악화시킬 수 있습니다. 연결된 문헌도 저나트륨혈증 평가의 일반적인 함정을 다룬 리뷰 한 편뿐이며, 약물에 특이적인 근거가 아닙니다. 따라서 이 예측은 현재 임상 데이터로 뒷받침되지 않습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European Journal of Internal Medicine | 저나트륨혈증 환자 평가 시 흔한 함정 10가지를 정리한 일반 리뷰이며, Mannitol에 특이적인 근거는 없음 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 197100027 | 대한디-만니톨주사액(25%) | 주사액 (무색투명한 액) | 허가사항 참조 |
| 199101334 | 이노엔20%만니톨주사액 | 수액용 주사제 | 허가사항 참조 |
| 200805048 | 아리돌흡입용캡슐콤비팩(만니톨) | 흡입용 캡슐 (콤비팩) | 허가사항 참조 |
| 197500054 | 중외20%만니톨주 | 주사액 (무색투명한 액) | 허가사항 참조 |
| 197100029 | 대한디-만니톨주사액(15%) | 주사액 (무색투명한 액) | 허가사항 참조 |

위 표는 전체 8건 중 5건만 나열한 것입니다.

## 안전성 고려사항

- **약물 상호작용**: 데이터에 100건의 상호작용이 확인되었으며, 일부 예시는 다음과 같습니다.
  - **주요(Major)**: Amikacin
  - **중등도(Moderate)**: Lamivudine, Formoterol, Salbutamol, Benazepril, Captopril, Carbamazepine, Citalopram, Dapagliflozin, Canagliflozin, Cisatracurium 등
  - **경미(Minor)**: Doxycycline

경고 및 금기 등 그 밖의 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 점수는 높지만 임상시험이 없고 문헌도 약물 특이적 근거가 없는 일반 리뷰 1편뿐입니다. 또한 이 질환의 병태생리상 삼투성 이뇨가 저나트륨혈증을 악화시킬 수 있어 기전적으로 오히려 우려됩니다.

**진행하려면 필요한 것:**
- 허가사항(경고, 금기, 적응증)의 확인 및 정리
- 상세한 작용 기전(MOA) 데이터 확보
- 신인성 항이뇨호르몬 부적절 분비 증후군에서 Mannitol의 효과와 안전성을 직접 평가한 전임상 또는 임상 근거

---

### 참고: 다른 예측 적응증 요약

모두 임상시험이 없으며 TxGNN 점수는 99.7~99.9%입니다. 순위 1위 예측과 달리 일부는 약물 자체의 효과가 아닌 부형제나 보조 요법 관련 연관성으로 보입니다.

| 순위 | 예측 질환 | 점수 | 근거 수준 | 결정 | 비고 |
|-----|---------|------|---------|------|------|
| 2 | 울혈성 심부전 | 99.90% | L4 | Hold | 급성 용적 확장으로 폐울혈이 악화될 수 있어 심부전에서 일반적으로 주의 대상. Mannitol 직접 시험 없음 |
| 3 | 급성 폐성심 | 99.88% | L4 | Hold | 1977년 ARDS 증례 보고 등 간접 근거뿐이며 용적 확장이 우심 부담에 해로울 수 있음 |
| 4 | 운동유발 악성고열 | 99.86% | L5 | Hold | 문헌 없음 |
| 5 | 악성고열 감수성 | 99.80% | L4 | Hold | Mannitol이 dantrolene 제형의 부형제이기 때문에 나타난 연관성으로 추정 |
| 6 | 가족성 주기성 마비 | 99.75% | L4 | Hold | 칼륨 주입 시 포도당 대신 쓰는 비활성 용매 역할일 뿐 치료 기전이 아님 |
| 7 | 저칼륨성 주기성 마비 | 99.72% | L4 | Hold | 위와 동일하게 용매로서의 보조적 사용 |
| 8 | 외안근마비를 동반한 선천성 다핵심 근병증 | 99.72% | L5 | Hold | RYR1 관련 질환과의 네트워크 근접성에 따른 예측 |
| 9 | 손 침범을 동반한 중등도 다소핵심 질환 | 99.71% | L5 | Hold | 위와 동일 |
| 10 | 가성뇌종양 (특발성 두개내압 항진) | 99.70% | L4 | 연구 과제 (S1) | 두개내압 감소에 대한 기전적 타당성이 가장 높음. 다만 문헌이 주로 1983~1994년의 일반 두개내압 연구이고, 반동성 두개내압 상승 때문에 단기 응급 조절용 사용에 한정됨 |

이 중 **가성뇌종양**은 삼투압 요법의 두개내압 감소 기전과 부합하여 가장 현실적인 후속 연구 후보입니다. 표준 치료(acetazolamide, 체중 감량, 시력 위협 시 수술)를 보완하는 단기 응급 처치로서의 가능성을 검토할 수 있습니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

