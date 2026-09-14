---
layout: default
title: Tiemonium Iodide
parent: 僅模型預測 (L5)
nav_order: 678
evidence_level: L5
indication_count: 1
---

# Tiemonium Iodide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Tiemonium Iodide: 적응증 미상에서 불면증(Insomnia)으로

## 한 문장 요약

Tiemonium Iodide(DB13666)는 원본 적응증 및 작용 기전 데이터가 확보되지 않은 상태입니다.
TxGNN 모델은 **불면증(Insomnia)**에 효과가 있을 수 있다고 예측했으나(예측 점수 99.44%),
이를 뒷받침하는 **임상시험이나 문헌은 현재 0건**이며, 예비 약리학적 추론은 오히려
이 예측 방향과 상충됩니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 미상 (원본 데이터 부재, DrugBank 재조회 필요) |
| 예측 신규 적응증 | 불면증 (Insomnia disease) |
| TxGNN 예측 점수 | 99.44% |
| 근거 수준 | L5 (모델 예측만 존재, 실제 연구 없음) |
| 한국 시판 현황 | 미상시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 없습니다. DrugBank ID(DB13666)만 확인되었으며,
원본 적응증 기록도 확보되지 않아 기존 적응증과 예측 신규 적응증 간의 연관성을 평가할 수 없습니다.

다만 예비 약리학적 검토에 따르면 Tiemonium Iodide는 **4급 암모늄(quaternary ammonium) 구조**를
가지고 있어 혈액뇌장벽(BBB) 투과율이 낮을 것으로 추정됩니다. 이는 일반적으로 중추신경계
진정 작용을 전제로 하는 불면증 치료 기전과는 방향성이 맞지 않으며, TxGNN 예측과
약리학적 상식 사이에 긴장 관계가 존재합니다.

따라서 이 예측은 지식그래프 상의 패턴 기반 추정일 가능성이 높고, 원본 적응증·MOA 자료를
확보한 뒤 재평가가 필요합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
근거 수준이 L5(모델 예측만 존재)에 불과하고, 이를 지지하는 임상시험이나 문헌이 전무합니다.
더불어 원본 MOA 및 적응증 데이터가 없는 상태에서, 확보된 예비 약리학적 특성(4급 암모늄 구조,
낮은 BBB 투과율)이 오히려 중추성 진정 기전을 전제로 하는 불면증 적응증과 방향성이
상충되어 S1 안전성 초평가 단계로 진행할 수 없습니다.

**진행하려면 필요한 것:**
- TFDA(한국 허가) 공식 사이트에서 허가사항/경고·금기 원문 확보 (DG001, Blocking)
- DrugBank API를 통한 정확한 작용 기전(MOA) 데이터 확보 (DG002, High)
- 원본 승인 적응증 확인 및 기록 보완
- ClinicalTrials.gov / PubMed 재검색을 통한 불면증 관련 근거 유무 확인
- 위 자료 확보 후 기전적 연관성 및 안전성 재평가 진행
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

