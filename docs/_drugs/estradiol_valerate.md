---
layout: default
title: Estradiol Valerate
parent: 僅模型預測 (L5)
nav_order: 252
evidence_level: L5
indication_count: 10
---

# Estradiol Valerate
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

# Estradiol Valerate: 폐경기 호르몬 대체요법에서 여성 Fragile X 증후군 보인자 증상으로

## 한 문장 요약

Estradiol Valerate(EV)는 17β-에스트라디올의 합성 에스테르로, 전 세계적으로 폐경기 호르몬 대체요법(HRT) 및 원발성 난소 기능 부전(POI) 치료에 사용되는 합성 에스트로겐입니다.
TxGNN 모델은 **FMR1 전돌연변이 여성 보인자의 증상성 Fragile X 증후군(Symptomatic Form of Fragile X Syndrome in Female Carrier)**에 효과가 있을 수 있다고 예측하며,
현재 이 적응증에 대해 **임상시험 0건, 문헌 0편**으로 예측을 직접 뒷받침하는 근거는 없습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 허가 이력 없음 (전 세계적으로 폐경기 HRT, POI에 사용) |
| 예측 신규 적응증 | 여성 보인자의 증상성 Fragile X 증후군 (Symptomatic Form of Fragile X Syndrome in Female Carrier) |
| TxGNN 예측 점수 | 99.94% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 수집되지 않았습니다. 알려진 약리학 정보에 따르면, Estradiol Valerate는 경구 투여 후 장관 및 간에서 신속히 가수분해되어 활성 대사물인 17β-에스트라디올을 방출하며, 에스트로겐 수용체(ERα, ERβ)에 결합해 생리적 에스트로겐 효과를 발휘합니다. 전 세계적으로 EV를 포함한 HRT 제제(Progynova, Cyclacur 등)는 난소 기능 저하 또는 POI 관련 에스트로겐 결핍 증상 치료에 광범위하게 사용됩니다.

FMR1 유전자 전돌연변이(premutation, 55–200 CGG 반복)를 보유한 여성 보인자는 Fragile X 관련 원발성 난소 기능 부전(FXPOI)을 높은 빈도로 경험하며, 이로 인한 조기 에스트로겐 결핍이 유발됩니다. 이론적으로 EV의 활성 대사물인 에스트라디올은 FXPOI에 따른 에스트로겐 부족을 호르몬 대체 방식으로 보충할 수 있습니다. TxGNN의 고득점(99.94%)은 지식 그래프 내 **FMR1 → 난소 기능 부전 → 에스트로겐 축**이라는 네트워크 인접성에서 비롯된 계산적 예측으로 판단됩니다.

다만, 이 예측의 기전적 연결은 FXPOI에 따른 **호르몬 대체**라는 간접적 측면에만 해당합니다. Fragile X 증후군의 핵심인 신경인지 증상(지적 장애, 언어 발달 지연, 자폐 스펙트럼 특성) 자체를 에스트라디올이 개선한다는 직접적 생물학적 근거는 현재 제시되지 않으며, 관련 임상 연구도 전무합니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 한국 시판 정보

현재 한국에 등록된 허가 이력이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 점수가 99.94%로 높지만, 여성 Fragile X 증후군 보인자를 대상으로 EV의 효능을 직접 평가한 임상시험 및 문헌 근거가 전무합니다(L5). 예측 기전은 FXPOI로 인한 에스트로겐 결핍의 호르몬 보충이라는 간접 경로에 기반할 뿐이며, Fragile X 핵심 증상에 대한 치료 가능성은 아직 입증되지 않았습니다.

**진행하려면 필요한 것:**
- 상세한 약물 작용 기전(MOA) 데이터 확보 (DrugBank API 조회)
- 한국 MFDS 허가사항 확인 — 안전성 경고·금기 포함 (현재 허가 이력 없음으로 인해 안전성 데이터 전무)
- FXPOI 여성에서의 에스트라디올 보충 효과에 관한 전향적 파일럿 연구 문헌 탐색
- Fragile X 증후군 여성 보인자 대상 표적 임상시험 설계 가능성 검토

> **⚠️ 연구 참고용 면책 고지**: 본 보고서는 TxGNN 모델의 계산 예측에 기반한 연구 참고 자료이며, 의료 조언을 구성하지 않습니다. 모든 약물 재창출 후보는 임상 검증을 거쳐야 합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

