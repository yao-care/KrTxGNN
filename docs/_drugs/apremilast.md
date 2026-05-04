---
layout: default
title: Apremilast
parent: 僅模型預測 (L5)
nav_order: 78
evidence_level: L5
indication_count: 10
---

# Apremilast
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

# Apremilast: 건선성 관절염에서 류마티스 관절염으로

## 한 문장 요약

Apremilast는 PDE4(4형 포스포디에스테라아제) 선택적 억제제로, 미국 FDA에서 건선성 관절염 및 판상 건선 치료제로 허가된 경구용 소분자 항염증 약물이나, 현재 한국에는 허가·시판되지 않습니다.
TxGNN 모델은 이 약물이 **류마티스 관절염(Rheumatoid Arthritis)**에 효과가 있을 수 있다고 예측하며(TxGNN 점수 98.09%),
현재 **6건의 임상시험**과 **19편의 문헌**이 이 방향을 지지하지만, 핵심 Phase 2 RCT가 조기 종료되고 주요 지표에서 유의미한 차이를 입증하지 못해 근거 강도에 한계가 있습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 건선성 관절염 (국내 미허가; 미국 FDA 허가) |
| 예측 신규 적응증 | 류마티스 관절염 (Rheumatoid Arthritis) |
| TxGNN 예측 점수 | 98.09% |
| 근거 수준 | L2 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Apremilast는 PDE4를 선택적으로 억제하여 세포 내 cAMP 농도를 증가시키고, 이를 통해 TNF-α, IL-17, IL-23, IFN-γ 등 주요 염증성 사이토카인의 생성을 광범위하게 억제합니다. 이 기전은 건선성 관절염(PsA)뿐 아니라 면역 매개 활막 염증 전반에 이론적으로 적용 가능합니다.

류마티스 관절염(RA)과 건선성 관절염은 활막 염증의 핵심 경로—특히 TNF-α/IL-17 축—를 공유합니다. 두 질환 모두 TNF 억제제가 1차 표적 치료제로 사용되며, 활막 병리 기전에 상당한 중복이 존재합니다. 이는 PDE4 억제 기전이 RA 활막 염증에도 적용 가능하다는 기전적 근거가 됩니다.

