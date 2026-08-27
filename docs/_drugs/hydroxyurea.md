---
layout: default
title: Hydroxyurea
parent: 僅模型預測 (L5)
nav_order: 304
evidence_level: L5
indication_count: 10
---

# Hydroxyurea
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

# Hydroxyurea: 백혈병·겸상적혈구병에서 유방암(Female Breast Carcinoma)으로

## 한 문장 요약

Hydroxyurea는 ribonucleotide reductase 억제제 계열의 세포독성 약물로, 문헌상 백혈병·겸상적혈구병·진성다혈구증 등 골수증식성 질환 치료에 오랫동안 사용되어 온 약물입니다.
TxGNN 모델은 **유방암(Female Breast Carcinoma)**에 효과가 있을 수 있다고 예측하며, 현재 직접적인 유방암 임상시험은 등록되어 있지 않으나 **20편의 문헌**(병용요법 Phase I/II 연구 포함)이 이 방향을 뒷받침합니다. 다만 한국(자료상 "台灣/TFDA" 표기 혼재) 내 허가 정보는 확인되지 않았습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 국내 허가 자료 없음 (미상시) — 문헌상 백혈병, 겸상적혈구병 등에 사용 |
| 예측 신규 적응증 | 유방암 (Female Breast Carcinoma) |
| TxGNN 예측 점수 | 99.97% |
| 근거 수준 | L3 |
| 한국 시판 현황 | ✗ 미상시 (미허가) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 Hydroxyurea에 대한 상세한 작용 기전(MOA) 공식 데이터는 확보되지 않았습니다([Data Gap]). 다만 Evidence Pack에 포함된 예측 근거(repurposing rationale)에 따르면, Hydroxyurea는 **ribonucleotide reductase 억제제**로서 DNA 합성에 필수적인 디옥시리보뉴클레오티드 생성을 차단해 세포주기를 S기에 정지시키고, 방사선 증감 효과(radiosensitization)를 유발하는 것으로 알려져 있습니다. 이 기전은 다양한 고형암에서 화학요법 보조제/증감제로 사용되어 온 이론적 근거이기도 합니다.

