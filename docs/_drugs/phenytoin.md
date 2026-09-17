---
layout: default
title: Phenytoin
parent: 높은 근거 (L1-L2)
nav_order: 551
evidence_level: L2
indication_count: 10
---

# Phenytoin
{: .fs-9 }

근거 수준: **L2** | 예측 적응증: **10** 건
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

# Phenytoin: 뇌전증에서 삼차신경통(Trigeminal Neuralgia)으로

> **분석 방법론 노트**: TxGNN 원본 점수 기준 1위 후보는 "trigeminal nerve neoplasm(삼차신경 종양)"이지만, 근거 팩 자체의 문헌 분류가 "문자 매칭 오류로 추정, phenytoin에 항종양 기전 없음"이라 명시하고 있습니다. 이에 본 보고서는 **10개 예측 후보 중 실제 임상 근거(전향적 연구 1건 + 문헌 20편)가 뒷받침되는 삼차신경통(원 순위 9위)을 주 후보로** 다루고, 나머지 9개 후보는 비교표와 요약으로 함께 제시합니다.

## 한 문장 요약

Phenytoin(페니토인)은 전압-의존성 나트륨 채널을 차단하는 대표적 항경련제로, 원래 뇌전증(간질) 발작의 치료·예방에 사용되어 왔습니다. TxGNN 모델이 제시한 10개 신규 적응증 후보 중 **삼차신경통(Trigeminal Neuralgia)**이 완료된 전향적 임상연구 1건, 다기관 후향적 연구(144례), 유럽신경학회 가이드라인 등 **20편의 문헌**으로 가장 강하게 뒷받침되며, 실제로 급성 발작 시 정맥주사 rescue 치료제로 이미 임상 현장에서 사용되고 있습니다. 나머지 후보들(놀람유발발작, 음향유발발작 등 희귀 반사성 뇌전증군)은 대부분 동물모델·개별 사례 수준에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 뇌전증(간질) 발작 치료 및 예방 *(공식 허가 데이터 없음, 문헌 기반 확인)* |
| 예측 신규 적응증 | 삼차신경통 (Trigeminal Neuralgia) |
| TxGNN 예측 점수 | 99.97% (원본 순위 1163위 / 보고서 내 10개 후보 중 9위) |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

Phenytoin은 hydantoin계 항경련제로 전압-의존성 나트륨 채널을 억제하여 신경세포의 과흥분성 방전을 차단합니다. 공식 MOA 문서는 확보되지 않았으나(Data Gap), 문헌 전반에서 이 나트륨 채널 차단 기전이 일관되게 보고됩니다.

