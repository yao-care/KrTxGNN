---
layout: default
title: Vandetanib
parent: 僅模型預測 (L5)
nav_order: 717
evidence_level: L5
indication_count: 10
---

# Vandetanib
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

# Vandetanib: 갑상선수질암에서 신세포암으로

## 한 문장 요약

Vandetanib은 다중 키나제 억제제(VEGFR2/EGFR/RET)로, 해외에서 갑상선수질암(Medullary Thyroid Cancer) 치료제로 승인되었으나 국내에는 아직 시판되지 않았습니다. TxGNN 모델은 **신세포암(Renal Cell Carcinoma)**에도 효과가 있을 수 있다고 예측하며, 현재 **4건의 관련 임상시험**과 **6편의 문헌**이 확인되나, 대부분 소규모이거나 조기 종료되어 근거는 제한적입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 갑상선수질암 (해외 승인, 국내 허가 자료 없음) |
| 예측 신규 적응증 | 신세포암 (Renal Cell Carcinoma) |
| TxGNN 예측 점수 | 99.92% |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 공식적인 작용기전(MOA) 자료는 확보되어 있지 않습니다(DrugBank 조회 필요, Data Gap DG002). 다만 근거 자료에 따르면 Vandetanib은 VEGFR2를 중심으로 한 혈관신생 억제 작용과 RET·EGFR 억제 작용을 겸비한 다중 키나제 억제제이며, 이 기전을 통해 갑상선수질암에서 효능이 입증되어 있습니다.

신세포암, 특히 투명세포암(ccRCC)은 VHL-HIF-VEGF 경로 과활성화로 혈관신생에 크게 의존하는 종양으로, 이미 승인된 sunitinib·pazopanib·cabozantinib 등 동일 계열 항혈관신생제가 표준 치료제로 사용되고 있습니다. Vandetanib의 VEGFR2 억제 기전은 이들과 class effect를 공유하므로 이론적 타당성이 있습니다.

다만 실제로 vandetanib을 RCC에 직접 적용한 임상시험 4건 중 2건(NCT02495103, NCT01372813)은 각각 N=7, N=3의 소규모로 조기 종료(TERMINATED)되어, 효과 부족을 시사하는 부정적 신호로 해석될 여지가 있습니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00566995](https://clinicaltrials.gov/study/NCT00566995) | Phase 2 | 완료 | 37 | Von Hippel Lindau 병 관련 신장 종양에서 vandetanib(ZD6474) 유효성 평가 |
| [NCT01191892](https://clinicaltrials.gov/study/NCT01191892) | Phase 2 | 완료 | 82 | 진행성 요로상피암 1차 치료에서 carboplatin+gemcitabine ± vandetanib 병용 (신세포암 특이적이지 않음, 간접 관련) |
| [NCT02495103](https://clinicaltrials.gov/study/NCT02495103) | Phase 1/2 | 조기 종료 | 7 | HLRCC/SDH 관련 신장암 및 산발성 유두상 신세포암에서 vandetanib+metformin 병용, 소규모로 조기 종료 |
| [NCT01372813](https://clinicaltrials.gov/study/NCT01372813) | Phase 2 | 조기 종료 | 3 | 진행성 투명세포신세포암에서 vandetanib 단독요법, N=3로 조기 종료되어 판독 불가 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [36302175](https://pubmed.ncbi.nlm.nih.gov/36302175/) | 2023 | RCT (비-vandetanib) | Clin Cancer Res | SDH 결핍 GIST·갈색세포종·부신경절종·HLRCC 관련 신세포암 환자 대상 Guadecitabine Phase 2 시험 |
| [40779213](https://pubmed.ncbi.nlm.nih.gov/40779213/) | 2025 | Review/전임상 | Clin Exp Metastasis | Fumarate hydratase 결핍 전이성 신세포암(FHdRCC)의 대사·후성유전학적 재프로그래밍 표적 치료 리뷰 |
| [26677336](https://pubmed.ncbi.nlm.nih.gov/26677336/) | 2015 | Review | OncoTargets Ther | Vandetanib을 포함한 항혈관신생 다중키나제억제제 class effect 리뷰(nintedanib 중심) |
| [28477875](https://pubmed.ncbi.nlm.nih.gov/28477875/) | 2017 | Review | Bull Cancer | Cabozantinib 작용기전·효능·적응증 리뷰 (동일 계열 다중키나제억제제 참고자료) |
| [24451769](https://pubmed.ncbi.nlm.nih.gov/24451769/) | 2012 | Review | ASCO Educ Book | 진행성 갑상선암 전신치료 리뷰, vandetanib이 RET 키나제 억제제로 FDA 승인됨을 기술 (갑상선암, RCC 아님) |
| [31043488](https://pubmed.ncbi.nlm.nih.gov/31043488/) | 2019 | 전임상 (마우스모델) | Mol Cancer Res | TFE3 Xp11.2 전위 신세포암 마우스 모델에서 신규 치료 표적 및 진단 마커(GPNMB) 규명 |

---

## 한국 시판 정보

현재 국내 시판 허가 정보가 없습니다 (미시판, 허가증 0건).

---

## 세포독성

Vandetanib은 알려진 다중 키나제 억제제 계열 항암제로 판단되어 아래 정보를 기재합니다.

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (다중 키나제 억제제 — VEGFR2/EGFR/RET 억제) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
vandetanib을 RCC에 직접 적용한 임상시험 4건 중 2건은 소규모(N=3, N=7)로 조기 종료되어 효능을 뒷받침하기에 근거가 불충분합니다. 또한 국내 미시판 상태이며, TFDA 급 안전성·금기 자료(DG001, Blocking)와 공식 MOA 자료(DG002, High)가 모두 누락되어 있어 안전성 초평가(S1) 단계 진입이 불가능합니다.

**진행하려면 필요한 것:**
- 안전성/금기 정보 확보 — 해외 허가 라벨(FDA/EMA Caprelsa) 검토 (DG001)
- 공식 작용기전(MOA) 자료 확보 — DrugBank API 조회 (DG002)
- 조기 종료된 NCT02495103·NCT01372813의 종료 사유 및 중간 결과 확인
- 대규모·무작위 RCC 임상시험 데이터 확보 또는 신규 연구 설계 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

