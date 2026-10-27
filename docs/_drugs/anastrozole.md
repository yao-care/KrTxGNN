---
layout: default
title: Anastrozole
parent: 높은 근거 (L1-L2)
nav_order: 75
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-15
description: "Anastrozole: 예측 신규 적응증 여성 유방암 (Female Breast Carcinoma) (근거 수준 L1). 기존 적응증: 허가 적응증 문서는 링크 형태로만 제공되어 본문 확인 불가 (허가사항 참조). 문헌상 폐경 후 호르몬 수용체 양성 유방암"
monitor_inn: "Anastrozole"
predicted_indications: ["neuroblastoma", "vertebral anomalies and variable endocrine and T-cell dysfunction", "ganglioneuroblastoma (disease)", "retroperitoneal neoplasm", "monocytic leukemia", "rhabdomyosarcoma (disease)", "myeloid leukemia", "collagenopathy", "lymphocytic hypereosinophilic syndrome"]
---

# Anastrozole
{: .fs-9 }

근거 수준: **L1** | 예측 적응증: **10** 건
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

## Anastrozole: 유방암(기존 적응증)에서 여성 유방암 확인(예측 신규 적응증)으로
{: .text-alpha }

## 한 문장 요약

Anastrozole은 비스테로이드성 아로마타제 억제제로, 한국에서 호르몬 수용체 양성 유방암 치료제로 허가되어 시판되고 있습니다.
TxGNN 모델은 **여성 유방암(Female Breast Carcinoma)**에 효과가 있을 것으로 예측하며, 현재 **30건의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다.
다만 이 예측은 이미 확립된 기존 적응증을 재확인한 것이므로, 엄밀한 의미의 새로운 재창출 후보는 아닙니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 문서는 링크 형태로만 제공되어 본문 확인 불가 (허가사항 참조). 문헌상 폐경 후 호르몬 수용체 양성 유방암 |
| 예측 신규 적응증 | 여성 유방암 (Female Breast Carcinoma) |
| TxGNN 예측 점수 | 99.68% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 4건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 이번 보고서용 데이터에 포함되어 있지 않습니다. 다만 문헌에 따르면 Anastrozole은 3세대 비스테로이드성 아로마타제 억제제로, 폐경 후 여성에서 말초 조직의 에스트로겐 합성을 낮춥니다.

호르몬 수용체 양성 유방암은 에스트로겐에 의존하여 성장하므로, 에스트로겐 합성 차단은 기전상 직접적인 치료 표적입니다. 이 예측 적응증은 Anastrozole의 기존 시판 적응증과 사실상 같은 영역이어서, 예측의 타당성은 높습니다.

참고로 같은 예측 목록의 신경모세포종, 횡문근육종, 골수성 백혈병 등 다른 질환은 임상시험이나 의미 있는 문헌 근거가 없고 에스트로겐 의존 기전도 확인되지 않아, 네트워크 기반 예측의 한계로 보입니다.

## 임상시험 근거

