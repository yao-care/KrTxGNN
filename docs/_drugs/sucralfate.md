---
layout: default
title: Sucralfate
parent: 모델 예측만 (L5)
nav_order: 705
evidence_level: L5
indication_count: 1
monitor_inn: "SUCRALFATE"
predicted_indications: ["duodenal obstruction"]
last_modified_at: 2026-10-28
description: "Sucralfate: 예측 신규 적응증 십이지장 폐쇄 (Duodenal Obstruction) (근거 수준 L5). 기존 적응증: 확인 불가 (허가 적응증이 문서 링크로만 제공됨)"
---

# Sucralfate
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **1** 건
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

## Sucralfate: 기존 적응증에서 십이지장 폐쇄로
{: .text-alpha }

## 한 문장 요약

Sucralfate는 국소 작용 점막 보호제로, 한국에서 단일 성분 정제로 허가되어 있습니다. 다만 허가 적응증 본문은 문서 링크로만 제공되어 구체적인 내용을 확인할 수 없습니다.
TxGNN 모델은 **십이지장 폐쇄(Duodenal Obstruction)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 연구한 임상시험은 **0건**, 문헌은 **6편**(모두 관련 질환 중심의 증례, 리뷰, 수의학 연구)에 그칩니다. 근거는 모델 예측 수준(L5)입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 적응증이 문서 링크로만 제공됨) |
| 예측 신규 적응증 | 십이지장 폐쇄 (Duodenal Obstruction) |
| TxGNN 예측 점수 | 0.9930 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가 건수 | 1건 (단일 성분 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 데이터베이스에 없습니다. 알려진 정보에 따르면 Sucralfate는 국소 작용 점막 보호제입니다. 산성 환경에서 중합되어 끈적한 보호막을 형성하고, 궤양 부위에 결합하며, 담즙산과 펩신을 흡착합니다. 국소 프로스타글란딘 분비와 점막 방어를 자극할 가능성도 있습니다. 이러한 작용은 십이지장 궤양에서 확립된 효과를 설명합니다.

십이지장 궤양은 흉터나 부종으로 폐쇄를 일으킬 수 있습니다. 그러나 폐쇄는 기계적 결과이므로, 점막 보호제가 고정된 협착이나 종괴를 풀어줄 것으로 기대하기는 어렵습니다. 기껏해야 원인이 되는 소화성 궤양 질환을 치료하는 데 도움이 될 수 있습니다.

TxGNN 모델(딥러닝)의 높은 점수(0.9930)는 모델이 학습한 Sucralfate 관련 질환인 십이지장 궤양과 십이지장 폐쇄 사이의 유사성을 반영했을 가능성이 크며, 생물학적 근거를 의미하지는 않습니다. 또한 Sucralfate는 위석(bezoar)을 형성할 수 있고, 위 배출 지연 환자에서 위 출구 문제를 악화시킨 보고가 있어 이 질환에서는 안전성 우려가 있습니다.

## 문헌 근거

십이지장 폐쇄 자체를 직접 다룬 연구는 없습니다. 아래 문헌은 관련 질환(궤양 및 그 합병증)을 다루며, 대부분 Sucralfate와 직접 관련이 없습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [9596550](https://pubmed.ncbi.nlm.nih.gov/9596550/) | 1998 | Review | J Rheumatol Suppl | NSAID 관련 위장관 합병증(출혈, 천공, 위 출구 폐쇄)의 예방 전략 |
| [12635419](https://pubmed.ncbi.nlm.nih.gov/12635419/) | 2003 | Review | Gastroenterol Clin North Am | 임신 중 위·십이지장 궤양의 빈도, 증상, 치료 |
| [8165479](https://pubmed.ncbi.nlm.nih.gov/8165479/) | 1994 | 증례 보고 | Surg Endosc | 위공장문합술 후 거대 문합부 궤양과 그 합병증(폐쇄 포함) |
| [6428868](https://pubmed.ncbi.nlm.nih.gov/6428868/) | 1984 | 증례 보고 | Endoscopy | Billroth II 절제술 및 크론병 환자의 담관 결석 용해 중 Sucralfate를 맹루(blind loop)에 주입 |
| [3758011](https://pubmed.ncbi.nlm.nih.gov/3758011/) | 1986 | 수의학 연구 | Equine Vet J | 망아지의 위·십이지장 궤양 |
| [2004991](https://pubmed.ncbi.nlm.nih.gov/2004991/) | 1991 | 수의학 증례 | J Am Vet Med Assoc | 개의 십이지장 천공 궤양 수술 치료 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202102428 | 아루사민정(수크랄페이트) | 흰색의 원형 정제 | 적응증 본문 없음 (허가사항 문서 링크만 제공됨) |

허가 건수는 단일 성분 1건이며, 제조사는 (주)인트로바이오파마입니다.

## 안전성 고려사항

- **지식 그래프상 금기 관계** (허가 문구가 아닌 TxGNN 지식 그래프 기반): 고혈당, 만성 신장병, 만성 신부전 증후군, 말기 신부전
- **약물 상호작용**: 조회 결과 총 100건이 확인되었으며, 주요 항목은 다음과 같습니다.
  - **Major**: Dolutegravir, Bictegravir
  - **Moderate**: Doxycycline, Tetracycline, Alendronic acid, Risedronic acid, Ibandronate, Pioglitazone, Alogliptin, Acarbose, Albiglutide, Allopurinol, Ascorbic acid, Baloxavir marboxil, Calcifediol
  - **Minor**: Acebutolol, Atenolol, Betaxolol, Bisoprolol, Anagrelide
- **이 적응증과 관련된 우려**: 위석 형성 및 위 배출 지연 환자에서 위 출구 문제를 악화시킬 수 있다는 보고가 있습니다.

허가사항의 경고 및 금기 문구는 확인하지 못했으므로 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
십이지장 폐쇄를 직접 연구한 임상시험이나 문헌이 없어 근거 수준이 L5이며, 점수는 TxGNN 모델(딥러닝)이 학습한 십이지장 궤양 등 관련 질환과의 유사성을 반영했을 가능성이 크고 생물학적 근거는 아닙니다. 기계적 폐쇄에 대한 기전적 타당성이 낮고 위석 형성 등 안전성 우려도 있어 현 단계에서는 진행을 보류합니다.

**진행하려면 필요한 것:**
- 허가사항(경고, 금기, 적응증 본문) 확보: 식약처 사이트에서 허가 문서를 내려받아 분석
- 작용 기전(MOA) 데이터 보완 (DrugBank 조회)
- 십이지장 폐쇄 환자를 직접 대상으로 한 임상 또는 전임상 근거
- 위 배출 지연 및 위석 형성 위험에 대한 안전성 평가
- 신기능 저하 환자에 대한 사용 지침 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

