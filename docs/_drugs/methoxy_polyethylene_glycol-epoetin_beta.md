---
layout: default
title: Methoxy Polyethylene Glycol-Epoetin Beta
parent: 모델 예측만 (L5)
nav_order: 473
evidence_level: L5
indication_count: 7
---

# Methoxy Polyethylene Glycol-Epoetin Beta
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

# METHOXY POLYETHYLENE GLYCOL-EPOETIN BETA: 적응증 미상에서 원발성 혈소판 방출 장애로

## 한 문장 요약

METHOXY POLYETHYLENE GLYCOL-EPOETIN BETA(DrugBank ID: DB09107)는 기존 적응증 및 작용기전 자료가 확보되지 않은 상태입니다.
TxGNN 모델은 **원발성 혈소판 방출 장애(Primary Release Disorder of Platelets)**에 효과가 있을 수 있다고 예측하지만,
현재 이를 뒷받침하는 임상시험이나 문헌은 **한 건도 없으며**, 예측은 모델 점수에만 근거합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (평가팩 미기재) |
| 예측 신규 적응증 | 원발성 혈소판 방출 장애 (Primary Release Disorder of Platelets) |
| TxGNN 예측 점수 | 99.36% (rank 10225) |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 기존 적응증 정보도 평가팩에 확보되어 있지 않아,
기전상 원발성 혈소판 방출 장애에 왜 적용 가능할 수 있는지 판단할 근거가 부족합니다.

DrugBank 조회는 성공했으나(query_log id 2) 기전(MOA) 및 적응증 상세 필드는 채워지지 않았으며,
이는 평가팩의 Blocking/High 등급 데이터 갭(DG001 TFDA 경고·금기, DG002 작용기전)과 직접 연결됩니다.
기전적 타당성을 평가하려면 DrugBank API 재조회 또는 원 문헌 확인이 선행되어야 합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

(ClinicalTrials.gov 및 ICTRP 모두 0건 조회, query_log id 3–4 확인)

## 문헌 근거

현재 관련 문헌이 없습니다.

(PubMed 조회 0건, query_log id 5 확인)

## 한국 시판 정보

현재 한국에 시판 중인 제품이 없습니다 (허가증 0건, 미시판).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

(주요 경고·금기·DDI 모두 데이터 갭 상태이며, DDI 조회 결과 자체가 not_found)

## 결론 및 다음 단계

**결정: Hold**

**사유:**
작용기전, 기존 적응증, 임상시험, 문헌 근거가 모두 확보되지 않았고 TxGNN 예측 점수만 존재하는 L5 수준입니다.
한국 내 시판 이력도 없어 규제·안전성 검토를 시작할 최소 기반조차 부족합니다.

**진행하려면 필요한 것:**
- DrugBank API 재조회를 통한 작용기전(MOA) 및 기존 적응증 확보
- TFDA/식약처 등 규제기관 허가사항(경고·금기) 확보 — 현재 Blocking 데이터 갭(DG001)
- 원발성 혈소판 방출 장애 관련 전임상·기전 문헌 탐색 (현재 임상시험·문헌 모두 0건)
- 한국 시판·허가 현황 재확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

