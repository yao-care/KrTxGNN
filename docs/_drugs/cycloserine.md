---
layout: default
title: Cycloserine
parent: 僅模型預測 (L5)
nav_order: 227
evidence_level: L5
indication_count: 7
---

# Cycloserine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Cycloserine: 기존 적응증 정보 없음에서 과민성대장증후군(예측)으로

## 한 문장 요약

Cycloserine(DrugBank ID: DB00260)은 한국에 시판 중인 허가 제품이 없으며, 근거팩에도 기존 승인 적응증 정보가 등재되어 있지 않습니다.
TxGNN 모델은 **과민성대장증후군(Irritable Bowel Syndrome)**에 효과가 있을 수 있다고 예측(점수 99.95%)하지만,
현재 이를 뒷받침하는 **임상시험이나 문헌은 전무**하여 모델 예측 외에는 근거가 없는 상태입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (근거팩 미등재) |
| 예측 신규 적응증 | 과민성대장증후군 (Irritable Bowel Syndrome) |
| TxGNN 예측 점수 | 99.95% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미판매 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 없습니다(Data Gap, 심각도: High). 근거팩에는 Cycloserine의 기존 승인 적응증도 기재되어 있지 않아, 기존 적응증과 과민성대장증후군 사이의 기전적 연관성을 판단할 근거가 없습니다.

이 예측에 대한 기전적 근거는 "TxGNN 지식그래프 예측 점수가 높다"는 것 외에는 존재하지 않으며, 임상시험이나 문헌 등 실제 연구 근거도 전혀 없습니다. 따라서 이 예측은 순수 모델 기반 가설 단계(L5)에 머물러 있습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

현재 한국에 시판 중인 제품이 없습니다(허가증 0건, 시판 상태: 미판매).

## 안전성 고려사항

안전성 정보(주요 경고, 금기, 약물 상호작용)가 근거팩에 등재되어 있지 않습니다(DDI 조회 결과: not_found). 원개발국 규제기관의 첨부문서 확인이 필요합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측된 신규 적응증(과민성대장증후군)을 뒷받침하는 임상시험이나 문헌이 전혀 없고, 약물의 작용기전(MOA)조차 데이터 갭 상태입니다. 또한 안전성 정보(경고·금기·DDI)가 모두 결측이라 S1 안전성 초평가 단계로 진입할 수 없는 Blocking 데이터 갭(DG001)이 존재합니다.

**진행하려면 필요한 것:**
- 규제기관 원문 첨부문서(경고·금기·DDI) 확보 — Blocking
- DrugBank API를 통한 정확한 작용기전(MOA) 데이터 확보 — High
- 과민성대장증후군에 대한 전임상 또는 기전 연구 근거 축적
- 참고: 같은 근거팩 내 불면증(L3, NCT03395392 등 3건)과 결막염(L4, 문헌 3편)은 상대적으로 근거가 더 있으나, 불면증의 경우 Cycloserine이 오히려 불면증을 부작용으로 유발한다는 문헌(PMID 36712725)이 있어 예측 방향과 상충되므로 별도 정밀 검토가 필요합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

