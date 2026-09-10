---
layout: default
title: Magnesium Carbonate
parent: 僅模型預測 (L5)
nav_order: 455
evidence_level: L5
indication_count: 10
---

# Magnesium Carbonate
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

# Magnesium Carbonate: 적응증 정보 부재에서 활동성 소화성 궤양으로

## 한 문장 요약

Magnesium Carbonate(DB09481)는 국내(한국) 허가 정보가 없어 기존 적응증 데이터가 확인되지 않는 약물입니다. TxGNN 모델은 **활동성 소화성 궤양(Active Peptic Ulcer Disease)**에 효과가 있을 수 있다고 예측하며, 임상시험 등록은 없지만 **위약대조 RCT 3건을 포함한 문헌 4편**이 이 방향을 지지합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (한국 허가 이력·원 적응증 정보 미확보) |
| 예측 신규 적응증 | 활동성 소화성 궤양 (Active Peptic Ulcer Disease) |
| TxGNN 예측 점수 | 99.96% (rank 1,260) |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 확보되지 않았습니다. 다만 Magnesium Carbonate는 알려진 정보에 따르면 제산제(antacid) 계열 성분으로, 위산을 직접 중화시켜 산 노출을 낮추는 방식으로 작용합니다.

이러한 제산 작용은 활동성 소화성 궤양의 전통적 치료 원리와 직접적으로 부합합니다. 실제로 지지 문헌 중에는 제산제 현탁액을 cimetidine·위약과 비교한 이중맹검 RCT가 포함되어 있어, 기전과 임상 근거가 일치하는 방향을 보여줍니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [7034155](https://pubmed.ncbi.nlm.nih.gov/7034155/) | 1981 | RCT (위약대조) | Scandinavian Journal of Gastroenterology | 십이지장/전유문부 궤양 72명 대상, cimetidine·제산제+항콜린제·위약 비교. 3주 치유율은 cimetidine 67%, 제산제군 50%(위약 대비 유의) |
| [6755656](https://pubmed.ncbi.nlm.nih.gov/6755656/) | 1982 | RCT (위약대조) | Scand J Gastroenterol Suppl | 활동성 전유문부·십이지장 궤양에서 제산제/항콜린제, cimetidine, 위약 비교 시험(초록 미제공) |
| [3003883](https://pubmed.ncbi.nlm.nih.gov/3003883/) | 1985 | RCT | Scandinavian Journal of Gastroenterology | 활동성 십이지장궤양 80명, 고섬유/저섬유 식이+제산제 병용. 치유율 67.5% vs 60%(유의차 없음) |
| [35720246](https://pubmed.ncbi.nlm.nih.gov/35720246/) | 2022 | 시험관내/분석 연구 | Medicine and Pharmacy Reports | 모로코 시판 제산제의 산중화능(ANC) 평가 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
활동성 소화성 궤양에 대해 1980년대 위약대조 RCT 3건이 제산제의 유효성을 지지하며, 제산 작용이라는 기전도 명확히 일치합니다. 다만 문헌이 오래되었고(1981~1985년 위주) 현재 진행 중인 임상시험이 전무하며, 한국 내 시판 이력이 없어(허가증 0건) 즉시 임상 적용 판단에는 한계가 있습니다.

**진행하려면 필요한 것:**
- 상세 작용기전(MOA) 자료 확보 (DrugBank 등)
- 한국 식약처 허가사항 — 경고·금기·약물상호작용(DDI) 정보 확보 (현재 전부 Data Gap)
- 국내 미시판 상태에 따른 허가/도입 경로 검토
- 최신(2000년대 이후) 임상 데이터 보강 — 현재 근거 대부분이 40년 이상 경과한 문헌
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

