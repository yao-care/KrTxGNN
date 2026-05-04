---
layout: default
title: Atorvastatin Calcium Trihydrate
parent: 僅模型預測 (L5)
nav_order: 96
evidence_level: L5
indication_count: 0
---

# Atorvastatin Calcium Trihydrate
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

Evidence Pack 분석 완료. `predicted_indications`가 비어 있고 대부분의 필드가 데이터 갭 상태이므로, 보고서 형식을 준수하면서 현 상황을 정확히 반영합니다.

---

# Atorvastatin Calcium Trihydrate: TxGNN 예측 없음 — 평가 보류

## 한 문장 요약

Atorvastatin Calcium Trihydrate는 스타틴(Statin) 계열의 약물로, HMG-CoA 환원효소 억제를 통한 콜레스테롤 저하 및 심혈관 질환 예방에 사용되는 것으로 알려져 있습니다.
현재 Evidence Pack에는 **TxGNN이 예측한 신규 적응증이 없으며**, 한국 허가 데이터와 안전성 정보도 확인되지 않아 약물 재창출 평가를 완전히 수행하기 어렵습니다.
DrugBank ID 미확정 및 한국 시판 데이터 부재로 인해 **추가 데이터 수집 후 재평가**가 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | 데이터 없음 (TxGNN 예측 미수행) |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | L5 (모델 예측 부재) |
| 한국 시판 현황 | ✗ 미확인 (未上市) |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 이 예측이 타당한 이유는?

현재 TxGNN 예측 결과가 없어 신규 적응증에 대한 기전 분석을 수행할 수 없습니다.

Atorvastatin Calcium Trihydrate는 Atorvastatin의 칼슘 삼수화물 염 형태입니다. 일반적으로 이 성분은 HMG-CoA 환원효소를 억제하여 간에서의 콜레스테롤 합성을 줄이는 기전으로 알려져 있으나, 본 Evidence Pack에는 공식 MOA 데이터가 포함되어 있지 않습니다.

DrugBank ID가 확정되지 않은 상태로, 지식 그래프(KG) 기반 예측이 정상적으로 수행되지 않았을 가능성이 높습니다. DrugBank 조회는 성공(success)으로 기록되었으나 ID가 반환되지 않아, 약물명 정규화 또는 매핑 단계에서 불일치가 발생했을 것으로 추정됩니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증 데이터가 전무하고, DrugBank ID 미확정으로 인해 지식 그래프 기반 재창출 후보 생성 자체가 이루어지지 않았습니다. 한국 허가 데이터 및 안전성 정보도 부재하여 평가를 진행할 수 없습니다.

**진행하려면 필요한 것:**
- **DrugBank ID 확정**: `ATORVASTATIN CALCIUM TRIHYDRATE` → `DB01076 (Atorvastatin)` 매핑 수동 검토
- **TxGNN 예측 재실행**: DrugBank ID 확정 후 KG 및 DL 예측 재수행
- **한국 MFDS 허가 데이터 조회**: 약물명 변형(`아토르바스타틴`, `Atorvastatin`) 으로 재검색
- **MOA 데이터 수집**: DrugBank API 재조회 (`DB01076`)
- **안전성 정보 확보**: MFDS 허가사항 PDF 다운로드 후 경고·금기 항목 파싱
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

