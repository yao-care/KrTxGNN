---
layout: default
title: Hydroxocobalamin
parent: 僅模型預測 (L5)
nav_order: 303
evidence_level: L5
indication_count: 2
---

# Hydroxocobalamin
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

# Hydroxocobalamin: 원 적응증 미기록에서 식도정맥류 출혈(Esophageal Varices with Bleeding)로

## 한 문장 요약

Hydroxocobalamin(DrugBank ID: DB00200)은 이번 Evidence Pack에 원 적응증 및 작용 기전(MOA) 정보가 기록되어 있지 않습니다. TxGNN 모델은 **식도정맥류 출혈(Esophageal Varices with Bleeding)**에 효과가 있을 수 있다고 예측(점수 99.23%)하며, 거의 동일한 점수로 **식도정맥류(출혈 없음)**도 함께 예측되었습니다. 다만 현재 이를 뒷받침하는 **임상시험이나 문헌은 0건**으로, 순수 모델 예측 단계(L5)입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (원본 데이터셋에 원 적응증 미기록) |
| 예측 신규 적응증 | 식도정맥류 출혈 (Esophageal Varices with Bleeding) |
| TxGNN 예측 점수 | 99.23% |
| 근거 수준 | L5 (모델 예측만 있음, 실제 연구 없음) |
| 한국 시판 현황 | ✗ 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터와 원 적응증 기록이 모두 제공되지 않았습니다. TxGNN 모델은 DrugBank 지식그래프(DB00200) 상의 약물-질병 관계 패턴 학습을 통해 식도정맥류 출혈에 대한 잠재적 연관성을 예측하였으나, 이 예측을 뒷받침할 기전적 근거는 현재 Evidence Pack에 포함되어 있지 않습니다.

주목할 점은, 순위 2위 예측인 "식도정맥류(출혈 없음)"이 1위 예측과 거의 동일한 점수(0.99232435... vs 0.99232435...)와 인접한 순위(rank 11778 / 11779)를 보인다는 것입니다. 이는 모델이 "출혈 유무"라는 세부 임상적 차이를 구분해서 학습했다기보다, "식도정맥류"라는 질환 군 전체와의 넓은 연관성을 포착했을 가능성을 시사합니다. 따라서 이 예측은 기전적 타당성 검증 없이는 신뢰도를 판단하기 어렵습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- TxGNN 예측 점수는 높으나(99.23%), 이를 뒷받침하는 임상시험·문헌 근거가 전무하여 L5(모델 예측 단독) 수준에 그칩니다.
- 원 적응증, 작용 기전(MOA), 허가사항(경고·금기) 정보가 모두 확보되지 않아 기전적 타당성 및 안전성을 판단할 수 없습니다.
- 특히 "TFDA 仿單警語/禁忌" 데이터 갭(DG001)은 **Blocking** 등급으로 지정되어 있어, 현 상태로는 S1 안전성 초평 단계에 진입할 수 없습니다.
- 해당 약물은 한국(원 데이터 기준 지역) 내 시판 허가 이력이 없습니다(허가증 0건).

**진행하려면 필요한 것:**
- DrugBank API를 통한 작용 기전(MOA) 데이터 확보 (DG002)
- 규제기관 공식 라벨/허가사항(경고, 금기, 상호작용) 확보 — S1 안전성 초평 진입을 위한 필수 선행 조건 (DG001)
- ClinicalTrials.gov, ICTRP, PubMed에 대한 검색어 확장(동의어·MeSH 용어 포함) 재조회를 통한 근거 재탐색
- "식도정맥류 출혈" vs "식도정맥류(출혈 없음)" 두 예측이 별개 기전에 의한 것인지, 동일 질환군 연관성의 중복 예측인지에 대한 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

