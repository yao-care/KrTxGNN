---
layout: default
title: Dacarbazine
parent: 僅模型預測 (L5)
nav_order: 232
evidence_level: L5
indication_count: 1
---

# Dacarbazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Dacarbazine: 악성흑색종에서 상부 소화호흡관 종양으로

## 한 문장 요약

Dacarbazine(DTIC)은 알킬화 계열 세포독성 항암제로, 전 세계적으로 악성흑색종·호지킨병 등의 치료에 사용되어 온 약물입니다(국내 미상영으로 한국 허가 자료상 적응증 확인은 불가). TxGNN 모델은 **상부 소화호흡관 종양(Upper Aerodigestive Tract Neoplasm)**에 효과가 있을 수 있다고 예측하며, 현재 **임상시험 1건(중단됨)**과 **문헌 20편**이 확인되나 대부분 유사체인 테모졸로마이드(temozolomide) 자료에 의존하고 있어 근거는 초기 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 악성흑색종 등 (국내 미상영으로 한국 허가 데이터 없음, 해외 승인 정보 기준) |
| 예측 신규 적응증 | 상부 소화호흡관 종양 (Upper Aerodigestive Tract Neoplasm) |
| TxGNN 예측 점수 | 99.26% |
| 근거 수준 | L3 |
| 한국 시판 현황 | 미상영 (허가 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

DrugBank의 상세 작용 기전(MOA) 데이터는 현재 확보되지 않았습니다(Data Gap, 우선순위 High). 다만 dacarbazine은 일반적으로 알려진 이미다졸카르복사미드 계열의 알킬화제(alkylating agent)로, 체내에서 활성 대사체인 MTIC(5-(3-methyltriazen-1-yl)imidazole-4-carboxamide)로 전환되어 DNA를 메틸화함으로써 세포독성을 나타내는 것으로 알려져 있습니다.

근거 문헌 다수는 dacarbazine 자체가 아니라 경구용 유사체인 temozolomide(같은 활성 대사체 MTIC를 공유)를 다루고 있습니다. 대표적으로 NCT00423150 임상시험과 그 후속 논문(PMID 23443801)은 MGMT 프로모터 메틸화가 있는 상부 소화호흡관암·대장암 환자에서 temozolomide의 반응을 평가했습니다. 두 약물이 동일한 DNA 메틸화 기전을 공유한다는 점에서, 상부 소화호흡관 종양에 대한 dacarbazine의 잠재적 효과를 뒷받침하는 간접 근거로 볼 수 있습니다.

또한 dacarbazine 자체가 갑상선수질암(PMID 7826911)이나 두경부 혈관육종(PMID 8346929, CYVADIC 요법 성분) 치료에 사용된 사례가 있어, 두경부·소화호흡관 영역 종양에 대한 실제 임상 적용 사례도 일부 존재합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00423150](https://clinicaltrials.gov/study/NCT00423150) | Phase 2 | 중단(Terminated) | 86 | MGMT 프로모터 메틸화 바이오마커로 선별된 진행성 상부 소화호흡관암(대장암, 비소세포폐암, 두경부암, 식도암 포함) 환자 대상 temozolomide(dacarbazine 유사체) 유효성·안전성 평가 |

※ 본 시험은 dacarbazine이 아닌 유사체 temozolomide를 대상으로 하며, dacarbazine 자체의 직접 임상시험은 현재 등록되어 있지 않습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [23443801](https://pubmed.ncbi.nlm.nih.gov/23443801/) | 2013 | Phase 2 임상연구 | Molecular Cancer Therapeutics | MGMT 메틸화 양성 진행성 상부 소화호흡관암·대장암 환자에서 temozolomide 반응 평가(NCT00423150 결과 논문) |
| [7826911](https://pubmed.ncbi.nlm.nih.gov/7826911/) | 1994 | 임상연구 | Annals of Oncology | 진행성 갑상선수질암에서 dacarbazine + 5-FU 병용 화학요법 |
| [41481311](https://pubmed.ncbi.nlm.nih.gov/41481311/) | 2026 | Phase 3 RCT | JAMA Oncology | 말단부 흑색종 1차 치료에서 Toripalimab vs Dacarbazine 비교 |
| [34654328](https://pubmed.ncbi.nlm.nih.gov/34654328/) | 2024 | 후향적 증례연구 | Ear, Nose & Throat Journal | 두경부 악성 부신경절종 임상병리학적 특징 및 치료 |
| [11163509](https://pubmed.ncbi.nlm.nih.gov/11163509/) | 2001 | 후향적 분석 | Int J Radiat Oncol Biol Phys | 후각신경모세포종(비강 내 상부 소화호흡관 종양) 방사선치료 결과 |
| [8346929](https://pubmed.ncbi.nlm.nih.gov/8346929/) | 1993 | 리뷰 | Gan To Kagaku Ryoho | 두경부 혈관육종 화학요법(CYVADIC: dacarbazine 포함 병용요법) |
| [34705104](https://pubmed.ncbi.nlm.nih.gov/34705104/) | 2022 | 리뷰 | J Cancer Res Clin Oncol | EBV 관련 암(비인두암 등 상부 소화호흡관 종양 포함)의 전 세계 부담 추정 |
| [20627492](https://pubmed.ncbi.nlm.nih.gov/20627492/) | 2010 | 리뷰 | Clinical Oncology | 갑상선수질암 개관 |
| [20564093](https://pubmed.ncbi.nlm.nih.gov/20564093/) | 2010 | 후향적 연구 | Cancer | 두경부 부위를 침범한 호지킨림프종의 특징 및 예후 |
| [12113649](https://pubmed.ncbi.nlm.nih.gov/12113649/) | 2002 | 리뷰 | Am J Clin Dermatol | 흑색종 환자 관리 현황(dacarbazine 기존 적응증 배경) |

## 세포독성 (항종양약)

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 항암제 (알킬화제, 이미다졸카르복사미드 유도체) |
| 골수억제 위험 | 중등도~고 (호중구감소증·혈소판감소증 보고) |
| 구토 유발성 등급 | 고위험군 (highly emetogenic 계열로 분류) |
| 모니터링 항목 | CBC(백혈구 분획 포함), 간기능 |
| 취급 방호 | 세포독성 항암제 취급 규정(개인보호구, 폐기 절차) 준수 필요 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (TFDA/한국 허가 경고·금기 자료 미확보 — Data Gap, Blocking 등급)

## 결론 및 다음 단계

**결정: Hold**

**사유:**
안전성 경고·금기 자료가 전혀 확보되지 않아(DG001, Blocking) 안전성 초기평가(S1) 자체가 불가능한 상태입니다. 또한 직접 근거는 조기 중단된 단일 Phase 2 연구(그마저도 dacarbazine이 아닌 유사체 temozolomide 대상) 1건과 다수의 간접·배경 문헌에 그쳐 근거 수준이 L3에 머뭅니다.

**진행하려면 필요한 것:**
- TFDA/한국 식약처 허가 경고·금기 자료 확보 (DG001 해소)
- DrugBank API를 통한 상세 MOA 확인 (DG002 해소)
- dacarbazine 자체(유사체 temozolomide 아님)의 상부 소화호흡관 종양 대상 직접 임상 데이터 추가 확인
- 국내 미상영 상태이므로 도입 시 별도 허가 경로 검토 필요
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

