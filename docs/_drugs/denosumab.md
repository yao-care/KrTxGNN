---
layout: default
title: Denosumab
parent: 僅模型預測 (L5)
nav_order: 204
evidence_level: L5
indication_count: 2
---

# Denosumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Denosumab: 골다공증/골 전이에서 중증 비증식성 당뇨병성 망막증으로

## 한 문장 요약

Denosumab은 RANKL(핵인자-κB 수용체 활성화 리간드)을 표적으로 하는 완전 인간 단클론항체로, 골다공증 및 골 전이에 의한 골격 관련 합병증 예방에 사용되어 온 약물입니다. TxGNN 모델은 **중증 비증식성 당뇨병성 망막증(Severe Nonproliferative Diabetic Retinopathy)**에 효과가 있을 수 있다고 예측하며 예측 점수는 99.63%입니다. 그러나 현재 이 특정 적응증을 직접 지지하는 임상시험이나 문헌은 전혀 확인되지 않았습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 골다공증, 골 전이 관련 골격 합병증 예방 |
| 예측 신규 적응증 | 중증 비증식성 당뇨병성 망막증 (Severe Nonproliferative Diabetic Retinopathy) |
| TxGNN 예측 점수 | 99.63% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 본 Evidence Pack에 Denosumab의 상세 작용 기전(MOA) 데이터가 포함되어 있지 않습니다. 알려진 정보에 따르면, Denosumab은 RANKL에 특이적으로 결합하여 RANK-RANKL 신호전달을 차단함으로써 파골세포 활성화를 억제하며, 이를 통해 골 흡수를 감소시킵니다.

RANKL/RANK/OPG(오스테오프로테게린) 신호 축은 뼈 대사 이외에도 혈관 세포, 특히 망막 주위세포(pericyte)의 생존 조절에 잠재적 역할을 한다는 가설이 있습니다. 당뇨병 환경에서 OPG/RANKL 비율이 변화하면 망막 미세혈관의 주위세포 소실이 가속화되어 비증식성 당뇨병성 망막증의 병리 기전을 촉진할 수 있다는 것입니다. 또한 RANKL이 VEGF 발현을 상향 조절한다는 연구가 있어, Denosumab이 이 경로를 차단함으로써 비정상적 혈관 생성 구동력을 간접적으로 낮출 가능성도 제기됩니다.

다만 이러한 기전적 연결고리는 현재까지 순수한 가설 수준에 머물러 있습니다. 중증 비증식성 당뇨병성 망막증을 직접 대상으로 한 전임상 연구나 임상시험이 전무하여, TxGNN의 높은 예측 점수는 지식 그래프 내 경로 연관성을 반영하는 것으로 해석해야 하며 실제 치료 효과의 증거로 간주해서는 안 됩니다.

---

## 임상시험 근거

현재 중증 비증식성 당뇨병성 망막증에 관련된 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 중증 비증식성 당뇨병성 망막증에 관련된 문헌이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
중증 비증식성 당뇨병성 망막증에 대한 직접적인 임상시험 또는 문헌 근거가 전혀 없는 L5 수준으로, RANKL 신호와 망막 주위세포의 연관성은 기전 가설 단계에 그치고 있어 당장 개발 투자를 진행하기에는 근거가 불충분합니다.

**진행하려면 필요한 것:**
- Denosumab 공식 MOA 및 DrugBank 카테고리 데이터 확보 (DrugBank API 조회)
- RANKL/RANK 신호와 망막 주위세포 생존의 연관성을 검토한 전임상(세포·동물 모델) 연구 탐색
- 당뇨병성 망막증 동물 모델에서의 Denosumab 효능 실험
- 한국 허가 현황 확인 (MFDS 조회)
- 안전성 프로파일 확보 (허가사항 PDF 파싱 및 경고·금기 정리)
- 참고: 인접 적응증인 당뇨병성 망막증(Rank 2, L4)에는 간접 임상시험 1건 및 관련 문헌 2편이 존재하므로, 해당 범위로 탐색 범위를 확장하면 가설 검증의 출발점을 마련할 수 있습니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

