---
layout: default
title: Calcitriol
parent: 모델 예측만 (L5)
nav_order: 171
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Calcitriol: 예측 신규 적응증 비타민 D 결핍 (obsolete vitamin D deficiency, 폐기된 질환 용어) (근거 수준 L5)."
monitor_inn: "CALCITRIOL"
predicted_indications: ["obsolete vitamin D deficiency", "renal tubular acidosis", "acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "Dahlberg-Borer-Newcomer syndrome", "hereditary hypophosphatemic rickets"]
---

# Calcitriol
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **7** 건
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

# Calcitriol: 활성형 비타민 D에서 비타민 D 결핍(폐기된 질환 용어)으로

## 한 문장 요약

Calcitriol은 활성형 비타민 D로, 한국에서 연질캡슐, 장용정, 주사제 등 여러 제형으로 허가되어 시판 중입니다.
TxGNN 모델은 **비타민 D 결핍(obsolete vitamin D deficiency)**에 효과가 있을 수 있다고 예측하지만, 이 방향을 지지하는 **임상시험은 0건, 문헌도 0편**이어서 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 예측 신규 적응증 | 비타민 D 결핍 (obsolete vitamin D deficiency, 폐기된 질환 용어) |
| TxGNN 예측 점수 | 99.96% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 (모두 단일제, 유효) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 calcitriol은 비타민 D의 활성 형태이므로, 비타민 D 결핍이라는 질환과 기전상 연결될 가능성은 있습니다.

다만 이 예측에는 한계가 큽니다.
- 예측된 질환명이 **폐기된(obsolete) 용어**로 분류되어 있습니다.
- 영양성 비타민 D 결핍의 표준 치료는 calcitriol이 아니라 cholecalciferol이나 ergocalciferol입니다.
- 높은 점수는 지식 그래프 구조에서 나온 예측일 뿐, 실제 임상 근거가 뒷받침하지 않습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

허가증은 총 20건이며 대부분 수출용 연질캡슐입니다. 내수용 중심의 주요 허가는 아래와 같습니다. 허가 적응증은 허가사항 문서 링크로만 확인되어 본문 요약이 불가능하므로, 각 허가번호의 허가사항을 직접 참조해야 합니다.

| 허가번호 | 제품명 | 제형 | 제조사 |
|---------|------|------|------|
| 199602290 | 칼시오연질캡슐0.25마이크로그램 | 연질캡슐 | 한미약품(주) |
| 199500386 | 칼시본연질캡슐 | 연질캡슐 | (주)한국피엠지제약 |
| 200000363 | 맥스마빌장용정 | 장용필름코팅정 | (주)유유제약 |
| 199400239 | 본키주1마이크로그람 | 주사제(앰플) | (주)유유제약 |
| 201105752 | 네오본주1마이크로그램 | 주사제(앰플) | 알보젠코리아(주) |

## 안전성 고려사항

허가사항의 경고 및 금기 정보는 이번 데이터에 포함되지 않았으므로 허가사항을 참조하세요.

- **지식 그래프 기반 금기 질환(허가 문구가 아닌 모델 데이터)**: 신장 질환, 신장석회증, 신장결석, SLC26A1 변이에 의한 신장결석 감수성, 급성 요산 신병증, 고칼슘혈증, 고인산혈증, 인 대사 질환, 사르코이드증, 비타민 과다증, 요관 축농증, 폐쇄성 동맥경화증
- **약물 상호작용**: 총 100건이 확인되었으며, 일부만 아래에 정리했습니다.
  - **Major**: Cholecalciferol, Calcifediol, Burosumab
  - **Moderate**: Fosphenytoin, Carbamazepine, 바르비탈계(Amobarbital, Butalbital, Butabarbital), 티아지드계 이뇨제(Hydrochlorothiazide, Chlorothiazide, Chlorthalidone 등), 담즙산 결합제(Cholestyramine, Colesevelam, Colestipol), Digoxin, Digitoxin, Aluminum hydroxide, Calcipotriol(외용)

## 결론 및 다음 단계

**결정: Hold**

**사유:**
임상시험과 문헌이 전혀 없는 L5 수준의 모델 예측이며, 질환 용어가 폐기된 용어인 데다 표준 치료도 다른 비타민 D 제제입니다. 현 시점에서 재창출을 진행할 근거가 부족합니다.

**진행하려면 필요한 것:**
- 허가사항(경고, 금기)의 확보: 식약처 허가사항 PDF 다운로드 및 분석이 선행되어야 하며, 이것이 없으면 안전성 선별을 진행할 수 없습니다.
- 상세한 작용 기전(MOA) 데이터: DrugBank 조회로 보완
- 현행 질환 분류 기준에 맞는 적응증 재정의와 calcitriol의 임상적 필요성(cholecalciferol 등 대비) 검토

**참고:** 이번 데이터에 포함된 다른 예측 중 **유전성 저인산혈증 구루병**(TxGNN 점수 99.28%)은 근거가 가장 충실합니다. calcitriol 단독요법의 Early Phase 1 시험(NCT03748966, 16명, 완료)과 고용량·저용량 활성 비타민 D 병용 Phase 4 시험(NCT03820518, 100명, 상태 불명)이 있고, 근거 수준은 L2, 권장 결정은 Proceed with Guardrails입니다. 우선 검토할 후보로는 비타민 D 결핍보다 이 적응증이 더 적합합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

