---
layout: default
title: Primidone
parent: 모델 예측만 (L5)
nav_order: 628
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-31
description: "Primidone: 예측 신규 적응증 삼차신경 신생물 (trigeminal nerve neoplasm) (근거 수준 L5). 기존 적응증: 확인 불가 (허가 정보에 적응증 본문 없이 문서 링크만 제공됨)"
monitor_inn: "PRIMIDONE"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
---

# Primidone
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **3** 건
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

## Primidone: 기존 적응증에서 삼차신경 신생물로
{: .text-alpha }

## 한 문장 요약

Primidone은 한국에서 대웅프리미돈정으로 시판 중인 항경련제입니다. 다만 허가 적응증의 상세 문구는 이번 보고서용으로 수집된 데이터에 포함되어 있지 않습니다.
TxGNN 모델은 **삼차신경 신생물(trigeminal nerve neoplasm)**에 효과가 있을 수 있다고 예측하지만, 이를 지지하는 **임상시험은 0건**, **문헌도 0편**입니다. 따라서 이 예측은 모델 점수에만 의존하며, 생물학적 근거는 확인되지 않습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 정보에 적응증 본문 없이 문서 링크만 제공됨) |
| 예측 신규 적응증 | 삼차신경 신생물 (trigeminal nerve neoplasm) |
| TxGNN 예측 점수 | 0.9999 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Primidone은 항경련제이며 체내에서 phenobarbital과 PEMA로 대사됩니다. 따라서 경련성 질환에서의 효능을 바탕으로 한 신경계 약물로 분류할 수 있습니다.

그러나 삼차신경 신생물과의 기전적 연관성은 뚜렷하지 않습니다. Primidone에는 알려진 항종양 활성이 없습니다. 매우 높은 예측 점수는 TxGNN 모델(딥러닝)이 관련 질환 사이에서 학습한 유사성을 반영한 것일 수 있으며, 생물학적 근거는 아닙니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 198000160 | 대웅프리미돈정 | 백색 정제 | 허가사항 문서 참조 (https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198000160/EE) |

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 그중 일부는 다음과 같습니다.
  - 주요(Major) 등급: Morphine, Eliglustat
  - 보통(Moderate) 등급: Doxycycline, Hydrocortisone, Dexamethasone, Betamethasone, Triamcinolone, Bupropion, Aprepitant, Metronidazole, Pioglitazone, Canagliflozin, Saxagliptin, Cholecalciferol, Calcitriol, Calcifediol, Difenoxin, Diphenoxylate, Dronabinol
  - 경미(Minor) 등급: Cimetidine
- **지식 그래프 기반 금기 관련 질환** (허가 문서 기재가 아니라 모델 지식 그래프의 약물-질환 금기 연결 기준):
  - 정신과 및 중독: 불안장애, 신경증, 기분부전장애, 물질 남용/의존
  - 포르피린증: 유전성 포르피린증, 포르피린 대사 질환
  - 장기 질환: 신장 질환, 간 질환, 담낭 질환
  - 혈액 질환: 혈소판감소증, 호중구감소증, 무과립구증, 빈혈, 백혈구감소증, 범혈구감소증
  - 수면 및 호흡: 수면무호흡증후군, 선천성 중추성 저환기 증후군

그 외 허가사항상의 경고 및 금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
삼차신경 신생물에 대한 임상시험과 문헌이 전혀 없고 기전적 근거도 없어, 모델 예측만 존재하는 L5 수준입니다. 예측 점수는 높지만 TxGNN 모델(딥러닝)이 관련 질환 사이에서 학습한 유사성을 반영한 것일 수 있으며, 생물학적 근거는 아닙니다.

**진행하려면 필요한 것:**
- 한국 허가사항 문서(경고, 금기, 적응증)의 확보와 분석
- 상세한 약물 작용 기전(MOA) 데이터 확보
- 삼차신경 신생물과 Primidone을 연결하는 전임상 또는 기전 근거
- 참고로, 같은 예측 목록의 **삼차신경통(trigeminal neuralgia)**은 나트륨 채널 조절이라는 기전적 타당성이 있어 별도의 연구 과제로 검토할 수 있습니다. 다만 현재 확보된 문헌은 carbamazepine 중심이며 Primidone 고유의 효능 데이터는 없습니다.
- 경련성 질환 계열(반사성 간질 등) 예측들은 항경련 기전상 개연성이 있으나, 인체 근거는 사례 보고와 동물 연구 수준에 그칩니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

