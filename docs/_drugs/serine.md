---
layout: default
title: Serine
parent: 僅模型預測 (L5)
nav_order: 634
evidence_level: L5
indication_count: 10
---

# Serine
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

# Serine: 아미노산 보충제에서 Familial Visceral Myopathy로

## 한 문장 요약

Serine은 비필수 아미노산으로, 한국에서 허가된 의약품 형태로 시판되고 있지 않으며 원 적응증 정보도 확보되지 않았습니다.
TxGNN 모델은 **Familial Visceral Myopathy(가족성 내장근육병증)**에 효과가 있을 수 있다고 예측(점수 99.99%)하지만,
이를 뒷받침하는 **임상시험이나 문헌은 현재 전혀 없습니다**.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (한국 미상장, 원 적응증 데이터 없음) |
| 예측 신규 적응증 | Familial Visceral Myopathy (가족성 내장근육병증) |
| TxGNN 예측 점수 | 99.99% (rank 427) |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미상장 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 없습니다. Serine은 비필수 아미노산으로 단백질 합성 및 일부 대사 경로에 관여하는 것으로 알려져 있으나, 구체적인 약리 기전 자료는 확보되지 않았습니다.

Evidence Pack에 기재된 평가 의견에 따르면, 이번 예측은 "임상시험이나 문헌 근거가 전혀 없이 TxGNN 모델 예측 점수만 존재하며, 기전 자료로 뒷받침되지 않는다"고 명시되어 있습니다. 즉, 지식그래프 상의 간접적 노드 연결에서 비롯된 점수일 가능성이 높고, 인과적 근거는 아닙니다.

참고로 이번 Evidence Pack에는 Serine에 대한 예측 적응증이 10건 포함되어 있는데, 2순위인 intestinal obstruction조차 관련 임상시험 9건이 모두 무관(grade C)으로 판정되었고, 6순위 angle-closure glaucoma의 문헌 근거는 "serine **protease** 56(PRSS56)" 유전자와의 명칭상 우연의 일치일 뿐 아미노산 Serine과는 무관한 것으로 확인되었습니다. 이는 이번 후보 전체가 모델 예측 신뢰도에 비해 실질 근거가 매우 취약함을 시사합니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 안전성 고려사항

현재 확보된 안전성 정보가 없습니다. TFDA 허가사항(경고/금기) 및 DrugBank 기전 자료가 모두 미확보 상태(Data Gap, 차단 등급)이므로, 임상 적용을 검토하기 전 별도의 안전성 자료 확보가 반드시 필요합니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 예측 신규 적응증(Familial Visceral Myopathy)에 대한 임상시험·문헌 근거가 전무하여(L5) 모델 예측 점수 외에 검증 가능한 근거가 없습니다.
- 약물 기전(MOA), 허가사항 경고/금기 등 핵심 안전성 데이터가 Blocking 수준의 Data Gap으로 남아 있어 S1 안전성 초평가 단계로도 진입할 수 없습니다.
- 한국 내 미상장 상태로 허가 이력 및 실사용 데이터가 없습니다.

**진행하려면 필요한 것:**
- TFDA(또는 해당국 규제기관) 공식 허가사항 확보 및 경고/금기 파싱 (DG001)
- DrugBank API 등을 통한 작용 기전(MOA) 데이터 확보 (DG002)
- Familial Visceral Myopathy와 Serine 대사 경로 간 기전적 연관성을 뒷받침할 전임상/기전 연구 확보
- 위 자료 없이는 추가 검토를 진행하지 않는 것을 권장합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

