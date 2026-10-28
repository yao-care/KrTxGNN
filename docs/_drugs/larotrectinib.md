---
layout: default
title: Larotrectinib
parent: 모델 예측만 (L5)
nav_order: 461
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Larotrectinib: 예측 신규 적응증 다발성 내분비 종양 (Multiple Endocrine Neoplasia) (근거 수준 L3). 기존 적응증: 허가 문서 링크만 확인되며 적응증 본문은 확인되지 않음 (허가사항 참조 필요)"
monitor_inn: "Larotrectinib"
predicted_indications: ["multiple endocrine neoplasia", "HER2 positive breast carcinoma"]
---

# Larotrectinib
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **2** 건
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

## Larotrectinib: NTRK 융합 양성 고형암에서 다발성 내분비 종양으로
{: .text-alpha }

## 한 문장 요약

Larotrectinib은 선택적 TRK 억제제로, 한국에서 비트락비(Vitrakvi)라는 제품명으로 허가되어 시판 중입니다. TxGNN 모델은 **다발성 내분비 종양(multiple endocrine neoplasia)**에 효과가 있을 수 있다고 예측하지만, 뒷받침하는 근거는 **1건의 임상시험(Phase 2 바스켓 시험)**과 **2편의 문헌**에 그치며 간접적인 수준입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 문서 링크만 확인되며 적응증 본문은 확인되지 않음 (허가사항 참조 필요) |
| 예측 신규 적응증 | 다발성 내분비 종양 (Multiple Endocrine Neoplasia) |
| TxGNN 예측 점수 | 0.9924 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 3건 |
| 권장 결정 | Hold (연구 질문 단계) |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 확보되지 않았습니다. 알려진 정보에 따르면 Larotrectinib은 선택적 TRK(TRKA/B/C) 억제제이며, NTRK 유전자 융합 양성 고형암에 대한 조직 비특이적(tumor-agnostic) 치료제로 사용됩니다.

다발성 내분비 종양(특히 MEN2)은 NTRK 융합이 아니라 RET 생식세포 활성화 돌연변이로 발생합니다. 따라서 TRK 억제와의 연관성은 간접적입니다. 관련 문헌은 RET 유래 갑상선 수질암과 RET 억제제 내성에 관한 것으로, 키나제 경로 간 상호작용 가능성은 시사하지만 TRK에 대한 직접적 의존성을 보여주지는 않습니다. 이점이 있다면 NTRK 융합 양성이라는 드문 일부 종양에 한정될 가능성이 높습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02465060](https://clinicaltrials.gov/study/NCT02465060) | Phase 2 | 진행 중 (모집 종료) | 6,452 | NCI-MATCH. 유전자 검사 기반 치료를 평가하는 바스켓 시험으로 larotrectinib/NTRK 융합 투약군 포함. MEN에 특이적이지 않고 단일군 비무작위 설계 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [31322645](https://pubmed.ncbi.nlm.nih.gov/31322645/) | 2019 | Review | Endocrine Reviews | 진행성 갑상선암에 대한 키나제 억제제 표적치료 개관 |
| [38438731](https://pubmed.ncbi.nlm.nih.gov/38438731/) | 2024 | 전임상/기전 연구 | NPJ Precision Oncology | RET 유래 암에서 선택적 RET 억제에 대한 내성 기전 (selpercatinib 투여 갑상선 수질암 환자) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202003383 | 비트락비캡슐25밀리그램 | 경질캡슐 (25 mg) | 허가사항 참조 |
| 202003384 | 비트락비캡슐100밀리그램 | 경질캡슐 (100 mg) | 허가사항 참조 |
| 202003385 | 비트락비액 | 경구용액제 | 허가사항 참조 |

(제조사: 바이엘코리아(주), 3건 모두 유효한 단일제)

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (TRK 억제제) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **약물 상호작용**: 이번 보고서용으로 수집된 데이터에서 총 100건의 상호작용이 확인되었으며, 그중 일부만 제시합니다.
  - **주요(Major)**: Clarithromycin
  - **중등도(Moderate)**: Hydrocortisone, Dexamethasone, Betamethasone, Triamcinolone, Budesonide, Pioglitazone, Aprepitant, Omeprazole, Cimetidine, Saxagliptin, Dolasetron, Dronabinol, Eliglustat, Naldemedine, Naltrexone, Cisapride, Clotrimazole
  - **경미(Minor)**: Naloxegol

경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold (연구 질문 단계)**

**사유:**
TxGNN 점수는 높지만, 다발성 내분비 종양은 RET 구동 질환으로 TRK 억제와의 기전적 연관이 간접적입니다. 근거는 비특이적 Phase 2 바스켓 시험 1건과 간접적 문헌 2편뿐이며, MEN에 직접 적용된 임상 데이터는 없습니다. NTRK 융합 양성이라는 드문 하위군에서만 이점이 기대됩니다.

**진행하려면 필요한 것:**
- 허가사항의 경고, 금기, 적응증 본문 확보 (현재 확인되지 않음)
- 작용 기전(MOA) 상세 데이터
- NTRK 융합 양성 다발성 내분비 종양 사례 또는 NCI-MATCH 내 해당 하위군 결과 확인
- NTRK 융합 검사에 기반한 환자 선별 전략 수립

### 참고: 기타 예측 적응증

| 순위 | 예측 질환 | 점수 | 근거 수준 | 비고 |
|------|---------|------|---------|------|
| 2 | HER2 양성 유방암 | 0.9914 | L4 | 다른 TRK 억제제(entrectinib)의 전임상 연구와 분비성 유방암 증례뿐. Hold |
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

