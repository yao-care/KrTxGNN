---
layout: default
title: Luspatercept
parent: 모델 예측만 (L5)
nav_order: 453
evidence_level: L5
indication_count: 10
---

# Luspatercept
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

# Luspatercept: 적응증 정보 없음에서 Monosomy X로

## 한 문장 요약

Luspatercept(DB12281)는 대만에 허가된 제품이 없어 원 적응증 정보가 확보되지 않았습니다. TxGNN 모델은 1순위로 **Monosomy X(단일 X 염색체 증후군)**에 대해 예측 점수 95.99%를 제시했지만, 이를 뒷받침하는 임상시험·문헌은 한 건도 없으며 근거 텍스트 자체가 "지식그래프 상의 간접 공출현 잡음일 가능성"을 지적하고 있습니다. 전체 10개 예측 적응증 모두 L5(모델 예측 단독) 수준입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (원 적응증 정보 미확보) |
| 예측 신규 적응증 | Monosomy X (단일 X 염색체 증후군) |
| TxGNN 예측 점수 | 95.99% (rank 47,208) |
| 근거 수준 | L5 (모델 예측만 있음, 임상시험·문헌 없음) |
| 대만 시판 현황 | 미상장 (허가 제품 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 Luspatercept의 상세 작용기전(MOA) 데이터는 확보되지 않았습니다(Drug-Level Data Gap, 심각도 High). 다만 개별 후보의 근거 텍스트(rank 7)에는 Luspatercept가 변형된 ActRIIB-Fc 융합단백질로 GDF11 등 TGF-β superfamily 리간드를 포집해 Smad2/3 신호를 억제함으로써 적혈구 후기 성숙을 촉진한다는 설명이 부분적으로 담겨 있으나, drug 레벨 MOA 필드 자체는 비어 있어 교차 검증이 필요합니다.

1순위 예측인 Monosomy X(단일 X 염색체, 터너증후군형)는 적혈구 성숙이나 TGF-β 신호와 알려진 기전적 연관성이 없으며, 근거 텍스트가 직접 "지식그래프 상의 간접 공출현 잡음일 가능성"을 명시합니다. 즉 TxGNN 점수는 높지만 생물학적 타당성은 낮습니다.

오히려 순위가 낮은 후보들이 기전상 더 설득력 있습니다: pyruvate kinase deficiency(6위), thalassemia beta+ silent allele(7위), Hb Bart's hydrops fetalis(10위)는 모두 적혈구 생성/용혈성 질환 계열로 Luspatercept의 적혈구 성숙 촉진 기전과 간접적으로 연결되어 별도로 "Research Question" 단계로 분류되어 있습니다. 다만 이들 역시 임상시험·문헌 근거는 전무합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다. (10개 예측 적응증 전체에서 ClinicalTrials.gov·ICTRP 등록 0건)

## 문헌 근거

현재 관련 문헌이 없습니다. (10개 예측 적응증 전체에서 PubMed 문헌 0건)

## 대만 시판 정보

대만 내 허가 제품이 없습니다 (미상장, 허가증 0건).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. 다만 대만 미상장으로 참조 가능한 허가사항 자체가 없으며, TFDA 첨부문서의 경고·금기 정보 확보가 Blocking 등급 데이터 갭(DG001)으로 남아 있습니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
10개 예측 적응증 모두 L5(모델 예측 단독)이며, 1순위 후보(Monosomy X)는 근거 텍스트 자체가 낮은 생물학적 타당성을 지적하고 있습니다. 임상시험·문헌·대만 허가 정보가 모두 부재해 실사용 근거로 진행하기 어렵습니다.

**진행하려면 필요한 것:**
- TFDA(또는 해당 규제기관) 첨부문서의 경고·금기 정보 확보 (Blocking, DG001)
- DrugBank 등을 통한 공식 MOA 확정 (High, DG002)
- 기전상 더 설득력 있는 후보(thalassemia beta+, PK deficiency, Hb Bart's hydrops fetalis)에 대한 ClinicalTrials.gov·PubMed 외부 재검색
- Monosomy X 예측이 실제 신호인지 지식그래프 잡음인지 판별할 추가 검증
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

