---
layout: default
title: Rifabutin
parent: 모델 예측만 (L5)
nav_order: 652
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-03
monitor_inn: "Rifabutin"
predicted_indications: ["HIV infectious disease", "multiple endocrine neoplasia", "sclerosing cholangitis", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "conjunctivitis", "leprosy", "endocarditis", "pneumocystosis", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection"]
description: "Rifabutin: 예측 신규 적응증 HIV 감염증 (HIV infectious disease) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200400200/EE"
---

# Rifabutin
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

## Rifabutin: HIV 감염증 (HIV infectious disease)
{: .text-alpha }

## 한 문장 요약

Rifabutin은 세균의 RNA 중합효소(rpoB)를 억제하는 리파마이신계 항생제입니다.
TxGNN 모델은 **HIV 감염증(HIV infectious disease)**에 효과가 있을 수 있다고 예측하지만, 현재까지의 임상시험과 문헌은 HIV 감염 환자의 결핵·MAC 등 기회감염을 다루거나 항레트로바이러스제와의 약물 상호작용을 평가한 것이며, HIV 감염 자체를 치료한 연구는 없어 근거 수준은 **L5**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200400200/EE |
| 예측 신규 적응증 | HIV 감염증 (HIV infectious disease) |
| TxGNN 예측 점수 | 0.9988 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 수집되지 않았습니다. 알려진 정보에 따르면 Rifabutin은 세균 DNA 의존성 RNA 중합효소(rpoB)를 억제하는 리파마이신계 약물이며, 항레트로바이러스 작용은 없습니다.

HIV 환자에서 Rifabutin의 가치는 HIV 자체를 억제하는 데 있지 않고, 결핵과 MAC(Mycobacterium avium complex) 같은 기회감염의 치료와 예방에 있습니다. 또한 Rifampin보다 CYP3A4 유도 작용이 약해, 용량 조절을 전제로 프로테아제 억제제 등 항레트로바이러스제와 함께 쓸 수 있습니다.

따라서 모델의 높은 예측 점수는 HIV 환자군과의 연관성을 반영한 것으로 보이며, HIV 감염 자체에 대한 치료 효과를 뒷받침하는 기전적 근거는 확인되지 않았습니다.

## 임상시험 근거

수집된 시험은 대부분 HIV 환자의 결핵·MAC 치료/예방 또는 약물 상호작용(PK) 평가이며, HIV 감염 자체를 치료 대상으로 한 시험은 없습니다. 관련성이 높은 시험을 정리했습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00002101](https://clinicaltrials.gov/study/NCT00002101) | Phase 3 | 완료 | 450 | AIDS 환자의 MAC 균혈증에서 clarithromycin/ethambutol에 Rifabutin 두 용량 또는 위약을 비교 |
| [NCT00001047](https://clinicaltrials.gov/study/NCT00001047) | Phase 3 | 완료 | 400 | AIDS 환자의 파종성 MAC에서 4가지 병용요법(Rifabutin 또는 clofazimine 포함) 비교 |
| [NCT00001030](https://clinicaltrials.gov/study/NCT00001030) | Phase 3 | 완료 | 1100 | HIV 환자의 MAC 예방에서 clarithromycin, Rifabutin, 병용 비교 |
| [NCT00002122](https://clinicaltrials.gov/study/NCT00002122) | Phase 3 | 완료 | 720 | HIV 환자의 파종성 MAC 예방에서 azithromycin·Rifabutin 단독/병용 비교 |
| [NCT00001995](https://clinicaltrials.gov/study/NCT00001995) | 해당 없음 | 완료 | 200 | AIDS 환자의 MAC 균혈증에서 Rifabutin 요법의 이중맹검 무작위 시험 |
| [NCT00001058](https://clinicaltrials.gov/study/NCT00001058) | Phase 2 | 완료 | 246 | AIDS 환자의 파종성 MAC에서 clarithromycin 기반 3가지 병용요법 비교 |
| [NCT00651066](https://clinicaltrials.gov/study/NCT00651066) | Phase 2 | 완료 | 47 | 베트남 결핵/HIV 환자에서 Rifabutin과 항레트로바이러스 요법의 약동학 |
| [NCT00640887](https://clinicaltrials.gov/study/NCT00640887) | Phase 2 | 완료 | 48 | 남아프리카 결핵/HIV 환자에서 Rifabutin과 항레트로바이러스 요법의 약동학 |
| [NCT00810446](https://clinicaltrials.gov/study/NCT00810446) | 해당 없음 | 완료 | 72 | HIV 환자에서 Mycobutin 사용 시 시판 후 안전성 조사 |
| [NCT00000877](https://clinicaltrials.gov/study/NCT00000877) | Phase 1 | 완료 | 31 | Indinavir와 Rifabutin의 정상 상태 약물 상호작용 |

## 문헌 근거

대부분 HIV 환자의 결핵·MAC 관리, 약물 상호작용, 약동학에 관한 문헌이며, HIV 감염 자체의 치료 효과를 평가한 연구는 없습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [28233512](https://pubmed.ncbi.nlm.nih.gov/28233512/) | 2017 | Review | Microbiol Spectr | HIV와 결핵의 상호 영향 및 병용 치료 고찰 |
| [17181373](https://pubmed.ncbi.nlm.nih.gov/17181373/) | 2006 | Review | Drugs | HIV/결핵 동시감염의 실용적 치료 접근, 리파마이신과 항레트로바이러스제의 상호작용 |
| [21819645](https://pubmed.ncbi.nlm.nih.gov/21819645/) | 2012 | 문헌 분석 | Int J Tuberc Lung Dis | 프로테아제 억제제 포함 ART와 결핵 치료에서 Rifabutin의 대체 가능성 |
| [33294914](https://pubmed.ncbi.nlm.nih.gov/33294914/) | 2021 | Cohort | J Antimicrob Chemother | 결핵/HIV 동시감염 소아에서 Rifabutin 약동학과 안전성 |
| [31139825](https://pubmed.ncbi.nlm.nih.gov/31139825/) | 2019 | Cohort | J Antimicrob Chemother | 소아에서 Rifabutin의 안전성과 효능, 중성구감소증 우려 |
| [36385424](https://pubmed.ncbi.nlm.nih.gov/36385424/) | 2023 | PK 모델링 | Br J Clin Pharmacol | Rifabutin과 dolutegravir 병용 시 집단 약동학 모델 |
| [10456381](https://pubmed.ncbi.nlm.nih.gov/10456381/) | 1999 | Review | Drug Saf | MAC 감염 치료제의 위험-이익 평가 |
| [9093233](https://pubmed.ncbi.nlm.nih.gov/9093233/) | 1997 | Review | Med Clin North Am | AIDS 환자의 비결핵 마이코박테리아 감염과 치료 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200400200 | 유유마이코부틴캡슐(리파부틴) | 경질캡슐제 | 적응증 본문은 링크로만 제공되어 확인 불가 (식약처 허가사항 참조) |

## 세포독성

해당 약물은 항종양약이 아니므로 이 섹션은 적용되지 않습니다.

## 안전성 고려사항

- **약물 상호작용**: 수집된 상호작용 정보는 총 100건이며, 이 중 대표 항목은 다음과 같습니다.
  - 주요(Major): Eliglustat
  - 중등도(Moderate): Clarithromycin, Doxycycline, Metronidazole, Morphine, Aprepitant, Pioglitazone, Dexamethasone, Hydrocortisone 등
  - 경미(Minor): Dolasetron
- 임상시험·문헌에서는 항레트로바이러스제(프로테아제 억제제, 신약 후보 등)와의 병용 시 약물 농도 변화가 반복적으로 평가되었으며, 소아에서 중성구감소증이 보고되었습니다.

그 외 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
수집된 연구는 HIV 환자의 결핵·MAC 치료/예방과 약물 상호작용에 관한 것이며, HIV 감염 자체를 치료 대상으로 한 연구가 없습니다. Rifabutin에는 항레트로바이러스 기전이 없어 높은 예측 점수(0.9988)만으로는 HIV 감염증 적응증을 뒷받침하기 어렵습니다.

**진행하려면 필요한 것:**
- HIV 감염 자체에 대한 효과를 평가한 직접적인 임상시험 또는 전임상 근거
- 상세한 작용 기전(MOA) 데이터 확보
- 허가사항의 경고 및 금기 정보 확인
- 항레트로바이러스제 병용 시 상호작용 관리 계획

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

