---
layout: default
title: Mannitol
parent: 모델 예측만 (L5)
nav_order: 494
evidence_level: L5
indication_count: 9
monitor_inn: "Mannitol"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "acute pulmonary heart disease", "exercise-induced malignant hyperthermia", "familial periodic paralysis", "hypokalemic periodic paralysis", "congenital multicore myopathy with external ophthalmoplegia", "moderate multiminicore disease with hand involvement", "nephrogenic diabetes insipidus", "central core myopathy"]
last_modified_at: 2026-10-31
description: "Mannitol: 예측 신규 적응증 신성 항이뇨 부적절 증후군 (근거 수준 L5). 기존 적응증: 허가증에 적응증 본문 대신 식약처 문서 링크만 수록되어 있어 구체적인 적응증 문구는 확인되지 않음"
---

# Mannitol
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **9** 건
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

## Mannitol: 허가 용도에서 신성 항이뇨 부적절 증후군으로
{: .text-alpha }

## 한 문장 요약

Mannitol은 한국에서 단일 성분 주사제와 흡입용 캡슐로 허가된 삼투성 약물입니다. TxGNN 모델은 **신성 항이뇨 부적절 증후군(nephrogenic syndrome of inappropriate antidiuresis)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 연구한 임상시험은 없고 **관련 문헌 1편**(저나트륨혈증 평가 일반 리뷰)만 있어 근거는 모델 예측 수준에 머뭅니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에 적응증 본문 대신 식약처 문서 링크만 수록되어 있어 구체적인 적응증 문구는 확인되지 않음 |
| 예측 신규 적응증 | 신성 항이뇨 부적절 증후군 |
| TxGNN 예측 점수 | 0.9997 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 8건 / 전체 8건) |
| 허가증 수 | 8건 (유효 8건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Mannitol은 삼투성 이뇨제로, 신장에서 물과 용질 배설을 늘리는 약물입니다.

신성 항이뇨 부적절 증후군은 물 재흡수가 과도해 저나트륨혈증이 생기는 질환입니다. 삼투성 이뇨가 이론상 수분 배설을 돕는다고 볼 여지는 있습니다. 그러나 Mannitol은 혈관 내 용적을 늘리고 용질을 함께 배설시키므로, 이 질환에서 이득이 제한적일 것으로 예상됩니다. 연결된 문헌도 저나트륨혈증 평가 시 흔한 함정을 다룬 일반 리뷰일 뿐 Mannitol 사용을 뒷받침하지 않습니다. 높은 TxGNN 점수는 임상 근거 없는 네트워크 기반 예측입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European Journal of Internal Medicine | 저나트륨혈증 환자 평가 시 흔한 함정 10가지를 정리한 리뷰. Mannitol 사용 근거는 제시하지 않음 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 197100027 | 대한디-만니톨주사액(25%) | 주사액 | 적응증 본문 없음(식약처 문서 링크만 수록) |
| 199101334 | 이노엔20%만니톨주사액 | 수액용 주사제 | 적응증 본문 없음(식약처 문서 링크만 수록) |
| 200805048 | 아리돌흡입용캡슐콤비팩(만니톨) | 흡입용 캡슐 | 적응증 본문 없음(식약처 문서 링크만 수록) |
| 197500054 | 중외20%만니톨주 | 주사액 | 적응증 본문 없음(식약처 문서 링크만 수록) |
| 197100029 | 대한디-만니톨주사액(15%) | 주사액 | 적응증 본문 없음(식약처 문서 링크만 수록) |

허가증은 총 8건이며, 위에는 5건만 나열했습니다.

## 안전성 고려사항

- **약물 상호작용**: 조회된 상호작용은 100건입니다. 이 중 확인된 대표 항목은 다음과 같습니다.
  - 주요(Major): Amikacin
  - 중등도(Moderate): Lamivudine, Formoterol, Salbutamol, Amifostine, Benazepril, Captopril, Carbamazepine, Citalopram, Canagliflozin, Dapagliflozin, 조영제(Iothalamic acid, Diatrizoate), 하제(Bisacodyl, Picosulfuric acid, Polyethylene glycol)
  - 경미(Minor): Doxycycline
- 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
이 질환을 직접 다룬 임상시험이나 문헌이 없고, 연결된 리뷰 1편도 Mannitol의 효과를 뒷받침하지 않습니다. 기전상 이득도 불확실해 근거 수준은 L5입니다.

**진행하려면 필요한 것:**
- 허가 적응증 원문 확인 (식약처 허가사항 문서 파싱)
- 허가사항의 경고 및 금기 정보 확보 (안전성 선별의 선행 조건)
- 작용 기전 데이터 확보 (예: DrugBank)
- 신성 항이뇨 부적절 증후군에서 삼투성 이뇨제의 효과와 안전성(용적 증가, 전해질 이상)을 직접 평가한 연구

### 참고: 다른 예측 신규 적응증 현황

| 순위 | 예측 질환 | TxGNN 점수 | 근거 수준 | 비고 |
|------|---------|-----------|----------|------|
| 2 | 급성 폐성심 | 0.9988 | L5 | 간접 문헌만 있으며 직접 연구가 없어 L5로 판정. 용적 증가로 우심 부하가 악화될 안전성 우려 |
| 3 | 운동유발 악성 고열 | 0.9986 | L5 | 임상시험과 문헌 없음 |
| 4 | 가족성 주기성 마비 | 0.9975 | L5 | 칼륨 무함유 희석액 역할 등 보조적 언급뿐 |
| 5 | 저칼륨성 주기성 마비 | 0.9972 | L5 | 칼륨 정맥투여 시 희석액 관련 보고뿐 |
| 6 | 외안근마비를 동반한 선천성 다핵심 근병증 | 0.9972 | L5 | 임상시험과 문헌 없음 |
| 7 | 손 침범 중등도 다소핵 질환 | 0.9971 | L5 | 임상시험과 문헌 없음 |
| 8 | 신성 요붕증 | 0.9970 | L5 | 삼투성 이뇨로 악화될 우려가 있어 기전상 부적절 |
| 9 | 중심핵 근병증 | 0.9969 | L5 | 임상시험과 문헌 없음 |

위 질환들은 모두 이 질환 자체를 직접 연구한 시험이나 문헌이 없어 L5로 정리했으며, 모두 Hold를 권장합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

