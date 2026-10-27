---
layout: default
title: Letermovir
parent: 모델 예측만 (L5)
nav_order: 469
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Letermovir: 예측 신규 적응증 외음질 칸디다증 (vulvovaginal candidiasis) (근거 수준 L5). 기존 적응증: 허가 적응증 텍스트가 링크로만 제공되어 구체적 문구를 확인할 수 없음 (허가사항 참조)"
monitor_inn: "LETERMOVIR"
predicted_indications: ["vulvovaginal candidiasis"]
---

# Letermovir
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

## Letermovir: 거대세포바이러스 감염에서 외음질 칸디다증으로
{: .text-alpha }

## 한 문장 요약

Letermovir는 CMV(거대세포바이러스)에 특이적으로 작용하는 항바이러스제로, 한국에서 프레비미스라는 제품명으로 허가·시판되고 있습니다.
TxGNN 모델은 **외음질 칸디다증(vulvovaginal candidiasis)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 **임상시험과 문헌은 없습니다**.
기전상 타당성도 낮아 모델 예측 단독 수준(L5)의 근거에 그칩니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 텍스트가 링크로만 제공되어 구체적 문구를 확인할 수 없음 (허가사항 참조) |
| 예측 신규 적응증 | 외음질 칸디다증 (vulvovaginal candidiasis) |
| TxGNN 예측 점수 | 99.88% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 3건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

Letermovir는 CMV의 터미나제 복합체(pUL56/pUL51/pUL89)를 억제하는 CMV 특이적 항바이러스제입니다. 상세한 작용 기전 데이터는 현재 이 보고서에 포함되어 있지 않아, 위 설명은 알려진 약리 정보에 근거합니다.

외음질 칸디다증은 *Candida* 종(주로 *C. albicans*)이 일으키는 진균 감염입니다. 진균에는 CMV 터미나제와 상동인 구조가 없어, Letermovir가 직접 항진균 작용을 할 만한 기전은 확인되지 않습니다.

따라서 높은 TxGNN 점수는 생물학적 근거라기보다 지식 그래프상의 인공적 연관(항진균제·항감염제와 공유하는 이웃 노드, 또는 칸디다증이 흔한 면역저하·이식 환자군과의 연관)일 가능성이 큽니다. CMV 관련 합병증이 줄어드는 간접 효과가 있더라도 칸디다증 치료라고 볼 수는 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201805301 | 프레비미스정480밀리그램 | 필름코팅정 (분홍색, 타원형) | 허가사항 참조 |
| 201805302 | 프레비미스주 | 주사제 (바이알) | 허가사항 참조 |
| 201805300 | 프레비미스정240밀리그램 | 필름코팅정 (노란색, 타원형) | 허가사항 참조 |

3건 모두 한국엠에스디(주) 제품이며 단일제로 유효 상태입니다.

## 안전성 고려사항

- **약물 상호작용**: 상호작용 조회 결과 총 100건이 확인되었으며, 그중 일부를 아래에 나열합니다.
  - **Major**: Eliglustat, Naloxegol, Cisapride
  - **Moderate**: Hydrocortisone, Dexamethasone, Betamethasone, Triamcinolone, Budesonide, Pioglitazone, Glimepiride, Chlorpropamide, Saxagliptin, Aprepitant, Omeprazole, Lansoprazole, Clarithromycin, Naldemedine, Nitisinone 등

주요 경고와 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
외음질 칸디다증에 대한 임상시험과 문헌이 전혀 없고, CMV 특이적 기전상 진균에 작용할 근거도 확인되지 않아 모델 예측만 존재하는 상태(L5)입니다.

**진행하려면 필요한 것:**
- 진균(*Candida*)에 대한 항진균 활성을 보여주는 전임상(in vitro) 데이터
- 허가사항(경고·금기·허가 적응증)의 확보 및 분석
- 상세한 작용 기전(MOA) 데이터
- 경로 적합성(투여 경로) 및 기존 적응증과의 유사성 평가
- 위 데이터가 확보되기 전에는 추가 임상 개발 투자를 보류할 것을 권고
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

