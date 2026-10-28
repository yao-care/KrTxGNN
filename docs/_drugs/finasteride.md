---
layout: default
title: Finasteride
parent: 모델 예측만 (L5)
nav_order: 349
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Finasteride: 예측 신규 적응증 Ambras형 전신 선천성 다모증 (Ambras type hypertrichosis universalis congenita) (근거 수준 L5). 기존 적응증: 허가증에 적응증 원문이 수록되어 있지 않아 확인할 수 없음 (허가사항 참조)"
monitor_inn: "FINASTERIDE"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly"]
---

# Finasteride
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

## Finasteride: 안드로겐성 탈모에서 Ambras형 선천성 전신 다모증으로
{: .text-alpha }

## 한 문장 요약

Finasteride는 제2형 5-알파 환원효소를 억제하여 DHT(디하이드로테스토스테론)를 낮추는 약물로, 한국에서 20건의 단일제 허가를 받아 시판 중입니다.
TxGNN 모델은 **Ambras형 전신 선천성 다모증(Ambras type hypertrichosis universalis congenita)**을 1순위로 예측했지만, 이를 뒷받침하는 임상시험과 문헌은 없습니다.
2순위인 **다모증(hypertrichosis)**에 대해서는 **간접적인 종설 문헌 4편**만 확인되었고, 직접적인 임상시험 근거는 **없습니다**.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에 적응증 원문이 수록되어 있지 않아 확인할 수 없음 (허가사항 참조) |
| 예측 신규 적응증 | Ambras형 전신 선천성 다모증 (Ambras type hypertrichosis universalis congenita) |
| TxGNN 예측 점수 | 0.9999 |
| 근거 수준 | L5 (1순위 기준) / L4 (2순위 다모증 기준) |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Finasteride는 제2형 5-알파 환원효소를 억제해 DHT를 낮추며, 안드로겐성 탈모 치료에 확립되어 있고 다모증(hirsutism)에는 오프라벨로 사용됩니다. 이 기전은 모낭에 작용하는 약물이라는 점에서 모발 관련 질환과 느슨하게 연결됩니다.

그러나 1순위인 Ambras 증후군은 TRPS1 조절에 영향을 주는 유전체 재배열과 관련된 선천성 질환으로, 안드로겐에 의해 유발되는 질환이 아닙니다. 따라서 기전상 근거가 약하며, 매우 높은 예측 점수는 TxGNN 모델(딥러닝)이 관련 질환 사이에서 학습한 유사성을 반영했을 가능성이 있을 뿐, 생물학적 근거는 아닙니다.

2순위인 다모증(hypertrichosis)은 일반적으로 안드로겐 비의존적이어서 기전이 부분적으로만 들어맞습니다. 안드로겐 의존성인 hirsutism과 구분해서 해석해야 합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

다음 문헌은 2순위 예측인 다모증(hypertrichosis) 기준입니다. 1순위 질환에 대한 문헌은 없습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [12223963](https://pubmed.ncbi.nlm.nih.gov/12223963/) | 2002 | Review | Ann Dermatol Venereol | 성인의 다모증은 의인성, 대사성, 영양성, 종양随伴성 원인이 있으며, 안드로겐 비의존 부위에서 나타나 호르몬 검사가 불필요함 |
| [10330884](https://pubmed.ncbi.nlm.nih.gov/10330884/) | 1999 | Review | Ther Umsch | 안드로겐성 탈모, 다모증(hirsutism), 다모증(hypertrichosis)의 새로운 치료 옵션 개관 |
| [12942187](https://pubmed.ncbi.nlm.nih.gov/12942187/) | 2003 | Review | Hautarzt | 남성형 탈모에 finasteride, 다모증에 레이저 제모 등 모발 질환 치료법 정리 |
| [12444520](https://pubmed.ncbi.nlm.nih.gov/12444520/) | 2002 | 방법론/진단 도구 | Hautarzt | 모발 밀도, 굵기, 성장 속도를 분석하는 TrichoScan 소개 |

이 문헌들은 모두 독일어 서술형 종설 또는 기법 논문으로, finasteride가 다모증(hypertrichosis)을 치료한다는 직접적 근거는 제공하지 않습니다.

## 한국 시판 정보

허가증 20건 모두 유효하며 모두 단일제입니다. 이 중 주요 5건은 다음과 같습니다. 허가 적응증은 허가증에 원문 대신 링크만 수록되어 있어 요약할 수 없으므로 허가사항을 참조하세요.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202001530 | 피나스텐정1밀리그램 | 필름코팅정 (황갈색 팔각형) | 허가사항 참조 |
| 200803186 | 유나시아정 | 필름코팅정 (황갈색 팔각형) | 허가사항 참조 |
| 201603906 | 비보존피나스테리드정5밀리그램 | 필름코팅정 (청색 원형) | 허가사항 참조 |
| 201402875 | 메리나정 | 필름코팅정 (황갈색 팔각형) | 허가사항 참조 |
| 201907898 | 텔콘알에프피나스테리드정5밀리그램 | 필름코팅정 (청색 사과모양) | 허가사항 참조 |

## 안전성 고려사항

- **지식 그래프상 금기 질환**: 간 질환(liver disease), 담낭 질환(gallbladder disease). 허가 문서가 아닌 지식 그래프 정보이므로 허가사항과 대조가 필요합니다.
- **약물 상호작용**: 총 100건이 조회되었으며, 일부로 Calcitriol, Doxycycline, Clotrimazole, Dolasetron, Dicyclomine, Chlorhexidine, Famotidine, Acetylsalicylic acid, Amoxicillin, Bupropion 등이 있습니다. 위험 등급은 모두 "알 수 없음"으로 표기되어 임상적 중요도를 판단할 수 없습니다.

그 밖의 경고 및 금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 매우 높지만 1순위 Ambras형 다모증은 임상시험과 문헌이 없고 기전상 근거도 약합니다. 2순위 다모증(hypertrichosis)도 간접적인 종설 4편뿐이며 안드로겐 비의존성 질환이라 기전 적합성이 제한적입니다. 3~6순위 예측 역시 근거가 없어 현 단계에서 진행하기 어렵습니다.

**진행하려면 필요한 것:**
- 허가 적응증과 경고·금기를 확인하기 위한 허가사항(첨부문서) 확보
- 상세 작용 기전(MOA) 데이터 보완
- 다모증(hypertrichosis)에서 finasteride의 효과를 직접 평가한 임상 또는 전임상 연구 탐색
- 안드로겐 의존성 다모증(hirsutism)과 안드로겐 비의존성 다모증(hypertrichosis)을 구분한 재평가
- 간 질환·담낭 질환 금기 및 상호작용 위험 등급에 대한 검증
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

