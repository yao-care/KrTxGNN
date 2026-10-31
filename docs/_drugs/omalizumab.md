---
layout: default
title: Omalizumab
parent: 모델 예측만 (L5)
nav_order: 563
evidence_level: L5
indication_count: 10
monitor_inn: "Omalizumab"
predicted_indications: ["bronchitis", "atopic eczema", "obstructive lung disease", "dermatitis", "bronchial neoplasm (disease)", "acne keloid", "acrodermatitis chronica atrophicans", "hydroa vacciniforme, familial", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease"]
last_modified_at: 2026-10-31
description: "Omalizumab: 예측 신규 적응증 기관지염 (근거 수준 L5). 기존 적응증: 허가증에는 적응증 본문 없이 허가 문서 링크만 있어 한국 허가 적응증은 확인되지 않았습니다. 약리학 자료상 사용례는 알레르기…"
---

# Omalizumab
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

## Omalizumab: 알레르기성 천식에서 기관지염으로
{: .text-alpha }

## 한 문장 요약

Omalizumab은 IgE에 결합하는 항체 의약품으로, 약리학 자료에는 중등증~중증 알레르기성 천식과 만성 특발성(자발성) 두드러기 치료에 쓰이는 것으로 기재되어 있습니다.
TxGNN 모델은 **기관지염(bronchitis)**에 효과가 있을 수 있다고 예측합니다.
다만 이 방향을 직접 뒷받침하는 근거는 거의 없습니다. 관련 임상시험은 2건(기관지염 직접 관련은 1건, 11명 규모)이고, 문헌 7편은 대부분 천식 또는 천식-COPD 중복 환자를 다룹니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에는 적응증 본문 없이 허가 문서 링크만 있어 한국 허가 적응증은 확인되지 않았습니다. 약리학 자료상 사용례는 알레르기성 천식, 만성 특발성 두드러기입니다. |
| 예측 신규 적응증 | 기관지염 |
| TxGNN 예측 점수 | 1.0000 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 5건 / 전체 6건) |
| 허가증 수 | 6건 (유효 5건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

이 보고서에 수집된 데이터에는 상세한 작용 기전 자료가 없습니다. 약리학 자료상 omalizumab은 IgE(IGHE)를 표적으로 하는 항체입니다. 일반적으로 유리 IgE에 결합해 비만세포와 호염기구의 FcεRI 매개 활성화를 줄이고, 알레르기성 기도 염증을 완화하는 것으로 이해됩니다.

기관지염과의 연관성은 간접적입니다. 지지 근거는 주로 천식과 천식-COPD 중복 환자에서 나온 것이며, 기관지염 자체를 대상으로 한 것이 아닙니다. 따라서 IgE가 주도하는 알레르기성 또는 호산구성 표현형을 가진 환자에서만 타당성이 있을 수 있습니다. 높은 TxGNN 점수는 TxGNN 모델(딥러닝)에서 나온 것으로, 기도 질환 등 관련 질환 간에 모델이 학습한 유사성을 반영한 것일 수 있으며 생물학적 근거는 아닙니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | 완료 | 11 | 천식과 호산구성 기관지염 환자에서 omalizumab 추가 시 prednisone 감량 효과를 보는 이중맹검 위약대조 시험입니다. 규모가 매우 작고 결과가 제시되지 않았으며 대상이 천식 환자라 간접적입니다. |
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Phase 2 | 완료 | 382 | 만성 자발성 두드러기에서 QGE031(후속 항IgE 후보)의 용량 탐색 시험입니다. 기관지염과는 직접 관련이 없습니다. |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Review | Clin Rev Allergy Immunol | 중등증~중증 지속성 천식에서 omalizumab의 효능과 허가 후 경험을 정리했습니다. |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Review | Expert Opin Pharmacother | 만성 기관지염 등 흡연 관련 기도질환이 동반된 천식 관리의 어려움을 다뤘습니다. 이런 환자는 대부분 임상시험에서 제외됩니다. |
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | 코호트 | Postepy Dermatol Alergol | 중장년 이상의 중증 알레르기성 천식-COPD 중복 환자에서 생물학적 치료가 유용할 수 있음을 보였습니다. |
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | 통합 안전성 분석 | Curr Med Res Opin | 알레르기성 천식 소아에서 omalizumab의 안전성과 내약성을 분석했습니다. |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Review | Masui | 기관지 천식·만성 기관지염 환자의 수술 전 관리를 다뤘고, omalizumab을 중증 알레르기성 천식 치료 선택지로 언급했습니다. |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | Review | Allergol Immunopathol | 소아에서 단클론항체의 예방·치료 활용을 개괄했습니다. |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | 증례 보고 | J Investig Allergol Clin Immunol | 기관지 열성형술 후 발생한 plastic bronchitis 사례입니다. 초록이 없어 omalizumab 효과 여부는 확인되지 않습니다. |

## 한국 시판 정보

허가 적응증 본문은 이 보고서에 수집된 데이터에 없습니다. 각 허가증에는 식약처 허가 문서 링크만 있어 적응증 확인이 필요합니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201602975 | 졸레어프리필드시린지주150 | 프리필드시린지 주사제 | 허가 문서 링크만 확인됨 |
| 200706212 | 졸레어주사 | 동결건조분말 주사제 (첨부용제 포함) | 허가 문서 링크만 확인됨 |
| 201704778 | 졸레어프리필드시린지주75 | 프리필드시린지 주사제 | 허가 문서 링크만 확인됨 |
| 202400492 | 졸레어프리필드시린지주300 | 프리필드시린지 주사제 | 허가 문서 링크만 확인됨 |
| 202503335 | 옴리클로펜주 | 자동주사기 펜 | 허가 문서 링크만 확인됨 |

이 외에 옴리클로프리필드시린지주(202401521)가 있어 허가증은 총 6건입니다. 졸레어 4건은 한국노바티스, 옴리클로 2건은 셀트리온 제품입니다.

## 안전성 고려사항

- **약물 상호작용 (총 8건)**
  - 보통(Moderate): Omacetaxine mepesuccinate
  - 경미(Minor): 황산아연, 아세트산아연, 글루콘산아연, 염화아연, Echinacea, 비타민 E
  - 약리학 자료상 표적 IgE(IGHE) 항체 관계도 기재되어 있습니다.

경고와 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
기관지염에 대한 직접 근거는 규모가 매우 작은 호산구성 기관지염 시험(n=11, 결과 미확인) 1건뿐입니다. 문헌도 대부분 천식 또는 천식-COPD 중복 환자를 다루어 효능 입증이 부족합니다. 근거 수준은 L5로 판단합니다. 참고로 같은 예측 목록에서 아토피 피부염(atopic eczema)과 폐쇄성 폐질환(obstructive lung disease)은 더 많은 임상시험 근거가 있어 별도로 검토할 가치가 있습니다.

**진행하려면 필요한 것:**
- NCT02049294의 결과 확인과 호산구성 기관지염을 대상으로 한 추가 대조시험
- 대상 표현형(IgE 매개 알레르기성 또는 호산구성 기관지염) 정의
- 상세한 작용 기전(MOA) 데이터 확보
- 식약처 허가사항(적응증, 경고, 금기)의 확인과 정리
- 시판 상태(취소 여부) 확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

