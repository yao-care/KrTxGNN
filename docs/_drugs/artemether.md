---
layout: default
title: Artemether
parent: 僅模型預測 (L5)
nav_order: 88
evidence_level: L5
indication_count: 10
---

# Artemether
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

# Artemether: 말라리아에서 후천성 혈관부종으로

## 한 문장 요약

Artemether는 WHO 필수 의약품 목록에 등재된 청호소(artemisinin) 유도체로, 전 세계 90개국 이상에서 artemether-lumefantrine 복합제(Coartem®)의 핵심 성분으로서 *Plasmodium falciparum* 말라리아 치료에 사용되고 있습니다.
TxGNN 모델은 **후천성 혈관부종(Acquired Angioedema)**에 효과가 있을 수 있다고 예측하나,
현재 이를 지지하는 **임상시험 및 문헌이 전무**하여 모델 예측만 존재하는 L5 근거 수준에 해당합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 말라리아 (글로벌 허가; 한국 미등록) |
| 예측 신규 적응증 | 후천성 혈관부종 (Acquired Angioedema) |
| TxGNN 예측 점수 | 99.90% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Artemether는 과산화 결합(endoperoxide bridge)을 내포한 세스퀴테르펜 락톤 계열 약물로, 말라리아 원충의 식포(food vacuole) 내 혈철소(heme)와 반응해 활성 자유라디칼을 생성합니다. 이 자유라디칼이 원충의 PfATP6 칼슘 펌프와 단백질 기능을 파괴하여 *P. falciparum*을 신속히 사멸시키는 기전은 충분히 검증되어 있습니다.

후천성 혈관부종과의 기전적 연결은 고도로 간접적입니다. 청호소 계열 약물이 NF-κB 억제 및 TGF-β 조절을 포함한 광범위한 면역조절 특성을 보인다는 보고가 있어, 이론적으로 보체계(complement system)에 영향을 줄 가능성이 제기됩니다. 후천성 혈관부종의 주요 병태생리는 C1-INH 결핍 또는 B세포 림프종에 의한 보체 과활성화인데, Artemether가 이 경로에 직접 작용한다는 전임상 데이터는 현재 존재하지 않습니다.

결론적으로, 이 예측은 지식 그래프 내 면역/보체 관련 노드들의 연결 패턴에서 비롯된 신호로 추정됩니다. TxGNN 점수(99.90%)가 높게 나타난 것은 그래프 위상 구조에 의한 것이며, 실제 임상 효능을 직접 시사하지는 않습니다. 기전적 타당성 확인을 위한 전임상 연구가 먼저 선행되어야 합니다.

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
후천성 혈관부종에 대한 임상시험 및 문헌 근거가 전혀 없으며, 기전적 연결도 간접적 추론에 그칩니다. L5 수준(모델 예측만 존재)에 해당하므로 현 단계에서 추가 자원 투자는 권장하지 않습니다.

**진행하려면 필요한 것:**
- C1-INH 경로 또는 보체계에 대한 Artemether의 체외(in vitro) 실험 데이터
- 기전적 타당성을 검증하는 전임상 연구 (동물 모델 포함)
- 작용 기전(MOA) 상세 정보 확보 (현재 Data Gap 존재)
- 한국 허가사항 및 안전성 정보(仿單) 확보
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

