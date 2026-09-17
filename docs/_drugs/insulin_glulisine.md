---
layout: default
title: Insulin Glulisine
parent: 모델 예측만 (L5)
nav_order: 398
evidence_level: L5
indication_count: 10
---

# Insulin Glulisine
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

# 인슐린 글루리진: 당뇨병에서 제1형 당뇨병으로

## 한 문장 요약

인슐린 글루리진(Insulin Glulisine, DrugBank DB01309)은 초속효성 인슐린 유사체로 당뇨병 환자의 식후 혈당 조절(bolus insulin)에 사용되는 약물입니다. TxGNN 모델은 **제1형 당뇨병(Type 1 Diabetes Mellitus)**에 효과가 있을 것으로 예측하며, 현재 **최소 3건 이상의 완료된 Phase 3 RCT를 포함한 50건의 임상시험**과 **19편의 문헌**이 이를 뒷받침합니다.

> ⚠️ **중요 주의**: 이 예측은 "새로운 적응증 발굴"이 아니라 **인슐린 글루리진의 기존 승인 적응증을 재발견한 것**일 가능성이 높습니다. Evidence Pack 상 `original_indications`가 데이터 누락([Data Gap])으로 비어 있어, 파이프라인이 이미 알려진 원 적응증을 "신규 예측"으로 오분류했을 개연성이 근거 문서 자체에 명시되어 있습니다. 아래 내용은 이 전제하에 해석해야 합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 누락 (단, 인슐린 글루리진은 임상적으로 당뇨병 전반의 식후 혈당조절제로 이미 널리 사용됨) |
| 예측 신규 적응증 | 제1형 당뇨병 (Type 1 Diabetes Mellitus) — 실질적으로는 기존 적응증일 가능성 높음 |
| TxGNN 예측 점수 | 99.55% |
| 근거 수준 | L1 (완료된 Phase 3 RCT ≥2건) |
| 한국 시판 현황 | 미출시 (허가 등록 0건) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold — 데이터 정합성 확인 필요 |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 확보되지 않았습니다([Data Gap]). 다만 알려진 약리학적 정보에 따르면, 인슐린 글루리진은 인간 인슐린의 아미노산 서열을 변형한 **초속효성 인슐린 유사체**로, 인슐린 수용체에 결합해 말초 조직의 포도당 흡수를 촉진하고 간의 포도당 생성을 억제하여 혈당을 낮춥니다. 이 기전은 제1형·제2형 당뇨병 모두에서 이미 확립되어 있으며, 특히 제1형 당뇨병 환자는 내인성 인슐린 분비가 거의 없어 외인성 인슐린(basal-bolus 요법의 bolus 성분)이 표준 치료의 필수 구성 요소입니다.

