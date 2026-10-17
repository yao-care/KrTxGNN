---
layout: default
title: Brivaracetam
parent: 모델 예측만 (L5)
nav_order: 157
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Brivaracetam: 예측 신규 적응증 시각성 간질 (Visual Epilepsy) (근거 수준 L5). 기존 적응증: 확인 불가 (허가 적응증이 PDF 링크로만 제공되어 본문을 확인할 수 없음. 문헌상 국소 발작 치료제로 알려져 있음)"
monitor_inn: "BRIVARACETAM"
predicted_indications: ["beta-ketothiolase deficiency"]
---

# Brivaracetam
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

# Brivaracetam: 간질(국소 발작 등)에서 시각성 간질로

## 한 문장 요약

Brivaracetam은 SV2A(시냅스 소포 단백질 2A)에 결합하는 항경련제로, 한국에서 간질 발작 치료제로 허가·시판되고 있습니다.
TxGNN 모델은 **시각성 간질(Visual Epilepsy)**에 효과가 있을 수 있다고 예측하지만, 이 적응증을 직접 다룬 임상시험은 없고 문헌 18편도 간질 전반을 다룬 일반 자료입니다.
한편 2순위 예측인 **간질중첩증(Status Epilepticus)**은 완료된 임상시험 1건과 체계적 문헌고찰 등 상대적으로 더 많은 근거가 있어, 아래에 함께 정리했습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 적응증이 PDF 링크로만 제공되어 본문을 확인할 수 없음. 문헌상 국소 발작 치료제로 알려져 있음) |
| 예측 신규 적응증 | 시각성 간질 (Visual Epilepsy) |
| TxGNN 예측 점수 | 99.51% |
| 근거 수준 | L4 (기전·전임상 수준의 간접 근거) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 |
| 권장 결정 | Hold (연구 질문 단계) |

> 참고: 예측 목록 전체에서는 간질중첩증(L3, Proceed with Guardrails)이 근거가 가장 풍부합니다. 아래 "다른 예측 적응증 요약"을 참조하세요.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 이 보고서용 자료에 없습니다. 다만 수집된 문헌에 따르면 Brivaracetam은 levetiracetam보다 SV2A에 15~30배 높은 친화도로 결합하는 항경련제이며, 국소 발작 및 전신 발작에서 항경련 효과가 보고되었습니다. 이는 시냅스 소포 방출과 신경 과흥분을 줄이는 기전으로 이해됩니다.

시각성 간질은 시각 자극으로 유발되는 반사성 간질 아형이어서, 일반적인 항경련 기전이 적용될 가능성은 있습니다. 또한 광과민성(photosensitivity) 모델이 항경련제 평가에 쓰여 왔으며, 관련 문헌(PMID 36528008)이 Brivaracetam과 levetiracetam을 이 모델 관점에서 논의합니다.

그러나 수집된 문헌은 간질중첩증 총설, 항경련제 기전, 국소 발작 보조요법 시험 등 일반적 내용이며 시각 유발 발작을 직접 다루지 않습니다. 따라서 기전적 타당성은 "그럴듯하다" 수준이며, 직접 입증된 것은 아닙니다.

## 임상시험 근거

현재 시각성 간질과 관련해 등록된 임상시험이 없습니다.

## 문헌 근거