삼차신경통 치료의 1차 표준 약물인 carbamazepine, oxcarbazepine 역시 동일하게 나트륨 채널을 차단하는 기전을 공유합니다. 실제로 phenytoin은 carbamazepine 이전 시대부터 삼차신경통 치료에 사용되어 온 역사적 약물이며, 현재는 경구 1차 약물이 효과가 없거나 환자가 탈수·경구섭취 곤란 상태인 급성 발작기(acute exacerbation)에 **정맥주사 rescue 치료**로 재조명되고 있습니다. 이는 "동일 기전 계열 약물이 이미 검증된 적응증에 대한 자연스러운 확장"이라는 점에서 기전적 타당성이 높습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03712254](https://clinicaltrials.gov/study/NCT03712254) | N/A (전향적 관찰) | 완료 | 15 | 삼차신경통 급성 악화기에 phenytoin 투여 효과를 평가한 전향적 체계적 연구. 경구 1차 약물(carbamazepine/oxcarbazepine) 치료가 어려운 급성 악화기 대응이 목적 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Guideline | European Journal of Neurology | 유럽신경학회(EAN) 삼차신경통 관리 공식 가이드라인 |
| [35469475](https://pubmed.ncbi.nlm.nih.gov/35469475/) | 2022 | 후향적 임상연구 | Cephalalgia | 삼차신경통 급성 악화 144례에서 IV lacosamide/phenytoin 유효성·안전성 분석 |
| [32981076](https://pubmed.ncbi.nlm.nih.gov/32981076/) | 2020 | Case series | Headache | 삼차신경통 위기(crisis) 환자군에서 IV phenytoin rescue 치료 반응 후향적 코호트 |
| [28761370](https://pubmed.ncbi.nlm.nih.gov/28761370/) | 2017 | Review/Analysis | Journal of Pain Research | Phenytoin과 carbamazepine의 삼차신경통 치료 근거를 마케팅 기반 vs 근거 기반으로 비판적 분석 |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | Review | Molecular Pain | 삼차신경통 병태생리부터 약물치료(phenytoin 포함)까지의 총설 |
| [29114270](https://pubmed.ncbi.nlm.nih.gov/29114270/) | 2017 | Review | Asian Journal of Neurosurgery | 삼차신경통 진단·치료 전반 개관 |
| [19445753](https://pubmed.ncbi.nlm.nih.gov/19445753/) | 2009 | Review | BMJ Clinical Evidence | 삼차신경통 임상적 근거 총정리 |
| [15062534](https://pubmed.ncbi.nlm.nih.gov/15062534/) | 2004 | Review | Neurologic Clinics | 삼차신경통·설인신경통 개관, 항경련제가 가장 효과적인 약물군으로 기술 |
| [39993829](https://pubmed.ncbi.nlm.nih.gov/39993829/) | 2024 | 임상 개관 | Clinical Medicine & Research | 급성 삼차신경통 통증 위기의 입원 관리 프로토콜 |
| [2215936](https://pubmed.ncbi.nlm.nih.gov/2215936/) | 1990 | Case report | Neurology | 전형적 삼차신경통 발생 전 전구 통증("pre-trigeminal neuralgia") 사례 기술 |

## 한국 시판 정보

국내 정식 허가 데이터 없음 — **미출시**, 허가증 0건 (`taiwan_regulatory.total_licenses = 0`).

## 다른 예측 후보 요약 (전체 10개 비교)

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 | 권장 결정 | 비고 |
|---|---|---|---|---|---|
| 1 | 삼차신경 종양 (trigeminal nerve neoplasm) | 99.99% | L5 | Hold | ⚠ 문헌이 대부분 삼차신경통·Sturge-Weber 등 무관 주제, KG 매핑 오류 추정 |
| 2 | 놀람유발간질 (startle epilepsy) | 99.98% | L4 | Research Question | 개별 사례·동물 행동모델 수준, 일부 문헌은 lamotrigine 주제 |
| 3 | 식사유발발작 (eating seizures) | 99.98% | L4 | Research Question | 유일한 임상시험은 Ginkgo biloba PK 상호작용 연구로 효능시험 아님 |
| 4 | 오르가즘유발발작 (orgasm-induced seizures) | 99.98% | L5 | Hold | 임상시험·문헌 전무 |
| 5 | 배뇨유발발작 (micturition-induced seizures) | 99.98% | L4 | Research Question | 유사 반사성 발작 사례(PMID 21561835, clobazam+phenytoin 성공)는 다른 적응증에 분류됨 |
| 6 | 사고유발발작 (thinking seizures) | 99.98% | L4 | Hold | 제시된 임상시험 3건 모두 이 적응증과 직접 관련 없음 |
| 7 | 음향유발발작 (audiogenic seizures) | 99.98% | **L3** | Research Question | DBA/2 마우스 등 다수 동물모델에서 phenytoin 직접 검증, 인체 근거는 없음 |
| 8 | 독서유발발작 (reading seizures) | 99.97% | L4 | Research Question | 특이적 임상 근거 없음, 일반 뇌전증/phenytoin 문헌만 존재 |
| **9** | **삼차신경통 (trigeminal neuralgia)** | **99.97%** | **L2** | **Proceed with Guardrails** | 본 보고서 주 후보 |
| 10 | 베타-케토티올라아제 결핍증 (beta-ketothiolase deficiency) | 99.95% | L5 | Hold | 대사질환, 나트륨채널 기전과 생물학적 연관성 없음, 근거 전무 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. *(본 근거 팩에는 경고·금기·DDI 정보가 확보되지 않았으며, DG001로 "Blocking" 등급 데이터 갭이 지정되어 있습니다.)*

참고로 문헌 근거 내에서 확인된 phenytoin의 알려진 이상반응으로는 혈소판감소증, 안구운동마비, 말초신경병증, EMPACT 증후군(뇌전이 방사선치료 병용 시 다형홍반), 치은비대 등이 반복적으로 보고됩니다. 정식 허가사항 확인 전까지 참고용으로만 활용하시기 바랍니다.

## 결론 및 다음 단계

**결정: Proceed with Guardrails** (삼차신경통 한정) / **Hold** (그 외 후보 전반)

**사유:**
- 삼차신경통은 완료된 전향적 연구 1건, 후향적 다기관 연구(n=144), 유럽신경학회 가이드라인 등 L2 수준 근거와 함께, phenytoin과 동일 기전(나트륨 채널 차단)의 1차 치료제가 이미 확립되어 있어 재창출 타당성이 높습니다. 다만 phenytoin 자체의 대규모 RCT는 없고 주로 급성기 IV rescue 용도로 국한됩니다.
- 나머지 9개 후보 중 음향유발발작(L3)만 동물모델 수준의 기전적 근거가 있고, 3개 후보(삼차신경 종양, 오르가즘유발발작, 베타-케토티올라아제 결핍증)는 임상·문헌 근거가 전무하거나 KG 매핑 오류로 추정되어 즉시 폐기(Hold)를 권고합니다.

**진행하려면 필요한 것:**
- TFDA(국내 규제기관) 공식 경고·금기·상호작용 정보 확보 (DG001, Blocking 등급 — S1 안전성 초평가 진입 전 필수)
- Phenytoin 공식 MOA/DrugBank 데이터 보강 (DG002)
- 삼차신경통 급성기 IV phenytoin에 대한 전향적 대조군 연구 추가 확보(현재는 대부분 후향적/비대조 연구)
- 음향유발발작 등 L3~L4 후보는 인체 대상 파일럿 연구 여부를 우선 확인 후 재평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

