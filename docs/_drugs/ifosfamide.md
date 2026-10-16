---
layout: default
title: Ifosfamide
parent: 모델 예측만 (L5)
nav_order: 413
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ifosfamide: 예측 신규 적응증 여성 유방암 (Female Breast Carcinoma) (근거 수준 L5). 기존 적응증: 확인 불가 (허가증에 문서 링크만 기재되어 있음)"
---

# Ifosfamide
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

# Ifosfamide: 항암화학요법제에서 여성 유방암으로

## 한 문장 요약

Ifosfamide는 DNA를 알킬화하는 항암제로, 한국에서는 홀록산주(1000 mg 주사제)로 시판되고 있습니다. 다만 허가 적응증 문구는 문서 링크로만 확인되어 구체적인 질환명은 이번 자료에서 확인되지 않았습니다.
TxGNN 모델은 **여성 유방암(female breast carcinoma)**에 효과가 있을 수 있다고 예측하며, 이 예측에 대해 **6건의 임상시험**과 **20편의 문헌**이 검토되었으나 대부분 2상 이하 또는 복합요법 연구입니다.
참고로 예측 순위가 더 낮은 **횡문근육종**은 3상 임상시험 근거가 가장 탄탄하여, 별도 검토할 만합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가증에 문서 링크만 기재되어 있음) |
| 예측 신규 적응증 | 여성 유방암 (Female Breast Carcinoma) |
| TxGNN 예측 점수 | 99.91% |
| 근거 수준 | L2 (3상 RCT 없음, 2상 시험과 문헌 중심) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold (연구 과제로 분류) |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 이번 자료에 없습니다. 다만 문헌에 따르면 Ifosfamide는 간 CYP450 효소로 활성화되는 알킬화 전구약물입니다. 활성 대사체인 isophosphoramide mustard가 DNA를 교차결합시켜 증식하는 종양세포의 사멸을 유도합니다.

이 기전은 유방암 세포에도 적용될 수 있습니다. 실제로 전이성 유방암에서 Ifosfamide 단독 요법의 반응률은 7~30%로 보고되었고, 병용요법에서는 더 높은 반응률이 보고되었습니다. 또한 유방암 조직에서 Ifosfamide를 대사하는 CYP 효소 발현이 확인된 연구도 있습니다.

