---
layout: default
title: Ifosfamide
parent: 모델 예측만 (L5)
nav_order: 413
evidence_level: L5
indication_count: 9
monitor_inn: "Ifosfamide"
predicted_indications: ["unclassified myelodysplastic syndrome", "partial deletion of the long arm of chromosome 5", "refractory cytopenia of childhood", "severe congenital hypochromic anemia with ringed sideroblasts", "aregenerative anemia", "rhabdomyosarcoma (disease)", "myelodysplastic syndrome", "monocytic leukemia", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
last_modified_at: 2026-10-23
description: "Ifosfamide: 예측 신규 적응증 미분류 골수이형성증후군 (근거 수준 L5). 기존 적응증: 확인 불가 (허가 적응증 텍스트 없이 허가사항 링크만 확인됨)"
---

# Ifosfamide
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

## Ifosfamide: 기존 허가 적응증 미확인에서 미분류 골수이형성증후군으로
{: .text-alpha }

## 한 문장 요약

Ifosfamide는 한국에서 부광약품의 주사제(홀록산주)로 허가된 알킬화 계열 항암제입니다. 다만 허가 적응증의 본문 텍스트는 이번 데이터에서 확인되지 않았습니다. TxGNN 모델은 **미분류 골수이형성증후군(unclassified myelodysplastic syndrome)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 다룬 **임상시험은 0건, 문헌도 0건**이어서 근거는 모델 예측 수준에 그칩니다. 오히려 알킬화제는 치료 관련 골수이형성증의 원인으로 알려져 있어 안전성 신호가 반대 방향을 가리킵니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 적응증 텍스트 없이 허가사항 링크만 확인됨) |
| 예측 신규 적응증 | 미분류 골수이형성증후군 |
| TxGNN 예측 점수 | 0.9971 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Ifosfamide는 간에서 활성화되는 DNA 알킬화 전구약물로, 세포독성 항암제 계열입니다.

이 계열은 육종 등 고형암에서 활성이 확립되어 있습니다. 반면 골수이형성증후군은 골수 기능 부전 질환이며, 알킬화제는 골수억제를 일으키고 치료 관련 골수이형성증(특히 5번 염색체 장완 결손 형태)과 연관되어 있습니다. 따라서 이 예측은 기전상 뒷받침되기 어렵고, 점수가 높은 이유는 치료 효과가 아니라 이상반응 연관성을 반영했을 가능성이 있습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200804588 | 홀록산주1000밀리그람(이포스파마이드) | 흰색의 결정성 가루가 들어있는 바이알 | 적응증 텍스트 없음 (허가사항 링크만 확인됨) |

제조사는 부광약품(주)이며 단일 성분 제제입니다. 허가 상태는 유효로 기록되어 있습니다.

## 세포독성

아래 내용은 이번에 정리된 데이터에 약물 독성 정보가 없어, 이 약물 계열에 대한 일반적인 약리학 지식에 근거했습니다. 자세한 내용은 허가사항의 경고 및 주의사항을 참조하세요.

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (알킬화제) |
| 골수억제 위험 | 중~고 (용량 의존적) |
| 구토 유발성 등급 | 중~고 (용량에 따라 다름) |
| 모니터링 항목 | CBC(분류 포함), 신기능, 소변 검사(출혈성 방광염), 신경학적 상태 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 이 중 20건이 확인되었습니다. 대부분 중등도(Moderate) 수준입니다.
  - 항진균제: Amphotericin B, Amphotericin B (lipid complex)
  - 혈당강하제: Chlorpropamide, Glimepiride, Glipizide, Glyburide, Tolazamide, Acetohexamide, Nateglinide, Repaglinide
  - 아미노글리코시드계: Kanamycin, Neomycin
  - 구토 조절 및 중추신경계 약물: Aprepitant, Metoclopramide, Dronabinol, Nabilone, Scopolamine, Bupropion, Morphine
  - 경미(Minor): Levofloxacin

주요 경고와 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
이 질환을 직접 다룬 임상시험과 문헌이 없어 근거 수준은 L5(모델 예측만 있음)입니다. 알킬화제가 치료 관련 골수이형성증과 연관된다는 점에서 기전상 타당성도 낮아, 현 단계에서 진행을 권하기 어렵습니다.

**진행하려면 필요한 것:**
- 허가사항(경고, 금기, 허가 적응증 본문) 확보 및 분석
- 작용 기전 데이터 보완
- 골수이형성증후군에서의 치료 효과를 직접 검증한 임상 또는 전임상 근거
- 치료 관련 골수이형성증 위험에 대한 안전성 평가

**참고:** 같은 예측 목록의 횡문근육종(rhabdomyosarcoma)은 Ifosfamide 병용요법의 임상시험과 문헌이 상대적으로 많습니다. 다만 Phase 3 시험은 주로 성인 연부조직육종을 대상으로 한 것이라, 횡문근육종 자체를 직접 입증한 근거는 제한적입니다. 이 후보는 별도로 검토하는 것이 좋습니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

