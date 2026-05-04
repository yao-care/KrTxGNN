---
layout: default
title: Eculizumab
parent: 僅模型預測 (L5)
nav_order: 238
evidence_level: L5
indication_count: 10
---

# Eculizumab
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

# Eculizumab: 발작성 야간 혈색소뇨증(PNH)에서 주기성 조혈증으로

## 한 문장 요약

Eculizumab은 보체 단백질 C5를 선택적으로 억제하는 인간화 단일클론항체로, 전 세계적으로 발작성 야간 혈색소뇨증(PNH)·비정형 용혈성 요독 증후군(aHUS)·중증 근무력증(MG) 등 보체 매개 희귀 혈액 질환 치료에 승인되어 있습니다.
TxGNN 모델은 **주기성 조혈증(Cyclic Hematopoiesis)**에 효과가 있을 수 있다고 예측하나, 현재 이를 지지하는 **임상시험 및 문헌이 전무**합니다.
기전적 연관성도 불명확하여 현재 단계에서는 추가 검증 없이 진행하기 어렵습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | PNH, aHUS (글로벌 승인; 한국 미허가) |
| 예측 신규 적응증 | 주기성 조혈증 (Cyclic Hematopoiesis) |
| TxGNN 예측 점수 | 99.97% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 공식 입력 데이터에서 작용 기전(MOA) 정보가 제공되지 않았으나, 공지된 사실에 따르면 Eculizumab은 보체 단백질 C5에 결합하여 C5a(과립구 활성 유도 인자) 및 C5b-9(막공격복합체, MAC) 생성을 차단하는 IgG2/4κ 인간화 단일클론항체입니다. 이 기전을 통해 비정상적인 보체 과활성화로 인한 적혈구 용해, 혈소판 활성화, 내피세포 손상을 억제합니다.

주기성 조혈증(Cyclic Neutropenia)은 **ELANE 유전자 돌연변이**로 인해 약 21일 주기로 호중구가 급감하는 유전성 조혈 질환입니다. 핵심 병리 기전은 골수 전구세포의 가속화된 세포사멸(apoptosis; unfolded protein response 경로)로, 이는 보체 매개 세포 파괴와는 전혀 다른 경로입니다. C5 억제는 이 주기적 골수 부전의 근본 원인을 교정할 직접적 기전을 갖지 않으며, 표준 치료는 G-CSF입니다.

TxGNN 모델의 높은 예측 점수(99.97%)는 지식 그래프(Knowledge Graph) 내 "혈액 질환(blood disorder)" 노드 간의 위상적 유사성에서 비롯된 것으로 추정되며, 실제 기전적 연관성을 반영하지 않을 가능성이 큽니다. 이는 KG 기반 예측 모델의 알려진 한계로, **해당 예측에 대한 독립적인 기전 검증이 필수**입니다.

---

## 임상시험 근거

현재 주기성 조혈증(Cyclic Hematopoiesis)에 대한 Eculizumab 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 주기성 조혈증(Cyclic Hematopoiesis)에 대한 Eculizumab 관련 문헌이 없습니다.

---

## 한국 시판 정보

한국 식품의약품안전처(MFDS) 등록 허가 기록이 확인되지 않았습니다. Eculizumab은 미국 FDA 및 유럽 EMA에서 PNH·aHUS 등의 적응증으로 승인되어 있으나, 현재 한국 내 시판 허가는 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
주기성 조혈증에 대한 임상시험 및 문헌 근거가 전무하며(근거 수준 L5), Eculizumab의 C5 억제 기전이 ELANE 돌연변이에 의한 주기적 골수 전구세포 세포사멸을 교정할 수 있다는 기전적 근거가 현재 없습니다. TxGNN 예측 점수가 높더라도 지식 그래프 노드 유사성에 따른 위양성(false positive) 가능성이 높은 것으로 판단됩니다.

**참고:** 10개 예측 적응증 중 **4순위 congenital neutropenia-myelofibrosis-nephromegaly syndrome**(L4) 및 **10순위 primary release disorder of platelets**(L4)는 일부 문헌이 확인되어 Research Question 단계로 분류되었습니다. 그러나 해당 문헌들은 대부분 Eculizumab의 기존 적응증(PNH, aHUS) 관련 문헌으로, 예측 질환과의 직접적 관련성은 추가 검토가 필요합니다.

**진행하려면 필요한 것:**
- Eculizumab 공식 작용 기전 데이터 확보 (DrugBank API 조회)
- 한국 MFDS 허가 현황 및 안전성 정보 확인 (TFDA/MFDS 공식 채널)
- 주기성 조혈증에서의 보체 시스템 역할에 관한 전임상 또는 기전 연구 문헌 탐색
- 혈액종양내과 및 희귀 혈액 질환 전문가의 독립적 기전 타당성 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

