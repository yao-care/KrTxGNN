---
layout: default
title: Daunorubicin
parent: 모델 예측만 (L5)
nav_order: 254
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Daunorubicin: 예측 신규 적응증 급성 림프모구성/림프구성 백혈병 (Acute Lymphoblastic/Lymphocytic Leukemia) (근거 수준 L5). 기존 적응증: 허가증에 적응증 원문이 제공되지 않아 확인할 수 없음 (허가사항 PDF 참조)"
monitor_inn: "Daunorubicin"
predicted_indications: ["Hodgkins lymphoma", "vertebral anomalies and variable endocrine and T-cell dysfunction", "ganglioneuroblastoma (disease)", "neuroblastoma", "ALK-positive large B-cell lymphoma", "adenosarcoma", "retroperitoneal neoplasm", "small cell lung carcinoma", "primary pulmonary lymphoma"]
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

<div id="pharmacist">

## 약사 평가 보고서

</div>

# Daunorubicin: 원발성 급성 백혈병 치료제에서 급성 림프모구성 백혈병으로

## 한 문장 요약

Daunorubicin은 안트라사이클린 계열의 항종양제로, 한국에서 주사제로 허가되어 시판 중입니다.
TxGNN 모델은 **급성 림프모구성/림프구성 백혈병(Acute Lymphoblastic Leukemia)**에 효과가 있을 수 있다고 예측하며, 현재 **27건의 임상시험**이 이 방향을 지지합니다. 다만 이 예측은 이미 임상에서 확립된 사용과 일치하므로 새로운 재창출 신호라기보다 기존 진료의 재확인에 가깝습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에 적응증 원문이 제공되지 않아 확인할 수 없음 (허가사항 PDF 참조) |
| 예측 신규 적응증 | 급성 림프모구성/림프구성 백혈병 (Acute Lymphoblastic/Lymphocytic Leukemia) |
| TxGNN 예측 점수 | 99.82% |
| 근거 수준 | L1 (완료된 Phase 3 RCT가 2건 이상: NCT00005596, NCT00002744, NCT00557193) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 3건 |
| 권장 결정 | Proceed with Guardrails |

참고로 L1 판정은 수집된 시험의 등록 정보에 근거한 것이며, 위 Phase 3 시험들은 대부분 다른 약제나 용법을 비교한 시험이라 daunorubicin 단독 효과를 직접 입증하지는 않습니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 수집되지 않았습니다. 다만 daunorubicin은 안트라사이클린 계열로, DNA에 끼어들고(intercalation) topoisomerase II를 억제하여 DNA 손상과 세포자멸사를 일으키는 것으로 알려져 있습니다. 이 기전은 빠르게 분열하는 림프모구에 잘 적용됩니다.

급성 림프모구성 백혈병(ALL)의 유도요법에서 daunorubicin은 hyper-CVAD, BFM, MRC UKALL/ECOG 등 표준 병용요법의 구성 성분입니다. 즉 이 예측은 새로운 용도의 발굴이라기보다 이미 확립된 임상 사용을 모델이 재현한 결과로 해석됩니다.

## 임상시험 근거

