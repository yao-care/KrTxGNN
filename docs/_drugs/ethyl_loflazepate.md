---
layout: default
title: Ethyl Loflazepate
parent: 僅模型預測 (L5)
nav_order: 257
evidence_level: L5
indication_count: 1
---

# Ethyl Loflazepate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Ethyl Loflazepate: 항불안제(벤조디아제핀)에서 불면증으로

## 한 문장 요약

Ethyl loflazepate는 GABA-A 수용체를 조절하는 벤조디아제핀 계열의 전구약물로, 체내에서 활성 대사체인 delorazepam(클로르데스메틸디아제팜)으로 전환됩니다.
TxGNN 모델은 **불면증(Insomnia)**에 효과가 있을 수 있다고 예측하며, 이는 벤조디아제핀 계열의 중추신경 억제 및 수면 촉진 기전에 기반한 것입니다.
다만 현재 이 예측을 직접 지지하는 **등록된 임상시험 및 문헌이 전혀 없어** 기전적 추론 단계에 머무르고 있습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (한국 미허가) |
| 예측 신규 적응증 | 불면증 (Insomnia) |
| TxGNN 예측 점수 | 99.76% |
| 근거 수준 | L4 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Ethyl loflazepate는 벤조디아제핀 계열의 전구약물로, 복용 후 체내에서 활성 대사체인 delorazepam으로 전환됩니다. 핵심 약리 기전은 GABA-A 수용체에 대한 **양성 이조절(positive allosteric modulation)**로, 억제성 신경전달물질 GABA의 작용을 강화함으로써 중추신경계를 전반적으로 억제합니다.

벤조디아제핀 계열 약물은 입면 잠복기를 단축하고 수면 시간을 연장하는 효과가 이미 잘 확립되어 있으며, 이는 불면증 치료에 있어 **계열 효과(class effect)**로 인정됩니다. Ethyl loflazepate의 GABA-A 수용체 조절 기전은 불면증 적응증에 대한 기전적 타당성을 간접적으로 뒷받침합니다.

다만 Evidence Pack 내 원래 허가 적응증 데이터가 누락되어 있고, 한국 내 허가 및 시판 이력도 없습니다. TxGNN 예측은 벤조디아제핀 계열 수준의 기전적 유사성에 기반한 것으로 보이며, 이 약물 특유의 불면증 임상 데이터는 현재 확인되지 않습니다.

---

## 임상시험 근거

현재 Ethyl loflazepate와 불면증을 대상으로 한 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 한국 시판 정보

해당 약물은 현재 한국에 허가된 제품이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 점수는 99.76%로 높으나, 이 적응증을 직접 지지하는 임상시험·문헌이 전혀 없으며 한국 내 허가 이력도 부재합니다. GABA-A 기전을 통한 수면 촉진 효과는 계열적으로 설득력이 있으나, 현재는 기전적 추론 수준(L4)에 그치므로 실증적 근거 확보 전까지 추가 진행을 보류합니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 상세 데이터 확보 (DrugBank API 조회 권장)
- 원래 허가 적응증 파악 (MFDS 또는 일본 PMDA·유럽 EMA 등 타국 허가사항 검토)
- Ethyl loflazepate 단독 또는 불면증 관련 전임상·임상 문헌 심층 검색
- 경고, 금기, 약물상호작용 등 안전성 원문 확인 (국내외 허가사항 PDF 검토)
- 유사 벤조디아제핀 계열 약물의 불면증 치료 효능·안전성 비교 분석
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

