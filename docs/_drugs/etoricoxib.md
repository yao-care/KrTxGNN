---
layout: default
title: Etoricoxib
parent: 僅模型預測 (L5)
nav_order: 306
evidence_level: L5
indication_count: 10
---

# Etoricoxib
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

# Etoricoxib: 미상 적응증에서 편두통(Migraine Disorder)으로

## 한 문장 요약

Etoricoxib(DrugBank DB01628)은 한국 내 시판 이력 및 기존 적응증 데이터가 확보되지 않은 COX-2 계열 약물입니다. TxGNN 모델은 **편두통(Migraine Disorder)**에 효과가 있을 수 있다고 예측(점수 99.90%)하지만, 현재 이를 뒷받침하는 **임상시험이나 문헌은 0건**으로, 모델 예측 단독 근거에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (원 적응증 데이터 미확보) |
| 예측 신규 적응증 | 편두통 (Migraine Disorder) |
| TxGNN 예측 점수 | 99.90% |
| 근거 수준 | L5 (모델 예측만 존재, 임상/문헌 증거 없음) |
| 한국 시판 현황 | 미상판매 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 Etoricoxib의 상세 작용기전(MOA) 및 기존 적응증 데이터는 확보되지 않았습니다(데이터 갭, 심각도: High — 기전 관련성 분석에 영향).

TxGNN 예측 근거에 따르면, 전립선소(prostaglandin)는 편두통의 신경성 염증 및 혈관확장 기전에 관여하며, 비선택적 NSAID는 이미 편두통 급성기 치료제로 확립되어 있습니다. Etoricoxib과 같은 COX-2 선택적 억제제도 같은 계열 추론(class inference)으로 효과 가능성이 제시되지만, **etoricoxib 자체에 대한 직접적 임상 증거는 현재 없습니다.**

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
편두통 적응증에 대해 TxGNN 모델 점수 외에 임상시험이나 문헌 근거가 전무하며(L5, S0), 약물의 작용기전(MOA)과 한국 내 허가사항/경고사항 데이터도 확보되지 않은 상태입니다(DG001 심각도 Blocking — 안전성 초기평가 S1 진입 불가). 근거 부족으로 다음 단계 진행을 보류합니다.

**진행하려면 필요한 것:**
- TFDA(식약처) 허가사항·경고/금기 문구 확보 (DG001, Blocking)
- DrugBank 작용기전(MOA) 데이터 확보 (DG002, High)
- 편두통 적응증에 대한 실제 임상시험 또는 문헌 근거
- 한국 내 시판/허가 현황 재확인

**참고:** 동일 Evidence Pack 내에서는 **두통 장애(headache disorder)** 예측(rank 9)이 가장 높은 근거 수준(L4, 문헌 5편, 근거단계 S1, "Research Question")을 보이고 있어, 향후 검토 시 편두통보다 우선순위로 고려할 만합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

