---
layout: default
title: Tinidazole
parent: 僅模型預測 (L5)
nav_order: 679
evidence_level: L5
indication_count: 10
---

# Tinidazole
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

# Tinidazole: 원충 감염증에서 폐경후 위축성 질염으로

## 한 문장 요약

Tinidazole은 5-nitroimidazole 계열 항원충제로, 원래 트리코모나스증·아메바증·지아르디아증 등 원충 감염증 치료에 사용되어 온 약물입니다(한국 허가 정보는 확인되지 않음). TxGNN 모델은 **폐경후 위축성 질염(Postmenopausal Atrophic Vaginitis)**에 효과가 있을 수 있다고 **99.93%**의 높은 점수로 예측했으나, 현재 이를 뒷받침하는 임상시험이나 문헌 근거는 확인되지 않았습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 트리코모나스증·아메바증·지아르디아증 등 원충 감염증 (해외 문헌 기준, 한국 허가 정보 없음) |
| 예측 신규 적응증 | 폐경후 위축성 질염 (Postmenopausal Atrophic Vaginitis) |
| TxGNN 예측 점수 | 99.93% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미허가 (시판되지 않음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 없습니다. 다만 문헌 근거에 따르면 tinidazole은 5-nitroimidazole 계열 약물로, 니트로기가 환원되면서 병원체 DNA를 손상시키는 방식으로 트리코모나스(*Trichomonas vaginalis*), 지아르디아, 아메바 등 원충 및 혐기성균을 사멸시키는 것으로 알려져 있습니다.

폐경후 위축성 질염은 폐경으로 인한 에스트로겐 결핍이 원인인 호르몬성 질환으로, 항원충·항균 기전과는 직접적인 생물학적 연관성이 없습니다. 평가 근거(rationale)에 따르면, 이 예측은 지식그래프 내 '질(vagina) 관련' 노드들의 해부학적 인접성 또는 동반질환 패턴에 의한 통계적 혼입(confounding) 가능성이 높으며, 실제 약리학적 연결고리는 확인되지 않았습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

한국에는 현재 허가된 tinidazole 제품이 없습니다 (미허가/미출시).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> ⚠️ 참고: 식약처 허가사항(경고·금기 등) 자료가 확보되지 않아, 안전성 초기 평가(S1) 단계 진입이 불가능한 상태입니다(Blocking Data Gap).

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 점수는 높지만(99.93%), 이를 뒷받침하는 임상시험이나 문헌이 전혀 없고(L5), 기전적으로도 항원충 작용과 폐경후 위축성 질염(호르몬성 질환) 사이에 직접적 연관성이 없습니다. 예측 근거 자체가 지식그래프 내 통계적 혼입일 가능성이 제기되어, 현 단계에서는 진행을 보류하는 것이 타당합니다.

**진행하려면 필요한 것:**
- 식약처(TFDA/한국 규제기관) 허가사항 — 경고 및 금기사항 확보 (Blocking)
- DrugBank 등에서 상세 작용 기전(MOA) 데이터 확보 (High)
- 폐경후 위축성 질염과 관련된 전임상 또는 관찰연구 근거 확보
- 대안으로, 동일 Evidence Pack 내 근거 수준이 더 높은 후보(예: AIDS, L3/S1, 문헌 18편·임상시험 1건)에 대한 별도 검토 고려
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

