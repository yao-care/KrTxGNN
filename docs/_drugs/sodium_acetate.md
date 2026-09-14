---
layout: default
title: Sodium Acetate
parent: 僅模型預測 (L5)
nav_order: 639
evidence_level: L5
indication_count: 10
---

# Sodium Acetate
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

# Sodium Acetate: 전해질 완충제에서 선천성 프로트롬빈 결핍증으로

## 한 문장 요약

Sodium Acetate는 전해질 및 산염기 균형을 조절하는 완충제로 알려져 있으며, 한국에는 아직 시판 허가 제품이 없습니다. TxGNN 모델은 **선천성 프로트롬빈 결핍증(Congenital Prothrombin Deficiency)**에 효과가 있을 수 있다고 예측했으나(예측 점수 99.98%), 이를 뒷받침하는 임상시험이나 문헌은 현재 하나도 확인되지 않았습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (한국 미시판, 허가 데이터 없음) |
| 예측 신규 적응증 | 선천성 프로트롬빈 결핍증 (Congenital Prothrombin Deficiency) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 없습니다. Evidence Pack에 기재된 설명에 따르면, Sodium Acetate는 전해질/산염기 균형을 조절하는 완충제로, 응고인자인 프로트롬빈의 합성이나 기능과 연결되는 알려진 기전은 없습니다.

TxGNN 예측 점수 자체는 99.98%로 매우 높지만, 이는 순수 그래프 임베딩 기반 예측이며 이를 뒷받침하는 임상시험, 문헌, 전임상 근거가 전혀 존재하지 않습니다. 따라서 현 시점에서는 기전적 타당성이 낮은 예측으로 판단됩니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 점수는 높으나(99.98%), 이를 지지하는 임상시험·문헌·기전적 근거가 전혀 없는 순수 모델 예측(L5)입니다. 또한 허가사항의 경고·금기 정보와 작용 기전(MOA) 데이터가 모두 확보되지 않아, 안전성 초기 평가(S1) 단계로 진입할 수 없는 상태입니다(DG001 Blocking, DG002 High).

**진행하려면 필요한 것:**
- TFDA/식약처 허가사항(경고·금기) 원문 확보 — DG001 (Blocking)
- DrugBank 등에서 상세 작용 기전(MOA) 데이터 확보 — DG002 (High)
- 선천성 프로트롬빈 결핍증에 대한 최소한의 전임상 또는 기전 연구 근거 확보
- 참고: 같은 Evidence Pack 내 소화불량(dyspepsia)·위마비(gastroparesis)는 SCFA 흡수 관련 간접 기전 가설(L4, Research Question)이 존재해, 향후 우선순위 재검토 시 함께 고려할 가치가 있습니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

