---
layout: default
title: Zolbetuximab
parent: 僅模型預測 (L5)
nav_order: 730
evidence_level: L5
indication_count: 10
---

# Zolbetuximab
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

# Zolbetuximab: 위암에서 당뇨병성 백내장(Diabetic Cataract)으로

## 한 문장 요약

Zolbetuximab은 CLDN18.2(Claudin-18.2) 양성 위암/위식도접합부 선암종에 대한 항체 기반 항암제로 알려져 있으나, 국내 정식 등재된 작용기전(MOA)·적응증 자료는 확인되지 않았습니다. TxGNN 모델은 **당뇨병성 백내장(Diabetic Cataract)**을 비롯해 백내장 계열 적응증 10건을 98% 이상의 높은 점수로 예측했지만, 이를 뒷받침하는 임상시험이나 문헌은 현재 하나도 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 위암/위식도접합부 선암종 (CLDN18.2 양성, 국내 공식 기록 없음) |
| 예측 신규 적응증 | 당뇨병성 백내장 (Diabetic Cataract) |
| TxGNN 예측 점수 | 98.49% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

Zolbetuximab의 작용기전은 국내 데이터베이스에 등재되어 있지 않습니다. 다만 알려진 정보에 따르면 이 약물은 CLDN18.2에 결합하는 단클론항체로, ADCC(항체의존성 세포독성)와 CDC(보체의존성 세포독성) 기전을 통해 CLDN18.2 양성 위암/위식도접합부 선암종 세포를 사멸시키는 방식으로 개발되었습니다.

CLDN18.2는 정상적으로는 위 점막 상피의 밀착연접(tight junction)에서만 제한적으로 발현되며, 수정체 상피세포·다원경로(polyol pathway)·최종당화산물(AGE) 축적 등 당뇨병성 백내장의 병리 기전과는 생물학적 연관성이 보고된 바 없습니다. 실제로 순위 1~10위 예측 적응증이 모두 백내장 계열(당뇨병성, 노년성, 피질성, 핵성, 미성숙, 유전성 등)에 집중되어 있는 점은, 지식그래프 상 안과 관련 노드가 희소하여 발생한 연결 잡음(false positive)일 가능성을 시사합니다. 즉, 기전적으로 뒷받침되는 가설이라기보다 TxGNN 임베딩 공간의 인위적 클러스터링으로 판단됩니다.

**참고: 상위 10개 예측 후보 전체**

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 |
|------|-----------|-----------|----------|
| 1 | Diabetic cataract | 98.49% | L5 |
| 2 | Mature cataract | 98.41% | L5 |
| 3 | Diabetes mellitus type 2 associated cataract | 98.41% | L5 |
| 4 | Immature cataract | 98.41% | L5 |
| 5 | Craniostenosis cataract | 98.41% | L5 |
| 6 | Tetanic cataract | 98.41% | L5 |
| 7 | Cortical cataract | 98.39% | L5 |
| 8 | Nuclear senile cataract | 98.39% | L5 |
| 9 | Senile cataract | 98.32% | L5 |
| 10 | Diabetic retinopathy | 98.20% | L5 |

10건 모두 임상시험·문헌 근거 없음, 기전 연관성 없음, Hold 권고로 일치합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

Zolbetuximab은 현재 한국에 허가된 제품이 없습니다 (미시판, 허가증 0건).

## 세포독성 (항종양약에만 해당)

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (항체 매개 세포독성 — ADCC/CDC 기전, CLDN18.2 표적 단클론항체) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 국내 미승인 상태로 취급 지침 자료 없음 |

## 안전성 고려사항

국내 미승인 약물로, 안전성 경고·금기·약물상호작용에 대한 공식 자료가 확인되지 않았습니다. 안전성 정보는 향후 허가사항 공개 시 참조하시기 바랍니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측된 10건 모두 근거 수준 L5(모델 예측만 존재, 실제 연구 없음)이며, 예측 적응증이 백내장 계열에 편중되어 있어 지식그래프 연결 잡음으로 판단됩니다. 또한 원 약물의 국내 허가사항, MOA, 안전성 자료가 모두 확보되지 않은 차단(Blocking) 수준의 데이터 공백 상태입니다.

**진행하려면 필요한 것:**
- TFDA/MFDS 등 규제기관의 정식 허가사항(경고·금기) 확보
- DrugBank API를 통한 공식 MOA 데이터 확인
- 당뇨병성 백내장/망막병증 관련 CLDN18.2 발현 여부에 대한 전임상 근거
- 예측 클러스터가 실제 생물학적 신호인지, 그래프 구조상 잡음인지에 대한 별도 검증
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

