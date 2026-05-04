---
layout: default
title: Glycol Salicylate
parent: 僅模型預測 (L5)
nav_order: 278
evidence_level: L5
indication_count: 10
---

# Glycol Salicylate
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

Evidence Pack 분석 완료. 아래는 완성된 평가 보고서입니다.

---

# Glycol Salicylate: 국소 진통·항염 (외용)에서 Glanzmann 혈소판무력증으로

## 한 문장 요약

Glycol salicylate는 수양산(salicylic acid) 글라이콜 에스터 유도체로, 외용 진통·항염제로서 근골격계 통증 완화에 사용됩니다.
TxGNN 모델은 **Glanzmann 혈소판무력증(Glanzmann thrombasthenia)**에 효과가 있을 수 있다고 예측하였으나,
이를 지지하는 임상시험 및 문헌이 **전혀 없으며**, 기전 분석상 예측 방향성에 심각한 임상적 우려가 있습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 없음 (한국 미상市) |
| 예측 신규 적응증 | Glanzmann 혈소판무력증 (Glanzmann thrombasthenia) |
| TxGNN 예측 점수 | 98.17% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미상市 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 Glycol salicylate의 상세 작용 기전 데이터(MOA)가 확보되어 있지 않습니다. 약물 계열 기반으로 추정하면, glycol salicylate는 COX-1 억제를 통해 트롬복산 A2(TXA2) 합성을 억제하고 혈소판 응집 반응에 영향을 미치는 것으로 알려져 있습니다. 외용 제형으로 사용 시 전신 흡수는 제한적입니다.

TxGNN이 이 예측을 생성한 배경은 수양산계 약물과 혈소판 기능 사이의 지식 그래프 연결에 기인한 것으로 보입니다. **그러나 이 예측은 치료 방향이 잘못 판단되었을 가능성이 매우 높습니다.** Glanzmann 혈소판무력증은 GPIIb/IIIa 수용체 결핍으로 인한 출혈성 질환입니다. 여기에 수양산계 약물의 COX-1 억제를 추가하면, TXA2 매개 혈소판 응집이 더욱 억제되어 출혈 위험을 치료하는 것이 아니라 **악화**시킬 수 있습니다. 모델이 "혈소판 기능에 영향을 미치는 약물"과 "혈소판 질환 치료제"를 혼동하여 관계 방향성을 오판했을 가능성이 높습니다.

**참고 (2순위 예측)**: 예측 2순위인 **자가면역 질환(Autoimmune disease, TxGNN 점수: 98.16%)**에 대해서는 COX 억제를 통한 PGE2/PGI2 감소로 항염 효과를 기대할 수 있다는 기전적 근거가 있으며, 1편의 임상 문헌(독일어, 류마티스성 요통 이중맹검 시험)도 확인됩니다. 1순위 예측에 비해 임상적 타당성이 상대적으로 높습니다.

---

## 임상시험 근거

현재 Glanzmann 혈소판무력증과 관련된 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 Glanzmann 혈소판무력증과 관련된 문헌이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
근거가 전혀 없는 L5 수준이며(임상시험 0건, 문헌 0편), 기전 분석상 수양산계 약물이 Glanzmann 혈소판무력증을 치료하는 것이 아니라 출혈 위험을 가중시킬 가능성이 높아 임상적으로 부적절한 예측으로 판단됩니다.

**진행하려면 필요한 것:**
- Glycol salicylate의 정확한 작용 기전 데이터(MOA) 확보 (DrugBank API 쿼리)
- 한국 MFDS 허가 현황 및 허가사항(경고·금기) 확인
- TxGNN 예측의 관계 방향성 오류 여부에 대한 추가 검토 (지식 그래프 엣지 방향 검증)
- 2순위 적응증(자가면역 질환)에 대한 추가 근거 탐색 및 별도 보고서 작성 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

