---
layout: default
title: Isosorbide Mononitrate
parent: 僅模型預測 (L5)
nav_order: 409
evidence_level: L5
indication_count: 10
---

# Isosorbide Mononitrate
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

# Isosorbide mononitrate: 협심증에서 다모증(Hypertrichosis)으로

## 한 문장 요약

Isosorbide mononitrate는 유기 질산염(organic nitrate) 계열 혈관확장제로, 국제적으로는 협심증 등 허혈성 심질환에 사용되어 온 약물입니다(한국 내 시판 정보는 확인되지 않음). TxGNN 모델은 **다모증(Hypertrichosis)**에 효과가 있을 수 있다고 예측했으나, 이를 뒷받침하는 임상시험이나 문헌은 전혀 없으며, 자체 기전 분석에서도 실제 약리학적 연관성이 확인되지 않았습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 허가 정보 없음(미출시). 국제적으로는 협심증(허혈성 심질환) 치료제로 알려짐 — 본 근거 팩에는 미기재 |
| 예측 신규 적응증 | 다모증 (Hypertrichosis) |
| TxGNN 예측 점수 | 99.995% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

근거 팩의 `repurposing_rationale`에 따르면 Isosorbide mononitrate는 유기 질산염(organic nitrate) 계열 NO donor로, 체내에서 대사되어 NO를 방출하고 가용성 구아닐산고리화효소(sGC)를 활성화해 cGMP를 증가시켜 혈관평활근을 이완시키는 기전을 가집니다(원본 MOA 필드는 데이터 갭이나, 예측 근거 텍스트에서 확인됨).

다모증은 모낭 성장 주기 조절과 관련된 질환으로, 이미 알려진 발모 치료제 minoxidil은 KATP channel opener 기전을 통해 작용합니다. 이는 Isosorbide mononitrate의 NO-cGMP 경로와는 표적이 다르며, 근거 팩 자체 분석에서도 "높은 TxGNN 점수는 지식그래프 임베딩 공간의 유사성 아티팩트(false positive)로 판단되며, 실제 약리학적 연관성은 확인되지 않는다"고 명시하고 있습니다. 즉 이 예측은 기전상 타당성이 낮은 것으로 평가됩니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 점수는 99.995%로 높지만, 이를 지지하는 임상시험이나 문헌 근거가 전무하고, 자체 기전 분석에서도 다모증과의 생물학적 연관성이 확인되지 않아(지식그래프 임베딩 유사성 아티팩트로 추정) 진행 근거가 부족합니다.

**진행하려면 필요한 것:**
- 상세한 작용기전(MOA) 데이터 확보 (data gap: DG002, High)
- 식약처(한국) 허가사항 경고·금기 정보 확보 — 한국 미출시로 현재 확인 불가 (data gap: DG001, Blocking)
- 다모증에 대한 전임상 또는 기전 연구 확보
- **참고**: 동일 예측 후보군 중 10위 폐동맥성고혈압(Pulmonary Arterial Hypertension)은 NO-cGMP 경로가 PAH 표준 치료 표적(riociguat, PDE5 억제제 등)과 중첩되어 기전적 타당성이 상대적으로 높고, 6편의 문헌(가설 생성 수준, L3)이 확인됩니다. 이 후보에 대해서는 별도 평가를 권장합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

