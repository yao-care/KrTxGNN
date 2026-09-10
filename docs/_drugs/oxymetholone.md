---
layout: default
title: Oxymetholone
parent: 僅模型預測 (L5)
nav_order: 527
evidence_level: L5
indication_count: 1
---

# Oxymetholone
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

# Oxymetholone: 적응증 미상에서 지루성 피부염으로

## 한 문장 요약

Oxymetholone은 합성 남성호르몬(안드로겐 아나볼릭 스테로이드) 계열 약물로, 현재 한국 내 허가 및 시판 이력이 없습니다. TxGNN 모델은 **지루성 피부염(Seborrheic Dermatitis)**에 효과가 있을 수 있다고 예측했으나(예측 점수 99.05%), 이를 지지하는 **임상시험이나 문헌 근거는 전혀 없으며**, 오히려 기전상 반대 방향(악화 요인)일 가능성이 높습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | 지루성 피부염 (Seborrheic Dermatitis) |
| TxGNN 예측 점수 | 99.05% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미상시 (허가 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 확보되지 않았으나(MOA: Data Gap), Oxymetholone은 합성 남성호르몬(androgenic anabolic steroid, AAS) 계열로, 안드로겐 수용체를 활성화하는 약물로 알려져 있습니다.

그러나 이번 예측은 기전상 타당성이 낮습니다. 안드로겐은 피지선 증식과 피지 분비를 촉진하는 것으로 알려져 있으며, AAS 사용자에서 여드름(acne)과 지루(seborrhea)가 흔한 부작용으로 보고됩니다. 이는 지루성 피부염의 병태생리와 **반대 방향**으로 작용합니다 — 안드로겐은 치료제가 아니라 악화/유발 인자로 알려져 있습니다.

TxGNN의 높은 점수(0.99)는 지식 그래프 내 "안드로겐-피지선-피부질환" 노드 간의 연관 강도를 반영한 것으로 추정되나, 이는 **치료적 관계와 병인적 관계를 구분하지 못한** 결과로 판단됩니다. 현재로서는 이 예측을 뒷받침하는 기전적 근거가 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

현재 한국 내 허가 및 시판 이력이 없습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
지지하는 임상시험이나 문헌 근거가 전무하며(L5), 기전상으로도 안드로겐이 지루성 피부염을 악화시킬 가능성이 높아 예측 방향성 자체에 의문이 있습니다. 현재 단계에서 추가 검토나 자원 투입을 권장하지 않습니다.

**진행하려면 필요한 것:**
- 상세 작용 기전(MOA) 데이터 확보
- TFDA 수준의 안전성 경고 및 금기사항 확보 (현재 Blocking 데이터 갭)
- 지루성 피부염에서 안드로겐 관련 실제 임상/전임상 근거 확인
- TxGNN 예측의 방향성(치료 vs. 악화) 재검증
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

