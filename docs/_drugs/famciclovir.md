---
layout: default
title: Famciclovir
parent: 僅模型預測 (L5)
nav_order: 313
evidence_level: L5
indication_count: 9
---

# Famciclovir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# FAMCICLOVIR: 기존 적응증 정보 없음에서 대상포진후신경통(Post-infectious Neuralgia)으로

## 한 문장 요약

FAMCICLOVIR의 기존 적응증 데이터는 이번 Evidence Pack에 기재되어 있지 않습니다(한국 미시판, 허가증 0건).
TxGNN 모델은 **대상포진후신경통(Post-infectious Neuralgia)**에 효과가 있을 수 있다고 예측하지만(예측 점수 99.75%),
관련 **임상시험 2건**은 모두 FAMCICLOVIR 자체를 시험하지 않았고, **직접적인 문헌 근거는 없습니다**.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (원 적응증 정보 미기재, 한국 미시판) |
| 예측 신규 적응증 | 대상포진후신경통 (Post-infectious Neuralgia) |
| TxGNN 예측 점수 | 99.75% |
| 근거 수준 | L4 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 없습니다(Data Gap). 다만 Evidence Pack에 포함된 분석 근거에 따르면,
FAMCICLOVIR은 수두대상포진바이러스(VZV) 복제를 억제하는 항바이러스제 계열로 파악되며,
대상포진후신경통은 급성 대상포진기의 바이러스 복제 및 신경 손상에 따른 후유증으로 알려져 있어,
VZV 복제 억제가 대상포진후신경통 발생률·병정을 낮출 수 있다는 기전적 가설은 합리적입니다.

다만 이번 Pack에 수록된 임상시험 2건은 각각 신경차단술(리포좀 부피바카인/로피바카인)과 옥시코돈 조기 투여를 평가한 것으로, **FAMCICLOVIR 자체를 시험한 연구가 아닙니다.** 즉 질환 맥락만 겹칠 뿐 직접적인 약물 근거는 이 데이터셋 안에 없습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT06798662](https://clinicaltrials.gov/study/NCT06798662) | N/A | 모집 예정 | 120 | 대상포진 급성 통증에 대한 리포좀 부피바카인/로피바카인 신경차단 + 펄스고주파 병용 효과 평가(3중맹검 RCT). FAMCICLOVIR 미포함, 질환 맥락만 겹침(관련성 등급 C). |
| [NCT03120962](https://clinicaltrials.gov/study/NCT03120962) | N/A | 상태 불명 | 140 | 대상포진 급성기 옥시코돈 조기 투여가 대상포진후신경통 예방에 미치는 효과 평가. FAMCICLOVIR 미포함(관련성 등급 C). |

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

현재 한국에 등록된 허가 정보가 없습니다 (미시판, 허가증 0건).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 높지만, 이 예측을 뒷받침하는 임상시험 2건 모두 FAMCICLOVIR 자체를 시험하지 않았고 관련 문헌도 없어 직접적인 근거가 부재합니다. 기전적 가설은 합리적이나 현재로서는 모델 예측과 간접 정황에 그치는 수준입니다.

**진행하려면 필요한 것:**
- FAMCICLOVIR을 직접 시험한 대상포진후신경통 임상시험 또는 관찰연구 확보
- 작용기전(MOA) 데이터 보완 (현재 Data Gap)
- 한국 내 허가/시판 경로 검토 (현재 허가증 0건)
- TFDA/식약처 허가사항 기반 안전성 자료(경고, 금기, DDI) 확보

**참고:** 같은 Evidence Pack 내 다른 예측 적응증인 "chickenpox"(실질 내용은 대상포진 관련)의 경우, FAMCICLOVIR 500mg을 직접 시험한 완료된 Phase 3 RCT([NCT01327144](https://clinicaltrials.gov/study/NCT01327144))가 존재해 근거 수준 L2, "Proceed with Guardrails"로 평가되어 있습니다. 대상포진 계열 적응증 전반을 검토할 경우 해당 후보도 함께 참고할 가치가 있습니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

