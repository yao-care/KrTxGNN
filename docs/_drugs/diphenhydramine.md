---
layout: default
title: Diphenhydramine
parent: 僅模型預測 (L5)
nav_order: 224
evidence_level: L5
indication_count: 1
---

# Diphenhydramine
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

# Diphenhydramine: 알레르기에서 주사성 결막염으로

## 한 문장 요약

Diphenhydramine은 제1세대 H1 수용체 길항제(항히스타민제)로, 알레르기·수면장애 등의 치료에 오랫동안 사용되어 온 약물입니다.
TxGNN 모델은 **주사성 결막염(Rosacea Conjunctivitis)**에 효과가 있을 수 있다고 예측하나,
현재 이 예측을 직접 지지하는 **임상시험 및 문헌은 존재하지 않습니다**.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 미기재 (제1세대 항히스타민제로 알려짐) |
| 예측 신규 적응증 | 주사성 결막염 (Rosacea Conjunctivitis) |
| TxGNN 예측 점수 | 99.20% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Diphenhydramine은 H1 수용체를 차단하는 제1세대 항히스타민제입니다. 주사성 결막염의 주요 병생리 중 하나는 비만세포(mast cell) 탈과립에 의한 조직아민(히스타민) 방출로, H1 수용체 차단이 결막의 혈관 확장과 염증 반응을 이론적으로 억제할 수 있다는 점에서 생물학적 타당성이 있습니다. TxGNN이 높은 점수(0.992)를 부여한 배경도 이 염증 경로 네트워크 상의 구조적 근접성에서 비롯된 것으로 추정됩니다.

그러나 Diphenhydramine의 항콜린성(anticholinergic) 부작용은 이 적응증에 있어 주요 반대 기전으로 작용할 수 있습니다. 항콜린 효과는 눈물 분비 및 마이봄샘 분비를 억제하여 건성안 증상을 악화시킬 가능성이 있으며, 이는 주사성 안병증(ocular rosacea)의 핵심 증상인 건성안과 직접 상충됩니다.

종합적으로, 히스타민 경로를 통한 기전 연결고리에는 생물학적 합리성이 있으나, 항콜린 부작용이 오히려 병생리를 악화시킬 수 있는 상충 기전이 존재합니다. 순효과(net benefit)를 검증한 임상 연구는 현재 없으며, 모델 예측만으로 효능을 단정하기 어렵습니다.

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
근거 수준이 L5(TxGNN 모델 예측만 존재)이며, 주사성 결막염에 대한 Diphenhydramine의 효능을 직접 지지하는 임상시험 또는 문헌이 전혀 없습니다. 더불어 항콜린 부작용이 해당 적응증의 병생리를 악화시킬 수 있는 상충 기전이 확인되어, 추가 근거 없이 진행은 부적절합니다.

**진행하려면 필요한 것:**
- 주사성 결막염 동물 모델 또는 세포 실험(전임상) 데이터
- Diphenhydramine 안점안 제형의 안전성 및 건성안 영향 평가
- 항히스타민제 계열의 주사성 결막염 관련 문헌 검토 (2세대 항히스타민제 비교 포함)
- TFDA/MFDS 허가사항 및 경고·금기 원문 확보
- MOA 상세 데이터 보강 (DrugBank API 조회)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

