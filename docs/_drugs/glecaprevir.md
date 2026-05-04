---
layout: default
title: Glecaprevir
parent: 僅模型預測 (L5)
nav_order: 267
evidence_level: L5
indication_count: 10
---

# Glecaprevir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Glecaprevir: C형간염에서 HIV 감염성 질환으로

## 한 문장 요약

Glecaprevir는 HCV NS3/4A 세린 단백분해효소 억제제로, Mavyret(글레카프레비르/피브렌타스비르) 복합제의 성분으로 C형간염(HCV 유전자형 1–6) 치료에 사용됩니다.
TxGNN 모델은 **HIV 감염성 질환(HIV infectious disease)**에 효과가 있을 수 있다고 예측하며,
현재 **15건의 임상시험**과 **20편의 문헌**이 검색되었으나, 이는 모두 HIV/HCV 공동감염자에서의 HCV 치료 연구로, HIV를 직접 치료 표적으로 한 근거는 없습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | C형간염 (HCV 유전자형 1–6, Mavyret 복합제 성분) |
| 예측 신규 적응증 | HIV 감염성 질환 (HIV infectious disease) |
| TxGNN 예측 점수 | 99.87% |
| 근거 수준 | L4 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 없습니다. 알려진 정보에 따르면 Glecaprevir는 HCV 비구조 단백질 NS3/4A **세린 단백분해효소(serine protease)**를 표적으로 하는 직접 작용 항바이러스제(DAA)입니다. 피브렌타스비르(NS5A 억제제)와 결합하여 Mavyret 복합제로 사용되며, HCV 유전자형 1–6 감염 환자에서 8–12주 치료 시 97% 이상의 지속 바이러스 반응(SVR12)을 달성합니다.

그러나 **HIV는 레트로바이러스**로, 복제 시 역전사효소(Reverse Transcriptase)와 아스파르트산 단백분해효소(HIV Protease, 아스파르트산 계열)를 사용합니다. 이는 HCV NS3/4A 세린 단백분해효소와 촉매 기전, 결합 부위, 단백질 서열 모두에서 근본적으로 상이하며, 교차 억제 근거가 없습니다. 모든 검색된 임상시험은 HIV/HCV 공동감염자에서 HCV를 치료 표적으로 설계된 것으로, HIV 자체를 치료한 연구는 단 한 건도 없습니다.

**TxGNN 예측 편향 분석**: 이번 예측의 고점수(99.87%)는 지식 그래프 내 HIV-HCV 공동감염 노드 밀도가 높아 발생한 **그래프 전파 효과(graph propagation artifact)**로 해석됩니다. 항바이러스 약리학적 예측이 아닌 질병 공동 출현 연결에 의한 통계적 부산물입니다.

---

## 임상시험 근거

