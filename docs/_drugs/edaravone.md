---
layout: default
title: Edaravone
parent: 모델 예측만 (L5)
nav_order: 299
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-20
description: "Edaravone: 예측 신규 적응증 헤파린 보조인자 2 결핍증 (heparin cofactor 2 deficiency) (근거 수준 L5). 기존 적응증: ALS 및 급성 허혈성 뇌졸중 (허가사항 원문 확인 필요)"
monitor_inn: "EDARAVONE"
predicted_indications: ["heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis"]
---

# Edaravone
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

## Edaravone: ALS·급성 허혈성 뇌졸중에서 헤파린 보조인자 2 결핍증으로
{: .text-alpha }

## 한 문장 요약

Edaravone은 활성산소(자유라디칼) 제거제로, 원래 근위축성 측삭경화증(ALS)과 급성 허혈성 뇌졸중 치료에 사용되는 약입니다.
TxGNN 모델은 **헤파린 보조인자 2 결핍증(heparin cofactor 2 deficiency)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**이며 모델 예측만 존재합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | ALS 및 급성 허혈성 뇌졸중 (허가사항 원문 확인 필요) |
| 예측 신규 적응증 | 헤파린 보조인자 2 결핍증 (heparin cofactor 2 deficiency) |
| TxGNN 예측 점수 | 0.9947 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Edaravone 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “에다라본 주사제가 ALS 환자에서 치료 효과를 나타내는 기전은 알려져 있지 않다.” 영어 원문: "The mechanism by which edaravone injection exert its therapeutic effect in patients with ALS is unknown." ([DailyMed: edaravone prescribing information, Piramal Critical Care Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=19862ae9-d6e1-70e6-e063-6394a90ae749), 버전 2025-10-07; 확인일 2026-11-19). 알려진 정보에 따르면, Edaravone은 활성산소를 제거하여 산화 스트레스와 혈관내피 손상을 줄이는 약물이며, ALS와 급성 허혈성 뇌졸중에서 사용됩니다.

헤파린 보조인자 2 결핍증은 더마탄 황산과 헤파린에 의한 트롬빈 억제가 약해져 생기는 유전성 혈전 소인입니다. Edaravone은 이 경로에 작용하지 않습니다. 굳이 연결한다면 혈관내피의 산화 손상 감소나 혈전 관련 신경 보호 효과 같은 간접적 가설 정도입니다.

따라서 이 연관성은 추측 수준이며, 높은 TxGNN 점수(0.9947) 외에는 이를 지지하는 자료가 없습니다.

### 참고: 두 번째 예측 질환

| 순위 | 예측 질환 | TxGNN 점수 | 근거 수준 | 권장 |
|------|---------|-----------|---------|------|
| 2 | 자발성 혈전증을 동반한 factor 5 과다 | 0.9906 | L5 | Hold |

Edaravone의 항산화·항염증 작용이 산화 스트레스에 의한 내피 및 혈소판 활성화를 이론적으로 줄일 수 있습니다. 그러나 factor V, 트롬빈 생성, 응고 경로를 직접 표적으로 하지 않으며, 임상시험과 문헌도 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202503235 | 라디컷현탁액(에다라본) | 현탁액 (갈색 유리병, 흰색) | 허가사항 원문 참조 |
| 201508336 | 라디컷주30mg(에다라본) | 주사제 (무색 투명 앰플) | 허가사항 원문 참조 |

두 제품 모두 제조사는 타나베파마코리아주식회사이며, 유효한 단독제 허가입니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측은 TxGNN 점수에만 근거하며, 임상시험과 문헌이 없고 기전적 연관성도 간접적이고 추측적입니다. 안전성 및 작용 기전 데이터도 부족해 현 단계에서 진행하기 어렵습니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기 등) 확보: 식약처(MFDS) 허가 문서를 내려받아 분석
- 상세한 약물 작용 기전(MOA) 데이터 확보
- 헤파린 보조인자 2 결핍증과 Edaravone의 연관성을 검증할 전임상 또는 기전 연구
- 투여 경로 적합성 평가 (현재 미확인)

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: edaravone prescribing information, Piramal Critical Care Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=19862ae9-d6e1-70e6-e063-6394a90ae749) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

