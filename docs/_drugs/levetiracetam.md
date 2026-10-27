---
layout: default
title: Levetiracetam
parent: 높은 근거 (L1-L2)
nav_order: 471
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-15
description: "Levetiracetam: 예측 신규 적응증 시각 유발 간질 (Visual epilepsy) (근거 수준 L1). 기존 적응증: 허가 적응증 텍스트가 링크 형태로만 제공되어 구체적인 문구는 확인되지 않음 (항경련제로 사용)"
monitor_inn: "LEVETIRACETAM"
predicted_indications: ["beta-ketothiolase deficiency"]
---

# Levetiracetam
{: .fs-9 }

근거 수준: **L1** | 예측 적응증: **10** 건
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

## Levetiracetam: 간질(항경련제 적응증)에서 시각 유발 간질로
{: .text-alpha }

## 한 문장 요약

Levetiracetam은 SV2A(시냅스 소포 단백질 2A)에 결합하는 항경련제로, 한국에서 간질 발작 치료에 사용되어 왔습니다.
TxGNN 모델은 **시각 유발 간질(Visual epilepsy)**에 효과가 있을 수 있다고 예측하지만, 이 질환에 대한 임상시험은 없고 문헌도 일반 발작 집단을 다룬 것이 대부분이어서 **직접적인 근거는 매우 제한적**입니다.
한편 예측 순위 9위인 **간질지속상태(Status epilepticus)**는 Phase 3 임상시험을 포함해 근거가 가장 탄탄하여 참고용으로 함께 정리했습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 텍스트가 링크 형태로만 제공되어 구체적인 문구는 확인되지 않음 (항경련제로 사용) |
| 예측 신규 적응증 | 시각 유발 간질 (Visual epilepsy) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L3 (임상시험 없음, 일반 발작 집단 대상 문헌 위주) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 (모두 단일제, 유효) |
| 권장 결정 | Hold (추가 연구 필요 과제) |

> 참고: 이 보고서가 제시한 상위 예측 10건 중 근거 수준이 가장 높은 것은 간질지속상태(L1, Proceed with Guardrails)입니다. 아래 별도 섹션에 정리했습니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 다만 수집된 문헌에 따르면 Levetiracetam은 SV2A에 결합하여 신경전달물질 방출을 억제하는 것으로 알려져 있으며, 국소 발작과 전신 발작 모두에 사용되는 확립된 항경련제입니다.

시각(광과민성) 간질은 이 범위에 속하는 반사성 간질입니다. 따라서 발작 억제라는 일반적 기전상 효과를 기대할 수 있습니다. 다만 수집된 문헌은 신생아, 뇌졸중 후, 신경중환자 등 일반 발작 집단을 다루고 있으며 시각 유발 발작만을 따로 연구한 자료는 없습니다.

참고로 같은 SV2A 리간드인 seletracetam의 광과민성 간질 환자 대상 Phase 2 시험(PMID 39827675)이 보고되어 있어, 이 기전이 광과민성 반응과 관련될 가능성을 시사합니다. 다만 이는 Levetiracetam 자체의 근거는 아닙니다.

## 임상시험 근거

시각 유발 간질(예측 1순위)에 대해 현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

