---
layout: default
title: Evolocumab
parent: 모델 예측만 (L5)
nav_order: 334
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Evolocumab: 예측 신규 적응증 혈우병 여성 보인자의 증상형 (symptomatic form of hemophilia in female carriers) (근거 수준 L5). 기존 적응증: 허가 적응증 본문은 확인되지 않음 (PCSK9 억제제로서 LDL-C 저하 치료제로 알려져 있음)"
monitor_inn: "Evolocumab"
predicted_indications: ["symptomatic form of hemophilia in female carriers", "familial apolipoprotein C-II deficiency", "thrombocytopenic purpura", "factor XI deficiency", "hemophilia A with vascular abnormality", "disease of catalytic activity"]
---

# Evolocumab
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **6** 건
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

## Evolocumab: 고콜레스테롤혈증에서 혈우병 여성 보인자의 증상형으로?
{: .text-alpha }

## 한 문장 요약

Evolocumab은 PCSK9를 억제하는 단클론항체로, 원래 LDL 콜레스테롤을 낮추는 지질 치료제로 사용되었습니다.
TxGNN 모델은 **혈우병 여성 보인자의 증상형(symptomatic form of hemophilia in female carriers)**에 효과가 있을 수 있다고 예측하지만, 현재 이 방향을 지지하는 **임상시험과 문헌은 없습니다**.
이 점수는 TxGNN 모델(딥러닝)에서 나온 것으로, 생물학적 근거가 아니라 모델이 관련 질환 사이에서 학습한 유사성을 반영할 수 있어 신중한 해석이 필요합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문은 확인되지 않음 (PCSK9 억제제로서 LDL-C 저하 치료제로 알려져 있음) |
| 예측 신규 적응증 | 혈우병 여성 보인자의 증상형 (symptomatic form of hemophilia in female carriers) |
| TxGNN 예측 점수 | 0.9982 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 2건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 이번 보고서용으로 수집된 자료에 없습니다. 다만 약물 상호작용 조회 결과에 따르면 Evolocumab은 PCSK9를 표적으로 하는 항체입니다. PCSK9를 억제하면 LDL 수용체 재순환이 늘어나 혈중 LDL-C가 낮아집니다.

반면 혈우병 보인자의 증상은 X 연관 응고인자(VIII/IX) 결핍으로 생기는 출혈 문제입니다. 지질 대사 경로와 응고 경로 사이에서 알려진 기전적 연결고리는 없습니다. 따라서 높은 TxGNN 점수는 생물학적 근거가 있는 예측이라기보다 TxGNN 모델(딥러닝)이 관련 질환 사이에서 학습한 유사성을 반영한 결과로 보는 것이 합리적입니다.

참고로 상위 10개 예측 중에서는 가족성 아포단백 C-II 결핍증(점수 0.9950)이 지질 대사 질환이라 상대적으로 연관성이 높습니다. 그러나 Evolocumab은 주로 LDL-C를 낮추고 중성지방에는 제한적 효과만 있어, 리포단백 리파아제 보조인자 결함을 해결하지 못합니다. 이 예측도 이론적 수준에 머뭅니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201701842 | 레파타주프리필드시린지(에볼로쿠맙) | 주사액 충전 프리필드시린지 | 허가 적응증 본문 미확인 (허가사항 참조) |
| 201701843 | 레파타주프리필드펜(에볼로쿠맙) | 프리필드시린지가 장착된 일회용 자동주입기 | 허가 적응증 본문 미확인 (허가사항 참조) |

두 제품 모두 암젠코리아유한회사가 허가받은 단일제입니다.

## 안전성 고려사항

- **약물 상호작용**: 조회 결과 1건이 확인되었으나 이는 약리학적 표적 정보입니다. 상대 성분은 PCSK9(proprotein convertase subtilisin/kexin type 9)이며, 임상적 상호작용 등급은 제시되지 않았습니다.

그 외 경고·금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 높지만 임상시험과 문헌이 전혀 없고(근거 수준 L5), 지질 저하 기전과 응고인자 결핍 사이에 타당한 연결고리도 없습니다. 상위 10개 예측 모두 근거 수준 L5, 권고 Hold입니다.

**진행하려면 필요한 것:**
- 상세한 약물 작용 기전 데이터(MOA) 확보
- 허가사항(경고·금기·적응증 본문) 수집 및 안전성 검토
- 예측 적응증과 관련된 전임상 또는 임상 근거 탐색
- 지질 대사 질환(예: 가족성 아포단백 C-II 결핍증)처럼 기전적 연관성이 상대적으로 높은 후보를 우선 재평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

