---
layout: default
title: Omalizumab
parent: 모델 예측만 (L5)
nav_order: 563
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Omalizumab: 예측 신규 적응증 기관지염 (Bronchitis) (근거 수준 L5). 기존 적응증: 중등증~중증 IgE 매개 지속성 천식…"
monitor_inn: "Omalizumab"
predicted_indications: ["bronchitis", "atopic eczema", "obstructive lung disease", "dermatitis", "bronchial neoplasm (disease)", "acne keloid", "acrodermatitis chronica atrophicans", "hydroa vacciniforme, familial"]
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

# Omalizumab: 알레르기성 천식에서 기관지염으로

## 한 문장 요약

Omalizumab은 항-IgE 단클론항체로, 원래 중등증~중증 IgE 매개 지속성 천식과 만성 특발성(자발성) 두드러기 치료에 사용되었습니다.
TxGNN 모델은 **기관지염(bronchitis)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 지지하는 근거는 **2건의 임상시험**과 **7편의 문헌**에 그치며 모두 간접 근거입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 중등증~중증 IgE 매개 지속성 천식, 만성 특발성 두드러기 (한국 허가 적응증 원문은 이번 데이터에서 확인되지 않아 약리학 데이터 기준으로 기재) |
| 예측 신규 적응증 | 기관지염 (Bronchitis) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L4 (간접·기전 근거 수준) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 6건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

Omalizumab은 유리 IgE에 결합해 IgE가 비만세포·호염기구의 FcεRI 수용체에 결합하는 것을 막고, 이들 세포의 수용체 발현도 낮춥니다. 그 결과 알레르기성 기도 염증이 줄어듭니다. 이 약의 약리학적 표적은 IgE 중쇄(IGHE)입니다.

기관지염과의 연관성은 간접적입니다. 천식 및 천식-COPD 중복 환자에서 만성 기관지염이 동반 표현형으로 나타나기 때문에 TxGNN이 이를 연결했을 가능성이 있습니다. 기관지염 자체를 표적으로 한 시험은 없습니다.

따라서 기전상 알레르기·호산구성 기도 염증이 있는 일부 환자군에서는 적용 가능성이 있지만, 일반적인 감염성·만성 기관지염 전반으로 확대할 근거는 없습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | 완료 | 11 | 지속성 호산구성 기관지염을 동반한 천식 환자에서 omalizumab의 스테로이드 절감 효과를 평가한 이중맹검 위약대조 시험. 소규모이고 천식·알레르기성 기도 집단에 가까워 기관지염 직접 근거로는 제한적 |
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Phase 2 | 완료 | 382 | 만성 자발성 두드러기에서 QGE031의 용량탐색 시험(omalizumab은 대조약). 기관지염 집단이 아니므로 관련성 간접적 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | 코호트 | Postepy Dermatol Alergol | 중증 알레르기성 천식-COPD 중복 환자(중장년·고령)에서 omalizumab 등 생물학적 제제의 유용성 시사 |
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | 안전성 통합분석 | Curr Med Res Opin | 알레르기성 천식 소아에서 omalizumab의 안전성·내약성 평가 |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | 리뷰 | Expert Opin Pharmacother | 흡연 유발 기도질환(만성 기관지염 포함)을 동반한 천식의 치료 과제 |
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | 리뷰 | Clin Rev Allergy Immunol | 천식에서 omalizumab의 허가 및 시판 후 경험 |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | 리뷰 | Masui | 기관지 천식·만성 기관지염 환자의 수술 전 관리(일본어). omalizumab이 중증 알레르기성 천식에 사용 가능함을 언급 |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | 리뷰 | Allergol Immunopathol | 소아 단클론항체의 예방·치료 활용 개관 |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | 증례 보고 | J Investig Allergol Clin Immunol | 기관지 온열성형술 후 발생한 플라스틱 기관지염 증례 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201602975 | 졸레어프리필드시린지주150 (한국노바티스) | 프리필드시린지 주사제 | [허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201602975/EE) 참조 |
| 200706212 | 졸레어주사 (한국노바티스) | 동결건조분말 바이알 주사제 | [허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200706212/EE) 참조 |
| 201704778 | 졸레어프리필드시린지주75 (한국노바티스) | 프리필드시린지 주사제 | [허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201704778/EE) 참조 |
| 202400492 | 졸레어프리필드시린지주300 (한국노바티스) | 프리필드시린지 주사제 | [허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202400492/EE) 참조 |
| 202503335 | 옴리클로펜주 (셀트리온) | 자동주사기 펜(피하투여) | [허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202503335/EE) 참조 |

이 외에 옴리클로프리필드시린지주(셀트리온, 허가번호 202401521)가 있어 총 6건이 유효합니다.

## 안전성 고려사항

- **약물 상호작용**: 총 8건이 확인되었습니다.
  - 중등도: Omacetaxine mepesuccinate
  - 경미: 아연 제제(황산아연, 아세트산아연, 글루콘산아연, 염화아연), Echinacea, 비타민 E
  - 약리학적 표적 상호작용: IgE 중쇄(IGHE) 결합(작용 기전 자체에 해당)

그 외 경고·금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
기관지염을 직접 표적으로 한 시험은 없습니다. 유일한 Phase 2/3 시험은 11명 규모이고 천식 및 호산구성 기도 질환 집단이어서 간접 근거에 그칩니다. 문헌도 대부분 천식 중심의 리뷰입니다. 본 예측은 기전 수준(L4)의 가설로 보는 것이 적절합니다.

**진행하려면 필요한 것:**
- 알레르기·호산구성 표현형을 가진 기관지염 환자군을 정의하는 가설 수립 (천식·천식-COPD 중복 환자의 하위군 분석 포함)
- 해당 표현형에서 효능을 검증하는 대조 임상시험 또는 후향 코호트 근거
- 한국 허가사항 원문(적응증, 경고, 금기)의 확보 및 분석
- 상세 작용 기전 데이터 보완

참고로 같은 약물의 다른 예측 적응증 중 알레르기성 천식과 폐쇄성 폐질환(COPD)은 근거 수준 L1로 평가되어 "Proceed with Guardrails"가 권고됩니다. 다만 알레르기성 천식은 이미 승인된 적응증이므로 재창출 후보로서 의미가 있는지는 별도로 검토해야 합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

