---
layout: default
title: Bromocriptine
parent: 僅模型預測 (L5)
nav_order: 153
evidence_level: L5
indication_count: 10
---

# Bromocriptine
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

# Bromocriptine: 파킨슨병/고프로락틴혈증에서 선천성 푸코실화 결함 당질화 장애(CDG)로

---

## 한 문장 요약

Bromocriptine은 도파민 D2/D3 수용체 작용제로, 파킨슨병, 고프로락틴혈증, 말단비대증 및 제2형 당뇨병(Cycloset 제형) 치료에 사용되는 약물입니다.
TxGNN 모델은 **선천성 당질화 결함 장애 - 푸코실화 결함형(Congenital Disorder of Glycosylation with Defective Fucosylation)**에 효과가 있을 수 있다고 예측하였습니다.
현재 이를 뒷받침하는 임상시험과 문헌 근거는 **0건**으로, 순수 모델 예측 단계(L5)에 해당합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 파킨슨병, 고프로락틴혈증 (한국 허가사항 미등록) |
| 예측 신규 적응증 | 선천성 당질화 결함 장애 - 푸코실화 결함형 (CDG with Defective Fucosylation) |
| TxGNN 예측 점수 | 99.83% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 이 Evidence Pack에 상세한 작용 기전 데이터가 포함되어 있지 않습니다. 알려진 정보에 따르면 Bromocriptine은 도파민 D2/D3 수용체를 직접 자극하는 작용제로서, 중추신경계의 도파민 신호를 증강시키고 시상하부-뇌하수체 축에서 프로락틴 분비를 억제합니다. 부가적으로 세로토닌 5-HT2C 수용체 및 알파 아드레날린 수용체와의 상호작용도 보고되어 있으며, Cycloset 제형의 경우 일주기 리듬(circadian rhythm)을 통한 인슐린 감수성 개선 기전도 확인되어 있습니다.

선천성 당질화 결함 장애(CDG)는 단백질 또는 지질의 당질화(glycosylation) 과정에 관여하는 효소의 유전적 결함으로 발생하는 희귀 선천성 대사 질환군입니다. 이 중 **푸코실화 결함형**은 GDP-fucose 생합성 또는 골지체 내 GDP-fucose 수송 경로의 이상으로 인해 발생하며, SLC35C1 등 관련 유전자 돌연변이가 원인으로 알려져 있습니다. 현재까지 표준 치료제가 없는 미충족 의료 수요가 높은 영역입니다.

TxGNN 모델이 이 연결을 예측한 이론적 근거는 다음과 같습니다: 도파민 D2R 활성화 → cAMP 하향 조절 → PKA 경로 조절 → 골지체 소포 운반 기능에 간접 영향 → 이론적으로 푸코실전이효소(fucosyltransferase) 활성 조절 가능성. 그러나 이 기전적 연결고리는 **고도로 추측적**이며, Bromocriptine이 CDG 푸코실화 결함형에 효과를 보인다는 직접적인 세포 실험 또는 임상 데이터는 현재 전혀 존재하지 않습니다.

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
선천성 당질화 결함 장애 - 푸코실화 결함형에 대한 Bromocriptine의 효능을 지지하는 임상시험이나 문헌 근거가 전혀 없으며, 도파민 D2R 신호와 푸코실화 경로 간 기전적 연결고리도 간접적이고 추측적인 수준에 불과합니다. L5 수준의 모델 예측만으로는 개발 진행을 정당화하기 어렵습니다.

**진행하려면 필요한 것:**
- Bromocriptine 상세 작용 기전 데이터 (DrugBank DB11901 조회 권고)
- 한국 MFDS 허가사항 및 안전성 정보 확인 (경고, 금기, DDI 포함)
- 전임상 탐색 연구: 도파민 D2R 신호 활성화가 GDP-fucose 합성·수송 경로에 미치는 영향 평가
- CDG 환자 유래 세포 모델(섬유아세포)에서의 Bromocriptine 표현형 회복 시험
- 희귀 대사 질환 전문가 자문을 통한 기전 타당성 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

