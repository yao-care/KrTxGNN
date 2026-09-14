---
layout: default
title: Tenofovir Alafenamide
parent: 僅模型預測 (L5)
nav_order: 666
evidence_level: L5
indication_count: 3
---

# Tenofovir Alafenamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Tenofovir Alafenamide: 항레트로바이러스제에서 원숭이면역결핍바이러스(SIV) 감염으로

## 한 문장 요약

Tenofovir Alafenamide(TAF, DB09299)는 문헌상 HIV 항레트로바이러스 치료·예방(PrEP)에 사용되는 NRTI 계열 전구약물입니다.
TxGNN 모델은 **원숭이면역결핍바이러스(SIV) 감염**에 효과가 있을 것으로 예측(점수 99.89%)했으나,
이는 비인간영장류(마카크) 동물 모델 질환으로, **1건의 관련성 낮은 임상시험**과 **9편의 동물실험 문헌**만이 확인되며 실제 인체 적응증 후보로 보기 어렵습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 허가 정보 없음 (문헌상 HIV 항레트로바이러스제로 사용) |
| 예측 신규 적응증 | 원숭이면역결핍바이러스 감염 (Simian Immunodeficiency Virus Infection) |
| TxGNN 예측 점수 | 99.89% |
| 근거 수준 | L3 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

DrugBank의 공식 MOA 데이터는 현재 확보되지 않았습니다. 다만 근거팩의 재창출 근거(rationale) 자료에 따르면,
TAF는 **NRTI(뉴클레오타이드 역전사효소 억제제) 계열 전구약물**로서 바이러스 역전사효소를 억제하는 방식으로 작용하는 것으로 파악됩니다.

SIV는 HIV와 같은 렌티바이러스(lentivirus)속에 속하는 역전사바이러스로, 기전상으로는 TAF의 항바이러스 작용을 유추 적용할 수 있습니다.
그러나 **SIV 감염은 인체 질환이 아니라 비인간영장류(마카크) 동물 모델 질환**입니다. 확인된 문헌 9편은 모두 HIV 예방/치료제 개발을 위한
전임상(SHIV/SIV 마카크) 실험이며, TAF를 SIV라는 "독립된 인체 적응증"에 사용하기 위한 근거가 아닙니다. 즉 TxGNN이 지식그래프상
SIV와 HIV 노드가 가깝게 연결되어 있어 예측한 것으로, **임상적으로 실행 가능한 재창출 후보로 보기 어렵습니다.**

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | 불명 | 12 | HIV 감염자 대상 Vedolizumab+항레트로바이러스 병용요법으로 바이러스 영구관해 유도 시도 (TAF/SIV와 직접 관련 없음, 관련성 등급 C — NLP 키워드 오매칭 추정) |

> 위 시험은 SIV를 다루지 않으며 TAF도 개입약물이 아닙니다. 관련성 등급이 낮아(C) 참고용으로만 표기합니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [38134382](https://pubmed.ncbi.nlm.nih.gov/38134382/) | 2024 | 동물실험(마카크) | J Infect Dis | TAF/Elvitegravir 질내 삽입제의 성접촉 전후 SHIV 예방효과 연장 |
| [31362305](https://pubmed.ncbi.nlm.nih.gov/31362305/) | 2019 | 동물실험(마카크) | J Infect Dis | 경구 TAF 단독/TAF+FTC 병용의 질내 SHIV 감염 예방효과 |
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | 동물실험(마카크) | J Infect Dis | 경구 FTC+TAF 화학예방요법의 직장 SHIV 감염 예방효과 |
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | 동물실험(마카크) | Nature Communications | 조기치료 개시+초장기지속형 항바이러스 요법을 통한 SHIV 관해 |
| [35913838](https://pubmed.ncbi.nlm.nih.gov/35913838/) | 2022 | 동물실험(마카크) | J Antimicrob Chemother | TAF 방출 생분해성 임플란트의 질내 보호 안전성·유효성 |
| [16810108](https://pubmed.ncbi.nlm.nih.gov/16810108/) | 2006 | 동물실험(유아 마카크) | J Acquir Immune Defic Syndr | 경구 TDF 및 국소 GS-7340(TAF)의 반복 경구 SIV 노출 방어효과 |
| [39559349](https://pubmed.ncbi.nlm.nih.gov/39559349/) | 2024 | 동물실험(인간화 마우스) | Frontiers in Immunology | SIV/HIV 항바이러스 전략 검증용 이중목적 인간화 마우스 모델 |
| [31730629](https://pubmed.ncbi.nlm.nih.gov/31730629/) | 2019 | 동물실험(방법론) | PLoS ONE | 마카크 대상 경구 항레트로바이러스제 매일 투여 훈련 프로토콜 |
| [22740713](https://pubmed.ncbi.nlm.nih.gov/22740713/) | 2012 | 동물실험(마카크) | J Infect Dis | 경구 PrEP 중 급성 SHIV 감염 시 염증 반응 및 CD4 손실 완화 |

> 문헌 9편 모두 전임상(비인간영장류/인간화 마우스) 단계이며, 인체 임상 근거는 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (한국 미시판 상태로 현지 허가 자료 및 DDI 정보가 확보되지 않았습니다.)

---

## 참고: 그 외 예측 적응증 (2, 3순위)

- **Feline Acquired Immunodeficiency Syndrome (FIV, 2순위)**: 임상시험·문헌 근거 전무(L5), 고양이 수의학 질환으로 인체 재창출 대상 아님.
- **신경발달장애(운동실조·언어부재·백질감소, 3순위)**: 기전적 연관성 없음, 근거 전무(L5), TxGNN 위양성 추정.

두 예측 모두 이번 보고서의 검토 범위에서 제외하며, 참고용으로만 기재합니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 예측된 1순위 적응증(SIV 감염)은 동물 모델 질환으로, 인체 임상 재창출 대상이 될 수 없습니다.
- 한국 허가 자료, TFDA/식약처 수준의 경고·금기 정보(Blocking 데이터 갭)가 전혀 확보되지 않아 안전성 초기 평가(S1) 진입이 불가능합니다.
- 관련 임상시험은 1건뿐이며 관련성 등급도 낮습니다(C등급, 사실상 매칭 오류로 판단).

**진행하려면 필요한 것:**
- TFDA(또는 MFDS) 공식 허가사항 확보 — 경고/금기/DDI 정보 (Blocking)
- DrugBank 등에서 공식 MOA 데이터 확보
- TAF의 실제 인체 적응증(HIV 감염, HBV 감염 등) 기준으로 TxGNN 예측 재실행 및 동물 모델 질환 필터링 적용
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

