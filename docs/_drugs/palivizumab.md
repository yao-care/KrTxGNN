---
layout: default
title: Palivizumab
parent: 모델 예측만 (L5)
nav_order: 576
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Palivizumab: 예측 신규 적응증 설소 양성 종양 (benign neoplasm of tongue) (근거 수준 L5). 기존 적응증: 허가 적응증 본문은 이번 데이터에 포함되지 않았습니다(허가사항 문서 링크만 확인됨). 허가사항을 직접 확인해야 합니다"
monitor_inn: "Palivizumab"
predicted_indications: ["benign neoplasm of tongue", "epiglottis neoplasm", "cervical neuroblastoma", "benign neoplasm of hypopharynx", "benign neoplasm of floor of mouth", "tumor of testis and paratestis", "cystic neoplasm", "schwannoma of jugular foramen", "mesenchymoma", "thyroglossal duct cyst"]
---

# Palivizumab
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

## Palivizumab: RSV 예방에서 설소 양성 종양(Benign Neoplasm of Tongue)으로
{: .text-alpha }

## 한 문장 요약

Palivizumab은 RSV(호흡기세포융합바이러스)의 F 단백질을 표적으로 하는 인간화 단일클론항체로, 한국에서 시나지스주사액으로 시판되고 있습니다.
TxGNN 모델은 **설소 양성 종양(benign neoplasm of tongue)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다. 예측은 모델 계산에만 근거합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문은 이번 데이터에 포함되지 않았습니다(허가사항 문서 링크만 확인됨). 허가사항을 직접 확인해야 합니다. |
| 예측 신규 적응증 | 설소 양성 종양 (benign neoplasm of tongue) |
| TxGNN 예측 점수 | 99.94% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 없습니다. 알려진 정보에 따르면 Palivizumab은 RSV F 단백질에 결합해 바이러스를 중화하는 단일클론항체입니다.

설소 양성 종양에는 RSV와 관련된 병리나 F 단백질 표적이 알려져 있지 않습니다. 따라서 이 약이 효과를 내려면 아직 확인되지 않은 비표적(off-target) 기전이 필요합니다. 높은 TxGNN 점수(99.94%)는 계산상의 예측일 뿐이며, 기전상 타당성을 입증하지 못합니다.

같은 모델이 예측한 다른 후보(상위 10건: 후두개 신생물, 경부 신경모세포종, 하인두 양성 종양, 구강저 양성 종양, 고환 및 부고환 종양, 낭성 신생물, 경정맥공 신경초종, 중간엽종, 갑상설관 낭종)도 모두 마찬가지로 기전적 연관성이 확인되지 않았고 임상시험·문헌 근거가 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201605448 | 시나지스주사액50밀리그램(팔리비주맙) | 바이알 주사제 (투명 내지 약간의 유백색 액) | 허가사항 문서 참조 |
| 201605447 | 시나지스주사액100밀리그램(팔리비주맙) | 바이알 주사제 (투명 내지 약간의 유백색 액) | 허가사항 문서 참조 |

두 제품 모두 한국아스트라제네카(주)가 허가를 보유한 단일제이며 유효 상태입니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 매우 높지만 임상시험과 문헌 근거가 전혀 없고(L5), 항RSV 항체와 해당 질환 사이에 확인된 기전적 연관성도 없습니다. 현재로서는 재창출을 진행할 근거가 부족합니다.

**진행하려면 필요한 것:**
- 허가사항(경고, 금기, 적응증)의 확인 및 정리
- 상세한 작용 기전(MOA) 데이터 확보
- 설소 양성 종양과 RSV F 단백질 또는 다른 표적 사이의 기전적 연관성에 대한 전임상 근거
- 관련 임상시험 또는 문헌 근거 (현재 없음)
- 투여 경로 적합성 평가 (현재 미평가)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

