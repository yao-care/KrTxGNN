---
layout: default
title: Docetaxel
parent: 모델 예측만 (L5)
nav_order: 284
evidence_level: L5
indication_count: 10
---

# Docetaxel
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

# Docetaxel: 유방암 등 기허가 항종양 적응증에서 여성 유방암(Female Breast Carcinoma)으로

## 한 문장 요약

Docetaxel은 미세소관을 안정화하는 탁산(taxane)계 세포독성 항암제로, 한국에서 단일 성분 주사제 6건이 허가되어 시판되고 있습니다. TxGNN 모델은 **여성 유방암(female breast carcinoma)**에 효과가 있을 수 있다고 예측하며(예측 점수 99.90%), 이 방향을 지지하는 **임상시험 46건**(이 중 상위 10건 표시)과 **문헌 20편**이 확인됩니다. 다만 이 적응증은 이미 허가 범위에 포함되어 있을 가능성이 높아, 새로운 재창출이라기보다 기존 용도의 확인에 가깝습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에 적응증 원문이 아닌 허가사항 문서 링크만 수록되어 있어 구체적 문구는 확인되지 않음 (허가사항 참조 필요) |
| 예측 신규 적응증 | 여성 유방암 (Female Breast Carcinoma) |
| TxGNN 예측 점수 | 99.90% |
| 근거 수준 | L1 (완료된 Phase 3 RCT 다수) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 6건 (모두 유효, 단일 성분) |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Docetaxel은 미세소관을 안정화하여 유사분열 방추체의 해체를 막고, G2/M기 정지와 세포자멸사를 일으키는 탁산계 항암제입니다. 빠르게 분열하는 종양 세포에 작용하는 기전이므로 유방암에도 적용될 수 있습니다.

유방암에서는 Docetaxel 병용요법을 평가한 대규모 Phase 3 연구가 다수 완료되어 있습니다. 문헌에는 조기 유방암에서 docetaxel+cyclophosphamide(TC)와 안트라사이클린 기반 요법을 비교한 ABC 시험(PMID 28398846)이 포함되어 있습니다. 다만 이 적응증은 이미 시판 허가 범위일 가능성이 높으므로, 이번 예측은 신규 적응증 발굴이라기보다 기존 용도를 재확인하는 성격입니다.

## 임상시험 근거