시각 유발 간질에 대해 수집된 문헌 중 비교적 관련성이 높은 자료는 다음과 같습니다. 모두 특정 질환이 아닌 일반 발작 집단을 대상으로 합니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | RCT | Pediatrics | 신생아 발작에서 Levetiracetam과 페노바르비탈 비교 |
| [35963261](https://pubmed.ncbi.nlm.nih.gov/35963261/) | 2022 | RCT (Phase 3) | The Lancet Neurology | 뇌내출혈 급성기에서 예방적 Levetiracetam의 발작 예방 효과 평가 |
| [34286461](https://pubmed.ncbi.nlm.nih.gov/34286461/) | 2022 | 메타분석 | Neurocritical Care | 신경중환자에서 발작 예방 목적 Levetiracetam의 효능과 이상반응 검토 |
| [39808752](https://pubmed.ncbi.nlm.nih.gov/39808752/) | 2025 | 네트워크 메타분석 | Neurology | 뇌졸중 후 발작에서 항경련제 비교 |
| [33060105](https://pubmed.ncbi.nlm.nih.gov/33060105/) | 2021 | 메타분석 | Arch Dis Child | 소아 경련성 간질지속상태에서 Levetiracetam 평가 |
| [38678766](https://pubmed.ncbi.nlm.nih.gov/38678766/) | 2024 | RCT (공개 라벨) | Seizure | 급성 뇌염 증후군 소아에서 페니토인과 Levetiracetam 비교 |
| [21936590](https://pubmed.ncbi.nlm.nih.gov/21936590/) | 2011 | 리뷰 | CNS Drugs | 간질에서 Levetiracetam 개요 |
| [12915343](https://pubmed.ncbi.nlm.nih.gov/12915343/) | 2003 | 리뷰 | Epileptic Disorders | Levetiracetam 안전성 프로파일 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201805181 | 큐팜엑스알서방정500밀리그램 | 서방성 필름코팅정 | 허가사항 문서 참조 |
| 201301649 | 원프라정250밀리그램 | 필름코팅정 | 허가사항 문서 참조 |
| 201908013 | 케파베아정250밀리그램 | 필름코팅정 | 허가사항 문서 참조 |
| 201605338 | 레비티람주500mg | 주사제 | 허가사항 문서 참조 |
| 201605863 | 케프라엑스알서방정750밀리그램 | 서방성 필름코팅정제 | 허가사항 문서 참조 |

허가 적응증 문구는 이 보고서에 수집된 데이터에서 확인되지 않았으며, 허가사항 문서는 식품의약품안전처 의약품안전나라에서 확인할 수 있습니다. 한국에는 정제, 서방정, 주사제 등 총 20건의 유효 허가가 있습니다.

## 안전성 고려사항

허가사항의 경고 및 금기 정보는 수집되지 않았으므로 허가사항을 참조하세요.

- **약물 상호작용**: 총 100건이 조회되었으며, 중등도(Moderate)로 분류된 주요 항목은 Morphine, Morphine(리포좀), Dronabinol, Nabilone, Metoclopramide, Opium, Sibutramine입니다. 중추신경 억제 효과가 겹칠 수 있는 약물이 다수 포함됩니다.
- **지식그래프상 금기 연관 질환**: 허가사항이 아닌 모델의 지식그래프에서 도출된 정보로, 불안장애, 정신병적 장애, 조현정동장애, 신장 질환, 간 질환, 호중구감소증, 무과립구증, 백혈구감소증, 범혈구감소증 등이 연관되어 있습니다. 참고용으로만 활용하세요.
- **문헌에서 보고된 이상반응**: 잇몸 증식, 저나트륨혈증, 발작 악화(Levetiracetam-induced seizure aggravation), 과민성(irritability) 등이 보고되었습니다.

## 간질지속상태: 근거가 가장 풍부한 예측 (참고)

| 항목 | 내용 |
|------|------|
| TxGNN 예측 점수 | 99.91% |
| 근거 수준 | L1 |
| 권장 결정 | Proceed with Guardrails |

### 주요 임상시험

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01960075](https://clinicaltrials.gov/study/NCT01960075) | Phase 3 | 완료 | 478 | 벤조디아제핀 불응성 간질지속상태에서 fosphenytoin, valproate, Levetiracetam 비교 (ESETT) |
| [NCT01150331](https://clinicaltrials.gov/study/NCT01150331) | Phase 3 | 완료 | 203 | 병원 전 단계에서 IV Levetiracetam + clonazepam과 clonazepam 단독 비교 |
| [NCT02920060](https://clinicaltrials.gov/study/NCT02920060) | Phase 2 | 완료 | 80 | 소아 불응성 전신 경련성 간질지속상태에서 Levetiracetam과 valproate 비교 |
| [NCT04926844](https://clinicaltrials.gov/study/NCT04926844) | Phase 2 | 완료 | 144 | 소아 전신 경련성 간질지속상태에서 Levetiracetam + midazolam 병용 |
| [NCT07052136](https://clinicaltrials.gov/study/NCT07052136) | 해당 없음 | 완료 | 138 | 소아 간질지속상태에서 Levetiracetam과 valproic acid 비교 |
| [NCT06403150](https://clinicaltrials.gov/study/NCT06403150) | Phase 4 | 완료 | 62 | 경련성 간질지속상태에서 Levetiracetam과 fosphenytoin 비교 (공개 라벨) |
| [NCT07046611](https://clinicaltrials.gov/study/NCT07046611) | Phase 2/3 | 모집 중 | 124 | 소아에서 ketamine + Levetiracetam 병용 평가 |
| [NCT06907173](https://clinicaltrials.gov/study/NCT06907173) | Phase 3 | 모집 중 | 770 | ketamine + Levetiracetam과 Levetiracetam 단독 비교 (KESETT) |

### 주요 문헌

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [31774955](https://pubmed.ncbi.nlm.nih.gov/31774955/) | 2019 | RCT | N Engl J Med | 벤조디아제핀 불응성 간질지속상태에서 세 가지 항경련제 비교 |
| [32203691](https://pubmed.ncbi.nlm.nih.gov/32203691/) | 2020 | RCT | Lancet | 연령군별 ESETT 결과 분석 |
| [33190679](https://pubmed.ncbi.nlm.nih.gov/33190679/) | 2020 | RCT | Health Technol Assess | 소아에서 페니토인 대안으로서의 Levetiracetam (EcLiPSE) |

ESETT에서 Levetiracetam은 fosphenytoin, valproate와 비슷한 효능을 보였습니다. 즉 **우월한 약이 아니라 합리적인 대안**으로 해석됩니다.

## 결론 및 다음 단계

**결정: Hold** (시각 유발 간질 기준)

**사유:**
시각 유발 간질에 대해서는 임상시험이 없고, 수집된 문헌도 일반 발작 집단 연구에 그칩니다. TxGNN 점수는 높지만 이를 뒷받침하는 직접 근거가 부족합니다. 반면 간질지속상태는 Phase 3 근거가 있어 **Proceed with Guardrails**가 가능합니다.

**진행하려면 필요한 것:**
- 광과민성(시각 유발) 간질 환자 대상 Levetiracetam 임상 연구 (예: 간헐적 광자극에 대한 광발작 반응 평가)
- 허가사항의 경고 및 금기 정보 확보 (현재 안전성 정보 미확보)
- 작용 기전(MOA) 데이터 보강
- 간질지속상태로 진행할 경우: 신기능에 따른 용량 조절, 행동 이상반응 모니터링, 국내 프로토콜 준수

**기타 예측 질환 요약:** 시작 순위 외에 시동 발작(startle epilepsy, L3), 청각 유발 발작(L4), 읽기 발작(L4)은 소규모 임상 연구 또는 증례 위주의 근거가 있어 추가 연구 과제 수준입니다. 사고 유발·식사 유발·배뇨 유발 발작(L4)은 직접 근거가 없고, 오르가즘 유발 발작과 베타-케토티올라제 결핍증(L5)은 모델 예측만 있어 보류(Hold)가 적절합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

