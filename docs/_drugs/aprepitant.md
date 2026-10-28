---
layout: default
title: Aprepitant
parent: 모델 예측만 (L5)
nav_order: 81
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Aprepitant: 예측 신규 적응증 신장성 항이뇨 부적절 증후군 (nephrogenic syndrome of inappropriate antidiuresis) (근거 수준 L5). 기존 적응증: 허가 적응증 텍스트 없음 (허가증 링크만 확인됨)"
monitor_inn: "Aprepitant"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "hypertrichosis (disease)", "pulmonary hypertension", "leprosy", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "kyphoscoliotic heart disease", "syndrome with a Dandy-Walker malformation as major feature", "subarachnoid hemorrhage (disease)", "isolated genetic hair shaft abnormality"]
---

# Aprepitant
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 약사 평가 보고서

</div>

## Aprepitant: 항구토 적응증에서 신장성 항이뇨호르몬 부적절 분비 증후군으로
{: .text-alpha }

## 한 문장 요약

Aprepitant는 NK1 수용체 길항제로, 한국에서 단일제 캡슐로 허가되어 시판 중입니다. 다만 허가 적응증 원문은 이번에 확보한 자료에 텍스트로 포함되어 있지 않습니다.
TxGNN 모델은 **신장성 항이뇨 부적절 증후군(nephrogenic syndrome of inappropriate antidiuresis)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험은 0건, 직접 관련 문헌도 0편**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 텍스트 없음 (허가증 링크만 확인됨) |
| 예측 신규 적응증 | 신장성 항이뇨 부적절 증후군 (nephrogenic syndrome of inappropriate antidiuresis) |
| TxGNN 예측 점수 | 0.9997 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 4건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 없습니다. 알려진 정보에 따르면 Aprepitant는 NK1(substance P) 수용체 길항제입니다. substance P/NK1 신호가 바소프레신 관련 경로를 통해 수분 균형에 관여할 가능성은 있으나, 가설 수준입니다.

신장성 항이뇨 부적절 증후군(nephrogenic SIAD)은 바소프레신 V2 수용체(AVPR2)의 활성화 돌연변이로 발생합니다. 이는 중추 NK1 차단 효과보다 하류에서 일어나는 변화이므로, 기전상 연결고리는 약합니다. 높은 TxGNN 점수는 계산상 예측일 뿐입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 이 적응증과 직접 관련된 문헌이 없습니다.

참고로 3순위 예측 질환인 폐고혈압에서 검색된 1편(PMID 28261651)은 Aprepitant와 무관한 pazopanib+cisplatin 1상 시험으로, 잘못 연결된 결과로 판단됩니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202200038 | 아탄트캡슐125밀리그램 | 경질캡슐 (상부 분홍색, 하부 흰색) | 허가사항 참조 |
| 202200037 | 아탄트캡슐80밀리그램 | 경질캡슐 (흰색) | 허가사항 참조 |
| 200610725 | 에멘드캡슐80밀리그램 | 경질 젤라틴 캡슐 (흰색) | 허가사항 참조 |
| 200610726 | 에멘드캡슐125밀리그램 | 경질 젤라틴 캡슐 (상부 분홍색, 하부 흰색) | 허가사항 참조 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 일부 주요 항목은 다음과 같습니다.
  - **Major**: Fentanyl, Alfentanil, Acalabrutinib
  - **Moderate**: Paclitaxel, Abemaciclib, Nifedipine, Ibuprofen, Hydrocortisone, Levonorgestrel, Fluvoxamine, Gefitinib 등
  - **Minor**: Dolutegravir

그 외 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 매우 높지만 임상시험과 문헌 근거가 전혀 없고(L5), 질환의 원인인 V2 수용체 활성화 돌연변이는 NK1 차단으로 설명하기 어렵습니다. 현 단계에서 진행하기에는 근거가 부족합니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기 포함) 확보 및 분석
- 상세한 작용 기전 데이터(MOA) 확보
- substance P/NK1과 바소프레신 경로의 연관성을 보여주는 전임상 또는 기전 연구
- 참고: 예측 목록 중 지주막하출혈은 기전상 가장 개연성이 있으나, 이 역시 현재 근거는 없으며 우선 검토 대상으로 고려할 수 있음
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

