---
layout: default
title: Pitavastatin
parent: 僅模型預測 (L5)
nav_order: 558
evidence_level: L5
indication_count: 10
---

# Pitavastatin
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

# Pitavastatin: 고콜레스테롤혈증에서 Familial Combined Hyperlipidemia(비활성 진단명)로

## 한 문장 요약

Pitavastatin은 HMG-CoA reductase 억제제 계열(statin)로, 일반적으로 고콜레스테롤혈증/이상지질혈증 치료에 사용되는 약물입니다.
TxGNN 모델은 **"Familial Combined Hyperlipidemia"(obsolete 진단명)**에 효과가 있을 것으로 예측했으나(점수 99.998%),
이 질병명은 이미 폐기된(obsolete) 온톨로지 용어이며 **임상시험 0건, 문헌 0편**으로 실제 근거는 전혀 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 이상지질혈증/고콜레스테롤혈증 (statin 계열 일반 적응증, 한국 허가 자료 없음) |
| 예측 신규 적응증 | Familial Combined Hyperlipidemia (obsolete 진단명, TxGNN rank 157) |
| TxGNN 예측 점수 | 99.998% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 이 약물의 상세한 작용기전(MOA) 데이터는 확보되어 있지 않습니다(Data Gap). 다만 evidence pack 내 다른 예측 항목들의 기전 설명을 종합하면, Pitavastatin은 HMG-CoA reductase를 억제하여 간에서의 콜레스테롤 합성을 줄이고, 이에 대한 대상성 반응으로 LDL 수용체 발현을 높여 혈중 LDL을 낮추는 전형적인 statin 기전을 가진 것으로 파악됩니다.

이번 예측 대상인 "Familial Combined Hyperlipidemia"에 대해서는, 이론적으로는 콜레스테롤 합성 억제가 혼합형 고지혈증에도 기전적 합리성을 가질 수 있습니다. 그러나 **이 질병명 자체가 이미 폐기(obsolete)된 온톨로지 용어**이며, 임상시험이나 문헌에서 이 진단명을 직접 다룬 근거가 전혀 확인되지 않습니다. 즉 TxGNN 지식그래프 임베딩 점수만 높을 뿐, 실증적 뒷받침이 없는 상태입니다.

참고로 이 evidence pack 안에는 동일 약물에 대해 훨씬 강한 근거(L1, Phase 3/4 RCT 다수)를 가진 다른 예측 항목들(예: hyperlipoproteinemia, familial hypercholesterolemia)이 존재합니다. 이들은 사실상 statin의 기존/공인 적응증에 가까운 항목으로, 별도로 평가할 가치가 있습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 점수는 높지만(99.998%), 대상 질병명("Familial Combined Hyperlipidemia")이 이미 폐기된 온톨로지 용어이고 임상시험·문헌 근거가 전무하여(L5, S0) 실질적 검토 단계로 넘어갈 근거가 부족합니다. 또한 이 약물은 한국에 미출시 상태로 허가 자료(TFDA 경고/금기)도 확보되지 않았습니다.

**진행하려면 필요한 것:**
- 질병 매핑 재검증: obsolete 용어를 현재 사용되는 표준 진단명(예: 혼합형 이상지질혈증)으로 재매핑 후 재평가
- TFDA(또는 MFDS) 수준의 경고/금기 사항 확보 (DG001, Blocking – S1 안전성 초평가 진입 필수 조건)
- 상세 작용기전(MOA) 데이터 확보 (DG002, High – DrugBank 조회 필요)
- 동일 데이터셋 내 근거 수준이 높은 다른 예측 항목(hyperlipoproteinemia, familial hypercholesterolemia 등)에 대한 별도 평가서 작성 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

