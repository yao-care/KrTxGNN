---
layout: default
title: Liothyronine
parent: 모델 예측만 (L5)
nav_order: 478
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Liothyronine: 예측 신규 적응증 신장 저형성/무형성 (renal hypodysplasia/aplasia) (근거 수준 L5). 기존 적응증: 이번 보고서용으로 정리된 데이터에는 허가 적응증 본문이 없습니다(허가증 PDF 링크만 확인됨). 허가사항 확인이 필요합니다"
monitor_inn: "Liothyronine"
predicted_indications: ["renal hypodysplasia/aplasia", "bilateral renal agenesis", "nodular goiter (disease)", "Carney complex", "peripheral dysostosis", "Potter sequence", "acrodysostosis with or without hormone resistance", "angiomyxoma", "myxoma", "hypotrichosis simplex of the scalp"]
---

# Liothyronine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 약사 평가 보고서

</div>

# Liothyronine: 갑상선호르몬 보충에서 신장 저형성/무형성으로

## 한 문장 요약

Liothyronine은 합성 삼요오드티로닌(T3) 제제로, 한국에서 갑상선호르몬 제제로 허가되어 시판되고 있습니다. TxGNN 모델은 **신장 저형성/무형성(renal hypodysplasia/aplasia)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 다룬 **임상시험은 0건, 문헌도 0편**이어서 모델 예측 외의 근거는 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 이번 보고서용으로 정리된 데이터에는 허가 적응증 본문이 없습니다(허가증 PDF 링크만 확인됨). 허가사항 확인이 필요합니다. |
| 예측 신규 적응증 | 신장 저형성/무형성 (renal hypodysplasia/aplasia) |
| TxGNN 예측 점수 | 99.95% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Liothyronine은 활성형 갑상선호르몬(T3)의 단일 성분 제제이며, 갑상선호르몬 신호는 전반적인 장기 발생에 관여하는 것으로 알려져 있습니다.

그러나 출생 후 투여하는 liothyronine이 선천성 신장 기형을 되돌릴 수 있는 확립된 기전은 없습니다. 높은 TxGNN 점수는 지식 그래프상의 연관성에 근거한 예측일 뿐, 이를 뒷받침하는 임상시험이나 문헌이 없습니다.

참고로 같은 약물에 대한 다른 상위 예측 질환(양측 신장 무형성, Potter 연쇄, Carney complex, 점액종 등)도 모두 L5 수준이며 Hold로 평가되었습니다. 결절성 갑상선종은 TSH 억제라는 역사적 근거가 있으나, 확인된 문헌은 1980년 고양이 갑상선기능항진증 사례 보고뿐이어서 인체 근거로 볼 수 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

(참고: 7위 예측 질환인 말단이골증(acrodysostosis)에는 20편의 문헌이 연결되어 있으나, 갑상선기능저하증 병용요법, 우울증 보강요법, 갑상선호르몬 저항성 등 다른 질환을 다룬 것이어서 신장 질환 예측의 근거가 되지 않습니다.)

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201503196 | 테트로닌정5㎍ (리오티로닌나트륨) | 흰색의 타원형 정제 | 허가증 PDF 참조 |
| 201707572 | 테트로닌정 (리오티로닌나트륨) (수출용) | 흰색의 원형 정제 | 허가증 PDF 참조 |

두 제품 모두 (주)다림바이오텍이 제조하는 단일제이며 유효 상태입니다.

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 확인되었으며, 표시된 상위 항목은 모두 중등도(Moderate)입니다. 주요 항목은 다음과 같습니다.
  - 당뇨병 치료제: acarbose, metformin, pioglitazone, alogliptin, linagliptin, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide, albiglutide, dulaglutide
  - 위산억제제: omeprazole, rabeprazole, dexlansoprazole
  - 미네랄 제제: calcium phosphate, calcium acetate, magnesium oxide
  - 교감신경 작용 약물: epinephrine, isometheptene, diethylpropion
- **지식 그래프상 금기 질환** (허가사항 문구가 아닌 TxGNN 지식 그래프 기반): 고혈압, 뇌하수체기능저하증 및 관련 유전질환, 선천성 성선자극호르몬저하성 성선기능저하증(Kallmann 증후군 포함), 골다공증, 당뇨병 및 당뇨병성 케톤산증, 관상동맥질환, 심근경색, 흉선 질환

허가사항의 경고 및 금기 문구는 확인되지 않았으므로 반드시 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
신장 저형성/무형성에 대한 임상시험과 문헌이 없고, 구조적 발생 이상을 호르몬 제제로 교정할 수 있다는 기전적 근거도 없습니다. 근거는 모델 예측(L5)에 그칩니다.

**진행하려면 필요한 것:**
- 허가사항(경고, 금기, 적응증) 확보 및 분석. 안전성 선별 단계로 넘어가기 위한 필수 선행 과제입니다.
- DrugBank 등에서 상세 작용 기전(MOA) 확보
- 신장 발생 이상과 갑상선호르몬 신호의 연관성을 보여주는 전임상 또는 임상 근거
- 신장 질환 예측을 대신해 인체 근거가 있는 후보 질환(예: 결절성 갑상선종의 TSH 억제요법)을 재검토하는 방안
- 투여 경로 적합성 평가(현재 미평가 상태)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

