---
layout: default
title: Flubendazole
parent: 僅模型預測 (L5)
nav_order: 326
evidence_level: L5
indication_count: 10
---

# Flubendazole
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

# Flubendazole: 구충제(기생충 감염 치료)에서 방광암종(Urinary Bladder Carcinoma)으로

## 한 문장 요약

Flubendazole은 benzimidazole계 구충제로 알려져 있으나, 본 평가팩에는 정확한 기존 적응증 데이터가 없습니다(Data Gap).
TxGNN 모델은 **방광암종(Urinary Bladder Carcinoma)**에 효과가 있을 수 있다고 예측하지만(예측 점수 99.99%),
현재 이를 뒷받침하는 **임상시험이나 문헌은 전혀 없어** 순수 모델 예측 단계에 머물러 있습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (구충제/benzimidazole계로 알려져 있으나 evidence pack에는 미기재) |
| 예측 신규 적응증 | 방광암종 (Urinary Bladder Carcinoma) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미상장 (시판되지 않음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 flubendazole 자체의 상세 작용기전(MOA) 데이터는 확보되지 않았습니다. 다만 flubendazole이 속한 benzimidazole계 구충제(mebendazole, fenbendazole 등)는 β-tubulin에 결합해 미세관(microtubule) 중합을 억제함으로써 암세포의 유사분열을 정지시키고 세포자멸사를 유도하는 기전이 널리 보고되어 있습니다. 이는 이 계열 약물 전반에 대한 잘 알려진 노약재창출(repurposing) 가설입니다.

다만 이 가설은 flubendazole 본인에 대한 직접 증거가 아니라 동일 계열 약물로부터의 유추이며, 본 예측 순위 1위(urinary bladder carcinoma)에 대해서는 관련 임상시험이나 문헌이 전혀 확인되지 않았습니다. 참고로 evidence pack 내 2순위 예측(urinary bladder neoplasm)에서는 동일 계열 약물인 fenbendazole을 이용한 방광암 전임상 병용요법 문헌 1건이 확인되어, benzimidazole계 전반의 항암 가능성을 간접적으로 뒷받침하고 있습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 한국 시판 정보

현재 한국에 등록된 허가 제품이 없습니다 (미상장, 허가증 0건).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 점수는 99.99%로 매우 높지만, 예측 순위 1위 적응증(방광암종)에 대해 실질적인 임상시험·문헌 근거가 전혀 없고(L5), flubendazole 자체의 작용기전과 안전성 데이터도 결측 상태입니다. 현 단계에서는 규제기관 초기 안전성 검토(S1) 진입이 불가능합니다.

**진행하려면 필요한 것:**
- 규제기관 허가사항(경고·금기 등 첨부문서) 확보 — 안전성 초기 평가(S1) 진입에 필수 (Blocking)
- flubendazole의 작용기전(MOA) 데이터 확보 — DrugBank 등에서 재조회 필요 (High)
- flubendazole 자체(또는 동일 계열 fenbendazole/mebendazole)의 방광암 관련 전임상·임상 증거 추가 확보
- 기존 적응증(원 승인 정보) 확인 — 현재 데이터 공백으로 기전 연관성 분석 제한
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

