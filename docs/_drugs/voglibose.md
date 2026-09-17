---
layout: default
title: Voglibose
parent: 모델 예측만 (L5)
nav_order: 725
evidence_level: L5
indication_count: 10
---

# Voglibose
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

# Voglibose: 제2형 당뇨병에서 제1형 당뇨병(인슐린 병용요법)으로

## 한 문장 요약

Voglibose는 α-glucosidase 억제제 계열 약물로, 장내 탄수화물 분해를 지연시켜 식후 혈당 상승을 억제하는 목적으로 사용되어 왔습니다(제2형 당뇨병/내당능장애, 문헌 근거 기반). TxGNN 모델은 **제1형 당뇨병(Insulin-Dependent Diabetes Mellitus, IDDM)**의 인슐린 병용요법 보조제로서 효과가 있을 수 있다고 예측하며, 현재 **8건의 관련 임상시험**과 **4편의 문헌**(그중 IDDM 환자 대상 소규모 임상연구 1건 포함)이 이 방향을 뒷받침합니다.

> **참고**: TxGNN이 가장 높은 원점수로 예측한 적응증은 "두피 다모증(hypotrichosis simplex of the scalp)"이었으나, 근거 자료가 전혀 없고 Evidence Pack 자체의 기전 분석에서도 "모델 임베딩 공간의 위상적 유사성에 따른 노이즈"로 판정되어(L5/S0/Hold) 이 보고서에서는 제외했습니다. 대신 실제 임상시험·문헌 근거가 확인된 2순위 예측(제1형 당뇨병, L3/S2)을 중심으로 평가합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 제2형 당뇨병 / 내당능장애 (α-glucosidase 억제제, 공식 허가 라벨 데이터 없음 — 문헌 근거 기반 추정) |
| 예측 신규 적응증 | 제1형 당뇨병(IDDM) — 인슐린 병용요법 보조 |
| TxGNN 예측 점수 | 99.80% (rank 4509) |
| 근거 수준 | L3 (관찰 연구/문헌 리뷰) |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

공식 DrugBank MOA 필드는 데이터 공백(Data Gap, DG002) 상태이지만, 수집된 임상시험·문헌 자료를 종합하면 Voglibose는 **α-glucosidase 억제제**로서 소장에서 이당류를 단당류로 분해하는 효소를 억제해 탄수화물 흡수 속도를 늦추고 식후 혈당 급상승을 완화하는 기전을 가진 것으로 확인됩니다.

이 기전은 제2형 당뇨병(인슐린 저항성)과 제1형 당뇨병(자가면역성 베타세포 파괴)이라는 서로 다른 병태생리를 가진 두 질환 사이에서, **질병의 근본 원인을 치료하는 것이 아니라 대사적 보조 역할**로 연결됩니다. 즉 Voglibose는 IDDM 환자의 자가면역 병리를 치료할 수는 없지만, 강화 인슐린요법을 받는 환자에서 식후·야간 혈당 변동폭을 줄이는 보조제로 작용할 수 있다는 것이 이 예측의 핵심 근거입니다.

실제로 문헌 근거(PMID 10778865)는 저녁 식전 Voglibose 투여가 강화 인슐린요법 중인 IDDM 환자의 야간 저혈당을 개선했다고 보고하고 있어, 기전상 타당성이 실제 임상 관찰로 일부 뒷받침됩니다. 다만 해당 연구는 10명 규모의 소규모 연구이며, 제1형 당뇨병을 전용 목표로 설계된 대규모 임상시험은 아직 없습니다.

---

## 임상시험 근거

