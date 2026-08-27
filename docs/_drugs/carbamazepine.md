---
layout: default
title: Carbamazepine
parent: 僅模型預測 (L5)
nav_order: 172
evidence_level: L5
indication_count: 10
---

# Carbamazepine
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

# Carbamazepine: 간질/삼차신경통에서 삼차신경 종양(Trigeminal Nerve Neoplasm)으로

## 한 문장 요약

Carbamazepine은 전압-개폐 나트륨 채널을 차단하는 항경련제로, 국제적으로 간질(부분발작)과 삼차신경통(Trigeminal Neuralgia)의 1차 치료제로 널리 사용되어 온 약물입니다. TxGNN 모델은 이번 평가 대상 중 가장 높은 순위로 **삼차신경 종양(Trigeminal Nerve Neoplasm)**을 예측했으나, 현재 확보된 근거(임상시험 1건·문헌 20편)를 검토한 결과 이는 "종양이 삼차신경을 압박해 유발된 이차성 신경통"과 "삼차신경통(질환명 자체)"이 혼동된 질병 개체(disease entity) 매핑 오류일 가능성이 높습니다. 실제로 carbamazepine이 항종양 기전을 갖는다는 근거는 전혀 없으며, 바로 다음 순위(2순위, 삼차신경통)가 훨씬 견고한 근거(L1, 완료된 Phase 2/3 RCT 다수)를 갖고 있어 함께 확인이 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 간질(부분발작) 및 삼차신경통 — 국제적으로 확립된 표준 적응증(일반 약리 지식). 한국 허가 정보는 확보되지 않음 |
| 예측 신규 적응증 | 삼차신경 종양 (Trigeminal Nerve Neoplasm) |
| TxGNN 예측 점수 | 99.998% (모델 내 순위 169위) |
| 근거 수준 | L4 (전임상/기전 수준 — 치료 목적 임상시험 없음) |
| 한국 시판 현황 | 미상영 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

> 참고: 2순위 예측인 **삼차신경통(Trigeminal Neuralgia)**은 TxGNN 점수 99.991%(순위 457위)로 1순위보다 모델 점수는 낮지만, 실제 임상 근거 수준은 **L1(Proceed with Guardrails)**로 훨씬 견고합니다. 모델 순위와 임상적 타당성이 반드시 일치하지 않는 사례로, 아래 "타당성" 섹션에서 함께 설명합니다.

---

## 이 예측이 타당한 이유는?

Carbamazepine의 공식 작용기전(MOA) 데이터는 이번 Evidence Pack에서 확보되지 않았습니다(DrugBank 조회 미완료). 다만 증거 자료 내 기전 분석(repurposing rationale)에 따르면, carbamazepine은 **전압-개폐 나트륨 채널을 차단하여 삼차신경 근부/신경절 내 이상 고빈도 방전을 억제**하는 것으로 설명되며, 이는 삼차신경통 치료의 전 세계적 표준 기전으로 잘 알려져 있습니다.

문제는 1순위로 예측된 "삼차신경 종양"입니다. 관련 문헌들을 살펴보면 schwannoma, 림프종, 지방종, 유피낭종, 정맥혈관종 등 **종양이 삼차신경을 압박해 이차성 신경통을 유발한 증례**가 대부분이며, 이 경우 carbamazepine은 나트륨 채널 차단을 통해 통증 증상만 완화할 뿐 종양 자체를 치료하지 않습니다. 실제로 다수의 증례(PMID 30741017, 15235745 등)에서는 오히려 "carbamazepine 투여에도 증상이 개선되지 않아" 종양이 발견된 경위가 기술되어 있어, carbamazepine의 유효성을 뒷받침하기보다는 **감별진단의 실패 사례**에 가깝습니다. 즉, 이번 예측은 "삼차신경통"이라는 질환명과 "삼차신경 종양"이라는 원인 병변이 데이터상 혼동되어 발생한 개체 매핑 오류(entity confusion)로 판단됩니다.

반면 2순위 "삼차신경통" 자체는 carbamazepine이 이미 전 세계적으로 승인·사용 중인 1차 치료제이며, 다수의 완료된 Phase 2~4 RCT가 이를 직접 뒷받침합니다. 다만 이는 "새로운 적응증 발굴"이라기보다 **기존에 확립된 적응증을 모델이 재확인한 결과**에 가깝습니다.

---

## 임상시험 근거

