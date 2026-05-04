---
layout: default
title: Apraclonidine Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 77
evidence_level: L5
indication_count: 0
---

# Apraclonidine Hydrochloride
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

`txgnn-pipeline` 스킬을 확인했습니다. 이 작업은 파이프라인 실행이 아닌 Evidence Pack 보고서 생성이므로 v5 프롬프트 형식에 따라 진행합니다.

---

Evidence Pack을 분석한 결과:

- `predicted_indications`: 비어 있음 (TxGNN 예측 없음)
- `original_indications`: 비어 있음
- `original_moa`: `[Data Gap]` → 표시 금지
- `taiwan_regulatory.licenses`: 0건 → 시판 정보 섹션 생략
- `safety`: 전부 `[Data Gap]` → 대체 문구 사용
- 항종양약 해당 없음 → 세포독성 섹션 생략

---

# Apraclonidine Hydrochloride: 재창출 평가 불가 — 데이터 보완 후 재실행 필요

## 한 문장 요약

Apraclonidine Hydrochloride에 대해 Evidence Pack을 수신하였으나, 기존 적응증 및 작용 기전(MOA) 데이터가 확보되지 않은 상태입니다.
TxGNN 모델의 **예측 결과가 생성되지 않았으며**, 시판 허가 기록도 없어 **현 시점에서 재창출 후보 평가를 진행할 수 없습니다.**
DrugBank ID 확인 및 규제 기관 자료 보완 후 파이프라인 재실행이 필요합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | Evidence Pack에 미포함 |
| 예측 신규 적응증 | 예측 결과 없음 |
| TxGNN 예측 점수 | — |
| 근거 수준 | L5 (예측 없음) |
| 시판 현황 | 미시판 (未上市) |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 결과가 생성되지 않았고, 기존 적응증·작용 기전(MOA)·안전성 데이터가 모두 누락되어 재창출 후보 평가를 수행할 수 없습니다. 시판 허가 기록도 없어 현지 규제 맥락 역시 확인이 불가능합니다.

**진행하려면 필요한 것:**
- DrugBank ID 및 작용 기전(MOA) 확보 (DrugBank API 조회)
- 원래 허가 적응증 정보 확보 (FDA, EMA 또는 TFDA 자료 참조)
- 안전성 정보 추출 (허가사항 PDF 다운로드 및 파싱 — DG001 해소)
- 위 데이터 보완 후 TxGNN 예측 파이프라인 재실행
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

