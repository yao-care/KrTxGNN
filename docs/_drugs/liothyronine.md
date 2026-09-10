---
layout: default
title: Liothyronine
parent: 僅模型預測 (L5)
nav_order: 443
evidence_level: L5
indication_count: 10
---

# Liothyronine
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

# Liothyronine: 적응증 데이터 없음(한국 미판매)에서 신장형성이상/무형성증으로

## 한 문장 요약

Liothyronine(DB00279)은 합성 T3 갑상선호르몬 제제이나, 한국에는 현재 허가된 제품이 없고 Evidence Pack상 기존 적응증 정보도 확인되지 않습니다. TxGNN 모델은 **신장형성이상/무형성증(Renal Hypodysplasia/Aplasia)**에 효과가 있을 수 있다고 예측했으며(예측 점수 99.95%), 그러나 이를 뒷받침하는 임상시험이나 문헌은 현재 전혀 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (한국 허가 이력 없음) |
| 예측 신규 적응증 | 신장형성이상/무형성증 (Renal Hypodysplasia/Aplasia) |
| TxGNN 예측 점수 | 99.95% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미판매 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 없습니다. Evidence Pack에 기록된 근거 해설에 따르면, TxGNN의 높은 예측 점수는 지식 그래프상에서 갑상선축과 신장 발달 유전자 네트워크 간의 **간접적 연관성**(예: 갑상선호르몬이 태아 장기 발달에 미치는 영향)을 반영한 결과일 가능성이 큽니다.

그러나 liothyronine이 신장형성이상/무형성증을 치료하거나 개선할 수 있다는 **직접적인 병태생리학적 기전 근거는 없으며**, 임상 또는 문헌 근거도 전혀 없습니다. 즉, 이 예측은 지식 그래프 임베딩상의 통계적 유사성(노이즈)일 가능성이 높다는 것이 근거 해설의 결론입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

현재 한국에 허가된 Liothyronine 제품이 없습니다 (미판매, 허가증 0건).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 높지만(99.95%) 이를 뒷받침하는 임상시험·문헌 근거가 전혀 없고, 기전상으로도 직접적 연관성이 확인되지 않아 지식 그래프상의 통계적 노이즈일 가능성이 높습니다(근거 수준 L5, decision stage S0).

**진행하려면 필요한 것:**
- 작용 기전(MOA) 및 TFDA/식약처 수준 허가사항(경고·금기) 데이터 보강 (Blocking data gap: DG001, DG002)
- 신장 발달과 갑상선호르몬 신호전달의 연관성을 뒷받침할 전임상/기전 연구
- 참고: 동일 Evidence Pack 내 **nodular goiter(결절성 갑상선종, rank 3)** 후보는 L2 근거 수준에 임상시험 2건·문헌 20편을 보유하며 "Proceed with Guardrails"로 평가되어, 우선 검토 가치가 더 높습니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

