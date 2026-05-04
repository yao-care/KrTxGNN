---
layout: default
title: Bacampicillin
parent: 僅模型預測 (L5)
nav_order: 116
evidence_level: L5
indication_count: 10
---

# Bacampicillin
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

# Bacampicillin: 세균성 감염에서 후두개염 (Epiglottitis)으로

## 한 문장 요약

Bacampicillin은 Ampicillin의 경구 전구약물(prodrug)로, β-lactam 계열 광범위 항생제입니다.
TxGNN 모델은 **후두개염(Epiglottitis)**에 효과가 있을 수 있다고 예측하며,
기전적 연관성은 성립하나 이를 직접 지지하는 임상시험이나 문헌은 현재 확인되지 않습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 세균성 감염 (등록 허가 정보 없음) |
| 예측 신규 적응증 | 후두개염 (Epiglottitis) |
| TxGNN 예측 점수 | 99.92% |
| 근거 수준 | L4 |
| 시판 현황 | ✗ 미등록 |
| 허가증 수 | 0건 |
| 권장 결정 | Research Question |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 확인되지 않았습니다. 알려진 정보에 따르면, Bacampicillin은 Ampicillin의 경구 전구약물로, 위장관에서 흡수된 후 혈중에서 활성 약물인 Ampicillin으로 전환됩니다. Ampicillin은 세균 세포벽 합성에 필수적인 페니실린 결합 단백질(PBP)에 결합하여 살균 작용을 발휘합니다.

후두개염은 주로 *Haemophilus influenzae* type b(Hib) 또는 *Streptococcus* 속 균에 의해 발생하는 급성 상기도 염증으로, 기도 폐쇄를 초래할 수 있는 응급 질환입니다. Ampicillin은 이들 병원체에 대한 항균 활성을 보유하고 있어, 기전상 적용 가능성이 존재합니다.

다만 현대 임상에서는 β-lactamase 생성 *H. influenzae* 균주 비율이 증가함에 따라 3세대 세팔로스포린(Cefotaxime, Ceftriaxone)이 표준 치료제로 자리잡았습니다. Bacampicillin은 내성 문제로 후두개염 현행 1차 치료 지침에서 권고되지 않으며, 직접적인 임상 근거도 부재합니다.

---

## 임상시험 근거

현재 후두개염(Epiglottitis)에 대한 Bacampicillin 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 후두개염에 대한 관련 문헌이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Research Question**

**사유:**
Bacampicillin의 활성 대사체 Ampicillin이 후두개염의 주요 병원체(*H. influenzae*, *Streptococcus* spp.)에 대한 항균 활성을 보유하여 기전적 연관성은 성립하나, 직접적인 임상 근거가 전무하고 β-lactamase 내성 확산으로 인해 현대 치료 지침에서 Ampicillin 계열은 더 이상 1차 선택약이 아닙니다.

**진행하려면 필요한 것:**
- DrugBank를 통한 상세 작용 기전(MOA) 및 DrugBank ID 확인
- 허가사항 PDF를 통한 경고·금기·약물 상호작용 정보 보완 (현재 Blocking 데이터 갭)
- β-lactamase 내성 현황에 관한 현행 역학 데이터 검토
- 후두개염 현행 치료 지침(IDSA 등)과의 위치 비교 분석
- 참고: 동일 약물에서 **요도 질환(Urethral Disease, Rank 9)**에 대해 직접 임상 문헌([PMID 2921050](https://pubmed.ncbi.nlm.nih.gov/2921050/), 남성 비임균성 요도염 파일럿 연구, 1989)이 1건 존재하며, 1순위 후두개염보다 직접적인 임상 근거를 보유하고 있어 병행 검토를 권장합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

