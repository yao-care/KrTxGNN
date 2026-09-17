---
layout: default
title: Trihexyphenidyl
parent: 중등도 근거 (L3-L4)
nav_order: 705
evidence_level: L4
indication_count: 10
---

# Trihexyphenidyl
{: .fs-9 }

근거 수준: **L4** | 예측 적응증: **10** 건
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

# Trihexyphenidyl: 적응증 정보 부족 상태에서 주의력결핍 과다행동장애(ADHD)로

## 한 문장 요약

Trihexyphenidyl은 기존 적응증 및 작용기전(MOA) 정보가 현재 근거팩에 확보되어 있지 않습니다.
TxGNN 모델은 **주의력결핍 과다행동장애(ADHD)**에 효과가 있을 수 있다고 예측(점수 99.92%)했으나,
현재 이를 뒷받침하는 임상시험은 없고 **문헌 1건**만 존재하며, 그마저도 ADHD를 직접 다루지 않습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | 주의력결핍 과다행동장애 (Attention-Deficit/Hyperactivity Disorder) |
| TxGNN 예측 점수 | 99.92% |
| 근거 수준 | L4 |
| 한국 시판 현황 | 미판매 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 확보되어 있지 않습니다. 근거팩 자체의 평가에 따르면,
Trihexyphenidyl은 muscarinic 수용체 길항제(anticholinergic)로 추정되나, 이 기전이 ADHD의
핵심 병리(도파민/노르아드레날린 경로)와 합리적으로 연결된다는 근거는 부족한 것으로 나타났습니다.

유일하게 매칭된 문헌(PMID 21506147)도 ADHD를 직접 다룬 연구가 아니라, tic 장애와 dystonia가
동반된 임상 증후군에 대한 사례 시리즈입니다. 즉 이번 1순위 예측은 TxGNN 모델 점수는 높지만,
실제 문헌·기전적 뒷받침은 약한 상태이며, 예측 신뢰도를 그대로 받아들이기 어렵습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [21506147](https://pubmed.ncbi.nlm.nih.gov/21506147/) | 2011 | Case Series | Movement Disorders | Tic 장애와 지속성 dystonia가 동반된 임상 증후군 사례 시리즈로, ADHD 치료 효과에 대한 직접적 근거는 아님 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
경고·금기 등 안전성 정보가 전혀 확인되지 않아(DG001, Blocking) S1 안전성 초기평가 자체가
불가능한 상태입니다. 또한 1순위 예측 적응증(ADHD)은 TxGNN 점수는 높지만 문헌적·기전적
근거가 약해 근거팩 자체에서도 "합리적 연결 부족"으로 평가되었습니다.

**진행하려면 필요한 것:**
- TFDA/식약처 등 규제기관 허가사항(경고·금기) 확보 (DG001, Blocking)
- DrugBank 등에서 작용기전(MOA) 데이터 확보 (DG002)
- ADHD에 대한 직접적인 임상시험 또는 문헌 확보
- 참고: 근거팩 내 다른 후보 중 **PARK19A(청소년기 발병 파킨슨병)**, **PLA2G6-associated neurodegeneration**, **atypical juvenile parkinsonism**은 anticholinergic 기전과의 정합성이 상대적으로 높고 decision_stage가 S1(Research Question)으로 평가되어, ADHD보다 우선 검토할 가치가 있음
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

