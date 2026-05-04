---
layout: default
title: Amphotericin B
parent: 僅模型預測 (L5)
nav_order: 68
evidence_level: L5
indication_count: 0
---

# Amphotericin B
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

Evidence Pack 분석 완료. `predicted_indications: []`이고 `original_indications: []`이며 한국 허가 없음(0건)인 상태입니다. 데이터 부족 케이스로 적용 가능한 섹션만 출력합니다.

---

# AMPHOTERICIN B: 예측 데이터 부족으로 재창출 평가 대기 중

---

## 한 문장 요약

AMPHOTERICIN B(DB00681)는 한국 미시판 약물로, 현재 허가 적응증 데이터와 작용 기전(MOA) 정보가 모두 누락되어 있습니다.
TxGNN 모델의 예측 결과가 생성되지 않아 **신규 적응증 후보가 존재하지 않으며**, 이에 따라 임상시험·문헌 근거 분석도 진행할 수 없는 상태입니다.
핵심 데이터(원래 적응증, MOA, TxGNN 예측값) 보완 후 재평가가 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 |
| 예측 신규 적응증 | 없음 (TxGNN 예측 미생성) |
| TxGNN 예측 점수 | 없음 |
| 근거 수준 | 평가 불가 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
`predicted_indications` 배열이 비어 있어 TxGNN이 재창출 후보 적응증을 산출하지 못했으며, 기존 적응증·MOA 데이터도 모두 누락되어 있어 재창출 타당성 분석의 최소 요건을 충족하지 못합니다.

**진행하려면 필요한 것:**

- **[필수 — Blocking]** 기존 허가 적응증 확보: 한국 MFDS 또는 WHO/DrugBank에서 원래 승인 적응증 조회
- **[필수 — High]** 작용 기전(MOA) 확보: DrugBank API(DB00681) 조회하여 `mechanism_of_action` 필드 추출
- **[필수]** TxGNN 예측 재실행: 위 두 데이터를 보완한 뒤 KG·DL 예측 파이프라인 재실행 (`scripts/run_kg_prediction.py`)
- **[권장]** 안전성 데이터 확보: MFDS 허가사항 PDF 다운로드 및 경고·금기사항 파싱
- **[권장]** 한국 시판 현황 재확인: MFDS 의약품통합정보시스템(nedrug.mfds.go.kr) 재조회
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

