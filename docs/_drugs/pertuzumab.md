---
layout: default
title: Pertuzumab
parent: 僅模型預測 (L5)
nav_order: 546
evidence_level: L5
indication_count: 10
---

# Pertuzumab
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

# Pertuzumab: HER2 양성 유방암에서 Normal-like 유방암 아형으로

## 한 문장 요약

Pertuzumab은 HER2(인간 표피성장인자 수용체 2)를 표적하는 단클론항체로, 국제적으로 HER2 양성 유방암 치료에 널리 사용되어 왔습니다. TxGNN 모델은 **Normal-like 유방암 아형(normal breast-like subtype of breast carcinoma)**에 효과가 있을 수 있다고 예측하지만, 이 아형은 통상 HER2 발현이 낮아 기전상 불일치 가능성이 제기됩니다. 현재 **6건의 임상시험**이 확인되었으나 문헌 근거는 없으며, 제시된 시험들 대부분이 실제로는 HER2 양성 환자를 대상으로 한 것이어서 질병 라벨과 시험 수집 기준 간 매핑 오류 가능성을 인공 검토해야 합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | HER2 양성 유방암 (한국 정식 허가 정보 없음) |
| 예측 신규 적응증 | Normal-like 유방암 아형 (Normal Breast-like Subtype of Breast Carcinoma) |
| TxGNN 예측 점수 | 99.93% |
| 근거 수준 | L3 |
| 한국 시판 현황 | 미상시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, Pertuzumab은 HER2 표적 단클론항체 계열의 약물이며, HER2-HER3 이형이합체화(heterodimerization)를 차단하여 HER2 신호전달을 억제하는 방식으로 작용합니다. 이 기전은 다수의 임상시험에서 HER2 양성 유방암 치료제로 확립되어 있습니다.

다만 Normal-like 유방암 아형은 분자아형 분류상 대체로 HER2 발현이 낮은 것으로 알려져 있어, Pertuzumab의 HER2 표적 기전과 직접적으로 부합하지 않을 가능성이 있습니다. 실제로 아래 제시된 임상시험들은 모두 "HER2 양성 유방암"을 수집 기준으로 삼고 있어, TxGNN이 예측한 질병 라벨(normal-like subtype)과 시험 수집단 사이에 온톨로지(ontology) 매핑 오류가 존재할 가능성이 있습니다. 이 점은 임상적 타당성을 판단하기 전 반드시 인공 검토가 필요한 부분입니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01796197](https://clinicaltrials.gov/study/NCT01796197) | Phase 2 | 완료 | 23 | 염증성 유방암 술전요법으로 Paclitaxel+Trastuzumab+Pertuzumab 평가. HER2 양성 환자 대상으로, normal-like 아형과 불일치 가능성 있음(등급 C) |
| [NCT04329065](https://clinicaltrials.gov/study/NCT04329065) | Phase 2 | 모집 중 | 25 | WOKVAC 백신을 항HER2 표적치료 및 항암화학요법과 병용한 술전 면역반응·안전성 연구 |
| [NCT06348134](https://clinicaltrials.gov/study/NCT06348134) | Phase 2 | 모집 중 | 74 | 나이지리아 HER2 양성 유방암 여성 대상 술전-술후 항HER2 치료 효능·안전성 평가 |
| [NCT04750122](https://clinicaltrials.gov/study/NCT04750122) | Phase 1/2 | 모집 중 | 46 | 환자유래 종양세포 클러스터 기반 시험관내 약물 스크리닝을 활용한 HER2 양성 조기유방암 술전요법 |
| [NCT05900206](https://clinicaltrials.gov/study/NCT05900206) | Phase 2 | 모집 중 | 370 | ARIADNE 시험: Trastuzumab deruxtecan(T-DXd) vs 표준 술전요법 비교, 비전이성 HER2 양성 유방암 대상. HER2 표적 시험으로 normal-like 아형 특이적 수집 기준 아님(등급 C) |
| [NCT05582499](https://clinicaltrials.gov/study/NCT05582499) | Phase 2 | 모집 중 | 716 | FASCINATE-N: 정밀 술전요법 플랫폼 연구, 임상 아형 기반이나 이 분자아형에 특이적 수집 기준 미확인(등급 C) |

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

한국에는 현재 허가된 Pertuzumab 제품이 없습니다 (미상시판, 허가증 0건).

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (HER2 단클론항체, 전통적 세포독성 화학요법제 아님) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측된 적응증(Normal-like 유방암 아형)은 통상 HER2 발현이 낮은 분자아형으로, Pertuzumab의 HER2 표적 기전과 불일치할 가능성이 있습니다. 제시된 임상시험 6건 모두 실제로는 HER2 양성 환자를 수집 기준으로 삼고 있어, TxGNN 질병 라벨과 시험 대상군 간 온톨로지 매핑 오류가 의심됩니다. 관련 문헌 근거도 전무하여 근거 수준(L3)에 비해 실질적 신뢰도는 낮습니다.

**진행하려면 필요한 것:**
- Normal-like 아형의 정의 및 HER2 발현 상태에 대한 재검증
- TxGNN 질병 라벨과 임상시험 수집 기준 간 온톨로지 매핑 검증(인공 리뷰)
- Pertuzumab의 MOA 및 MFDS 안전성 자료(경고/금기/DDI) 확보 — DG001(허가사항), DG002(작용기전) 해결 필요
- 한국 내 허가·유통 현황 재확인

> 참고: 동일 Evidence Pack 내 **progesterone-receptor positive/negative breast cancer** (rank 2, 3)는 각각 다수의 완료된 Phase 3 RCT(예: NCT04629846, NCT03726879, NCT01120184)와 관련 문헌을 보유하여 근거 수준 L1로 평가되며, HER2 표적 기전과의 부합도도 높습니다. 이 적응증들이 더 실행 가능성 높은 대안 후보로 판단됩니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

