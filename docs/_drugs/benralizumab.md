---
layout: default
title: Benralizumab
parent: 모델 예측만 (L5)
nav_order: 134
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Benralizumab: 예측 신규 적응증 피부염 (Dermatitis) (근거 수준 L5). 기존 적응증: 중증 호산구성 천식(추가 유지치료) 및 호산구성 육아종증 다발혈관염(EGPA…"
monitor_inn: "BENRALIZUMAB"
predicted_indications: ["thrombocytopenia due to immune destruction", "dermatitis", "acne keloid", "neonatal dermatomyositis", "amyopathic dermatomyositis"]
---

# Benralizumab
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **5** 건
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

# Benralizumab: 중증 호산구성 천식에서 피부염으로

## 한 문장 요약

Benralizumab(벤라리주맙)은 IL-5 수용체 알파(IL-5Rα)를 표적으로 하는 단클론항체로, 원래 중증 호산구성 천식의 추가 유지치료에 사용되었습니다.
TxGNN 모델은 **피부염(Dermatitis)**에 효과가 있을 수 있다고 예측하며(예측 점수 99.16%), 현재 **3건의 임상시험**(Phase 2)과 **20편의 문헌**(대부분 리뷰)이 이 방향과 관련되어 있습니다.
다만 Phase 3 근거는 없고, Phase 2 무작위 대조시험은 조기 종료되어 신중한 해석이 필요합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 중증 호산구성 천식(추가 유지치료) 및 호산구성 육아종증 다발혈관염(EGPA, 미국 FDA 2024년 확대 승인 기준). 한국 허가 적응증 원문은 데이터에 텍스트로 제공되지 않아 허가사항 확인이 필요합니다. |
| 예측 신규 적응증 | 피부염 (Dermatitis) |
| TxGNN 예측 점수 | 99.16% |
| 근거 수준 | L2 (Phase 2 임상시험 존재, 단 Phase 3 없음 및 무작위 대조시험 조기 종료) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold (연구 질문 단계, 추가 확인 필요) |

> 참고: 데이터상 1순위 예측은 "면역성 혈소판감소증"(점수 99.34%)이나 임상시험·문헌 근거가 전혀 없어, 근거가 있는 2순위 "피부염"을 중심으로 평가했습니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 충분히 수집되어 있지 않습니다. 알려진 정보에 따르면, Benralizumab은 IL-5Rα에 결합하여 항체 의존성 세포독성(ADCC)을 통해 호산구와 호염기구를 제거하는 단클론항체입니다. 호산구성 천식에서의 효능이 입증되어 있어, 호산구가 관여하는 다른 질환에도 기전상 적용 가능할 수 있습니다.

아토피피부염 등 2형 염증성 피부질환에서는 호산구, 호염기구, 2형 선천림프구(ILC2)가 염증에 기여합니다. 따라서 이들 세포를 줄이는 Benralizumab이 해당 경로를 조절할 가능성은 있습니다. 그러나 피부염 환자에서 효능이 입증되었다는 직접적 근거는 현재 제공된 자료에 없습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04605094](https://clinicaltrials.gov/study/NCT04605094) | Phase 2 | 조기 종료 | 194 | 중등도~중증 아토피피부염에서 16주 위약 대조, 36주 연장 시험(HILLIER). 가장 엄격한 설계이나 종료 사유 확인 필요(효능 부족 가능성) |
| [NCT03563066](https://clinicaltrials.gov/study/NCT03563066) | Phase 2 | 완료 | 20 | 아토피피부염에서 호산구·호염기구·ILC2에 대한 작용을 보는 소규모 기전 연구 |
| [NCT06734884](https://clinicaltrials.gov/study/NCT06734884) | Phase 2 | 모집 예정 | 96 | 호산구증가 동반 약물반응(DRESS)에서 효능·안전성 평가. 시작 예정 2027-01 |

## 문헌 근거

제공된 문헌은 대부분 생물학적 제제 전반을 다룬 리뷰이며, 피부염에 대한 Benralizumab 효능을 직접 입증하는 연구는 없습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [35987486](https://pubmed.ncbi.nlm.nih.gov/35987486/) | 2022 | Review | J Allergy Clin Immunol Pract | 임신 중 아토피 질환 생물학적 제제(benralizumab 포함)의 안전성 검토 |
| [39600395](https://pubmed.ncbi.nlm.nih.gov/39600395/) | 2024 | Review | Allergologie Select | 아토피 질환, 두드러기, 혈관부종 생물학적 제제 최신 동향 및 과민반응 안전성 |
| [36411004](https://pubmed.ncbi.nlm.nih.gov/36411004/) | 2023 | Review | Immunol Allergy Clin North Am | 임신·수유 중 알레르기 비염, 천식, 아토피피부염 단클론항체 사용 |
| [34642091](https://pubmed.ncbi.nlm.nih.gov/34642091/) | 2021 | Review | Ann Allergy Asthma Immunol | 천식, 두드러기, 비용종, 아토피피부염 등에서 생물학적 제제 선택 지침 |
| [31690400](https://pubmed.ncbi.nlm.nih.gov/31690400/) | 2019 | Review | Allergy Asthma Proc | 중증 천식, 아토피피부염, 만성 두드러기의 면역생물학적 치료 |
| [33236428](https://pubmed.ncbi.nlm.nih.gov/33236428/) | 2020 | Review | Pediatr Allergy Immunol | 소아 알레르기 질환에서 항IL-5 치료 |
| [37170653](https://pubmed.ncbi.nlm.nih.gov/37170653/) | 2023 | Review | Clin Transl Sci | 천식, 만성 두드러기, 아토피피부염 등 알레르기 질환 면역치료 동향 |
| [42383238](https://pubmed.ncbi.nlm.nih.gov/42383238/) | 2026 | Review | Curr Ther Res | 소아 아토피피부염 단클론항체의 효능과 안전성 |
| [38878020](https://pubmed.ncbi.nlm.nih.gov/38878020/) | 2024 | Cohort | J Allergy Clin Immunol | Benralizumab, dupilumab, mepolizumab 투여 환자에서 백신 접종 후 SARS-CoV-2 면역 저하 |
| [37259416](https://pubmed.ncbi.nlm.nih.gov/37259416/) | 2023 | Review | Pharmaceuticals (Basel) | 천식 및 알레르기 질환 생물학적 치료의 과거·현재·미래 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201903766 | 파센라프리필드시린지주30밀리그램(벤라리주맙) | 주사제(프리필드시린지) | 허가사항 원문(식약처 의약품안전나라) 참조 |

제조사는 한국아스트라제네카(주)입니다.

## 안전성 고려사항

- **약물 상호작용**: 약물 간 상호작용은 확인되지 않았으며, 약리학적 표적인 IL-5 수용체 알파 소단위(IL5RA)에 대한 결합 정보만 조회되었습니다.

그 외 경고·금기 등 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
피부염에 대해 Phase 2 시험이 있으나, 가장 엄격한 설계의 무작위 위약 대조시험(NCT04605094)이 조기 종료되었고 Phase 3 근거가 없습니다. 제공된 문헌도 대부분 리뷰로, 피부염에서의 직접적 효능 근거가 부족합니다.

**진행하려면 필요한 것:**
- NCT04605094의 종료 사유 및 결과 확인(효능 부족 여부 판단)
- NCT03563066 기전 연구의 결과 확인
- 허가사항 원문에서 경고·금기 등 안전성 정보 확보
- 상세한 작용 기전(MOA) 데이터 보완
- 아토피피부염 등 피부염 하위 유형별 효능을 평가한 근거 확보
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

