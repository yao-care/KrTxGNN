---
layout: default
title: Ranolazine
parent: 僅模型預測 (L5)
nav_order: 592
evidence_level: L5
indication_count: 1
---

# Ranolazine
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

# Ranolazine: 만성 협심증에서 신성 항이뇨 부적절 증후군으로

## 한 문장 요약

Ranolazine(DB00243)은 해외에서 만성 협심증(Chronic Angina) 치료제로 알려져 있으나, 한국에는 아직 허가·시판되지 않은 약물입니다.
TxGNN 모델은 **신성 항이뇨 부적절 증후군(Nephrogenic Syndrome of Inappropriate Antidiuresis)**에 효과가 있을 수 있다고 예측했으나(점수 99.65%),
현재 이를 뒷받침하는 **임상시험이나 문헌 근거는 전무**하여 순수 모델 예측 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 만성 협심증 (해외 승인 기준, 한국 허가 정보 없음) |
| 예측 신규 적응증 | 신성 항이뇨 부적절 증후군 (Nephrogenic Syndrome of Inappropriate Antidiuresis) |
| TxGNN 예측 점수 | 99.65% (전체 순위 6,590위) |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 이 약물의 상세 작용기전(MOA) 데이터가 확보되지 않았습니다(Data Gap). DrugBank 조회를 통한 MOA 보완이 필요한 상태입니다.

TxGNN의 기전적 연관성 분석(mechanistic_link) 및 기존 적응증과의 유사성 분석(similarity_to_original) 역시 아직 수행되지 않은 상태(pending)입니다. 즉, 이번 예측은 모델이 산출한 점수 외에 이를 뒷받침할 기전적 설명이나 실제 근거가 현재로서는 없습니다.

만성 협심증(원 적응증)과 신성 항이뇨 부적절 증후군(예측 적응증)은 임상적으로 서로 다른 질환 범주에 속하며, 현재 확보된 정보만으로는 두 적응증 간의 약리학적 연결고리를 설명하기 어렵습니다. 향후 MOA 데이터 확보와 문헌 검색이 선행되어야 이 예측의 타당성을 평가할 수 있습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (TFDA/식약처 수준의 경고·금기·상호작용 정보가 현재 확보되지 않아 S1 안전성 초평가가 불가능한 상태입니다.)

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수(99.65%)는 높으나 이를 뒷받침하는 임상시험, 문헌, 기전 근거가 전혀 없고(L5), 안전성 정보(경고·금기·DDI)와 MOA가 모두 확보되지 않아 안전성 초평가(S1) 진입이 불가능합니다. 또한 한국 내 허가·시판 이력이 없어 규제 경로 확인도 필요합니다.

**진행하려면 필요한 것:**
- TFDA(또는 식약처) 공식 자료를 통한 경고/금기 사항 확보 (Blocking 항목)
- DrugBank API를 통한 정확한 작용기전(MOA) 확인
- 신성 항이뇨 부적절 증후군 관련 임상시험·문헌 검색 (ClinicalTrials.gov, PubMed 재조회)
- 기전적 연관성(mechanistic_link) 및 원 적응증과의 유사성 분석 완료
- 한국 내 허가 가능성 및 규제 경로 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

