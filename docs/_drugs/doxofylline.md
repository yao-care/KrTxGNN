---
layout: default
title: Doxofylline
parent: 僅模型預測 (L5)
nav_order: 232
evidence_level: L5
indication_count: 10
---

# Doxofylline
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

# Doxofylline: 기관지 천식/COPD에서 Pierre Robin 증후군(염색체 이상 동반)으로

## 한 문장 요약

Doxofylline은 메틸잔틴 계열의 기관지 확장제로, 기관지 천식 및 만성 폐쇄성 폐질환(COPD) 치료에 사용되어 왔으며 현재 국내 시판 이력이 없습니다. TxGNN 모델은 **Pierre Robin 증후군(염색체 이상 동반, Pierre Robin syndrome associated with a chromosomal anomaly)**에 효과가 있을 수 있다고 예측(99.54%)하였으나, 현재 이를 뒷받침하는 **임상시험과 관련 문헌이 전무**하여 근거 수준은 L5에 해당합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 기관지 천식, 만성 폐쇄성 폐질환(COPD) (문헌 근거) |
| 예측 신규 적응증 | Pierre Robin 증후군(염색체 이상 동반) |
| TxGNN 예측 점수 | 99.54% |
| 근거 수준 | L5 |
| 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다(MOA Data Gap). 알려진 정보에 따르면, Doxofylline은 메틸잔틴 유도체로 포스포다이에스터라제(PDE) 억제를 통해 기관지 확장 효과를 나타냅니다. 또한 아데노신 수용체를 차단하지 않는(adenosine non-blocking) 특성 덕분에 동일 계열의 테오필린 대비 심혈관계·위장관 부작용이 현저히 적다는 것이 문헌에서 일관되게 보고되고 있습니다(PMID 11268710, PMID 2781149).

Pierre Robin 증후군(염색체 이상 동반)은 소하악증, 설후퇴, 구개열을 특징으로 하는 배아기 안면 발달 이상으로, 선천성 구조적 기형에 해당합니다. Doxofylline의 PDE 억제 및 아데노신 수용체 조절 기전은 하악골 발달이나 Meckel 연골 분화 같은 안면 배아 형태 형성 과정과 알려진 교차점이 없습니다. 기저 원인인 염색체 이상은 유전체 구조 문제로, 소분자 약물이 개입할 수 있는 범주가 아닙니다.

TxGNN 모델의 높은 예측 점수(99.54%)는 지식 그래프(KG) 내 호흡기 질환 노드와 Pierre Robin 증후군의 기도 폐쇄 특성 사이의 위상적 연결로 인한 **위양성 신호(topological artifact)**로 판단됩니다. 실제로 상위 10개 예측 적응증 대부분이 염색체 이상, 선천성 구조 기형, 대사 저장 장애 등 소분자 약물 개입이 원칙적으로 불가능한 질환군으로 구성되어 있어, 이 패턴을 강하게 뒷받침합니다.

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
Pierre Robin 증후군(염색체 이상 동반)은 선천성 구조 기형으로, Doxofylline의 작용 기전과 생물학적 접점이 없으며 임상시험 및 문헌 근거가 전무합니다. TxGNN 예측 점수가 높더라도 기전적 타당성이 없는 L5 수준 예측은 재창출 연구 진행의 근거가 되지 않습니다.

**진행하려면 필요한 것:**
- Doxofylline 상세 MOA 데이터 확보 (DrugBank API 조회, DG002 해소)
- 허가사항 안전성 정보(경고·금기) 확인 (DG001 해소, MFDS 또는 원산지국 허가사항 PDF 파싱)
- 임상적으로 타당성이 있는 예측 적응증에 대한 심층 검토 권고 — 예: 순위 9번 **"heart disease"(L4, Research Question)**: 심부전 합병 저산소혈증 환자에서 메틸잔틴 투여 효과를 다룬 이중맹검 RCT(PMID 8088931)가 존재하며, 아데노신 비차단 특성으로 인한 심장 안전성 우위가 기전적으로 타당하여 추가 근거 수집 가치가 있음

---

> **면책 사항**: 본 보고서는 연구 목적으로만 제공되며, 의료 조언을 구성하지 않습니다. 약물 재창출 후보는 임상 검증을 거쳐야 실제 적용이 가능합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

