---
layout: default
title: Vasopressin
parent: 僅模型預測 (L5)
nav_order: 718
evidence_level: L5
indication_count: 2
---

# Vasopressin
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

# Vasopressin: 적응증 정보 없음에서 선천성 프로트롬빈 결핍증으로

## 한 문장 요약

이번 Evidence Pack에는 Vasopressin(DB00067)의 기존 적응증 및 작용기전(MOA) 정보가 포함되어 있지 않습니다.
TxGNN 모델은 **선천성 프로트롬빈 결핍증(Congenital Prothrombin Deficiency)**에 효과가 있을 수 있다고 예측(점수 99.63%)하지만,
관련 **임상시험은 0건**이며, 제시된 **문헌 3편** 역시 이 질환을 직접 다루지 않아 근거가 약합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (허가 자료 미확보) |
| 예측 신규 적응증 | 선천성 프로트롬빈 결핍증 (Congenital Prothrombin Deficiency) |
| TxGNN 예측 점수 | 99.63% (rank 6912) |
| 근거 수준 | L4 |
| 한국 시판 현황 | 미상시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다(DrugBank MOA 조회 필요, DG002).

다만 제공된 재창출 근거(rationale)에 따르면, Vasopressin은 V2 수용체 작용을 통해 혈관내피세포에서 vWF/Factor VIII 방출을 유도할 수 있으며, 이는 desmopressin(DDAVP)과 유사한 class effect로 알려져 있습니다. 그러나 이 기전은 Factor VIII 결핍을 표적으로 하며, 선천성 프로트롬빈(Factor II) 결핍증의 병태생리(간에서의 합성 결함)와는 직접적인 연관이 없습니다.

TxGNN의 높은 예측 점수는 지식그래프 상 "응고인자 대체요법" 노드 간의 간접적 연결을 반영한 것으로 추정되며, 프로트롬빈에 특이적인 기전적 근거는 확인되지 않습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Review | Autoimmunity Reviews | 후천성 A형 혈우병(항-FVIII 항체) 개요. 선천성 프로트롬빈 결핍증과 직접 관련 없음 |
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Case Report | Rinsho Ketsueki (일본혈액학회지) | 선천성 Factor V+VIII 복합 결핍 1예, DDAVP 투여 사례 (Factor II 결핍 아님) |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Case Report | Rinsho Ketsueki (일본혈액학회지) | Factor V+VIII 복합 결핍 임산부의 제왕절개 관리 (Factor II 결핍 아님) |

**주의:** 위 3편 모두 대상 질환(선천성 프로트롬빈 결핍증)을 직접 다루지 않으며, 관련성 분류가 "pending" 상태입니다.

## 한국 시판 정보

한국 내 허가증이 없습니다 (미상시, 총 0건).

## 안전성 고려사항

안전성 관련 자료(경고, 금기, 약물상호작용)가 현재 확보되지 않았습니다. 특히 TFDA/식약처 첨부문서(경고·금기) 미확보(DG001, Blocking)로 인해 안전성 초기평가(S1) 단계 진입이 불가능한 상태입니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측된 신규 적응증(선천성 프로트롬빈 결핍증)에 대한 직접적인 임상시험이나 문헌이 전혀 없고, 제시된 문헌 3편도 다른 응고인자 결핍(Factor V/VIII)을 다룬 것으로 기전적 연관성이 약합니다. 또한 MOA와 안전성 첨부문서 자료 부재로 안전성 초기평가(S1) 진입이 원천적으로 막혀 있습니다(Blocking data gap).

**진행하려면 필요한 것:**
- DrugBank API를 통한 Vasopressin 상세 작용기전(MOA) 확보
- TFDA/식약처 공식 첨부문서(경고, 금기) 확보 (DG001 해소)
- 선천성 프로트롬빈 결핍증에 특이적인 전임상/기전 연구 확인
- Vasopressin의 기존 승인 적응증 데이터 보완 (현재 원본 데이터 공백)

**참고:** 2순위 예측 적응증인 약물유발성 골다공증(drug-induced osteoporosis, 점수 99.62%)은 관련 임상시험·문헌이 전혀 없고 기전적 타당성도 확인되지 않아(근거 수준 L5) 이번 평가 대상에서 제외했습니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

