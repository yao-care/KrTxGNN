---
layout: default
title: Tegafur
parent: 僅模型預測 (L5)
nav_order: 660
evidence_level: L5
indication_count: 10
---

# Tegafur
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

# Tegafur: 위암에서 대장 종양으로

## 한 문장 요약

Tegafur는 5-FU(5-fluorouracil)의 경구 전구약물로, UFT(tegafur+uracil)나 S-1(tegafur+gimeracil+oteracil) 등 복합제 형태로 위암 화학요법에 널리 사용되어 온 성분입니다.
TxGNN 모델은 **대장 종양(Colonic Neoplasm)**에도 효과가 있을 것으로 예측하며,
현재 **30건의 임상시험**(다수의 완료된 Phase 3 RCT 포함)과 **20편의 문헌**이 이 방향을 강하게 지지합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 위암 (일반적으로 알려진 사용 — 한국 내 허가 이력 없음) |
| 예측 신규 적응증 | 대장 종양 (Colonic Neoplasm) |
| TxGNN 예측 점수 | 99.90% |
| 근거 수준 | L1 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 없습니다. 알려진 정보에 따르면, Tegafur는 fluoropyrimidine 계열 세포독성 항암제이며 5-FU의 경구 전구약물로, UFT나 S-1과 같은 복합제의 핵심 성분입니다. 5-FU는 티미딜산 합성효소(thymidylate synthase)를 억제하여 DNA 합성을 차단함으로써 항종양 효과를 나타냅니다.

