---
layout: default
title: Mogamulizumab
parent: 僅模型預測 (L5)
nav_order: 488
evidence_level: L5
indication_count: 7
---

# Mogamulizumab
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

# Mogamulizumab: 성인 T세포 백혈병/림프종에서 전립선 요도 요로상피암으로

## 한 문장 요약

Mogamulizumab은 항CCR4 단클론항체로, 원래 **성인 T세포 백혈병/림프종(ATL)**과 **피부 T세포 림프종(MF/SS)** 치료에 사용됩니다. TxGNN 모델은 **전립선 요도 요로상피암(Prostatic Urethra Urothelial Carcinoma)**에 효과가 있을 수 있다고 예측(점수 99.44%)하지만, 현재 이를 뒷받침하는 **임상시험과 문헌 근거는 전무**합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 성인 T세포 백혈병/림프종(ATL), 피부 T세포 림프종(MF/SS) |
| 예측 신규 적응증 | 전립선 요도 요로상피암 (Prostatic Urethra Urothelial Carcinoma) |
| TxGNN 예측 점수 | 99.44% (rank 9156) |
| 근거 수준 | L5 |
| 대만 시판 현황 | 미출시 (허가증 0건) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

Mogamulizumab의 공식 작용기전(MOA) 필드는 Evidence Pack상 데이터 공백(DG002, High severity)이지만, 예측 근거(rationale) 텍스트에 따르면 이 약물은 **항CCR4 단클론항체**로, CCR4 양성 조절 T세포(Treg)와 악성 CCR4+ T세포를 제거하는 기전을 가지며 ATL 및 피부 T세포 림프종(MF/SS)에 승인되어 있습니다.

전립선 요도 요로상피암은 상피성 고형암으로, 종양 미세환경 내 Treg 침윤은 면역종양학에서 일반적으로 관찰되는 현상입니다. 그러나 이 특정 암종에서 CCR4 발현량이나 Treg 의존도가 mogamulizumab 표적 가설을 뒷받침할 만큼 충분하다는 근거는 없으며, 기전 연관성은 **약함(추론성 외삽)**으로 평가됩니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 대만 시판 정보

대만에 허가된 제품이 없습니다 (미출시, 허가증 0건).

## 세포독성

Mogamulizumab은 백혈병/림프종 적응증을 가진 항종양 생물학적 제제이므로 본 섹션을 포함합니다.

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제/면역치료 (항CCR4 단클론항체 — 고전적 세포독성 화학요법 아님) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
근거 수준이 L5(모델 예측만 존재, 실제 임상시험·문헌 없음)이며, TFDA 안전성 정보(경고·금기·DDI)가 전혀 확보되지 않아(DG001, Blocking) S1 안전성 초기평가조차 진행할 수 없습니다. 기전 연관성도 추론성 외삽 수준으로 평가되어 현 시점에서는 진행이 어렵습니다.

**진행하려면 필요한 것:**
- TFDA 원 라벨(仿單) 확보 및 경고·금기 파싱 (DG001, Blocking)
- DrugBank API를 통한 상세 MOA 데이터 확보 (DG002, High)
- 전립선 요도 요로상피암에서의 CCR4 발현/Treg 침윤 전임상 데이터
- 관련 임상시험·문헌 지속 모니터링 (현재 0건)

> 참고: 이번 Evidence Pack에는 순위 2~7위 후보(신장골반 육종양 이행세포암, 방광 요로상피암 육종양 변이형, 신우 유두상 요로상피암, HHV-8 관련 종양, 외배엽간엽종, 악성 피부 과립세포종양)도 함께 포함되어 있으며, 모두 동일하게 **L5·Hold**로 평가되고 임상시험·문헌 근거가 없습니다. 이 중 HHV-8 관련 종양은 바이러스 잠복기 면역조절과 CCR4+ Treg의 간접적 연관 가설이 상대적으로 합리적이나, 이 역시 검증 데이터는 없습니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

