---
layout: default
title: Ustekinumab
parent: 모델 예측만 (L5)
nav_order: 775
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ustekinumab: 예측 신규 적응증 피부염 (Dermatitis) (근거 수준 L5). 기존 적응증: 허가 적응증 원문이 링크로만 제공되어 구체적인 질환명을 확인할 수 없음 (MFDS 허가 문서 참조)"
monitor_inn: "USTEKINUMAB"
predicted_indications: ["dermatitis", "neonatal dermatomyositis", "acne keloid", "acrodermatitis chronica atrophicans", "amyopathic dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "hydroa vacciniforme, familial", "severe nonproliferative diabetic retinopathy", "pityriasis lichenoides", "acute lichenoid pityriasis"]
---

# Ustekinumab
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

# Ustekinumab: 건선·크론병 등 기존 적응증에서 피부염으로

## 한 문장 요약

Ustekinumab은 IL-12/IL-23의 공통 p40 소단위를 차단하는 단클론항체로, 한국에서 여러 제품으로 허가·시판되고 있습니다. TxGNN 모델은 **피부염(dermatitis)**에 효과가 있을 수 있다고 예측하며(점수 99.99%), 현재 **6건의 임상시험**과 **20편의 문헌**이 검토되었습니다. 다만 직접 관련된 근거는 아토피피부염 대상 Phase 2 시험 2건에 한정되며, 효능은 설득력 있게 입증되지 않았습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 원문이 링크로만 제공되어 구체적인 질환명을 확인할 수 없음 (MFDS 허가 문서 참조) |
| 예측 신규 적응증 | 피부염 (Dermatitis) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L2 (완료된 Phase 2 무작위 시험이 있으나 효능이 불충분하여 보수적으로 해석) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 8건 |
| 권장 결정 | Hold (연구 질문 단계) |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 DrugBank에 없습니다. 알려진 정보에 따르면 ustekinumab은 인간 IL-12/IL-23 길항 단클론항체로, 두 사이토카인이 공유하는 p40 소단위를 차단해 Th1·Th17 경로를 억제합니다.

아토피피부염은 Th2 축이 중심이지만, 만성 병변, 아시아인 환자, 소아 환자에서는 Th22와 Th17/Th1 활성도 일부 관여합니다. 접촉피부염과 홍피증성 건선도 Th1/Th17이 부분적으로 관여합니다. 따라서 기전상 적용 가능성은 있으나 근거는 약한 편입니다.

아토피피부염 Phase 2 시험 2건이 완료되었지만, 성인 대상 발표 결과(PMID 27304428)는 Th2 표적 약제(dupilumab, IL-13 억제제)에 비해 설득력 있는 효능을 보이지 못했습니다. 높은 TxGNN 점수는 건선 관련 피부과 맥락의 영향을 일부 받은 것으로 보이므로 신중한 해석이 필요합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01945086](https://clinicaltrials.gov/study/NCT01945086) | Phase 2 | 완료 | 79 | 일본인 중증 아토피피부염에서 ustekinumab 2개 용량 vs 위약, 무작위 이중맹검 (가장 강력한 대조 근거) |
| [NCT01806662](https://clinicaltrials.gov/study/NCT01806662) | Phase 2 | 완료 | 32 | 이전 치료에 반응이 불충분한 만성 아토피피부염 대상 무작위 파일럿 연구 |
| [NCT05535738](https://clinicaltrials.gov/study/NCT05535738) | Phase 2/3 | 활성, 모집 종료 | 45 | 생물학적 제제(ustekinumab 포함)를 이용한 접촉피부염 모델 연구, 기전 연구 성격 |
| [NCT02074982](https://clinicaltrials.gov/study/NCT02074982) | Phase 3 | 완료 | 676 | 판상 건선에서 secukinumab vs ustekinumab 비교 (피부염 직접 근거 아님) |
| [NCT01356758](https://clinicaltrials.gov/study/NCT01356758) | 해당 없음 | 완료 | 126 | 중증 건선 환자의 생물학적 제제 치료 중 심혈관 위험 평가 (효능 근거 아님) |
| [NCT07352566](https://clinicaltrials.gov/study/NCT07352566) | Phase 4 | 모집 예정 | 10 | 피부 내 약물 시험용 초소형 장치 연구 (기술 연구, 효능 자료 없음) |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [27304428](https://pubmed.ncbi.nlm.nih.gov/27304428/) | 2017 | RCT (Phase 2) | Exp Dermatol | 중등도~중증 아토피피부염 성인 33명 대상 이중맹검 위약대조 연구 |
| [28338223](https://pubmed.ncbi.nlm.nih.gov/28338223/) | 2017 | RCT (Phase 2) | Br J Dermatol | 일본인 중증 아토피피부염에서 ustekinumab의 효능·안전성 평가 |
| [32927498](https://pubmed.ncbi.nlm.nih.gov/32927498/) | 2020 | 네트워크 메타분석 | Cochrane Database Syst Rev | 습진 전신치료제 간 상대적 효과 비교 |
| [33074565](https://pubmed.ncbi.nlm.nih.gov/33074565/) | 2021 | 체계적 문헌고찰·메타분석 | Allergy | 중등도~중증 아토피피부염 전신치료 근거 평가 (EAACI 지침용) |
| [29164954](https://pubmed.ncbi.nlm.nih.gov/29164954/) | 2018 | 체계적 문헌고찰 | J Dermatolog Treat | 아토피피부염에서 ustekinumab의 효능·안전성 평가 |
| [29098604](https://pubmed.ncbi.nlm.nih.gov/29098604/) | 2018 | 체계적 문헌고찰·메타분석 | Am J Clin Dermatol | 아토피피부염에서 생물학적 제제의 효능 평가 |
| [33849369](https://pubmed.ncbi.nlm.nih.gov/33849369/) | 2022 | 실제 임상 근거 분석 | J Dermatolog Treat | 아토피피부염에서 ustekinumab의 실제 효과, 일화적 보고는 결과가 상충 |
| [36208443](https://pubmed.ncbi.nlm.nih.gov/36208443/) | 2022 | Review | Dermatol Ther | ustekinumab의 허가 외 사용 문헌 종합 |
| [32347968](https://pubmed.ncbi.nlm.nih.gov/32347968/) | 2020 | Review | Contact Dermatitis | 알레르기 접촉피부염에서 생물학적 제제 사용 자료 검토 |
| [32172523](https://pubmed.ncbi.nlm.nih.gov/32172523/) | 2020 | Review | Clin Drug Investig | 임상시험에서 실패한 아토피피부염 치료제의 실패 원인 분석 |

## 한국 시판 정보

허가 적응증 원문은 MFDS 허가 문서 링크로만 제공되어 본문 요약이 불가능합니다. 각 허가번호의 허가 문서를 참조하세요.

| 허가번호 | 제품명 | 제형 | 제조사 |
|---------|------|------|--------|
| 202401434 | 스테키마프리필드주 | 프리필드시린지 주사제 | (주)셀트리온 |
| 201607286 | 스텔라라피하주사 | 바이알 주사제 | (주)한국얀센 |
| 202402336 | 스테키마정맥주사 | 바이알 주사제 | (주)셀트리온 |
| 201801521 | 스텔라라정맥주사 | 바이알 주사제 | (주)한국얀센 |
| 201103892 | 스텔라라프리필드주 | 프리필드시린지 주사제 | (주)한국얀센 |

이 외에 삼성바이오에피스의 에피즈텍 3개 제품(프리필드주, 프리필드펜주, 정맥주사)이 허가되어 총 8건이 유효합니다.

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 주요 항목은 다음과 같습니다.
  - 중등도: 코르티코스테로이드 계열(hydrocortisone, prednisone, prednisolone, dexamethasone, betamethasone, triamcinolone, budesonide), simvastatin, 항응고제(warfarin, apixaban, rivaroxaban, dicoumarol), 방사성의약품(iobenguane I-131, ibritumomab tiuxetan, tositumomab)
  - 경미: 아연 제제(zinc sulfate, acetate, gluconate, chloride)
- **참고**: 면역억제 작용으로 감염 위험이 있으므로, 소아·신생아 등 취약 집단에서는 특히 주의가 필요합니다. 경고·금기 등 그 밖의 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold (연구 질문 단계)**

**사유:**
아토피피부염에서 완료된 Phase 2 시험 2건이 있으나, 성인 대상 발표 결과는 Th2 표적 약제에 비해 설득력 있는 효능을 보이지 못했습니다. 높은 TxGNN 점수도 건선 관련 맥락의 영향을 받았을 가능성이 있어, 현재로서는 임상 도입보다 추가 연구 질문으로 다루는 것이 적절합니다.

**진행하려면 필요한 것:**
- MFDS 허가사항(경고·금기·허가 적응증)을 확보하여 안전성 검토 진행 (현재 안전성 선별을 진행할 수 없는 상태)
- 상세한 작용 기전(MOA) 데이터 보완 (DrugBank 조회)
- 아토피피부염 Phase 2 결과의 재분석, 그리고 Th17/Th22 우세 하위집단(만성 병변, 아시아인, 소아)에 대한 표적 임상시험 설계 검토
- 접촉피부염 등 하위 유형별로 근거를 구분하여 평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