문제는 연관성의 "방향"입니다. 근거 문서의 `repurposing_rationale`은 "이는 인슐린 글루리진의 핵심 약리작용 그 자체(자가면역 파괴로 인한 인슐린 절대 결핍을 외인성 인슐린으로 대체)이며, 노인즈 신호(老藥新用 signal)가 아니라 원 적응증 데이터 결손으로 인한 오분류일 가능성이 크다"고 명시적으로 경고합니다. 즉, 임상시험·문헌 근거는 매우 강력하지만, 이는 "새로운 치료 가설"을 지지하는 근거가 아니라 "이미 확립된 표준 치료"를 재확인하는 근거로 해석하는 것이 타당합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04196231](https://clinicaltrials.gov/study/NCT04196231) | Phase 4 | 완료 | 258 | 인슐린+GLP-1RA 또는 SGLT-2i 병용요법과 basal-bolus 인슐린 요법의 혈당조절 지속성 비교 |
| [NCT01202474](https://clinicaltrials.gov/study/NCT01202474) | Phase 4 | 완료 | 100 | 소아·청소년 제1형 당뇨병에서 Apidra(글루리진)+Lantus basal-bolus 요법의 HbA1c 목표 달성률 평가 |
| [NCT00546702](https://clinicaltrials.gov/study/NCT00546702) | Phase 3 | 완료 | 142 | 제1형 당뇨병 환자 대상 글루리진+글라진 26주 병용요법의 유효성·안전성 평가 |
| [NCT00290979](https://clinicaltrials.gov/study/NCT00290979) | Phase 3 | 완료 | 250 | 제1형 당뇨병에서 글루리진 vs 인슐린 리스프로 28주 비열등성 시험 |
| [NCT00467376](https://clinicaltrials.gov/study/NCT00467376) | Phase 3 | 완료 | 485 | 제1형·제2형 당뇨병에서 글루리진 vs 리스프로(글라진 병용) 효능·저혈당 빈도 비교 |
| [NCT01768559](https://clinicaltrials.gov/study/NCT01768559) | Phase 3 | 완료 | 894 | 릭시세나타이드 vs 글루리진(1일1회/3회) 26주 비교, HbA1c 및 체중 변화 평가 |
| [NCT04974528](https://clinicaltrials.gov/study/NCT04974528) | Phase 3 | 완료 | 319 | 소아 제1형·제2형 당뇨병에서 흡입형 인슐린(Afrezza) vs 속효성 인슐린 유사체(글루리진 포함) 비교 |
| [NCT02685449](https://clinicaltrials.gov/study/NCT02685449) | Phase 4 | 불명 | 70 | 소아 제1형 당뇨병, CSII 사용 시 순단백질 식사 후 인슐린 요구량 교차 연구 |
| [NCT02048189](https://clinicaltrials.gov/study/NCT02048189) | Phase 4 | 중단 | 14 | 지속피하인슐린주입(CSII, Apidra) vs 다회주사 비교, 모집 부족으로 조기 종료 |
| [NCT01087567](https://clinicaltrials.gov/study/NCT01087567) | Phase 4 | 완료 | 23 | 신규 진단 제2형 당뇨병 대상 집중 인슐린요법 예비연구(제1형 특이적 근거로는 관련성 낮음) |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [16308840](https://pubmed.ncbi.nlm.nih.gov/16308840/) | 2005 | RCT | Horm Metab Res | 제1형 당뇨병 683명 무작위 배정, 글루리진 vs 리스프로 효능·안전성 비교 |
| [19496630](https://pubmed.ncbi.nlm.nih.gov/19496630/) | 2009 | Review | Drugs | 인슐린 글루리진의 당뇨병 관리 전반에 대한 종합 리뷰 |
| [23243636](https://pubmed.ncbi.nlm.nih.gov/23243636/) | 2012 | Review | Drugs of Today | 소아·청소년 제1형 당뇨병에서 속효성/지속형 인슐린 유사체 개관(글루리진 포함) |
| [35933650](https://pubmed.ncbi.nlm.nih.gov/35933650/) | 2022 | Cohort | Acta Diabetologica | CSII 펌프 치료 시 글루리진 vs 리스프로/아스파트 코호트 비교, HbA1c·저혈당·DKA 발생률 |
| [28544684](https://pubmed.ncbi.nlm.nih.gov/28544684/) | 2017 | Cohort | Pediatr Int | 소아 제1형 당뇨병 20례, CSII용 글루리진 1년 사용 후 식후 혈당 유의 개선 |
| [16123473](https://pubmed.ncbi.nlm.nih.gov/16123473/) | 2005 | Cohort | Diabetes Care | 소아·청소년 제1형 당뇨병에서 글루리진의 약동학·식후혈당·안전성 평가 |
| [21457066](https://pubmed.ncbi.nlm.nih.gov/21457066/) | 2011 | RCT | Diabetes Technol Ther | 제1형 당뇨병 CSII 사용자 대상 글루리진 vs 아스파트 vs 리스프로 3원 교차 RCT |
| [21291333](https://pubmed.ncbi.nlm.nih.gov/21291333/) | 2011 | RCT | Diabetes Technol Ther | 소아 제1형 당뇨병 26주 시험, 글루리진 vs 리스프로 basal-bolus 요법 비교 |
| [19614947](https://pubmed.ncbi.nlm.nih.gov/19614947/) | 2009 | - | Diabetes Obes Metab | 일본인 제1형 당뇨병 환자 대상 글루리진 vs 리스프로(글라진 병용) 효능·안전성 |
| [18076215](https://pubmed.ncbi.nlm.nih.gov/18076215/) | 2008 | - | Clin Pharmacokinet | 인슐린 글루리진의 임상 약동학·약력학 개관 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (주요 경고, 금기, DDI 모두 데이터 미확보 — DDI 조회 결과 `not_found`)

## 결론 및 다음 단계

**결정: Hold — 데이터 정합성 확인 필요**

**사유:**
- 임상시험(다수의 완료된 Phase 3 RCT 포함)과 문헌 근거 자체는 L1 수준으로 매우 강력하지만, 이는 "제1형 당뇨병에 대한 인슐린의 새로운 치료 가설"이 아니라 **이미 전 세계적으로 확립된 표준 치료(외인성 인슐린 대체요법)를 재확인**하는 근거입니다.
- Evidence Pack의 `repurposing_rationale`이 이 자체를 "老藥新用 신호가 아닌 원 적응증 데이터 결손으로 인한 파이프라인 오분류"로 명시적으로 경고하고 있어, 이 후보를 통상적인 "Proceed with Guardrails" 재창출 후보로 진행하는 것은 부적절합니다.
- 아울러 인슐린 글루리진은 해외에서 이미 널리 시판되는 확립된 제제임에도 한국 허가증이 0건, DDI 조회도 `not_found`로 나타나 지역 규제 데이터 자체가 불완전할 가능성이 있습니다.

**진행하려면 필요한 것:**
- `drug.original_indications` 필드의 실제 원 적응증 데이터 보완 (DrugBank/TFDA 라벨 조회) → 이 후보가 진짜 신규 적응증인지, 원 적응증 재탐지인지 확정
- DG001(허가사항 경고/금기) 및 DG002(MOA) 데이터 갭 해소
- 한국 내 인슐린 글루리진 실제 허가·유통 현황 재확인 (0건 표시가 실제 미허가인지 데이터 누락인지 검증)
- 위 확인 후에도 순위 2~10위(예: TRMA 증후군, opsismodysplasia 등)는 근거 수준 L5(모델 예측만 존재)로 별도 검증 전까지 진행 보류 유지 권장
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

