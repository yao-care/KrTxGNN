---
layout: default
title: Rufinamide
parent: 모델 예측만 (L5)
nav_order: 675
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
monitor_inn: "RUFINAMIDE"
predicted_indications: ["perioral myoclonia with absences"]
description: "Rufinamide: 예측 신규 적응증 Perioral myoclonia with absences (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200905916/EE"
---

# Rufinamide
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

## Rufinamide: Perioral myoclonia with absences
{: .text-alpha }

## 한 문장 요약

Rufinamide는 한국에서 항전간제로 허가·시판 중인 단일 성분 약물입니다. 다만 이 예측을 지지하는 **임상시험과 문헌은 현재 0건**이며, 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200905916/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200905915/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200905917/EE |
| 예측 신규 적응증 | Perioral myoclonia with absences |
| TxGNN 예측 점수 | 0.9951 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 3건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 알려진 바에 따르면, Rufinamide는 전압 의존성 나트륨 채널의 비활성 상태를 연장하는 항전간제로 알려져 있습니다. 이는 데이터 수집 결과가 아니라 일반 지식에 근거한 설명입니다.

FIRES는 치료가 어려운 뇌전증성 뇌병증으로, 신경염증이 주요 원인으로 거론됩니다. 나트륨 채널 차단은 발작의 일부에만 도움이 될 가능성이 있어, 기전상 연관성은 부분적입니다.

TxGNN은 같은 약물에 대해 다음 질환도 높은 점수로 예측했습니다. 모두 근거 수준 L5이며 권장 결정은 Hold입니다.

| 순위 | 예측 질환 | TxGNN 점수 | 기전상 참고 사항 |
|------|----------|-----------|----------------|
| 2 | 구주위 근간대경련을 동반한 결신 (Perioral myoclonia with absences) | 0.9951 | 나트륨 채널 차단제가 일부 전신 결신 발작을 악화시킬 수 있음 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200905916 | 이노베론필름코팅정200mg (루피나미드) | 분홍색 타원형 필름코팅정 (분할선 있음) | 허가사항 참조 |
| 200905915 | 이노베론필름코팅정400mg (루피나미드) | 분홍색 타원형 필름코팅정 (분할선 있음) | 허가사항 참조 |
| 200905917 | 이노베론필름코팅정100mg (루피나미드) | 분홍색 타원형 필름코팅정 (분할선 있음) | 허가사항 참조 |

3건 모두 (주)한독의 단일 성분 제품이며 유효한 허가 상태입니다.

## 안전성 고려사항

허가사항의 경고 및 금기 정보는 이번에 확인하지 못했으므로 허가사항을 직접 참조하세요.

- **지식 그래프 기반 금기 질환** (허가문서가 아닌 TxGNN 지식 그래프의 약물-질환 금기 연결 기준): 간부전, 간질환, 담낭 질환, 불안 장애, 신경증, 기분부전 장애, 백혈구감소증
- **약물 상호작용**: 총 100건이 조회되었으며, 아래는 그중 일부로 모두 중등도(Moderate)입니다.
  - 코르티코스테로이드류: Hydrocortisone, Prednisone, Triamcinolone, Betamethasone
  - 비타민 D류: Cholecalciferol, Calcifediol, Calcitriol
  - 중추신경계 작용 약물: Morphine, Bupropion, Dronabinol, Nabilone
  - 항구토제 및 위장관 약물: Ondansetron, Metoclopramide, Rolapitant, Diphenoxylate, Difenoxin
  - 기타: Pioglitazone, Eliglustat, Naloxegol, Nitisinone

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 점수는 높지만 이를 뒷받침하는 임상시험과 문헌이 없어 근거 수준이 L5에 머뭅니다. 또한 FIRES는 신경염증이 핵심이어서 나트륨 채널 차단 기전만으로는 연관성이 제한적입니다.

**진행하려면 필요한 것:**
- FIRES에서 Rufinamide를 평가한 임상시험, 증례 보고, 문헌 검토
- 상세한 약물 작용 기전(MOA) 데이터 확보
- 허가사항(경고, 금기, 허가 적응증)을 내려받아 확인하고 안전성 검토 진행
- 간 기능 및 백혈구 수치와 관련된 안전성 모니터링 계획 수립
- 병용 약물(특히 코르티코스테로이드)과의 상호작용 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

