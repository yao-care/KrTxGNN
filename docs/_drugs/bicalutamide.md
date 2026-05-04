---
layout: default
title: Bicalutamide
parent: 僅模型預測 (L5)
nav_order: 139
evidence_level: L5
indication_count: 10
---

# Bicalutamide
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

# Bicalutamide: 전립선암에서 여성 유방암으로

## 한 문장 요약

Bicalutamide는 비스테로이드성 안드로겐 수용체(AR) 길항제로, 전 세계적으로 전립선암 치료에 사용되어 온 항암제이나 한국에서는 현재 미허가 약물입니다.
TxGNN 모델은 총 10개의 신규 적응증을 예측하였으며 (TxGNN 1위: 다모증 99.69%), 그 중 **여성 유방암(Female Breast Carcinoma)**이 **1건의 Phase 2 임상시험**과 **20편의 문헌**으로 가장 높은 근거 수준(L2)을 보이며 최우선 재창출 후보로 부상합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 전립선암 (국제 표준 적응증; 한국 미허가) |
| 예측 신규 적응증 | 여성 유방암 (Female Breast Carcinoma) |
| TxGNN 예측 점수 | 99.11% |
| 근거 수준 | L2 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Bicalutamide는 비스테로이드성 안드로겐 수용체(AR) 길항제입니다. 안드로겐(테스토스테론·DHT)이 AR에 결합하는 것을 경쟁적으로 차단하여 AR의 핵 이동과 전사 활성화를 억제합니다. 전립선암에서 AR 신호 차단이 종양 성장을 억제하는 것과 동일한 기전이 유방암에도 직접 적용됩니다.

유방암에서 AR은 ER+/PR+ 유방암의 약 70–90%, 삼중음성 유방암(TNBC)의 luminal androgen receptor(LAR) 아형에서 약 20–50%에서 발현됩니다. 특히 기존 내분비 치료(AI·타목시펜)나 HER2 표적 치료를 적용할 수 없는 TNBC-LAR 아형 환자에게 AR은 치료 가능한 유일한 표적이 되며, bicalutamide의 AR 길항 기전은 이 아형에 직접 적용될 수 있는 강력한 생물학적 근거를 제공합니다.

