---
layout: default
title: Paclitaxel
parent: 높은 근거 (L1-L2)
nav_order: 529
evidence_level: L1
indication_count: 10
---

# Paclitaxel
{: .fs-9 }

근거 수준: **L1** | 예측 적응증: **10** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 약사 평가 보고서

</div>

# Paclitaxel: 적응증 데이터 미확보에서 유방암(Female Breast Carcinoma)으로

## 한 문장 요약

Paclitaxel(紫杉醇, DrugBank ID DB01229)은 미세관 안정화 기전을 가진 세포독성 항암제로, 본 Evidence Pack에는 한국 허가 이력 및 원 적응증 데이터가 확보되어 있지 않습니다.
TxGNN 모델은 **유방암(Female Breast Carcinoma)**에 효과가 있을 것으로 예측(점수 99.99%)하며, 현재 **20편의 문헌**이 이를 뒷받침합니다. 다만 근거 자료 자체가 명시하듯, 이는 이미 전 세계적으로 확립된 Paclitaxel의 표준 치료 적응증과 일치하여 **엄밀한 의미의 "노리포지셔닝(신규 재창출) 후보"라기보다는 모델 예측 정확도를 검증하는 사례**에 가깝습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 미확보 (한국 허가 이력 없음, `original_indications` 필드 공란) |
| 예측 신규 적응증 | 유방암 (Female Breast Carcinoma) — 단, 국제적으로 이미 확립된 표준 적응증 |
| TxGNN 예측 점수 | 99.99% (rank 241) |
| 근거 수준 | L1 |
| 한국 시판 현황 | 미출시 (허가 제품 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails (단, 아래 유의사항 참고) |

---

## 이 예측이 타당한 이유는?

Evidence Pack의 `original_moa` 필드는 데이터 누락(Blocking-level 데이터 갭, DG002)으로 표시되어 있으나, Paclitaxel은 약리학적으로 잘 알려진 약물입니다. β-tubulin에 결합하여 미세관을 비정상적으로 안정화시키고, 유사분열 방추사의 정상적 해중합을 억제함으로써 세포주기를 G2/M기에 정지시키고 세포자멸사(apoptosis)를 유도하는 것이 핵심 기전입니다.

이러한 미세관 표적 세포독성 기전은 빠르게 증식하는 유방암 세포에 특히 효과적이며, 실제로 Paclitaxel은 전이성·조기 유방암 치료의 표준 화학요법 약제(단독 또는 trastuzumab·pertuzumab·atezolizumab·pembrolizumab 등과 병용)로 이미 광범위하게 사용되고 있습니다.

**주의:** 근거 자료에 포함된 재창출 근거(rationale)는 이 적응증이 "Paclitaxel의 이미 승인된 표준 치료이며, 노리포지셔닝 후보가 아니다"라고 명시적으로 밝히고 있습니다. 즉 본 예측은 TxGNN 모델이 알려진 임상적 사실과 일치하는 결과를 냈다는 **검증 사례(validation case)**로 해석하는 것이 정확합니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다. (해당 예측 적응증에 직접 매핑된 `clinical_trials` 데이터 없음)

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | RCT | Cancer | 전이성 유방암에서 doxorubicin+paclitaxel 병용요법의 효능·독성 평가 Phase II 다기관 시험 |
| [32461977](https://pubmed.ncbi.nlm.nih.gov/32461977/) | 2020 | Cohort/Clinical Study | BioMed Research International | HER2 양성 유방암에서 epirubicin/cyclophosphamide + weekly paclitaxel-trastuzumab 신보조요법의 실사용 효능 평가 |
| [31783552](https://pubmed.ncbi.nlm.nih.gov/31783552/) | 2019 | Review | Biomolecules | Paclitaxel의 유방암 기전 및 임상 효과, 내성 문제에 대한 종합 리뷰 |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug and Therapeutics Bulletin | 유방암·난소암에서 Paclitaxel/Docetaxel 초기 승인 경과 및 임상적 근거 리뷰 |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | Preclinical/Combination Study | Chemical Biology & Drug Design | 환자유래 유방암 모델에서 Paclitaxel 병용요법의 바이오마커 탐색 |
| [31515668](https://pubmed.ncbi.nlm.nih.gov/31515668/) | 2019 | (분류 미정) | Cancer Chemotherapy and Pharmacology | SRSF3 하향조절을 통한 구강편평세포암·유방암의 Paclitaxel 감수성 증가 기전 연구 |
| [39009452](https://pubmed.ncbi.nlm.nih.gov/39009452/) | 2024 | (분류 미정) | Journal for ImmunoTherapy of Cancer | 삼중음성유방암에서 Paclitaxel이 종양연관대식세포를 통해 PD-1 차단 효과를 증강시키는 기전 |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | (분류 미정) | Nature Communications | TEKT4 유전자 변이와 유방암의 Paclitaxel 내성 간 연관성 규명 |
| [20665703](https://pubmed.ncbi.nlm.nih.gov/20665703/) | 2011 | (분류 미정) | Journal of Cellular Physiology | ZD6474가 유방암세포에서 Paclitaxel의 항증식·세포자멸사 효과를 증강시킨다는 전임상 연구 |
| [36964413](https://pubmed.ncbi.nlm.nih.gov/36964413/) | 2023 | (분류 미정) | Human Cell | TIPE2가 자가포식 및 암줄기세포 특성 억제를 통해 유방암세포의 Paclitaxel 감수성을 높인다는 연구 |

---

## 한국 시판 정보

한국에 등록된 허가 제품이 없습니다 (`total_licenses` = 0, `market_status` = 미출시). Paclitaxel 성분 자체는 전 세계적으로 널리 사용되는 항암제이나, 본 Evidence Pack 기준으로는 한국 내 허가 이력이 확인되지 않았습니다.

---

## 세포독성 (항종양약)

Paclitaxel은 taxane 계열의 대표적 세포독성 화학요법제로, 다음은 해당 약물 클래스에 대한 일반적 임상 정보입니다 (DrugBank 상세 toxicity 데이터는 미확보 상태이므로 국내 허가사항 확인 필요).

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (Taxane계, 미세관 안정화제) |
| 골수억제 위험 | 高 — 호중구감소증(neutropenia)이 흔하며, 발열성 호중구감소증 위험 존재 |
| 구토 유발성 등급 | 중등도 (moderate emetogenic potential) |
| 모니터링 항목 | CBC(특히 호중구 수), 간기능, 말초신경병증(감각이상) 여부, 투여 전 과민반응 예방 전처치 필요 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 (조제·투여 시 개인보호장비 착용) |

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails (단, 조건부)**

**사유:**
- 문헌 근거 수준은 L1(다수 임상연구 포함)로 충분하나, 근거 자료 자체가 이 적응증을 "이미 확립된 표준치료이며 신규 재창출 후보가 아님"이라고 명시하고 있어 실질적인 **재창출(repurposing) 가치는 제한적**입니다.
- 한국 허가·시판 데이터, MOA 공식 자료, 안전성 경고 정보가 모두 미확보 상태(Blocking-level 데이터 갭 DG001 포함)로, S1 안전성 초기평가 단계 진입이 현재 불가능합니다.

**진행하려면 필요한 것:**
- 한국 허가사항(경고/금기/DDI) 원문 확보 — 식약처 자료 기반 (DG001, Blocking)
- DrugBank API를 통한 공식 MOA·독성 데이터 확보 (DG002, High)
- 한국 내 실제 허가·시판 여부 재확인 (현재 데이터상 미출시로 표시되었으나 실제 제네릭 유통 여부 교차 검증 필요)
- 진정한 신규 재창출 신호를 찾기 위해서는 본 Evidence Pack의 다른 예측 적응증(rank 9~10 등 완전 미지 적응증, 현재 L5/Hold)에 대한 추가 전임상 검증이 더 유의미할 수 있음
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

