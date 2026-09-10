---
layout: default
title: Carboplatin
parent: 僅模型預測 (L5)
nav_order: 176
evidence_level: L5
indication_count: 10
---

# Carboplatin
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

# Carboplatin: 백금 계열 세포독성 항암제에서 유방암(Female Breast Carcinoma)으로

## 한 문장 요약

Carboplatin은 DNA에 교차결합을 형성해 종양세포를 사멸시키는 백금 계열 세포독성 항암제입니다. 한국 내 허가 자료가 없어 정확한 기존 승인 적응증은 확인되지 않지만, TxGNN 모델은 **유방암(Female Breast Carcinoma)**에 효과가 있을 것으로 예측하며, 현재 **다수의 Phase 2/3 임상시험**과 **20편의 문헌**이 이 방향을 뒷받침합니다(근거수준 **L1**).

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 자료 없음 (한국 미상장, MOA·적응증 원본 자료 미확보) |
| 예측 신규 적응증 | 유방암 (Female Breast Carcinoma) |
| TxGNN 예측 점수 | 99.86% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✗ 미상장 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

Carboplatin의 상세한 작용기전(MOA) 원본 자료는 이번 Evidence Pack에서 확보되지 않았습니다. 다만 여러 예측 적응증에 걸쳐 반복적으로 제시된 기전 정보에 따르면, Carboplatin은 백금 화합물로서 DNA에 교차결합(cross-link)을 형성해 DNA 복제·전사를 저해함으로써 세포 사멸을 유도하는 세포독성 항암제입니다.

