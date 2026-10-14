---
layout: default
title: Upadacitinib
parent: 모델 예측만 (L5)
nav_order: 772
evidence_level: L5
indication_count: 2
---

# Upadacitinib
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **2** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 약사 평가 보고서

</div>

# Upadacitinib: 허가 적응증에서 콜로보마성 소안구증-근위부 단축형 이형성 증후군으로

## 한 문장 요약

Upadacitinib(국내 제품명: 린버크서방정)은 한국에서 시판 중인 단일제로, 허가 적응증 원문은 데이터에 텍스트로 수록되어 있지 않습니다.
TxGNN 모델은 **콜로보마성 소안구증-근위부 단축형 이형성 증후군(colobomatous microphthalmia-rhizomelic dysplasia syndrome)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험은 0건**, **문헌도 0편**입니다.
따라서 현재는 모델 예측만 존재하는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에 적응증 텍스트가 없고 허가사항 문서 링크만 있어 확인 불가 |
| 예측 신규 적응증 | 콜로보마성 소안구증-근위부 단축형 이형성 증후군 (colobomatous microphthalmia-rhizomelic dysplasia syndrome) |
| TxGNN 예측 점수 | 99.61% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 upadacitinib은 선택적 JAK1 억제제로 면역조절 약물입니다. 그러나 JAK-STAT 신호전달이 이 증후군의 병태생리와 연결된다는 자료는 이번에 수집된 데이터에 없습니다.

이 증후군은 눈 콜로보마, 소안구증, 근위부 사지 단축을 동반하는 극히 드문 선천성 발달 이상입니다. 면역억제 기반의 JAK 억제가 구조적 발달 결함을 교정할 가능성은 낮아 보입니다.

TxGNN 점수 0.996은 모델 기반 예측일 뿐입니다. 극희귀 선천성 기형 증후군에서 이렇게 높은 점수가 나온 것은 실제 치료 효과보다 지식그래프의 구조나 인접한 유전자·경로의 공유를 반영했을 가능성이 있습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202004222 | 린버크서방정15밀리그램(유파다시티닙반수화물) | 보라색 양면 볼록 장방형 서방성 필름코팅정 ("a15" 각인) | 허가사항 문서 링크만 제공됨 ([링크](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202004222/EE)) |
| 202201070 | 린버크서방정30밀리그램(유파다시티닙반수화물) | 빨간색 양면 볼록 장방형 서방성 필름코팅정 ("a30" 각인) | 허가사항 문서 링크만 제공됨 ([링크](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202201070/EE)) |

## 안전성 고려사항

- **약물 상호작용**: 총 359건이 확인되었으며, 주요 항목은 다음과 같습니다.
  - **Major**: 코르티코스테로이드류(hydrocortisone, triamcinolone, dexamethasone, beclomethasone, betamethasone, budesonide, prednisone, prednisolone), clarithromycin, cobicistat, deferiprone, iobenguane (I-131)
  - **Moderate**: aprepitant, cimetidine, miconazole, deferasirox
  - **Minor**: 아연 제제(zinc sulfate, zinc acetate, zinc gluconate)

허가사항의 경고·금기 정보는 이번 데이터에 포함되어 있지 않으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
임상시험과 문헌 근거가 없고 기전적 연결고리도 확인되지 않아, 높은 TxGNN 점수만으로는 진행하기 어렵습니다. 선천성 발달 이상에 면역조절제를 적용하는 생물학적 타당성도 약합니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기·적응증) 문서의 확보 및 분석 (현재 안전성 선별 진행을 막는 항목)
- 작용 기전(MOA) 데이터 보완 (DrugBank 조회)
- JAK-STAT 경로와 이 증후군 병태생리의 연관성에 대한 전임상·유전학적 근거
- 관련 임상시험 및 문헌 검색의 재수행

## 참고: 두 번째 예측 질환

두 번째 예측 질환인 **합지증-단지증 증후군(brachydactyly-syndactyly syndrome)**(TxGNN 점수 99.58%)도 임상시험 0건, 문헌 0편으로 근거 수준은 L5이고 권장 결정은 Hold입니다. 이 질환은 선천성 골격 기형이므로 면역조절제의 기전적 근거가 약하며, 점수는 그래프 기반 연관성을 반영한 것으로 보입니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

