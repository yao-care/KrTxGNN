---
layout: default
title: Adapalene
parent: 僅模型預測 (L5)
nav_order: 24
evidence_level: L5
indication_count: 1
---

# Adapalene
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

# Adapalene: 여드름에서 혈장 아연 상승으로

## 한 문장 요약

Adapalene은 제3세대 국소 레티노이드로, 원래 여드름(Acne Vulgaris) 치료에 사용되어 왔습니다.
TxGNN 모델은 **혈장 아연 상승(zinc, elevated plasma)**에 효과가 있을 수 있다고 예측하나,
현재 이 방향을 지지하는 **임상시험 및 문헌 근거가 전무**합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (한국 미시판) |
| 예측 신규 적응증 | 혈장 아연 상승 (zinc, elevated plasma) |
| TxGNN 예측 점수 | 99.51% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 제공되지 않았습니다. 알려진 정보에 따르면, Adapalene은 제3세대 국소 레티노이드로서 RAR-β/γ(레티노산 수용체)에 선택적으로 결합하여 세포 분화 및 염증을 조절합니다.

이론적 기전 연결고리는 다음과 같습니다. RAR/RXR 이형이합체는 아연 손가락 단백질(zinc finger protein) 구조를 가지며, 아연을 구조적 보조인자로 필요로 합니다. RAR 경로 활성화는 금속티오네인(metallothionein) 발현 조절을 통해 세포 내외 아연 분포에 간접적인 영향을 줄 수 있습니다. 또한 임상적으로 아연 결핍이 비타민 A 대사를 저해한다는 사실은 양방향 상호작용의 가능성을 시사합니다.

다만, '혈장 아연 상승(zinc, elevated plasma)'은 확립된 질병 진단명이 아닌 실험실 이상 소견이며, 임상적 의미가 불명확합니다. TxGNN의 높은 예측 점수(0.995)는 지식 그래프 내 아연–비타민 A–RAR 공출현 관계를 반영한 것으로, 실제 인과적 치료 연관성을 직접 의미하지는 않습니다.

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
TxGNN 예측 점수(99.51%)는 높으나, 이를 지지하는 임상시험 및 문헌 근거가 전혀 없는 L5 수준이며, 예측 대상이 명확한 질환이 아닌 실험실 이상 소견입니다. 한국 미시판 약물로 국내 안전성 데이터도 부재하여 현 단계에서 진행은 권장되지 않습니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 상세 데이터 확보 (DrugBank API 조회)
- 혈장 아연 상승과 레티노이드 간 연관성에 관한 전임상·기초 연구 탐색
- '혈장 아연 상승'의 임상적 정의 및 치료 가능 여부 명확화
- 한국 식품의약품안전처 허가 현황 및 TFDA 안전성(경고·금기) 데이터 확보
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

