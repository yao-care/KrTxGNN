---
layout: default
title: Valsartan
parent: 僅模型預測 (L5)
nav_order: 716
evidence_level: L5
indication_count: 7
---

# Valsartan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Valsartan: 고혈압에서 악성 신혈관성 고혈압(Malignant Renovascular Hypertension)으로

## 한 문장 요약

Valsartan은 안지오텐신 II 수용체 차단제(ARB) 계열 약물로, 원래 고혈압 및 심부전 치료에 사용되었습니다.
TxGNN 모델은 **악성 신혈관성 고혈압(Malignant Renovascular Hypertension)**에 효과가 있을 수 있다고 예측하며,
현재 관련 임상시험은 없고 **1편의 동물모델 문헌**만이 이 방향을 뒷받침합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 고혈압 (국내 허가 정보 없음) |
| 예측 신규 적응증 | 악성 신혈관성 고혈압 (Malignant Renovascular Hypertension) |
| TxGNN 예측 점수 | 99.97% |
| 근거 수준 | L4 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 DrugBank의 상세 작용기전(MOA) 필드는 비어 있습니다. 다만 근거 자료에 따르면 Valsartan은 안지오텐신 II 제1형(AT1) 수용체 길항제로, angiotensin II에 의한 혈관 수축과 사구체내압 상승을 차단하는 것으로 알려져 있습니다.

기존 적응증인 고혈압과 예측된 신규 적응증인 악성 신혈관성 고혈압은 모두 RAAS(레닌-안지오텐신-알도스테론계) 과활성이 핵심 병태생리인 질환입니다. 악성 신혈관성 고혈압은 신동맥 협착으로 인한 레닌 분비 항진과 급격한 혈압 상승을 특징으로 하며, ARB의 작용기전과 직접적으로 연관됩니다.

다만 이 연관성을 뒷받침하는 근거는 현재 악성 고혈압 동물모델(쥐) 연구 1편뿐이며, 사람을 대상으로 한 임상 데이터는 아직 없습니다. 기전적 타당성은 높으나 임상적 검증은 이루어지지 않은 단계입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [11560862](https://pubmed.ncbi.nlm.nih.gov/11560862/) | 2001 | 전임상(동물연구) | Circulation | AT1 수용체 차단이 신장 염증과 연관하여 치명적 악성 고혈압 발생을 예방함을 동물모델에서 확인 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
현재 근거 수준은 L4(전임상 동물연구)에 그치며, 사람 대상 임상 데이터가 전혀 없습니다. 또한 국내 허가사항(경고, 금기, 약물상호작용) 정보가 완전히 비어 있어 안전성 초기 평가(S1) 자체가 불가능한 상태입니다.

**진행하려면 필요한 것:**
- 규제기관 허가사항 원문(경고/금기/DDI) 확보 — Blocking 등급 데이터 갭(DG001) 해소
- Valsartan의 상세 작용기전(MOA) 데이터 확보 (DrugBank API 조회, DG002)
- 악성 신혈관성 고혈압에 대한 사람 대상 연구(사례보고 이상) 존재 여부 확인
- 국내 시판 여부 및 허가 현황 재확인 (현재 미시판, 허가 0건으로 등록됨)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

