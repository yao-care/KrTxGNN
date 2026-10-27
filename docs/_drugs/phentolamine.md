---
layout: default
title: Phentolamine
parent: 모델 예측만 (L5)
nav_order: 599
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Phentolamine: 예측 신규 적응증 혈관 질환 (Vascular Disease) (근거 수준 L5). 기존 적응증: 확인 불가 (허가 적응증 본문이 링크로만 제공됨)"
monitor_inn: "Phentolamine"
predicted_indications: ["visceral calciphylaxis", "venous thoracic outlet syndrome", "arterial thoracic outlet syndrome", "neurogenic thoracic outlet syndrome", "blue toe syndrome", "angiodysplasia of stomach", "hemangioendothelioma", "atheroembolism of kidney", "idiopathic spontaneous coronary artery dissection"]
---

# Phentolamine
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

## Phentolamine: 허가 적응증 정보 미확인에서 혈관 질환으로
{: .text-alpha }

## 한 문장 요약

Phentolamine은 비선택적 알파-아드레날린 차단제로, 한국에서는 주사제(펜톨민주사)로 시판되고 있습니다. 다만 허가 적응증 본문은 이번 데이터에 포함되어 있지 않습니다.
TxGNN 모델은 **혈관 질환(Vascular Disease)**에 효과가 있을 수 있다고 예측하며, 현재 **8건의 임상시험**과 **20편의 문헌**이 관련되어 있습니다. 그러나 대부분은 약물을 연구 도구로 사용했거나 간접적으로만 관련된 자료이며, 직접적인 치료 근거는 제한적입니다.

> 참고: 예측 순위 1위는 내장 석회방어증(visceral calciphylaxis)이지만 임상시험과 문헌이 전혀 없습니다(근거 수준 L5). 따라서 이 보고서는 근거가 가장 많은 2위 예측인 "혈관 질환"을 중심으로 작성했습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 적응증 본문이 링크로만 제공됨) |
| 예측 신규 적응증 | 혈관 질환 (Vascular Disease) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L3 (대부분 종설·기전 연구, 직접적인 치료 시험 부재) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold (추가 연구 과제로 분류) |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 없습니다. 알려진 정보에 따르면 Phentolamine은 비선택적 알파-아드레날린 길항제로, 교감신경에 의한 혈관 수축을 줄이고 혈관 저항을 낮추는 혈관 확장 작용을 합니다.

이 기전은 카테콜아민이 원인인 혈관 위기, 즉 갈색세포종 위기, 코카인 관련 혈관병증, 고혈압 응급에서 이미 사용되는 치료 원리와 일치합니다. 문헌에서도 이런 상황에서 Phentolamine 사용이 반복적으로 언급됩니다.

