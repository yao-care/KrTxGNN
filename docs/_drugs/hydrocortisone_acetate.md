---
layout: default
title: Hydrocortisone Acetate
parent: 僅模型預測 (L5)
nav_order: 300
evidence_level: L5
indication_count: 10
---

# Hydrocortisone Acetate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Hydrocortisone Acetate: 미시판 상태에서 원형탈모증(Alopecia Areata)으로

## 한 문장 요약

Hydrocortisone Acetate(DrugBank ID: DB14539)는 코르티코스테로이드 계열 성분이나, 한국 내 허가·시판 정보는 현재 등재되어 있지 않습니다.
TxGNN 모델은 **원형탈모증(Alopecia Areata)**에 효과가 있을 수 있다고 예측하며,
현재 **1건의 완료된 Phase 3 임상시험**과 **2편의 관련 문헌**이 이 방향을 뒷받침합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (한국 허가 이력 없음, 원 적응증 데이터 미확보) |
| 예측 신규 적응증 | 원형탈모증 (Alopecia Areata) |
| TxGNN 예측 점수 | 99.94% |
| 근거 수준 | L2 (완료된 Phase 3 RCT 1건) |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 Hydrocortisone Acetate의 상세한 작용 기전(MOA) 데이터는 확보되지 않았습니다. 다만 Hydrocortisone Acetate는 코르티코스테로이드(글루코코르티코이드) 계열 성분으로, 일반적으로 항염증·면역억제 작용을 통해 다양한 피부 염증성 질환에 사용되는 것으로 알려져 있습니다.

원형탈모증은 모낭을 표적으로 하는 자가면역성·염증성 질환으로, 임상적으로 국소 또는 병변내(intralesional) 코르티코스테로이드 투여가 표준 치료법 중 하나로 자리잡고 있습니다. 실제로 확보된 근거 자료를 보면, 소아 원형탈모증 환자를 대상으로 한 Phase 3 RCT에서 Hydrocortisone 1% 크림이 대조군 치료제로 사용되었고, 1973년 문헌에서는 중증 원형탈모증에 Hydrocortisone Acetate 병변내 주사 치료가 보고된 바 있습니다.

즉, TxGNN이 예측한 "코르티코스테로이드 → 자가면역성 탈모 질환"이라는 연결고리는 임상 현장에서 이미 실제로 활용되어 온 치료 접근과 기전적으로 일치하며, 이는 예측의 타당성을 뒷받침합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | 완료 | 41 | 소아 원형탈모증 환자에서 Clobetasol Propionate 0.05% 크림과 Hydrocortisone 1% 크림의 효과를 비교한 무작위 대조시험. 국소 스테로이드 치료의 임상적 활용이 흔하지만, 어떤 역가(potency)의 스테로이드가 안전하고 효과적인지에 대한 고품질 근거는 부족했던 상황에서 수행됨 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [4755919](https://pubmed.ncbi.nlm.nih.gov/4755919/) | 1973 | 증례 보고 | Przeglad dermatologiczny | 중증 원형탈모증 환자에서 Hydrocortisone Acetate 현탁액의 병변내 피하주사 치료 사례 보고 |
| [153470](https://pubmed.ncbi.nlm.nih.gov/153470/) | 1979 | 리뷰 | MMW, Munchener medizinische Wochenschrift | 신규 국소 코르티코스테로이드(fluocortin butyl ester)의 항염증 효과가 Hydrocortisone Acetate와 대등하나 전신 부작용이 적다는 점을 비교 논의한 피부질환 국소치료 동향 리뷰 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
원형탈모증에 대한 코르티코스테로이드 치료 접근 자체는 기전적으로 타당하고 완료된 Phase 3 RCT 1건이 존재하지만, 시험 규모가 작고(41명) 대상이 소아로 제한적입니다. 또한 한국 내 허가·시판 이력이 전혀 없고, 허가사항(경고·금기·DDI) 데이터가 전면 공백 상태(Blocking 등급 Data Gap)여서 안전성 초기 평가(S1) 단계에 진입할 수 없습니다.

**진행하려면 필요한 것:**
- 허가 당국(예: 한국 MFDS 또는 원 허가국) 공식 허가사항 문서 확보 – 경고, 금기, DDI 정보
- DrugBank API를 통한 상세 작용기전(MOA) 데이터 확보
- 성인 대상 및 더 큰 표본 규모의 원형탈모증 관련 임상 근거 추가 확인
- 국내 시판/허가 경로 존재 여부 및 진입 가능성 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

