---
layout: default
title: Oxaliplatin
parent: 僅模型預測 (L5)
nav_order: 523
evidence_level: L5
indication_count: 4
---

# Oxaliplatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Oxaliplatin: 백금계 세포독성 화학요법제에서 악성 흉막 중피종으로

## 한 문장 요약

Oxaliplatin은 제3세대 백금계(Platinum) 세포독성 화학요법제입니다. 다만 이번 Evidence Pack에는 한국 내 기존 허가·적응증 정보가 없습니다(한국 미시판).
TxGNN 모델은 **악성 흉막 중피종(Malignant Pleural Mesothelioma)**에 효과가 있을 수 있다고 예측하며,
현재 **5건의 임상시험**(그중 완료된 Phase 2 시험 포함)과 **20편의 문헌**이 이 방향을 지지합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (한국 허가 정보 미확보, DG001 Blocking) |
| 예측 신규 적응증 | 악성 흉막 중피종 (Malignant Pleural Mesothelioma) |
| TxGNN 예측 점수 | 99.68% |
| 근거 수준 | L2 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 DrugBank 등록 정보에는 상세한 작용기전(MOA) 데이터가 없습니다(DG002, High severity). 다만 근거 자료(repurposing rationale)에 따르면, Oxaliplatin은 제3세대 백금계 세포독성 화학요법제로 DNA에 백금-DNA 부가물(adduct)을 형성하여 DNA 복제와 전사를 억제하고 암세포 사멸(apoptosis)을 유도하는 것으로 알려져 있습니다.

악성 흉막 중피종(MPM)의 표준 치료는 백금계 약물(Cisplatin)과 Pemetrexed 병용요법입니다. Oxaliplatin은 동일 계열(platinum class) 약물로, 기전상 Cisplatin의 대체제로 적용 가능하며 특히 신기능 저하나 Cisplatin 불내성 환자에게 대안이 될 수 있습니다. 실제로 Gemcitabine, Raltitrexed, Vinorelbine 등과의 병용요법으로 MPM에서 다수의 Phase 2 임상시험이 완료되어 이 기전적 타당성을 뒷받침합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00859469](https://clinicaltrials.gov/study/NCT00859469) | Phase 2 | 완료 | 29 | Oxaliplatin+Gemcitabine을 MPM/복막 중피종의 1차 또는 2차 화학요법으로 평가한 시험. 약물-적응증 직접 대응 |
| [NCT00996385](https://clinicaltrials.gov/study/NCT00996385) | Phase 2 | 불명 | 29 | Velcade(Bortezomib)+Eloxatin(Oxaliplatin) 병용, 기치료 MPM/복막 중피종 환자 대상 2단계 시험 |
| [NCT03210298](https://clinicaltrials.gov/study/NCT03210298) | N/A | 불명 | 1000 | PIPAC(복강 내 가압 에어로졸 화학요법) 다기관 국제 등록 연구, 악성 흉막/복막 질환 치료 관찰 |
| [NCT05107674](https://clinicaltrials.gov/study/NCT05107674) | Phase 1 | 모집 중 | 345 | CBL-B 억제제 NX-1607 1상 시험, 진행성 악성종양(중피종 일부 포함) 대상 |
| [NCT06310473](https://clinicaltrials.gov/study/NCT06310473) | Phase 2 | 모집 예정 | 30 | 국소진행성 식도위접합부/위암 대상 Cadonilimab+화학요법 신보조요법 시험 (간접 관련) |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [14609447](https://pubmed.ncbi.nlm.nih.gov/14609447/) | 2003 | Phase 2 임상시험 | Clinical Lung Cancer | Gemcitabine+Oxaliplatin 병용, MPM 환자 25명 대상 다기관 2상 시험 |
| [12525529](https://pubmed.ncbi.nlm.nih.gov/12525529/) | 2003 | Phase 2 임상시험 | J Clin Oncol | Raltitrexed+Oxaliplatin 병용, MPM 환자 70명 대상 2상 시험 결과 |
| [11989592](https://pubmed.ncbi.nlm.nih.gov/11989592/) | 2001 | 코호트(Pilot) | Tumori | Oxaliplatin+Raltitrexed, 수술 불가능 MPM 파일럿 연구 |
| [19091133](https://pubmed.ncbi.nlm.nih.gov/19091133/) | 2008 | 관찰연구 | J Occup Med Toxicol | Pemetrexed 치료 후 재발 MPM에서 Oxaliplatin±Gemcitabine 효능·안전성 평가 |
| [15639727](https://pubmed.ncbi.nlm.nih.gov/15639727/) | 2005 | Phase 2 임상시험 | Lung Cancer | Vinorelbine+Oxaliplatin, 미치료 MPM 1차 치료 2상 시험 |
| [15893013](https://pubmed.ncbi.nlm.nih.gov/15893013/) | 2005 | Phase 2 임상시험 | Lung Cancer | Raltitrexed-Oxaliplatin 2차 치료, 반응률 낮음(음성 결과, 안전성은 양호) |
| [31455014](https://pubmed.ncbi.nlm.nih.gov/31455014/) | 2019 | Review | Int J Mol Sci | Cisplatin/Oxaliplatin/Pemetrexed이 MPM 면역관문 발현에 미치는 영향, 면역치료 병용 근거 |
| [12601280](https://pubmed.ncbi.nlm.nih.gov/12601280/) | 2003 | Review | Curr Opin Oncol | MPM 화학요법 최신 동향, Platinum 병용요법의 반응률 개선 |
| [12610498](https://pubmed.ncbi.nlm.nih.gov/12610498/) | 2003 | Review | Br J Cancer | MPM 화학요법 과거 결과 및 최신 개발 동향 종합 |
| [10930799](https://pubmed.ncbi.nlm.nih.gov/10930799/) | 2000 | Review(임상시험 7건) | Eur J Cancer | 중피종 환자 163명, 9년간 Raltitrexed-Oxaliplatin 병용요법 경험 종합 |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (백금계/Platinum-based agent, 제3세대) |
| 골수억제 위험 | 데이터 없음 - 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 데이터 없음 - 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 데이터 없음 - 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 세포독성 항암제 취급 규정 준수 필요 (일반 원칙) |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
완료된 Phase 2 임상시험(NCT00859469)과 다수의 코호트/2상 연구가 Oxaliplatin 기반 병용요법의 MPM 치료 가능성을 뒷받침하며, 백금계 약물로서의 기전적 타당성도 명확합니다. 다만 한국 내 허가·안전성 데이터가 전무하여(DG001 Blocking) 안전성 초기 평가(S1) 단계까지 진행이 불가능한 상태입니다.

**진행하려면 필요한 것:**
- 한국 식약처(MFDS) 허가사항(경고/금기/DDI) 원문 확보 — Blocking 항목
- DrugBank 기반 상세 MOA 및 독성 데이터 보완
- 한국 내 Oxaliplatin 기존 승인 적응증 및 시판 현황 재확인 (현재 총 0건 허가로 기록됨)
- 조직학적 아형(상피양형·육종양형 등)별 반응률 차이를 고려한 환자군 선정 기준 수립 (참고: 육종양형 아형은 근거 수준 L4로 별도 Hold 권고됨)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

