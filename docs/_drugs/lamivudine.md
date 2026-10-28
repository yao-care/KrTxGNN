---
layout: default
title: Lamivudine
parent: 모델 예측만 (L5)
nav_order: 455
evidence_level: L5
indication_count: 5
monitor_inn: "LAMIVUDINE"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia", "chronic hepatitis C virus infection"]
last_modified_at: 2026-10-28
description: "Lamivudine: 예측 신규 적응증 시미안 면역결핍 바이러스 감염 (근거 수준 L5). 기존 적응증: 확인 불가 (허가 적응증 본문이 링크 형태로만 제공되어 내용 확인 불가)"
---

# Lamivudine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **5** 건
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

## Lamivudine: 허가 적응증에서 시미안 면역결핍 바이러스 감염으로
{: .text-alpha }

## 한 문장 요약

Lamivudine은 핵산유사체 계열 역전사효소 억제제로, 한국에서 단일 성분 제제로 허가되어 있습니다. 다만 이번 데이터에 포함된 허가 적응증 항목은 문서 링크만 있고 본문이 없어, 구체적인 적응증은 확인하지 못했습니다.
TxGNN 모델은 **시미안 면역결핍 바이러스 감염(Simian Immunodeficiency Virus Infection)**에 효과가 있을 수 있다고 예측합니다. 이를 직접 연구한 임상시험은 없고 **15편의 문헌**(대부분 원숭이 등 동물 모델 연구)이 있어, 근거 수준은 L5입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 적응증 본문이 링크 형태로만 제공되어 내용 확인 불가) |
| 예측 신규 적응증 | 시미안 면역결핍 바이러스 감염 |
| TxGNN 예측 점수 | 0.9993 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가 건수 | 단일 성분 허가 5건 (유효 5건, 취소 0건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 lamivudine은 핵산유사체 역전사효소 억제제(NRTI) 계열입니다. 이 계열은 HIV-1과 B형 간염 바이러스(HBV)의 역전사효소(중합효소)를 표적으로 합니다.

SIV는 HIV와 가까운 렌티바이러스로 역전사효소가 유사하므로, 기전상 활성은 충분히 가능합니다. 마카크 원숭이 연구에서 lamivudine이 포함된 병용요법이 SIV를 억제했고, HIV-1에서 보이는 내성 변이(M184V)가 SIV 역전사효소에서도 나타났습니다.

그러나 SIV 감염은 사람의 적응증이 아니라 동물 모델입니다. 따라서 직접적인 임상 용도가 없으며, HIV 치료를 뒷받침하는 전임상 근거로서의 가치가 큽니다. 또한 대부분의 연구가 병용요법이어서 lamivudine 단독의 기여도를 분리하기 어렵습니다.

## 문헌 근거

임상시험 등록은 현재 없습니다. 아래는 주요 문헌 10편입니다. 모두 SIV 관련 전임상 연구 또는 리뷰이며 사람 대상 RCT는 없습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [12021341](https://pubmed.ncbi.nlm.nih.gov/12021341/) | 2002 | 전임상 | J Virol | 신생 마카크에서 lamivudine 또는 emtricitabine 치료 후 5주 내 M184V 내성 변이 출현. 인체 HIV-1 양상과 유사 |
| [19240457](https://pubmed.ncbi.nlm.nih.gov/19240457/) | 2009 | 전임상 | AIDS | zidovudine, lamivudine, indinavir 노출 후 예방요법의 질내 SIV 전파 예방 효과 평가 |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | 전임상 | J Virol | SIV 감염 마카크에서 4제 항레트로바이러스 요법 시 빠른 바이러스 감소 |
| [12502828](https://pubmed.ncbi.nlm.nih.gov/12502828/) | 2003 | 전임상 | J Virol | tenofovir가 lamivudine 병용 중에도 SIV의 M184V 복귀를 선택 |
| [15919889](https://pubmed.ncbi.nlm.nih.gov/15919889/) | 2005 | 전임상 | J Virol | efavirenz, lamivudine, tenofovir 병용으로 RT-SHIV 감염 마카크의 바이러스량 억제 |
| [11689641](https://pubmed.ncbi.nlm.nih.gov/11689641/) | 2001 | 전임상 | J Virol | HAART로 바이러스혈증이 줄어도 SHIV 감염 마카크에서 골수 조혈 결함 지속 |
| [14610172](https://pubmed.ncbi.nlm.nih.gov/14610172/) | 2003 | 전임상 | J Virol | 조기 항바이러스 요법이 SIVmac251 감염 마카크의 림프구 증식에 미치는 영향 예비 보고 |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | 전임상 | Antivir Ther | HIV-2, SIV, SHIV에 대한 승인 항HIV 약물 16종의 활성 평가 |
| [12163615](https://pubmed.ncbi.nlm.nih.gov/12163615/) | 2002 | 전임상 | J Virol | M184V 변이가 약독화 SIV 변이체의 복귀를 지연시킬 수 있음 |
| [31658118](https://pubmed.ncbi.nlm.nih.gov/31658118/) | 2020 | Review | Curr Opin HIV AIDS | islatravir의 HIV-1 치료·예방 역할 (lamivudine 자체와는 간접 관련) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201001033 | 리벅스정(라미부딘)(수출용) | 연한 주황색 장방형 필름코팅정 | 허가 문서 링크만 제공되어 적응증 본문 확인 불가 |
| 199907321 | 쓰리티씨정150밀리그램(라미부딘) | 흰색 다이아몬드형 필름코팅정 | 허가 문서 링크만 제공되어 적응증 본문 확인 불가 |
| 200108711 | 컴비비어정 | 백색~유백색 장방형 필름코팅정 | 허가 문서 링크만 제공되어 적응증 본문 확인 불가 |
| 200810687 | 제픽스정100밀리그램(라미부딘) | 연한 주황색 장방형 필름코팅정 | 허가 문서 링크만 제공되어 적응증 본문 확인 불가 |
| 202001791 | 도바토정 | 흰색 타원형 필름코팅정 | 허가 문서 링크만 제공되어 적응증 본문 확인 불가 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었습니다. 중등도로 분류된 주요 항목은 lactitol, mannitol, naltrexone, orlistat, sorbitol입니다. 그 밖에 metformin, cimetidine, omeprazole, vancomycin 등 다수가 등급 미확정으로 조회되었습니다.
- **지식 그래프상 금기 관계** (허가사항 문구가 아니라 지식 그래프에 기록된 관계): 간부전, 신장 질환, 췌장염, 간 질환, 근병증, 호중구감소증, 무과립구증, 빈혈, 지방간, 젖산산증, 근염 등.

허가사항의 경고 및 금기 정보는 이번 데이터에 포함되어 있지 않으므로 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
SIV 감염은 사람의 적응증이 아닌 동물 모델이며, 이 질환을 직접 다룬 임상시험이 없습니다. 문헌은 전임상 연구 위주이고 대부분 병용요법이어서 lamivudine 단독 효과를 판단하기 어려워 근거 수준은 L5입니다. 허가 적응증 본문과 허가사항의 안전성 정보도 확인되지 않았습니다.

**진행하려면 필요한 것:**
- 식약처 허가사항 문서에서 허가 적응증과 경고·금기 정보 확보
- DrugBank 등에서 작용 기전(MOA) 데이터 확보
- SIV를 사람 적응증이 아닌 전임상 모델로 보고, 실제 사람 대상 후보 적응증(예: HIV-1 관련)을 별도로 평가
- 이 예측이 사람 대상 재창출 가설로 적합한지 재검토 (현재로서는 연구용 모델 근거로만 해석 가능)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

