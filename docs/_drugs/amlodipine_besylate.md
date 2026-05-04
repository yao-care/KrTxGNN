---
layout: default
title: Amlodipine Besylate
parent: 僅模型預測 (L5)
nav_order: 62
evidence_level: L5
indication_count: 0
---

# Amlodipine Besylate
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

# Amlodipine Besylate: 데이터 부족으로 재창출 평가 보류

## 한 문장 요약

Amlodipine Besylate의 Evidence Pack에는 기존 적응증, 작용 기전(MOA), TxGNN 예측 신규 적응증 데이터가 모두 누락되어 있습니다.  
DrugBank 조회는 1건 성공하였으나 DrugBank ID가 추출되지 않아 예측 파이프라인이 실행되지 않았고,  
현재 한국 시판 허가 이력이 **0건**으로 확인되어 안전성·근거 평가를 진행할 수 없는 상태입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 |
| 예측 신규 적응증 | 없음 (TxGNN 예측 미실행) |
| TxGNN 예측 점수 | 없음 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미상장 |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**  
TxGNN 예측 결과가 없고, 기존 적응증·작용 기전·안전성 데이터가 모두 누락되어 있어 재창출 평가의 어떤 단계도 수행할 수 없습니다. DrugBank 조회는 성공(1건)했으나 ID가 연결되지 않아 파이프라인 전체가 중단된 상태입니다.

**진행하려면 필요한 것:**

| 우선순위 | 항목 | 조치 방법 |
|----------|------|-----------|
| 🔴 Blocking | 허가사항 경고·금기 데이터 (DG001) | TFDA 공식 사이트에서 허가사항 PDF 다운로드 및 파싱 |
| 🟠 High | 작용 기전 (MOA) 데이터 (DG002) | DrugBank API에서 `amlodipine` 으로 재조회, DrugBank ID 수동 매핑 |
| 🟠 High | DrugBank ID 미연결 문제 해결 | 조회 키워드 검토 — `AMLODIPINE BESYLATE` → `amlodipine` 으로 정규화 후 재시도 |
| 🟡 Medium | 한국 시판 현황 재확인 | 조회 약물명 정규화 후 MFDS 허가 DB 재조회 |
| 🟡 Medium | TxGNN 예측 재실행 | DrugBank ID 확보 후 KG·DL 예측 파이프라인 재구동 |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

