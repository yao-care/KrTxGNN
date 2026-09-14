---
layout: default
title: Topotecan
parent: 僅模型預測 (L5)
nav_order: 688
evidence_level: L5
indication_count: 10
---

# Topotecan
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

# Topotecan: 재발성 난소암에서 유방암으로

## 한 문장 요약

Topotecan은 Topoisomerase I 억제제 계열의 세포독성 항암제로, 근거팩 내 서술 기준 재발성 난소암 등 실체 종양에서 사용되어 온 약물입니다. TxGNN 모델은 **유방암(Female Breast Carcinoma)**에도 효과가 있을 수 있다고 예측하며, 현재 **5건의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다. 단, 한국 내 공식 허가 적응증·안전성 데이터가 존재하지 않아(DG001 Blocking) 실제 진행 전 보완이 필요합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 허가 데이터 없음(미시판). 근거팩 서술 기준 재발성 난소암 등이 국제적으로 승인된 적응증으로 언급됨 |
| 예측 신규 적응증 | 유방암 (Female Breast Carcinoma) |
| TxGNN 예측 점수 | 99.92% |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

공식 작용 기전(MOA) 데이터는 현재 확보되지 않았습니다(DG002, High severity). 다만 근거팩 내 기전 서술에 따르면, Topotecan은 Topoisomerase I 억제제로서 DNA 단일가닥 절단을 유발하고 재결합을 차단하여 증식 속도가 빠른 종양세포에 세포독성을 나타냅니다. 이 기전은 특정 암종에 국한되지 않고 여러 고형암에 공통적으로 작용합니다.

유방암, 특히 삼중음성유방암(TNBC)은 증식 속도가 높은 아형으로, Topoisomerase I 억제제에 대한 감수성이 상대적으로 높을 수 있습니다. 실제로 문헌에서는 TNBC의 치료표적으로 TFDP1-topotecan 관계를 규명한 최신 연구(2025)와 BCRP 매개 내성을 역전시켜 topotecan 효능을 증강하는 다수의 기전 연구가 확인되며, 1990~2000년대에는 전이성 유방암 대상 Phase II 임상시험도 다수 수행된 바 있습니다. 이는 TxGNN 예측의 기전적 타당성을 뒷받침합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | 중단 | N/A | 고용량 topotecan+ifosfamide/etoposide(TIME) 후 자가줄기세포구조, 전이성 유방암 직접 평가(중단되었으나 직접 증거) |
| [NCT02282020](https://clinicaltrials.gov/study/NCT02282020) | Phase 3 | 완료 | 266 | gBRCA 변이 재발성 난소암에서 olaparib 단독요법 vs 의사선택 단일 화학요법(topotecan 등) 비교 |
| [NCT04739800](https://clinicaltrials.gov/study/NCT04739800) | Phase 2 | 모집종료(진행중) | 120 | 백금저항성 재발 난소암/복막암에서 durvalumab+olaparib+cediranib 병용 대 표준화학요법(topotecan 포함) 비교 |
| [NCT02419495](https://clinicaltrials.gov/study/NCT02419495) | Phase 1 | 중단 | 221 | selinexor를 표준 화학/면역요법과 병용 시 안전성 평가, 진행성 악성종양 대상 |
| [NCT04279509](https://clinicaltrials.gov/study/NCT04279509) | N/A | 불명 | 35 | 환자유래 오가노이드 기반 고처리량 약물 스크리닝으로 불응성 고형암 화학요법제 선택 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [10362325](https://pubmed.ncbi.nlm.nih.gov/10362325/) | 1999 | RCT | Am J Clin Oncol | CALGB Phase II 임상시험: 전이성 유방암 환자에서 topotecan 단독요법 평가(53명 등록) |
| [11455218](https://pubmed.ncbi.nlm.nih.gov/11455218/) | 2001 | Cohort | Onkologie | 뇌전이 동반 유방암 환자 대상 topotecan 1차 화학요법 파일럿 연구 |
| [9413954](https://pubmed.ncbi.nlm.nih.gov/9413954/) | 1997 | Cohort | Br J Cancer | 진행성 유방암·비소세포폐암에서 지속주입 topotecan, 효능 증가 근거 없음 |
| [9626200](https://pubmed.ncbi.nlm.nih.gov/9626200/) | 1998 | 임상시험 | J Clin Oncol | Stage IV 유방암에서 paclitaxel+topotecan+G-CSF 병용 Phase II |
| [40300683](https://pubmed.ncbi.nlm.nih.gov/40300683/) | 2025 | 기전연구 | Int J Biol Macromol | 삼중음성유방암(TNBC)에서 TFDP1이 topotecan 치료표적으로 작용함을 규명 |
| [26623560](https://pubmed.ncbi.nlm.nih.gov/26623560/) | 2015 | 전임상 | Oncotarget | 말기 전이성 TNBC 전임상모델에서 metronomic topotecan+pazopanib 병용요법 효능 |
| [31408695](https://pubmed.ncbi.nlm.nih.gov/31408695/) | 2019 | 기전연구 | Pharmacol Res | Daidzein이 BCRP 매개 topotecan 내성을 역전시켜 유방암 항암효과 증강 |
| [15836850](https://pubmed.ncbi.nlm.nih.gov/15836850/) | 2005 | 기전연구 | J Surg Res | Quercetin이 MCF-7/MDA-MB-231 유방암세포에서 topotecan 세포독성에 미치는 영향 |
| [10930538](https://pubmed.ncbi.nlm.nih.gov/10930538/) | 2000 | 기전연구 | Biochem Pharmacol | Topotecan 내성 유방암세포주에서 BCRP/MXR/ABCP 발현 확인 |
| [12089223](https://pubmed.ncbi.nlm.nih.gov/12089223/) | 2002 | 약동학연구 | J Clin Oncol | BCRP/P-gp 억제제 GF120918 병용 시 경구 topotecan 생체이용률 증가 |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (Topoisomerase I 억제제, camptothecin 유도체) |
| 골수억제 위험 | 고위험 — 문헌(PMID 8617580, 난소·생식세포종 대상)에서 골수억제가 주요 독성으로 보고됨(호중구 최저치 약 1.55×10³/mm³, 혈소판 최저치 약 20,500/mm³) |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | CBC(백혈구·호중구·혈소판 분획 포함), 감염 징후 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
유방암 적응증에 대해 Phase II 임상시험(TIME 요법 등 직접 개입 연구 포함)과 다수의 기전·내성 관련 문헌이 축적되어 있어 L2 수준의 근거를 확보하고 있습니다. 그러나 한국 내 허가 정보(DG001, Blocking)와 공식 MOA 데이터(DG002, High)가 없어 안전성 초기평가(S1)를 통과하지 못한 상태이므로, 가드레일 하에서만 진행이 가능합니다.

**진행하려면 필요한 것:**
- TFDA(식약처) 공식 허가사항·경고·금기 정보 확보 (DG001 해소 — Blocking)
- DrugBank 등에서 공식 작용기전(MOA) 데이터 확보 (DG002 해소)
- 한국 내 미시판 상태이므로 도입/수입 경로 및 규제 전략 검토
- 구토 유발성 등급 등 세부 독성 프로파일에 대한 허가사항 기반 확인
- 유방암 아형(특히 TNBC)별 반응률 차이를 검증할 전향적 임상 데이터
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

