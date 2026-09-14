---
layout: default
title: Trastuzumab Deruxtecan
parent: 僅模型預測 (L5)
nav_order: 695
evidence_level: L5
indication_count: 1
---

# Trastuzumab Deruxtecan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Trastuzumab Deruxtecan: HER2 표적 항암제에서 약물유발성 골다공증으로

## 한 문장 요약

Trastuzumab Deruxtecan(T-DXd)은 HER2를 표적으로 하는 항체-약물 복합체(ADC)로, 국내에는 아직 허가되지 않은 약물입니다. TxGNN 모델은 **약물유발성 골다공증(Drug-induced Osteoporosis)**에 효과가 있을 수 있다고 예측했으나, 현재 이를 뒷받침하는 **임상시험이나 문헌은 전혀 없으며**, 기전적으로도 모순되는 예측으로 판단됩니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (한국 미허가, HER2 표적 항체-약물 복합체로 분류) |
| 예측 신규 적응증 | 약물유발성 골다공증 (Drug-induced Osteoporosis) |
| TxGNN 예측 점수 | 99.31% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미상영 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Trastuzumab Deruxtecan은 HER2 표적 항체에 topoisomerase I 억제제(DXd) 계열의 세포독성 페이로드를 결합한 항체-약물 복합체(ADC)입니다. 상세한 작용기전(MOA) 데이터는 현재 확보되지 않았지만(Data Gap), 근거팩에 기재된 기전 요약에 따르면 이 약물은 골대사 조절 경로(RANKL/OPG, 파골세포 활성)와 직접적인 연관성이 알려져 있지 않습니다.

오히려 세포독성 화학요법 계열 약물은 임상적으로 **화학요법 유발성 골질 손실(chemotherapy-induced bone loss)**을 부작용으로 유발하는 경우가 많으며, 이는 치료 기전이 아니라 잠재적 이상반응에 해당합니다. 즉 이번 예측은 "치료 효과"가 아니라 "약물 부작용"과 혼동되었을 가능성이 있으며, 생물학적으로 모순되는 방향으로 판단되어 높은 의심이 필요합니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 세포독성

이 약물은 세포독성 페이로드(topoisomerase I 억제제, DXd)를 탑재한 항체-약물 복합체(ADC)로 분류되는 항종양제입니다.

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 기반 ADC (HER2 표적 항체 + topoisomerase I 억제제 페이로드) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 세포독성 의약품 취급 규정 준수 필요 (ADC 페이로드 특성상 표준 세포독성 약물에 준하는 취급 권장) |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 근거 수준이 L5(모델 예측만 존재, 실제 임상 근거 없음)이며, 기전적으로도 골다공증 치료 효과가 아닌 골질 손실 부작용과 혼동되었을 가능성이 있어 생물학적 타당성이 낮습니다.
- 안전성 정보(TFDA 경고/금기, DG001)가 Blocking 수준으로 누락되어 있어 안전성 초기 평가(S1) 단계 진입이 불가능합니다.

**진행하려면 필요한 것:**
- DrugBank API를 통한 상세 작용기전(MOA) 데이터 확보 (DG002)
- TFDA 공식 허가사항(경고/금기) 확보 및 파싱 (DG001, Blocking)
- 골대사 관련 기전 문헌 또는 전임상 근거 추가 확인 — 현재는 예측 방향 자체의 재검토 필요
- 국내 허가 여부 및 글로벌 승인 적응증 정보 보완
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

