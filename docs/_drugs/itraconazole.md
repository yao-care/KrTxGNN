---
layout: default
title: Itraconazole
parent: 僅模型預測 (L5)
nav_order: 412
evidence_level: L5
indication_count: 1
---

# Itraconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Itraconazole: 전신 진균감염에서 폐포자충증(Pneumocystosis)으로

## 한 문장 요약

Itraconazole은 트리아졸계 항진균제로, 전신 진균감염 치료에 사용되는 약물입니다. TxGNN 모델은 **폐포자충증(Pneumocystosis)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 임상시험은 없고 **20편의 문헌**만 확인되며, 그마저도 대부분 폐포자충증 자체보다는 면역저하 환자의 다른 기회감염 예방을 다룬 간접적 근거입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 전신 진균감염 치료제 (본 팩 내 한국 허가 정보 없음) |
| 예측 신규 적응증 | 폐포자충증 (Pneumocystosis) |
| TxGNN 예측 점수 | 99.34% |
| 근거 수준 | L4 |
| 한국 시판 현황 | 미판매 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용기전(MOA) 데이터는 확보되지 않았습니다. 다만 널리 알려진 바로는, Itraconazole은 트리아졸계 항진균제로 진균의 CYP51(lanosterol 14α-demethylase)을 억제해 ergosterol 합성을 차단함으로써 항진균 효과를 냅니다.

그러나 이 예측에는 중요한 기전상 의문점이 있습니다. Pneumocystis jirovecii는 세포막 형성에 자체 합성한 ergosterol이 아니라 **숙주의 콜레스테롤**을 주로 이용하는 것으로 알려져 있어, 아졸계 약물이 다른 사상균/효모균 감염과 달리 이 병원체에 직접적인 살진균 효과를 낼지는 근본적으로 불확실합니다. 실제로 문헌에서 Itraconazole은 장기이식·HIV 면역저하 환자에서 조직포자충증 등 **다른 기회감염을 예방**하는 목적으로 주로 다뤄지며, 폐포자충증(PCP) 자체의 표준 치료는 여전히 TMP-SMX입니다. 즉 TxGNN 점수는 매우 높지만, 이는 "면역저하 환자에서 함께 언급되는 빈도"에 의한 예측일 가능성이 있고 직접적 항-Pneumocystis 활성 근거는 아닙니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | RCT | HIV Medicine | HIV 감염자 대상 이중맹검 위약대조 시험, Itraconazole 캡슐의 심부 진균감염 예방 효과 평가 (PCP 특이적 시험 아님) |
| [12606318](https://pubmed.ncbi.nlm.nih.gov/12606318/) | 2003 | 미분류(기초연구) | Am J Respir Cell Mol Biol | Pneumocystis carinii의 lanosterol 14α-demethylase(Erg11) 특성 분석 - PC가 아졸계 항진균제에 본질적으로 내성을 가짐을 시사 |
| [30429396](https://pubmed.ncbi.nlm.nih.gov/30429396/) | 2018 | 코호트 | Indian J Med Microbiol | 면역정상/면역저하 환자의 호흡기 진균 병원체 프로파일 및 CD4+T세포 수와의 상관관계 비교 |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | 코호트 | Transplantation Proceedings | 신장이식 환자에서 침습성 진균감염 단일기관 경험 |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | 리뷰 | BMJ Clinical Evidence | HIV 환자 기회감염의 1차/2차 예방요법 개관 |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | 리뷰 | Current Clinical Topics in Infectious Diseases | 골수이식 수혜자의 감염 예방 및 치료 전략 |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | 리뷰 | Seminars in Respiratory Infections | 폐이식 후 감염(세균성 폐렴 포함)의 예방·진단·치료 동향 |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | 리뷰 | Drugs | Pneumocystis carinii 등 전신 원충 감염의 치료·예방제 개관 |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | 증례보고 | Frontiers in Immunology | STAT1 돌연변이 소아에서 Talaromyces marneffei와 Pneumocystis jirovecii 동시 감염 사례 |
| [8187612](https://pubmed.ncbi.nlm.nih.gov/8187612/) | 1994 | 증례보고 | Deutsche Medizinische Wochenschrift | AIDS 환자에서 초기 PCP 의심 후 파종성 히스토플라스마증으로 확진된 사례 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
폐포자충증에 대한 직접적 치료 근거(임상시험 전무, RCT 없음)가 부족하며, Pneumocystis가 ergosterol 대신 숙주 콜레스테롤을 이용한다는 생물학적 특성상 아졸계 약물의 직접적 항균 효과 자체가 기전적으로 의문시됩니다. 확인된 문헌 20편도 대부분 PCP가 아닌 다른 기회감염(조직포자충증 등) 예방 맥락에서 Itraconazole을 다루고 있어, TxGNN의 높은 예측 점수(99.34%)를 임상적 근거로 해석하기에는 이릅니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기) 확보 — 현재 Blocking 등급 데이터 갭 (DG001)
- Itraconazole의 상세 작용기전(MOA) 데이터 확보 — High 등급 데이터 갭 (DG002)
- Pneumocystis jirovecii에 대한 직접적 in vitro/in vivo 항균 활성 데이터
- 약물상호작용(DDI) 정보 재조회 (현재 not_found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

