---
layout: default
title: Trastuzumab Emtansine
parent: 모델 예측만 (L5)
nav_order: 756
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Trastuzumab Emtansine: 예측 신규 적응증 정상 유방형 유방암 (normal breast-like subtype of breast carcinoma) (근거 수준 L5). 기존 적응증: HER2 양성 유방암 (허가 문서는 링크로만 확인되어 본문 확인 불가)"
monitor_inn: "Trastuzumab emtansine"
predicted_indications: ["synovium cancer", "tenosynovial giant cell tumor", "tenosynovial giant cell tumor, localized type", "malignant giant cell tumor", "human herpesvirus 8-related tumor", "ectomesenchymoma"]
---

# Trastuzumab Emtansine
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

## Trastuzumab emtansine: HER2 양성 유방암에서 정상 유방형(normal breast-like) 유방암으로
{: .text-alpha }

## 한 문장 요약

Trastuzumab emtansine(T-DM1)은 HER2를 표적으로 하는 항체-약물 접합체(ADC)로, 원래 HER2 양성 유방암 치료에 사용되었습니다.
TxGNN 모델은 **정상 유방형 유방암(normal breast-like subtype of breast carcinoma)**에 효과가 있을 수 있다고 예측하지만, 이 예측을 뒷받침하는 **임상시험은 0건**, **문헌도 0편**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | HER2 양성 유방암 (허가 문서는 링크로만 확인되어 본문 확인 불가) |
| 예측 신규 적응증 | 정상 유방형 유방암 (normal breast-like subtype of breast carcinoma) |
| TxGNN 예측 점수 | 99.82% |
| 근거 수준 | L5 (모델 예측만 있음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 T-DM1은 HER2를 표적으로 하는 항체-약물 접합체로, 미세소관 억제제인 DM1을 HER2 발현 암세포에 전달합니다. HER2 양성 유방암에서의 효능이 입증되어 있어, 같은 유방암 범주의 다른 아형에도 이론상 적용을 검토할 수 있습니다.

다만 기전상 근거는 약합니다. 정상 유방형 아형은 일반적으로 HER2 음성이고 HER2 의존성이 낮습니다. 따라서 T-DM1의 효과를 기대할 기전적 이유가 뚜렷하지 않습니다. 높은 TxGNN 점수는 유방암 전반과의 네트워크상 근접성에서 비롯된 것으로 보이며, 이를 지지하는 임상시험이나 문헌은 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201400326 | 캐싸일라주100밀리그램(트라스투주맙엠탄신) | 동결건조 주사제 (주용제 첨가 후 사용) | [허가 문서 링크](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201400326/EE) 참조 |
| 201400327 | 캐싸일라주160밀리그램(트라스투주맙엠탄신) | 동결건조 주사제 (주용제 첨가 후 사용) | [허가 문서 링크](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201400327/EE) 참조 |

두 제품 모두 (주)한국로슈가 제조·판매하는 단일제이며, 현재 유효한 허가입니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 항체-약물 접합체(ADC). 미세소관 억제 세포독성 페이로드(DM1)를 포함하는 표적 항종양제 |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 세포독성 약물 취급 규정에 따른 조제·취급 여부를 허가사항에서 확인해야 합니다 |

## 안전성 고려사항

- **약물 상호작용**: 이번에 확인된 상호작용은 총 100건이며, 그중 일부만 표시되어 있습니다. 확인된 항목 중 **Major(주요)** 등급은 다음과 같습니다.
  - Acetylsalicylic acid
  - Deferasirox
  - Abciximab
  - Apixaban
  - Argatroban
  - Betrixaban
  - Bivalirudin
  - Cangrelor
  - Caplacizumab
  - Cilostazol
  
  대부분 항응고제·항혈소판제 계열로, 출혈 위험과 관련해 주의가 필요합니다.
- **Moderate(중등도)** 등급으로는 Clarithromycin, Metronidazole, Tinidazole, Naltrexone, Rosuvastatin, Simvastatin, Cobicistat, Fenfluramine, Dexfenfluramine, Sibutramine 등이 확인되었습니다.

주요 경고와 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
정상 유방형 아형은 일반적으로 HER2 음성이어서 T-DM1의 작용 기전과 맞지 않습니다. 임상시험과 문헌도 전혀 없어 근거는 모델 예측(L5)뿐이므로, 현 단계에서는 보류가 적절합니다.

**진행하려면 필요한 것:**
- 해당 아형에서 HER2 발현 또는 증폭이 확인되는 환자군이 있는지 확인하고, 이를 뒷받침하는 전임상 또는 임상 근거 확보
- 허가사항(국내 허가 문서)의 적응증, 경고, 금기 사항 확인 및 정리
- 상세한 약물 작용 기전(MOA) 데이터 보완
- 참고: 같은 예측 목록의 "프로게스테론 수용체 양성/음성 유방암", "루미날 A/B 유방종양"은 기존 HER2 양성 적응증과 상당 부분 겹치는 하위 집단입니다. 이들은 진정한 재창출이라기보다 기존 적응증의 하위 범주로 보는 것이 타당하며, 별도 평가가 필요합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

