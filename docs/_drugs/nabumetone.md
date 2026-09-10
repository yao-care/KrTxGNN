---
layout: default
title: Nabumetone
parent: 僅模型預測 (L5)
nav_order: 493
evidence_level: L5
indication_count: 10
---

# Nabumetone
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

# Nabumetone: 골관절염·류마티스관절염에서 골관절염 감수성(Osteoarthritis Susceptibility)으로

## 한 문장 요약

Nabumetone은 원래 골관절염(OA) 및 류마티스관절염(RA) 치료에 사용되는 비스테로이드성 소염진통제(NSAID) 계열 약물입니다.
TxGNN 모델은 이번 평가에서 가장 높은 순위로 **골관절염 감수성(Osteoarthritis Susceptibility)**을 예측했지만,
현재 이를 뒷받침하는 **임상시험 0건, 문헌 0편**으로 실질적 근거가 없는 상태입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 골관절염, 류마티스관절염 (NSAID 계열 — 국내 허가 자료 없음, 해외 자료 기준) |
| 예측 신규 적응증 | 골관절염 감수성 (Osteoarthritis Susceptibility) |
| TxGNN 예측 점수 | 99.9991% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미판매 (국내 허가 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, Nabumetone은 비산성(non-acidic) 전구약물로,
간에서 활성대사체인 6-methoxy-2-naphthylacetic acid(6-MNA)로 전환된 뒤 COX-1/COX-2를 억제하여
소염·진통 효과를 나타내는 NSAID입니다.

다만 "osteoarthritis susceptibility"는 골관절염 발병의 **유전적 소인/위험 유전자** 수준의 개념으로,
nabumetone의 COX 억제라는 약리 기전과 직접적으로 대응되지 않습니다. TxGNN 점수는 지식그래프 상에서
osteoarthritis 노드와의 위상적 근접성에서 비롯된 것으로 추정되며, 실제 약리학적 연관성이라기보다는
**KG 임베딩 노이즈**에 가까운 것으로 평가됩니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

국내 허가 정보가 없습니다 (시판 현황: 미판매).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
1순위 예측 적응증인 "골관절염 감수성"은 임상시험·문헌 근거가 전혀 없는 L5 수준이며,
기전상으로도 nabumetone의 약리 작용과 직접 연결되지 않는 KG 노이즈 가능성이 높아 현 단계에서 진행할 근거가 부족합니다.

**참고:** 동일 Evidence Pack 내 다른 후보들은 근거 수준이 더 높습니다 — 류마티스관절염(L1, Proceed with Guardrails),
골관절염(L1, Proceed with Guardrails)은 nabumetone의 기존 승인 적응증에 해당하며, 관절병증(arthropathy, L2, Research Question)은
임상시험 2건·문헌 20편의 실질적 근거를 갖춘 확장 적응증 후보로 별도 검토 가치가 있습니다.

**진행하려면 필요한 것:**
- DrugBank API를 통한 상세 작용기전(MOA) 데이터 확보 (DG002)
- 국내 허가사항(경고·금기) 확보 — 현재 S1 안전성 초평가 진입이 차단된 상태 (DG001, Blocking)
- "골관절염 감수성" 대신 근거가 확인된 관절병증(arthropathy) 후보에 대한 재평가
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

