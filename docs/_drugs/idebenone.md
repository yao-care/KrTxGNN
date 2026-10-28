---
layout: default
title: Idebenone
parent: 모델 예측만 (L5)
nav_order: 412
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Idebenone: 예측 신규 적응증 간성 포르피린증 (Hepatic Porphyria) (근거 수준 L5). 기존 적응증: 허가 적응증 텍스트가 링크 형태로만 제공되어 구체적인 내용을 확인할 수 없음 (허가사항 참조)"
monitor_inn: "Idebenone"
predicted_indications: ["hepatic porphyria", "hepatopulmonary syndrome", "primitive portal vein thrombosis", "hepatoportal sclerosis", "idiopathic copper-associated cirrhosis", "early-onset familial noncirrhotic portal hypertension", "immune-mediated necrotizing myopathy", "osteogenesis imperfecta-retinopathy-seizures-intellectual disability syndrome", "antisynthetase syndrome", "focal myositis"]
---

# Idebenone
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

## Idebenone: 기존 적응증 정보 미확인에서 간성 포르피린증으로
{: .text-alpha }

## 한 문장 요약

Idebenone은 합성 단쇄 코엔자임 Q10(CoQ10) 유사체로, 한국에서 단일제(락손필름코팅정 150mg)로 허가되어 시판 중입니다.
TxGNN 모델은 **간성 포르피린증(Hepatic Porphyria)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 지지하는 **임상시험은 0건, 문헌도 0건**입니다.
따라서 이 예측은 모델 예측만 있는 단계(L5)입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 텍스트가 링크 형태로만 제공되어 구체적인 내용을 확인할 수 없음 (허가사항 참조) |
| 예측 신규 적응증 | 간성 포르피린증 (Hepatic Porphyria) |
| TxGNN 예측 점수 | 0.9992 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Idebenone은 합성 단쇄 CoQ10 유사체로, 미토콘드리아 호흡 사슬에서 전자 전달체 및 항산화제로 작용합니다.

간세포의 산화 스트레스를 줄일 수 있다는 점에서 간 질환에 대한 가설적 연결고리는 생각해 볼 수 있습니다. 그러나 이 작용이 헴(heme) 생합성 결함과 연결된다는 근거는 현재 데이터에 없습니다. 따라서 이 예측은 TxGNN 모델(딥러닝)이 산출한 점수이며, 모델이 관련 질환 사이에서 학습한 유사성을 반영할 수 있을 뿐 생물학적 근거는 아니고, 기전적으로 검증되지 않았습니다.

참고로 같은 모델이 예측한 다른 후보(상위 10건)에는 간문맥 관련 질환(비경화성 문맥압항진증, 일차성 문맥 혈전증, 간문맥 경화증), 구리 관련 간경변, 간폐증후군, 근염 계열 질환 등이 있으며, 모두 임상시험·문헌 근거가 없는 L5 단계입니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201906395 | 락손필름코팅정150밀리그램(이데베논) | 양면이 볼록한 주황색 원형 필름코팅정 | 허가사항 참조 (제공된 데이터에 적응증 본문 없음) |

- 제조사: 광동제약(주)
- 구분: 단일제, 유효 상태

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
간성 포르피린증에 대한 임상시험과 문헌이 전혀 없고 TxGNN 예측 점수만 있는 상태이며, 헴 생합성 결함과의 기전적 연결도 확인되지 않았습니다. 또한 허가사항의 경고·금기 정보가 확보되지 않아 안전성 1차 검토를 진행할 수 없습니다.

**진행하려면 필요한 것:**
- 식약처(MFDS) 허가사항(경고 및 금기) 확보 및 분석
- 기존 허가 적응증 본문 확인
- DrugBank 등에서 상세 작용 기전(MOA) 확보
- 간성 포르피린증에 대한 전임상 또는 기전 연구 탐색
- 투여 경로 적합성 및 기존 적응증과의 유사성 평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

