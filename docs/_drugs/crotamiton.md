---
layout: default
title: Crotamiton
parent: 僅模型預測 (L5)
nav_order: 187
evidence_level: L5
indication_count: 10
---

# Crotamiton
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

# Crotamiton: 옴 및 소양증 치료에서 털진드기증으로

## 한 문장 요약

Crotamiton은 옴(scabies) 및 소양증 치료에 사용되어 온 외부기생충 구제약(ectoparasiticide)입니다.
TxGNN 모델은 **털진드기증(Trombiculiasis)**에 효과가 있을 수 있다고 예측하며,
현재 임상시험 및 문헌 근거는 아직 없으나, **기전 유사성에 기반한 근거 수준 L4**로 평가됩니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 옴(Scabies), 소양증 — 국내 미허가, 알려진 약리 효능 기준 |
| 예측 신규 적응증 | 털진드기증 (Trombiculiasis) |
| TxGNN 예측 점수 | 96.24% |
| 근거 수준 | L4 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, Crotamiton은 외부기생충 구제약(ectoparasiticide)이자 소양 완화제(antipruritic)로, 옴(scabies)을 유발하는 **Sarcoptes scabiei** 진드기에 대한 살충 효과가 확인되어 있습니다.

털진드기(Trombicula) 유충은 Sarcoptes scabiei와 동일한 분류군인 **거미강 진드기목(Acari)**에 속합니다. 같은 분류군 내에서 Crotamiton의 진드기 살충 기전이 유사하게 작용할 생물학적 근거가 존재하며, 이는 단순한 모델 예측을 넘어 기전 타당성(mechanistic plausibility)을 갖춘 재창출 후보임을 시사합니다.

나아가, Crotamiton의 소양 완화 특성은 털진드기 유충 흡혈 후 발생하는 극심한 소양감과 피부 반응에 대한 증상 치료 효과도 기대할 수 있어, **기생충 구제 + 증상 완화**의 이중 치료 가치가 예상됩니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
Crotamiton의 진드기 살충 기전과 소양 완화 효과는 털진드기증에 대한 생물학적 타당성을 제공합니다. 다만 임상 근거가 전무하고 국내 미허가 약물이므로, 단계적 전임상·임상 검증이 선행되어야 합니다.

**진행하려면 필요한 것:**
- 상세 작용 기전(MOA) 데이터 확보 (DrugBank API 조회)
- 털진드기 동물 모델 또는 in vitro 전임상 연구 설계
- 안전성 허가사항 전문 확보 (경고, 금기, 이상반응 — TFDA 仿單 PDF 파싱)
- 국내 식약처(MFDS) 허가 가능성 및 시판 경로 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

