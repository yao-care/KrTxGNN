---
layout: default
title: Durvalumab
parent: 모델 예측만 (L5)
nav_order: 295
evidence_level: L5
indication_count: 6
monitor_inn: "Durvalumab"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
last_modified_at: 2026-10-31
description: "Durvalumab: 예측 신규 적응증 자궁인대 선암종 (근거 수준 L5). 기존 적응증: 확인 불가 (허가 문서 링크만 제공되고 적응증 본문이 없음)"
---

# Durvalumab
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

## Durvalumab: 한국 허가 적응증(본문 미확인)에서 자궁인대 선암종으로
{: .text-alpha }

## 한 문장 요약

Durvalumab(DB11714)은 한국에서 임핀지주라는 단일 성분 주사제로 허가되어 있습니다. 다만 이번에 정리한 데이터에는 허가 적응증 본문이 없고 허가 문서 링크만 있어, 기존 적응증은 확인하지 못했습니다.
TxGNN 모델은 **자궁인대 선암종(uterine ligament adenocarcinoma)**에 효과가 있을 수 있다고 예측합니다. 그러나 이 질환을 직접 다룬 **임상시험은 0건, 문헌도 0편**이어서 모델 예측만 있는 상태입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 문서 링크만 제공되고 적응증 본문이 없음) |
| 예측 신규 적응증 | 자궁인대 선암종 |
| TxGNN 예측 점수 | 0.9992 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 이번 데이터에서 확인되는 것은 durvalumab이 PD-L1을 표적으로 하는 항체 의약품이라는 점뿐입니다. 한국 허가 적응증 본문도 확인되지 않아, 기존 적응증과 신규 적응증의 연관성은 근거를 들어 설명할 수 없습니다.

가능한 추정은 부인과 선암에서 PD-L1 차단이 도움이 될 수 있다는 정도입니다. 하지만 자궁인대 선암종이라는 드문 부위에 대해서는 이를 뒷받침하는 데이터가 없습니다. 이 예측의 점수는 TxGNN 모델(딥러닝)에서 나온 것이며, 모델이 관련 질환 사이에서 학습한 유사성을 반영할 수 있으나 생물학적 근거는 아닙니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201804918 | 임핀지주(더발루맙) | 주사제 (바이알) | 허가 문서 링크만 제공되어 본문 미확인 |

- 제조사는 한국아스트라제네카(주)이며 단일 성분 제품입니다. 허가 상태는 유효(valid)입니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 면역치료 (항 PD-L1 항체). 기존 세포독성 화학요법제가 아님 |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **약물 상호작용**: 총 81건이 조회되었습니다(DDInter 기준). 주요 항목은 다음과 같습니다.
  - **Major**: Adalimumab
  - **Moderate**: 코르티코스테로이드 계열(hydrocortisone, prednisone, prednisolone, methylprednisolone, dexamethasone, betamethasone, budesonide, triamcinolone, deflazacort), roflumilast, alefacept, alemtuzumab, anakinra, 파상풍 톡소이드 백신, 탄저 백신
  - **Minor**: 아연 제제(acetate, gluconate, sulfate, chloride)
- 코르티코스테로이드와 면역억제제의 병용은 면역치료의 작용과 충돌할 수 있으므로 병용 시 주의가 필요합니다. 이는 일반적인 약리 원칙에 따른 해석이며, 이번 데이터에 근거 설명이 있는 것은 아닙니다.
- 경고와 금기 정보는 이번 데이터에 포함되지 않았습니다. 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
자궁인대 선암종에 대해서는 임상시험과 문헌이 모두 없어 TxGNN 예측만 있는 L5 단계입니다. 허가 적응증 본문과 작용 기전, 허가사항의 경고·금기 정보도 확인되지 않아 안전성 검토 단계로 넘어갈 수 없습니다.

참고로 같은 약물의 다른 예측 질환인 자궁경부 선암(endocervical carcinoma)에는 완료된 Phase 1 시험(NCT03452332, 20명, 방사선 병용) 1건이 있습니다. 이 시험은 대상 집단이 자궁경부 단독인지 혼합 종양인지 확인되지 않고 효능 근거도 아니어서, 이번 예측을 지지하는 근거로는 쓸 수 없습니다.

**진행하려면 필요한 것:**
- 한국 허가증 문서(MFDS)에서 적응증 본문과 경고·금기 정보 확보
- 작용 기전(MOA) 데이터 확보 (DrugBank 등)
- 자궁인대 선암종을 직접 다룬 임상시험 또는 문헌 탐색. 없다면 증례나 전임상 수준의 근거부터 확인
- 부인과 선암 전반에서 PD-L1 차단이 타당한지 검토. 이 질환이 매우 드문 만큼 자궁경부 선암 등 인접 질환의 근거를 우선 확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

