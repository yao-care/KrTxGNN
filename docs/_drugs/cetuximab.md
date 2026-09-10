---
layout: default
title: Cetuximab
parent: 僅模型預測 (L5)
nav_order: 193
evidence_level: L5
indication_count: 10
---

# Cetuximab
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

# Cetuximab: 두경부 편평세포암/전이성 대장직장암에서 폐 연골성 과오종으로

## 한 문장 요약

Cetuximab(DrugBank DB00002)은 EGFR(상피세포성장인자수용체)을 표적으로 하는 키메라 단클론항체로, 임상시험 근거들을 통해 두경부 편평세포암(HNSCC)과 전이성 대장직장암 치료에 널리 쓰이고 있는 것으로 확인됩니다(대만 허가 자료는 없음).
TxGNN 모델은 **폐 연골성 과오종(Chondroid Hamartoma)**에 효과가 있을 수 있다고 예측했으나(예측 점수 99.95%, 전체 순위 1475위), 이를 뒷받침하는 임상시험이나 문헌은 **0건**이며, 기전상 연관성도 확인되지 않았습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 두경부 편평세포암(HNSCC), 전이성 대장직장암 (EGFR 표적치료 — 대만 허가 자료 없음) |
| 예측 신규 적응증 | 폐 연골성 과오종 (Chondroid Hamartoma) |
| TxGNN 예측 점수 | 99.95% (순위 1475위) |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

Cetuximab은 EGFR을 표적으로 하는 항EGFR 단클론항체로, 종양세포의 성장 신호를 차단하는 방식으로 작용합니다. 다만 이번 Evidence Pack에는 상세 작용기전(MOA) 데이터가 확보되지 않았습니다(Data Gap, 심각도 High) — DrugBank 조회는 성공했으나 MOA 텍스트 필드 자체가 비어 있는 상태입니다.

폐 연골성 과오종은 양성 폐 종괴로, EGFR 경로와의 알려진 연관성이 없습니다. Evidence Pack의 기전 분석에서도 "TxGNN 예측 점수만 높을 뿐 기전상 근거는 없다"고 명시하고 있어, 이번 예측은 순수하게 모델 통계적 신호에 의존한 것으로 판단됩니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 세포독성

Cetuximab은 세포독성 화학요법이 아닌 항EGFR 표적치료제(단클론항체)로 분류됩니다. 구체적인 골수억제·구토 유발성·모니터링 데이터는 이번 Evidence Pack에 포함되어 있지 않으므로, 허가사항의 경고 및 주의사항을 참조하세요.

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (항EGFR 단클론항체) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
폐 연골성 과오종에 대한 예측은 TxGNN 모델 점수 외에 임상시험, 문헌, 기전적 근거가 전혀 없는 L5 수준입니다. 또한 TFDA 허가사항/경고·금기 정보(DG001, Blocking)가 확보되지 않아 안전성 초기평가(S1) 단계에 진입할 수 없는 상태입니다.

**진행하려면 필요한 것:**
- TFDA 공식 사이트에서 Cetuximab 사용설명서(경고·금기) 확보
- DrugBank API를 통한 상세 작용기전(MOA) 데이터 확보
- 폐 연골성 과오종에서 EGFR 발현/경로 연관성에 대한 전임상 연구

**참고:** 이번 Evidence Pack에는 총 10개의 예측 적응증이 포함되어 있으며, 그중 순위 10위 **전악성 신생물(pre-malignant neoplasm)**은 Phase 3 RCT(NCT01302834)를 포함해 L2 수준의 상대적으로 강한 근거를 갖추고 있습니다(Research Question, S2 단계). 실질적인 재창출 후보 검토가 필요하다면 해당 적응증을 별도로 평가하는 것을 권장합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

