---
layout: default
title: Icodextrin
parent: 僅模型預測 (L5)
nav_order: 307
evidence_level: L5
indication_count: 10
---

# Icodextrin
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

# Icodextrin: 복막투석(PD)에서 과민성대장증후군(IBS)으로

## 한 문장 요약

Icodextrin은 복막투석(PD)액에 사용되는 삼투압 조절 성분으로, 복강 내에서 아밀라아제·말타아제에 의해 대사되는 비경구(복강내 투여) 약물입니다.
TxGNN 모델은 **과민성대장증후군(Irritable Bowel Syndrome)**에 효과가 있을 수 있다고 예측(점수 98.53%)했으나, 이를 뒷받침하는 **임상시험과 문헌이 현재 전혀 없으며**, 평가팀 자체 분석에서도 지식 그래프상의 공동발생 편향(spurious correlation)일 가능성이 높다고 판단하고 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 복막투석(PD) 용액의 삼투압 조절 성분 (한국 허가 자료 없음) |
| 예측 신규 적응증 | 과민성대장증후군 (Irritable Bowel Syndrome) |
| TxGNN 예측 점수 | 98.53% |
| 근거 수준 | L5 (모델 예측만 있음, 실제 연구 없음) |
| 한국 시판 현황 | ✗ 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 확보되어 있지 않습니다. 확인된 정보에 따르면 Icodextrin은 복막투석액의 삼투압 조절 성분으로, 경구 흡수가 아닌 복강 내 투여를 통해 작용하며 복막의 아밀라아제·말타아제에 의해 말토올리고당으로 대사됩니다.

평가팀의 기전 분석 결과, Icodextrin은 경구 장관용 약물이 아니며 IBS의 병태생리(장 운동 조절, 내장 과민성)와 연결되는 알려진 약리 경로가 없습니다. 임상시험·문헌 근거가 전혀 확인되지 않는 점을 함께 고려하면, 이 예측은 지식 그래프 내 질병 군집 간 간접 연결에 의한 공동발생 편향일 가능성이 높은 것으로 판단됩니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
근거 수준이 L5(모델 예측만 존재, 실제 연구 없음)이며 임상시험·문헌 근거가 전무합니다. 평가팀 자체 판단으로도 기전적 연관성이 낮아 지식 그래프 공동발생 편향으로 추정되므로, 현 시점에서 임상 개발을 진행할 근거가 부족합니다.

**진행하려면 필요한 것:**
- TFDA(허가기관) 원 라벨의 경고·금기 정보 확보 — 현재 데이터 공백(DG001, Blocking)으로 S1 안전성 초기평가 진입이 불가능한 상태
- 상세 작용기전(MOA) 데이터 확보 — DrugBank 등에서 추가 조회 필요 (DG002, High)
- IBS와의 기전적 연관성을 뒷받침할 전임상(in vitro/in vivo 장관 동력학) 데이터
- 관련 임상시험 또는 관찰 연구 신규 등록 여부 지속 모니터링

**참고 — 함께 평가된 다른 예측 후보(2~10순위)**
동일 평가에서 non-syndromic esophageal malformation, C1 inhibitor deficiency, potassium deficiency disease, serpinopathy, hereditary angioedema, esophageal disease, familial visceral myopathy, renal tubular acidosis, vitamin deficiency disorder 등 9건이 함께 예측되었으나 모두 임상시험·문헌 근거가 없고(evidence level L5, 단 renal tubular acidosis는 L4) 전부 **Hold** 판정입니다. 특히 potassium deficiency disease(4순위)는 Icodextrin 사용 시 알려진 전해질 손실(저나트륨혈증 등) 부작용과 방향이 상반되어, 단순 근거 부족을 넘어 **잠재적 역방향 위험 신호**로 별도 주의가 필요합니다. non-syndromic esophageal malformation과 familial visceral myopathy는 구조적/유전적 질환으로 약물 재창출 논리 자체가 적용되기 어려운 후보로 추적 우선순위에서 제외를 권장합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

