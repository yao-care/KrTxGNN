---
layout: default
title: Rufinamide
parent: 모델 예측만 (L5)
nav_order: 675
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "RUFINAMIDE"
predicted_indications: ["perioral myoclonia with absences"]
description: "Rufinamide: 예측 신규 적응증 Perioral myoclonia with absences (근거 수준 L5). 기존 적응증: 이 약은 1세 이상의 환자에서 레녹스-가스토 증후군과 관련된 발작 치료 시 부가요법으로 사용된다."
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
| 기존 적응증 | 이 약은 1세 이상의 환자에서 레녹스-가스토 증후군과 관련된 발작 치료 시 부가요법으로 사용된다. ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200905916/EE)) |
| 예측 신규 적응증 | Perioral myoclonia with absences |
| TxGNN 예측 점수 | 0.9951 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 3건 / 전체 3건) |
| 허가증 수 | 3건 (유효 3건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Rufinamide 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “루피나미드가 항뇌전증 효과를 나타내는 정확한 기전은 알려져 있지 않다. 시험관 내 연구 결과에 따르면 루피나미드의 주요 작용 기전은 나트륨 채널 활성의 조절, 특히 채널의 불활성 상태 연장인 것으로 시사된다.” 영어 원문: "The precise mechanism(s) by which rufinamide exerts its antiepileptic effect is unknown. The results of in vitro studies suggest that the principal mechanism of action of rufinamide is modulation of the activity of sodium channels and, in particular, prolongation of the inactive state of the channel." ([DailyMed: Banzel (rufinamide) prescribing information, Eisai Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0a3fa925-1abd-458a-bd57-4ae780a1ef2d), 버전 2022-12-15; 확인일 2026-11-19). 일반적으로 알려진 바에 따르면, Rufinamide는 전압 의존성 나트륨 채널의 비활성 상태를 연장하는 항전간제로 알려져 있습니다. 이는 데이터 수집 결과가 아니라 일반 지식에 근거한 설명입니다.

FIRES는 치료가 어려운 뇌전증성 뇌병증으로, 신경염증이 주요 원인으로 거론됩니다. 나트륨 채널 차단은 발작의 일부에만 도움이 될 가능성이 있어, 기전상 연관성은 부분적입니다.

TxGNN은 같은 약물에 대해 다음 질환도 높은 점수로 예측했습니다. 모두 근거 수준 L5이며 권장 결정은 Hold입니다.

| 순위 | 예측 질환 | TxGNN 점수 | 기전상 참고 사항 |
|------|----------|-----------|----------------|
| 2 | 구주위 근간대경련을 동반한 결신 (Perioral myoclonia with absences) | 0.9951 | 나트륨 채널 차단제가 일부 전신 결신 발작을 악화시킬 수 있음 |

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 200905916 | 이노베론필름코팅정200mg (루피나미드) | 양면이 볼록하고 분할선이 있는 분홍색의 타원형 필름코팅정 | (주)한독 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200905916/EE) | 유효 |
| 200905915 | 이노베론필름코팅정400mg (루피나미드) | 양면이 볼록하고 분할선이 있는 분홍색의 타원형 필름코팅정 | (주)한독 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200905915/EE) | 유효 |
| 200905917 | 이노베론필름코팅정100mg (루피나미드) | 양면이 볼록하고 분할선이 있는 분홍색의 타원형 필름코팅정 | (주)한독 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200905917/EE) | 유효 |

<!-- licenses:end -->

모두 (주)한독의 제품입니다(허가 건수와 상태는 빠른 개요와 위 표 참조).

<!-- review:begin kr-lic-20261124c-rufinamide-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “3건 모두 (주)한독의 단일 성분 제품이며 유효한 허가 상태입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 이 사이트 자료의 성분란에는 일치한 성분만 기록되어 허가 품목별 단일 성분·복합 성분 여부를 확인할 수 없으므로, 단일·복합 표기를 빼고 건수는 쓰지 않고 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-rufinamide-1 -->

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

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Banzel (rufinamide) prescribing information, Eisai Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0a3fa925-1abd-458a-bd57-4ae780a1ef2d) |
| 2026-11-24 | 단일·복합 표기: “3건 모두 (주)한독의 단일 성분 제품이며 유효한 허가 상태입니다.” → 확인할 수 없는 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