이 기전은 BRCA1/2 등 상동재조합 복구(homologous recombination repair) 결함이 있는 종양, 즉 삼중음성유방암(TNBC)이나 유전성 유방난소암증후군(HBOC) 환자의 종양에서 특히 효과적인 것으로 알려져 있습니다(합성치사 효과). 실제로 Carboplatin과 Paclitaxel 병용요법(또는 Docetaxel/Trastuzumab과의 병용인 TCH 요법)은 TNBC 및 HER2 양성 유방암의 선행보조·전이성 치료에서 이미 널리 쓰이는 요법으로, 이는 TxGNN 예측의 기전적 타당성을 뒷받침합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00005963](https://clinicaltrials.gov/study/NCT00005963) | Phase 2 | 완료 | 53 | Docetaxel+Carboplatin 1차 전이성 유방암 치료 |
| [NCT02978495](https://clinicaltrials.gov/study/NCT02978495) | Phase 2 | 완료 | 154 | NACATRINE: TNBC 선행보조 Carboplatin 전향적 연구 |
| [NCT04095364](https://clinicaltrials.gov/study/NCT04095364) | Phase 3 | 진행중(비모집) | 450 | Paclitaxel/Carboplatin+Letrozole 유지요법 vs Letrozole 단독 |
| [NCT00021255](https://clinicaltrials.gov/study/NCT00021255) | Phase 3 | 완료 | 3222 | AC-T vs AC-TH vs TCH(Docetaxel+Carboplatin+Trastuzumab) 보조요법, HER2+ 유방암 |
| [NCT00047255](https://clinicaltrials.gov/study/NCT00047255) | Phase 3 | 완료 | 263 | Docetaxel+Trastuzumab ± Carboplatin 1차 HER2+ 전이성 유방암 |
| [NCT01445418](https://clinicaltrials.gov/study/NCT01445418) | Phase 1 | 완료 | 103 | PARP억제제(Olaparib)+Carboplatin, BRCA1/2 변이 유방·난소암 |
| [NCT01237067](https://clinicaltrials.gov/study/NCT01237067) | Phase 1 | 완료 | 77 | Olaparib+Carboplatin PK/PD 연구 |
| [NCT01618136](https://clinicaltrials.gov/study/NCT01618136) | Phase 1/2 | 완료 | 41 | PARP억제제(E7449)+Carboplatin/Paclitaxel 병용 |
| [NCT03076372](https://clinicaltrials.gov/study/NCT03076372) | Phase 1 | 상태 미상 | 34 | MM-310(도세탁셀 전구약물) 병용 초기 연구 |
| [NCT00616967](https://clinicaltrials.gov/study/NCT00616967) | Phase 2 | 진행중(비모집) | 68 | Carboplatin+Nab-paclitaxel ± Vorinostat, HER2 음성 수술전 화학요법 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [24794243](https://pubmed.ncbi.nlm.nih.gov/24794243/) | 2014 | RCT | Lancet Oncol | GeparSixto: TNBC·HER2+ 조기유방암 선행보조 Carboplatin 추가 효과 |
| [33208340](https://pubmed.ncbi.nlm.nih.gov/33208340/) | 2021 | RCT | Clin Cancer Res | NeoSTOP: TNBC 안트라사이클린 유무 Carboplatin 요법 비교 |
| [39671272](https://pubmed.ncbi.nlm.nih.gov/39671272/) | 2025 | RCT | JAMA | CamRelief: Camrelizumab+화학요법(Carboplatin 포함) 선행보조 TNBC |
| [40593759](https://pubmed.ncbi.nlm.nih.gov/40593759/) | 2025 | RCT | Nat Commun | ARX788+Pyrotinib vs TCbHP(Carboplatin 포함), HER2+ 유방암 |
| [33256829](https://pubmed.ncbi.nlm.nih.gov/33256829/) | 2020 | Phase 2 Trial | Breast Cancer Res | Carboplatin+Bevacizumab, 유방암 뇌전이 환자 대상 |
| [38309017](https://pubmed.ncbi.nlm.nih.gov/38309017/) | 2024 | RCT (Phase 3) | Eur J Cancer | BROCADE3: Veliparib+Carboplatin+Paclitaxel, BRCA변이 유방암 최종 OS 결과 |
| [16720915](https://pubmed.ncbi.nlm.nih.gov/16720915/) | 2006 | Review | Med Oncol | Paclitaxel-Carboplatin 병용의 시너지·효능·안전성 근거 종합 |
| [8893899](https://pubmed.ncbi.nlm.nih.gov/8893899/) | 1996 | Cohort | Semin Oncol | Paclitaxel 및 Carboplatin 단독/병용, 진행성 유방암 |
| [40779028](https://pubmed.ncbi.nlm.nih.gov/40779028/) | 2025 | Cohort | Breast Cancer Res Treat | Carboplatin+Gemcitabine+Mifepristone, 진행성 유방암·난소암 |
| [25247558](https://pubmed.ncbi.nlm.nih.gov/25247558/) | 2014 | Meta-analysis | PLoS One | Carboplatin·Bevacizumab이 TNBC 선행보조 병리학적 완전관해율 개선 |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (백금(Platinum) 계열, DNA 교차결합제) |
| 골수억제 위험 | 고위험 — 백금 계열 공통적으로 혈소판감소증이 특히 흔하게 발생. 구체적 발생률 자료는 이번 Evidence Pack에 확보되지 않아 허가사항 참조 필요 |
| 구토 유발성 등급 | 중등도~고위험 |
| 모니터링 항목 | CBC(혈소판 포함), 신기능(BUN/Cr, GFR), 전해질, 청력검사(이독성 가능성) |
| 취급 방호 | 세포독성 항암제 취급 규정 준수 필요 (조제·투여 시 개인보호구 착용, 폐기물 별도 처리) |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
다수의 완료·진행중 Phase 2/3 임상시험과 RCT 문헌이 TNBC 및 HER2 양성 유방암에서 Carboplatin 병용요법의 확립된 임상적 지위를 뒷받침하여(L1) 예측 신뢰도는 높으나, 한국 내 허가·MOA·안전성 원본 자료가 확보되지 않아(Blocking data gap) 곧바로 임상 적용을 권고하기는 어렵습니다.

**진행하려면 필요한 것:**
- 관계 당국(TFDA 등) 공식 허가사항 및 경고·금기 정보 확보
- DrugBank 등에서 정확한 작용기전(MOA) 및 독성 프로파일 확인
- 유방암 아형(TNBC vs HR+/HER2+)별 반응 차이를 반영한 임상 프로토콜 설계
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