*(predicted_indications[0] "삼차신경 종양" 기준)*

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT06853119](https://clinicaltrials.gov/study/NCT06853119) | N/A | 모집 예정 | 120 | 삼차신경통 환자의 뇌 기능/구조 변화를 MRI로 분석하는 관찰 연구로, 치료 목적 시험이 아니며 carbamazepine 유효성과 직접 관련 없음 (관련성 등급 C) |

**한 건 외 관련 치료 목적 임상시험은 등록되어 있지 않습니다.**

---

## 문헌 근거

*(predicted_indications[0] "삼차신경 종양" 기준, 관련성 높은 순 최대 10편)*

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [36824641](https://pubmed.ncbi.nlm.nih.gov/36824641/) | 2022 | Review | Acta Clin Croat | 삼차신경통의 치료 옵션 개관. 혈관 압박 또는 종양성 병변이 원인이 될 수 있음을 언급 |
| [3181365](https://pubmed.ncbi.nlm.nih.gov/3181365/) | 1988 | 동물실험 | Exp Neurol | Carbamazepine이 신경종(neuroma)에서 자발적 이상 방전을 억제함을 보고 — 신경 손상 부위의 통증 완화 기전과 관련되나 항종양 효과는 아님 |
| [30741017](https://pubmed.ncbi.nlm.nih.gov/30741017/) | 2023 | Case Report | Br J Neurosurg | 삼차신경 원발성 신경림프종 증례. Carbamazepine 처방에도 증상 개선 없어 종양이 발견됨 |
| [12590697](https://pubmed.ncbi.nlm.nih.gov/12590697/) | 2003 | Case Report | Neurosurgery | 삼차신경 유육종(sarcoid granuloma) 증례로 schwannoma와 감별이 어려웠던 사례 |
| [27729607](https://pubmed.ncbi.nlm.nih.gov/27729607/) | 2016 | Case Report | No Shinkei Geka | Meckel's cave 유피낭종이 동안신경마비 및 삼차신경통으로 발현된 증례 |
| [25433061](https://pubmed.ncbi.nlm.nih.gov/25433061/) | 2014 | Case Report/Review | No Shinkei Geka | Carbamazepine으로 통증 조절이 불충분했던 소뇌교각 지방종에 의한 삼차신경통 증례 |
| [25968963](https://pubmed.ncbi.nlm.nih.gov/25968963/) | 2015 | Case Report/Review | World Neurosurg | 정맥혈관종에 의한 삼차신경통 증례 및 문헌고찰 |
| [33989821](https://pubmed.ncbi.nlm.nih.gov/33989821/) | 2021 | Case Report | World Neurosurg | 추체사대뇌수막종(petroclival meningioma)이 삼차신경통으로 발현된 증례 |
| [26768887](https://pubmed.ncbi.nlm.nih.gov/26768887/) | 2016 | Case Report/Review | Turk Neurosurg | 뇌하수체선종이 삼차신경통으로 단독 발현된 드문 증례 |
| [23796885](https://pubmed.ncbi.nlm.nih.gov/23796885/) | 2012 | Case Report | Pediatr Neurosurg | 소아기 소뇌교각 지방종 관련 삼차신경통 증례 |

**공통 패턴**: 대부분 종양(schwannoma, 림프종, 지방종, 수막종, 뇌하수체선종 등)이 삼차신경을 압박해 통증을 유발한 증례이며, carbamazepine은 증상 완화 목적으로만 사용되었고 종양 치료 효과는 보고되지 않았습니다. RCT나 대조군 연구는 확인되지 않았습니다.

---

## 한국 시판 정보

Carbamazepine은 현재 한국에서 **미상영** 상태이며, 확보된 허가증은 0건입니다. 허가 관련 데이터가 없어 별도 표를 제공하지 않습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

*(주요 경고, 금기, 약물상호작용 데이터 모두 확보되지 않았습니다 — DG001 참조)*

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- "삼차신경 종양"에 대한 치료 목적 임상시험이 없고, 확인된 문헌은 모두 "종양에 의한 이차성 삼차신경통" 증례로 구성되어 있어 carbamazepine이 종양 자체에 작용한다는 근거가 없습니다.
- 증거 자료 자체의 기전 분석에서도 이번 예측이 "질병 개체 매핑 오류(삼차신경통과의 혼동)"일 가능성을 명시하고 있어(evidence_level L4, decision_stage S1), 현재로서는 진행 근거가 부족합니다.
- 반면 2순위 "삼차신경통"은 이미 확립된 carbamazepine의 표준 적응증으로, 새로운 재창출 후보라기보다는 모델 검증(sanity check) 성격이 강합니다.

**진행하려면 필요한 것:**
- TxGNN 예측에 사용된 질병 개체(disease entity) ID 재검증 — "trigeminal nerve neoplasm"과 "trigeminal neuralgia"가 혼동되지 않았는지 원본 매핑 확인
- 항종양 기전 관련 전임상 데이터(세포주/동물모델) 추가 확보 시 재평가
- DrugBank를 통한 carbamazepine 공식 MOA 데이터 확보 (DG002)
- 한국 허가사항(경고·금기·DDI) 확보를 위한 TFDA/식약처 자료 조회 (DG001, Blocking)
- 별도로 2순위 "삼차신경통" 신호는 이미 확립된 적응증 재확인 성격이므로, 진정한 재창출 후보로서 가치는 낮으나 참고 자료로 병기 권장
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

