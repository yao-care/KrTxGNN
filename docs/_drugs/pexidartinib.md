---
layout: default
title: Pexidartinib
parent: 모델 예측만 (L5)
nav_order: 596
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Pexidartinib: 예측 신규 적응증 HER2 양성 유방암 (HER2 positive breast carcinoma) (근거 수준 L5). 기존 적응증: 건활막 거대세포종(TGCT). 한국 허가증에는 적응증 본문 대신 허가 문서 링크만 등록되어 있어…"
monitor_inn: "Pexidartinib"
predicted_indications: ["HER2 positive breast carcinoma", "normal breast-like subtype of breast carcinoma", "progesterone-receptor positive breast cancer", "progesterone-receptor negative breast cancer", "breast tumor luminal A or B", "synovium cancer", "synovium disease", "dermatofibrosarcoma protuberans", "multifocal choroiditis", "malignant giant cell tumor"]
---

# Pexidartinib
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

## Pexidartinib: 건활막 거대세포종에서 HER2 양성 유방암으로
{: .text-alpha }

## 한 문장 요약

Pexidartinib은 CSF1R 억제제로, 원래 수술이 어려운 증상성 건활막 거대세포종(TGCT) 치료에 사용되었습니다.
TxGNN 모델은 **HER2 양성 유방암(HER2 positive breast carcinoma)**에 효과가 있을 수 있다고 예측하지만, 현재 **임상시험은 0건**이고 간접적인 전임상 수준의 **문헌 1편**만 있어 근거가 매우 제한적입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 건활막 거대세포종(TGCT). 한국 허가증에는 적응증 본문 대신 허가 문서 링크만 등록되어 있어, 문헌에 기술된 한국 승인 적응증을 기준으로 함 |
| 예측 신규 적응증 | HER2 양성 유방암 (HER2 positive breast carcinoma) |
| TxGNN 예측 점수 | 0.9998 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 충분하지 않습니다. 알려진 정보에 따르면 Pexidartinib은 CSF1R(집락자극인자-1 수용체)을 억제하는 경구 티로신 키나제 억제제이며, KIT와 FLT3-ITD에도 활성이 있습니다. CSF1R은 종양 관련 대식세포(TAM)의 생존과 면역억제 환경 형성에 관여합니다.

기존 적응증인 TGCT는 CSF1 과발현이 원인인 종양입니다. 유방암에서도 TAM을 표적으로 삼으면 항종양 면역을 높일 수 있다는 이론적 근거가 있습니다. 다만 연결된 유일한 논문(PMID 41986650)은 CDK4/6 억제제로 유발되는 면역억제를 CSF1R 억제제가 완화한다는 전임상 연구입니다. 이 연구는 HR+/HER2- 유방암을 다루므로 HER2 양성 질환에 특화된 근거가 아니며 Pexidartinib 자체의 임상 자료도 아닙니다. 따라서 이 예측은 타당성은 있으나 간접적인 가설 수준입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [41986650](https://pubmed.ncbi.nlm.nih.gov/41986650/) | 2026 | 전임상/기전 연구 | Oncogene | CSF1R 억제제가 CDK4/6 억제제 유발 면역억제를 완화해 HR+/HER2- 유방암에서 항종양 면역을 높임 (HER2 양성 질환 대상 아님) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202108140 | 투랄리오캡슐200밀리그램 (펙시다티닙염산염, 한국다이이찌산쿄) | 캡슐 | 허가 문서 링크로 제공됨 (https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202108140/EE) |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (CSF1R/KIT/FLT3 티로신 키나제 억제제) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 간기능 (문헌상 장기 간독성 안전성 분석이 보고됨, PMID 33289960). 그 외 항목은 허가사항 참조 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **간독성**: 수집된 문헌과 근거 평가에서 간독성이 주요 위험으로 지적되며, 간기능 모니터링과 REMS 유형의 제한이 필요하다고 평가됩니다.
- **약물 상호작용**: 상호작용 조회 결과 총 100건이 확인되었고, 아래는 그중 표시된 20건입니다.
  - **Major**: Acarbose, Rabeprazole, Doxycycline, Pioglitazone, Bupropion, Aprepitant, Omeprazole, Tetracycline, Chenodeoxycholic acid, Clarithromycin, Dexlansoprazole, Minocycline
  - **Moderate**: Famotidine, Ranitidine, Metformin, Dexamethasone, Budesonide, Cimetidine, Magnesium oxide, Saxagliptin
  - 위산억제제(PPI, H2 차단제)와의 병용은 특히 주의가 필요합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
HER2 양성 유방암에 대한 예측은 모델 점수에만 의존하며, 임상시험이 없고 간접적인 전임상 논문 1편만 있어 L5 수준입니다. 간독성 위험이 큰 약물이므로 이 근거만으로 진행하기는 어렵습니다.

참고로 예측 목록의 TGCT 관련 항목(synovium cancer, synovium disease, malignant giant cell tumor)은 이미 승인된 기존 적응증에 해당하므로 신규 재창출 후보가 아닙니다. 이 항목들에서 보이는 L1 근거(ENLIVEN 3상)는 HER2 양성 유방암에 대한 근거가 아닙니다.

**진행하려면 필요한 것:**
- HER2 양성 유방암 모델에서 Pexidartinib 단독 또는 병용(항HER2 치료 등)의 전임상 효능 자료
- 유방암 환자 대상 Pexidartinib 임상 자료 (현재 없음)
- 허가사항(MFDS)의 경고, 금기, 간독성 관리 기준 확인
- 작용 기전 자료 보완 및 유방암 TAM 표적 가설의 검증
- 간독성 위험 대비 유방암에서의 기대 이익 평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

