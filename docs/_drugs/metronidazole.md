---
layout: default
title: Metronidazole
parent: 모델 예측만 (L5)
nav_order: 513
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-15
description: "Metronidazole: 예측 신규 적응증 폐포자충증 (Pneumocystosis) (근거 수준 L5). 기존 적응증: 1. 유효균종 : 질트리콤나스, 이질아메바, 혐기성균 2. 적응증 : 1) 트리코모나스 증 : 트리코모나스…"
monitor_inn: "Metronidazole"
predicted_indications: ["pneumocystosis", "punctate epithelial keratoconjunctivitis", "ulcerative proctosigmoiditis", "nocardiosis", "postmenopausal atrophic vaginitis", "papillary conjunctivitis", "myiasis", "cap polyposis", "ulceration of vulva"]
---

# Metronidazole
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

## Metronidazole: 혐기성 세균·원충 감염에서 폐포자충증(Pneumocystosis)으로
{: .text-alpha }

## 한 문장 요약

Metronidazole은 혐기성 세균과 원충 감염 치료에 널리 쓰이는 니트로이미다졸계 항미생물제입니다. TxGNN 모델은 **폐포자충증(Pneumocystosis)**에 효과가 있을 수 있다고 예측했지만, 이를 직접 뒷받침하는 **임상시험은 0건**입니다. 검색된 **문헌 10편**도 대부분 일반 총설이나 증례이고, 폐포자충증에 대한 metronidazole의 효능을 보여주는 것은 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 유효균종 : 질트리콤나스, 이질아메바, 혐기성균 2. 적응증 : 1) 트리코모나스 증 : 트리코모나스 전립선 정관염, 요도염, 질염, 자궁내막염, 자궁경관염, 자궁경부미란 및 지알디아증, 빈센트씨 완상구립염 2) 아메바증 : 급성장아메바, 아메바성 간종양, 급성 아메바성이질 3)… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202402170/EE)) |
| 예측 신규 적응증 | 폐포자충증 (Pneumocystosis) |
| TxGNN 예측 점수 | 0.9999 |
| 근거 수준 | L5 (모델 예측만 있음) |
| 한국 시판 현황 | 시판 중 (유효 허가 17건 / 전체 20건) |
| 허가증 수 | 20건 (유효 17건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Metronidazole 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “니트로이미다졸계 약물인 메트로니다졸은 혐기성 환경에서 대부분의 편성 혐기성균에 대해 항균 효과를 나타낸다. 메트로니다졸은 수동 확산에 의해 미생물 내로 들어가 감수성 혐기성 세균의 세포질에서 활성화되면 환원되는데, 이 과정에는 페레독신과 같은 세포 내 전자 전달 공여체와 메트로니다졸의 니트로기로의 전자 전달이 포함되며, 그 결과 수명이 짧은 니트로소 자유 라디칼이 형성된다.” 영어 원문: "Metronidazole, a nitroimidazole, exerts antibacterial effects in an anaerobic environment against most obligate anaerobes. Once metronidazole enters the organism by passive diffusion and activated in the cytoplasm of susceptible anaerobic bacteria, it is reduced; this process includes intra-cellular electron transport donors such as ferredoxin and transfer of an electron to the nitro group of the metronidazole leading to formation of a short-lived nitroso free radical." ([DailyMed: metronidazole prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=49360d6f-c8b3-420e-af75-154cf7b05255), 버전 2026-11-02; 확인일 2026-11-19). 일반적으로 metronidazole은 혐기성 세균과 원충 내부에서 니트로기가 환원되어 활성화되고, 이 활성 대사체가 DNA를 손상시키는 방식으로 작용합니다.

이 기전은 폐포자충증에는 맞지 않습니다. Pneumocystis는 진균이어서 metronidazole이 의존하는 니트로환원효소 활성화 경로가 없습니다. 표준 치료제는 trimethoprim-sulfamethoxazole입니다. 따라서 0.9999라는 높은 예측 점수는 TxGNN 모델(딥러닝)이 산출한 값이며, 모델이 관련 질환 사이에서 학습한 유사성을 반영할 수 있을 뿐 생물학적 근거는 아닙니다. 기전상 타당성은 낮다고 판단합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Review | Mayo Clin Proc | 항기생충제 전반 총설. Metronidazole의 폐포자충증 효능 근거 없음 |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | Am Fam Physician | Metronidazole은 아메바증·트리코모나스증에, 폐포자충 폐렴에는 TMP-SMX를 권고 |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Review | Clin Pharmacokinet | 항원충 치료의 약동학적 근거 총설. 직접적 근거 없음 |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Review | Clin Pharm | AIDS 감염 합병증 치료 총설. 폐포자충 폐렴이 가장 흔한 합병증으로 다뤄짐 |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Review | Top Antivir Med | HIV 관련 기회감염의 현황 개괄. Metronidazole 효능 언급 없음 |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Review | Rev Infect Dis | 항균제 예방 투여 임상시험 비평. 폐포자충증과 무관 |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | 증례보고 | Am Rev Respir Dis | 건강한 성인의 폐포자충·CMV 폐렴. 이전에 설사로 metronidazole을 복용했을 뿐 치료 효과와 무관 |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | 증례보고 | Kansenshogaku Zasshi | AIDS 환자 2례. 아메바성 이질에 metronidazole을 썼고, 폐포자충 폐렴은 별개 합병증 |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | 증례보고 | J Formos Med Assoc | AIDS 환자의 CMV·아메바성 대장염에 의한 천공. 폐포자충증 근거 아님 |
| [42178576](https://pubmed.ncbi.nlm.nih.gov/42178576/) | 2026 | 증례보고 | J Med Case Rep | 사코이드증에서 첫 증상으로 나타난 소뇌 농양. 폐포자충증 근거 아님 |

## 한국 시판 정보

한국에는 17건의 유효 허가가 있으며, 이 중 다수는 수출용입니다. 허가 적응증 본문은 허가사항 PDF 링크로만 제공되어 요약하지 못했습니다. 주요 5건은 다음과 같습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 196500004 | 후라시닐정 | 흰색 원형 정제 | [허가사항 PDF 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/196500004/EE) |
| 199500289 | 메트리날주 | 주사액 | [허가사항 PDF 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199500289/EE) |
| 199900910 | 후라니졸주 | 주사액 | [허가사항 PDF 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199900910/EE) |
| 198400094 | 트리젤주 | 주사액 | [허가사항 PDF 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198400094/EE) |
| 199902024 | 메로겔 | 질용 겔 | [허가사항 PDF 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199902024/EE) |

## 안전성 고려사항

허가사항 기반의 경고·금기 정보는 이번 데이터에 포함되지 않았으므로 허가사항을 참조하세요. 참고용 정보는 다음과 같습니다.

- **지식 그래프 기반 금기 관련 질환** (허가 문구가 아니라 TxGNN 지식 그래프의 약물-질환 연결 정보): 간부전·간질환, 간질, 신장질환, 혈액질환(호중구감소증, 무과립구증, 백혈구감소증, 혈액응고질환), 말초신경병증·말초신경계 질환, 뇌질환, 시신경 질환, 울혈성 심부전, 당뇨병·당뇨병성 케톤산증, 통풍, 담낭질환, 물질 남용·의존, 피부염, 비감염성 수막염 등
- **약물 상호작용**: 조회된 100건 중 상위 20건을 확인했습니다.
  - **Major**: Ethanol (알코올)
  - **Moderate**: Paclitaxel, Adalimumab, Trastuzumab emtansine, Ethinylestradiol, Estradiol, Butalbital, Amiodarone, Celecoxib, Amobarbital, Loperamide
  - 나머지는 Minor 등급입니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
폐포자충증에 대한 근거는 모델 예측뿐입니다. 임상시험이 없고 문헌도 효능을 보여주지 못합니다. 또한 Pneumocystis는 진균이어서 metronidazole의 작용 기전이 적용되지 않으며, 표준 치료제(TMP-SMX)가 이미 확립되어 있습니다.

**진행하려면 필요한 것:**
- 작용 기전 데이터 확보와 Pneumocystis에 대한 in vitro 활성 등 전임상 근거
- 허가사항 PDF 파싱을 통한 경고·금기·적응증 본문 확인 (현재 안전성 심사 불가)
- 이 데이터셋의 다른 예측 중 재검토 가치가 있는 후보: **모세포(cap) 폴립증**은 증례 보고와 항염증 기전 가설이 있어 가장 생물학적으로 그럴듯하며, 근거 수준은 L4(Research Question)입니다. 다만 희귀질환이고 대조 시험 자료는 없습니다.

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: metronidazole prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=49360d6f-c8b3-420e-af75-154cf7b05255) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

