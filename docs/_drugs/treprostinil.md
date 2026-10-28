---
layout: default
title: Treprostinil
parent: 모델 예측만 (L5)
nav_order: 759
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Treprostinil: 예측 신규 적응증 폐동정맥 기형 (Pulmonary Arteriovenous Malformation) (근거 수준 L5). 기존 적응증: 폐동맥 고혈압(PAH). 허가증에는 원문 링크만 연결되어 있어 구체적 문구는 허가사항 원문에서 확인해야 합니다"
monitor_inn: "TREPROSTINIL"
predicted_indications: ["pulmonary arteriovenous malformation (disease)", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "malformation syndrome with odontal and/or periodontal component", "Ambras type hypertrichosis universalis congenita"]
---

# Treprostinil
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **5** 건
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

## Treprostinil: 폐동맥 고혈압에서 폐동정맥 기형으로
{: .text-alpha }

## 한 문장 요약

Treprostinil은 프로스타사이클린 유사체로, 원래 폐동맥 고혈압(PAH) 치료에 사용되는 약입니다. TxGNN 모델은 **폐동정맥 기형(Pulmonary Arteriovenous Malformation)**에 효과가 있을 수 있다고 예측했지만, 이 질환을 지지하는 **임상시험은 0건, 문헌도 0편**입니다. 모델 예측만 있는 상태이며, 오히려 혈관확장 작용이 병태를 악화시킬 가능성도 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 폐동맥 고혈압(PAH). 허가증에는 원문 링크만 연결되어 있어 구체적 문구는 허가사항 원문에서 확인해야 합니다. |
| 예측 신규 적응증 | 폐동정맥 기형 (Pulmonary Arteriovenous Malformation) |
| TxGNN 예측 점수 | 0.9970 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 2건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 확보되지 않았습니다. 알려진 정보에 따르면 Treprostinil은 프로스타사이클린 유사체입니다. 폐혈관과 전신혈관을 확장하고 혈소판 응집을 억제합니다. 이 기전은 폐혈관 병변이 핵심인 PAH에 직접 작용합니다.

폐동정맥 기형은 동맥과 정맥이 비정상적으로 직접 연결된 구조적 혈관 단락입니다. 흔히 유전성 출혈성 모세혈관확장증(HHT)과 관련되며, 주로 색전술로 치료합니다. 이번 예측은 폐혈관 질환과의 네트워크상 근접성에서 비롯된 계산상의 결과로 보입니다. 혈관확장 작용이 오히려 단락이나 저산소혈증을 악화시킬 수 있다는 우려도 있습니다. 따라서 기전상 타당성은 낮고, 이 예측은 신중하게 해석해야 합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201001269 | 레모둘린주사 1mg/mL, 2.5mg/mL, 5mg/mL, 10mg/mL | 주사제 (유리 바이알) | 허가증 원문 참조 |
| 202401656 | 타이바소흡입액 0.6mg/mL | 흡입 액제 (플라스틱 용기) | 허가증 원문 참조 |

## 안전성 고려사항

- **지식그래프 기반 금기 질환** (허가사항이 아니라 지식그래프의 약물-질환 금기 연결 정보): 신장 질환, 요관 농축증, 간 질환, 담낭 질환, 저혈압성 질환, 혈액 응고 질환, 폐 질환, 희귀 폐질환. 폐동정맥 기형 환자에게 적용할 때는 특히 저혈압과 폐 질환 관련 위험을 검토해야 합니다.
- **약물 상호작용**: 총 100건이 확인되었습니다. 이 중 주요 중등도(Moderate) 상호작용은 다음과 같습니다.
  - 에피네프린, 에페드린 (비강 제형 포함)
  - 아세틸살리실산(아스피린)
  - SGLT2 억제제: canagliflozin, dapagliflozin, empagliflozin, ertugliflozin
  - 만니톨, 글리세린, 파파베린
  - 식욕억제제: fenfluramine, dexfenfluramine, sibutramine
- 위험도가 확정되지 않은 상호작용(Unknown)으로는 pantoprazole, omeprazole, lansoprazole, prednisone, simvastatin, 염화칼륨이 있습니다.

허가사항의 경고 및 금기 항목은 별도로 허가사항 원문을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
폐동정맥 기형에 대한 임상시험과 문헌이 전혀 없고, 근거가 모델 예측뿐(L5)입니다. 혈관확장 작용이 구조적 단락을 악화시킬 수 있다는 기전상 우려도 있어 현 시점에서 진행하기 어렵습니다.

**진행하려면 필요한 것:**
- 폐동정맥 기형(HHT 관련 포함)에서 프로스타사이클린 계열 약물의 효과와 안전성을 평가한 전임상 또는 임상 자료
- 단락 악화와 저산소혈증 위험을 평가하는 안전성 검토
- 허가사항(경고, 금기) 원문 확인
- 상세한 작용 기전(MOA) 데이터 보완

**참고:** 같은 약물에 대해 TxGNN이 예측한 다른 후보 중 **선천성 심장질환 연관 폐동맥 고혈압**과 **결합조직질환 연관 폐동맥 고혈압**은 관찰 연구와 체계적 문헌고찰이 있어 근거 수준 L3, 권고 결정 "Proceed with Guardrails"로 평가되었습니다. 다만 이 두 질환은 기존 PAH 적응증의 하위군에 가까워, 엄밀한 의미의 새로운 질환은 아닙니다. 우선순위를 둔다면 폐동정맥 기형보다 이들 후보를 먼저 검토하는 것이 합리적입니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

