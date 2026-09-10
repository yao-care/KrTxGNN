---
layout: default
title: Lorazepam
parent: 僅模型預測 (L5)
nav_order: 448
evidence_level: L5
indication_count: 10
---

# Lorazepam
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

# Lorazepam: 진정·항불안·항경련 용도에서 불면증으로

## 한 문장 요약

Lorazepam은 GABA-A 수용체 양성 알로스테릭 조절제로 작용하는 벤조디아제핀 계열 약물로, 진정·항불안·항경련 효과가 임상적으로 잘 알려져 있습니다(단, 한국 허가 정보는 확인되지 않음).
TxGNN 모델은 **불면증(Insomnia)**에 효과가 있을 것으로 예측하며, 현재 **23건의 임상시험**과 **18편의 문헌**이 이 방향을 뒷받침합니다.
다만 이 예측은 완전히 새로운 적응증이라기보다, 임상에서 이미 수십 년간 실제 사용되어 온 용도(재확인형 근거)에 가깝습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (DrugBank 원 적응증 정보 미기재, 한국 허가 자료 없음) |
| 예측 신규 적응증 | 불면증 (Insomnia) |
| TxGNN 예측 점수 | 99.80% |
| 근거 수준 | L2 |
| 한국 시판 현황 | ✗ 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 확보되지 않았습니다([Data Gap]). 다만 증거 팩 내 근거 서술에 따르면 Lorazepam은 GABA-A 수용체를 표적으로 하는 벤조디아제핀 계열 약물로, 진정·항불안·항경련 효과가 확립되어 있습니다.

