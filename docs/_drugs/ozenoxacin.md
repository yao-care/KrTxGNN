---
layout: default
title: Ozenoxacin
parent: 僅模型預測 (L5)
nav_order: 528
evidence_level: L5
indication_count: 10
---

# Ozenoxacin
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

# Ozenoxacin: [적응증 정보 없음]에서 말라리아로

## 한 문장 요약

Ozenoxacin은 국소 외용 항균제(퀴놀론계)로, 현재 한국에는 시판되지 않은 약물입니다.
TxGNN 모델은 **말라리아(Malaria)**에 효과가 있을 수 있다고 예측했으나,
관련 임상시험이나 문헌 근거는 **전혀 없으며**, 기전상으로도 연관성이 매우 약합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (전신 적응증 데이터 미확보) |
| 예측 신규 적응증 | 말라리아 (Malaria) |
| TxGNN 예측 점수 | 99.16% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미상시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 확보되지 않았습니다. 알려진 정보에 따르면, Ozenoxacin은 퀴놀론계 항균제로 세균의 DNA gyrase/topoisomerase IV를 억제하는 기전을 가진 국소 외용 제형(농가진 치료용) 약물입니다.

일부 구세대 퀴놀론계 약물(예: ciprofloxacin)이 말라리아 원충의 apicoplast DNA 복제를 간접적으로 억제한다는 오래된 관찰이 있으나, 이는 ozenoxacin 특이적 증거가 아니며 약효도 미약한 수준입니다. 또한 ozenoxacin은 전신 흡수를 목적으로 하지 않는 외용 제형이므로, 전신 항말라리아 치료 농도에 도달할 약동학적 근거가 없습니다.

10개 예측 적응증 중 세균 감염과 방향성이 가장 유사한 것은 회귀열(relapsing fever, rank 4)이었으나, 이 역시 전신 스피로헤타 감염에 대한 임상·전임상 근거가 전무합니다. 나머지 예측 적응증(PAPA 증후군, 척추관절병증 감수성, 혈장 아연 상승 등)은 세균 감염과 기전적 연관성이 없어 지식그래프 임베딩상의 노이즈로 판단됩니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

현재 한국에 시판 허가된 제품이 없습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 점수는 높으나(99.16%), 이를 뒷받침할 임상시험·문헌 증거가 전혀 없고(L5), 기전상 연관성도 추정 수준에 그칩니다. 또한 이 약물은 국소 외용 제형으로 전신 감염 질환인 말라리아 치료에 필요한 전신 노출을 달성할 수 없어, 현재 단계에서는 근거 부족으로 진행이 부적절합니다.

**진행하려면 필요한 것:**
- Ozenoxacin의 상세 작용 기전(MOA) 및 항원충 활성 관련 전임상/체외 데이터
- TFDA(또는 관련 규제기관) 허가사항의 경고 및 금기사항 확보 (현재 Blocking 데이터 갭)
- 전신 흡수 가능성 및 약동학 데이터 (외용제 → 전신 적응증 전환 가능성 평가)
- 말라리아 원충에 대한 direct in vitro 활성 시험 결과
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

