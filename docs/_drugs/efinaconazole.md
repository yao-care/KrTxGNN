---
layout: default
title: Efinaconazole
parent: 僅模型預測 (L5)
nav_order: 240
evidence_level: L5
indication_count: 10
---

# Efinaconazole
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

# Efinaconazole: 조갑진균증에서 타액선 대세포암종으로

## 한 문장 요약

Efinaconazole은 삼아졸계 항진균제로, 조갑진균증(손발톱 백선) 치료에 사용되는 외용 항진균제입니다.
TxGNN 모델은 **타액선 대세포암종(Salivary Gland Large Cell Carcinoma)**에 효과가 있을 수 있다고 예측하였으나,
현재 이 예측을 지지하는 **임상시험 0건**, **문헌 0편**으로 근거가 전혀 없습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 조갑진균증 (손발톱 백선, Onychomycosis) |
| 예측 신규 적응증 | 타액선 대세포암종 (Salivary Gland Large Cell Carcinoma) |
| TxGNN 예측 점수 | 50.00% (모델 내 순위: 2,099,705위) |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Efinaconazole은 삼아졸계 항진균제로, 진균의 세포막 구성 성분인 에르고스테롤 합성 경로에서 핵심 효소인 **CYP51(라노스테롤 14α-탈메틸효소)**을 억제합니다. 에르고스테롤이 고갈되면 진균 세포막 기능이 손상되어 항진균 효과가 나타납니다. 현재 이용 가능한 근거 팩에 상세 MOA 데이터가 포함되어 있지 않으나, 공개된 약리학 정보에 근거하여 평가하였습니다.

타액선 대세포암종과의 기전적 연관성은 매우 간접적입니다. 포유류 세포에도 CYP51이 존재하여 콜레스테롤 합성에 관여하므로, 이론상 종양 세포의 지질 대사를 교란할 수 있다는 가설이 제기될 수 있습니다. 그러나 Efinaconazole은 **진균 CYP51에 대한 선택성이 매우 높고**, 국소 외용제로 설계된 약물이어서 전신 노출이 극히 제한적입니다. 항진균 농도에서의 전신 CYP 억제 효과는 동일 삼아졸계 약물인 ketoconazole·metyrapone과 비교할 수 없는 수준입니다.

TxGNN 예측 점수 **0.5는 모델의 경계값(boundary value)**에 해당하며, 순위 2,099,705위는 해당 모델이 이 약물-질환 조합에 대해 사실상 의미 있는 재창출 가능성을 인식하지 못하고 있음을 나타냅니다. 이번에 예측된 상위 10개 적응증이 모두 이 점수대에 집중된 점도 예측의 신뢰도가 낮음을 시사합니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 한국 시판 정보

Efinaconazole은 현재 한국에 허가된 제품이 없습니다 (허가 기록 0건).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 점수 0.5(경계값)와 순위 2,099,705위는 모델이 이 약물-질환 조합에 대해 의미 있는 예측 신호를 포착하지 못했음을 나타냅니다. 전체 10개 예측 적응증 모두 임상시험·문헌 근거가 전혀 없는 L5 수준이며, Efinaconazole의 외용 제형 특성상 종양학적 재창출에 요구되는 전신 약물 농도를 확보하기 어렵습니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 데이터 확보 (DrugBank API 조회를 통한 DG002 해소)
- MFDS 허가 현황 및 국내 유통 경로 재확인
- 경구·전신 투여 가능한 대체 제형 존재 여부 검토
- 동일 계열 삼아졸계 약물(itraconazole, ketoconazole)의 항종양 전임상 연구 문헌 검토
- 콜레스테롤 대사와 암 생물학 간 연관성에 관한 기초 연구 수행 후 재평가
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

