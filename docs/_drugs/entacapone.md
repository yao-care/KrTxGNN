---
layout: default
title: Entacapone
parent: 僅模型預測 (L5)
nav_order: 246
evidence_level: L5
indication_count: 10
---

# Entacapone
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

# ENTACAPONE: 파킨슨병에서 PLA2G6 관련 신경퇴행으로

---

## 한 문장 요약

ENTACAPONE은 COMT(카테콜-O-메틸트랜스퍼라제) 억제제로, 해외에서 파킨슨병 환자의 levodopa 병용 보조치료에 허가된 약물입니다.
TxGNN 모델은 **PLA2G6 관련 신경퇴행(PLA2G6-associated neurodegeneration)**에 효과가 있을 수 있다고 예측하나,
현재 이 예측을 지지하는 **임상시험이나 관련 문헌이 전혀 없습니다**.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 파킨슨병 보조치료 (levodopa 병용, 해외 허가) |
| 예측 신규 적응증 | PLA2G6 관련 신경퇴행 (PLA2G6-associated neurodegeneration) |
| TxGNN 예측 점수 | 99.76% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 제공되지 않았습니다. 알려진 정보에 따르면, ENTACAPONE은 COMT를 억제하여 levodopa의 말초 대사를 차단하고, 뇌로 전달되는 levodopa 양을 증가시켜 도파민 가용성을 높이는 방식으로 파킨슨병의 "on-off" 변동을 개선합니다.

PLA2G6 관련 신경퇴행(PLAN, NBIA2)은 PLA2G6 유전자 돌연변이에 의해 발생하는 희귀 신경퇴행 질환으로, 뇌철 침착 신경퇴행증(NBIA)의 한 유형입니다. 일부 환자는 후기 단계에서 도파민 신경세포 손상이 동반될 수 있어, 이론적으로 COMT 억제와 간접적 연관성이 존재할 수 있습니다.

그러나 이 연결 고리는 매우 취약합니다. PLAN의 핵심 병리는 인지질 대사 이상으로 인한 축삭 구형체(axonal spheroids) 형성과 세포막 리모델링 장애이며, 도파민 신경세포 손상은 이차적 현상에 불과합니다. 현재까지 ENTACAPONE의 PLAN에 대한 전임상 또는 임상 연구가 전혀 존재하지 않으며, TxGNN의 높은 예측 점수는 지식 그래프 내 신경퇴행 질환 노드 간의 위상학적 유사성에서 비롯된 것으로 해석됩니다.

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
PLA2G6 관련 신경퇴행에 대한 ENTACAPONE의 효능을 지지하는 임상시험 및 문헌이 전무하며, 기전 연관성도 이론적 추론 수준에 그칩니다. 한국 내 미시판 약물로 규제 경로 수립도 선행되어야 합니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 상세 데이터 확보 (DrugBank API 조회)
- 안전성 정보 확보 (경고, 금기사항, 약물 상호작용)
- PLAN 전임상 모델(세포 또는 동물)에서 COMT 억제 효과 평가 기초 연구
- 한국 내 규제 허가 경로 및 시판 가능성 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

