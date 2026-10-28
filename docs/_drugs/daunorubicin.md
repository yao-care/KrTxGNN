---
layout: default
title: Daunorubicin
parent: 모델 예측만 (L5)
nav_order: 254
evidence_level: L5
indication_count: 10
monitor_inn: "Daunorubicin"
predicted_indications: ["Hodgkins lymphoma", "vertebral anomalies and variable endocrine and T-cell dysfunction", "ganglioneuroblastoma (disease)", "neuroblastoma", "ALK-positive large B-cell lymphoma", "adenosarcoma", "retroperitoneal neoplasm", "small cell lung carcinoma", "primary pulmonary lymphoma", "pulmonary blastoma"]
last_modified_at: 2026-10-28
description: "Daunorubicin: 예측 신규 적응증 호지킨 림프종 (근거 수준 L5). 기존 적응증: 허가 적응증 본문을 확인할 수 없음 (허가증에는 식약처 문서 링크만 수록)"
---

# Daunorubicin
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

## Daunorubicin: 허가 적응증 정보 확인 불가 상태에서 호지킨 림프종으로
{: .text-alpha }

## 한 문장 요약

Daunorubicin은 안트라사이클린 계열의 항암제로, 한국에서 단일 성분 주사제 3건의 허가증이 확인됩니다. 다만 허가 적응증 본문은 이번 자료에 담기지 않았습니다.
TxGNN 모델은 **호지킨 림프종(Hodgkin's lymphoma)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 다룬 임상시험이나 문헌은 확인되지 않았습니다. 현재 근거는 모델 예측 수준입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문을 확인할 수 없음 (허가증에는 식약처 문서 링크만 수록) |
| 예측 신규 적응증 | 호지킨 림프종 |
| TxGNN 예측 점수 | 0.9981 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 3건 (단일 성분 3건, 모두 유효) |
| 권장 결정 | Hold |

근거 수준을 L5로 판정한 이유는 다음과 같습니다. 호지킨 림프종 항목의 임상시험 2건은 비호지킨 림프종 또는 급성 B림프모구성 백혈병을 다룹니다. 문헌 중 호지킨 림프종을 언급한 자료는 안트라사이클린 전반을 다룬 리뷰와 혈액종양 총설이며, daunorubicin의 호지킨 림프종 효능을 직접 연구한 자료는 없습니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 daunorubicin은 DNA에 삽입(intercalation)되고 topoisomerase II를 억제하는 안트라사이클린으로 알려져 있습니다. 이 기전은 호지킨 림프종의 표준 요법인 ABVD에 포함된 doxorubicin과 같은 계열의 것입니다.

따라서 기전상 호지킨 림프종에 적용될 가능성은 있습니다. 그러나 이는 계열 수준의 추론입니다. 제공된 임상시험과 문헌에서 daunorubicin 자체의 호지킨 림프종 효능은 확인되지 않았습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00002471](https://clinicaltrials.gov/study/NCT00002471) | Phase 2 | 완료 | 정보 없음 | 고위험 비림프모구성 림프종 및 급성 B림프모구성 백혈병, 재발성 비호지킨 림프종에 대한 집중 단기 병용화학요법 시험. 호지킨 림프종 대상 여부와 daunorubicin의 역할은 확인 불가 |
| [NCT00002691](https://clinicaltrials.gov/study/NCT00002691) | Phase 2 | 완료 | 정보 없음 | 소아·청소년 진행성 비호지킨 림프종 LSA5 프로토콜. 호지킨 림프종과 다른 질환이라 간접 근거에 그침 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [30231396](https://pubmed.ncbi.nlm.nih.gov/30231396/) | 2018 | Review | ASCO Educational Book | 안트라사이클린(daunorubicin 포함)이 소아 호지킨 림프종 등의 요법의 근간이며, 심장독성이 임상 사용의 제약이라는 내용 |
| [14584273](https://pubmed.ncbi.nlm.nih.gov/14584273/) | 2003 | 총설 | Gan to Kagaku Ryoho | 진행성 호지킨 림프종의 1차 요법은 ABVD라는 내용. daunorubicin 자체의 효능 자료는 아님 |
| [10410671](https://pubmed.ncbi.nlm.nih.gov/10410671/) | 1999 | 총설 | Gan to Kagaku Ryoho | 혈액종양 치료 개요. 진행성 호지킨 림프종 표준요법 언급 |
| [17610809](https://pubmed.ncbi.nlm.nih.gov/17610809/) | 2007 | 체계적 문헌고찰 | Health Technol Assess | 소아 암 환자의 안트라사이클린 심장독성에 대한 심장보호 방법 평가 |
| [9387047](https://pubmed.ncbi.nlm.nih.gov/9387047/) | 1997 | 임상시험 | Invest New Drugs | 재발·불응성 림프종 19명에 리포좀 daunorubicin 투여. 고용량군에서 완전반응 1명, 부분반응 일부 관찰 (비호지킨 림프종 중심) |
| [11699226](https://pubmed.ncbi.nlm.nih.gov/11699226/) | 2001 | 임상시험 | Leuk Lymphoma | 예후 불량 비호지킨 림프종에서 리포좀 daunorubicin 병용요법(COP-X) 시행. 평가 가능 32명 중 81% 반응 |

위 문헌은 대부분 비호지킨 림프종이나 안트라사이클린 일반을 다룹니다. 호지킨 림프종에서 daunorubicin 효능을 직접 입증한 문헌은 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202400632 | 다우노신주20밀리그램(다우노루비신염산염) | 동결건조분말 주사제 (첨부용제 포함) | 적응증 본문 확인 불가 (식약처 문서 링크만 수록) |
| 201309135 | 주사용다우노마이신20밀리그램(다우노루비신염산염)(수출용) | 바이알 (결정 또는 가루) | 적응증 본문 확인 불가 (식약처 문서 링크만 수록) |
| 199801567 | 다우노신주(다우노루비신염산염)(수출용) | 동결건조분말 바이알 (첨부용제 포함) | 적응증 본문 확인 불가 (식약처 문서 링크만 수록) |

허가증 3건은 모두 단일 성분이며 유효 상태입니다. 이 중 2건은 수출용입니다. 시판 현황은 취소 여부 정보가 없어 확인할 수 없습니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (안트라사이클린 계열) |
| 골수억제 위험 | 고 (일반적으로 안트라사이클린 계열의 주요 독성) |
| 구토 유발성 등급 | 중 |
| 모니터링 항목 | CBC (분류 포함), 간·신기능, 심기능 (누적 용량에 따른 심장독성) |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

허가사항의 경고 및 주의사항을 참조하세요. 위 내용은 약물 계열의 일반 지식에 근거하며, 이번 자료에는 독성 데이터가 포함되어 있지 않습니다.

## 안전성 고려사항

**약물 상호작용**: 상호작용 100건이 조회되었으며, 아래는 일부입니다.
- **Major**: Cisapride, Dolasetron, Papaverine, Deferiprone, Macimorelin
- **Moderate**: Famotidine, Loperamide, Clarithromycin, Ondansetron, Granisetron, Palonosetron, Levofloxacin, Eliglustat, Rolapitant, Palifermin 등
- **Minor**: Metronidazole

주요 경고와 금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
호지킨 림프종에 대한 TxGNN 점수는 높지만, daunorubicin의 호지킨 림프종 효능을 직접 연구한 임상시험이나 문헌이 없어 근거가 모델 예측 수준(L5)에 머뭅니다. 허가 적응증과 안전성 정보도 확인되지 않은 상태입니다.

**진행하려면 필요한 것:**
- 식약처 허가사항(첨부문서)에서 허가 적응증, 경고, 금기 확보
- 작용 기전 데이터 확보 (DrugBank 등)
- 호지킨 림프종에서 daunorubicin을 직접 평가한 임상시험 또는 문헌 탐색
- NCT00002471의 대상 집단과 daunorubicin 포함 여부 확인
- 한국 시판 및 허가 유지 여부 확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

