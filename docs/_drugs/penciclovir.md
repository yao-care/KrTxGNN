---
layout: default
title: Penciclovir
parent: 僅模型預測 (L5)
nav_order: 541
evidence_level: L5
indication_count: 10
---

# Penciclovir
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

# Penciclovir: 헤르페스 감염에서 신규 적응증(불명확)으로

## 한 문장 요약

Penciclovir는 항헤르페스바이러스 약물로 알려져 있으나, 한국 내 허가 정보와 작용 기전 데이터가 확보되지 않았습니다. TxGNN 모델은 fascioliasis(간질충증) 등 여러 기생충/종양 질환에 대해 통계적으로 높은 예측 점수를 부여했지만, 이를 뒷받침하는 임상시험이나 문헌은 **전혀 없으며**, 기전적으로도 타당성이 낮습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인되지 않음 (Data Gap) |
| 예측 신규 적응증 | Fascioliasis (간질충증) |
| TxGNN 예측 점수 | 99.06% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미상시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 확보되지 않았습니다. 다만 Penciclovir는 구아노신 유사체로서 헤르페스바이러스(HSV/VZV)의 타이미딘 키나아제에 의해 인산화된 후 바이러스 DNA 중합효소를 억제하는 항바이러스제로 알려져 있습니다.

이 기전은 흡충류(Fasciola), 조충류(Taenia), 장내 기생충, 악성 중피종 등 예측된 적응증들과 생물학적 연관성이 없습니다. TxGNN 예측 근거(`repurposing_rationale`)에서도 상위 10개 예측 모두 "기전상 연관성 없음", "순수 지식그래프 통계적 관련성"이라고 명시하고 있어, 이번 예측 세트는 기전 가설 없이 모델 점수만 존재하는 사례입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

한국 내 허가 제품이 없습니다 (미상시, 허가증 0건).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측된 10개 적응증 전부가 evidence_level L5(모델 예측만 존재, 임상/문헌 근거 없음)이며, 자체 기전 분석에서도 생물학적 타당성이 없다고 명시되어 있습니다. 원래 적응증, MOA, 한국 허가 정보, 안전성 정보까지 모두 Data Gap 상태로 S1 안전성 초평가조차 진행할 수 없습니다.

**진행하려면 필요한 것:**
- DrugBank API를 통한 Penciclovir의 정확한 기존 적응증 및 MOA 확보 (DG002)
- 한국 내 허가 여부 및 시판 현황 재확인
- 허가사항(경고/금기) 확보 (DG001, Blocking) — 이것이 해결되기 전까지는 어떤 신규 적응증도 안전성 검토 불가
- 예측된 적응증에 대한 최소한의 전임상/기전 연구 존재 여부 확인 후 재평가
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

