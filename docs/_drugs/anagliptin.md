---
layout: default
title: Anagliptin
parent: 僅模型預測 (L5)
nav_order: 71
evidence_level: L5
indication_count: 8
---

# Anagliptin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Anagliptin: 2형 당뇨병에서 Opsismodysplasia로

## 한 문장 요약

Anagliptin은 DPP-4(dipeptidyl peptidase-4) 억제제 계열의 경구용 혈당강하제로, 원래 2형 당뇨병 치료에 사용됩니다.
TxGNN 모델은 **Opsismodysplasia**에 효과가 있을 수 있다고 예측하나,
이를 뒷받침하는 **임상시험 및 문헌이 전무**하여 현재 모델 예측만 존재하는 상태입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 2형 당뇨병 (DPP-4 억제제, 일본 허가) |
| 예측 신규 적응증 | Opsismodysplasia |
| TxGNN 예측 점수 | 99.43% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, Anagliptin은 DPP-4 억제제 계열에 속하며 인크레틴 호르몬(GLP-1, GIP)의 분해를 차단해 혈당 조절 효과를 나타냅니다. 일본에서 2형 당뇨병 치료제로 허가된 약물이지만, 한국에는 현재 시판 허가가 없습니다.

Opsismodysplasia는 INPPL1(SHIP2 인산화효소) 기능 상실 돌연변이에 의해 발생하는 희귀 골격 이형성증입니다. 주요 병리 기전은 PI3K/Akt 신호 경로의 이상 조절과 연골세포 발달 장애입니다. DPP-4 억제제는 이론상 DPP-4가 분해하는 일부 성장인자 조절 펩타이드(IGF-1 관련 인자 등)에 영향을 줄 수 있으나, 이 경로는 SHIP2→PI3K 축과 직접적인 연결 고리가 없습니다.

기전적 연관성은 극히 미약합니다. Opsismodysplasia는 단일 유전자 기반의 골격 발달 질환으로, DPP-4 억제를 통한 합리적인 개입 경로가 현재로서는 확인되지 않습니다. 이번 TxGNN 예측은 지식 그래프 내 간접적인 노드 연결에서 비롯된 것으로 보이며, 생물학적 타당성 측면의 추가 검토가 필요합니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 한국 시판 정보

Anagliptin은 현재 한국에 허가된 제품이 없습니다 (허가증 0건, 미시판).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
Opsismodysplasia와 DPP-4 억제제 간의 기전적 연결이 극히 약하며, 이를 뒷받침하는 임상시험이나 문헌 근거가 전혀 존재하지 않습니다. 현재 TxGNN 모델 예측만 존재하는 L5 수준의 근거로는 추가 개발 진행이 어렵습니다.

**진행하려면 필요한 것:**
- Anagliptin의 상세 작용 기전 데이터(MOA) 확보 — DrugBank API 조회 권장
- 허가사항 기반 안전성 정보(경고, 금기) 확보
- SHIP2/PI3K 경로와 DPP-4 억제 간 기전 연관성에 대한 전임상 근거 생성
- Opsismodysplasia 세포 또는 동물 모델에서의 탐색적 실험 설계 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

