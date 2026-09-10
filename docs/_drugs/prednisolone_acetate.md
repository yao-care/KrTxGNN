---
layout: default
title: Prednisolone Acetate
parent: 僅模型預測 (L5)
nav_order: 573
evidence_level: L5
indication_count: 10
---

# Prednisolone Acetate
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

# Prednisolone Acetate: 안과용 코르티코스테로이드에서 기생충성 결막염(Parasitic Conjunctivitis)으로

## 한 문장 요약

Prednisolone Acetate(DrugBank DB15566)는 국소 안과용 코르티코스테로이드 계열 약물로, 현재 한국에는 허가된 제품이 없습니다.
TxGNN 모델은 **기생충성 결막염(Parasitic Conjunctivitis)**에 효과가 있을 것으로 예측했으나(TxGNN 점수 **99.74%**),
실제로는 **사례보고 1편**만 확인되고 기전상으로도 치료 목표와 상충되는 부분이 있어 근거 수준이 낮습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 등재된 정보 없음 (한국 허가 이력 없음) |
| 예측 신규 적응증 | 기생충성 결막염 (Parasitic Conjunctivitis) |
| TxGNN 예측 점수 | 99.74% |
| 근거 수준 | L4 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 DrugBank 등재 정보에 상세 작용기전(MOA)이 없습니다. 다만 예측 근거 자료에 따르면, Prednisolone Acetate는 국소(안과용) 당질코르티코이드 수용체(glucocorticoid receptor) 작용제로 항염증·면역억제 작용을 나타냅니다.

기생충성 결막염(예: *Dirofilaria repens*에 의한 안구 사상충증)은 감염성 질환으로, 스테로이드는 병인인 기생충 자체를 제거하지 못합니다. 오히려 항기생충 치료 없이 스테로이드를 단독 사용할 경우 국소 면역반응을 억제해 기생충 생존이나 감염 악화를 조장할 위험이 있습니다.

즉 이번 예측은 TxGNN 임베딩 공간에서의 점수는 높지만(99.74%), 기전상 치료 목표와 상충되는 방향이어서 임상적 타당성은 낮습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [26846596](https://pubmed.ncbi.nlm.nih.gov/26846596/) | 2016 | Case Report/Review | Eye (London, England) | 안구 인수공통감염증인 *Dirofilaria repens* 감염에 의한 기생충성 결막염 발생 사례 보고 (초록 미제공) |

## 한국 시판 정보

현재 한국에 허가된 Prednisolone Acetate 제품이 없습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 근거가 사례보고 1편(Tier 3)뿐이며, 임상시험 등록이 전무합니다.
- 기전상 스테로이드 단독 사용이 기생충 감염을 악화시킬 위험이 있어, 예측 방향과 치료 목표가 상충합니다.
- 작용기전(MOA), 한국 허가사항·경고/금기 정보가 모두 Data Gap 상태로, 안전성 초기 평가(S1) 진입이 불가능합니다.

**진행하려면 필요한 것:**
- DrugBank API를 통한 상세 작용기전(MOA) 데이터 확보
- TFDA(또는 국내 규제기관) 허가사항의 경고·금기 정보 확보 (Blocking data gap)
- 기생충성 결막염에 대한 항기생충제 병용 여부를 포함한 전임상/임상 근거 추가 확보

---

**참고 — 동일 후보군 내 더 근거가 강한 예측 적응증**

이번 Evidence Pack에는 기생충성 결막염 외에도 9개의 예측 적응증이 포함되어 있습니다. 그중 다음 2건은 근거 수준과 기전 타당성이 더 높아 우선 검토를 권장합니다.

| 예측 적응증 | 근거 수준 | 권장 결정 | 비고 |
|---|---|---|---|
| 춘계 각결막염 (Vernal Conjunctivitis, VKC) | L3 | Proceed with Guardrails | Th2/IgE 매개 알레르기성 질환으로 국소 스테로이드가 임상 표준 치료. 비교임상시험 및 동일 계열 약물(loteprednol) 장기 안전성 자료 존재. IOP·백내장 모니터링 필요 |
| 유두형 결막염 (Papillary Conjunctivitis, GPC) | L3 | Research Question | 알레르기성 발병기전으로 스테로이드 사용이 합리적이나, 근거 대부분이 prednisolone 자체가 아닌 동일 계열 약물(loteprednol)에서 유래 |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

