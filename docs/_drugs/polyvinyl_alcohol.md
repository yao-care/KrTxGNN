---
layout: default
title: Polyvinyl Alcohol
parent: 모델 예측만 (L5)
nav_order: 614
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
monitor_inn: "POLYVINYL ALCOHOL"
predicted_indications: ["congenital ichthyosiform erythroderma", "self-healing collodion baby", "lamellar ichthyosis", "bathing suit ichthyosis"]
description: "Polyvinyl Alcohol: 예측 신규 적응증 선천성 어린선증양 홍색피부증 (congenital ichthyosiform erythroderma) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201503557/EE"
---

# Polyvinyl Alcohol
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **4** 건
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

## Polyvinyl Alcohol: 선천성 어린선증양 홍색피부증 (congenital ichthyosiform erythroderma)
{: .text-alpha }

## 한 문장 요약

Polyvinyl alcohol(폴리비닐알코올)은 한국에서 점안액 성분으로 허가되어 사용되어 왔습니다.
TxGNN 모델은 **선천성 어린선증양 홍색피부증(Congenital Ichthyosiform Erythroderma)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 **임상시험과 문헌은 한 건도 확인되지 않았습니다.** 모델 예측 단계의 가설입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201503557/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200908143/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201101693/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199500494/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201004679/EE;  |
| 예측 신규 적응증 | 선천성 어린선증양 홍색피부증 (congenital ichthyosiform erythroderma) |
| TxGNN 예측 점수 | 0.9990 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 6건 |
| 권장 결정 | Hold |

기타 예측 후보: 자연 치유성 콜로디온 아기(0.9983), 층판 어린선증(0.9972), 수영복 어린선증(0.9954). 모두 L5, Hold입니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 폴리비닐알코올은 막을 형성하는 수용성 고분자로, 점안액에서 윤활·보습 목적으로 사용됩니다.

가설상으로는 피부 표면에 보습막 또는 폐쇄막을 형성하여 경피 수분 손실을 줄이고 피부 장벽 기능을 일시적으로 보조할 가능성이 있습니다. 다만 이는 검증되지 않은 추정이며, 뒷받침하는 데이터가 없습니다.

선천성 어린선증양 홍색피부증은 유전성 각화 장애이므로, 효과가 있더라도 근본 치료가 아닌 증상 완화 수준에 그칠 것입니다. 층판 어린선증과 수영복 어린선증은 주로 TGM1 변이와 관련되며, 폴리비닐알코올이 이 경로에 작용한다는 근거는 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201503557 | 한림피브이에이점안액(수출용) | 점안액 | 허가 적응증 본문 미확인 (허가 문서 참조) |
| 200908143 | 티어리칸점안액(수출용) | 점안액 | 허가 적응증 본문 미확인 (허가 문서 참조) |
| 201101693 | 트리플액션리리프점안액(수출용) | 점안액 | 허가 적응증 본문 미확인 (허가 문서 참조) |
| 199500494 | 루버리칸점안액(수출용) | 점안액 | 허가 적응증 본문 미확인 (허가 문서 참조) |
| 201004679 | 한뮤린점안액(수출용) | 점안액 | 허가 적응증 본문 미확인 (허가 문서 참조) |

허가증은 총 6건이며 모두 단일제, 유효 상태입니다. 모두 수출용 점안액이고 외용 피부제형은 없습니다. 나머지 1건은 루테리칸점안액(201103131, 수출용)입니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

참고로 지식그래프상 금기 질환 연결에는 고혈압, 당뇨병, 심장질환, 폐쇄각 녹내장, 갑상선기능항진증, 동맥경화 등이 있습니다. 이는 허가 문서가 아닌 모델 지식그래프에서 유래한 것이므로 참고용으로만 보아야 합니다. 약물 상호작용 정보는 확인되지 않았습니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 높지만 임상시험과 문헌이 전혀 없고 작용 기전 자료도 없어 근거가 모델 예측뿐(L5)입니다. 또한 현재 허가 제형이 점안액이므로, 피부 적용을 위한 제형 및 경로 적합성이 확인되지 않았습니다.

**진행하려면 필요한 것:**
- 허가사항의 경고·금기 정보 확보 (현재 확인 불가 상태이며 안전성 검토의 선행 조건)
- 작용 기전(MOA) 데이터 확보
- 피부 적용 시 경피 흡수와 안전성 평가, 특히 신생아 피부 적용 여부 검토
- 어린선증 환자 대상 전임상 또는 소규모 탐색 연구 등 최소한의 실증 근거
- 국소 피부용 제형의 경로 적합성 평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

