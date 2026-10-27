---
layout: default
title: Sotatercept
parent: 모델 예측만 (L5)
nav_order: 700
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Sotatercept: 예측 신규 적응증 급성 림프모구성 백혈병 (acute lymphoblastic leukemia) (근거 수준 L5). 기존 적응증: 확인 불가 (허가 적응증이 문서 링크로만 제공되어 본문을 확인하지 못함)"
monitor_inn: "Sotatercept"
predicted_indications: ["acute lymphoblastic leukemia (disease)", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "drug-induced osteoporosis", "diabetic cataract", "HER2 positive breast carcinoma", "transitional cell carcinoma", "prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant"]
---

# Sotatercept
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

## Sotatercept: 폐동맥 고혈압에서 급성 림프모구성 백혈병으로
{: .text-alpha }

## 한 문장 요약

Sotatercept는 액티빈 수용체 IIA-Fc 융합 단백질로, 한국에서 주사제(제품명 윈레브에어)로 허가·시판되고 있습니다.
TxGNN 모델은 **급성 림프모구성 백혈병(acute lymphoblastic leukemia)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 **임상시험과 문헌은 0건**으로 모델 예측만 있는 상태입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 적응증이 문서 링크로만 제공되어 본문을 확인하지 못함) |
| 예측 신규 적응증 | 급성 림프모구성 백혈병 (acute lymphoblastic leukemia) |
| TxGNN 예측 점수 | 99.78% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 4건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Sotatercept는 TGF-beta 슈퍼패밀리에 속하는 액티빈과 성장분화인자(GDF)를 포획(trap)하는 액티빈 수용체 IIA-Fc 융합 단백질입니다. 이 경로는 조혈 조절과 관련이 있다고 알려져 있습니다.

다만 이 경로가 급성 림프모구성 백혈병과 직접 연결된다는 기전적 근거는 현재 데이터로 확인되지 않습니다. 기존 적응증과의 연관성도 평가할 수 없어, 이 예측은 계산 모델의 출력에 머물러 있으며 검증이 필요합니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202501871 | 윈레브에어키트주45밀리그램 | 동결건조 주사제(바이알) + 용제 프리필드시린지 | 허가사항 문서 참조 |
| 202501872 | 윈레브에어주45밀리그램 | 동결건조 주사제(바이알) | 허가사항 문서 참조 |
| 202501873 | 윈레브에어주60밀리그램 | 동결건조 주사제(바이알) | 허가사항 문서 참조 |
| 202501874 | 윈레브에어키트주60밀리그램 | 동결건조 주사제(바이알) + 용제 프리필드시린지 | 허가사항 문서 참조 |

4건 모두 한국엠에스디(주)의 단일제이며 유효 상태입니다.

## 다른 예측 적응증 (참고)

TxGNN이 예측한 다른 후보도 모두 임상시험·문헌 근거가 없는 L5 수준이며 권장 결정은 Hold입니다.

| 순위 | 예측 질환 | TxGNN 점수 | 비고 |
|------|---------|-----------|------|
| 2 | 중증 비증식성 당뇨망막병증 | 99.77% | 망막 혈관 재형성과의 연관은 추측 수준이며, 안구 내 안전성은 알려져 있지 않음 |
| 3 | 당뇨망막병증 | 99.72% | 위와 동일한 추측성 근거 |
| 4 | 약물 유발 골다공증 | 99.65% | 액티빈 억제와 뼈 대사의 연관은 그럴듯하나 미검증 |
| 5 | 당뇨병성 백내장 | 99.49% | 뚜렷한 기전적 연결 없음 |
| 6 | HER2 양성 유방암 | 99.43% | 액티빈 경로의 종양 영향은 맥락에 따라 달라 확립되지 않음 |
| 7-10 | 요로상피(이행세포) 암종 및 아형 | 99.34~99.39% | 질환 온톨로지 유사성에 의한 예측일 가능성이 높음 |

## 결론 및 다음 단계

**결정: Hold**

**사유:**
급성 림프모구성 백혈병에 대한 예측은 점수(99.78%)가 높지만 임상시험과 문헌이 전혀 없고 기전 연결도 확인되지 않아 모델 예측 단계(L5)에 머물러 있습니다.

**진행하려면 필요한 것:**
- 상세한 작용 기전(MOA) 데이터 확보와 액티빈/GDF 신호와 급성 림프모구성 백혈병 간 연관성 검토
- 관련 임상시험 및 문헌 탐색 (현재 없음)
- 허가사항(첨부문서)의 경고, 금기, 약물 상호작용 정보 확보 및 안전성 검토
- 기존 허가 적응증 본문 확인 (현재 문서 링크만 확인됨)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

