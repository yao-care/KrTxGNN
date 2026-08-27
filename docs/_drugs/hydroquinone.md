---
layout: default
title: Hydroquinone
parent: 僅模型預測 (L5)
nav_order: 302
evidence_level: L5
indication_count: 4
---

# Hydroquinone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Hydroquinone: 대만 미상영 의약품에서 지루성 각화증(Seborrheic Keratosis)으로

## 한 문장 요약

Hydroquinone(DrugBank ID: DB09526)은 대만에서 시판 허가가 없는 의약품으로, 현재 기존 승인 적응증 및 작용기전(MOA) 정보가 확보되지 않은 상태입니다.
TxGNN 모델은 **지루성 각화증(Seborrheic Keratosis)**에 효과가 있을 수 있다고 예측하며(예측 점수 99.73%), 현재 **직접 관련 임상시험은 없고 문헌 2편**만이 간접적으로 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (대만 미상영 의약품, 허가증 0건) |
| 예측 신규 적응증 | 지루성 각화증 (Seborrheic Keratosis) |
| TxGNN 예측 점수 | 99.73% |
| 근거 수준 | L4 |
| 한국 시판 현황 | ✗ 미상영 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Hydroquinone은 타이로시나제(tyrosinase)를 억제하여 멜라닌 생성을 감소시키는 기전으로 작용하는 것으로 알려져 있습니다. 이 기전은 이론상 지루성 각화증 및 그 변이형인 흑색구진성 피부병(dermatosis papulosa nigra, DPN)의 색소 침착 외관을 완화시킬 수 있습니다. 다만 이는 각질 증식(keratotic proliferation) 자체—즉 병의 본질적 병리—에는 작용하지 않는 **대증적 치료**이며, 병인 치료가 아닙니다.

현재 확보된 문헌 2편 모두 지루성 각화증을 주요 연구 대상으로 하지 않습니다. PMID 33046430은 아시아인 환자의 안면 색소질환 복합치료에 대한 전향적 관찰연구로 색소질환 전반을 다루며, SK를 특정하지 않습니다. PMID 17373158은 DPN(SK의 변이형) 치료옵션 리뷰로, hydroquinone이 보조적 미백 옵션으로 언급될 가능성은 있으나 DPN의 표준 치료는 냉동치료·전기소작 등입니다.

**Hydroquinone이 지루성 각화증 치료에 직접 효과가 있음을 검증한 임상시험은 현재까지 없습니다.** 또한 상세 작용기전(MOA) 데이터는 아직 구조화되어 확보되지 않았습니다(DrugBank API 조회 필요).

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [17373158](https://pubmed.ncbi.nlm.nih.gov/17373158/) | 2007 | Review | Journal of drugs in dermatology : JDD | 흑색구진성 피부병(DPN, SK의 변이형) 치료옵션 리뷰. 조직학적으로 SK와 유사하며, 미용적 제거가 주된 치료 목적임을 설명 |
| [33046430](https://pubmed.ncbi.nlm.nih.gov/33046430/) | 2021 | Cohort | Journal of plastic, reconstructive & aesthetic surgery : JPRAS | 아시아인 환자 대상 안면 색소질환 복합치료 알고리즘에 대한 전향적 관찰연구. 여러 색소질환이 동시 발생하는 경우가 많음을 보고 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 예측 신규 적응증(지루성 각화증)에 대한 직접적인 임상시험이 전혀 없고, 확보된 문헌 2편도 SK를 주요 연구 대상으로 하지 않아 근거 수준이 L4(전임상/기전 추정 수준)에 불과합니다.
- 안전성 초기평가(S1)에 필수적인 TFDA 허가사항(경고·금기) 정보가 확보되지 않아(DG001, **Blocking**) 안전성 평가 자체가 진행 불가능한 상태입니다.
- 대만 내 시판 허가가 없는 의약품으로, 기존 승인 적응증 정보 자체가 부재합니다.

**진행하려면 필요한 것:**
- TFDA 공식 사이트에서 Hydroquinone 허가사항(경고·금기) 확보 — 안전성 평가 진입을 위한 필수 선행 조건 (DG001, Blocking)
- DrugBank API를 통한 정확한 작용기전(MOA) 데이터 확보 (DG002, High)
- 지루성 각화증에 특화된 전향적 연구 또는 임상시험 데이터 확보
- **참고**: 이번 Evidence Pack에 포함된 3순위 예측 적응증 'exanthem'은 첨부된 임상시험 7건이 실제로는 모두 기미(melasma)/색소침착 관련 연구이며 exanthem(발진성 질환)과 임상적으로 무관합니다. TxGNN 질병 매핑 오류 가능성이 있어 별도 데이터 품질 검토가 필요합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

