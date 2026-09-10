---
layout: default
title: Fluorouracil
parent: 僅模型預測 (L5)
nav_order: 333
evidence_level: L5
indication_count: 10
---

# Fluorouracil
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

# Fluorouracil: 적응증 정보 없음에서 보트리오이드형 배아성 횡문근육종(질)으로

## 한 문장 요약

Fluorouracil(5-FU, DrugBank ID DB00544)은 대표적인 세포독성 항암제 계열 성분이지만, 이번 Evidence Pack에는 기존 승인 적응증 및 작용기전(MOA) 정보가 확보되어 있지 않고 한국 내 시판 허가도 없습니다(미상영). TxGNN 모델은 **보트리오이드형 배아성 횡문근육종(질)(Botryoid-type Embryonal Rhabdomyosarcoma of the Vagina)**에 효과가 있을 수 있다고 예측(점수 99.75%)했으나, 이를 뒷받침하는 임상시험이나 문헌은 **현재 0건**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (Evidence Pack에 원 적응증 미기재) |
| 예측 신규 적응증 | 보트리오이드형 배아성 횡문근육종(질) (Botryoid-type Embryonal Rhabdomyosarcoma of the Vagina) |
| TxGNN 예측 점수 | 99.75% (rank 5088/전체) |
| 근거 수준 | L5 (모델 예측만 있음, 실제 연구 없음) |
| 한국 시판 현황 | 미상영 (허가 0건) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 확보되지 않았습니다(Data Gap, High severity). Evidence Pack의 예측 근거(repurposing_rationale)에 따르면, 이 예측은 **TxGNN 지식그래프 임베딩상 다른 육종(sarcoma) 계열 적응증과의 유사성에만 기반**하며, 직접적인 임상적 또는 기전적 지지 자료는 없는 상태입니다.

참고로 같은 Evidence Pack 내 다른 후보(rank 2, rhabdomyosarcoma 전반)에서는 "5-FU는 pyrimidine 유사체/thymidylate synthase 억제제로서 항증식 기전상 소아 육종에 이론적으로 적용 가능하나, 현행 횡문근육종 표준요법(VAC: vincristine/actinomycin D/cyclophosphamide)은 5-FU를 골격으로 하지 않아 기전 연관성은 간접적 추론 수준"이라고 명시되어 있습니다. 즉 순위 1위 적응증에 대해서는 이 정도의 간접적 추론조차 뒷받침할 자료가 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

국내(한국) 허가 정보가 없습니다 (시판 허가 0건, 미상영).

## 세포독성

Evidence Pack 내 다른 예측 항목(rank 8)의 rationale에서 "5-FU는 thymidylate synthase 억제제/세포독성 항대사물질(cytotoxic antimetabolite)"로 명시되어 있어, fluoropyrimidine 계열 세포독성 항암제로 판단됩니다.

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 항암제 (Fluoropyrimidine 계열, thymidylate synthase 억제제) |
| 골수억제 위험 | Evidence Pack 내 rationale에서 "5-FU 골수억제 독성"이 언급되나 정량 데이터는 없음 — 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 데이터 없음 — 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 세포독성 항암제 일반 원칙상 CBC(혈구감별계산 포함), 간신기능 — 상세 프로토콜은 허가사항 참조 |
| 취급 방호 | 세포독성 의약품 취급 규정 준수 필요 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (TFDA 경고/금기 자료는 Blocking 등급 Data Gap으로 미확보, 약물상호작용 조회 결과 "not_found")

## 결론 및 다음 단계

**결정: Hold**

**사유:**
1순위 예측인 보트리오이드형 배아성 횡문근육종(질)은 TxGNN 모델 점수만 존재하고 임상시험·문헌이 전무한 L5 수준이며, 안전성 핵심 정보(TFDA 경고·금기)가 Blocking 등급 Data Gap으로 남아 있어 초기 안전성 평가(S1) 진입 자체가 불가능합니다.

**진행하려면 필요한 것:**
- TFDA(식약처) 경고 및 금기 정보 확보 — 허가사항 PDF 파싱 필요 (DG001, Blocking)
- DrugBank API 등을 통한 작용기전(MOA) 데이터 확보 (DG002, High)
- 1순위 적응증에 대한 전임상/임상 근거 축적 (현재 전무)
- 참고: 동일 Evidence Pack 내 rank 7 "liver sarcoma"는 근거 수준 L3(관찰연구), decision_stage S2로 상대적으로 근거가 두터우나, 관련 임상시험 5건 중 다수가 원발성 간육종이 아닌 대장직장암/HCC 대상(관련성 Grade C)이라 별도 심층 검토가 필요합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

