---
layout: default
title: Dutasteride
parent: 僅模型預測 (L5)
nav_order: 236
evidence_level: L5
indication_count: 10
---

# Dutasteride
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

# Dutasteride: 양성 전립선 비대증에서 Ambras형 선천성 전신 다모증으로

## 한 문장 요약

Dutasteride는 5α-환원효소(Type 1 및 Type 2)를 억제하여 테스토스테론의 DHT 전환을 차단하는 약물로, 양성 전립선 비대증(BPH) 치료에 사용됩니다.
TxGNN 모델은 **Ambras형 선천성 전신 다모증(Ambras type hypertrichosis universalis congenita)**에 효과가 있을 수 있다고 예측하나,
현재 이를 지지하는 임상시험과 문헌이 **전혀 없으며**, 기전상 연관성도 매우 희박합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 양성 전립선 비대증 (BPH) ※ 한국 미허가 |
| 예측 신규 적응증 | Ambras형 선천성 전신 다모증 (Ambras type hypertrichosis universalis congenita) |
| TxGNN 예측 점수 | 99.998% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미허가 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, Dutasteride는 5α-환원효소 억제제(5-ARI)로 Type 1 및 Type 2 효소를 모두 차단하여 테스토스테론이 강력한 안드로겐인 디하이드로테스토스테론(DHT)으로 전환되는 것을 억제합니다. 이를 통해 전립선 크기를 줄이고, 안드로겐 의존성 모낭에서의 모발 소실을 늦춥니다.

**기전상 방향이 반대입니다.** Dutasteride는 DHT를 낮춰 안드로겐 의존성 모낭의 모발 성장을 감소시키는 방향으로 작용합니다. 그러나 Ambras형 선천성 전신 다모증은 8번 염색체 역위(8p21.3-q22.1)에 의한 선천성 기형으로, 안드로겐 신호 경로와 직접적인 연관이 없습니다. 이 질환에서 과도한 모발 성장은 발달 유전자 이상에서 비롯되며, DHT 억제로 교정될 수 있는 메커니즘이 아닙니다.

따라서 이 높은 TxGNN 예측 점수(99.998%)는 지식 그래프 내에서 Dutasteride가 모발 성장 관련 노드와 광범위하게 연결된 구조적 특성에서 비롯된 모델 노이즈(model noise)로 판단됩니다.

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

**결정: Hold**

**사유:**
Ambras형 선천성 전신 다모증에 대한 임상시험 및 문헌 근거가 전혀 없으며, 5α-환원효소 억제 기전과 이 질환의 병인(8번 염색체 역위) 사이에 유의미한 생물학적 연관성이 없습니다. 높은 TxGNN 점수는 모발 관련 노드 연결로 인한 모델 아티팩트로 판단됩니다.

**진행하려면 필요한 것:**
- Dutasteride 공식 허가사항(경고, 금기, 약물 상호작용) 확보 — MFDS 또는 동등 데이터베이스 조회 필요 (현재 Blocking Data Gap)
- 작용 기전(MOA) 데이터 보완 — DrugBank API 조회 필요 (현재 High Data Gap)
- 한국 내 허가 가능성 검토 — 현재 0건 허가로 시판 이력 없음
- 재창출 후보 재검토 시, 기전 연관성이 더 높은 **彌漫性 원형탈모(Rank 8, L4)** 또는 **안드로겐성 탈모** 방향을 우선 검토할 것을 권고
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