완료된 시험과 관련성이 높은 시험을 우선하여 정리했습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00390793](https://clinicaltrials.gov/study/NCT00390793) | Phase 2 | 완료 | 107 | Ph 양성 ALL에서 hyper-CVAD + dasatinib 병용 |
| [NCT00184041](https://clinicaltrials.gov/study/NCT00184041) | Phase 2 | 완료 | 47 | 성인 ALL에서 PEG-asparaginase 포함 관해 후 강화요법 |
| [NCT00199056](https://clinicaltrials.gov/study/NCT00199056) | Phase 4 | 완료 | 225 | 성인 ALL 다기관 강화 유도·공고요법 |
| [NCT00131027](https://clinicaltrials.gov/study/NCT00131027) | Phase 3 | 불명 | 240 | BCR-ABL 음성 ALL에서 고용량 methotrexate 공고요법 (daunorubicin은 간접 근거) |
| [NCT00005596](https://clinicaltrials.gov/study/NCT00005596) | Phase 3 | 완료 | 1076 | 소아 표준위험 ALL에서 4가지 병용 화학요법 비교 |
| [NCT00002744](https://clinicaltrials.gov/study/NCT00002744) | Phase 3 | 완료 | 1970 | 소아 표준위험 ALL에서 mercaptopurine vs thioguanine 및 IT 요법 비교 |
| [NCT00557193](https://clinicaltrials.gov/study/NCT00557193) | Phase 3 | 완료 | 218 | 영아 ALL에서 강화 화학요법 ± lestaurtinib |
| [NCT02003222](https://clinicaltrials.gov/study/NCT02003222) | Phase 3 | 활성, 모집 종료 | 488 | BCR-ABL 음성 B계열 ALL에서 blinatumomab 추가 |
| [NCT03643276](https://clinicaltrials.gov/study/NCT03643276) | Phase 3 | 모집 중 | 5000 | 소아·청소년 ALL 국제 협력 프로토콜 (AIEOP-BFM ALL 2017) |
| [NCT02660762](https://clinicaltrials.gov/study/NCT02660762) | Phase 2 | 불명 | 100 | 젊은 성인 저위험 Ph 음성 ALL에서 수정 MRC UKALL XII/ECOG E2993 요법 |

대부분의 시험에서 daunorubicin은 병용요법의 일부이며, 시험이 평가하는 핵심 질문은 병용된 다른 약제입니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202400632 | 다우노신주20밀리그램(다우노루비신염산염) | 동결건조분말 주사제 (첨부용제 포함) | 허가사항 PDF 참조 |
| 201309135 | 주사용다우노마이신20밀리그램(다우노루비신염산염)(수출용) | 결정 또는 가루가 든 바이알 | 허가사항 PDF 참조 |
| 199801567 | 다우노신주(다우노루비신염산염)(수출용) | 동결건조분말 바이알 (첨부용제 포함) | 허가사항 PDF 참조 |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (안트라사이클린 계열) |
| 골수억제 위험 | 고 (안트라사이클린 계열의 일반적 특성) |
| 구토 유발성 등급 | 중등도 |
| 모니터링 항목 | CBC (분류 포함), 간기능, 신기능, 심기능 (누적 용량에 따른 심독성 평가) |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

위 내용은 약물 계열의 일반적 특성에 근거한 것이며, 상세한 사항은 허가사항의 경고 및 주의사항을 참조하세요.

## 안전성 고려사항

- **약물 상호작용**: 수집된 상호작용은 총 100건입니다. 이 중 주요(Major) 등급은 다음과 같습니다.
  - Cisapride
  - Dolasetron
  - Papaverine
  - Deferiprone
  - Macimorelin
- 중등도(Moderate) 등급에는 famotidine, loperamide, clarithromycin, levofloxacin, ondansetron, granisetron, palonosetron 등이 포함됩니다.
- 안트라사이클린의 누적 용량에 따른 심독성이 주요 우려사항이며, 병용 약물의 부담도 고려해야 합니다.

경고 및 금기 항목은 허가사항을 참조하세요.

## 기타 예측 적응증 요약

| 순위 | 예측 질환 | 점수 | 근거 수준 | 비고 |
|------|---------|------|----------|------|
| 2 | 호지킨 림프종 | 99.81% | L3 | 표준요법(ABVD)은 doxorubicin 사용, daunorubicin 직접 근거 약함 |
| 4 | 신경절신경모세포종 | 99.80% | L5 | 임상시험·문헌 없음 |
| 5 | 신경모세포종 | 99.78% | L4 | 전임상 및 오래된 소규모 연구 위주 |
| 9 | 소세포폐암 | 99.76% | L3 | 주로 세포주 연구, 임상시험은 daunorubicin 특이적이지 않음 |

3위(척추 이상 및 내분비·T세포 기능 이상 증후군), 7위(선육종), 10위(원발성 폐 림프종) 등 나머지 예측은 근거가 없거나 매우 빈약하며, 3위는 지식그래프 산물일 가능성이 높습니다.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
급성 림프모구성 백혈병은 daunorubicin 포함 병용요법이 널리 사용되는 확립된 영역이며, 다수의 완료된 Phase 2~4 시험이 이를 뒷받침합니다. 다만 심독성과 높은 상호작용 부담 때문에 안전장치가 필요합니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기·적응증)의 확인: 허가증 PDF에서 내용을 확보해야 합니다.
- 작용 기전 데이터의 보완
- 누적 용량 기반의 심기능 모니터링 계획
- 주요 상호작용 약물(특히 QT 연장 관련 약물)의 병용 관리 방안
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

