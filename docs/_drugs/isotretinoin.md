---
layout: default
title: Isotretinoin
parent: 僅模型預測 (L5)
nav_order: 410
evidence_level: L5
indication_count: 2
---

# Isotretinoin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Isotretinoin: 적응증 정보 미확보에서 악성 신혈관성 고혈압(예측)으로

## 한 문장 요약

Isotretinoin(DrugBank ID: DB00982)은 이번 Evidence Pack에서 원본 적응증과 작용기전(MOA) 정보가 확보되지 않았습니다. TxGNN 모델은 **악성 신혈관성 고혈압(Malignant Renovascular Hypertension)**에 효과가 있을 수 있다고 예측(점수 99.01%)했으나, 이를 뒷받침하는 임상시험이나 문헌은 현재 하나도 확인되지 않았습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인되지 않음 (DrugBank 조회에도 원본 적응증·MOA 정보 미확보) |
| 예측 신규 적응증 | 악성 신혈관성 고혈압 (Malignant Renovascular Hypertension) |
| TxGNN 예측 점수 | 99.01% |
| 근거 수준 | L5 (모델 예측만 있음, 실제 연구 없음) |
| 한국 시판 현황 | ✗ 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. Isotretinoin은 일반적으로 레티노산 수용체(RAR) 계열 약물로 알려져 있으나, 이번 Evidence Pack에는 원본 적응증과 MOA가 모두 확보되지 않아 신장혈관성 고혈압과의 기전상 연관성을 검증할 근거가 없습니다.

Evidence Pack 자체의 분석에 따르면, TxGNN의 99.01% 점수는 지식그래프 상의 임베딩 유사도만을 반영할 뿐 실제 기전 증거는 아닙니다. 또한 2순위 예측인 "malignant hypertensive renal disease" 역시 1순위와 동일한 점수(rank 14329, 14328로 인접)를 보이는데, 이는 독립적인 기전 가설이라기보다 TxGNN 질병 온톨로지 상 인접 노드에 대한 중복 예측일 가능성이 높습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. 다만 TFDA/MFDS 라벨의 경고·금기 정보 자체가 미확보 상태(Blocking 등급 데이터 갭)로, 안전성 초기 평가(S1) 단계로 진입할 수 없는 상황입니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 두 예측 적응증 모두 임상시험·문헌 근거가 전무한 L5 수준(모델 예측만 존재)입니다.
- 한국 내 미출시 상태이며, 안전성 라벨 정보(경고·금기)가 확보되지 않아 안전성 초기 평가조차 진행할 수 없습니다.
- 기전적 연관성도 검증 불가능한 상태입니다.

**진행하려면 필요한 것:**
- TFDA 공식 사이트에서 허가사항(경고·금기) PDF 확보 및 파싱 (Blocking 데이터 갭)
- DrugBank API를 통한 원본 적응증 및 작용기전(MOA) 재확인
- 악성 신혈관성 고혈압 관련 전임상/기전 연구 존재 여부 조사
- 한국 내 허가·시판 여부 재확인
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

