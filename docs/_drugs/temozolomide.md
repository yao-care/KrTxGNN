---
layout: default
title: Temozolomide
parent: 僅模型預測 (L5)
nav_order: 663
evidence_level: L5
indication_count: 2
---

# Temozolomide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Temozolomide: 기존 적응증 정보 없음에서 성인 성상세포종으로

## 한 문장 요약

Temozolomide(테모졸로마이드, DrugBank ID: DB00853)는 한국 내 허가·시판 이력이 없어 기존 적응증 데이터가 확보되지 않은 상태입니다.
TxGNN 모델은 **성인 성상세포종(Adult Astrocytic Tumour)**에 효과가 있을 것으로 **99.36%** 확률로 예측하며,
현재 **2건의 임상시험**(Phase 3 완료 포함)과 **20편의 문헌**(다수의 완료된 Phase 3 RCT 포함)이 이 방향을 강하게 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (한국 미출시, 원 적응증 정보 미수집) |
| 예측 신규 적응증 | 성인 성상세포종 (Adult Astrocytic Tumour) |
| TxGNN 예측 점수 | 99.36% |
| 근거 수준 | L1 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Temozolomide는 경구 알킬화제(alkylating agent) 전구약물로, 혈액뇌장벽을 통과한 뒤 생리적 pH 조건에서 활성대사체 MTIC로 전환됩니다. 이후 구아닌 O6/N7 위치에 DNA 메틸화 손상을 일으켜 종양세포의 apoptosis를 유도하는 기전을 가집니다.

이 기전은 성상세포종(glioblastoma를 포함)에 대한 표준 화학요법의 근간으로, MGMT 프로모터 메틸화 상태와 약물 반응성 간의 연관성 또한 분자생물학적으로 잘 정립되어 있습니다.

예측된 신규 적응증인 "성인 성상세포종"은 실제로 Stupp 등의 2005년 NEJM 연구를 시작으로 다수의 완료된 Phase 3 RCT를 통해 방사선치료+TMZ 병용요법의 생존 이익이 반복적으로 입증된 영역입니다. 이는 TxGNN 예측의 기전적 타당성을 강하게 뒷받침합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00052455](https://clinicaltrials.gov/study/NCT00052455) | Phase 3 | 완료 | 500 | 재발성 WHO Grade III/IV 성상세포종에서 TMZ 단독요법 vs PCV(procarbazine/lomustine/vincristine) 비교 |
| [NCT00960492](https://clinicaltrials.gov/study/NCT00960492) | Phase 1 | 완료 | 26 | 신규진단 교모세포종에서 XL184(cabozantinib) + TMZ + 방사선치료 병용 용량설정 (TMZ는 표준 병용요법 성분) |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [40779733](https://pubmed.ncbi.nlm.nih.gov/40779733/) | 2025 | RCT | J Clin Oncol | MGMT 비메틸화 신규진단 교모세포종에서 ipilimumab+nivolumab 이중 면역관문차단 병용 Phase II/III (NRG BN007) |
| [30782343](https://pubmed.ncbi.nlm.nih.gov/30782343/) | 2019 | RCT | Lancet | MGMT 메틸화 신규진단 교모세포종, lomustine-TMZ 병용 vs TMZ 단독 (CeTeG/NOA-09) |
| [26670971](https://pubmed.ncbi.nlm.nih.gov/26670971/) | 2015 | RCT | JAMA | Tumor-Treating Fields + TMZ 유지요법 vs TMZ 단독 |
| [25920709](https://pubmed.ncbi.nlm.nih.gov/25920709/) | 2015 | RCT | J Neurooncol | 신규진단 역형성 성상세포종에서 방사선+TMZ 병용 후 13-cis 레티노산 유지요법 |
| [24552317](https://pubmed.ncbi.nlm.nih.gov/24552317/) | 2014 | RCT | N Engl J Med | 신규진단 교모세포종에서 bevacizumab 추가요법 무작위 시험 |
| [22578793](https://pubmed.ncbi.nlm.nih.gov/22578793/) | 2012 | RCT | Lancet Oncol | 고령 악성 성상세포종에서 TMZ 단독 vs 방사선치료 단독 (NOA-08) |
| [19269895](https://pubmed.ncbi.nlm.nih.gov/19269895/) | 2009 | RCT | Lancet Oncol | 방사선+TMZ 병용/유지요법의 5년 생존 분석 (EORTC-NCIC) |
| [15758009](https://pubmed.ncbi.nlm.nih.gov/15758009/) | 2005 | RCT | N Engl J Med | 신규진단 교모세포막종에서 방사선+TMZ 병용요법 (Stupp 요법, 표준치료 확립 연구) |
| [36809318](https://pubmed.ncbi.nlm.nih.gov/36809318/) | 2023 | Review | JAMA | 성인 원발성 뇌종양(교모세포종 등) 전반에 대한 리뷰 |

---

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (알킬화제, Imidazotetrazine 유도체) |
| 골수억제 위험 | 중~고 — 알킬화제 계열 특성상 혈소판감소증·호중구감소증 발생 가능하나, 본 Evidence Pack에는 구체적 등급 데이터가 없어 허가사항 확인 필요 |
| 구토 유발성 등급 | 데이터 없음 — 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | CBC(백혈구 분획 포함), 간·신기능 |
| 취급 방호 | 세포독성 항암제 표준 취급 규정 준수 필요 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
성인 성상세포종에 대한 TMZ의 효능은 Stupp 2005(NEJM) 연구를 포함해 다수의 완료된 Phase 3 RCT로 뒷받침되며 근거 수준 L1에 해당합니다. 다만 한국 내 허가·시판 이력이 전무하고, 규제기관 수준의 경고·금기 정보 확보가 Blocking 데이터 갭으로 남아 있어 안전성 초기평가 단계 진입에 제약이 있습니다.

**진행하려면 필요한 것:**
- 규제기관(허가) 수준의 경고·금기 정보 확보 — Blocking 데이터 갭
- DrugBank 기반 상세 작용기전(MOA) 및 독성 프로파일 정식 확인 — High 우선순위 데이터 갭
- 한국 내 허가/시판 현황 확인 (현재 0건)
- 참고: 동일 Evidence Pack 내 2순위 후보인 마미신경총 종양(cauda equina neoplasm)은 근거 수준 L4로, 추가 기전·임상 자료 없이는 Hold 상태 유지 권장
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

