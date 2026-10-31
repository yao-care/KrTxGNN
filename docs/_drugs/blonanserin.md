---
layout: default
title: Blonanserin
parent: 모델 예측만 (L5)
nav_order: 152
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-31
description: "Blonanserin: 예측 신규 적응증 망막 이영양증 (retinal dystrophy with or without extraocular anomalies) (근거 수준 L5). 기존 적응증: 조현병 (한국 허가 적응증 원문은 확인되지 않았으며, 데이터베이스상 임상 용도 정보에 근거함)"
monitor_inn: "BLONANSERIN"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "congenital disorder of glycosylation with defective fucosylation", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "hydranencephaly (disease)", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "syndromic myopia", "myopia X-linked", "atypical glycine encephalopathy", "myopia 26, X-linked, female-limited"]
---

# Blonanserin
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

## Blonanserin: 조현병에서 망막 이영양증으로
{: .text-alpha }

## 한 문장 요약

Blonanserin은 도파민 D2 및 세로토닌 5-HT2A 수용체를 차단하는 약물로, 원래 조현병 치료에 사용되었습니다.
TxGNN 모델은 **망막 이영양증(retinal dystrophy with or without extraocular anomalies)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험은 0건**, **문헌도 0편**입니다.
현재로서는 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 조현병 (한국 허가 적응증 원문은 확인되지 않았으며, 데이터베이스상 임상 용도 정보에 근거함) |
| 예측 신규 적응증 | 망막 이영양증 (retinal dystrophy with or without extraocular anomalies) |
| TxGNN 예측 점수 | 0.9998 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 8건 / 전체 8건) |
| 허가증 수 | 8건 (유효 8건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 약리학 데이터에 따르면 blonanserin은 도파민 D2 수용체(DRD2)와 세로토닌 5-HT2A 수용체(HTR2A)에 작용하는 약물이며, 일본에서 조현병 치료제로 승인되어 있습니다.

그러나 기존 적응증(조현병)과 예측 적응증(유전성 망막 이영양증) 사이에서 확립된 기전적 연결고리는 없습니다. 유전성 망막 이영양증은 주로 광수용체 또는 망막색소상피 기능에 관여하는 단일 유전자 결함으로 발생하며, 수용체 길항제가 질병 경과를 바꿀 것이라는 근거는 없습니다.

TxGNN 점수(0.9998)는 TxGNN 모델(딥러닝)이 산출한 값으로, 관련 질환 간에 모델이 학습한 유사성을 반영할 수 있으며 생물학적 근거는 아닙니다. 따라서 이 예측은 가설 수준으로만 해석해야 합니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201901254 | 로나큐정2밀리그램(블로난세린) | 정제 (흰색 원형) | 허가사항 원문 참조 |
| 201900776 | 로나큐정8밀리그램(블로난세린) | 정제 (흰색 원형) | 허가사항 원문 참조 |
| 201504175 | 로나센정8밀리그램(블로난세린) | 정제 (흰색 원형) | 허가사항 원문 참조 |
| 201707313 | 파마블로난세린정8밀리그램 | 정제 (흰색 원형) | 허가사항 원문 참조 |
| 201901253 | 로나큐정4밀리그램(블로난세린) | 정제 (흰색 원형) | 허가사항 원문 참조 |

이 외에 3건의 허가가 더 있어 총 8건이 모두 단일 성분 제제로 유효합니다.

## 안전성 고려사항

- **약물 상호작용**: 약리학 데이터상 blonanserin은 5-HT2A 수용체(HTR2A)와 D2 수용체(DRD2)에 작용합니다. 이는 표적 수용체 정보이며, 개별 약물 간 상호작용 등급 정보는 아닙니다.

그 외 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측된 신규 적응증에 대한 임상시험과 문헌이 전혀 없고, 기전적 연결고리도 확립되어 있지 않습니다. 같은 모델이 제시한 상위 9개 예측 모두 근거 수준이 L5이며, 일부(근시 관련)는 도파민 길항이라는 약리 방향이 가설과 반대일 가능성도 있습니다.

**진행하려면 필요한 것:**
- 상세한 약물 작용 기전(MOA) 데이터 확보
- 한국 허가사항(경고·금기·적응증) 원문 확인 및 분석
- 망막 이영양증과 도파민/세로토닌 신호 사이의 기전적 연관성에 대한 전임상 근거
- 관련 임상시험 및 문헌 근거 확보 전까지 추가 개발 보류
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

