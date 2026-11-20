---
layout: default
title: Omalizumab
parent: 모델 예측만 (L5)
nav_order: 563
evidence_level: L5
indication_count: 9
monitor_inn: "Omalizumab"
predicted_indications: ["bronchitis", "atopic eczema", "dermatitis", "bronchial neoplasm (disease)", "acne keloid", "acrodermatitis chronica atrophicans", "hydroa vacciniforme, familial", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease"]
last_modified_at: 2026-11-20
description: "Omalizumab: 예측 신규 적응증 기관지염 (bronchitis) (근거 수준 L5). 기존 적응증: 1. 알레르기성 천식 (Allergic Asthma) ○ 성인 및 청소년 (12세 이상) 다음 증상을…"
---

# Omalizumab
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

## Omalizumab: 기관지염 (bronchitis)
{: .text-alpha }

## 한 문장 요약

Omalizumab은 유리 IgE에 결합하는 항IgE 단클론항체입니다. TxGNN 모델은 **기관지염(bronchitis)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 연구한 근거는 확인되지 않았습니다. 이 방향과 관련된 자료는 임상시험 2건과 문헌 7편이지만, 기관지염에서 효능을 뒷받침하는 연구는 없어 근거 수준은 **L5**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 알레르기성 천식 (Allergic Asthma) ○ 성인 및 청소년 (12세 이상) 다음 증상을 동반하는 성인 및 청소년(12세 이상) 알레르기성 천식 환자에 있어서 천식 조절을 개선하기 위 한 추가 요법제. 1. 통년성 대기 알러젠에 대하여 시험관 내(in vitro) 반응… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201602975/EE)) |
| 예측 신규 적응증 | 기관지염 (bronchitis) |
| TxGNN 예측 점수 | 1.0000 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 5건 / 전체 6건) |
| 허가증 수 | 6건 (유효 5건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Omalizumab 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “천식, 비용종을 동반한 만성 비부비동염 및 IgE 매개 식품 알레르기 오말리주맙 제제는 비만세포, 호염기구 및 수지상세포 표면의 고친화성 IgE 수용체(FcεRI)에 대한 IgE의 결합을 억제하여, 이들 세포에서 FcεRI의 하향조절을 초래한다. 알레르기성 천식 환자에서 오말리주맙 제제 투여는 혈액 및 조직 호산구 감소와 IL-4, IL-5 및 IL-13을 포함한 염증 매개체의 감소로 입증되는 바와 같이 IgE 매개 염증을 억제한다.” 영어 원문: "Asthma, Chronic Rhinosinusitis with Nasal Polyps, and IgE-Mediated Food Allergy Omalizumab products inhibit the binding of IgE to the high-affinity IgE receptor (FcεRI) on the surface of mast cells, basophils, and dendritic cells, resulting in FcεRI down-regulation on these cells. In allergic asthmatics, treatment with omalizumab products inhibit IgE-mediated inflammation, as evidenced by reduced blood and tissue eosinophils and reduced inflammatory mediators, including IL-4, IL-5, and IL-13." ([DailyMed: Omlyclo (omalizumab-igec) prescribing information, CELLTRION USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=dbd8709f-1636-45d9-ba94-5a3bc5f22f84), 버전 2026-10-06; 확인일 2026-11-19). 알려진 정보로는 omalizumab이 유리 IgE에 결합해 혈중 IgE를 낮추고, 비만세포와 호염기구의 FcεRI 매개 활성화를 줄입니다. 이 작용은 알레르기성 기도 염증과 관련이 있어, IgE가 주도하는 기도 질환에서는 기전상 적용 가능성을 생각해 볼 수 있습니다.

다만 이 연결은 간접적입니다. 기관지염에 관한 자료는 대부분 천식 환자군이나 기도질환 전반을 다룬 연구에서 나왔고, 기관지염 자체를 정의된 질환으로 평가한 연구는 아닙니다. 따라서 IgE가 병태를 주도하는 특정 표현형에서만 가설이 성립할 수 있으며, 높은 예측 점수만으로 효능을 뒷받침하기는 어렵습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | 완료 | 11 | 지속성 호산구성 기관지염 환자에서 omalizumab의 스테로이드 절감 효과를 보는 이중맹검 위약대조 시험입니다. 실제 보고된 대상은 지속적인 객담 호산구증가를 동반한 중증 천식 환자였고, omalizumab의 효과는 충분하지 않았을 가능성이 있습니다. 규모가 매우 작아 기관지염 근거로 쓰기 어렵습니다. |
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Phase 2 | 완료 | 382 | 만성 자발성 두드러기 환자 대상 QGE031 용량탐색 시험입니다. 기관지염 대상이 아니어서 간접 근거일 뿐입니다. |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Review | Clin Rev Allergy Immunol | 중등도~중증 지속성 천식에서 omalizumab의 효능과 허가 후 경험을 정리했습니다. 기관지염은 다루지 않습니다. |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Review | Expert Opin Pharmacother | 만성 기관지염 등 흡연 관련 기도질환을 동반한 천식 환자의 치료 과제를 논의했습니다. 이런 환자는 대부분의 임상시험에서 제외되어 약물 치료의 불확실성이 큽니다. |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Review | Masui | 기관지 천식 또는 만성 기관지염 환자의 수술 전 관리를 다룹니다. omalizumab은 치료 선택지로만 언급됩니다. |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Case report | J Investig Allergol Clin Immunol | 기관지 열성형술 후 발생한 플라스틱 기관지염 1례입니다. 효능 근거는 아닙니다. |
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | 안전성 분석 | Curr Med Res Opin | 알레르기성 천식 소아에서 omalizumab의 안전성과 내약성을 통합 분석했습니다. |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | Review | Allergol Immunopathol | 소아에서 단클론항체의 예방·치료 활용을 개괄했습니다. 기관지염 특이 근거는 없습니다. |

## 한국 시판 정보

유효한 허가증 5건 중 제품별 정보입니다. 허가 적응증 원문은 텍스트가 아닌 허가정보 링크로만 확인되며, 별도로 취소된 허가증이 1건 있습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201602975 | 졸레어프리필드시린지주150 | 프리필드시린지 주사제 | 허가 문서 링크만 확인됨 |
| 200706212 | 졸레어주사 | 동결건조분말 주사제 (첨부용제 포함) | 허가 문서 링크만 확인됨 |
| 201704778 | 졸레어프리필드시린지주75 | 프리필드시린지 주사제 | 허가 문서 링크만 확인됨 |
| 202400492 | 졸레어프리필드시린지주300 | 프리필드시린지 주사제 | 허가 문서 링크만 확인됨 |
| 202503335 | 옴리클로펜주 | 자동주사기 펜 | 허가 문서 링크만 확인됨 |

## 안전성 고려사항

- **약물 상호작용**: 총 8건이 확인되었습니다.
  - 중등도: omacetaxine mepesuccinate
  - 경미: 황산아연, 아세트산아연, 글루콘산아연, 염화아연, 에키네시아, 비타민 E
  - 이 밖에 omalizumab이 IgE(IGHE)를 표적으로 하는 항체라는 약리학 정보가 있습니다.
- 허가사항의 경고 및 금기는 이번에 정리된 자료에 없으므로 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
기관지염에서 omalizumab의 효능을 직접 뒷받침하는 연구가 없습니다. 관련 시험은 소규모이고 대상이 천식 환자였으며, 효과가 충분하지 않았을 가능성도 있습니다. 문헌은 대부분 천식을 다룬 리뷰입니다. 예측 점수가 높아도 근거 수준은 L5이므로 현 단계에서는 보류를 권고합니다.

**진행하려면 필요한 것:**
- IgE 주도 표현형의 기관지염 환자를 정의하고, 대상 집단을 설정하는 근거 확보
- 기관지염을 직접 평가하는 임상시험 또는 관찰 연구 자료
- 상세한 작용 기전(MOA) 데이터와 기관지염 병태와의 기전적 연결 분석
- 허가사항의 경고 및 금기 정보 확인

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Omlyclo (omalizumab-igec) prescribing information, CELLTRION USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=dbd8709f-1636-45d9-ba94-5a3bc5f22f84) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

