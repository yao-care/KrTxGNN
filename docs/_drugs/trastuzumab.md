---
layout: default
title: Trastuzumab
parent: 모델 예측만 (L5)
nav_order: 754
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-28
monitor_inn: "TRASTUZUMAB"
predicted_indications: ["malignant cutaneous granular cell skin tumor", "ectomesenchymoma", "human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "kidney pelvis sarcomatoid transitional cell carcinoma", "prostatic urethra urothelial carcinoma"]
description: "Trastuzumab: 예측 신규 적응증 Malignant cutaneous granular cell skin tumor (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202302082/EE"
---

# Trastuzumab
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **6** 건
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

## Trastuzumab: Malignant cutaneous granular cell skin tumor
{: .text-alpha }

## 한 문장 요약

Trastuzumab은 HER2를 표적으로 하는 단클론항체로, 원래 HER2 양성 유방암 치료에 사용되어 왔습니다.
다만 이 적응증은 이미 승인된 HER2 양성 유방암 중 수용체 특성으로 구분한 하위 집단이어서, 엄밀한 의미의 재창출은 아닙니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202302082/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202302083/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201707851/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201400158/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201400159/EE;  |
| 예측 신규 적응증 | Malignant cutaneous granular cell skin tumor |
| TxGNN 예측 점수 | 0.9948 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 8건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Trastuzumab은 HER2 수용체에 결합하는 단클론항체이며, HER2 양성 유방암에서 효능이 입증되어 있습니다.

HER2 양성 종양의 상당수는 프로게스테론 수용체(PR)도 함께 양성(HR+/HER2+)입니다. 따라서 이 예측은 새로운 질환이라기보다 이미 승인된 적응증의 하위 집단에 해당합니다. 치료 효과는 PR 상태가 아니라 **HER2 상태**에 좌우됩니다.

임상시험에는 내분비치료(fulvestrant, tamoxifen, letrozole)나 CDK4/6 억제제(palbociclib, abemaciclib)를 병용하는 HR+/HER2+ 질환 연구가 포함되어 있어, 이 하위 집단에서의 병용 전략이 활발히 연구되고 있음을 보여 줍니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | 완료 | 3270 | 화학요법 단독 vs 화학요법+trastuzumab 보조요법 무작위 비교. HR+/HER2+를 포함하는 직접적 3상 근거 |
| [NCT01750073](https://clinicaltrials.gov/study/NCT01750073) | Phase 2 | 완료 | 92 | paclitaxel+cyclophosphamide 선행화학요법에서 trastuzumab 추가 여부 비교 |
| [NCT02260531](https://clinicaltrials.gov/study/NCT02260531) | Phase 2 | 완료 | 36 | 뇌전이 유방암에서 cabozantinib 단독 또는 trastuzumab 병용 |
| [NCT00134680](https://clinicaltrials.gov/study/NCT00134680) | Phase 2 | 완료 | 33 | ER/PR 양성, ErbB2 양성 전이성 유방암에서 letrozole+trastuzumab |
| [NCT04334330](https://clinicaltrials.gov/study/NCT04334330) | Phase 2 | 불명 | 34 | ER/PR 양성, HER2 양성 뇌전이에서 palbociclib+trastuzumab+pyrotinib+fulvestrant |
| [NCT04886531](https://clinicaltrials.gov/study/NCT04886531) | Phase 2 | 모집 중 | 30 | ER 양성, HER2 양성 암에서 수술 전 neratinib+내분비치료+trastuzumab |
| [NCT02152943](https://clinicaltrials.gov/study/NCT02152943) | Phase 1 | 완료 | 37 | HR+/HER2+ 진행성 암에서 everolimus+letrozole+trastuzumab 병용 |
| [NCT00194779](https://clinicaltrials.gov/study/NCT00194779) | Phase 2 | 완료 | 50 | HER2 양성 유방암 선행 화학요법 계획 (간접적 관련) |
| [NCT02774681](https://clinicaltrials.gov/study/NCT02774681) | Phase 2 | 종료(조기 중단) | 12 | HER2 양성 뇌전이 유방암에서 palbociclib 단일군 시험, 데이터 제한적 |
| [NCT00053339](https://clinicaltrials.gov/study/NCT00053339) | Phase 3 | 철회 | 0 | trastuzumab ± tamoxifen 비교 설계였으나 환자 등록 없음 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [32353342](https://pubmed.ncbi.nlm.nih.gov/32353342/) | 2020 | RCT | Lancet Oncol | HR+/HER2+ 진행성 유방암에서 abemaciclib+trastuzumab(±fulvestrant)과 trastuzumab+화학요법 비교 (monarcHER) |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | RCT | Ann Oncol | HER2 양성 조기 유방암에서 trastuzumab+pertuzumab 이중 차단의 de-escalation 전략 (WSG-ADAPT) |
| [26874901](https://pubmed.ncbi.nlm.nih.gov/26874901/) | 2016 | RCT | Lancet Oncol | trastuzumab 기반 보조요법 후 neratinib 12개월 투여 (ExteNET) |
| [15894097](https://pubmed.ncbi.nlm.nih.gov/15894097/) | 2005 | 메타분석 | Lancet | 조기 유방암에서 화학요법과 호르몬 치료의 재발 및 15년 생존 효과 |
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | 코호트 | Lancet Oncol | 수술 전 pertuzumab+trastuzumab의 5년 무진행생존 및 안전성 (NeoSphere) |
| [31410192](https://pubmed.ncbi.nlm.nih.gov/31410192/) | 2019 | 다기관 코호트 분석 | Theranostics | ER+/PR+/HER2+ 삼중 양성 유방암의 분자적 특성과 trastuzumab 반응성 |
| [21151204](https://pubmed.ncbi.nlm.nih.gov/21151204/) | 2011 | Review | Nat Rev Clin Oncol | HER2·호르몬 수용체 양성 유방암에서 아로마타제 억제제와 항HER2 병용 전략 |
| [40339592](https://pubmed.ncbi.nlm.nih.gov/40339592/) | 2025 | 2a상 | Lancet Oncol | HR+/HER2+ 전이성 유방암에서 zanidatamab+palbociclib+fulvestrant |
| [39631485](https://pubmed.ncbi.nlm.nih.gov/39631485/) | 2024 | Review | Pharmacol Res | HER2, HR, PR 상태에 따른 유방암 표적·세포독성 치료제 정리 |
| [26253814](https://pubmed.ncbi.nlm.nih.gov/26253814/) | 2015 | Review | Breast | 유방암 내재 분자 아형의 임상적 의미 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200511046 | 허셉틴주150밀리그램 | 동결건조분말 주사제 (바이알) | 허가 적응증 본문 확인 불가 (PDF 링크 형태로만 제공) |
| 201402190 | 허셉틴피하주사600밀리그램 | 액체 주사제 (피하주사, 바이알) | 허가 적응증 본문 확인 불가 (PDF 링크 형태로만 제공) |
| 201400158 | 허쥬마주150mg | 동결건조분말 주사제 (바이알) | 허가 적응증 본문 확인 불가 (PDF 링크 형태로만 제공) |
| 201707851 | 삼페넷주150밀리그램 | 동결건조분말 주사제 (바이알) | 허가 적응증 본문 확인 불가 (PDF 링크 형태로만 제공) |
| 202302082 | 투젭타주150밀리그램 | 동결건조물 주사제 (바이알) | 허가 적응증 본문 확인 불가 (PDF 링크 형태로만 제공) |

허가증은 총 8건(전부 단일제, 유효)이며, 위 표는 그중 주요 5건입니다. 나머지는 허쥬마주440mg, 삼페넷주440밀리그램, 투젭타주440밀리그램입니다.

## 세포독성

Trastuzumab은 세포독성 화학요법제가 아닌 HER2 표적 단클론항체이지만, 항종양 목적으로 사용됩니다.

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (HER2 표적 단클론항체) |
| 골수억제 위험 | 낮음 (단독 사용 시). 병용 화학요법에 따라 달라질 수 있음 |
| 구토 유발성 등급 | 낮음 |
| 모니터링 항목 | 심기능(좌심실 박출률), 병용 화학요법에 따른 CBC. 심독성 관련 문헌이 있음 (PMID 17687157) |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **약물 상호작용**: 총 94건이 확인되었으며, 이 중 주요(Major) 등급은 다음과 같습니다.
  - Deferiprone
  - Samarium (153Sm) lexidronam
  - Adalimumab
  - Baricitinib
- 중등도(Moderate) 등급에는 warfarin, paclitaxel, azathioprine, alemtuzumab 등이 있습니다.

주요 경고와 금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
완료된 3상 무작위 시험(NCT01275677)과 다수의 RCT 문헌이 HER2 양성 유방암에서 trastuzumab의 효능을 뒷받침하며, HR+/HER2+ 하위 집단 대상 병용요법 연구도 진행되고 있습니다. 다만 이 적응증은 새로운 재창출이 아니라 승인된 적응증의 하위 집단이므로, 효과는 PR 상태가 아닌 HER2 상태로 판단해야 합니다.

**진행하려면 필요한 것:**
- 한국 허가사항(경고, 금기, 적응증 본문) 확인. 현재 허가 정보가 PDF 링크로만 제공됨
- 작용 기전(MOA) 상세 데이터 보완
- HER2 양성 확진을 전제로 한 사용 제한 (HER2 음성 luminal A, 삼중음성 유방암은 대상 아님)
- 심기능 모니터링 계획 및 주요 상호작용 약물 병용 시 관리 방안

### 참고: 기타 예측 적응증

| 예측 적응증 | TxGNN 점수 | 근거 수준 | 권장 |
|---|---|---|---|
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

