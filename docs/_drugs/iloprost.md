---
layout: default
title: Iloprost
parent: 높은 근거 (L1-L2)
nav_order: 387
evidence_level: L1
indication_count: 9
---

# Iloprost
{: .fs-9 }

근거 수준: **L1** | 예측 적응증: **9** 건
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

# Iloprost: 기존 적응증 정보 없음에서 HIV 감염 관련 폐동맥고혈압으로

## 한 문장 요약

Iloprost(DrugBank ID: DB01088)는 한국 내 허가 이력과 공식 작용기전(MOA) 기록이 없는 자료 공백이 큰 약물입니다.
TxGNN 모델은 이 약물에 대해 9개의 신규 적응증을 예측했으며, 이 중 가장 근거가 탄탄한 것은
**HIV 감염 관련 폐동맥고혈압(Pulmonary Arterial Hypertension associated with HIV infection)**으로,
**완료된 Phase 3 무작위대조시험(RCT) 1건**과 **4편의 문헌**이 이를 지지합니다.
다만 TxGNN 점수 자체가 가장 높았던 두 예측(두피 단순형 저모증, 선천성 저모증)은 평가 결과 기전상 근거가 없는
지식그래프 임베딩의 위양성(false positive)으로 판단되어 제외했습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 자료 없음 (등록된 원 적응증 및 MOA 기록 없음) |
| 예측 신규 적응증 | HIV 감염 관련 폐동맥고혈압 (Pulmonary Arterial Hypertension associated with HIV infection) |
| TxGNN 예측 점수 | 99.21% |
| 근거 수준 | L1 |
| 한국 시판 현황 | 미상장 (시판되지 않음) |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Iloprost의 공식 작용기전(MOA) 데이터는 현재 등록되어 있지 않습니다. 다만 근거 자료의 기전 분석에 따르면,
Iloprost는 합성 프로스타사이클린(PGI2) 유사체로 IP 수용체를 매개로 폐혈관 확장, 혈소판 응집 억제,
혈관평활근 증식 억제 작용을 나타내는 것으로 분석됩니다.

HIV 관련 폐동맥고혈압(HIV-PAH)은 WHO Group 1 PAH의 아형으로, 원발성 PAH와 동일한 폐혈관 수축·재형성 병리기전을
공유합니다. Iloprost는 이미 PAH 치료제로서의 계열 효과(class effect)가 확립되어 있어, 기전상 HIV-PAH에도
직접 적용 가능하다는 분석입니다.

반면 TxGNN 점수 1·2위였던 "두피 단순형 저모증"과 "선천성 저모증"은 모근 성장을 촉진하는 PGF2α 계열
(latanoprost, bimatoprost 등, FP 수용체 작용)과 Iloprost의 PGI2/IP 수용체 기전이 근본적으로 다르며,
임상시험·문헌 근거가 전무합니다. 지식그래프 내 프로스타글란딘 계열 클러스터링에 의한 위양성으로 판단되어
이번 보고서의 핵심 예측에서 제외했습니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00709956](https://clinicaltrials.gov/study/NCT00709956) | Phase 3 | 완료 | 64 | 증상성 특발성/가족성 PAH 및 HIV·약물독소 관련 PAH 환자 대상 이중맹검, 무작위, 위약대조, 교차설계 시험. Iloprost Power 15 단회 투여의 운동능력 개선 효과 평가 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [17195895](https://pubmed.ncbi.nlm.nih.gov/17195895/) | 2006 | Review | Mount Sinai J Med | HIV 관련 폐동맥고혈압(HIV-PAH)의 발생률(HIV 감염자의 약 0.5%), 병태생리, 임상양상 개관 |
| [14720012](https://pubmed.ncbi.nlm.nih.gov/14720012/) | 2003 | Review | Am J Respir Med | 프로스타노이드 계열의 PAH 치료 전반 개관. HIV 감염 관련 PAH를 원발성 PAH와 병리기전이 유사한 그룹으로 분류 |
| [31090367](https://pubmed.ncbi.nlm.nih.gov/31090367/) | 2019 | Cohort/Registry | Terapevticheskii Arkhiv | 러시아 국가 PAH 레지스트리 6년 관찰 분석. 유병률, 임상경과, 치료현황, 사망률 평가 |
| [18260882](https://pubmed.ncbi.nlm.nih.gov/18260882/) | 2007 | Review | Kardiologiia | 원발성 PAH 및 결합조직질환·선천성심질환·HIV 감염 등 동반 PAH에서의 프로스타사이클린 및 유사체 대조시험 결과 개관 |

---

## 한국 시판 정보

현재 한국 내 등재된 허가증이 없습니다. 시판 현황: 미상장(Not marketed).

---

## 다른 예측 적응증 요약 (참고)

TxGNN은 총 9개 적응증을 예측했으나, 근거 수준 편차가 커 아래와 같이 정리합니다.

| 순위 | 예측 적응증 | 근거 수준 | 권장 결정 | 비고 |
|------|-----------|---------|---------|------|
| 3 | 선천성심질환 관련 PAH | L2 | Proceed with Guardrails | 임상시험 1건(상태 불명) + 문헌 20편, WHO Group 1 PAH 아형 |
| 6 | 결합조직질환 관련 PAH | L3 | Proceed with Guardrails | RCT 없음, 다수 코호트/증례 문헌(경화증 등) |
| 4 | 폐동정맥기형 | L4 | Hold | 구조적 병변으로 기전 연관성 약함, 문헌 1편(간접) |
| 7 | 주혈흡충증 관련 PAH | L4 | Research Question | 질환 특이적 문헌 없음, 소아 PH 일반 연구만 존재 |
| 8 | 만성 용혈성빈혈 관련 PAH | L5 | Hold | 임상/문헌 근거 전무, 이론적 기전 유사성만 존재 |
| 1, 2, 9 | 두피 저모증, 선천성 저모증, 미만성 원형탈모증 | L5 | Hold | 기전 불일치, 근거 전무 — 지식그래프 위양성 가능성 높음, 후속 조치 불필요 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (TFDA 수준 경고·금기·약물상호작용 자료는 현재 확보되지 않았으며, 이는 S1 안전성 초평가 진입을 막는 차단(Blocking) 등급 자료 공백입니다.)

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
HIV 관련 PAH에 대해서는 완료된 Phase 3 RCT와 다수의 문헌이 계열 효과(class effect) 및 병리기전상의
타당성을 뒷받침합니다. 다만 이 약물은 한국 내 미상장 상태이며 공식 안전성 자료(경고·금기)가 전무해
실제 진행 전 반드시 규제·안전성 자료 확보가 선행되어야 합니다.

**진행하려면 필요한 것:**
- TFDA(또는 해당 규제기관) 공식 라벨 확보 및 경고/금기사항 해석 (DG001, Blocking 등급 — S1 안전성 초평가 필수 선행조건)
- DrugBank API 등을 통한 공식 작용기전(MOA) 데이터 보강 (DG002)
- HIV-PAH 적응증에 특이적인 후속 임상 데이터(대규모/장기 추적) 확인
- 두피 저모증·선천성 저모증·원형탈모증 등 L5 예측 3건은 추가 조사 우선순위에서 제외 권장
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

