---
layout: default
title: Ethosuximide
parent: 모델 예측만 (L5)
nav_order: 324
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-15
description: "Ethosuximide: 예측 신규 적응증 신인성 항이뇨호르몬 부적절 분비 증후군 (Nephrogenic Syndrome of Inappropriate Antidiur… (근거 수준 L5). 기존 적응증: 결신발작(소발작)"
monitor_inn: "ETHOSUXIMIDE"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
---

# Ethosuximide
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **1** 건
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

## Ethosuximide: 소발작(결신발작)에서 신인성 항이뇨호르몬 부적절 분비 증후군으로
{: .text-alpha }

## 한 문장 요약

Ethosuximide는 한국에서 허가된 단일제로, 일반적으로 결신발작(소발작) 치료에 사용되는 T형 칼슘 채널 차단제입니다.
TxGNN 모델은 **신인성 항이뇨호르몬 부적절 분비 증후군(Nephrogenic Syndrome of Inappropriate Antidiuresis, NSIAD)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 지지하는 **임상시험과 문헌은 각각 0건**으로 모델 예측만 존재합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 결신발작(소발작) ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201200246/EE)) |
| 예측 신규 적응증 | 신인성 항이뇨호르몬 부적절 분비 증후군 (Nephrogenic Syndrome of Inappropriate Antidiuresis) |
| TxGNN 예측 점수 | 0.9991 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Ethosuximide 처방 정보(Prescribing Information)의 “Clinical Pharmacology” 항목에 따르면(비공식 번역): “에토숙시미드는 결신(소발작) 발작에서 흔히 나타나는 의식 소실과 관련된 초당 3회의 발작성 극서파 활동을 억제한다. 간질양 발작의 빈도는 감소하는데, 이는 운동피질의 억제 및 경련 자극에 대한 중추신경계 역치의 상승에 의한 것으로 보인다.” 영어 원문: "Ethosuximide suppresses the paroxysmal three cycle per second spike and wave activity associated with lapses of consciousness which is common in absence (petit mal) seizures. The frequency of epileptiform attacks is reduced, apparently by depression of the motor cortex and elevation of the threshold of the central nervous system to convulsive stimuli." ([DailyMed: Zarontin (ethosuximide) prescribing information, Parke-Davis Div of Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0e008f33-70a1-4bc6-b3a0-d45214418ab6), 버전 2026-05-25; 확인일 2026-11-19). 일반적으로 알려진 바로 ethosuximide는 T형 칼슘 채널을 차단하여 결신발작을 억제하는 항경련제입니다.

NSIAD는 V2 수용체 유전자(AVPR2)의 기능 획득 돌연변이 등으로 수용체가 지속적으로 활성화되어 발생하는 질환입니다. 현재 확인된 자료에서는 T형 칼슘 채널 차단과 바소프레신 V2 수용체 신호 또는 신장의 수분 조절을 연결하는 확립된 경로가 없습니다.

TxGNN 모델(딥러닝)의 높은 점수(0.9991)는 모델이 관련 질환 간에 학습한 유사성을 반영했을 가능성이 있는 계산상 예측일 뿐, 생물학적 근거가 아닙니다. 기전적 연관성은 현재로서는 추측 수준이며 전임상 모델에서 검증이 필요합니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201200246 | 자론티연질캡슐(에토숙시미드) (영풍제약) | 투명한 내용물이 든 분홍색의 타원형 연질캡슐제 | 허가 적응증 원문은 허가정보 문서(식약처 의약품안전나라)를 참조하세요 |

## 안전성 고려사항

- **지식그래프 기반 금기 관련 질환**: 허가사항 문구가 아니라 TxGNN 지식그래프(PrimeKG)의 약물-질환 금기 연결 정보입니다. 불안장애, 신경증, 기분부전장애, 신장 질환, 요관농양, 혈액 질환, 간 질환, 담낭 질환, 전신홍반루푸스(소아 포함), 호중구감소증, 무과립구증, 급성 간헐성 포르피린증이 포함됩니다. 특히 신장 질환이 포함되어 있어 신장 질환인 NSIAD에 적용할 때 주의가 필요합니다.
- **약물 상호작용**: 총 92건이 확인되었으며, 이 중 주요 항목은 모두 중등도(Moderate)입니다.
  - 아프레피탄트, 모르핀(리포좀 제제 포함), 아편, 드로나비놀, 나빌론, 메토클로프라미드
  - 시부트라민, 에탄올, 코비시스타트, 엽산, 데페라시록스, 프로메타진
  - 레보류코보린, 류코보린, 포스타마티닙, 클로로퀸, 메플로퀸, 하이드록시클로로퀸, 클로르페니라민

허가사항의 경고 및 금기 내용은 이번 자료에 포함되지 않았으므로 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 점수는 매우 높지만 지지하는 임상시험과 문헌이 없고 기전적 연관성도 확인되지 않아 근거 수준이 L5(모델 예측만 존재)입니다. 또한 허가사항의 경고·금기 정보를 확인하지 못해 안전성 검토를 진행할 수 없습니다.

**진행하려면 필요한 것:**
- 식약처 허가사항(적응증, 경고, 금기) 문서를 내려받아 분석
- 작용 기전 데이터 보완 (DrugBank 조회)
- AVPR2/GNAS 신호 경로와의 연관성을 검증하는 전임상 연구 설계
- NSIAD 관련 임상시험 및 문헌 재검색
- 신장 질환 관련 지식그래프 금기 신호에 대한 안전성 평가

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Zarontin (ethosuximide) prescribing information, Parke-Davis Div of Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0e008f33-70a1-4bc6-b3a0-d45214418ab6) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

