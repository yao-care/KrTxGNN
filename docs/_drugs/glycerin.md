---
layout: default
title: Glycerin
parent: 모델 예측만 (L5)
nav_order: 388
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Glycerin: 예측 신규 적응증 마미증후군 (Cauda Equina Syndrome) (근거 수준 L5). 기존 적응증: 점안제 제품(안구 충혈 완화…"
monitor_inn: "GLYCERIN"
predicted_indications: ["cauda equina syndrome", "open-angle glaucoma", "primary hereditary glaucoma", "alopecia", "congenital hypotrichosis milia", "irritable bowel syndrome", "hypotrichosis simplex of the scalp", "diffuse alopecia areata", "migraine disorder", "migraine with brainstem aura"]
---

# Glycerin
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

## Glycerin: 점안제 적응증에서 마미증후군(Cauda Equina Syndrome)으로
{: .text-alpha }

## 한 문장 요약

Glycerin은 한국에서 점안액(안구 충혈 완화, 안구건조 증상 완화용 제품)으로 허가된 단일 성분 의약품입니다.
TxGNN 모델은 **마미증후군(Cauda Equina Syndrome)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다.
따라서 이 예측은 컴퓨터 모델 기반 가설 수준에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 점안제 제품(안구 충혈 완화, 안구건조 증상 완화 등). 허가 적응증 원문은 링크 형태로만 확인되어 상세 문구는 허가사항 참조 필요 |
| 예측 신규 적응증 | 마미증후군 (Cauda Equina Syndrome) |
| TxGNN 예측 점수 | 99.60% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 3건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Glycerin은 삼투성 물질로, 점안제에서는 윤활·보습 성분으로 쓰입니다. 다만 이것이 마미증후군에 적용 가능하다는 점은 데이터로 확인되지 않았습니다.

마미증후군은 척수 신경근이 눌리거나 부종이 생겨 발생하는 질환입니다. 삼투 작용을 통한 부종 완화가 이론상 연관될 수는 있으나, 추측에 불과합니다. 높은 TxGNN 점수는 지식 그래프상 유사성에서 나온 계산 결과일 뿐 실제 연구로 검증되지 않았습니다.

참고로 TxGNN 상위 예측 중 개방각 녹내장은 삼투성 안압 하강 효과라는 간접적 근거가 있습니다(근거 수준 L4). 다만 이는 주로 급성 폐쇄각 발작에 쓰이던 경구 투여 방식에서 유래한 것이며, 만성 개방각 녹내장에 대한 직접 근거는 아닙니다. 아래 표는 1순위 예측인 마미증후군 기준입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201101880 | 레드니스리리프점안액(수출용) | 점안제 (무색투명한 용기, 무색~엷은 황색 액) | 허가사항 참조 |
| 200403812 | 퓨어에이드드라이아이릴리프티얼스루브리칸트점안액(수출용) | 점안액 (투명한 용기, 무색~미황색 맑은 액) | 허가사항 참조 |
| 201106948 | 멕시멈레드니스릴리프점안액(수출용) | 점안제 (무색투명한 용기, 무색~엷은 황색 액) | 허가사항 참조 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 확인되었으며, 대부분 중등도(Moderate) 수준입니다. 주요 항목은 다음과 같습니다.
  - 중등도: Abiraterone, Tramadol, Acetazolamide, Hydrocortisone, Salbutamol, Alfuzosin, Hydrochlorothiazide, Amiloride, Amiodarone, Amisulpride, Benazepril, Anagrelide, Propofol, Apalutamide, Apomorphine, Triamcinolone, Arsenic trioxide, Lumefantrine, Asenapine
  - 경미(Minor): Doxycycline

경고 및 금기 등 그 밖의 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
마미증후군에 대한 임상시험과 문헌이 전혀 없고, 예측은 TxGNN 점수(99.60%)에만 의존합니다. 현재 허가 제형이 점안제여서 신경계 질환에 필요한 투여 경로와도 맞지 않을 가능성이 큽니다.

**진행하려면 필요한 것:**
- 상세한 약물 작용 기전(MOA) 데이터 확보
- 허가사항(식약처 첨부문서)의 경고·금기 정보 확인 및 정리
- 마미증후군에서 삼투 작용이 부종이나 신경근 압박에 미치는 영향을 다루는 전임상 또는 임상 근거
- 필요 투여 경로와 현재 허가 제형(점안제)의 적합성 검토
- 상대적으로 간접 근거가 있는 개방각 녹내장 등 다른 예측 적응증의 우선 검토 여부 판단
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