다만 Ifosfamide는 일반적인 유방암 아형의 표준 치료 기반 약물이 아닙니다. 따라서 사용은 불응성 질환이나 화생성 유방암, 엽상종양 같은 특수 조직형으로 제한될 가능성이 큽니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00026078](https://clinicaltrials.gov/study/NCT00026078) | Phase 2 | 불명 | 42 | 전이성 유방암 1차 치료에서 docetaxel + ifosfamide 병용 평가 (관련성 가장 높음) |
| [NCT00012311](https://clinicaltrials.gov/study/NCT00012311) | Phase 2 | 불명 | 미상 | 전이성 유방암에서 다주기 고용량 화학요법과 최적 표준용량 화학요법 비교 |
| [NCT00002854](https://clinicaltrials.gov/study/NCT00002854) | Phase 1 | 완료 | 33 | 진행성 암에서 고용량 cisplatin, cyclophosphamide, etoposide, ifosfamide 등 순차 투여 + 자가 줄기세포 지지 |
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | 중단 | 미상 | 전이성 유방암에서 고용량 topotecan, ifosfamide/mesna, etoposide + 자가 줄기세포 구제 |
| [NCT00003086](https://clinicaltrials.gov/study/NCT00003086) | Phase 1/2 | 중단 | 12 | 4기 유방암에서 samarium-153 포함 이중 자가 골수이식 |
| [NCT00020722](https://clinicaltrials.gov/study/NCT00020722) | Phase 2 | 중단 | 7 | 4기 유방암에서 줄기세포 이식 후 활성화 T세포 치료 |

대부분 고용량 병용요법 연구여서 Ifosfamide 단독 효과를 분리해 판단하기 어렵습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [14586149](https://pubmed.ncbi.nlm.nih.gov/14586149/) | 2003 | Review | Oncology | 진행성 유방암에서 단독 반응률 7~30%, 병용 시 더 높은 반응률. mesna로 요독성 감소 |
| [39306877](https://pubmed.ncbi.nlm.nih.gov/39306877/) | 2024 | Cohort | Current Problems in Cancer | 화생성 유방암에서 Ifosfamide 기반 1차 화학요법 경험 |
| [39074497](https://pubmed.ncbi.nlm.nih.gov/39074497/) | 2024 | Cohort | JNCCN | 악성 엽상종양에서 보조 화학요법의 장기 예후 영향 |
| [8918497](https://pubmed.ncbi.nlm.nih.gov/8918497/) | 1996 | Phase 2 | J Clin Oncol | 전이성 유방암 1차 치료에서 ifosfamide + vinorelbine |
| [8445421](https://pubmed.ncbi.nlm.nih.gov/8445421/) | 1993 | Phase 2 | J Clin Oncol | 전이성 유방암 1차 치료에서 ifosfamide + mitoxantrone |
| [11932893](https://pubmed.ncbi.nlm.nih.gov/11932893/) | 2002 | Phase 2 | Cancer | 안트라사이클린 내성 전이성 유방암에서 paclitaxel(24시간 주입) + ifosfamide |
| [9226029](https://pubmed.ncbi.nlm.nih.gov/9226029/) | 1997 | 임상연구 | Tumori | 기치료 진행성 유방암에서 ifosfamide + etoposide |
| [1390313](https://pubmed.ncbi.nlm.nih.gov/1390313/) | 1992 | 문헌고찰 | Ann Oncol | 유방암에서 Ifosfamide 사용 개관, 단독 요법 객관적 반응 약 20% |
| [1720382](https://pubmed.ncbi.nlm.nih.gov/1720382/) | 1991 | Review | Drugs | Ifosfamide/mesna의 항종양 활성, 약동학, 치료 효능 종합 고찰 |
| [14970873](https://pubmed.ncbi.nlm.nih.gov/14970873/) | 2004 | 기전 연구 | Br J Cancer | 유방암 조직의 CYP3A4, CYP2C9, CYP2B6 발현과 Ifosfamide 대사 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200804588 | 홀록산주1000밀리그람(이포스파마이드) (부광약품) | 흰색의 결정성 가루가 들어있는 바이알 (주사제) | 허가 적응증 본문은 문서 링크로만 제공되어 확인되지 않음 |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (알킬화제, oxazaphosphorine 계열) |
| 골수억제 위험 | 고 (문헌에서 골수억제가 주요 독성으로 언급됨) |
| 구토 유발성 등급 | 중~고 (약물 계열 기준의 일반적 평가, 허가사항 확인 필요) |
| 모니터링 항목 | CBC(분류 포함), 신기능, 간기능, 소변검사(혈뇨), 신경학적 증상 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

허가사항의 경고 및 주의사항을 함께 참조하세요.

## 안전성 고려사항

- **약물 상호작용**: 이번 조회에서 총 100건이 확인되었고, 아래는 일부입니다.
  - 중등도: Amphotericin B, Bupropion, Aprepitant, Morphine, Metoclopramide, Scopolamine, Dronabinol, Nabilone, Kanamycin, Neomycin
  - 중등도(혈당강하제): Chlorpropamide, Glimepiride, Glipizide, Glyburide, Nateglinide, Repaglinide, Tolazamide, Acetohexamide
  - 경미: Levofloxacin
- **문헌상 주의점**: mesna 병용 요로독성 예방, 신독성, 신경독성, 골수억제, 이차 백혈병/골수형성이상증후군 위험이 언급되었습니다.

주요 경고와 금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold (연구 과제로 분류)**

**사유:**
유방암에서 Ifosfamide의 활성은 여러 2상 시험과 문헌으로 뒷받침되지만, 3상 RCT가 없고 표준 치료도 아닙니다. 또한 한국 허가 적응증 본문과 안전성 정보(경고·금기)가 확보되지 않아 안전성 심사를 진행할 수 없습니다.

**진행하려면 필요한 것:**
- 식약처 허가사항(첨부문서) 확보: 허가 적응증, 경고, 금기
- 상세한 약물 작용 기전(MOA) 데이터 (DrugBank 조회)
- 유방암에서 Ifosfamide를 직접 평가한 2상 이상 결과 확인 (예: NCT00026078 결과 확인)
- 불응성 또는 화생성 유방암 등 특수 조직형으로 대상 인구집단 한정
- 참고: 순위 7위 **횡문근육종**은 연성조직육종 3상 RCT(예: NCT00061984, NCT00003212) 근거로 L1, Proceed with Guardrails로 평가되었으나, 횡문근육종 특이적 3상 근거는 별도 확인이 필요합니다.
- 순위 2~6, 8~9위(골수형성이상증후군, 5q 결손, 소아 불응성 혈구감소증, 재생불량성 빈혈 등)는 근거가 없거나 Ifosfamide가 오히려 위험 요인이므로 Hold 권고입니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