이 적응증과 관련해 총 46건이 확인되었으며, 관련성이 높은 대표 10건을 정리했습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00003782](https://clinicaltrials.gov/study/NCT00003782) | Phase 3 | 완료 | 5351 | 림프절 양성 유방암 보조요법에서 AC-T, AT, ATC 3개 요법 비교 |
| [NCT00433589](https://clinicaltrials.gov/study/NCT00433589) | Phase 3 | 완료 | 6600 | MINDACT: 70개 유전자 검사로 보조화학요법 대상 선별 |
| [NCT00021255](https://clinicaltrials.gov/study/NCT00021255) | Phase 3 | 완료 | 3222 | HER2 양성 보조요법에서 AC-T, AC-TH, TCH 비교 |
| [NCT00003519](https://clinicaltrials.gov/study/NCT00003519) | Phase 3 | 완료 | 2778 | 림프절 양성 또는 고위험 유방암 보조요법에서 AT vs AC 비교 |
| [NCT00002707](https://clinicaltrials.gov/study/NCT00002707) | Phase 3 | 완료 | 2411 | 수술 전 AC 후 docetaxel 추가 여부 비교 |
| [NCT00887536](https://clinicaltrials.gov/study/NCT00887536) | Phase 3 | 완료 | 1613 | HER2 음성 유방암에서 TC+베바시주맙 vs TC vs TAC 비교 |
| [NCT00333775](https://clinicaltrials.gov/study/NCT00333775) | Phase 3 | 완료 | 736 | HER2 음성 전이성 유방암 1차 치료에서 베바시주맙+docetaxel vs docetaxel+위약 |
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Phase 3 | 완료 | 652 | HER2 양성 전이성 유방암에서 탁산+라파티닙 vs 탁산+트라스투주맙 |
| [NCT03588091](https://clinicaltrials.gov/study/NCT03588091) | Phase 3 | 완료 | 355 | HER2 양성 유방암 수술 전 치료에서 피로티닙+트라스투주맙+docetaxel vs 위약 병용 |
| [NCT00321633](https://clinicaltrials.gov/study/NCT00321633) | Phase 2 | 완료 | 148 | 전이성 유전성 유방암에서 carboplatin과 docetaxel을 직접 비교한 무작위 시험 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | RCT | J Clin Oncol | ABC 시험: 조기 유방암에서 TC 6주기와 탁산 포함 안트라사이클린 요법(TaxAC)을 비교 |
| [10791395](https://pubmed.ncbi.nlm.nih.gov/10791395/) | 2000 | Review | Lancet | 탁산류 개관: docetaxel과 paclitaxel은 진행성 유방암·폐암·난소암 치료의 근거 기반 요법 |
| [18624687](https://pubmed.ncbi.nlm.nih.gov/18624687/) | 2008 | Review | Expert Opin Drug Metab Toxicol | Docetaxel 개발 과정에서 얻은 약리·약동학 교훈 |
| [12868800](https://pubmed.ncbi.nlm.nih.gov/12868800/) | 2003 | Review | Breast Cancer Res Treat | 전이성 유방암에서 docetaxel-안트라사이클린 병용 근거 정리 |
| [9775340](https://pubmed.ncbi.nlm.nih.gov/9775340/) | 1998 | Review | Am J Health Syst Pharm | 전이성 유방암 치료제로서 docetaxel의 약리, 약동학, 임상시험, 이상반응 정리 |
| [16020974](https://pubmed.ncbi.nlm.nih.gov/16020974/) | 2005 | Phase 2 | Oncology | 전이성 유방암 1차 치료로 주 1회 docetaxel+gemcitabine의 효능·독성 평가 |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | Phase 2 | Cancer | 진행성 유방암 1차 치료로 capecitabine+docetaxel+epirubicin 병용 평가 |
| [19856651](https://pubmed.ncbi.nlm.nih.gov/19856651/) | 2009 | 용량 탐색 연구 | Tumori | 전이성 유방암에서 docetaxel+gemcitabine 용량 탐색 |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | 후향 연구 | Anti-Cancer Drugs | 보조 docetaxel 요법과 유방암 관련 림프부종의 연관성 평가 |
| [30991918](https://pubmed.ncbi.nlm.nih.gov/30991918/) | 2019 | 전임상 | Ther Deliv | Docetaxel과 알파리포산 공동 탑재 나노입자의 유방암 세포 효과 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201001267 | 탁셀로주(도세탁셀삼수화물) | 주사제 (본액 바이알+용매 바이알) | 허가사항 문서 참조 |
| 200907781 | 탁소젠주사(도세탁셀삼수화물) | 주사제 (본액 바이알+용매 바이알) | 허가사항 문서 참조 |
| 201004765 | 뉴탁셀에이주(도세탁셀삼수화물) (수출용) | 주사제 (본액 바이알+용매 바이알) | 허가사항 문서 참조 |
| 201502916 | 베로탁셀1-바이알주 (수출용) | 주사제 (1-바이알) | 허가사항 문서 참조 |
| 201110777 | 디탁셀1-바이알주(도세탁셀삼수화물) | 주사제 (1-바이알) | 허가사항 문서 참조 |

위 외에 베로탁셀1-바이알주(도세탁셀삼수화물, 허가번호 201300021, 종근당)가 추가로 허가되어 있어 총 6건입니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (탁산계, 미세소관 안정화제) |
| 골수억제 위험 | 고 (호중구감소증 및 발열성 호중구감소증 모니터링 필요) |
| 구토 유발성 등급 | 저~중등도 |
| 모니터링 항목 | CBC(분류 포함), 간기능, 체액 저류, 말초신경병증 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

허가사항의 경고 및 주의사항을 함께 참조하세요.

## 안전성 고려사항

- **약물 상호작용**: 이번에 수집된 데이터에서 총 100건의 상호작용이 확인되었으며, 일부를 아래에 정리했습니다. 이 약은 CYP3A4 관련 상호작용 부담이 큽니다.
  - **Major**: Clarithromycin
  - **Moderate**: Aprepitant, Metronidazole, Cimetidine, Eliglustat, Miconazole, Rolapitant, Rosuvastatin, Simvastatin, Tinidazole, Troglitazone
  - **Minor**: Dexamethasone, Levofloxacin, Prednisolone, Prednisone

허가사항 기반의 경고·금기 정보는 이번 데이터에 포함되어 있지 않으므로, 상세 내용은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
유방암에서 Docetaxel의 효능을 지지하는 Phase 3 RCT가 다수 완료되어 있어 근거 수준은 L1입니다. 다만 이 적응증은 이미 허가 범위에 포함될 가능성이 높아 재창출보다는 기존 적응증 확인에 해당하며, 호중구감소증 등 독성과 약물 상호작용 관리가 필요합니다.

**진행하려면 필요한 것:**
- MFDS 허가사항(경고·금기·적응증 원문) 확인 및 유방암이 기존 허가 적응증에 포함되는지 검증
- 상세한 작용 기전 데이터(MOA) 보완
- 호중구감소증·발열성 호중구감소증 모니터링, 간기능에 따른 용량 조정, 체액 저류·신경병증 관리 계획
- CYP3A4 관련 병용약물(예: clarithromycin) 점검 체계

## 참고: 기타 예측 적응증 요약

| 순위 | 예측 적응증 | 근거 수준 | 권장 |
|-----|-----------|----------|------|
| 2 | 유잉 육종 | L2 | Research Question |
| 3 | 고분화 태아형 폐 선암 | L4 | Hold |
| 4 | 소세포폐암 | L4 | Hold |
| 5 | 원발성 폐 림프종 | L5 | Hold |
| 6 | 질 포도상 배아형 횡문근육종 | L5 | Hold |
| 7 | 폐 모세포종 | L4 | Hold |
| 8 | 횡문근육종 | L2 | Research Question |
| 9 | 배아형 간외담관 횡문근육종 | L5 | Hold |
| 10 | 부수막 배아형 횡문근육종 | L5 | Hold |

소세포폐암의 경우 제공된 근거 대부분이 비소세포폐암(NSCLC) 관련이어서 직접 외삽은 어렵습니다. 유잉 육종과 횡문근육종은 gemcitabine 병용 중심의 소규모 Phase 2 근거에 그쳐, Docetaxel 단독 기여도는 불분명합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

