---
layout: default
title: Larotrectinib
parent: 모델 예측만 (L5)
nav_order: 461
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Larotrectinib: 예측 신규 적응증 다발성 내분비 종양 (Multiple Endocrine Neoplasia) (근거 수준 L5). 기존 적응증: 이 약은 알려진 획득 내성 돌연변이 없이 NTRK 유전자 융합을 보유한 다음 성인 및 소아 환자의 치료에…"
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
| 기존 적응증 | 이 약은 알려진 획득 내성 돌연변이 없이 NTRK 유전자 융합을 보유한 다음 성인 및 소아 환자의 치료에 사용한다. • 국소진행성, 전이성 또는 수술적 절제 시 중증 이환의 가능성이 높으며 기존 치료제(혹은 치료 요법) 이후진행되었거나 현재 이용 가능한 적합한 치료제가 없는 고형암 이… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202003383/EE)) |
| 예측 신규 적응증 | 다발성 내분비 종양 (Multiple Endocrine Neoplasia) |
| TxGNN 예측 점수 | 0.9924 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 3건 / 전체 3건) |
| 허가증 수 | 3건 (유효 3건) |
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

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 202003383 | 비트락비캡슐25밀리그램(라로트렉티닙황산염) | 미색 - 노란색 - 분홍색을 띤 노란색 고체가 든 “Bayer cross… | 바이엘코리아(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202003383/EE) | 유효 |
| 202003384 | 비트락비캡슐100밀리그램(라로트렉티닙황산염) | 미색 - 노란색 - 분홍색을 띤 노란색 고체가 든 “Bayer cross… | 바이엘코리아(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202003384/EE) | 유효 |
| 202003385 | 비트락비액(라로트렉티닙황산염) | 무색 - 노란색 또는 오렌지색 또는 빨간색 또는 갈색을 띤 이물이 없는… | 바이엘코리아(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202003385/EE) | 유효 |

<!-- licenses:end -->

(제조사: 바이엘코리아(주); 허가 건수와 상태는 빠른 개요 참조)

<!-- review:begin kr-lic-20261124c-larotrectinib-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “(제조사: 바이엘코리아(주), 3건 모두 유효한 단일제)” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 이 사이트 자료의 성분란에는 일치한 성분만 기록되어 허가 품목별 단일 성분·복합 성분 여부를 확인할 수 없으므로, 단일·복합 표기를 빼고 건수는 쓰지 않고 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-larotrectinib-1 -->

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

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-24 | 단일·복합 표기: “(제조사: 바이엘코리아(주), 3건 모두 유효한 단일제)” → 확인할 수 없는 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