최근 문헌에서는 EYA4, ATR inhibitor, RPA2 hyperphosphorylation 등 **DNA 복제 스트레스(replication stress)** 관련 기전 연구가 유방암 세포주에서 Hydroxyurea의 항종양 잠재력을 뒷받침하고 있습니다. 다만 이러한 높은 예측 점수는 "Hydroxyurea가 고전적인 DNA 합성 억제제"라는 광범위한 기전적 유사성을 반영할 가능성이 있으며, 유방암에 특이적인 신호가 아닐 수 있다는 점에 유의해야 합니다. 실제로 근거 목록의 상당수가 병용요법(combination regimen) 연구이며, Hydroxyurea 단독의 유방암 특이적 효능을 입증하는 무작위비교임상(RCT)은 아직 없습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다. (ClinicalTrials.gov, ICTRP 조회 결과 모두 0건)

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [1957839](https://pubmed.ncbi.nlm.nih.gov/1957839/) | 1991 | Phase I (병용요법) | Am J Clin Oncol | 진행성 위장관암·유방암 환자에서 5-FU+Leucovorin 후 Hydroxyurea 병용 투여(HALF regimen) Phase I 연구 |
| [7914447](https://pubmed.ncbi.nlm.nih.gov/7914447/) | 1994 | Phase I/II (병용, 자가조혈모세포이식) | Bone Marrow Transplant | 전이성 유방암에서 고용량 Cyclophosphamide+Thiotepa+Hydroxyurea 병용 후 자가조혈모세포 구제, 공고화학요법으로서 효과 보고 |
| [33631478](https://pubmed.ncbi.nlm.nih.gov/33631478/) | 2021 | Review | Pathol Res Pract | 유방암 병인에서 lncRNA의 역할에 대한 리뷰(Hydroxyurea 직접 언급 없음, 배경 기전 문헌) |
| [38211596](https://pubmed.ncbi.nlm.nih.gov/38211596/) | 2024 | Preclinical/In-silico | Drug Research | PI3K/AKT/mTOR 경로를 표적으로 한 Hydroxyurea-지질 접합체(HU-lipid conjugate) 설계, 유방암 치료 목적 세포 흡수·효능 개선 시도 |
| [37777742](https://pubmed.ncbi.nlm.nih.gov/37777742/) | 2023 | Preclinical | Mol Cancer | EYA4가 복제 스트레스 회피를 통해 유방암 진행·전이를 촉진, DNA 손상 관련 기전 연구 |
| [26844848](https://pubmed.ncbi.nlm.nih.gov/26844848/) | 2016 | Preclinical | Cancer Biother Radiopharm | Hydroxyurea 방사성표지 연구(백혈병·겸상적혈구병·HIV·건선 등 기존 용도 언급) |
| [21730979](https://pubmed.ncbi.nlm.nih.gov/21730979/) | 2011 | Preclinical | Br J Cancer | ATR 억제제 NU6027이 유방암·난소암 세포주에서 복제 스트레스 관련 기전으로 작용 |
| [32795962](https://pubmed.ncbi.nlm.nih.gov/32795962/) | 2020 | Preclinical | DNA Repair | Valproic acid가 RPA2 과인산화 매개 DNA 복구 경로를 통해 유방암 세포를 Hydroxyurea에 감작시킴 |
| [27504932](https://pubmed.ncbi.nlm.nih.gov/27504932/) | 2017 | Preclinical (In vitro) | J Cell Physiol | 혈청 기아(serum starvation) 조건에서 폐암·유방암(MCF-7) 세포의 화학저항성 특성 규명 |
| [28237610](https://pubmed.ncbi.nlm.nih.gov/28237610/) | 2017 | Case Report | Cancer Radiother | WHO grade 2 뇌수막종의 내장·골 전이 증례(유방암 병력 환자, 위험인자로 언급) |

> 참고: 상위 근거 다수는 유방암을 직접 표적으로 한 전임상/병용요법 연구이며, Hydroxyurea 단독의 유방암 적응증 확립을 위한 전용 RCT는 확인되지 않았습니다.

---

## 세포독성

**Hydroxyurea는 세포독성 항종양약(ribonucleotide reductase 억제제)으로 분류되어 본 섹션을 표시합니다.**

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 — Ribonucleotide reductase 억제제 (S기 세포주기 정지 유발) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 (Evidence Pack 내 독성 데이터 없음) |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 기전상 세포독성 항암제로 분류되므로 세포독성 약물 취급 규정 준수가 필요합니다 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 유방암 적응증에 대한 근거 수준은 L3(관찰연구/문헌 수준)로 평가되었으나, 실제로는 대부분 전임상 연구와 병용요법 Phase I/II 연구이며 유방암 특이적 RCT는 없습니다.
- 더 중요하게는, 안전성 초기평가(S1) 진입에 필요한 **TFDA/식약처 공식 경고문·금기사항 데이터가 Blocking 수준의 Data Gap(DG001)**으로 남아 있어, 안전성 평가 자체가 현재 진행 불가능한 상태입니다.
- 국내(한국) 허가 및 시판 정보도 확인되지 않아(0건), 실제 임상 적용 가능성을 판단할 규제적 근거가 부족합니다.

**진행하려면 필요한 것:**
- TFDA(또는 해당 규제기관) 공식 사용설명서(仿單)의 경고·금기사항 확보 및 파싱 (DG001, Blocking)
- DrugBank API를 통한 상세 작용 기전(MOA) 데이터 확보 (DG002, High)
- 유방암 특이적 전임상 또는 초기 임상(Phase I/II) 연구 추가 확인
- 골수억제 등 구체적 독성 프로파일 데이터 확보
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