> ⚠️ **주의**: 아래 임상시험은 모두 **HCV 치료**를 일차 목적으로 하며, HIV/HCV 공동감염은 하위 집단 또는 동반 조건으로 포함된 경우입니다. HIV를 직접 치료 표적으로 설계된 시험은 없습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02738138](https://clinicaltrials.gov/study/NCT02738138) | Phase 3 | 완료 | 153 | HCV 유전자형 1–6 및 HIV-1 공동감염 성인에서 G/P 효능·안전성 평가 (EXPEDITION-2) |
| [NCT03222583](https://clinicaltrials.gov/study/NCT03222583) | Phase 3 | 완료 | 546 | 비간경변 아시아 성인(HIV 공동감염 포함) HCV 유전자형 1–6 G/P 이중맹검 연구 |
| [NCT03235349](https://clinicaltrials.gov/study/NCT03235349) | Phase 3 | 완료 | 160 | 보상성 간경변 아시아 성인(HIV 공동감염 포함) G/P 효능·안전성 |
| [NCT02939989](https://clinicaltrials.gov/study/NCT02939989) | Phase 3 | 완료 | 33 | AbbVie HCV 임상 실패자에서 G/P+SOF+RBV 3제 요법; HIV 공동감염자 포함 (MAGELLAN-3) |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | 완료 | 87 | HIV/HCV 공동감염자 HCV 제거 후 심근 손상 및 심혈관 위험 개선 여부 탐색 (파일럿) |
| [NCT02634008](https://clinicaltrials.gov/study/NCT02634008) | Phase 3 | 완료 | 83 | 최근 발병 HCV(HIV 공동감염 포함)에서 Paritaprevir 및 G/P 비교 다국가 파일럿 |
| [NCT04042740](https://clinicaltrials.gov/study/NCT04042740) | Phase 2 | 완료 | 45 | 급성 HCV 감염(HIV-1 공동감염 포함)에서 G/P 4주 요법 효능 (PURGE-C) |
| [NCT04577482](https://clinicaltrials.gov/study/NCT04577482) | N/A | 완료 | 42 | DAA 치료 경험 만성 HCV 유전자형 1 환자에서 G/P 러시아 실제 임상 효과 (CHOICE) |
| [NCT04352309](https://clinicaltrials.gov/study/NCT04352309) | N/A | 완료 | 99 | HCV 간경변 환자 G/P 8주 러시아 실제 임상 효과 (EASY) |
| [NCT07040319](https://clinicaltrials.gov/study/NCT07040319) | Phase 1/2 | 모집 예정 | 30 | 임신 중 HCV 감염 여성(HIV 포함)에서 G/P 약동학 및 안전성 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [37671831](https://pubmed.ncbi.nlm.nih.gov/37671831/) | 2023 | 코호트 | J Antimicrob Chemother | HIV/HCV 공동감염 환자에서 G/P 실제 임상 SVR 반응 평가 — HIV 감염이 DAA 반응률에 미치는 영향 분석 |
| [31504702](https://pubmed.ncbi.nlm.nih.gov/31504702/) | 2020 | 약동학 | J Infect Dis | HIV 항레트로바이러스제와 G/P 병용 시 약물동태학적 상호작용 데이터 제공 |
| [29595065](https://pubmed.ncbi.nlm.nih.gov/29595065/) | 2018 | 리뷰 | Expert Opin Pharmacother | HCV 단백분해효소 억제제 치료 현황 (유럽·미국 HIV/HCV 공동감염자 25–30% 포함) |
| [36415300](https://pubmed.ncbi.nlm.nih.gov/36415300/) | 2022 | 증례 | J Prev Med Hyg | HIV 환자 G/P + ART 병용 중 간접 고빌리루빈혈증·황달 발생 이탈리아 첫 증례 보고 |
| [34664197](https://pubmed.ncbi.nlm.nih.gov/34664197/) | 2021 | 증례 | Clin J Gastroenterol | HIV/HCV 유전자형 4a 공동감염 혈우병 환자 G/P 치료 성공 증례 |
| [35877601](https://pubmed.ncbi.nlm.nih.gov/35877601/) | 2022 | 리뷰 | PLoS One | TB·HIV·HCV 신약 승인 타임라인 및 근거 비교 — 질환군 간 임상개발 환경 차이 분석 |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | 학회보고 | AIDS Reviews | 국제 바이러스 간염 학회 2017 — 범유전자형 DAA 및 WHO 2030 퇴치 목표 논의 |
| [31284039](https://pubmed.ncbi.nlm.nih.gov/31284039/) | 2019 | 메타분석 | Int J Antimicrob Agents | G/P HCV 유전자형 1–6 효능·안전성 체계적 문헌고찰 (13개 연구, n=3,082, SVR12 97.8%) |
| [29845496](https://pubmed.ncbi.nlm.nih.gov/29845496/) | 2018 | 리뷰 | Hepatology Int | G/P가 HCV 치료 접근성 확대 및 치료 기간·비용 단축 가능성 제시 |
| [38367631](https://pubmed.ncbi.nlm.nih.gov/38367631/) | 2024 | 리뷰 | Lancet Gastroenterol Hepatol | 전 세계 HCV DAA 약물의 등록·급여·접근 제한 현황 분석 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
Glecaprevir의 HCV NS3/4A 세린 단백분해효소 억제 기전은 HIV 복제 경로(역전사효소, 아스파르트산 단백분해효소)와 기전적 연관이 전혀 없으며, TxGNN의 99.87% 고점수는 지식 그래프 내 HIV-HCV 공동감염 노드 밀도에 의한 그래프 편향으로 판단됩니다. 약리학적 재창출 근거가 부재하여 추가 투자를 정당화하기 어렵습니다.

**진행하려면 필요한 것:**
- Glecaprevir의 HIV 역전사효소 또는 HIV 단백분해효소에 대한 체외(in vitro) 활성 데이터 (현재 없음, 수집 필요)
- 상세한 작용 기전(MOA) 데이터 보완 — DrugBank API 조회 권장 (DG002 해소)
- 만약 Flaviviridae 계열 교차 억제 가능성을 탐색한다면, Rank 8(Omsk 출혈열) 및 Rank 9(Kyasanur 산림병)에 대한 in vitro NS3 억제 실험이 보다 기전적으로 타당한 출발점
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

