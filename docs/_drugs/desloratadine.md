---
layout: default
title: Desloratadine
parent: 모델 예측만 (L5)
nav_order: 262
evidence_level: L5
indication_count: 4
monitor_inn: "desloratadine"
predicted_indications: ["nasal cavity disease", "recalcitrant atopic dermatitis", "IgE responsiveness, atopic", "rosacea conjunctivitis"]
last_modified_at: 2026-11-20
description: "Desloratadine: 예측 신규 적응증 비강 질환 (nasal cavity disease) (근거 수준 L5). 기존 적응증: 다음 질환의 증상 완화 1. 알레르기성 비염 2. 만성 특발성 두드러기"
---

# Desloratadine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **4** 건
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

## Desloratadine: H1 항히스타민제 → 비강 질환 (nasal cavity disease)
{: .text-alpha }

## 한 문장 요약

Desloratadine은 H1 수용체를 차단하는 항히스타민제 계열 약물입니다.
TxGNN 모델은 **비강 질환(nasal cavity disease)**에 효과가 있을 수 있다고 예측하지만, 현재 이 질환을 직접 다룬 **임상시험은 0건**이고 **문헌 2편**은 모두 동물 연구입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 다음 질환의 증상 완화 1. 알레르기성 비염 2. 만성 특발성 두드러기 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200008952/EE)) |
| 예측 신규 적응증 | 비강 질환 (nasal cavity disease) |
| TxGNN 예측 점수 | 0.9987 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Desloratadine 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “데스로라타딘은 선택적 H1 수용체 히스타민 길항 활성을 가진 지속형 삼환계 히스타민 길항제이다. 수용체 결합 자료에 따르면 2-3 ng/mL(7 nanomolar) 농도에서 데스로라타딘은 인간 히스타민 H1 수용체와 유의한 상호작용을 나타낸다.” 영어 원문: "Desloratadine is a long-acting tricyclic histamine antagonist with selective H1-receptor histamine antagonist activity. Receptor binding data indicates that at a concentration of 2-3 ng/mL (7 nanomolar), desloratadine shows significant interaction with the human histamine H1-receptor." ([DailyMed: Desloratadine Oral Solution (desloratadine) prescribing information, INA Pharmaceutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=41d5e0d4-6188-847b-e063-6294a90a2e2f), 버전 2025-10-23; 확인일 2026-11-19). 일반적으로 desloratadine은 H1 수용체 차단 계열 약물로 알려져 있으며, 히스타민이 관여하는 비강 증상에 기전상 적용 가능할 수 있습니다.

다만 이 예측의 높은 점수는 이미 알려진 알레르기 관련 용도와의 중복을 반영했을 가능성이 있어, 새로운 재창출 기회로 보기는 어렵습니다. 또한 "비강 질환"은 범위가 넓고 구체적이지 않은 분류입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [30488351](https://pubmed.ncbi.nlm.nih.gov/30488351/) | 2019 | 동물 연구 | Eur Arch Otorhinolaryngol | 난알부민 유도 알레르기 비염 쥐 모델에서 hesperidin과 thymol의 효과 평가 (desloratadine 직접 시험 아님) |
| [19769798](https://pubmed.ncbi.nlm.nih.gov/19769798/) | 2009 | 동물 연구 | Am J Rhinol Allergy | 고양이 비충혈 모델에서 loratadine과 montelukast 병용의 충혈 완화 효과, desloratadine과 pseudoephedrine 병용도 평가 |

두 문헌 모두 동물 모델 연구이며, 사람을 대상으로 desloratadine의 비강 질환 효과를 검증한 자료는 아닙니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200008952 | 에리우스정(데스로라타딘(미분화)) | 연한 청색의 양면이 볼록한 원형 정제 | 허가 적응증 텍스트 미기재 |

## 안전성 고려사항

- **약물 상호작용**: 조회된 상호작용은 총 266건이며, 일부 예시는 Calcitriol, Phentermine, Pantoprazole, Doxycycline, Morphine, Metformin, Omeprazole, Simvastatin, Epinephrine 등입니다. 이 자료에는 위험 등급이 구분되어 있지 않습니다(등급 미상).

## 결론 및 다음 단계

**결정: Hold**

**사유:**
이 예측을 직접 검증한 임상시험이 없고 문헌도 동물 연구뿐이어서 근거 수준은 L5입니다. 질환 정의가 넓고 비특이적이라 새로운 적응증으로서의 가치도 불분명합니다.

**진행하려면 필요한 것:**
- 허가사항(경고, 금기, 적응증)의 확보 및 검토
- 작용 기전(MOA) 데이터 보완
- 구체적인 비강 질환 하위 유형을 정의하고, 사람 대상 임상 근거를 확보

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Desloratadine Oral Solution (desloratadine) prescribing information, INA Pharmaceutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=41d5e0d4-6188-847b-e063-6294a90a2e2f) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

