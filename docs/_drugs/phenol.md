---
layout: default
title: Phenol
parent: 모델 예측만 (L5)
nav_order: 598
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-15
description: "Phenol: 예측 신규 적응증 만성 위축성 말단피부염 (acrodermatitis chronica atrophicans) (근거 수준 L5). 기존 적응증: 확인 불가 (허가 적응증 텍스트 대신 허가 문서 링크만 제공됨)"
monitor_inn: "PHENOL"
predicted_indications: ["acrodermatitis chronica atrophicans", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "neonatal dermatomyositis", "amyopathic dermatomyositis", "acne keloid", "hydroa vacciniforme, familial", "severe nonproliferative diabetic retinopathy", "dry eye syndrome"]
---

# Phenol
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **8** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 약사 평가 보고서

</div>

# Phenol: 허가 적응증 미확인에서 만성 위축성 말단피부염으로

## 한 문장 요약

Phenol은 한국에서 앰플 주사제 형태(수출용)로 허가된 단일 성분 의약품이며, 허가 적응증 본문은 이번 데이터에서 확인되지 않았습니다.
TxGNN 모델은 **만성 위축성 말단피부염(acrodermatitis chronica atrophicans)**에 효과가 있을 수 있다고 예측하지만, 이를 지지하는 **임상시험은 0건, 문헌도 0편**입니다.
전반적으로 모델 예측만 있는 단계(L5)입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 적응증 텍스트 대신 허가 문서 링크만 제공됨) |
| 예측 신규 적응증 | 만성 위축성 말단피부염 (acrodermatitis chronica atrophicans) |
| TxGNN 예측 점수 | 99.95% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 phenol은 단백질을 변성시키는 방부제이자 부식제, 신경파괴제(neurolytic agent)로 알려져 있습니다.

만성 위축성 말단피부염은 보렐리아(Borrelia) 감염의 후기 피부 증상입니다. Phenol은 스피로헤타 감염이나 이와 관련된 피부 위축 변화를 치료하는 것으로 알려진 바가 없어, 기전상 연결고리를 확인하지 못했습니다. 높은 예측 점수는 지식 그래프 기반 예측일 뿐, 이를 뒷받침하는 임상시험이나 문헌이 없습니다.

참고로 다른 예측 후보 중 **켈로이드성 여드름(acne keloid)**은 간접적인 가능성이 있습니다. 변형 phenol 필링(Exoderm)이 여드름 흉터와 주름 치료에 사용된 보고가 있기 때문입니다. 다만 이는 위축성 흉터에 대한 보고이며, 켈로이드성 여드름 자체를 평가한 것은 아니므로 유추 수준입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200200610 | 파오스클주(페놀)(수출명: Paoscle)(수출용) | 미황색 내지 황색의 투명한 액이 충진된 무색 투명한 앰플제 | 허가 문서 참조 (본문 미확인) |

## 안전성 고려사항

- **약물 상호작용**: 조회 결과 확인된 상호작용 정보가 없습니다.
- **지식 그래프상 금기 질환 (허가사항 문구가 아닌 모델 지식 그래프 기반)**: 간질, 간질환, 담낭질환, 당뇨병, 당뇨병성 케톤산증, 호중구감소증, 무과립구증, 심정지, 심장 전도장애, 방실차단, 호흡부전, 말초혈관질환, 활동성 소화성 궤양, 암, 림프종, 대상포진, 단순포진, 거대세포바이러스 감염, 피부염 등이 포함됩니다.
- 특히 phenol은 경피 흡수와 전신 독성 우려가 있어, 신생아·소아 대상 사용이나 안구 표면 사용은 안전성 측면에서 문제가 큽니다.

허가사항의 경고 및 금기 항목은 이번 데이터에 포함되지 않았으므로 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 1순위인 만성 위축성 말단피부염에 대해 임상시험과 문헌이 모두 없고 기전상 연결고리도 확인되지 않아 모델 예측만 존재합니다. 기존 허가 적응증과 안전성 정보도 확인되지 않은 상태입니다.

**진행하려면 필요한 것:**
- 식약처(MFDS) 허가사항 문서에서 허가 적응증, 경고, 금기 정보 확보
- DrugBank 등에서 작용 기전(MOA) 데이터 확보
- 켈로이드성 여드름 등 phenol 필링과 관련된 후보에 대해 phenol 특이적 문헌 및 임상 근거 추가 검토
- 투여 경로 적합성 및 전신/국소 독성에 대한 평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