전임상 연구에서 bicalutamide는 TNBC 세포주(MDA-MB-231)의 증식·침윤을 억제하고, AR-매개 β-catenin 전사 복합체를 차단하며, 독소루비신·도세탁셀과 상승 효과를 보였습니다. 2026년 최신 연구에서는 ERK 억제제(GDC-0994)와의 병합이 FOXC2를 통한 페롭토시스(ferroptosis) 유도라는 새로운 항종양 기전을 제시하고 있으며, 면역관문억제제(nivolumab + ipilimumab)와의 병합 전략도 현재 Phase 2 임상시험으로 검증 중입니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03650894](https://clinicaltrials.gov/study/NCT03650894) | Phase 2 | 등록 완료·추적 중 (완료 예정 2026-12) | 30 | 전이성 HER2 음성 유방암에서 Nivolumab + Bicalutamide + Ipilimumab 병합 요법의 안전성·효능 평가. 항안드로겐 AR 차단과 면역관문억제를 결합하여 화학요법을 배제하거나 지연시키는 전략 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [40853613](https://pubmed.ncbi.nlm.nih.gov/40853613/) | 2025 | Review | Current Medical Science | TNBC 항안드로겐 요법 최신 현황: bicalutamide·enzalutamide·enobosarm이 AR+ TNBC LAR 아형의 주요 치료 전략으로 검토; 면역·화학·표적요법과의 병합 연구 동향 정리 |
| [31434793](https://pubmed.ncbi.nlm.nih.gov/31434793/) | 2020 | Phase II | The Oncologist | ER+/AR+ 진행성 유방암에서 Bicalutamide + AI 병합 Phase II 연구: 6개월 임상이익률 16.7%, 반응률 0%로 조기 종료. AI 내성 ER+ 유방암에서는 효과 제한적; 단독 TNBC-LAR 아형에 전략 집중 필요성 시사 |
| [21633166](https://pubmed.ncbi.nlm.nih.gov/21633166/) | 2011 | Translational | J Clin Investigation | TNBC 6개 분자 아형(BL1/BL2/IM/M/MSL/LAR) 정의. LAR 아형 확인 및 bicalutamide가 유효한 AR 표적 치료 후보임을 최초로 제시한 기반 연구 |
| [35027319](https://pubmed.ncbi.nlm.nih.gov/35027319/) | 2022 | Review | Clinical Breast Cancer | 아포크린 유방암종: ER 음성·AR 양성 특성으로 정의; PIK3CA/PTEN/AKT 돌연변이 동반 빈도 높음. AR 표적 치료의 주요 후보 아형 |
| [39063165](https://pubmed.ncbi.nlm.nih.gov/39063165/) | 2024 | In vitro/In vivo | Int J Mol Sci | 인간·개 염증성 유방암(IBC/IMC) 세포주에서 bicalutamide + 독소루비신/도세탁셀 병합이 증식·이동·침윤 억제에 상승 효과 확인 |
| [40974527](https://pubmed.ncbi.nlm.nih.gov/40974527/) | 2026 | Preclinical | Science China Life Sci | Bicalutamide(AR 억제) + GDC-0994(ERK 억제) 병합이 FOXC2 통한 페롭토시스 유도로 TNBC에 강력한 항종양 효과; AR 단독 억제의 한계를 병합 전략으로 극복 |
| [32332626](https://pubmed.ncbi.nlm.nih.gov/32332626/) | 2020 | In vitro | Medicine | MDA-MB-231 TNBC 세포에서 bicalutamide의 증식·침윤 억제 효과 확인; AR-PI3K/AKT/mTOR 신호 차단을 통한 항종양 기전 제시 |
| [31917699](https://pubmed.ncbi.nlm.nih.gov/31917699/) | 2020 | In vitro | Anti-Cancer Drugs | AR+ TNBC에서 bicalutamide + 커큐민 병합이 단독 치료 대비 강력한 세포사멸·항증식 효과; 자연 유래 물질과의 병합 상승 기전 분석 |
| [24888812](https://pubmed.ncbi.nlm.nih.gov/24888812/) | 2016 | Case Report | J Clin Oncol | AR 양성 전이성 유방암 환자에서 bicalutamide 단독 투여로 완전 반응(CR) 달성. AR 표적 치료의 임상 실현 가능성을 보여 준 최초 주요 증례 |
| [29069648](https://pubmed.ncbi.nlm.nih.gov/29069648/) | 2017 | In vitro/Translational | Cell Physiol Biochem | ER 음성 유방암에서 bicalutamide가 AR-β-catenin 전사 복합체를 억제하는 기전 규명; AR 양성 ER 음성 유방암에서의 표적 치료 분자적 근거 강화 |

---

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (비스테로이드성 안드로겐 수용체 길항제; 전통적 세포독성 화학요법제 아님) |
| 골수억제 위험 | 저 (골수억제 부작용 보고 없음; 세포독성 화학요법과 병합 시 화학요법 성분의 골수억제 모니터링 필요) |
| 구토 유발성 등급 | 저 (경구 투여 항안드로겐제; 구역·구토 위험 최소) |
| 모니터링 항목 | 간기능 검사(ALT/AST; 드문 간독성 감시), QTc 연장 여부, 혈당 |
| 취급 방호 | 항종양제로서 기본 취급 주의 권장; 전통 세포독성 화학요법 대비 노출 위험 낮음 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
AR 양성 유방암(특히 TNBC-LAR 아형)에 대한 bicalutamide의 분자 기전적 근거가 견고하며, Phase 2 임상시험(NCT03650894)이 진행 중이고 전임상·번역 연구를 포함한 20편의 문헌이 이를 지지합니다. 단, 한국 미허가 약물로 핵심 임상시험 결과가 아직 미공개이며 안전성 데이터 수집이 완료되지 않아 세부 검증이 선행되어야 합니다.

**진행하려면 필요한 것:**
- NCT03650894 Phase 2 임상시험 결과 발표(예정: 2026년 말) 확인
- MFDS 허가사항 및 안전성 정보(주요 경고·금기·DDI) 수집
- AR 양성 TNBC 환자 선별을 위한 동반 진단(companion diagnostics) 전략 수립
- 한국 내 도입 경로(임상시험 신청 또는 허가외 사용 프로토콜) 규제 전략 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

