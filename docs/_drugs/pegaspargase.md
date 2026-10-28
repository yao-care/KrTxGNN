---
layout: default
title: Pegaspargase
parent: 모델 예측만 (L5)
nav_order: 581
evidence_level: L5
indication_count: 7
monitor_inn: "PEGASPARGASE"
predicted_indications: ["pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma", "chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation", "follicular lymphoma", "methylcobalamin deficiency type cblE", "lymphoid neoplasm", "Hodgkins lymphoma", "blast phase chronic myelogenous leukemia, BCR-ABL1 positive"]
last_modified_at: 2026-10-27
description: "Pegaspargase: 예측 신규 적응증 전핵심 중심 이전 만성 림프구성 백혈병/소림프구성 림프종 (pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/…"
---

# Pegaspargase
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **7** 건
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

## Pegaspargase: 아스파라긴 분해 효소 → 전핵심 중심 이전 만성 림프구성 백혈병/소림프구성 림프종 (pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma)
{: .text-alpha }

## 한 문장 요약

Pegaspargase는 아스파라긴을 분해하는 효소 약물입니다.
TxGNN 모델은 **전핵심 중심 이전 만성 림프구성 백혈병/소림프구성 림프종(pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 다룬 임상시험이나 문헌은 **0건**으로 모델 예측만 존재합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202101033/EE |
| 예측 신규 적응증 | 전핵심 중심 이전 만성 림프구성 백혈병/소림프구성 림프종 (pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma) |
| TxGNN 예측 점수 | 0.9995 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 pegaspargase는 혈중 아스파라긴을 고갈시켜 아스파라긴 의존성이 높은 림프계 종양 세포의 성장을 억제하는 것으로 알려져 있습니다.

그러나 만성 림프구성 백혈병/소림프구성 림프종(CLL/SLL)에서 아스파라긴 고갈이 확립된 취약점이라는 근거는 없습니다. 따라서 이 예측의 기전적 연결은 추측 수준입니다. 같은 점수(0.9995)를 가진 유사한 CLL/SLL 항목이 함께 예측된 점으로 보아, 모델이 유사 노드를 중복 취급했을 가능성도 있습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202101033 | 온카스파동결건조주사(페그아스파르가제) | 동결건조 주사제 (용해 후 투명한 무색 용액) | 허가 적응증 텍스트 없음 (문서 링크만 확인됨) |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 효소 기반 항종양제 (아스파라긴 분해 효소) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요. 이 보고서에 포함된 문헌에서는 간독성, 췌장염, 혈전증, 과민반응이 주요 독성으로 보고됩니다. |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 확인되었으며, 이 중 확인된 항목은 모두 중등도(Moderate)입니다. 주요 항목은 다음과 같습니다.
  - 혈당 강하제: acarbose, metformin, albiglutide, alogliptin, canagliflozin, dapagliflozin, saxagliptin, dulaglutide, chlorpropamide
  - 코르티코스테로이드: hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide
  - 항생제: doxycycline, tetracycline, clarithromycin
  - 기타: bupropion, acetylsalicylic acid, chenodeoxycholic acid

경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
이 예측은 모델 점수만 있고 해당 질환을 직접 연구한 임상시험이나 문헌이 없어 근거 수준이 L5입니다. 기전적 연결도 확립되지 않았습니다.

**진행하려면 필요한 것:**
- 해당 질환(CLL/SLL)에서 아스파라긴 의존성을 뒷받침하는 전임상 또는 기전 연구
- 상세한 약물 작용 기전(MOA) 데이터
- 허가사항(경고, 금기)의 확보 및 검토
- 한국 시판 상태의 확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

