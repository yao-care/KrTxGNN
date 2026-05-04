---
layout: default
title: Arformoterol Tartrate
parent: 僅模型預測 (L5)
nav_order: 80
evidence_level: L5
indication_count: 0
---

# Arformoterol Tartrate
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

# Arformoterol Tartrate: 데이터 부족으로 재창출 평가 불가

## 한 문장 요약

Arformoterol Tartrate는 이번 Evidence Pack에 기존 적응증 정보, 작용 기전, 안전성 데이터가 모두 누락되어 있습니다.
TxGNN 모델에서 예측된 신규 적응증이 **0건**이며, 한국 시판 이력도 존재하지 않습니다.
현재 상태로는 재창출 가능성을 판단할 수 없으며, **데이터 보완 후 재평가**가 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (Evidence Pack 미포함) |
| 예측 신규 적응증 | 없음 (TxGNN 예측 결과 0건) |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | L5 (모델 예측 없음, 실제 연구 미확인) |
| 한국 시판 현황 | 미상시 |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 한국 시판 정보

해당 약물의 한국 내 허가 이력이 존재하지 않습니다. 현재 국내 시판 이력 및 허가증이 0건으로 확인됩니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 결과가 전혀 생성되지 않았으며, 기존 적응증·작용 기전·안전성 데이터가 모두 누락되어 있어 재창출 가능성을 평가할 근거가 없습니다. 본 Evidence Pack은 `Blocking` 등급 데이터 갭(DG001: TFDA 경고·금기 미확보)을 포함하고 있어 안전성 초평가 단계 진입 자체가 불가합니다.

**진행하려면 필요한 것:**
- **[DG001 - Blocking]** 한국 또는 TFDA 허가 정보 확보: 공식 허가사항(仿單) PDF 다운로드 및 경고·금기 항목 파싱
- **[DG002 - High]** 작용 기전(MOA) 확보: DrugBank API 재조회 (query_log에서 DrugBank 조회 성공 기록 있음 → 응답 내용 상세 분석 필요)
- **TxGNN 예측 재실행**: DrugBank ID 확보 후 KG 예측 파이프라인 재수행
- **규제 현황 확인**: 미국 FDA(Brovana®), 기타 허가 국가의 승인 적응증 문헌 검토

> ⚠️ **참고**: `query_log` 기준 DrugBank 조회(id: 2)는 `success` / `result_count: 1`로 기록되어 있으나, Evidence Pack에 결과가 반영되지 않았습니다. DrugBank 조회 결과 원본을 확인하여 MOA 및 DrugBank ID를 우선 복원하는 것을 권장합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

