---
layout: default
title: Lithium Carbonate
parent: 모델 예측만 (L5)
nav_order: 446
evidence_level: L5
indication_count: 10
---

# Lithium Carbonate
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

# Lithium Carbonate: 적응증 정보 없음에서 Pseudoachondroplasia로

## 한 문장 요약

Lithium Carbonate는 DrugBank 조회 결과 기존 적응증 및 작용기전(MOA) 정보가 확보되지 않았고, 한국 내 허가 이력도 없습니다.
TxGNN 모델은 초희귀 유전성 골격 발달 질환인 **Pseudoachondroplasia**에 효과가 있을 수 있다고 예측했으나(예측 점수 **99.98%**),
현재 이를 뒷받침하는 **임상시험이나 문헌은 전혀 없습니다**.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (DrugBank/허가 정보 미확보) |
| 예측 신규 적응증 | Pseudoachondroplasia |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L5 (모델 예측만 존재, 실제 연구 없음) |
| 한국 시판 현황 | 미상판 (허가증 0건) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 없습니다. Evidence Pack의 데이터 공백 목록(DG002, High)에도 이 항목이 명시되어 있어,
기전 근거를 DrugBank API로 추가 확인해야 하는 상태입니다.

Evidence Pack에 기재된 예측 근거(rationale)에 따르면, Pseudoachondroplasia는 COMP 유전자 돌연변이로 인한 연골 내 소포체 단백질 축적성 골격 발달 이상입니다.
리튬이 GSK-3β 억제제로서 canonical Wnt 신호를 활성화해 연골세포 분화에 영향을 줄 수 있다는 가설이 제시되었지만, 이는 통로 간 교차 추론(cross-pathway speculation)에 불과하며
COMP 관련 직접 문헌은 존재하지 않고, 리튬의 소포체 단백질 품질관리(ERAD 경로) 작용 기전도 알려진 바 없습니다.

즉 이 예측은 지식그래프(KG) 임베딩상의 통계적 연관성에 근거한 것으로, **기전상 타당성을 뒷받침할 실제 근거는 현재 부족**합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

현재 한국 내 허가 이력이 없습니다 (허가증 0건, 미상판).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

(참고: Evidence Pack 데이터 공백 DG001은 "허가사항 경고/금기" 정보 부재를 Blocking 등급으로 지정하고 있어, 안전성 초기 평가(S1) 자체가 현재 불가능한 상태입니다.)

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 신규 적응증(Pseudoachondroplasia)을 뒷받침하는 임상시험과 문헌이 전무하며(L5, S0), 제시된 기전 연결 역시 저자 스스로 "간접적 추론"·"KG 임베딩 편향 가능성"으로 평가하고 있습니다.
Pseudoachondroplasia 외 나머지 9개 예측 적응증(순위 2~10) 역시 모두 동일하게 L5/S0/Hold 등급이며, 대부분 초희귀 유전질환으로 실제 근거가 없습니다.
또한 허가사항 경고·금기 정보(DG001, Blocking)가 없어 안전성 초기 평가 자체가 불가능합니다.

**진행하려면 필요한 것:**
- TFDA(한국 허가) 수준의 경고/금기 정보 확보 — 현재 Blocking 데이터 공백(DG001)
- DrugBank API를 통한 작용기전(MOA) 확보 — High 데이터 공백(DG002)
- Pseudoachondroplasia 관련 전임상(동물/세포주) 또는 사례보고 수준 근거 확보
- COMP/ERAD 경로에 대한 리튬의 직접적 작용 여부 문헌 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

