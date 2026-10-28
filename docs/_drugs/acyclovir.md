---
layout: default
title: Acyclovir
parent: 모델 예측만 (L5)
nav_order: 23
evidence_level: L5
indication_count: 9
monitor_inn: "Acyclovir"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "common wart", "hepatitis C induced liver cirrhosis", "eosinophilic pustular folliculitis", "sequela of COVID-19", "vulvovaginal candidiasis", "papular urticaria", "disease of orbital region", "epidemic keratoconjunctivitis"]
last_modified_at: 2026-10-27
description: "Acyclovir: 예측 신규 적응증 점상 상피성 각결막염 (punctate epithelial keratoconjunctivitis) (근거 수준 L5). 기존 적응증: 이 약은 재발성 구순포진의 초기 치료에 사용합니다"
---

# Acyclovir
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **9** 건
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

## Acyclovir: 핵산 유사체 계열 항바이러스제 → 점상 상피성 각결막염 (punctate epithelial keratoconjunctivitis)
{: .text-alpha }

## 한 문장 요약

Acyclovir는 헤르페스 바이러스의 DNA 중합효소를 억제하는 항바이러스제입니다.
TxGNN 모델은 **점상 상피성 각결막염(punctate epithelial keratoconjunctivitis)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 다룬 임상시험은 없고 관련 문헌 2편도 이 질환과 직접적인 관련이 없습니다.
따라서 현재 근거는 모델 예측 수준(L5)에 머뭅니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 이 약은 재발성 구순포진의 초기 치료에 사용합니다.; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199801312/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199701432/EE; 이 약은 단순포진(물집) 바이러스 감염증(초기 및 재발성 생식기 포진(물집)과 구순포진(물집) 포함)에 사용합니다.; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199201002/EE; https://nedrug.mfds.go.k |
| 예측 신규 적응증 | 점상 상피성 각결막염 (punctate epithelial keratoconjunctivitis) |
| TxGNN 예측 점수 | 0.9967 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 최소 20건 (목록이 일부일 수 있음) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 수집되지 않았습니다. 일반적으로 acyclovir는 바이러스 티미딘 키나아제에 의해 인산화된 뒤 헤르페스 바이러스의 DNA 중합효소를 억제하는 것으로 알려져 있습니다.

이번에 수집된 문헌 2편은 미포자충성 각결막염(microsporidial keratoconjunctivitis)과 AIDS 환자의 각막 지질증(corneal lipidosis)을 다룹니다. 두 질환 모두 헤르페스 바이러스가 원인이 아니므로 acyclovir와의 항바이러스 기전상 연결고리를 찾기 어렵습니다. 높은 예측 점수는 헤르페스성 안질환과의 유사성에서 비롯된 것일 가능성이 있으며, 실제 기전을 반영한다고 보기는 어렵습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [21934222](https://pubmed.ncbi.nlm.nih.gov/21934222/) | 2011 | 증례 시리즈 | Indian J Pathol Microbiol | 인도 동부 코호트의 미포자충성 각결막염 특징 기술. acyclovir 효능에 대한 직접 근거 아님 |
| [7825685](https://pubmed.ncbi.nlm.nih.gov/7825685/) | 1995 | 증례 보고/리뷰 | Am J Ophthalmol | AIDS 환자 2명에서 약물 유발성 각막 지질증 보고. 점상 상피성 각결막염의 치료 근거 아님 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202002583 | 헤르페진크림 | 크림 | 재발성 구순포진의 초기 치료 |
| 199201022 | 씨크로크림 | 크림 | 단순포진 바이러스 감염증(초기 및 재발성 생식기 포진과 구순포진 포함) |
| 200301629 | 에이버크림 | 크림 | 단순포진 바이러스 감염증(초기 및 재발성 생식기 포진과 구순포진 포함) |
| 202007060 | 아시클로크림 | 크림 | 단순포진 바이러스 감염증(초기 및 재발성 생식기 포진과 구순포진 포함) |
| 199201976 | 팜젠아시클로버연고 | 연고 | 단순포진 바이러스 감염증(초기 및 재발성 생식기 포진과 구순포진 포함) |

위 표는 주요 허가 5건만 나열한 것이며, 허가증은 최소 20건입니다. 목록이 일부일 수 있습니다.

## 안전성 고려사항

- **약물 상호작용**: 총 100건의 상호작용 정보가 조회되었습니다. 중등도로 분류된 주요 항목은 balsalazide, mesalazine, olsalazine, sulfasalazine, trospium입니다. 그 밖에 amphotericin B, metformin, morphine 등이 등급 미상으로 조회되었습니다.

허가사항의 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
점상 상피성 각결막염을 직접 연구한 임상시험이 없고, 수집된 문헌 2편도 헤르페스 바이러스와 무관한 질환을 다룹니다. 모델 점수만으로는 신규 적응증 추진을 뒷받침하기 어렵습니다.

**진행하려면 필요한 것:**
- 점상 상피성 각결막염에서 acyclovir를 직접 평가한 임상 또는 전임상 근거
- 이 질환의 원인(바이러스성 여부)과 acyclovir 기전의 연관성 검토
- 상세한 작용 기전 데이터 확보
- 허가사항의 경고 및 금기 정보 확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

