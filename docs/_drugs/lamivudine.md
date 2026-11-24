---
layout: default
title: Lamivudine
parent: 모델 예측만 (L5)
nav_order: 455
evidence_level: L5
indication_count: 5
monitor_inn: "LAMIVUDINE"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia", "chronic hepatitis C virus infection"]
last_modified_at: 2026-11-24
description: "Lamivudine: 예측 신규 적응증 시미안 면역결핍 바이러스 감염 (근거 수준 L5). 기존 적응증: 만성 활동성 B형 간염 바이러스 감염증 환자(혈중 HBV-DNA 양성환자에 한함)의 바이러스 증식억제…"
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
| 기존 적응증 | 만성 활동성 B형 간염 바이러스 감염증 환자(혈중 HBV-DNA 양성환자에 한함)의 바이러스 증식억제. 만성B형 간염 치료를 처음으로 시작하는 경우 : 라미부딘 투여 환자에서 내성 발현율이 높으므로, 내성에 대한 더 높은 유전적 장벽(genetic barrier)이 있는 다른… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201001033/EE)) |
| 예측 신규 적응증 | 시미안 면역결핍 바이러스 감염 |
| TxGNN 예측 점수 | 0.9993 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 8건 / 전체 10건) |
| 허가증 수 | 10건 (유효 8건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Lamivudine 처방 정보(Prescribing Information)의 “Mechanism of Action” 및 “Microbiology” 항목에 따르면(비공식 번역): “라미부딘은 항레트로바이러스제이다. […] 라미부딘은 합성 뉴클레오시드 유사체이다. 세포 내에서 라미부딘은 인산화되어 활성 5′-삼인산 대사체인 라미부딘 삼인산(3TC-TP)이 된다. 3TC-TP의 주된 작용 방식은 뉴클레오티드 유사체가 삽입된 후 DNA 사슬 종결을 통해 HIV-1 역전사효소(RT)를 억제하는 것이다.” 영어 원문: "Lamivudine is an antiretroviral agent. […] Lamivudine is a synthetic nucleoside analogue. Intracellularly, lamivudine is phosphorylated to its active 5′-triphosphate metabolite, lamivudine triphosphate (3TC-TP). The principal mode of action of 3TC-TP is inhibition of HIV-1 reverse transcriptase (RT) via DNA chain termination after incorporation of the nucleotide analogue." ([DailyMed: Epivir (lamivudine) prescribing information, ViiV Healthcare Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=89226149-47fa-4f7d-bb1f-1aa7034486b8), 버전 2024-08-15; 확인일 2026-11-19). 알려진 정보에 따르면 lamivudine은 핵산유사체 역전사효소 억제제(NRTI) 계열입니다. 이 계열은 HIV-1과 B형 간염 바이러스(HBV)의 역전사효소(중합효소)를 표적으로 합니다.

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

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201001033 | 리벅스정(라미부딘)(수출용) | 연한 주황색의 양면이 볼록한 장방형 필름코팅정 | (주)오스코리아제약 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201001033/EE) | 유효 |
| 199907321 | 쓰리티씨정150밀리그램(라미부딘) | 흰색의 다이아몬드형 필름 코팅 정제 | (주)글락소스미스클라인 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199907321/EE) | 유효 |
| 200108711 | 컴비비어정 | 백색 내지 유백색의 장방형 필름 코팅 정제 | (주)글락소스미스클라인 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200108711/EE) | 유효 |
| 200810687 | 제픽스정100밀리그램(라미부딘) | 연한 주황색의 양면이 볼록한 장방형 필름코팅정 | (주)글락소스미스클라인 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200810687/EE) | 유효 |
| 202001791 | 도바토정 | 흰색의 양면이 볼록한 타원형 필름코팅정 | (주)글락소스미스클라인 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202001791/EE) | 유효 |

위 표는 허가 10건 중 5건입니다.

<!-- licenses:end -->

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

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Epivir (lamivudine) prescribing information, ViiV Healthcare Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=89226149-47fa-4f7d-bb1f-1aa7034486b8) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

