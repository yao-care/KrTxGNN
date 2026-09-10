---
layout: default
title: Lactic Acid
parent: 僅模型預測 (L5)
nav_order: 420
evidence_level: L5
indication_count: 10
---

# Lactic Acid
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

# Lactic Acid: 기존 적응증 미상에서 비정형 대동맥 축착증(Atypical Coarctation of Aorta)으로

## 한 문장 요약

Lactic acid(DB04398)는 국내 허가 이력이 없고 원래 적응증 및 작용기전 정보도 확보되지 않은 물질입니다. TxGNN 모델은 **비정형 대동맥 축착증(Atypical Coarctation of Aorta)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 **임상시험이나 문헌은 전혀 없습니다(0건)**. 이 예측은 모델 임베딩 공간에서 나온 순수 통계적 결과로, 실증적 근거가 없는 상태입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인되지 않음 (등재 적응증 자료 없음) |
| 예측 신규 적응증 | 비정형 대동맥 축착증 (Atypical Coarctation of Aorta) |
| TxGNN 예측 점수 | 99.59% |
| 근거 수준 | L5 (임상시험 0건, 문헌 0건) |
| 한국 시판 현황 | ✗ 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 없습니다. Lactic acid는 체내 대사 중간산물로, 원래 적응증 정보 자체도 확보되지 않아 기존 적응증과 신규 적응증 간의 연관성을 판단할 근거가 없습니다.

Evidence Pack에 기재된 재창출 근거(rationale)에 따르면, 비정형 대동맥 축착증은 극히 드문 선천성 심혈관 기형으로, lactic acid의 대사적 특성과 분자적으로 알려진 연결고리가 없습니다. 이 예측은 TxGNN 임베딩 공간에서 자료가 희소한 영역(rare disease)에 대해 높은 점수가 산출된 사례로, 실제 기전적 타당성보다는 모델의 구조적 한계로 인한 잡음(noise)일 가능성이 높습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 한국 시판 정보

국내(대만 기준 자료) 허가 정보가 없습니다. 본 약물은 현재 미출시 상태이며, 등록된 허가증이 0건입니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
1순위 예측 적응증(비정형 대동맥 축착증)은 TxGNN 점수는 높지만 임상시험·문헌 근거가 전무한 L5 등급이며, 원료의약품 자체의 작용기전과 기존 적응증 정보도 확보되지 않아 안전성 초기 평가(S1)조차 진행할 수 없는 상태입니다. 참고로 2순위(aortic malformation), 6순위(esophageal disease), 9순위(eye disease) 등은 임상시험·문헌 수는 많으나, 검토 결과 대부분 lactate를 치료제가 아닌 수술 중 관류/대사 모니터링 지표로 언급하거나, 종양 세포가 생성하는 내인성 lactate의 병리적 역할을 다룬 기초연구로, 외인성 lactic acid 투여를 지지하는 근거로 보기 어렵습니다.

**진행하려면 필요한 것:**
- TFDA/식약처 등 규제기관의 허가사항(경고·금기) 확보 (현재 Blocking 데이터 갭)
- DrugBank 기반 작용기전(MOA) 데이터 확보
- lactic acid의 실제 승인 적응증(원 용도) 확인 — 현재 원본 데이터 자체가 누락되어 있어 재창출 타당성 평가의 기준점이 없음
- 상기 데이터 미보완 시, 본 후보는 현 단계에서 추가 진행 보류 권장
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

