---
layout: default
title: Fentanyl
parent: 모델 예측만 (L5)
nav_order: 343
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Fentanyl: 예측 신규 적응증 신원성 항이뇨 부적절 증후군 (Nephrogenic Syndrome of Inappropriate Antidiuresis) (근거 수준 L5). 기존 적응증: 허가 적응증 본문은 확인되지 않았습니다(허가증에는 문서 링크만 수록)"
monitor_inn: "FENTANYL"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "Tourette syndrome"]
---

# Fentanyl
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **2** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 약사 평가 보고서

</div>

## Fentanyl: 통증 치료에서 신원성 항이뇨 부적절 증후군으로
{: .text-alpha }

## 한 문장 요약

Fentanyl은 강력한 아편유사제 진통제로, 한국에서 패취, 주사, 설하정, 구강정 등 다양한 제형으로 허가되어 시판되고 있습니다. TxGNN 모델은 **신원성 항이뇨 부적절 증후군(Nephrogenic Syndrome of Inappropriate Antidiuresis)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 지지하는 **임상시험은 0건, 문헌도 0편**이며 모델 예측 점수만 있는 상태입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문은 확인되지 않았습니다(허가증에는 문서 링크만 수록) |
| 예측 신규 적응증 | 신원성 항이뇨 부적절 증후군 (Nephrogenic Syndrome of Inappropriate Antidiuresis) |
| TxGNN 예측 점수 | 0.9946 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 fentanyl은 mu-아편유사제 수용체 작용제로 알려져 있으며, 아편유사제는 바소프레신 분비와 신장의 수분 처리에 영향을 줄 수 있습니다.

그러나 신성 항이뇨 부적절 증후군은 신장의 바소프레신 V2 수용체(AVPR2) 기능획득 돌연변이로 발생하며, 순환 바소프레신과 무관하게 작용합니다. 따라서 fentanyl과의 약리학적 연결고리가 뚜렷하지 않습니다. 오히려 아편유사제는 SIADH 유사 효과와 관련되어 있어 상태를 악화시킬 가능성도 있습니다. 이 점수는 TxGNN 모델(딥러닝)에서 나온 것이며, 관련 질환 사이에서 모델이 학습한 유사성을 반영할 수 있을 뿐 생물학적 근거는 아닙니다.

참고로 두 번째 예측 질환인 **뚜렛 증후군**(TxGNN 점수 0.9905)도 임상시험과 문헌 근거가 없습니다. 내인성 아편유사제 체계가 도파민 분비를 조절한다는 점은 알려져 있으나, 순수 mu-작용제인 fentanyl을 쓸 치료적 근거는 확립되어 있지 않습니다. 의존성과 남용 가능성 때문에 소아·청소년에게 흔한 만성 신경발달 질환에는 부적합한 후보입니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202100399 | 펜타덤패취50μg/h(수출용) | 패취 | 허가사항 참조 |
| 201403356 | 명문펜타닐패취50㎍/h(수출용) | 패취 | 허가사항 참조 |
| 201601706 | 펜타칸설하정 267마이크로그램 | 설하정(필름코팅정) | 허가사항 참조 |
| 201506803 | 펜타덤패취100㎍/h | 패취 | 허가사항 참조 |
| 199704613 | 하나구연산펜타닐주사 | 주사제 | 허가사항 참조 |

## 안전성 고려사항

- **약물 상호작용**: 데이터 조회 결과 총 100건이 확인되었으며, 주요 항목은 다음과 같습니다.
  - **Major**: Alvimopan, Aprepitant, Bupropion, Clarithromycin, Clotrimazole, Dexamethasone, Dexfenfluramine, Dolasetron, Fenfluramine, Granisetron, Lorcaserin
  - **Moderate**: Atropine, Cimetidine, Clidinium, Dicyclomine, Dronabinol, Eluxadoline, Glycerol phenylbutyrate, Glycopyrronium, Hyoscyamine
- **지식 그래프 기반 금기 질환(참고용, 허가사항 문구 아님)**: 고혈압, 기립성 저혈압, 저혈압, QT 연장 증후군, torsades de pointes, 간부전, 간질환, 신장질환, 췌장염, 담낭질환, 염증성 장질환, 천식, 만성폐쇄성폐질환(COPD), 불안장애, 양성 전립선 비대증, 물질 남용/의존 등

구체적인 경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 점수는 높지만 임상시험과 문헌 근거가 전혀 없고(L5), 신원성 항이뇨 부적절 증후군의 병태생리(AVPR2 기능획득 돌연변이)와 fentanyl의 약리 사이에 타당한 기전적 연결이 없습니다. 아편유사제 특성상 오히려 증상을 악화시킬 수 있고, 의존성·남용 위험도 큽니다.

**진행하려면 필요한 것:**
- 허가사항(MFDS 첨부문서) 확인: 허가 적응증, 경고, 금기
- 작용 기전(MOA) 데이터 보완
- AVPR2 경로 및 아편유사제-바소프레신 상호작용에 대한 전임상·기전 근거
- 임상시험 및 문헌 근거 확보 (현재 없음)
- 뚜렛 증후군 등 다른 예측 질환도 동일하게 근거 보강 필요
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

