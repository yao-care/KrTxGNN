---
layout: default
title: Hemin
parent: 모델 예측만 (L5)
nav_order: 399
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Hemin: 예측 신규 적응증 혈소판감소성 자반증 (Thrombocytopenic Purpura) (근거 수준 L5). 기존 적응증: 허가 적응증 본문이 링크로만 제공되어 구체적인 문구를 확인할 수 없음 (MFDS 허가 문서 참조)"
monitor_inn: "Hemin"
predicted_indications: ["thrombocytopenic purpura", "hemophilia", "C1 inhibitor deficiency", "acquired coagulation factor deficiency", "serpinopathy with toxic serpin polymerization", "hereditary angioedema with C1Inh deficiency", "inherited thrombophilia", "symptomatic form of hemophilia in female carriers", "hereditary von Willebrand disease", "congenital factor XI deficiency"]
---

# Hemin
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

## Hemin: 급성 간성 포르피린증에서 혈소판감소성 자반증으로
{: .text-alpha }

## 한 문장 요약

Hemin은 헴(heme) 보충 요법제로, 주사제(놀모상주)로 알려져 있으나 한국에서는 현재 시판되지 않습니다(허가 취소 여부는 출처에 정보가 없어 확인되지 않음). TxGNN 모델(딥러닝)은 **혈소판감소성 자반증(thrombocytopenic purpura)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다. 이 예측은 TxGNN 모델(딥러닝)의 계산 결과로, 관련 질환 사이에서 모델이 학습한 유사성을 반영할 뿐이며 실제 근거는 아직 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 링크로만 제공되어 구체적인 문구를 확인할 수 없음 (MFDS 허가 문서 참조) |
| 예측 신규 적응증 | 혈소판감소성 자반증 (Thrombocytopenic Purpura) |
| TxGNN 예측 점수 | 0.9979 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 다만 Hemin은 헴 보충 요법제로, 포르피린증에서 헴 산화효소-1(HO-1)을 유도하고 간의 ALAS1 발현을 낮추는 것으로 알려져 있습니다.

이 기전과 혈소판감소성 자반증(면역성 또는 혈전성) 사이에 확립된 연관성은 없습니다. TxGNN 모델(딥러닝)의 높은 점수(0.9979)는 모델이 관련 질환 사이에서 학습한 유사성을 반영할 수 있으나, 생물학적 근거나 기전상 타당성, 임상적 효과를 의미하지 않습니다.

참고로 같은 모델이 예측한 다른 후보(혈우병, C1 억제제 결핍, 후천성 응고인자 결핍, 유전성 혈관부종, 유전성 혈전성향증, 폰빌레브란트병, 선천성 제XI인자 결핍 등)도 모두 L5 수준이며 Hold입니다. 특히 후천성 응고인자 결핍과 유전성 혈전성향증의 경우, Hemin 주입이 혈전정맥염이나 응고 이상을 일으킬 수 있어 치료 근거보다 안전성 우려가 큽니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201110836 | 놀모상주(헤민) | 진한 갈색 액이 투명한 앰플에 든 주사제 | MFDS 허가 문서 링크로만 제공됨 ([문서 보기](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201110836/EE)) |

제조사는 (주)삼오제약이며, 단일제로 유효 상태입니다.

## 안전성 고려사항

- **약물 상호작용**: 총 74건이 확인되었으며, 일부 주요 항목은 다음과 같습니다.
  - **주요(Major) 등급**: 에티닐에스트라디올, 에스트라디올, 결합형 에스트로겐, 부탈비탈, 아모바르비탈, 페노바르비탈
  - **중등도(Moderate) 등급**: 아세틸살리실산, 알테플라제, 압식시맙, 아픽사반, 디피리다몰, 아나그렐리드, 아칼라브루티닙, 항트롬빈 III, 이브리투모맙 티욱세탄 등 (항응고·항혈소판 계열이 다수)
- **응고 관련 우려**: 데이터에 따르면 Hemin 주입 시 혈전정맥염과 응고 이상이 알려진 이상반응입니다. 출혈·혈전 질환에 사용할 때는 특히 주의가 필요합니다.

경고 및 금기 사항의 상세 내용은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
혈소판감소성 자반증에 대한 임상시험과 문헌이 전혀 없고, 확립된 작용 기전도 없어 근거 수준은 L5(모델 예측만 존재)입니다. 상위 10개 예측 모두 같은 상태이며, 일부는 Hemin의 이상반응(혈전·응고 이상)과 충돌할 가능성이 있습니다.

**진행하려면 필요한 것:**
- 허가 적응증과 경고·금기 내용의 정확한 확인 (MFDS 허가 문서 내용 확보)
- Hemin의 작용 기전 데이터 (DrugBank 등)
- 혈소판감소성 자반증과 Hemin의 연관성을 보여주는 전임상 또는 기전 연구
- 혈전 및 응고 이상 위험을 고려한 안전성 평가
- 관련 임상시험 또는 문헌이 확인될 경우 근거 수준 재평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

