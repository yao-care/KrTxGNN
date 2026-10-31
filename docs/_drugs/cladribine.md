---
layout: default
title: Cladribine
parent: 모델 예측만 (L5)
nav_order: 218
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-31
description: "Cladribine: 예측 신규 적응증 수막주위 배아형 횡문근육종 (parameningeal embryonal rhabdomyosarcoma) (근거 수준 L5). 기존 적응증: 허가 적응증 텍스트가 데이터에 포함되어 있지 않아 확인할 수 없습니다(허가사항 원문 참조 필요)"
monitor_inn: "CLADRIBINE"
predicted_indications: ["parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "embryonal extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "rhabdomyosarcoma (disease)", "liver sarcoma"]
---

# Cladribine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **7** 건
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

## Cladribine: 기존 적응증에서 배아형 횡문근육종으로
{: .text-alpha }

## 한 문장 요약

Cladribine은 퓨린 뉴클레오시드 유사체로, 한국에서 경구 정제(마벤클라드정)와 주사제(류스타틴주사액)로 허가되어 시판 중입니다.
TxGNN 모델은 **배아형 횡문근육종(parameningeal embryonal rhabdomyosarcoma)**에 효과가 있을 수 있다고 예측하지만(점수 0.9977), 이 예측을 지지하는 **임상시험은 0건, 문헌은 0건**으로 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 텍스트가 데이터에 포함되어 있지 않아 확인할 수 없습니다(허가사항 원문 참조 필요). |
| 예측 신규 적응증 | 수막주위 배아형 횡문근육종 (parameningeal embryonal rhabdomyosarcoma) |
| TxGNN 예측 점수 | 0.9977 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 2건) |
| 권장 결정 | Hold |

> 참고: 상위 예측 6건(횡문근육종 및 그 하위 유형)은 점수가 99.74~0.9977로 서로 매우 비슷합니다. 질환 분류 체계의 구조에서 비롯된 신호로 보이므로 독립된 예측 여러 건이 아니라 **하나의 예측 군집**으로 해석하는 것이 적절합니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 이 보고서에 정리된 자료에 없습니다. 일반적으로 알려진 바에 따르면 Cladribine(2-chloro-2'-deoxyadenosine)은 아데노신 탈아미노효소에 분해되지 않는 퓨린 뉴클레오시드 유사체입니다. 데옥시시티딘 키나아제 활성이 5'-뉴클레오티드분해효소보다 높은 세포 안에서 삼인산 형태로 축적되어 DNA 가닥 손상과 세포자멸사를 일으킵니다. 이 작용은 림프구 계열 세포에서 잘 확립되어 있습니다.

그러나 횡문근육종이라는 고형 종양에서 이 기전이 작동한다는 근거는 현재 자료에 없습니다. 뉴클레오시드 유사체의 세포독성이 고형 종양에도 적용될 수 있다는 가설은 추측 단계입니다. 높은 점수는 TxGNN 모델(딥러닝)이 산출한 값으로, 관련 질환 사이에서 모델이 학습한 유사성을 반영할 수 있으며 생물학적 근거는 아닙니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

횡문근육종 예측에 직접 해당하는 문헌은 없습니다. 참고로, 7순위 예측인 간 육종(liver sarcoma)에 연결된 문헌은 다음 1편뿐이며 간 육종을 직접 다룬 것이 아닙니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [15241520](https://pubmed.ncbi.nlm.nih.gov/15241520/) | 2004 | Case report | Der Hautarzt | 무증상형(smoldering) 전신 비만세포증에서 Cladribine 치료 성공 사례. 혈액 종양에 대한 보고이며 간 육종의 직접 근거는 아님 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201904640 | 마벤클라드정 (머크) | 흰색의 원형 정제 | 허가사항 원문 참조 필요 |
| 199704348 | 류스타틴주사액 (지피테라퓨틱스코리아) | 투명한 무색 용액이 든 바이알(주사제) | 허가사항 원문 참조 필요 |

## 세포독성

Cladribine은 퓨린 유사체 계열의 세포독성 항대사제로 판단됩니다. 이 데이터에는 세포독성 관련 상세 정보가 없으므로 허가사항의 경고 및 주의사항을 참조하세요. 다만 지식 그래프에는 호중구감소증, 혈소판감소증, 무과립구증, 빈혈과 같은 혈액학적 이상이 금기 질환으로 연결되어 있어, 사용 시 혈구 수치 모니터링이 필요할 가능성이 큽니다.

## 안전성 고려사항

- **지식 그래프 기반 금기 질환**(허가사항 문구가 아닌 TxGNN 지식 그래프의 약물-질환 금기 관계): 신장 질환, 요관 농양(pyoureter), 혈소판감소증, 고요산혈증, 호중구감소증, 무과립구증, 말초신경계 질환, 말초신경병증, 빈혈, 대적혈구성 빈혈
- **약물 상호작용**(총 100건 조회, 주요 항목):
  - **Major**: 코르티코스테로이드류(Hydrocortisone, Triamcinolone, Dexamethasone, Betamethasone, Budesonide, Prednisolone, Prednisone), Deferiprone, 방사성의약품 및 방사성 면역치료제(Ibritumomab tiuxetan, Iobenguane I-131, Tositumomab, Samarium-153 lexidronam, Strontium-89 chloride)
  - **Moderate**: Palifermin, Dipyridamole, Cilostazol, Eltrombopag

허가사항의 경고 및 금기 정보는 이 데이터에 포함되어 있지 않으므로 허가사항 원문을 반드시 확인해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
횡문근육종에 대한 예측은 모델 점수(0.9977)만 있고 임상시험과 문헌이 전혀 없어 근거 수준이 L5입니다. 횡문근육종 관련 예측들은 서로 상관된 하나의 군집이어서 독립된 근거로 볼 수 없으며, 고형 종양에서의 작용 기전도 입증되지 않았습니다.

**진행하려면 필요한 것:**
- 허가사항 원문(적응증, 경고, 금기)의 확보 및 분석
- 상세한 약물 작용 기전(MOA) 데이터 확보
- 횡문근육종 세포주 및 동물 모델에서의 전임상 효능 근거
- 소아·청소년 횡문근육종에서 Cladribine 사용에 관한 문헌 및 임상시험 조사
- 골수억제, 신장애, 신경독성 등 안전성 위험에 대한 평가 계획
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