수집된 임상시험은 모두 제2형 당뇨병 환자 대상이며, 제1형 당뇨병을 전용 목표로 한 시험은 없습니다. 아래는 Voglibose의 기전·약동학·안전성을 뒷받침하는 배경 근거로서 제시합니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00970528](https://clinicaltrials.gov/study/NCT00970528) | Phase 4 | 완료 | 124 | 인슐린 글라진 단독/메트포르민 병용 T2DM 환자에서 Acarbose vs Voglibose 효능·안전성 비교 |
| [NCT02049814](https://clinicaltrials.gov/study/NCT02049814) | Phase 4 | 완료 | 494 | 메트포르민 병용 T2DM에서 Voglibose vs Acarbose HbA1c 비열등성 평가 |
| [NCT01993927](https://clinicaltrials.gov/study/NCT01993927) | N/A (시판후조사) | 완료 | 742 | Voglibose 장기 투여 시판후 감시 연구(내당능장애→T2DM 진행 예방) |
| [NCT01309698](https://clinicaltrials.gov/study/NCT01309698) | Phase 4 | 완료 | 24 | Voglibose와 Vildagliptin 병용 시 정상상태 약동학/약력학 평가 |
| [NCT02287402](https://clinicaltrials.gov/study/NCT02287402) | Phase 4 | 완료 | 197 | AO-128(Voglibose 개발코드) 시판후 연구, 내당능장애 환자 대상 |
| [NCT00837577](https://clinicaltrials.gov/study/NCT00837577) | Phase 3 | 완료 | 133 | Voglibose 단독요법에 Sitagliptin 추가 시 효능·안전성(일본 T2DM) |
| [NCT01055652](https://clinicaltrials.gov/study/NCT01055652) | Phase 1 | 완료 | 28 | Voglibose 병용 시 Dapagliflozin 약동학 상호작용 평가(일본 T2DM) |
| [NCT00368134](https://clinicaltrials.gov/study/NCT00368134) | Phase 3 | 완료 | 370 | Vildagliptin vs Voglibose 12주 이중맹검 비교 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [10778865](https://pubmed.ncbi.nlm.nih.gov/10778865/) | 2000 | Cohort/Clinical Study | Metabolism: Clinical and Experimental | 강화 인슐린요법 중인 IDDM 환자 10명 대상, 저녁 식전 Voglibose 0.3mg 투여로 야간 저혈당 개선 |
| [12387032](https://pubmed.ncbi.nlm.nih.gov/12387032/) | 2002 | Review | Nihon Rinsho (일본 임상의학) | 인슐린과 α-glucosidase 억제제 병용요법에 대한 리뷰 |
| [39723258](https://pubmed.ncbi.nlm.nih.gov/39723258/) | 2024 | Review | Frontiers in Pharmacology | 당뇨병 치료제가 치과 임플란트 성공률에 미치는 영향 종합 리뷰(T1DM/T2DM 모두 포함, 간접 참고) |
| [9778959](https://pubmed.ncbi.nlm.nih.gov/9778959/) | 1998 | Case Report | Nihon Ronen Igakkai Zasshi | 류마티스관절염·하시모토병 동반 고령 서서히 진행하는 IDDM(SPIDDM) 증례 보고 (배경 자료, Voglibose 직접 언급 없음) |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (한국 규제기관 라벨/경고 데이터는 현재 확보되지 않았습니다 — DG001, Blocking 등급)

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
IDDM 환자에서 야간 저혈당 개선 효과를 시사하는 소규모 임상 관찰(n=10)이 존재하고 기전상 타당성도 있으나, 제1형 당뇨병을 전용 목표로 설계된 임상시험이 전무하며(L3, Research Question 단계) 한국 내 시판 이력과 허가 라벨/안전성 데이터(DG001, Blocking)가 없어 즉시 진행 가능한 근거 수준에 미치지 못합니다.

**진행하려면 필요한 것:**
- 제1형 당뇨병 환자를 직접 대상으로 한 전용 임상시험(RCT) 설계 및 실행
- 규제기관 공식 허가사항(경고, 금기, 약물상호작용) 확보 — TFDA/MFDS 원문 라벨 조회 필요 (DG001 해소)
- DrugBank API를 통한 공식 MOA 데이터 확보 (DG002 해소)
- 한국 내 시판 여부 및 도입 가능성 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

