---
layout: default
title: Carbetocin
parent: 僅模型預測 (L5)
nav_order: 173
evidence_level: L5
indication_count: 2
---

# Carbetocin
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

# Carbetocin: 원 적응증 미상에서 Isotretinoin-like Syndrome(예측)으로

## 한 문장 요약

Carbetocin(DrugBank ID: DB01282)은 원래 어떤 적응증에 사용되었는지에 대한 자료 자체가 현재 확보되지 않은 상태입니다(원 적응증·작용기전 모두 데이터 갭). TxGNN 모델은 **Isotretinoin-like Syndrome**에 효과가 있을 수 있다고 예측했으나(예측 점수 99.15%), 이를 뒷받침하는 **임상시험이나 문헌은 현재 0건**이며, 근거 수준은 가장 낮은 단계인 **L5(모델 예측만 존재)**입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 자료 없음 (원 적응증·작용기전 데이터 갭, DG002) |
| 예측 신규 적응증 | Isotretinoin-like Syndrome |
| TxGNN 예측 점수 | 99.15% (단, 전체 후보 중 순위는 12,711위로 상위권은 아님) |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미출시 (등록 허가 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용기전(MOA) 데이터가 확보되지 않은 상태입니다(데이터 갭 DG002, 심각도 High). 다만 근거 팩에 포함된 참고 정보에 따르면, Carbetocin은 약리학적으로 장시간 작용형 옥시토신 수용체(OXTR) 작용제로 자궁 평활근 및 시상하부-뇌하수체 경로에 작용하는 것으로 추정됩니다(이는 원 자료의 공식 MOA 필드가 아닌 참고 추론 정보입니다).

그러나 이번에 예측된 "Isotretinoin-like Syndrome"은 표준 질병 온톨로지에서 흔히 쓰이는 명칭이 아니며, OXTR 신호 경로와 이 증후군의 병태생리 사이에 현재 식별 가능한 기전적 연결고리가 없습니다. 근거 팩 자체도 이 예측이 TxGNN 질병 어휘집(disease_vocab.csv)의 노드 명명이나 군집화 과정에서 발생한 잡음(위양성)일 가능성을 배제할 수 없다고 명시하고 있으며, 해당 질병 노드의 정식 정의(MONDO/ICD 대응 코드) 확인을 선행 과제로 제시하고 있습니다.

또한 예측 점수(99.15%)는 매우 높지만, 전체 후보 순위는 12,711위로 상대적으로 낮아 점수와 순위 사이에 괴리가 있습니다. 이는 TxGNN의 원시 점수만으로 우선순위를 판단하기 어렵다는 점을 시사하므로, 점수 단독 해석에는 주의가 필요합니다.

참고로 근거 팩에는 2순위 예측 후보로 **Goodman Syndrome**(원위 관절 구축증 계열의 희귀 유전 질환, 예측 점수 99.06%, 순위 13,781위)도 포함되어 있으나, 이 역시 OXTR 경로와의 알려진 병리학적 연관성이 없으며 동일한 수준의 기전적 타당성 문제를 안고 있습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 한국 시판 정보

Carbetocin은 현재 미출시 상태이며, 등록된 허가증이 없습니다(허가증 0건).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 근거 수준이 가장 낮은 L5(모델 예측만 존재, 임상시험·문헌 0건)이며, 원 적응증과 작용기전 데이터가 모두 확보되지 않아 기전적 타당성을 검증할 방법이 없습니다.
- 예측된 질병명("Isotretinoin-like Syndrome", "Goodman Syndrome") 자체가 표준 질병 온톨로지 용어인지 불확실하여, 모델 노이즈(위양성) 가능성이 높습니다.

**진행하려면 필요한 것:**
- 한국(및 대만) 허가사항(라벨) 확보·파싱 — 현재 Blocking 등급 데이터 갭(DG001)으로 안전성 초기평가(S1) 자체가 불가능한 상태
- DrugBank 등에서 정확한 원 적응증 및 작용기전(MOA) 확인 (DG002)
- disease_vocab.csv 상 "Isotretinoin-like Syndrome"·"Goodman Syndrome" 노드의 MONDO/ICD 매핑 여부 검증
- 동의어를 포함한 임상시험·문헌 재검색(예: distal arthrogryposis 계열 용어)
- 위 데이터 보강 후 재평가하여 근거 수준(L5→L4 이상) 상향 여부 확인
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

