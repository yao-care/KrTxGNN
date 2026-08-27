---
layout: default
title: Canakinumab
parent: 僅模型預測 (L5)
nav_order: 167
evidence_level: L5
indication_count: 10
---

# Canakinumab
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

# Canakinumab: 자가염증성 질환 중심의 다중 예측 적응증 스크리닝 평가

## 한 문장 요약

Canakinumab(DrugBank ID: DB06168)은 IL-1β를 표적으로 하는 단일클론항체로, 이번 Evidence Pack에는 원래 승인 적응증 데이터가 입력되지 않은 상태(Data Gap)로 접수되었습니다.
TxGNN 모델은 총 **10개 질환**을 신규 적응증 후보로 예측했으나, 예측 점수(TxGNN score)와 실제 임상적 타당성 사이에 큰 괴리가 있습니다 — 점수 1위인 **간경색(hepatic infarction)**은 기전상 근거가 약한 반면(L5), 점수는 6위이지만 **가족성 지중해열(FMF)**은 이미 실제 승인 적응증을 모델이 "재발견"한 사례(L1)이고, **Blau 증후군**과 **PFAID**는 동일 계열(IL-1 inflammasome) 질환으로서 근거 수준 L3의 연구 가치가 있는 후보입니다. 현재 임상시험·문헌 근거는 10개 후보 모두 0건으로 조회되었습니다.

---

## 빠른 개요 (표)

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (Data Gap — `original_indications`, `original_moa` 모두 미입력) |
| 예측 신규 적응증 수 | 10건 (rank 1~10) |
| TxGNN 최고 점수 후보 | 간경색 (hepatic infarction), 99.86% — 단, 근거 수준 L5(기전 반박) |
| 임상적으로 가장 유의미한 후보 | 가족성 지중해열(FMF, L1·기승인 재발견), Blau 증후군(L3), PFAID(L3) |
| 근거 수준 분포 | L1×1, L3×2, L4×1, L5×6 |
| 한국(대만 데이터 기준) 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 (전체) | **Hold** (안전성 데이터 Blocking Gap 해소 전까지) |

### 전체 후보 순위표

| 순위 | 예측 질환 | TxGNN 점수 | 근거 수준 | 결정 단계 | 권고 |
|------|----------|-----------|----------|----------|------|
| 1 | 간경색 (hepatic infarction) | 99.86% | L5 | S0 | Hold |
| 2 | 간정맥폐쇄병 (hepatic veno-occlusive disease) | 99.82% | L4 | S0 | Hold |
| 3 | 간자반증 (peliosis hepatis) | 99.78% | L5 | S0 | Hold |
| 4 | 복합 면역결핍 증후군 | 99.71% | L5 | S0 | Hold |
| 5 | PFAID (주기열-영아소장결장염 자가염증증후군) | 99.57% | L3 | S1 | Research Question |
| 6 | 가족성 지중해열 (FMF) | 99.41% | L1 | S3 | Proceed with Guardrails |
| 7 | 피부외 비만세포종 | 99.35% | L5 | S0 | Hold |
| 8 | Blau 증후군 | 99.34% | L3 | S2 | Research Question |
| 9 | 모노소미 X (터너증후군) | 99.31% | L5 | S0 | Hold |
| 10 | 간혈관육종 | 99.30% | L5 | S0 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터(`original_moa`)는 확보되지 않았습니다(Data Gap, DG002). 다만 각 예측 후보의 기전 근거(`repurposing_rationale`)에 공통적으로 기술된 정보에 따르면, canakinumab은 **IL-1β를 표적으로 하는 항 IL-1β 단일클론항체**로 확인됩니다.

이 정보를 바탕으로 후보들을 다음과 같이 나눌 수 있습니다.

**① 기전상 타당한 후보 (자가염증질환 계열)**
FMF, PFAID, Blau 증후군은 모두 **inflammasome(NLRP3/pyrin/NLRC4/NOD2 경로) 과활성화로 IL-1β가 과다 분비되는 단일유전자 자가염증질환**이라는 공통 기전을 가집니다. FMF는 canakinumab의 실제 승인 적응증이며, TxGNN이 이를 다시 찾아낸 것은 모델의 신뢰도를 검증하는 "앵커(anchor)" 역할을 합니다. Blau 증후군과 PFAID는 동일 계열의 질환으로, "class effect(계열 효과)"에 근거해 치료적 개연성이 있습니다.

