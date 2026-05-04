---
layout: default
title: Rosuvastatin Calcium
parent: 僅模型預測 (L5)
nav_order: 293
evidence_level: L5
indication_count: 0
---

# Rosuvastatin Calcium
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

# Rosuvastatin Calcium: 예측 적응증 없음 — 데이터 부족으로 평가 불가

---

## 한 문장 요약

Rosuvastatin Calcium은 HMG-CoA 환원효소 억제제(스타틴) 계열 약물로, 고콜레스테롤혈증 및 심혈관 질환 예방에 널리 사용됩니다.
현재 Evidence Pack에 TxGNN 예측 적응증 데이터가 존재하지 않아 재창출 후보 평가를 진행할 수 없으며,
규제 데이터베이스 매칭 오류(DG001 · DG002)로 인해 허가 정보·MOA·안전성 데이터가 모두 누락된 상태입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 데이터 미수집 (매칭 실패) |
| 예측 신규 적응증 | 예측 없음 |
| TxGNN 예측 점수 | N/A |
| 근거 수준 | 평가 불가 (예측 결과 없음) |
| 한국 시판 현황 | 미등록 (데이터 파이프라인 확인 필요) |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증이 전혀 없고, 허가 데이터·MOA·안전성 정보가 모두 누락되어 있어 현재 상태에서는 재창출 가능성 평가 자체가 불가능합니다.

**진행하려면 필요한 것:**

- **[DG001 · Blocking]** MFDS/TFDA 데이터베이스에서 "Rosuvastatin Calcium" 매칭 재시도 — 약물명 변형(예: Rosuvastatin, 로수바스타틴 등) 또는 성분명 정규화 후 재검색 필요
- **[DG002 · High]** DrugBank API를 통한 DrugBank ID 및 MOA 데이터 수집 — 쿼리 로그상 `result_status: success`이나 `drugbank_id`가 null로 반환된 원인 확인 필요
- TxGNN 예측 파이프라인 재실행 및 `repurposing_candidates` 산출 여부 확인
- 위 데이터 갭 해소 후 Evidence Pack v5 재생성 및 평가 재개
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