전임상 단계에서 이미 의미 있는 근거가 축적되어 있습니다. 인간 RA 환자 유래 활막 세포를 이용한 ex vivo 연구(PMID 20525198)에서 Apremilast가 TNF-α의 자발적 생성을 억제함이 확인되었고, 콜라겐 유발 관절염(CIA) 마우스 모델(PMID 30072998)에서 Th1/Th17 세포 억제, 조절 T세포(Treg) 증가 및 골 미란 감소 효과가 보고되었습니다. 다만, 이러한 전임상 신호는 임상 단계에서 충분히 재현되지 않았습니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01285310](https://clinicaltrials.gov/study/NCT01285310) | Phase 2 | 조기 종료 | 237 | MTX 불충분 반응 RA 환자 대상 이중맹검 무작위 대조 시험. ACR20 반응은 일부 달성되었으나 ACR50/ACR70에서 통계적 유의차 미달. 공개 결과: PMID 25779750. 미달 효능이 종료 원인으로 추정됨 |
| [NCT01250548](https://clinicaltrials.gov/study/NCT01250548) | Phase 2 | 완료 | 34 | 활동성 RA 환자에서 Apremilast의 안전성, 반응 발현 시간 및 지속 효능 평가. 소규모(n=34)이나 개념 검증(PoC) 근거 제공 |
| [NCT01204138](https://clinicaltrials.gov/study/NCT01204138) | Phase 2 | 철회 | 0 | TNF 억제제 병용 중인 RA 환자 대상 크로스오버 연구로 계획되었으나, 입록 시작 전 철회—유효 데이터 없음 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [25779750](https://pubmed.ncbi.nlm.nih.gov/25779750/) | 2015 | Phase 2 RCT | Arthritis & Rheumatology | MTX 불충분 반응 RA 환자 이중맹검 위약 대조 RCT; ACR20 개선 관찰, ACR50/70 통계적 유의차 없음 |
| [20525198](https://pubmed.ncbi.nlm.nih.gov/20525198/) | 2010 | Ex vivo / 기전 연구 | Arthritis Research & Therapy | RA 환자 활막 세포에서 Apremilast의 TNF-α 자발적 생성 억제 확인; 관절염 마우스 모델에서 효능 입증 |
| [30072998](https://pubmed.ncbi.nlm.nih.gov/30072998/) | 2018 | 동물 모델 (CIA) | Frontiers in Immunology | CIA 마우스에서 Apremilast 투여 후 Th1/Th17 억제, Treg 증가, 골 미란 감소 확인 |
| [26097790](https://pubmed.ncbi.nlm.nih.gov/26097790/) | 2014 | PK 임상 연구 | Clinical Pharmacology in Drug Development | RA/PsA 환자에서 Apremilast + MTX 병용 시 양방향 약동학적 상호작용 없음 확인—병용 안전성 근거 |
| [24797159](https://pubmed.ncbi.nlm.nih.gov/24797159/) | 2014 | 약물 리뷰 | Drugs | Apremilast 최초 글로벌 허가 개요; PsA, 건선, AS, Behçet, RA 등 적응증 개발 파이프라인 포함 |
| [33403021](https://pubmed.ncbi.nlm.nih.gov/33403021/) | 2020 | 체계적 문헌고찰 | Therapeutic Advances in Musculoskeletal Disease | 자가면역/염증 질환 간 표적 치료제 공유 개발 체계적 분석; Apremilast의 다적응증 가능성 언급 |
| [40283434](https://pubmed.ncbi.nlm.nih.gov/40283434/) | 2025 | 서술적 리뷰 | Journal of Clinical Medicine | Rituximab, Apremilast, Upadacitinib의 관절염(RA 포함) 치료 역할 및 기전 비교 최신 검토 |
| [40863428](https://pubmed.ncbi.nlm.nih.gov/40863428/) | 2025 | 횡단면 연구 | Journal of Personalized Medicine | RA, SpA, PsA 환자 처방 데이터베이스 분석; 2차 생물의약품 선택 전략 및 ITABIO 권고 적용 실태 검토 |
| [41234514](https://pubmed.ncbi.nlm.nih.gov/41234514/) | 2025 | 리뷰 | Biologics: Targets & Therapy | 류마티스 질환에서 이중 생물의약품 병용 전략(DBT) 검토; 단독 요법 실패 시 Apremilast 포함 병용 가능성 분석 |
| [32453211](https://pubmed.ncbi.nlm.nih.gov/32453211/) | 2021 | 증례 보고 | Journal of Clinical Rheumatology | 혈청반응 양성 RA 환자에서 Rituximab 관련 수장족저 농포증을 Apremilast로 성공적으로 치료한 증례 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
류마티스 관절염 대상 핵심 Phase 2 RCT(NCT01285310, n=237)가 조기 종료되었으며, 공개된 결과(PMID 25779750)에서 ACR50/ACR70 등 주요 이차 지표의 통계적 유의성을 달성하지 못했습니다. 전임상 및 PK 근거는 기전적 타당성을 시사하나, 현재까지의 임상 데이터는 Apremilast를 기존 허가 RA 치료제(MTX, TNF 억제제, JAK 억제제 등)의 대안으로 지지하기에 불충분합니다.

**진행하려면 필요한 것:**
- 공식 안전성 및 MOA 데이터 확보 (FDA 처방 정보, DrugBank API 조회)
- 한국 MFDS 허가 타당성 검토 (현재 국내 미허가 상태)
- 기존 생물의약품에 불내성이거나 접근이 어려운 RA 하위 집단 대상 소규모 탐색 연구 설계 검토
- TxGNN 1위 예측인 편두통(migraine disorder, TxGNN 98.66%)에 대한 전임상·기전 데이터 별도 탐색 (현재 임상 근거 전무, L5)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

