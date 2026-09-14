---
layout: default
title: Spironolactone
parent: 僅模型預測 (L5)
nav_order: 645
evidence_level: L5
indication_count: 2
---

# Spironolactone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Spironolactone: 기존 적응증 정보 없음에서 두피 단순 무모증(Hypotrichosis Simplex of the Scalp)으로

## 한 문장 요약

Spironolactone은 알도스테론 길항제 계열 약물이나, 본 Evidence Pack에는 기존 승인 적응증과 공식 작용기전(MOA) 정보가 등록되어 있지 않습니다.
TxGNN 모델은 **두피 단순 무모증(Hypotrichosis Simplex of the Scalp)**에 효과가 있을 수 있다고 예측했으나(예측 점수 99.26%),
이를 뒷받침하는 임상시험·문헌 근거는 현재 전혀 없으며 근거 수준은 최하 등급(L5)입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 등록된 정보 없음 |
| 예측 신규 적응증 | 두피 단순 무모증 (Hypotrichosis Simplex of the Scalp) |
| TxGNN 예측 점수 | 99.26% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미상장 (국내 미출시) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

공식 작용기전(MOA) 데이터는 현재 확보되지 않았습니다(DrugBank 조회 필요, DG002). 다만 TxGNN 매칭 근거에 기재된 내용에 따르면, Spironolactone은 알도스테론 길항제이자 항안드로겐 약물로, 여성형 안드로겐성 탈모(androgenetic alopecia)에서 모낭 안드로겐 수용체 활성을 억제하는 방식으로 임상적으로 사용된 바 있습니다.

그러나 예측된 신규 적응증인 두피 단순 무모증(hypotrichosis simplex of the scalp)은 CDSN, APCDD1 등 유전자 돌연변이에 의한 상염색체 우성 유전질환으로, 모낭 각화 이상과 모낭 주기 발달 결함이 병인이며 안드로겐 경로와는 직접적 연관이 없습니다. 즉 항안드로겐 기전에서 유전성 무모증으로의 외삽 근거는 약합니다.

2순위 후보인 congenital hypotrichosis milia 역시 비안드로겐 의존성 희귀 유전질환으로, 동일한 문제(기전적 연관성 부재)가 지적되고 있습니다. 두 후보 모두 TxGNN의 지식그래프 위상학적 유사성에 기반한 추론일 가능성이 높으며, 생물학적 실증 근거는 뒷받침되지 않습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
근거 수준이 L5(모델 예측만 존재)로, 임상시험이나 문헌 근거가 전혀 없으며 기전적 연관성도 자체 평가상 약하다고 명시되어 있습니다. 또한 TFDA/식약처 공식 라벨(경고·금기, DG001, Blocking)과 MOA(DG002) 등 핵심 데이터가 누락되어 있어 안전성 초기평가(S1) 단계 진입이 불가능한 상태입니다.

**진행하려면 필요한 것:**
- 규제기관 공식 라벨(경고사항·금기사항) 확보 — DG001, Blocking, S1 진입 필수 조건
- DrugBank API를 통한 공식 MOA 데이터 확보 — DG002
- Hypotrichosis simplex / congenital hypotrichosis milia 관련 전임상·문헌 근거 추가 조사 또는 부재 확인
- 국내(한국) 허가 및 시판 현황 재확인
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

