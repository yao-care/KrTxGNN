---
layout: default
title: Abacavir Sulfate
parent: 僅模型預測 (L5)
nav_order: 11
evidence_level: L5
indication_count: 0
---

# Abacavir Sulfate
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

Evidence Pack을 분석했습니다. `predicted_indications` 배열이 비어 있고 핵심 데이터 갭이 다수 존재하는 특수 케이스입니다. 표준 형식을 기반으로 하되, 데이터가 없는 섹션은 규칙에 따라 생략하고 현황을 정확히 반영한 보고서를 작성합니다.

---

# Abacavir Sulfate: TxGNN 예측 결과 없음 — 평가 보류

## 한 문장 요약

Abacavir Sulfate는 HIV-1 감염 치료에 사용되는 항바이러스제로, 국제적으로 뉴클레오시드 역전사효소 억제제(NRTI) 계열로 분류되어 있습니다.
이번 Evidence Pack에는 **TxGNN 예측 적응증이 없으며**, 작용 기전(MOA), 한국 시판 정보, 안전성 경고 등 핵심 데이터에 **중대한 갭**이 존재합니다.
현재 상태로는 재창출 가능성 평가를 진행할 수 없으며, 데이터 보완 후 재실행이 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (한국 MFDS 허가 데이터 미수록) |
| 예측 신규 적응증 | 없음 (TxGNN 파이프라인 예측 결과 없음) |
| TxGNN 예측 점수 | — |
| 근거 수준 | 평가 불가 (예측 없음) |
| 한국 시판 현황 | ✗ 미시판 (데이터 파이프라인 재확인 필요) |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

> ⚠️ **데이터 정합성 주의**: Abacavir Sulfate는 국제적으로 Ziagen, Kivexa, Triumeq 등 복합제로 광범위하게 시판되고 있습니다. 한국 MFDS 허가가 0건으로 조회된 것은 데이터 수집 파이프라인 오류일 가능성이 있습니다. MFDS 원본 데이터를 재확인하시기 바랍니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> 📌 MFDS 공식 허가사항 조회 필요 (DG001 해소 전까지 안전성 초평가 불가)

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 적응증 결과가 없어 재창출 가능성 평가의 출발점 자체가 없으며, 한국 허가 데이터·작용 기전·안전성 경고 등 Blocking 수준의 데이터 갭이 미해소 상태입니다. 파이프라인 재실행 및 데이터 보완 없이는 어떤 단계도 진행할 수 없습니다.

**진행하려면 필요한 것:**

- **[최우선 — DG001 해소]** MFDS 또는 허가사항 PDF 파싱으로 경고·금기 정보 확보
- **[최우선 — DG002 해소]** DrugBank API 재조회로 DrugBank ID 및 MOA 확보  
  (Abacavir는 DrugBank DB01048로 등재되어 있을 가능성 높음)
- **[파이프라인 재확인]** 한국 MFDS 데이터 수집 로직 점검 — 0건은 파이프라인 오류 의심
- **[TxGNN 재실행]** DrugBank 매핑 성공 후 KG 및 DL 예측 재실행
- **[DDI 재조회]** DrugBank ID 확보 후 약물 상호작용 재쿼리
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

