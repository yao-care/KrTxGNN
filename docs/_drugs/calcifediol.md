---
layout: default
title: Calcifediol
parent: 모델 예측만 (L5)
nav_order: 169
evidence_level: L5
indication_count: 2
monitor_inn: "CALCIFEDIOL"
predicted_indications: ["obsolete vitamin D deficiency", "renal tubular acidosis"]
last_modified_at: 2026-10-27
description: "Calcifediol: 예측 신규 적응증 폐기된 비타민 D 결핍 (obsolete vitamin D deficiency) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202301717/EE"
---

# Calcifediol
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **2** 건
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

## Calcifediol: 비타민 D 대사체 → 폐기된 비타민 D 결핍 (obsolete vitamin D deficiency)
{: .text-alpha }

## 한 문장 요약

Calcifediol은 25-하이드록시비타민 D3로, 순환 혈중 비타민 D의 주요 대사체이자 칼시트리올의 직접적인 전구체입니다.
TxGNN 모델은 **폐기된 비타민 D 결핍(obsolete vitamin D deficiency)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**이어서 모델 예측 단계에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202301717/EE |
| 예측 신규 적응증 | 폐기된 비타민 D 결핍 (obsolete vitamin D deficiency) |
| TxGNN 예측 점수 | 0.9999 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 1건 (단일제 1건, 유효) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 수집되지 않았습니다. 다만 Calcifediol은 간에서 만들어지는 비타민 D3의 25-수산화 대사체로, 활성형인 칼시트리올의 직접 전구체입니다. 따라서 비타민 D 결핍 상태를 교정하는 데 기전상 적용 가능성이 있습니다.

다만 이 질환명은 온톨로지에서 폐기(obsolete) 처리된 용어입니다. 높은 예측 점수는 현재 사용되는 비타민 D 결핍 관련 용어와 겹치는 과거 명칭을 반영했을 가능성이 크며, 진정한 의미의 새로운 재창출 기회라고 보기는 어렵습니다. 이 예측을 뒷받침하는 임상시험이나 문헌도 확인되지 않았습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202301717 | 칼디올연질캡슐20마이크로그램(칼시페디올)(수출용) | 연한 살색의 타원형 연질캡슐 (무색~미황색 투명 내용액) | 적응증 텍스트 미기재 |

## 안전성 고려사항

- **약물 상호작용**: 총 57건이 확인되었으며, 주요(Major) 등급은 다음과 같습니다.
  - Cholecalciferol
  - Calcitriol
  - Burosumab
- 중등도(Moderate) 등급 상호작용에는 다음이 포함됩니다.
  - 항경련제: fosphenytoin, carbamazepine, 바르비튜레이트계(amobarbital, butalbital, butabarbital)
  - 티아지드계 이뇨제: hydrochlorothiazide, chlorothiazide, chlorthalidone 등
  - 담즙산 결합제: cholestyramine, colesevelam, colestipol
  - 기타: 수산화알루미늄, 국소 칼시포트리올, digitoxin

허가사항의 경고 및 금기는 이번 자료에서 확인되지 않았으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 질환명이 폐기된 용어이고, 직접 연구한 임상시험과 문헌이 없어 근거가 모델 예측뿐(L5)입니다. 기존 비타민 D 결핍 관련 용도와 중복되는 개념일 가능성이 높습니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기·적응증)의 확보 및 분석
- 상세한 약물 작용 기전(MOA) 데이터
- 현행 질환 용어와의 대응 관계 정리 및 해당 질환을 직접 다룬 임상시험·문헌 확인
- 한국 시판·허가 상태 확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

