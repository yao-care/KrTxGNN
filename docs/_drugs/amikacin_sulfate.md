---
layout: default
title: Amikacin Sulfate
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L5
indication_count: 0
---

# Amikacin Sulfate
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

# Amikacin Sulfate: 재창출 평가 불가 — TxGNN 예측 적응증 없음

---

## 한 문장 요약

Amikacin Sulfate는 아미노글리코사이드 계열 항생제로 알려진 약물이나, 이번 Evidence Pack에는 기존 적응증 및 작용 기전 데이터가 포함되지 않았습니다.
TxGNN 모델의 예측 적응증이 생성되지 않아 신규 적응증 후보를 평가할 수 없는 상태이며,
임상시험·문헌 근거 또한 확보되지 않았습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (허가 데이터 없음) |
| 예측 신규 적응증 | 없음 (TxGNN 예측 미생성) |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | 평가 불가 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증이 생성되지 않았고, 기존 적응증 및 작용 기전(MOA) 데이터가 모두 누락되어 재창출 가능성을 평가할 수 없습니다. DrugBank 조회는 성공(1건)하였으나 결과가 Evidence Pack에 반영되지 않아 후속 처리가 필요합니다.

**진행하려면 필요한 것:**
- DrugBank 조회 결과(DrugBank ID, MOA, 적응증, 경고)를 Evidence Pack에 반영 후 TxGNN 예측 재실행 — DG002 해소 필수
- 허가사항(MFDS/TFDA) PDF 검토를 통한 경고·금기 항목 확보 — DG001 해소 필수
- 예측 적응증 확보 후 임상시험(ClinicalTrials.gov, CRIS) 및 PubMed 근거 수집 재진행
- 해당 시장 내 시판 현황 재확인 (현재 허가 0건)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

