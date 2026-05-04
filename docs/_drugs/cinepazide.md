---
layout: default
title: Cinepazide
parent: 僅模型預測 (L5)
nav_order: 168
evidence_level: L5
indication_count: 10
---

# Cinepazide
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

# Cinepazide: 허가 적응증 미확인에서 고전형 호지킨 림프종(림프구 결핍형)으로

---

## 한 문장 요약

Cinepazide는 PDE 억제 및 혈관 확장 특성을 가진 약물로 역사적으로 알려져 있으나, 현재 데이터에서 공식 허가 적응증이 확인되지 않으며 한국 내 시판 이력도 없습니다.
TxGNN 모델은 **고전형 호지킨 림프종 림프구 결핍형(classic Hodgkin lymphoma, lymphocyte-depleted type)**에 효과가 있을 수 있다고 예측하나,
이를 지지하는 **임상시험 및 문헌이 전혀 존재하지 않으며**, TxGNN 예측 순위 또한 전체 약물-질환 쌍 중 최하위권(1,998,370위)에 해당합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인된 허가 적응증 없음 |
| 예측 신규 적응증 | 고전형 호지킨 림프종 림프구 결핍형 (classic Hodgkin lymphoma, lymphocyte-depleted type) |
| TxGNN 예측 점수 | 50% (순위: 1,998,370위 — 예측 신뢰도 극히 낮음) |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 Cinepazide의 상세 작용 기전(MOA) 데이터가 없습니다. 알려진 정보에 따르면 Cinepazide는 PDE(phosphodiesterase) 억제 및 혈관 확장 특성을 가진 약물로 분류되며, 과거 뇌혈관 및 말초혈관 질환 영역에서 연구된 바 있습니다. 그러나 이 특성들이 혈액암 치료와 어떻게 연결되는지에 대한 전임상 또는 임상 근거는 전혀 없습니다.

림프구 결핍형 호지킨 림프종은 전체 호지킨 림프종 중 가장 희귀하고 예후가 불량한 아형으로, EBV 관련 병인과 CD30+ Reed-Sternberg 세포의 증식이 핵심 기전입니다. 표준 치료는 고강도 복합 화학요법이며, Brentuximab vedotin 등 CD30 표적 치료제가 개발되어 있습니다. Cinepazide의 혈관 활성 기전이 CD30 신호전달, NF-κB 경로, 또는 종양 면역 미세환경에 작용한다는 증거는 문헌상 확인되지 않습니다.

TxGNN 예측 점수(50%)와 순위(1,998,370위)를 함께 고려하면, 이 예측은 모델 전체 예측의 최하위권에 해당하며 모든 10개 후보 적응증이 동일한 점수와 인접 순위로 묶여 있습니다. 이는 모델이 실질적인 약물-질환 연관 신호를 포착했다기보다 기본값에 수렴한 결과일 가능성이 높습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> 참고: 본 약물은 한국 내 미시판 약물로 국내 공식 허가 사항이 존재하지 않습니다. 해외 규제기관 자료 및 원저자 문헌을 통한 안전성 프로파일 확보가 필요합니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
Cinepazide는 MOA 불명, 한국 내 미허가·미시판 상태이며, 예측 대상인 고전형 호지킨 림프종(림프구 결핍형)에 대한 임상시험·문헌 근거가 전무합니다. TxGNN 예측 순위가 최하위권(1,998,370위)으로 모델 예측 자체의 신뢰도도 매우 낮아 근거 수준 L5 단계에 해당합니다.

**진행하려면 필요한 것:**
- Cinepazide의 상세 작용 기전(MOA) 규명 (DrugBank API 재조회 또는 문헌 검색)
- 호지킨 림프종 또는 CD30+ 혈액암에 대한 전임상(in vitro / in vivo) 데이터 확보
- 한국 및 해외(일본, 프랑스 등 기존 사용 국가) 규제 허가 현황 재조사
- 경고, 금기, 약물 상호작용 포함 안전성 프로파일 완성
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

