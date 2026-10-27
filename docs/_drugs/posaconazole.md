---
layout: default
title: Posaconazole
parent: 모델 예측만 (L5)
nav_order: 615
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Posaconazole: 예측 신규 적응증 폐포자충증 (Pneumocystosis) (근거 수준 L5). 기존 적응증: 허가 적응증 원문이 링크 형태로만 제공되어 구체적인 적응증 텍스트는 확인할 수 없음 (허가사항 참조)"
monitor_inn: "posaconazole"
predicted_indications: ["pneumocystosis"]
---

# Posaconazole
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **1** 건
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

## Posaconazole: 침습성 진균 감염에서 폐포자충증(Pneumocystosis)으로
{: .text-alpha }

## 한 문장 요약

Posaconazole은 트리아졸계 항진균제로, 한국에서 현탁액과 장용정으로 허가되어 시판 중입니다.
TxGNN 모델은 **폐포자충증(Pneumocystosis)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 검증한 임상시험은 없고 **관련 임상시험 1건**(간접적)과 **문헌 5편**(대부분 가이드라인·리뷰)만 있어 근거는 약합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 원문이 링크 형태로만 제공되어 구체적인 적응증 텍스트는 확인할 수 없음 (허가사항 참조) |
| 예측 신규 적응증 | 폐포자충증 (Pneumocystosis) |
| TxGNN 예측 점수 | 99.77% |
| 근거 수준 | L4 (전임상·기전 수준의 간접 근거만 있음. 모델 예측 외 직접 연구는 없음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 허가사항 기준의 상세한 작용 기전 데이터가 없습니다. 일반적으로 posaconazole은 진균의 lanosterol 14-alpha-demethylase(CYP51)를 억제하여 ergosterol 합성을 차단하는 트리아졸계 항진균제입니다. 혈액암 환자 등 고위험군에서 곰팡이에 활성이 있는 예방 요법으로 사용되어 침습성 칸디다증과 아스페르길루스증을 크게 줄인 것으로 보고되어 있습니다.

그러나 이 기전은 폐포자충증에는 잘 맞지 않습니다. *Pneumocystis jirovecii*는 세포막에 ergosterol이 거의 없고 cholesterol 등 다른 스테롤을 사용하기 때문에, 기존 아졸계의 작용 방식으로는 효과를 기대하기 어렵습니다. TxGNN의 높은 점수는 다른 항진균제 및 진균성 폐 감염과의 네트워크 근접성을 반영한 것일 가능성이 크며, 실제 기전적 적합성을 의미한다고 보기 어렵습니다.

Posaconazole은 폐 상피 내벽액(ELF)으로 이행되는 것으로 보고되어 폐 조직에 노출될 수는 있습니다. 하지만 이는 일반적인 폐 노출을 뒷받침할 뿐, *Pneumocystis*에 대한 활성을 입증하지는 않습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | 완료 | 602 | 동종 조혈모세포이식 성인에서 rezafungin과 표준 항균 요법의 침습성 진균 질환 예방 효과 비교 (ReSPECT 연구) |

이 시험은 rezafungin을 평가한 것으로 posaconazole 자체의 폐포자충증 효능 자료는 얻을 수 없습니다. 관련성은 낮음(C등급)으로 평가되며, 이 적응증의 근거 수준을 높이는 데 사용할 수 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Review | Swiss Med Wkly | 칸디다증, 아스페르길루스증, 크립토코쿠스증, 폐포자충 폐렴 개관. 곰팡이 활성이 있는 posaconazole 예방이 고위험 혈액종양 환자의 침습성 진균 감염을 줄임 |
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2026 | Guideline | Lancet Infect Dis | 영국 의료진균학회의 중증 진균 질환 진단 모범 권고 2025 개정판 |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Guideline | Zhonghua Jie He He Hu Xi Za Zhi | 중국흉부학회의 침습성 폐 진균 질환 진단·치료 지침 2025년판 |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review | Clin Pharmacokinet | 항진균제 등의 폐 상피 내벽액 침투 평가 |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Cohort | Transpl Infect Dis | 간이식 후 급성 GVHD 환자의 감염 합병증 후향 분석 |

이 문헌들은 진균 감염 전반 또는 약동학을 다루며, posaconazole의 폐포자충증 치료 효능을 직접 입증한 연구는 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200711475 | 녹사필현탁액(포사코나졸(미분화)) | 현탁액 | 허가사항 참조 (적응증 원문 미확인) |
| 201502727 | 녹사필장용정100밀리그램(포사코나졸(미분화)) | 장용성 필름코팅정 | 허가사항 참조 (적응증 원문 미확인) |

두 제품 모두 한국엠에스디(주)가 허가를 보유하고 있으며 유효 상태입니다.

## 안전성 고려사항

- **약물 상호작용**: 총 269건이 보고되었습니다. 이 중 주요(Major) 상호작용은 다음과 같습니다.
  - Loperamide
  - Triamcinolone
  - Budesonide
- 중등도(Moderate) 상호작용에는 다음이 포함됩니다.
  - 위산억제제: famotidine, ranitidine, cimetidine, omeprazole, rabeprazole
  - 스테로이드: hydrocortisone, dexamethasone, betamethasone
  - 기타: aprepitant, clarithromycin, saxagliptin, bisacodyl

경고 및 금기 등 그 외 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
폐포자충증에 대한 직접적인 임상시험이나 문헌 근거가 없고, *Pneumocystis*에 ergosterol이 거의 없어 azole계 기전이 적용되기 어렵습니다. 높은 TxGNN 점수는 모델 예측일 뿐이므로 현재로서는 진행을 보류하는 것이 타당합니다.

**진행하려면 필요한 것:**
- 허가사항(경고, 금기, 적응증)의 확보 및 분석: 현재 안전성 선별을 진행할 수 없는 상태
- posaconazole의 상세 작용 기전 데이터 확인(DrugBank 등)
- *Pneumocystis*에 대한 전임상(in vitro·동물) 활성 자료 확보
- posaconazole을 직접 평가한 폐포자충증 임상시험 또는 증례 연구 탐색
- 기존 표준 치료(예: TMP-SMX)와 비교했을 때 posaconazole을 사용할 임상적 타당성 검토
- 다수의 주요 약물 상호작용을 고려한 병용약 관리 계획 수립
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

