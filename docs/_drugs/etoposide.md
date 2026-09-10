---
layout: default
title: Etoposide
parent: 僅模型預測 (L5)
nav_order: 305
evidence_level: L5
indication_count: 10
---

# Etoposide
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

# Etoposide: 세포독성 항암제에서 상피성 폐아세포종(Well-differentiated Fetal Adenocarcinoma of the Lung)으로

## 한 문장 요약

Etoposide는 Topoisomerase II 억제제 계열의 세포독성 항암제로, 한국 내 공식 허가 정보는 이번 Evidence Pack에서 확인되지 않았습니다(미상, 허가증 0건). TxGNN 모델은 **상피성 폐아세포종(Well-differentiated Fetal Adenocarcinoma of the Lung)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 임상시험은 없으며 **1편의 사례 보고**만 존재합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인되지 않음 (한국 허가 자료 미확보) |
| 예측 신규 적응증 | 상피성 폐아세포종 (Well-differentiated Fetal Adenocarcinoma of the Lung) |
| TxGNN 예측 점수 | 99.94% |
| 근거 수준 | L4 |
| 한국 시판 현황 | 미상 (시판되지 않음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 확보되지 않았습니다. 다만 Evidence Pack 내 다른 후보 적응증들의 분석 근거를 보면, Etoposide는 Topoisomerase II 억제제로서 빠르게 증식하는 세포의 DNA 이중가닥을 절단하여 항암 효과를 나타내는 것으로 기술되어 있습니다.

상피성 폐아세포종은 폐모세포종(Pulmonary Blastoma) 계열 중 상피 성분으로만 구성된 고분화 아형입니다. 그러나 이 후보에 대한 근거는 폐모세포종 사례 보고 1편에서 분류상 부수적으로 언급된 수준이며, 이 아형에 특이적인 치료 근거는 없습니다. 매우 희귀한 종양이라 표준 치료 지침 자체가 부재하며, TxGNN 예측은 폐모세포종 계열 전체에 대한 기전적 유사성 추론에 기반한 것으로 보입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [33107372](https://pubmed.ncbi.nlm.nih.gov/33107372/) | 2020 | Case Report | The Journal of International Medical Research | 전형적 이상성(biphasic) 폐모세포종 사례 보고. 우상엽 절제술 및 보조화학요법(nedaplatin+paclitaxel) 시행, 재발 후 경과 기술. 상피성 폐아세포종은 폐모세포종의 구성 아형으로 언급되었을 뿐, 이 아형 자체에 대한 Etoposide 치료 근거는 없음 |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 항암제 (Topoisomerase II 억제제) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
상피성 폐아세포종에 대한 근거는 사례 보고 1편(부수적 언급)뿐이며, 관련 임상시험이 전무합니다. 극히 희귀한 종양으로 표준 치료 지침조차 없어, 현재 근거 수준(L4)으로는 진행을 뒷받침하기 어렵습니다.

**진행하려면 필요한 것:**
- 이 아형에 특이적인 전임상 또는 추가 사례 축적 데이터
- 작용 기전(MOA) 확인 (DrugBank 조회 등, DG002)
- 규제기관 허가사항의 경고/금기 정보 확보 (DG001, Blocking 등급 — S1 안전성 초평가 진입에 필수)
- 한국 내 허가 및 시판 현황 확인

**참고:** 동일 Evidence Pack 내에는 이보다 근거 수준이 높은 후보 적응증이 함께 수집되어 있습니다. **소세포폐암(Small Cell Lung Carcinoma, L1·Proceed with Guardrails)**과 **유잉육종(Ewing Sarcoma, L1·Proceed with Guardrails)**, **횡문근육종(Rhabdomyosarcoma, L1·Proceed with Guardrails)**은 다수의 완료된 Phase 3 RCT로 뒷받침되므로, 우선순위 검토 시 함께 고려할 가치가 있습니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

