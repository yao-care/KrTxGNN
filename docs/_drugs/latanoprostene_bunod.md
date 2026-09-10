---
layout: default
title: Latanoprostene Bunod
parent: 僅模型預測 (L5)
nav_order: 429
evidence_level: L5
indication_count: 10
---

# Latanoprostene Bunod
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Latanoprostene Bunod: 안압 하강(녹내장)에서 내장 석회화방어증(Visceral Calciphylaxis)으로

## 한 문장 요약

Latanoprostene Bunod는 국내 허가 자료가 없어 공식 기존 적응증은 확인되지 않으나, 관련 임상시험 제목(원발개방각녹내장, 고안압증)으로 미루어 NO 공여 프로스타글란딘 계열의 안압 하강제로 개발된 약물로 추정됩니다. TxGNN 모델은 **내장 석회화방어증(Visceral Calciphylaxis)**에 효과가 있을 수 있다고 예측했지만(예측 점수 99.76%), 이를 뒷받침하는 임상시험이나 문헌은 **현재 전혀 없으며**, 기전상 연관성도 확인되지 않습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 국내 허가 자료 없음 (미시판). 공개 임상시험 자료 기준 안압 하강(원발개방각녹내장·고안압증) 목적으로 개발된 약물로 추정 |
| 예측 신규 적응증 | 내장 석회화방어증 (Visceral Calciphylaxis) |
| TxGNN 예측 점수 | 99.76% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 확보되지 않았습니다(Blocking-level 데이터 갭). 다만 연계된 임상시험·문헌 정보를 통해 추정하면, Latanoprostene Bunod는 NO 공여 프로스타글란딘 F2α 유사체로, 대사되어 latanoprost acid(FP 수용체 작용제, 포도막공막 유출 촉진)와 부티레이트 모노나이트레이트(NO 방출, 소주망/쉴렘관 평활근 이완을 통한 방수 유출 증가)로 작용하는 것으로 알려져 있습니다. 이는 안압 하강 목적에 부합하는 기전입니다.

그러나 이번 예측 신규 적응증인 **내장 석회화방어증**은 소혈관의 병적 석회화와 혈전 형성을 특징으로 하는 질환으로, 안압·방수 유출이나 혈관 평활근 이완 기전과 생물학적으로 연결되는 알려진 경로가 없습니다. TxGNN 근거 자료 자체에도 "지식 그래프 상의 통계적 연관성일 뿐, 임상적·문헌적 근거가 없다"고 명시되어 있어, 현재로서는 기전상 타당성을 인정하기 어렵습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

현재 한국에 허가된 제품이 없습니다 (미시판, 허가증 0건).

## 안전성 고려사항

라벨상 주요 경고·금기 정보 및 약물상호작용 자료가 아직 확보되지 않았습니다(TFDA 허가사항 원문 미확보, Blocking 등급 데이터 갭). 안전성 평가를 위해서는 우선 허가사항 원문 확보가 필요하며, 그 전까지는 별도 안전성 판단을 내릴 수 없습니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 점수는 높지만(99.76%), 이를 뒷받침하는 임상시험·문헌 근거가 전무하고(L5), 기전상 연관성도 확인되지 않습니다. 또한 국내 미시판 상태이며 기본 안전성 자료(경고·금기)조차 확보되지 않아, 현 단계에서 진행 근거가 부족합니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 공식 데이터 확보 (DrugBank API 조회)
- TFDA/허가 당국 라벨 원문 확보 및 경고·금기 사항 파싱 (Blocking 데이터 갭 해소)
- 내장 석회화방어증과의 생물학적 연관성을 뒷받침할 전임상 또는 기전 연구 존재 여부 재확인
- 관련성이 확인되지 않을 경우, 아래 참고 목록의 대체 적응증(예: vascular disease) 검토로 전환

---

## 참고: 전체 예측 적응증 순위 요약 (10건)

동일 약물에 대해 TxGNN이 제시한 상위 10개 후보 중, 1위(Visceral Calciphylaxis) 외에 상대적으로 근거가 있는 항목은 다음과 같습니다.

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 | 권장 결정 | 비고 |
|------|-----------|-----------|----------|----------|------|
| 1 | Visceral calciphylaxis | 99.76% | L5 | Hold | 임상시험·문헌 없음, 기전 연결 없음 |
| 2 | Primary hereditary glaucoma | 99.71% | L3 | Proceed with Guardrails | 약리 기전(안압 하강)상 유사 계열 외삽, 유전성 아형 직접 근거는 없음 |
| 3 | Arterial thoracic outlet syndrome | 99.63% | L5 | Hold | 해부학적 압박 질환, 기전 무관 |
| 4 | Venous thoracic outlet syndrome | 99.63% | L5 | Hold | 상동 |
| 5 | Neurogenic thoracic outlet syndrome | 99.56% | L5 | Hold | 상동 |
| 6 | Vascular disease | 99.53% | L3 | Research Question | NCT03949244(Phase 4, 완료, 갑상혈관 미세혈류 측정) 등 인체 시험 존재, 다만 치료 효능시험은 아님 |
| 7 | Idiopathic spontaneous coronary artery dissection | 99.52% | L5 | Hold | 이론상 오히려 위험 증가 가능성, 안전성 우려 |
| 8 | Angiodysplasia of stomach | 99.51% | L5 | Hold | 혈관 이완이 지혈에 불리할 수 있음 |
| 9 | Lymphangiectasis | 99.48% | L5 | Hold | 기전 연결 없음 |
| 10 | Hemangioendothelioma | 99.47% | L4 | Hold | 문헌은 치료 근거가 아닌 안전성 경고(망막박리 사례보고) |

전체적으로 이 약물에 대한 TxGNN 예측군은 근거 수준이 낮으며(대부분 L5), 유일하게 실제 인체 시험 데이터가 존재하는 **6위 Vascular disease**(L3, Research Question)가 추가 탐색 가치가 있는 후보로 판단됩니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

