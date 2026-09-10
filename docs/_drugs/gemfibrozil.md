---
layout: default
title: Gemfibrozil
parent: 僅模型預測 (L5)
nav_order: 345
evidence_level: L5
indication_count: 10
---

# Gemfibrozil
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

# Gemfibrozil: 고지혈증에서 류마티스 관절염으로

## 한 문장 요약

Gemfibrozil은 PPAR-α 작용제 계열의 지질 조절제(fibrate)로, 원래 고중성지방혈증 등 고지혈증 치료에 사용되어 온 약물입니다.
TxGNN 모델은 **류마티스 관절염(Rheumatoid Arthritis)**에 효과가 있을 수 있다고 예측하며,
현재 관련 임상시험은 없고 **4편의 전임상/증례 수준 문헌**만이 이 방향을 간접적으로 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 고지혈증(고중성지방혈증) 계열 — 대만 정식 허가 기록 없음(TFDA 미상) |
| 예측 신규 적응증 | 류마티스 관절염 (Rheumatoid Arthritis) |
| TxGNN 예측 점수 | 99.90% |
| 근거 수준 | L4 |
| 대만 시판 현황 | 미상 (未上市) |
| 허가증 수 | 0건 |
| 권장 결정 | Research Question (추가 검증 필요) |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 제공되지 않았습니다(Data Gap). 다만 근거 자료 내 기전 분석에 따르면 Gemfibrozil은 **PPAR-α 작용제**로, PPAR-α 활성화는 NF-κB 경로를 억제하고 TNF-α, IL-6 등 염증 매개물질의 발현을 낮추는 것으로 알려져 있습니다. 이는 류마티스 관절염의 활막 염증 병리와 이론적으로 연결될 수 있는 지점입니다.

다만 이 기전 연관성은 gemfibrozil 자체를 직접 겨냥한 것이 아니라, 같은 fibrate 계열 약물(bezafibrate 등)의 동물모델 연구에서 도출된 유추 근거가 대부분입니다. 즉 "약물 계열 수준"에서의 개연성은 있으나, gemfibrozil이라는 개별 성분에 특정된 직접 증거는 아직 약합니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [30074417](https://pubmed.ncbi.nlm.nih.gov/30074417/) | 2019 | 전임상 (Rat AIA 모델) | Modern Rheumatology | Gemfibrozil(30mg/kg) + 저용량 prednisolone 병용이 adjuvant 유발 관절염 랫드 모델에서 고용량 스테로이드 단독요법과 유사한 관리 효과를 보임 |
| [41207105](https://pubmed.ncbi.nlm.nih.gov/41207105/) | 2026 | 전임상 (동물모델, 동계열 약물 bezafibrate) | International Immunopharmacology | Pan-PPAR 작용제 bezafibrate가 PPAR-γ 의존적 기전을 통해 실험적 류마티스 관절염의 염증 경로를 완화시킴 (gemfibrozil 자체 데이터 아님) |
| [20083653](https://pubmed.ncbi.nlm.nih.gov/20083653/) | 2010 | 전임상 (EAE 모델, RA 아님) | Journal of Immunology | Myelin basic protein priming이 산화질소를 매개로 T세포 Foxp3 발현을 낮춤; 자가면역 조절 기전 연구로 RA와 간접적으로만 관련 |
| [18039017](https://pubmed.ncbi.nlm.nih.gov/18039017/) | 2007 | 증례보고 | American Journal of Clinical Dermatology | 수장홍반(Palmar erythema)의 원인 고찰 — RA와의 직접 연관성은 낮음 |

---

## 대만 시판 정보

현재 대만에 시판 중인 허가 정보가 없습니다 (未上市, 허가증 0건).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Research Question (추가 검증 필요, Hold에 준함)**

**사유:**
- Gemfibrozil과 류마티스 관절염을 직접 연결하는 임상시험은 전무하며, 문헌 근거도 gemfibrozil 자체를 다룬 것은 1건(랫드 모델)뿐이고 나머지는 동계열 약물 또는 무관한 질환 모델입니다.
- PPAR-α 매개 항염 기전은 이론적 개연성은 있으나, 이는 약물 계열 수준의 유추이지 gemfibrozil 고유의 직접 증거가 아닙니다.

**진행하려면 필요한 것:**
- Gemfibrozil 단독 성분에 대한 RA 관련 전임상 또는 초기 임상 데이터 확보
- TFDA 仿單 경고/금기사항 확보 (현재 Blocking 등급 Data Gap)
- 작용기전(MOA) 상세 데이터 확보 (DrugBank API 조회)
- 대만 시판 여부 및 허가 현황 재확인 (현재 미상 상태)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