다만 "혈관 질환"은 매우 넓은 개념이어서 구체적인 적응증으로 보기 어렵습니다. 근거 대부분이 기전, 생리학 연구 또는 오래된 종설·증례 문헌이므로, 기전상 가능성은 있어도 임상적 효능이 입증된 것은 아닙니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT06286059](https://clinicaltrials.gov/study/NCT06286059) | Phase 2/3 | 불명 | 60 | 복잡 PCI 후 조영제 유발 급성 신손상 고위험 환자에서 Phentolamine의 예방 효과·안전성 평가. 약물을 직접 검증하지만 소규모이고 상태 미확인 |
| [NCT05997732](https://clinicaltrials.gov/study/NCT05997732) | Phase 4 | 모집 중 | 30 | 교감신경-혈관 신호 전달에서 아드레날린 수용체의 역할과 성별 차이 (기전 연구, 치료 목적 아님) |
| [NCT05525416](https://clinicaltrials.gov/study/NCT05525416) | 해당 없음 | 완료 | 17 | 고지대 저산소 노출 시 교감신경 혈관 반응의 성별 차이 (약물은 탐침으로 추정) |
| [NCT05219799](https://clinicaltrials.gov/study/NCT05219799) | Early Phase 1 | 모집 중 | 72 | 저산소성 혈관 확장의 성별 차이와 비만의 영향 (연구 도구로 추정) |
| [NCT02966665](https://clinicaltrials.gov/study/NCT02966665) | Phase 1 | 모집 중 | 420 | 고혈압 재활과 운동에 따른 혈관 기능 연구 (생리학적 탐침으로 추정) |
| [NCT01422616](https://clinicaltrials.gov/study/NCT01422616) | Phase 3 | 완료 | 4,587 | 급성 허혈성 뇌졸중에서 저용량 rtPA와 집중 혈압 강하 (ENCHANTED). Phentolamine이 시험 대상이 아님 |
| [NCT00716079](https://clinicaltrials.gov/study/NCT00716079) | 해당 없음 | 완료 | 2,839 | 뇌내출혈에서 조기 집중 혈압 강하 (INTERACT2). Phentolamine이 시험 대상이 아님 |
| [NCT00226096](https://clinicaltrials.gov/study/NCT00226096) | 해당 없음 | 완료 | 404 | 급성 뇌내출혈에서 조기 집중 혈압 강하 (INTERACT). Phentolamine과의 관련성이 간접적 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [949032](https://pubmed.ncbi.nlm.nih.gov/949032/) | 1976 | Review | Am Heart J | Phentolamine의 임상 사용이 항고혈압제에서 울혈성 심부전, 급성 심근경색 후 좌심실 기능 개선으로 확대됨 |
| [37758424](https://pubmed.ncbi.nlm.nih.gov/37758424/) | 2023 | Review | Emerg Med Clin North Am | 부신 응급 상황에서 갈색세포종 등 카테콜아민 폭풍 시 Phentolamine으로 신속한 혈압 조절 |
| [28363516](https://pubmed.ncbi.nlm.nih.gov/28363516/) | 2017 | Review | Atherosclerosis | 코카인 중독에서 나타나는 혈관 질환 |
| [25657055](https://pubmed.ncbi.nlm.nih.gov/25657055/) | 2015 | Review | Trends Cardiovasc Med | 코카인 사용의 심혈관계 영향 |
| [8795497](https://pubmed.ncbi.nlm.nih.gov/8795497/) | 1996 | Review | J R Soc Med | 코카인 관련 심근경색의 치료 접근 |
| [3415797](https://pubmed.ncbi.nlm.nih.gov/3415797/) | 1988 | Review | Am J Hypertens | 갈색세포종 위기 증례. 혈압은 Phenoxybenzamine, Phentolamine, Nitroprusside로 조절 |
| [8497771](https://pubmed.ncbi.nlm.nih.gov/8497771/) | 1993 | Review | Schweiz Med Wochenschr | 고혈압 위기의 병태생리와 치료 |
| [235062](https://pubmed.ncbi.nlm.nih.gov/235062/) | 1975 | 기타 | Medicine | 고혈압 환자에서 아세틸콜린, 도파민, Phentolamine에 대한 신장 혈관 반응 |
| [12879109](https://pubmed.ncbi.nlm.nih.gov/12879109/) | 2000 | 기타 | Drugs Today | 경구 Phentolamine(Vasomax): 근육벽 혈관에 대한 강력한 직접 혈관 확장제 |
| [99030](https://pubmed.ncbi.nlm.nih.gov/99030/) | 1978 | 기타 | Am J Med | 후부하 감소와 전신 혈관 확장제를 이용한 심부전 치료 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200200196 | 펜톨민주사(펜토라민메실레이트) | 앰플(무색~미황색 액체) | 허가 적응증 본문은 허가사항 문서를 참조 (이연제약) |

## 안전성 고려사항

- **약물 상호작용**: 데이터에 총 100건의 상호작용이 있으며, 아래는 일부입니다.
  - 중등도: Bupropion, Morphine, Dronabinol, SGLT2 억제제(Canagliflozin, Dapagliflozin, Empagliflozin, Ertugliflozin)
  - 경미: 각종 인슐린 제제(human, aspart, degludec, detemir, glargine, glulisine, lispro 등)
- **예측 질환별 우려**: 위 혈관이형성증(angiodysplasia of stomach)에서는 혈관 확장으로 출혈이 악화될 수 있고, 자발성 관상동맥 박리에서는 저혈압과 반사성 빈맥이 우려됩니다.

경고·금기 등 허가사항 기반 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
혈관 질환에 대한 예측 점수는 높지만, 직접 효능을 검증한 시험은 소규모이고 상태가 불명확한 NCT06286059 한 건뿐입니다. 나머지 시험은 약물을 연구 도구로 쓰거나 다른 중재를 평가한 것이며, 문헌도 대부분 종설과 기전 설명입니다. 허가사항의 경고·금기 정보도 확인되지 않아 안전성 평가를 시작할 수 없습니다.

**진행하려면 필요한 것:**
- 허가사항(첨부문서) 확보: 허가 적응증, 경고, 금기 확인 (필수)
- 작용 기전(MOA) 및 약물 정보 DB 보강
- "혈관 질환"을 구체적인 질환(예: 조영제 유발 신손상, 카테콜아민 관련 혈관 위기)으로 좁히기
- NCT06286059의 진행 상태와 결과 확인, 필요 시 더 큰 규모의 무작위 대조 시험 설계
- 투여 경로 적합성 검토(현재 주사제 앰플 1종만 시판)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