불면증에 대한 예측은 이러한 GABA-A 매개 진정 작용의 직접적 연장선입니다. 실제로 Lorazepam은 임상에서 이미 수면 유도 목적으로 오랫동안 사용되어 왔으며(예: TID 용법의 만성 불면증 치료, 다른 수면제와의 병용 연구), 이번 예측은 새로운 기전 발견이라기보다 기존 off-label/역사적 사용 패턴을 데이터 기반으로 재확인한 결과에 가깝습니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03331042](https://clinicaltrials.gov/study/NCT03331042) | Phase 3 | 완료 | 85 | Diphenhydramine+Zolpidem+Lorazepam 병용제(SM-1)의 일시적 불면증 효능·안전성 평가, 4-way crossover |
| [NCT02671760](https://clinicaltrials.gov/study/NCT02671760) | Phase 2 | 완료 | 39 | Diphenhydramine+Zolpidem+Lorazepam 병용제가 총 수면시간에 미치는 약력학적 효과 평가 |
| [NCT04396327](https://clinicaltrials.gov/study/NCT04396327) | Phase 2 | 미모집 | 14 | SM-1(Lorazepam 병용 포함) vs 활성대조군, 일시적 불면증 3시간 phase-advance 모델 |
| [NCT03338764](https://clinicaltrials.gov/study/NCT03338764) | Phase 3 | 철회 | 0 | SM-1(병용제) 계열 일시적 불면증 효능 평가 시험이었으나 등록 전 철회 |
| [NCT04572750](https://clinicaltrials.gov/study/NCT04572750) | NA | 완료 | 170 | 벤조디아제핀(Lorazepam 등) 장기 복용자 대상 전자기기 기반 자가 중단 관리 프로그램 |
| [NCT06584513](https://clinicaltrises.gov/study/NCT06584513) | NA | 모집중 | 470 | 고령자 대상 벤조디아제핀/진정수면제 사용 감소를 위한 환자중심 개입(BE-SAFE) |
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | 불명 | 1400 | 대만 고령자 대상 수면제(벤조디아제핀 포함) 장단기 사용 패턴 및 위험-효익 전향적 코호트 |
| [NCT01343095](https://clinicaltrials.gov/study/NCT01343095) | NA | 중단 | 8 | 중환자실 야간 소음 감소가 섬망 및 진정제 사용량에 미치는 영향 평가 |
| [NCT01893632](https://clinicaltrials.gov/study/NCT01893632) | Phase 2 | 중단 | 2 | Gabapentin을 이용한 벤조디아제핀 의존 치료(직접적 Lorazepam 효능 시험 아님) |
| [NCT00826553](https://clinicaltrials.gov/study/NCT00826553) | Phase 1 | 중단 | 6 | 기계환기 환자에서 α2 작용제 vs GABA 작용제 진정이 수면다원검사 소견에 미치는 영향 비교 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [3280615](https://pubmed.ncbi.nlm.nih.gov/3280615/) | 1988 | RCT | Journal of Clinical Pharmacology | 만성 불면증 환자에서 Lorazepam(2mg)과 Flurazepam(30mg) 비교, 이중맹검 교차시험 — Lorazepam이 대부분 수면 지표에서 우수 |
| [10220122](https://pubmed.ncbi.nlm.nih.gov/10220122/) | 1999 | Cohort/Clinical Study | International Clinical Psychopharmacology | 만성 불면증에서 1일 3회 저용량(0.5mg TID) vs 취침 전 고용량(1.5mg HS) Lorazepam 비교 |
| [30625122](https://pubmed.ncbi.nlm.nih.gov/30625122/) | 2018 | Review | The Medical Letter on Drugs and Therapeutics | 만성 불면증 치료제 전반에 대한 검토 (벤조디아제핀 포함) |
| [30625124](https://pubmed.ncbi.nlm.nih.gov/30625124/) | 2018 | Review(부속표) | The Medical Letter on Drugs and Therapeutics | 만성 불면증에 사용되는 경구 수면제 비교표 |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta-analysis/Cohort | Acta Pharmaceutica | 고령 환자 대상 진정제(트랑퀼라이저) 치료 효과 메타분석 — 용량·부작용 평가 |
| [15341891](https://pubmed.ncbi.nlm.nih.gov/15341891/) | 2004 | Cohort | Sleep Medicine | 대규모 관리의료 인구집단에서 수면제 처방 패턴 분석 |
| [25453732](https://pubmed.ncbi.nlm.nih.gov/25453732/) | 2014 | 관찰연구 | Clinical Therapeutics | 고령 중증질환 재향군인에서 벤조디아제핀/진정수면제 부적절 사용 실태 (Choosing Wisely) |
| [40110386](https://pubmed.ncbi.nlm.nih.gov/40110386/) | 2025 | 역학연구 | Alpha Psychiatry | 중국 동부지역 벤조디아제핀 및 Z-drug 처방 추세(2015–2021) 분석 |
| [19514972](https://pubmed.ncbi.nlm.nih.gov/19514972/) | 2009 | 전임상 연구 | Drug Delivery | Lorazepam 등 벤조디아제핀 비강 마이크로에멀전 제형 개발 및 동물 수면유도 효력 평가 |
| [35087274](https://pubmed.ncbi.nlm.nih.gov/35087274/) | 2022 | 문헌고찰 | Journal of Multidisciplinary Healthcare | COVID-19 환자의 불면증(coronasomnia) 치료 효능·안전성·약물상호작용 검토 |

---

## 한국 시판 정보

현재 한국에 허가된 Lorazepam 제품 정보가 확인되지 않습니다(미출시, 허가증 0건).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (참고: TFDA 수준의 경고/금기 정보는 현재 Blocking 등급 데이터 갭으로 분류되어 있어 S1 안전성 초평가 진입이 불가한 상태입니다.)

---

## 참고: 그 외 예측 적응증 (동일 후보 팩 내 추가 예측)

이 증거 팩에는 불면증 외에도 9개의 예측 적응증이 포함되어 있습니다. 대부분 반사성 발작(reflex seizure) 계열이며 근거 수준이 낮아 별도 검토가 필요합니다.

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 | 권장 결정 | 비고 |
|------|------------|-----------|----------|----------|------|
| 1 | 삼차신경 종양 (Trigeminal nerve neoplasm) | 99.87% | L5 | Hold | 임상시험/문헌 0건, 기전 연관성 없음 — KG 임베딩 위양성 가능성 높음 |
| 3 | 독서 유발 발작 (Reading seizures) | 99.64% | L4 | Research Question | 일반 광과민성 뇌전증 문헌 외삽, 해당 아형 직접 근거 없음 |
| 4 | 오르가즘 유발 발작 | 99.63% | L5 | Hold | 임상시험/문헌 0건 |
| 5 | 청각(음성) 유발 발작 | 99.63% | L4 | Research Question | 대부분 동물 금단증후군 연구, 치료 근거 아님 |
| 6 | 섭식 유발 발작 | 99.63% | L5 | Hold | 관련성 낮은 문헌뿐(가성발작, 세로토닌증후군 등) |
| 7 | 배뇨 유발 발작 | 99.63% | L3 | Proceed with Guardrails | Status epilepticus 표준치료 기전의 합리적 외삽, 해당 아형 직접시험은 없음 |
| 8 | 사고 유발 발작 | 99.63% | L4 | Research Question | 일반 뇌전증중첩증 문헌뿐, 특이적 근거 없음 |
| 9 | 경악 유발 간질 (Startle epilepsy) | 99.63% | L4 | Research Question | 1986년 소아 뇌전증 벤조디아제핀 리뷰 1편뿐 |
| 10 | 이상성 경련 동반 급성 뇌증 (AESD) | 99.47% | L5 | Hold | 임상시험/문헌 0건 |

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails** (불면증 적응증 기준)

**사유:**
- 불면증 예측은 Phase 2/3 완료 RCT 및 1988년 RCT(PMID 3280615)를 포함해 L2 수준의 근거를 갖추고 있으며, 이는 완전히 새로운 기전 가설이 아니라 이미 확립된 벤조디아제핀 수면유도 용도의 재확인입니다.
- 반면 최고 TxGNN 점수를 받은 삼차신경 종양 등 다수의 예측은 근거가 전무하거나(L5) 간접 외삽 수준(L4)에 그쳐 현 단계에서는 보류(Hold) 또는 연구질문(Research Question) 단계에 머물러야 합니다.

**진행하려면 필요한 것:**
- TFDA/한국 규제기관의 공식 경고·금기사항 자료 확보 (DG001, Blocking) — S1 안전성 초평가 진입 전제조건
- DrugBank 등에서 공식 작용기전(MOA) 데이터 확보 (DG002, High)
- 한국 내 허가·시판 현황 재확인 (현재 미출시로 기재됨)
- 배뇨 유발 발작 등 L3 후보에 대한 추가 문헌/증례 검토
- 삼차신경 종양 등 L5 후보는 추가 근거 없이는 파이프라인에서 제외 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

