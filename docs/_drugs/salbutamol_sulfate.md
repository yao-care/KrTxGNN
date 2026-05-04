---
layout: default
title: Salbutamol Sulfate
parent: 僅模型預測 (L5)
nav_order: 302
evidence_level: L5
indication_count: 0
---

# Salbutamol Sulfate
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

Evidence Pack을 분석했습니다. 해당 약물은 예측 적응증, 허가 데이터, MOA 데이터가 모두 부재한 특수 케이스입니다. 금지 사항(빈 섹션 생략, [Data Gap] 출력 금지)에 따라 보고서를 작성합니다.

---

# SALBUTAMOL SULFATE: 데이터 부재로 재창출 평가 보류

## 한 문장 요약

SALBUTAMOL SULFATE는 국제일반명(INN)으로 등록된 약물이나, 이번 Evidence Pack에는 **예측 신규 적응증 데이터가 포함되어 있지 않습니다.** 현재 시판 허가 이력이 확인되지 않으며, TxGNN 예측 결과 자체가 부재하여 약물 재창출 가능성을 평가할 수 없는 상태입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 데이터 없음) |
| 예측 신규 적응증 | 없음 |
| TxGNN 예측 점수 | — |
| 근거 수준 | L5 이하 (예측 결과 없음) |
| 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 결과, 임상시험 근거, 문헌 근거, MOA 데이터가 모두 부재하여 현 단계에서 약물 재창출 평가를 진행할 수 없습니다. 허가 데이터(총 0건)와 안전성 정보 역시 확보되지 않아 S1 안전성 초평가 진입 자체가 불가합니다.

**진행하려면 필요한 것:**

1. **TxGNN 예측 파이프라인 재실행** — `predicted_indications` 배열이 비어 있어 예측 결과가 없음. KG 예측 및 DL 예측 스크립트 실행 여부 확인 필요
2. **DrugBank ID 및 MOA 보완** — DrugBank API 쿼리는 성공(result\_count: 1)했으나 `drugbank_id`가 null인 상태. 매핑 결과를 Evidence Pack에 반영 필요
3. **허가사항 경고/금기 데이터 확보** — TFDA 또는 MFDS 공식 사이트에서 仿單 PDF 다운로드 후 파싱 (DG001 Blocking 해결)
4. **시판 현황 재확인** — SALBUTAMOL SULFATE는 전 세계적으로 광범위하게 허가된 기관지확장제로, 시판 현황 "未上市"는 데이터 파이프라인 오류 가능성이 높음. 원시 데이터 재점검 권장
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

