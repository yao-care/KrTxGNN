---
layout: default
title: Baricitinib
parent: 모델 예측만 (L5)
nav_order: 125
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Baricitinib: 예측 신규 적응증 콜로보마성 소안구증-근위지단 이형성 증후군 (colobomatous microphthalmia-rhizomelic dyspl… (근거 수준 L5). 기존 적응증: 허가 문서 링크만 확인되며 적응증 본문은 확인되지 않음"
monitor_inn: "BARICITINIB"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
---

# Baricitinib
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

## Baricitinib: 허가 적응증에서 콜로보마성 소안구증-근위지단 이형성 증후군으로
{: .text-alpha }

## 한 문장 요약

Baricitinib은 한국에서 올루미언트정(1mg, 2mg, 4mg)으로 시판 중인 단일제입니다. TxGNN 모델은 **콜로보마성 소안구증-근위지단 이형성 증후군(colobomatous microphthalmia-rhizomelic dysplasia syndrome)**에 효과가 있을 수 있다고 예측했습니다. 그러나 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**이어서 모델 예측만 존재하는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 문서 링크만 확인되며 적응증 본문은 확인되지 않음 |
| 예측 신규 적응증 | 콜로보마성 소안구증-근위지단 이형성 증후군 (colobomatous microphthalmia-rhizomelic dysplasia syndrome) |
| TxGNN 예측 점수 | 99.94% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 3건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 다만 Baricitinib은 일반적으로 JAK1/JAK2 억제제로 알려져 있으며, 염증성 JAK-STAT 신호 전달을 차단하는 약물입니다.

예측된 신규 적응증은 안구와 사지 뼈의 발생 이상을 특징으로 하는 희귀 발달 증후군입니다. 이 질환과 JAK-STAT 신호 전달 사이에서 이번에 확인된 자료만으로는 타당한 기전적 연결고리를 찾을 수 없습니다. 이런 증후군은 보통 발생 과정이나 유전적 원인으로 생기므로, 염증 경로를 억제한다고 교정될 것으로 기대하기 어렵습니다.

따라서 이 예측은 생물학적 근거보다 지식 그래프의 네트워크 구조에서 비롯되었을 가능성이 큽니다. 가설을 세우는 참고 신호로만 보는 것이 적절합니다.

같은 분석에서 두 번째로 제시된 예측은 **손발가락 단지증-합지증 증후군(brachydactyly-syndactyly syndrome, 점수 99.94%)**이며, 이 역시 임상시험과 문헌 근거가 없고 같은 이유로 보류 대상입니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201708281 | 올루미언트정4밀리그램(바리시티닙) | 분홍색 원형 필름코팅정 (한면 "Lilly", 다른 면 "4" 음각) | 허가 문서 참조 |
| 201708280 | 올루미언트정2밀리그램(바리시티닙) | 밝은 분홍색 타원형 필름코팅정 (한면 "Lilly", 다른 면 "2" 음각) | 허가 문서 참조 |
| 202402172 | 올루미언트정1밀리그램(바리시티닙) | 매우 밝은 분홍색 원형 필름코팅정 (한면 "Lilly", 다른 면 "1" 음각) | 허가 문서 참조 |

제조사는 모두 한국릴리(유)이며, 3건 모두 유효한 단일제 허가입니다.

## 안전성 고려사항

- **약물 상호작용**: 상호작용 조회 결과 총 100건이 확인되었으며, 주요 항목은 다음과 같습니다.
  - **Major**: 코르티코스테로이드 계열(Hydrocortisone, Triamcinolone, Betamethasone, Budesonide, Dexamethasone, Prednisolone, Prednisone), Deferiprone, 방사성의약품(Ibritumomab tiuxetan, Iobenguane I-131, Tositumomab I-131)
  - **Moderate**: Morphine, Acetylsalicylic acid(아스피린), Nitisinone, Opium
  - **Minor**: 아연 제제(Zinc acetate, gluconate, sulfate)

그 외 경고·금기 등 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 매우 높지만 임상시험과 문헌 근거가 전혀 없어 근거 수준이 L5에 머뭅니다. 또한 JAK-STAT 억제와 이 희귀 발달 증후군을 잇는 기전적 연결고리를 확인할 수 없습니다.

**진행하려면 필요한 것:**
- 허가 문서(첨부문서)의 적응증, 경고, 금기 정보 확보 및 분석
- 상세한 약물 작용 기전(MOA) 데이터 확보
- 예측 질환의 병태생리와 JAK-STAT 경로 간 연관성에 대한 전임상·기전 연구 근거
- 관련 임상시험 및 문헌 탐색 (현재 등록 건 없음)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

