---
layout: default
title: Avatrombopag Maleate
parent: 僅模型預測 (L5)
nav_order: 105
evidence_level: L5
indication_count: 0
---

# Avatrombopag Maleate
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

# Avatrombopag Maleate: 필수 데이터 미수집으로 평가 보류

---

## 한 문장 요약

Avatrombopag Maleate에 대한 약물 재창출 평가를 시도하였으나, 허가 적응증·작용 기전·TxGNN 예측 결과가 모두 누락된 상태입니다. 현재 Evidence Pack에는 평가를 진행하기 위한 최소 요건이 갖추어져 있지 않으며, **DG001(허가사항·Blocking)**과 **DG002(MOA·High)** 두 건의 데이터 갭이 해소된 후 재수집·재실행이 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 데이터 미수집 |
| 예측 신규 적응증 | TxGNN 예측 결과 없음 |
| TxGNN 예측 점수 | — |
| 근거 수준 | 평가 불가 |
| 한국 시판 현황 | 미시판 (未上市) |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증이 없고, 약물 기본 정보(허가 적응증·작용 기전·안전성 경고)가 모두 미수집 상태로 재창출 가능성 평가를 진행할 수 없습니다. DrugBank 쿼리는 성공(result_count: 1)하였으나 DrugBank ID가 반영되지 않아 모델 예측 실행의 선행 조건이 충족되지 않았습니다.

**진행하려면 필요한 것:**
- **DG001 (Blocking)** 허가사항 수집: TFDA 관방 사이트에서 仿單 PDF 다운로드 및 파싱 → 허가 적응증·경고·금기사항 확보
- **DG002 (High)** DrugBank ID 등록: DrugBank API 쿼리 결과(성공 1건)를 바탕으로 `drug.drugbank_id` 확보 및 MOA 입력
- 위 두 항목 해소 후 TxGNN 모델 예측 재실행 및 Evidence Pack v5 재생성
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

