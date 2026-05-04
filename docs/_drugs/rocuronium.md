---
layout: default
title: Rocuronium
parent: 僅模型預測 (L5)
nav_order: 285
evidence_level: L5
indication_count: 10
---

# Rocuronium
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

# Rocuronium: 마취용 신경근 차단에서 편두통으로

---

## 한 문장 요약

Rocuronium은 수술 중 기관 삽관 및 전신마취 보조를 위해 정맥 투여하는 비탈분극성 신경근 차단제입니다.
TxGNN 모델은 **편두통(Migraine Disorder)**에 효과가 있을 수 있다고 예측하나,
현재 이 방향을 직접 지지하는 임상시험과 문헌은 사실상 **전무**합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 수술 및 기관 삽관 보조를 위한 신경근 차단 |
| 예측 신규 적응증 | 편두통 (Migraine Disorder) |
| TxGNN 예측 점수 | 99.90% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미시판 (허가 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Rocuronium은 골격근 신경근 접합부(NMJ)의 니코틴성 아세틸콜린 수용체(nAChR)에 경쟁적으로 결합하여 근이완을 유도하는 비탈분극성 신경근 차단제입니다. 현재 시스템에 상세한 MOA 데이터가 등록되어 있지 않으나, 해당 약리 분류는 임상적으로 확립되어 있습니다.

편두통의 병태생리는 CGRP 분비 증가, 피질 확산성 억제(CSD), 삼차혈관계 활성화를 핵심 기전으로 합니다. Rocuronium의 골격근 NMJ 차단 작용은 이러한 중추 및 혈관 경로와 직접적인 교점이 없습니다. TxGNN의 높은 예측 점수(99.90%)는 지식 그래프 내 '간질-편두통 공병 노드'의 간접 연결에서 비롯된 것으로 추정되며, 실제 약리학적 근거를 반영하지 않을 가능성이 높습니다.

단, 전기경련치료(ECT) 맥락에서 Rocuronium-sugammadex 조합이 ECT 유발 전신 근육 수축을 차단함으로써 술후 두통 발생률을 낮출 수 있다는 제한적 근거가 존재합니다(PMID 23812022, RCT). 이는 시술 관련 두통의 예방적 적용이며, 편두통 질환의 능동 치료와는 구별되는 개념입니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | 완료 | 3,520 | 소아에게 표준 치료로 투여되는 미연구 약물의 약동학 특성 파악. Rocuronium이 표준 마취제로 포함되었으나 편두통은 연구 목표가 아님 |

> ⚠️ 위 시험은 편두통 치료를 목적으로 한 연구가 아닙니다. Rocuronium이 표준 마취약으로 포함된 소아 광역 PK 관찰 연구이며, 재창출 가설과 무관합니다.

---

## 문헌 근거

현재 Rocuronium의 편두통 치료 관련 문헌이 없습니다.

---

## 한국 허가 정보

현재 Rocuronium의 한국 허가 이력이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
Rocuronium의 신경근 차단 기전과 편두통 병태생리 사이에 직접적인 약리학적 접점이 확인되지 않으며, 편두통 치료를 목적으로 설계된 임상 근거가 전무합니다. TxGNN 예측 점수 99.90%는 지식 그래프의 간접 연결(간질-편두통 공병 노드)에서 비롯된 노이즈로 판단됩니다.

**진행하려면 필요한 것:**
- Rocuronium 상세 MOA 데이터 확보 (DrugBank API 조회)
- 한국 첨부문서 경고·금기 정보 확보 (허가기관 공식 문서)
- **별도 권고**: ECT 후 두통 예방 맥락(headache disorder, TxGNN 순위 10위, L4 근거)에 대해 독립적인 심층 평가 진행 — 해당 적응증에는 RCT 1건(PMID 23812022), Grade B 임상시험 2건이 존재하며, 재창출보다 **적응 확장(label extension)** 관점에서 검토 가치가 있음
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

