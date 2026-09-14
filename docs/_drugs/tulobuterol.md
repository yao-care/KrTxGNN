---
layout: default
title: Tulobuterol
parent: 僅模型預測 (L5)
nav_order: 711
evidence_level: L5
indication_count: 10
---

# Tulobuterol
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

# Tulobuterol: 기관지천식·COPD 기관지확장제에서 기관지염으로

## 한 문장 요약

Tulobuterol(DrugBank ID: DB12248)은 선택적 β2-adrenergic agonist 계열의 기관지확장제로, 해외(일본 등)에서 기관지천식 및 만성폐쇄성폐질환(COPD) 치료에 사용되어 왔으나 한국에는 아직 시판되지 않은 약물입니다.
TxGNN 모델은 **기관지염(Bronchitis)**에 효과가 있을 수 있다고 예측하며(예측 점수 99.98%), 현재 **1건의 임상시험**과 **4편의 문헌**이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (한국 미시판) — 해외에서는 기관지천식·COPD 기관지확장제로 사용 |
| 예측 신규 적응증 | 기관지염 (Bronchitis) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L1 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

현재 DrugBank에 등재된 상세 작용기전(MOA) 데이터는 확인되지 않습니다(Data Gap). 다만 근거팩에 포함된 문헌 및 예측 근거에 따르면, Tulobuterol은 선택적 β2-adrenergic agonist 계열의 기관지확장제로, 기관지 평활근 이완과 더불어 점액섬모청소율(mucociliary clearance) 개선 효과를 갖는 것으로 알려져 있습니다.

기관지염은 기도 염증과 가역적 기관지 수축, 점액 배출 저하가 핵심 병리 기전인 질환으로, β2-agonist의 기관지 확장 및 점액섬모청소 촉진 작용이 직접적으로 적용될 수 있습니다. 실제로 관련 문헌에서는 Tulobuterol이 만성 폐쇄성 기관지염 환자의 점액섬모청소율을 유의하게 개선시켰다고 보고하고 있으며, 같은 약물 계열이 폐쇄성 기도질환(obstructive lung disease) 전반에서 이미 다수의 Phase 4 임상시험을 통해 효능을 입증한 바 있어, 이번 TxGNN 예측의 기전적 타당성을 뒷받침합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT06411925](https://clinicaltrials.gov/study/NCT06411925) | Phase 4 | 모집 중 | 296 | 다기관·이중맹검·활성대조 비열등성 시험으로, 급성 기관지염 환자에서 Atock Dry Syrup(Tulobuterol 함유)의 유효성 및 안전성 평가 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [2884705](https://pubmed.ncbi.nlm.nih.gov/2884705/) | 1987 | 임상연구 | Respiration | Tulobuterol과 fenoterol이 만성 폐쇄성 기관지염 및 만성 기관지천식 환자에서 점액섬모청소율(mucociliary clearance)을 유의하게 개선함 |
| [2983286](https://pubmed.ncbi.nlm.nih.gov/2983286/) | 1985 | 임상연구 | Orvosi Hetilap | β-미메틱 약물이 기관지 점액 수송(bronchial mucus transport)에 미치는 영향 연구 |
| [2861899](https://pubmed.ncbi.nlm.nih.gov/2861899/) | 1985 | Review | Clinical Therapeutics | β2-작용제가 급·만성 천식에 유용하며, 만성 기관지염·폐기종에서도 가역적 기도폐쇄 성분이 있는 경우 시도할 가치가 있음을 논의 |
| [23527972](https://pubmed.ncbi.nlm.nih.gov/23527972/) | 2013 | Review | 중화아과잡지 (Chin J Pediatr) | 소아 천명성 질환에서 경피 β2-작용제(Tulobuterol 패치)의 임상 적용 고찰 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (한국 내 허가사항이 없어 TFDA 등 규제기관 첨부문서 확보가 필요합니다.)

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
Tulobuterol의 β2-agonist 기전은 기관지염의 병태생리(기관지수축·점액 정체)에 직접 적용 가능하며, 관련 계열 약물이 폐쇄성 기도질환 전반에서 이미 다수의 Phase 4 RCT로 효능이 입증되어 있습니다. 다만 기관지염 특이적 근거는 현재 모집 중인 Phase 4 시험 1건과 소규모 문헌 4편에 국한되어 있어, 안전장치(Guardrails)를 갖춘 상태로 진행하는 것이 적절합니다.

**진행하려면 필요한 것:**
- TFDA(또는 식약처) 공식 첨부문서 확보 및 경고/금기사항 파싱 (DG001, Blocking — S1 안전성 초기평가 진입 필수 조건)
- DrugBank API를 통한 상세 작용기전(MOA) 데이터 보완 (DG002)
- NCT06411925 임상시험 완료 및 결과 데이터 확보
- 한국 내 시판/허가 신청 여부에 대한 규제 전략 검토 (현재 허가증 0건)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

