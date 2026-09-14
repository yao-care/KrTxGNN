---
layout: default
title: Siltuximab
parent: 僅模型預測 (L5)
nav_order: 636
evidence_level: L5
indication_count: 10
---

# Siltuximab
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

# Siltuximab: 특발성 다중심성 캐슬만병(iMCD)에서 TAFRO 증후군으로

## 한 문장 요약

Siltuximab은 IL-6을 표적으로 하는 키메라 단클론항체로, 해외에서는 HIV/HHV-8 음성 특발성 다중심성 캐슬만병(iMCD) 치료제로 승인되어 있으나 한국에는 아직 출시되지 않았습니다.
TxGNN 모델은 10개 신규 적응증을 예측했는데, 이 중 실제 근거가 확인된 것은 **TAFRO 증후군**과 **Kaposi 육종** 2건뿐이며, 나머지 8건은 문헌·임상시험 근거가 전혀 없는 순수 모델 예측(L5)입니다.
근거 수준이 가장 높은 **TAFRO 증후군**에 대해서는 **19편의 문헌**(RCT 1건, 가이드라인/리뷰 다수, TAFRO 특이적 증례보고 포함)이 IL-6 차단 기전의 확장 가능성을 뒷받침합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 특발성 다중심성 캐슬만병(iMCD) — 문헌상 확인된 해외 승인 적응증(한국 허가 데이터 없음) |
| 예측 신규 적응증 | TAFRO 증후군 (TAFRO syndrome) |
| TxGNN 예측 점수 | 98.79% |
| 근거 수준 | L3 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

DrugBank의 공식 작용기전(MOA) 필드는 현재 비어 있습니다. 다만 근거로 수집된 다수의 문헌(PMID 24958337, 25601959, 26394632 등)에서 공통적으로 확인되는 바, Siltuximab은 **인간-마우스 키메라 IgG1κ 단클론항체로 IL-6에 직접 결합하여 IL-6 신호전달을 차단**하는 기전으로 작용합니다.

TAFRO 증후군(혈소판감소증·전신부종·발열·골수섬유화·장기비대)은 다수의 최신 문헌(PMID 38029058, 38927484, 34720942)에서 **특발성 다중심성 캐슬만병(iMCD)의 중증 아형 또는 근연 질환군**으로 다뤄지며, 두 질환 모두 병태생리학적으로 IL-6 과다분비가 핵심 원인으로 지목됩니다. Siltuximab은 이미 iMCD에서 위약대조 RCT(PMID 25042199)로 유효성이 입증되어 FDA·EU 승인을 받은 약제이므로, 동일 기전 스펙트럼 내 질환인 TAFRO 증후군으로의 적응증 확장은 기전상 타당성이 있습니다. 실제로 다수의 TAFRO 증례에서 empiric하게 anti-IL-6 요법이 사용되고 있다는 점(PMID 34720942, 32564425)이 이를 뒷받침합니다.

---

## 임상시험 근거

현재 TAFRO 증후군을 대상으로 한 등록된 관련 임상시험이 없습니다.

> 참고: 본 Evidence Pack의 다른 예측 적응증(Kaposi 육종, rank 5)에 매칭된 NCT02796859는 실제로는 조현병 보조치료 시험으로, 데이터 매칭 오류로 판단되어 제외했습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [25042199](https://pubmed.ncbi.nlm.nih.gov/25042199/) | 2014 | RCT | Lancet Oncology | iMCD 환자 대상 siltuximab 위약대조 RCT, IL-6 과다분비가 질환 핵심 기전임을 확인하고 유효성 입증 |
| [30181172](https://pubmed.ncbi.nlm.nih.gov/30181172/) | 2018 | Consensus Guideline | Blood | iMCD 국제 합의 치료 가이드라인, siltuximab을 1차 치료로 권고 |
| [38927484](https://pubmed.ncbi.nlm.nih.gov/38927484/) | 2024 | Review/Guidance | Biomedicines | TAFRO 증후군 진단·치료 가이드라인, anti-IL-6 요법 위치 정리 |
| [38029058](https://pubmed.ncbi.nlm.nih.gov/38029058/) | 2023 | Review | J Medical Cases | TAFRO 증후군 단계별 치료 알고리즘, IL-6 억제제 조기 투입 권고 |
| [34720942](https://pubmed.ncbi.nlm.nih.gov/34720942/) | 2021 | Case Report | Case Rep Oncology | TAFRO 증후군에서 iMCD 진단이 모호한 상태로 경험적 anti-IL-6 치료 시행 |
| [36652167](https://pubmed.ncbi.nlm.nih.gov/36652167/) | 2023 | Case Report + Review | J Nephrology | TAFRO 증후군에서 siltuximab 단독요법으로 신장병증 포함 관해 달성 |
| [32564425](https://pubmed.ncbi.nlm.nih.gov/32564425/) | 2020 | Case Report | Eur J Haematology | TAFRO 증후군 1차 치료로 siltuximab+rituximab 병용 사례 |
| [24958337](https://pubmed.ncbi.nlm.nih.gov/24958337/) | 2014 | Review | Drugs | Siltuximab의 iMCD 최초 글로벌 승인 경과 및 개발 배경 |
| [41345785](https://pubmed.ncbi.nlm.nih.gov/41345785/) | 2025 | Meta-analysis | Ann Hematology | iMCD에서 siltuximab 단독요법이 rituximab 기반 요법 대비 무진행생존 우위 |
| [36219975](https://pubmed.ncbi.nlm.nih.gov/36219975/) | 2022 | Review | Oncol Res Treat | 캐슬만병 스펙트럼(iMCD/TAFRO 포함) 최신 치료 동향 정리 |

---

## 한국 시판 정보

Siltuximab은 한국에서 허가된 제품이 없으며(허가증 0건), 현재 미출시 상태입니다. 국내 도입을 위해서는 별도의 신약 허가 절차가 필요합니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> ⚠️ 현재 TFDA 수준의 허가 경고/금기사항 데이터가 확보되지 않아(DG001, Blocking) 안전성 초기 평가(S1) 단계로 진입할 수 없는 상태입니다.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
TAFRO 증후군은 iMCD의 중증 아형으로 병리기전이 공유되며, iMCD에 대한 RCT(PMID 25042199)와 다수의 TAFRO 특이적 증례·가이드라인이 IL-6 차단 요법의 확장 근거를 제공합니다(L3, S2). 다만 나머지 9개 예측 적응증은 근거가 전무한 순수 모델 예측(L5, Hold)이므로 이번 보고서는 TAFRO 증후군에 한정하여 진행을 권고합니다.

**진행하려면 필요한 것:**
- TFDA(또는 FDA/EMA) 원본 허가 라벨의 경고·금기사항 확보 (DG001, Blocking — S1 안전성 초평가 선행조건)
- DrugBank API를 통한 공식 MOA 데이터 확보 (DG002)
- 한국 내 도입 시 CRIS 등록 임상시험 유무 확인 및 국내 허가 경로 검토
- TAFRO 증후군 진단기준 표준화 여부 확인 (질환 정의가 상대적으로 최근 정립되어 진단 이질성 존재)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