**② 기전상 근거가 약하거나 상반되는 후보**
간경색, 간자반증, 간혈관육종, 모노소미 X, 피부외 비만세포종은 혈관 폐쇄·염색체 이상·종양 등 **IL-1β가 핵심 기전이 아닌 병태생리**를 가지고 있어, TxGNN 고득점이 실제 인과관계보다는 지식그래프 임베딩상의 "간(肝) 관련 노드 근접성" 등 인공물(artifact)을 반영했을 가능성이 근거 텍스트에 명시되어 있습니다.

**③ 오히려 안전성 우려가 있는 후보**
복합 면역결핍 증후군은 IL-1β 억제가 오히려 감염 위험을 높일 수 있어, 치료 기회가 아닌 **잠재적 안전성 경고 신호**로 해석해야 합니다.

---

## 임상시험 근거

10개 예측 질환 전체(hepatic infarction, hepatic veno-occlusive disease, peliosis hepatis, syndrome with combined immunodeficiency, PFAID, FMF, extracutaneous mastocytoma, Blau syndrome, monosomy X, liver angiosarcoma)에 대해 ClinicalTrials.gov 및 ICTRP를 조회한 결과, **현재 관련 임상시험 등록이 없습니다** (query_log 기준 전체 0건).

> ⚠️ 다만 FMF의 경우, 근거 텍스트에 "본 데이터베이스의 0건 표시는 실제 임상시험 부재가 아니라 자료 수집 공백(data collection gap)"이라고 명시되어 있습니다. FMF는 canakinumab의 실제 승인 적응증으로 다수의 등록 임상시험이 존재할 것으로 추정되나, 이번 Evidence Pack 수집 과정에서 누락되었습니다.

---

## 문헌 근거

동일하게 10개 예측 질환 모두 PubMed 조회 결과 **현재 관련 문헌이 없습니다** (전체 0건).

> ⚠️ Blau 증후군 항목에는 "IL-1 억제 치료(canakinumab 포함)가 포도막염에 빠른 호전 효과를 보였다는 개별 증례 보고가 존재한다"는 기전 서술이 포함되어 있으나, 이 역시 본 Evidence Pack의 문헌 수집 단계에서는 반영되지 않은 자료 공백입니다.

---

## 한국 시판 정보

현재 한국(대만 규제 데이터 기준) 시판 허가 정보가 없습니다 — `total_licenses: 0`, 시판 상태: **미시판**. 등록된 허가증이 없어 별도 표를 생략합니다.

---

## 안전성 고려사항

`safety.key_warnings`, `safety.contraindications`, `safety.ddi` 항목이 모두 데이터 미확보 상태이며, 특히 이 공백은 Evidence Pack 메타데이터상 **Blocking(차단) 등급**으로 분류되어 있습니다.

> **[DG001] TFDA(현지 규제기관) 사용상 주의사항/금기 데이터 부재 — Severity: Blocking**
> 영향: 이 데이터가 확보되기 전까지 어떤 예측 후보도 S1 안전성 초기평가 단계로 진입할 수 없습니다.
> 조치 필요: 현지 규제기관 공식 사이트에서 첨부문서(仿單) PDF를 확보하여 파싱해야 합니다.

안전성 정보는 별도 확보 전까지 허가사항(원 개발사 라벨)을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold** (전체 파이프라인 기준) — 단, 후보별로 아래와 같이 세분화하여 진행을 권고합니다.

**사유:**
- 안전성 데이터(DG001)가 Blocking 등급 공백 상태로, 어떤 후보도 정식 S1 안전성 평가에 진입할 수 없습니다.
- TxGNN 점수 상위 후보(간경색, 간자반증, 간혈관육종, 모노소미 X 등)는 기전적으로 IL-1β와 직접 연관성이 낮아 근거 수준 L5로, 우선순위가 낮습니다.
- 복합 면역결핍 증후군은 치료 기회가 아닌 **안전성 경고 신호**로 재분류가 필요합니다.
- 반면 FMF(L1, 이미 승인된 적응증의 모델 재발견)는 모델 신뢰도 검증 앵커로 유효하며, Blau 증후군·PFAID(L3, class effect)는 개별 증례·소규모 연구 축적 시 등급 상향이 가능한 **연구 질문(Research Question)** 단계로 계속 추적할 가치가 있습니다.

**진행하려면 필요한 것:**
- TFDA(현지 규제기관) 사용상 주의사항·금기 데이터 확보 (DG001 해소, Blocking)
- DrugBank API를 통한 상세 작용기전(MOA) 데이터 보강 (DG002)
- FMF, Blau 증후군, PFAID에 대한 임상시험·문헌 재수집 (현재 0건 표시는 자료 수집 공백일 가능성이 근거 텍스트에 명시됨)
- 간(肝) 관련 고득점 후보(간경색·간자반증·간혈관육종)에 대해서는 지식그래프 임베딩 아티팩트 여부를 별도 검증
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