위암과 대장 종양은 모두 소화관 상피에서 기원하는 선암으로, 5-FU 계열 약물에 대한 반응 기전이 유사합니다. 실제로 Tegafur 기반 복합제(UFT, S-1)는 이미 대장암 보조/전이성 치료에서 다수의 대규모 Phase 3 RCT를 통해 효능이 입증되어 있어, TxGNN 예측의 기전적 타당성을 뒷받침합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00392899](https://clinicaltrials.gov/study/NCT00392899) | Phase 3 | 완료 | 2025 | 완치 절제된 Stage II 대장암에서 tegafur-uracil 보조화학요법 vs 관찰 비교 |
| [NCT00378716](https://clinicaltrials.gov/study/NCT00378716) | Phase 3 | 완료 | 1608 | 절제된 Stage II/III 대장암에서 UFT+LV vs 5-FU+LV 비교 |
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | 완료 | 1535 | Stage III 대장암 보조요법으로 UFT+LV vs TS-1 비교, 유전자 발현 기반 예측인자 탐색 |
| [NCT00898846](https://clinicaltrials.gov/study/NCT00898846) | N/A | 완료 | 1111 | UFT 보조화학요법을 받은 Stage II 대장암 환자의 예후인자 규명 |
| [NCT00152230](https://clinicaltrials.gov/study/NCT00152230) | Phase 3 | 완료 | 900 | Dukes C 대장직장암에서 UFT 보조요법 vs 수술 단독 비교(NSAS-CC) |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | 불명 | 1191 | Stage III 대장직장암 보조요법으로 SOX(옥살리플라틴+S-1) vs XELOX 비교 |
| [NCT00209742](https://clinicaltrials.gov/study/NCT00209742) | Phase 3 | 불명 | 340 | Stage III 대장직장암 술후 UFT+LV/UFT+PSK 병용요법 비교 |
| [NCT00439517](https://clinicaltrials.gov/study/NCT00439517) | Phase 2 | 완료 | 302 | 전이성 대장암 1차 치료로 FOLFOX+Cetuximab vs UFOX(UFT 포함)+Cetuximab 비교 |
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | 완료 | 161 | 전이성 대장직장암 1차 치료로 S-1 vs Capecitabine 안전성 비교(SALTO 연구) |
| [NCT00905047](https://clinicaltrials.gov/study/NCT00905047) | Phase 3 | 완료 | 89 | 진행성/전이성 대장직장암에서 Xeloda vs UFT+엽산 교차 비교 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT (ACTS-CC 02) | Clinical Colorectal Cancer | 고위험 Stage III 대장암에서 S-1+옥살리플라틴(SOX)의 UFT/LV 대비 우월성 검증 Phase 3 시험 |
| [33714860](https://pubmed.ncbi.nlm.nih.gov/33714860/) | 2021 | RCT (ACTS-CC 02, 업데이트) | ESMO Open | ACTS-CC 02의 5년 생존율 업데이트 및 병기별 하위군 분석 |
| [16648506](https://pubmed.ncbi.nlm.nih.gov/16648506/) | 2006 | RCT (NSABP C-06) | Journal of Clinical Oncology | Stage II/III 대장암에서 경구 UFT+LV와 정맥 5-FU+LV의 무병생존율·전체생존율 비교 |
| [26347106](https://pubmed.ncbi.nlm.nih.gov/26347106/) | 2015 | RCT (JFMC33-0502) | Annals of Oncology | Stage IIB/III 대장암 보조화학요법으로서 UFT/LV의 최적 투여 기간 규명 |
| [33950962](https://pubmed.ncbi.nlm.nih.gov/33950962/) | 2021 | 코호트 연구/메타분석 | Medicine | 대만 국가건강보험 데이터 기반, Stage II/III 대장암에서 UFT vs 5-FU 보조화학요법 효과 비교 |
| [35168560](https://pubmed.ncbi.nlm.nih.gov/35168560/) | 2022 | 전향적 관찰연구 (JFMC46-1201) | BMC Cancer | 재발 위험인자 보유 Stage II 대장암에서 UFT/LV 효능의 성향점수매칭 분석 |
| [38833114](https://pubmed.ncbi.nlm.nih.gov/38833114/) | 2024 | 전향적 관찰연구 (JFMC46-1201, 최종분석) | International Journal of Clinical Oncology | 고위험 Stage II 대장암 UFT/LV 보조요법의 5년 전체생존율 최종 결과 |
| [15108041](https://pubmed.ncbi.nlm.nih.gov/15108041/) | 2004 | RCT | International Journal of Clinical Oncology | 대장직장암에서 OK-432 면역화학요법과 UFT 병용의 효과·안전성 검증 |
| [25209093](https://pubmed.ncbi.nlm.nih.gov/25209093/) | 2014 | Review | Clinical Colorectal Cancer | 아시아 지역 전이성 대장직장암 치료 가이드라인 합의(fluoropyrimidine 계열 포함) |
| [17952521](https://pubmed.ncbi.nlm.nih.gov/17952521/) | 2007 | Review | Surgery Today | UFT(tegafur+uracil)의 폐암·위암·대장직장암·유방암 보조화학요법 임상 근거 및 기전 총설 |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (Fluoropyrimidine 계열, 5-FU 전구체) |
| 골수억제 위험 | 중등도 (호중구감소증, 혈소판감소증이 fluoropyrimidine 계열에서 흔히 보고됨) |
| 구토 유발성 등급 | 저~중등도 |
| 모니터링 항목 | CBC(백혈구/호중구/혈소판), 간·신기능, DPD 효소 활성(중증 독성 예방 목적) |
| 취급 방호 | 세포독성 항암제 취급 규정(개인보호구, 조제 시 생물학적 안전작업대 등) 준수 필요 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
대장 종양에 대해 다수의 완료된 Phase 3 RCT(NCT00392899, NCT00378716, NCT00660894, NCT00152230 등, 총 참여자 수천 명 규모)가 존재하며, fluoropyrimidine 계열 약물(UFT, S-1)의 대장암 치료 효과는 이미 임상적으로 잘 확립되어 있어 근거 수준은 L1로 매우 강합니다. 다만 한국 내 허가·시판 이력이 전무하고, TFDA 경고/금기 정보(DG001, Blocking)와 작용기전(DG002, High) 데이터가 모두 확보되지 않아 안전성 초기 평가(S1)에 진입할 수 없는 상태입니다.

**진행하려면 필요한 것:**
- 한국 식약처(TFDA) 허가사항 PDF 확보 및 경고·금기 정보 파싱 (DG001, Blocking — 최우선)
- DrugBank API를 통한 상세 작용기전(MOA) 데이터 확보 (DG002)
- 한국 내 등재/허가 현황 재조사 (UFT, S-1 등 복합제 형태의 등재 여부 확인)
- 국내 적용 시 DPD 효소 결핍 등 유전형 기반 중증독성 스크리닝 프로토콜 마련
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

