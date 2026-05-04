---
layout: default
title: Rufinamide
parent: 僅模型預測 (L5)
nav_order: 297
evidence_level: L5
indication_count: 5
---

# Rufinamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Rufinamide: Lennox-Gastaut 증후군에서 발열 감염 관련 뇌전증 증후군으로

## 한 문장 요약

Rufinamide는 전압 개폐 나트륨 채널 조절제로, 전 세계적으로 **Lennox-Gastaut 증후군(LGS)** 보조 치료에 허가된 항경련제입니다.
TxGNN 모델은 **발열 감염 관련 뇌전증 증후군(FIRES, Febrile Infection-Related Epilepsy Syndrome)**에 효과가 있을 수 있다고 예측하나,
현재 이를 지지하는 **임상시험 및 문헌 근거가 전무**하여 순수 모델 추론 단계에 머물러 있습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | Lennox-Gastaut 증후군 (LGS) 보조 치료 |
| 예측 신규 적응증 | 발열 감염 관련 뇌전증 증후군 (FIRES) |
| TxGNN 예측 점수 | 99.57% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미허가 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 확보되지 않았습니다. 알려진 정보에 따르면 Rufinamide는 전압 개폐 나트륨 채널(Nav1.x)의 불활성화 상태를 연장하여 신경세포의 고빈도 반복 방전을 억제합니다. 이 기전은 다양한 발작 유형을 동반하는 난치성 뇌전증, 특히 LGS의 추락 발작(atonic seizure) 억제에 효과적인 것으로 입증되어 있습니다.

FIRES는 감염 발생 후 수일 이내 초난치성 뇌전증 지속 상태(super-refractory status epilepticus)로 진행하는 증후군으로, 현재 표준 항경련 치료에 반응하지 않는 경우가 많아 대안 약물에 대한 미충족 의학적 수요가 큽니다. 나트륨 채널 조절제는 이론적으로 FIRES의 과도한 피질 방전을 억제할 수 있는 약리학적 근거를 가지며, FIRES 회복 이후 LGS와 유사한 후유 뇌전증이 발생하는 임상 사례가 보고되어 있어 두 질환 사이에는 임상적 연속성이 존재합니다. TxGNN 지식 그래프는 이러한 질환 분류학적 근접성을 반영하여 최고점(0.9957)을 부여했습니다.

다만 중요한 한계가 있습니다. FIRES의 발병 기전은 나트륨 채널 이상보다 염증 매개 경로가 더 핵심적인 역할을 하는 것으로 알려져 있어, 나트륨 채널 조절만으로는 충분한 치료 효과를 기대하기 어려울 수 있습니다. 현재 이 예측을 직접 지지하는 임상시험 또는 문헌이 전혀 존재하지 않으므로, 전임상 단계부터 체계적 검증이 선행되어야 합니다.

---

## 임상시험 근거

현재 Rufinamide와 발열 감염 관련 뇌전증 증후군(FIRES)에 관한 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 Rufinamide와 발열 감염 관련 뇌전증 증후군(FIRES)에 관한 관련 문헌이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
임상시험·문헌 근거가 전혀 없고 약물 상호작용(DDI) 및 안전성 경고 데이터도 확보되지 않은 상태로, TxGNN 모델 예측 단독으로는 임상 개발 진행 여부를 결정할 수 없습니다.

**진행하려면 필요한 것:**
- FIRES 동물 모델 또는 in vitro 시스템에서 나트륨 채널 조절제의 효과를 검증하는 전임상 연구 확보
- Rufinamide 작용 기전(MOA) 상세 데이터 수집 (DrugBank API 조회)
- MFDS(식품의약품안전처) 허가 정보 및 안전성 경고·금기사항 수집
- 약물 상호작용(DDI) 데이터 보완 (특히 항경련제 병용 시)
- 한국 내 약물 접근성 경로 확인 (현재 미허가 품목)
- FIRES 대상 나트륨 채널 조절제 계열 전반의 사례 보고(case report) 문헌 심층 탐색
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

