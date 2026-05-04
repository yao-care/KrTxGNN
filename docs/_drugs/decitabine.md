---
layout: default
title: Decitabine
parent: 僅模型預測 (L5)
nav_order: 199
evidence_level: L5
indication_count: 1
---

# Decitabine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# DECITABINE: 골수이형성증후군에서 소아 불응성 혈구감소증으로

---

## 한 문장 요약

Decitabine은 DNA 메틸화를 억제하는 항암제로, 국제적으로 성인 골수이형성증후군(MDS) 및 급성골수성백혈병(AML) 치료에 사용되고 있습니다. TxGNN 모델은 **소아 불응성 혈구감소증(Refractory Cytopenia of Childhood, RCC)**에 효과가 있을 수 있다고 예측하며, 현재 **0건의 임상시험**과 **1편의 문헌**이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 골수이형성증후군(MDS), 급성골수성백혈병(AML) (국제 허가 기준) |
| 예측 신규 적응증 | 소아 불응성 혈구감소증 (Refractory Cytopenia of Childhood) |
| TxGNN 예측 점수 | 99.03% |
| 근거 수준 | L3 |
| 한국 시판 현황 | ✗ 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 DrugBank에서 Decitabine의 상세 작용 기전(MOA) 데이터가 확인되지 않았습니다. 그러나 알려진 정보에 따르면, Decitabine은 **DNA 메틸전달효소 억제제(DNMTi)** 계열 약물로서, DNA 과메틸화를 역전시켜 비정상적으로 억제된 종양 억제 유전자 및 조혈 분화 유전자를 재활성화하는 기전을 가집니다.

소아 불응성 혈구감소증(RCC)은 소아 MDS의 주요 아형으로, 발병 기전에 조혈모세포의 비정상적 후성유전학적 조절(이상 과메틸화)이 핵심적으로 관여합니다. 이는 Decitabine의 작용 표적과 기전적으로 직접 부합합니다. 또한 RCC 환자는 동종조혈모세포이식(allo-HSCT) 전 교량 치료(bridging therapy)가 필요한 경우가 많으며, 저강도·저골수억제 특성을 지닌 Decitabine은 소아 환자의 취약한 골수 예비능을 보호하면서도 질환을 효과적으로 조절하는 데 적합합니다.

TxGNN 예측 점수 99.03%는 이 기전적 연관성을 강력히 뒷받침합니다. 다만, RCC 특이적 임상시험이 현재 전무하고 지지 문헌이 후향적 코호트 연구 1편에 그치므로, 임상 근거의 추가 확보가 전제 조건입니다.

---

## 임상시험 근거

현재 소아 불응성 혈구감소증(RCC) 대상 Decitabine 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|------|------|------|---------|
| [35624441](https://pubmed.ncbi.nlm.nih.gov/35624441/) | 2022 | 후향적 코호트 | BMC Pediatrics | 소아 MDS 환자에서 decitabine 병합 최소골수억제요법(DAC+MMR)을 allo-HSCT 전 교량 치료로 사용한 단일기관 10년 경험 보고; 유효성 및 안전성 데이터 포함 |

---

## 한국 시판 정보

한국 내 Decitabine 허가 제품이 없습니다 (허가증 0건).

---

## 세포독성

Decitabine은 azanucleoside 계열의 항종양 세포독성 약물입니다.

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (DNA 저메틸화제, Azanucleosides 계열) |
| 골수억제 위험 | **고위험** — 호중구감소증, 혈소판감소증, 빈혈이 주요 용량 제한 독성 |
| 구토 유발성 등급 | 저~중등도 |
| 모니터링 항목 | CBC (분류 포함), 간기능(ALT/AST/빌리루빈), 신기능(크레아티닌), 전해질 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 (조제 시 생물안전 캐비닛 사용, 밀폐형 주사 시스템 권고) |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 점수(99.03%)와 후성유전학적 기전 연관성은 강력하나, RCC 특이적 임상시험이 전무하고 지지 문헌이 후향적 코호트 1편에 그쳐 현 시점에서 본격적인 재창출 개발 착수는 이릅니다. 한국 내 미허가 상태이므로 규제 경로 검토도 병행해야 합니다.

**진행하려면 필요한 것:**
- RCC 특이적 Decitabine Phase 1/2 임상시험 프로토콜 설계 및 등록
- 안전성 정보 확보: FDA/EMA 허가 라벨 전문 검토 (경고, 금기, 특수 집단 주의사항)
- 상세 작용 기전(MOA) 데이터 확보 (DrugBank API 재조회, 문헌 검색)
- 소아 약동학/약력학(PK/PD) 데이터 검토 (성인 용량 체계와의 차이 확인)
- 기존 면역억제 요법 대비 Decitabine 교량 치료의 유효성·안전성 비교 근거 마련
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