시각성 간질에 직접 해당하는 문헌은 없으며, 아래는 간접 근거(우선순위: RCT > Review)입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [38576178](https://pubmed.ncbi.nlm.nih.gov/38576178/) | 2024 | RCT (Phase 3) | Epilepsia Open | 조절되지 않는 국소 발작 아시아 성인에서 보조요법 Brivaracetam의 효능·안전성·내약성 평가 |
| [38811492](https://pubmed.ncbi.nlm.nih.gov/38811492/) | 2024 | Review | Advances in Therapy | Brivaracetam은 SV2A 친화도가 levetiracetam보다 15~30배 높고, 전임상 및 임상적 이점을 정리 |
| [35061214](https://pubmed.ncbi.nlm.nih.gov/35061214/) | 2022 | 체계적 문헌고찰/네트워크 메타분석 | Drugs | 국소 발작 보조요법으로 쓰이는 3세대 항경련제(Brivaracetam 포함) 비교 |
| [32120063](https://pubmed.ncbi.nlm.nih.gov/32120063/) | 2020 | Review | Neuropharmacology | 현재 사용되는 항경련제의 작용 기전 정리 |
| [38117319](https://pubmed.ncbi.nlm.nih.gov/38117319/) | 2024 | Review | Intensive Care Medicine | 중환자실에서의 간질중첩증 관리 |
| [37684052](https://pubmed.ncbi.nlm.nih.gov/37684052/) | 2023 | Review | BMJ | 임신·수유 중 간질 관리 |
| [31195850](https://pubmed.ncbi.nlm.nih.gov/31195850/) | 2019 | Review | Expert Rev Neurother | 국소 간질에서 Brivaracetam의 효능과 안전성 |
| [40568060](https://pubmed.ncbi.nlm.nih.gov/40568060/) | 2025 | Review | J Epilepsy Res | Brivaracetam의 약리, 임상 효능, 안전성 |
| [37483441](https://pubmed.ncbi.nlm.nih.gov/37483441/) | 2023 | 체계적 문헌고찰/메타분석 | Front Neurol | 소아 간질에서 Brivaracetam의 안전성·효능 |
| [26664121](https://pubmed.ncbi.nlm.nih.gov/26664121/) | 2015 | Review | Neuropsychiatr Dis Treat | Brivaracetam의 프로파일과 간질 치료 잠재력 |

## 다른 예측 적응증 요약

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 | 비고 |
|------|-----------|-----------|----------|------|
| 2 | 간질중첩증 (Status Epilepticus) | 99.40% | L3 | 소아 대상 IV Brivaracetam vs levetiracetam 임상시험 [NCT07163572](https://clinicaltrials.gov/study/NCT07163572) (Phase 해당 없음, 완료, 152명). 체계적 문헌고찰 2건([32278203](https://pubmed.ncbi.nlm.nih.gov/32278203/), [41838218](https://pubmed.ncbi.nlm.nih.gov/41838218/))은 대부분 관찰·후향 자료를 요약. Phase 3 RCT 근거는 없음 |
| 3 | 청각유발 발작 (Audiogenic seizures) | 99.19% | L4 | 마우스 등 전임상 근거만 있음 |
| 4~8 | 섭식·오르가즘·사고·배뇨 유발 발작, 놀람 간질 | 99.19% | L4~L5 | 직접 근거 없음 (예측만 존재) |
| 9 | 베타-케토티올라제 결핍증 | 99.14% | L5 | SV2A 기전과의 연관성이 불분명하며, 그래프 기반 인공 예측일 가능성이 높음 |
| 10 | 청각 증상을 동반한 상염색체 우성 간질 | 99.10% | L5 | 직접 근거 없음 |

## 한국 시판 정보

허가 적응증 본문은 PDF 링크로만 제공되어 요약할 수 없습니다. 허가사항은 식약처 의약품안전나라에서 확인하세요.

| 허가번호 | 제품명 | 제형 | 제조사 |
|---------|------|------|-------|
| 201901308 | 브리비액트정25밀리그램 | 필름코팅정 | 한국유씨비제약 |
| 201901309 | 브리비액트정50밀리그램 | 필름코팅정 | 한국유씨비제약 |
| 201901307 | 브리비액트정10밀리그램 | 필름코팅정 | 한국유씨비제약 |
| 201901306 | 브리비액트액 | 액제 | 한국유씨비제약 |
| 202502767 | 부리팜정25밀리그램 | 필름코팅정 | 명인제약 |

전체 20건이 모두 유효한 단일제 허가이며, 취소된 허가는 없습니다. 오리지널(브리비액트) 외에 2025년 허가된 다수의 제네릭이 있습니다.

## 안전성 고려사항

**약물 상호작용**: 총 69건이 확인되었으며, 이 중 주요 항목은 다음과 같습니다.
- **중등도(Moderate)**: Morphine, Opium, Dronabinol, Nabilone, Metoclopramide, Sibutramine, Difenoxin, Diphenoxylate, Ethanol, Promethazine, Clopidogrel 등. 중추신경계 억제가 겹칠 수 있는 약물이 다수 포함됩니다.
- **경미(Minor)**: Omeprazole, Esomeprazole, Lansoprazole, Pantoprazole, Dexlansoprazole, Chlorpropamide, Tolbutamide, Cilostazol 등

그 밖의 경고·금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold** (시각성 간질 기준; 연구 질문 단계)

**사유:**
시각성 간질에 대한 임상시험이 없고 문헌도 일반적·간접적이어서 근거 수준은 L4입니다. 기전적으로 그럴듯하나 직접 입증이 없습니다. 참고로 간질중첩증은 L3로 Proceed with Guardrails 수준이므로 우선 검토 대상이 될 수 있습니다.

**진행하려면 필요한 것:**
- 시각 유발 발작·광과민성 간질에서 Brivaracetam을 직접 평가한 연구(예: 광과민성 모델의 광발작 반응 평가) 확보
- 허가사항(경고, 금기, 적응증 본문) 확보 및 분석. 현재 PDF 링크만 있어 안전성 선별을 진행할 수 없음
- 작용 기전(MOA) 데이터 보완
- (간질중첩증 경로) NCT07163572의 설계(무작위·눈가림 여부)와 결과 확인, 성인 대상 Phase 3 RCT 근거 확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