관련성이 높은 시험 위주로 10건을 나열했습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00784680](https://clinicaltrials.gov/study/NCT00784680) | Phase 3 | 완료 | 308 | 폐경 후 보조요법에서 Anastrozole, Tamoxifen, 병용군의 삶의 질 비교 |
| [NCT00327769](https://clinicaltrials.gov/study/NCT00327769) | Phase 3 | 완료 | 234 | 에스트로겐 수용체 양성 진행성 유방암 2차 치료에서 Fulvestrant와 Anastrozole 비교 |
| [NCT00143390](https://clinicaltrials.gov/study/NCT00143390) | Phase 3 | 완료 | 298 | 진행성/재발성 유방암 초기 호르몬 치료에서 Exemestane과 Anastrozole 비교 |
| [NCT00301457](https://clinicaltrials.gov/study/NCT00301457) | Phase 3 | 완료 | 1914 | Tamoxifen 2~3년 후 Anastrozole 6년 vs 3년 보조요법 |
| [NCT00300508](https://clinicaltrials.gov/study/NCT00300508) | Phase 3 | 완료 | 856 | 5년 보조 호르몬 치료 후 Anastrozole 3년 추가 vs 무치료 |
| [NCT03425838](https://clinicaltrials.gov/study/NCT03425838) | Phase 3 | 진행 중(모집 종료) | 1050 | 호르몬 수용체 양성 진행성 유방암에서 아로마타제 억제제 + CDK4/6 억제제 치료 순서 비교(SONIA) |
| [NCT02246621](https://clinicaltrials.gov/study/NCT02246621) | Phase 3 | 진행 중(모집 종료) | 493 | 비스테로이드성 아로마타제 억제제(Anastrozole 또는 Letrozole) + Abemaciclib vs 위약 |
| [NCT00256217](https://clinicaltrials.gov/study/NCT00256217) | Phase 2 | 완료 | 42 | 폐경 후 DCIS 및 초기 침윤성 유방암에서 Anastrozole 화학예방 |
| [NCT04272801](https://clinicaltrials.gov/study/NCT04272801) | Phase 2 | 진행 중(모집 종료) | 84 | 고령 여성 초기 유방암에서 수술 전 호르몬 치료 기간 설정 후 방사선 치료 결정 |
| [NCT00728949](https://clinicaltrials.gov/study/NCT00728949) | Phase 2 | 완료 | 93 | 항에스트로겐 치료 후 진행된 유방암에서 IMC-A12 단독 또는 항에스트로겐 병용 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [15639680](https://pubmed.ncbi.nlm.nih.gov/15639680/) | 2005 | RCT | Lancet | ATAC 시험: 폐경 후 유방암 5년 보조요법에서 Anastrozole이 Tamoxifen보다 무병생존기간 연장 |
| [31839281](https://pubmed.ncbi.nlm.nih.gov/31839281/) | 2020 | RCT | Lancet | IBIS-II 장기 결과: 고위험 여성에서 Anastrozole의 유방암 예방 효과 |
| [27908454](https://pubmed.ncbi.nlm.nih.gov/27908454/) | 2016 | RCT | Lancet | FALCON: 진행성 유방암에서 Fulvestrant 500 mg과 Anastrozole 1 mg 비교 |
| [42384406](https://pubmed.ncbi.nlm.nih.gov/42384406/) | 2026 | RCT | JAMA Surgery | NSABP B-35: DCIS에서 Anastrozole 또는 Tamoxifen 투여 시 절제연 폭과 국소 재발 분석 |
| [41632158](https://pubmed.ncbi.nlm.nih.gov/41632158/) | 2025 | Cohort | JAMA Network Open | 폐경 후 유방암에서 Anastrozole, Letrozole, Exemestane의 실제 임상 성과 비교 |
| [31615937](https://pubmed.ncbi.nlm.nih.gov/31615937/) | 2020 | 임상 연구 | Clin Cancer Res | neoMONARCH: 수술 전 Abemaciclib + Anastrozole의 세포주기 억제 및 면역 반응 |
| [20923259](https://pubmed.ncbi.nlm.nih.gov/20923259/) | 2010 | Review | Expert Opin Drug Saf | 보조요법에서 Tamoxifen 대비 Anastrozole의 우수한 효능 정리 |
| [28614542](https://pubmed.ncbi.nlm.nih.gov/28614542/) | 2017 | Review | Rev Assoc Med Bras | 유방암 화학예방 및 치료에서 Anastrozole 사용 문헌고찰 |
| [16439860](https://pubmed.ncbi.nlm.nih.gov/16439860/) | 2006 | Review | Oncology | 진행성 질환부터 초기 질환, 예방까지 Anastrozole의 역할 |
| [12421108](https://pubmed.ncbi.nlm.nih.gov/12421108/) | 2002 | Review | Drugs | 초기 유방암 보조요법에서 Anastrozole 1 mg이 Tamoxifen보다 유의하게 효과적 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200009025 | 아리미덱스정(아나스트로졸) | 백색의 원형 필름코팅정 | 허가사항 참조 |
| 200808866 | 에이덱스정(아나스트로졸) | 흰색의 원형 필름코팅정 | 허가사항 참조 |
| 200806188 | 테바아나스트로졸정1밀리그램 | 흰색 내지 밝은 회색의 원형 필름코팅정 | 허가사항 참조 |
| 200805384 | 아나스토정(아나스트로졸) | 흰색의 원형 필름코팅정 | 허가사항 참조 |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 호르몬 요법(아로마타제 억제제). 기존 세포독성 화학요법제는 아님 |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요. 문헌상 간독성 증례 보고가 있어 간기능 모니터링을 고려할 수 있습니다 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **금기(지식그래프 기반, 허가사항 아님)**: 심근허혈, 관상동맥질환 (실제 금기 여부는 허가사항 확인 필요)
- **약물 상호작용**: 총 100건이 조회되었으며 모두 위험도 등급이 미분류입니다. 주요 항목은 Bupropion, Pantoprazole, Glimepiride, Morphine, Metformin, Omeprazole, Rosiglitazone, Simvastatin, Prednisone, Acetylsalicylic acid 등입니다.
- **문헌상 안전성 신호**: Anastrozole에 의한 간독성 증례 보고(PMID 17033446)가 있습니다.

허가사항상의 경고 및 금기는 이번 보고서용 데이터에 포함되어 있지 않으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
다수의 완료된 Phase 3 RCT(ATAC 등)가 유방암에서 Anastrozole의 효능을 뒷받침하며 한국에서도 4건이 허가되어 시판 중입니다. 다만 이 예측은 신규 재창출이 아니라 기존 적응증의 재확인이고, 허가 적응증 본문과 안전성 정보가 확보되지 않았습니다.

**진행하려면 필요한 것:**
- 식약처 허가사항 PDF에서 적응증, 경고, 금기 정보 확인 및 정리
- DrugBank에서 상세 작용 기전(MOA) 데이터 보완
- 심근허혈·관상동맥질환 환자에 대한 안전성 검토
- 신경모세포종 등 근거가 없는 다른 예측 적응증은 별도의 근거가 확보되기 전까지 보류(Hold)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

