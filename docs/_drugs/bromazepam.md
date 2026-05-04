---
layout: default
title: Bromazepam
parent: 僅模型預測 (L5)
nav_order: 152
evidence_level: L5
indication_count: 1
---

# Bromazepam
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

# Bromazepam: 항불안제에서 편두통으로

## 한 문장 요약

Bromazepam은 GABA-A 수용체 양성 조절제로 작용하는 벤조디아제핀계 항불안·진정제입니다.
TxGNN 모델은 **편두통(Migraine Disorder)**에 효과가 있을 수 있다고 예측하며,
현재 **1건의 임상시험**이 확인되었으나 관련 문헌은 없으며, 직접적인 근거는 매우 제한적입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 항불안·진정 (벤조디아제핀계 약물) |
| 예측 신규 적응증 | 편두통 (Migraine Disorder) |
| TxGNN 예측 점수 | 99.06% |
| 근거 수준 | L4 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Bromazepam은 벤조디아제핀(Benzodiazepine)계 약물로, GABA-A 수용체 양성 조절제(Positive Allosteric Modulator, PAM)로 작용합니다. 중추신경계를 억제하여 항불안, 근육 이완, 진정 효과를 나타냅니다.

편두통과의 간접적인 기전 연관성으로는 다음이 제시됩니다: (1) 불안·스트레스 감소를 통한 편두통 유발인자 완화, (2) 근육 이완을 통한 두부 근긴장 경감, (3) 진정 작용을 통한 급성 발작 시 증상 보조 조절. 그러나 편두통의 표준 치료 기전인 삼차신경혈관 경로(CGRP/5-HT)와는 직접적인 작용점이 없으며, Triptan 계열·CGRP 길항제와의 기전적 중첩도 없습니다.

현재 상세한 작용 기전 데이터(MOA)가 없습니다. 위에 기술된 기전적 연관성은 간접적·이차적 추정에 해당하며, 직접적인 항편두통 효능을 뒷받침하는 근거는 부재합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04410536](https://clinicaltrials.gov/study/NCT04410536) | Phase 4 | 완료 | 25 | 약물 과용 두통(MOH) 환자 대상 거가 戒斷 프로그램 + 행동치료 병행 연구. Bromazepam은 편두통 치료제가 아닌 戒斷 과정 보조 항불안제 역할로 추정되며, 1차 종점은 MOH 재발률로 편두통 직접 치료 효과 평가가 아님. ⚠️ 관련성 낮음(등급 C) |

> **주의:** 확인된 임상시험 1건은 Bromazepam의 항편두통 효과를 직접 검증한 것이 아닙니다.

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
편두통에 대한 직접적인 임상 근거가 전무하며, 확인된 임상시험 1건도 Bromazepam의 항편두통 효능이 아닌 약물 과용 두통 戒斷 보조용으로 사용된 것으로 추정됩니다. TxGNN 예측 점수는 높으나 기전적 연관성이 간접적·이차적 수준에 머물러 있어 재창출 타당성을 지지하는 근거가 부족합니다.

**진행하려면 필요한 것:**
- 상세한 작용 기전 데이터 (MOA) — DrugBank API를 통한 확인 필요
- 허가사항(TFDA 또는 MFDS 仿單) 경고 및 금기 데이터 확보
- Bromazepam과 편두통 간 직접적인 전임상 또는 기전 연구 탐색
- 벤조디아제핀계 약물의 편두통 사용 시 의존성·내성 위험에 대한 안전성 평가 계획
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

