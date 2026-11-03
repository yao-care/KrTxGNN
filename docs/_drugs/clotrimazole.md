---
layout: default
title: Clotrimazole
parent: 모델 예측만 (L5)
nav_order: 230
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-03
monitor_inn: "CLOTRIMAZOLE"
predicted_indications: ["acne (disease)", "postmenopausal atrophic vaginitis"]
description: "Clotrimazole: 예측 신규 적응증 여드름 (acne (disease)) (acne (disease)) (근거 수준 L5). 기존 적응증: 이 약은 피부사상균, 효모 곰팡이, 기타 진균에 의한 피부진균증(백선, 어루러기, 피부칸디다증…"
---

# Clotrimazole
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **2** 건
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

## Clotrimazole: 여드름 (acne (disease)) (acne (disease))
{: .text-alpha }

## 한 문장 요약

Clotrimazole은 아졸계 항진균제로, 한국에서 국소·질 투여 제형으로 시판되고 있습니다. TxGNN 모델은 **여드름(acne (disease))**에 효과가 있을 수 있다고 예측하지만, 직접 뒷받침하는 근거는 복합제를 대상으로 한 **1건의 임상시험**(중단됨)뿐이며 문헌은 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 이 약은 피부사상균, 효모 곰팡이, 기타 진균에 의한 피부진균증(백선, 어루러기, 피부칸디다증, 칸디다성 외음염 및 칸디다성 귀두염), 상기 진균류에 중복감염된 피부질환, 코리네박테륨에 의한 홍색음선에 사용합니다.; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/197500236/EE; 이 약은 칸디다성 질염에 사용합니다.; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198400021/EE; 이 약은 무좀, 완선(사타구니백선), 체부백선에 사용합니다.; ht |
| 예측 신규 적응증 | 여드름 (acne (disease)) (acne (disease)) |
| TxGNN 예측 점수 | 0.9986 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 19건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 확보되지 않았습니다. 일반적으로 clotrimazole은 진균의 CYP51(lanosterol 14-alpha-demethylase)을 억제하는 아졸계 항진균제로 알려져 있으며, 시험관 내에서 일부 항균 및 항염 활성도 보고되어 있습니다.

여드름과의 연결은 간접적입니다. Malassezia나 Cutibacterium acnes에 대한 작용, 국소 염증 완화를 통해 영향을 줄 가능성이 있습니다. 그러나 여드름에 대한 직접적인 기전 근거나 임상 근거는 없으며, 높은 예측 점수는 계산에 의한 예측일 뿐입니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | 중단(Suspended) | 80 | beclomethasone + gentamicin + clotrimazole 3종 복합 크림의 효능 비교. 결과 미공개 |

이 시험은 스테roid와 항생제가 함께 들어 있어 clotrimazole 단독 효과를 판단할 수 없습니다. 제목이 잘려 있어 대상 질환이 여드름인지도 확정하기 어렵습니다. 따라서 여드름 자체를 직접 다룬 시험으로 인정하기 어렵습니다.

## 한국 시판 정보

허가 목록은 일부만 수집되었을 수 있습니다. 주요 허가 5건은 다음과 같습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 198400401 | 카마졸크림 | 백색 크림제 | 피부사상균, 효모 곰팡이, 기타 진균에 의한 피부진균증(백선, 어루러기, 피부칸디다증, 칸디다성 외음염 및 칸디다성 귀두염), 상기 진균류에 중복감염된 피... |
| 201508135 | 로마졸질정100mg | 질정제 | 칸디다성 질염 |
| 200008589 | 카네스텐1질정 | 질정 | 칸디다성 질염 |
| 199906850 | 카네스텐크림 | 크림 | 피부사상균, 효모 곰팡이, 기타 진균에 의한 피부진균증(백선, 어루러기, 피부칸디다증, 칸디다성 외음염 및 칸디다성 귀두염), 상기 진균류에 중복감염된 피... |
| 201506002 | 카네덤플러스크림 | 크림제 | 염증, 가려움 및 습진 등의 임상증상을 수반하는 피부 진균증(백선, 피부 칸디다증, 어루러기) |

## 안전성 고려사항

- **약물 상호작용**: 수집된 상호작용 자료 100건 중 일부를 보면, fentanyl, alfentanil, hydrocodone, amiodarone과는 Major 등급 상호작용이 있습니다. abemaciclib, paclitaxel, nifedipine, amlodipine, apixaban, aprepitant, estradiol, levonorgestrel 등과는 Moderate 등급 상호작용이 보고되어 있습니다.

그 밖의 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 여드름을 직접 다룬 근거는 복합제 대상의 중단된 시험 1건뿐이고 문헌도 없어, 모델 예측 수준(L5)에 머물러 있습니다.

**진행하려면 필요한 것:**
- clotrimazole 단독 제제의 여드름 대상 임상시험 또는 문헌
- 작용 기전 데이터 확보
- 허가사항의 경고·금기 정보 확인

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

