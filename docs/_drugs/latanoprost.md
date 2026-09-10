---
layout: default
title: Latanoprost
parent: 僅模型預測 (L5)
nav_order: 428
evidence_level: L5
indication_count: 10
---

# Latanoprost
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

# LATANOPROST: 안압 강하(녹내장)에서 원발성 유전성 녹내장으로

## 한 문장 요약

Latanoprost는 안압을 낮추는 표준 치료 약물로 사용되어 온 프로스타글란딘(PGF2α) 유사체입니다. TxGNN 모델은 **원발성 유전성 녹내장(Primary Hereditary Glaucoma)**에도 효과가 있을 것으로 예측하며, 이는 병인이 유전성이라는 점만 다를 뿐 사실상 기존 약리 적응증 범주 내 세부 유형에 해당합니다. 현재 **1건의 완료된 Phase 2 임상시험**이 이 방향을 뒷받침하며, 관련 문헌은 아직 확인되지 않았습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (한국 허가 정보 없음, DrugBank MOA도 미확보) |
| 예측 신규 적응증 | 원발성 유전성 녹내장 (Primary Hereditary Glaucoma) |
| TxGNN 예측 점수 | 99.88% |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 DrugBank의 상세 작용 기전(MOA) 데이터는 확보되지 않았습니다(Data Gap). 다만 근거 자료에 따르면, Latanoprost는 PGF2α 전구약물 유사체로 FP 수용체에 작용해 포도막공막 경로를 통한 방수 유출을 촉진하는, 임상에서 표준적으로 쓰이는 안압 강하 기전을 가진 것으로 알려져 있습니다.

원발성 유전성 녹내장은 병인이 유전적이라는 점만 다를 뿐, 안압 상승이라는 동일한 병태생리 범주에 속합니다. 즉 이번 예측은 완전히 새로운 질환으로의 재창출이라기보다, 동일 약리 범주 내에서 세부 적응증(유전성 아형)으로 확장되는 성격에 가깝습니다.

이 때문에 기전상 적용 가능성은 매우 높게 평가되며, 실제로 관련 Phase 2 임상시험에서도 소아/난치성 원발성 녹내장 환자를 대상으로 Latanoprost의 안압 강하 효과와 안전성이 평가된 바 있습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | 완료 | 37 | 수술적 치료에 반응하지 않는 소아 원발성 녹내장(PG) 환자에서 latanoprost와 dorzolamide의 안압 강하 효과 및 안전성을 평가 |

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

현재 한국 내 시판 허가 정보가 없습니다 (시판 현황: 미시판, 허가증 0건).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
원발성 유전성 녹내장은 latanoprost의 핵심 약리 기전(FP 수용체 매개 안압 강하)에 부합하는 세부 적응증으로, 완료된 Phase 2 임상시험(L2 근거 수준) 결과가 이를 뒷받침합니다. 다만 한국 내 시판 허가가 없고, TFDA(현지 규제당국) 수준의 경고/금기 정보가 확보되지 않아 안전성 검토 없이 바로 진행할 수는 없습니다.

**진행하려면 필요한 것:**
- TFDA 공식 사이트에서 허가사항(경고, 금기, 상호작용) 확보 — 현재 Blocking 등급 데이터 갭
- DrugBank API를 통한 상세 작용 기전(MOA) 확인
- 한국 내 시판/허가 신청 여부 검토
- 유전성 아형에 특이적인 추가 임상 근거(문헌·임상시험) 축적
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

