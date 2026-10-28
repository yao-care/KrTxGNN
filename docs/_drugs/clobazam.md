---
layout: default
title: Clobazam
parent: 모델 예측만 (L5)
nav_order: 222
evidence_level: L5
indication_count: 3
monitor_inn: "Clobazam"
predicted_indications: ["perioral myoclonia with absences", "restless legs syndrome", "polymicrogyria with optic nerve hypoplasia"]
last_modified_at: 2026-10-28
description: "Clobazam: 예측 신규 적응증 구순주위 근간대발작 동반 absence (근거 수준 L5). 기존 적응증: 이 보고서용으로 정리된 자료에는 허가 적응증 문구가 없습니다(허가증에는 식약처 문서 링크만 있음)"
---

# Clobazam
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

## Clobazam: 기존 적응증에서 구순주위 근간대발작 동반 absence(perioral myoclonia with absences)로
{: .text-alpha }

## 한 문장 요약

Clobazam은 1,5-벤조디아제핀 계열의 항경련제로, 한국에서 단일성분 제품 4건의 허가증이 확인됩니다. 다만 이 자료에는 허가 적응증의 구체적인 문구가 담겨 있지 않습니다.
TxGNN 모델은 **구순주위 근간대발작 동반 absence(perioral myoclonia with absences)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다. 따라서 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 이 보고서용으로 정리된 자료에는 허가 적응증 문구가 없습니다(허가증에는 식약처 문서 링크만 있음). |
| 예측 신규 적응증 | 구순주위 근간대발작 동반 absence |
| TxGNN 예측 점수 | 0.9979 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 4건 (모두 유효, 단일성분) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 없습니다. 알려진 정보에 따르면 Clobazam은 GABA-A 수용체를 매개로 한 억제 작용을 강화하는 1,5-벤조디아제핀계 항경련제입니다.

구순주위 근간대발작 동반 absence는 absence 발작과 입 주위의 근간대 경련이 나타나는 전신 유전성 간질 증후군입니다. GABA 계열 항경련 기전이 생물학적으로 적용 가능할 수 있습니다.

다만 이 연관성은 Clobazam의 일반적인 항경련 활성에서 추정한 것이며, 높은 TxGNN 점수(0.9979)도 계산상의 예측일 뿐입니다. 임상시험과 문헌이 제공되지 않아 직접 검증된 바는 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 198100698 | 센틸정10밀리그람(클로바잠) | 백색의 원형 정제 | 식약처 허가 문서 참조 |
| 198100711 | 센틸정5밀리그람(클로바잠) | 백색의 원형 정제 | 식약처 허가 문서 참조 |
| 200109979 | 푸리지움5밀리그람(클로바잠) | 백색의 원형 정제 | 식약처 허가 문서 참조 |
| 200109980 | 푸리지움10밀리그람(클로바잠) | 백색의 원형 정제 | 식약처 허가 문서 참조 |

제조사는 모두 (주)한독입니다.

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 기록되어 있습니다. 주요 항목은 다음과 같습니다.
  - 주의 수준 높음(Major): Morphine, Morphine(리포좀), Eliglustat
  - 중등도(Moderate): Bupropion, Aprepitant, Omeprazole, Esomeprazole, Lansoprazole, Cimetidine, Clarithromycin, Metoclopramide, Dronabinol, Fenfluramine, Dexfenfluramine
  - 경미(Minor): 마그네슘·알루미늄·칼슘 계열 제산제

그 외 경고 및 금기 등 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 질환을 직접 다룬 임상시험이나 문헌이 없고 모델 예측과 기전적 추정만 있어 근거 수준은 L5입니다. 허가사항의 경고·금기 정보도 확보되지 않아 안전성 검토를 진행할 수 없습니다.

**진행하려면 필요한 것:**
- 식약처 허가사항(적응증, 경고, 금기)을 내려받아 정리
- DrugBank에서 작용 기전(MOA) 데이터 확보
- 구순주위 근간대발작 동반 absence에서 Clobazam을 다룬 임상시험·문헌 조사
- 높은 상호작용 부담(100건)을 고려한 안전성 평가 계획

---

### 참고: 다른 예측 후보 (모두 Hold, 근거 수준 L5)

| 순위 | 예측 질환 | TxGNN 점수 | 비고 |
|-----|---------|-----------|------|
| 2 | 하지불안 증후군(restless legs syndrome) | 0.9930 | 클로나제팜 등 벤조디아제핀이 주로 수면 유지 개선 목적으로 비공식 사용된 바 있어 계열 수준의 근거는 있으나, 1차 치료제와는 기전이 다르고 진정·내성·의존성 부담이 있습니다. |
| 3 | 시신경 저형성 동반 다소뇌회증(polymicrogyria with optic nerve hypoplasia) | 0.9909 | 발작 증상 조절에 한정된 효과만 기대되며, 기저 기형이나 시신경 저형성에는 효과가 없을 것으로 보입니다. |
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

