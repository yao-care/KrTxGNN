---
layout: default
title: Ipratropium
parent: 모델 예측만 (L5)
nav_order: 435
evidence_level: L5
indication_count: 9
monitor_inn: "ipratropium"
predicted_indications: ["nasal cavity disease", "pharyngitis", "acute laryngopharyngitis", "respiratory malformation", "papillary conjunctivitis", "Rienhoff syndrome", "tracheal disease", "anaphylaxis", "food-dependent exercise-induced anaphylaxis"]
last_modified_at: 2026-10-31
description: "Ipratropium: 예측 신규 적응증 비강 질환 (nasal cavity disease) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199803475/EE"
---

# Ipratropium
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

## Ipratropium: 무스카린 수용체 길항제 → 비강 질환 (nasal cavity disease)
{: .text-alpha }

## 한 문장 요약

Ipratropium은 무스카린 수용체를 차단하는 항콜린성 약물로, 국내에서는 흡입액 및 분무액 제제로 허가되어 있습니다. TxGNN 모델은 **비강 질환(nasal cavity disease)**에 효과가 있을 수 있다고 예측합니다(예측 점수 0.9986). 다만 이 질환을 직접 다룬 임상시험은 없고, 간접적인 문헌 2편만 확인되어 근거는 모델 예측 수준입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199803475/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199304302/EE |
| 예측 신규 적응증 | 비강 질환 (nasal cavity disease) |
| TxGNN 예측 점수 | 0.9986 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 확보되지 않았습니다. 알려진 정보에 따르면 ipratropium은 무스카린 수용체 길항제입니다. 비강 점막의 분비샘은 콜린성 자극으로 분비가 늘어나므로, 무스카린 차단은 콧물(rhinorrhea) 감소로 이어질 수 있습니다.

따라서 비강 점막의 과다 분비가 문제인 질환에서는 기전상 적용 가능성이 있습니다. 다만 이번에 수집된 문헌은 모두 간접 근거이며, 비강 질환에 대한 임상시험은 없습니다. 이 예측은 기전 추정과 모델 점수에 의존하는 단계입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [39047643](https://pubmed.ncbi.nlm.nih.gov/39047643/) | 2024 | 전임상 | Colloids Surf B Biointerfaces | 알레르기 비염 치료를 위해 활성산소(ROS) 반응성 하이드로겔로 ipratropium을 전달하는 새로운 방식을 제시. 잦은 분무 투여와 비점막 자극 문제를 개선하려는 전임상 연구 |
| [42524014](https://pubmed.ncbi.nlm.nih.gov/42524014/) | 2026 | 리뷰 | Adv Pharm Bull | 파킨슨병에서의 비강 내 약물 전달 임상 연구 개관. 비강 질환 자체나 ipratropium을 다룬 연구는 아니며 간접 근거에 그침 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199803475 | 리노벤트비액(이프라트로퓸브롬화물수화물) | 정량분무식 용기에 든 무색투명한 액제 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199803475/EE) |
| 199304302 | 아트로벤트흡입액유디비(이프라트로퓸브롬화물수화물) | 1회용 폴리에틸렌 용기에 든 흡입용 액제 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199304302/EE) |

## 안전성 고려사항

- **약물 상호작용**: 총 106건이 확인되었으며, 수집된 주요 항목은 모두 중등도(Moderate)입니다. 대부분 항콜린 작용이 겹치는 약물입니다.
  - 항콜린제: hyoscyamine, atropine, glycopyrronium, clidinium, dicyclomine, mepenzolate, methscopolamine, propantheline, scopolamine, trospium, aclidinium
  - 항히스타민제: promethazine, chlorpheniramine, acrivastine
  - 기타: eluxadoline, prucalopride, 흡입 인슐린, physostigmine(점안), acetylcholine

경고 및 금기 등 그 밖의 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 비강 질환을 직접 다룬 임상시험이 없고, 문헌도 전임상 연구와 다른 질환의 리뷰뿐이어서 근거 수준이 L5입니다.
- 모델 예측 점수는 높지만 이를 뒷받침하는 직접 근거가 부족합니다.

**진행하려면 필요한 것:**
- 비강 질환(구체적으로 콧물이 주 증상인 비염 등)에서 ipratropium의 효능을 평가한 임상시험 또는 체계적 문헌고찰
- 작용 기전 데이터 확보
- 허가사항(경고, 금기) 확보 및 비강 투여 경로의 적합성 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

