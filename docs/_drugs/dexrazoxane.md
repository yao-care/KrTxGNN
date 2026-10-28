---
layout: default
title: Dexrazoxane
parent: 모델 예측만 (L5)
nav_order: 274
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Dexrazoxane: 예측 신규 적응증 경화성 담관염 (Sclerosing Cholangitis) (근거 수준 L5). 기존 적응증: 확인 불가 (허가 정보에 적응증 본문 대신 문서 링크만 수록됨)"
monitor_inn: "Dexrazoxane"
predicted_indications: ["sclerosing cholangitis", "bronchitis", "paratyphoid fever", "conjunctivitis", "epiglottitis", "peritonitis", "laryngitis", "urinary tract infection (disease)", "pyelonephritis", "cystitis"]
---

# Dexrazoxane
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

## Dexrazoxane: 허가 적응증 미확인 상태에서 경화성 담관염으로
{: .text-alpha }

## 한 문장 요약

Dexrazoxane은 한국에서 단일제 주사제(카디옥산주)로 허가·시판 중이나, 이 보고서에 정리된 데이터에는 허가 적응증의 구체적 내용이 확인되지 않습니다.
TxGNN 모델은 **경화성 담관염(Sclerosing Cholangitis)**에 효과가 있을 수 있다고 예측하지만, 이를 지지하는 **임상시험은 0건, 문헌도 0편**으로 모델 예측 단계(L5)에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 정보에 적응증 본문 대신 문서 링크만 수록됨) |
| 예측 신규 적응증 | 경화성 담관염 (Sclerosing Cholangitis) |
| TxGNN 예측 점수 | 0.9999 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 다만 Dexrazoxane은 철 킬레이트 작용과 topoisomerase II 촉매 억제 작용을 가진 약물로 알려져 있으며, 철 의존적 산화 스트레스를 줄이는 것으로 이해됩니다.

이 작용이 담즙정체성 또는 섬유화성 간 손상과 이어질 가능성은 이론적으로 생각해 볼 수 있습니다. 그러나 이는 추측일 뿐이며, 이번 데이터로는 뒷받침되지 않습니다. 기존 적응증과 신규 적응증 사이의 연관성도 아직 평가되지 않았습니다.

TxGNN 모델(딥러닝)의 점수가 매우 높더라도 이는 모델이 관련 질환 간에 학습한 유사성을 반영한 것일 수 있으며 생물학적 근거는 아니므로, 실제 효능을 보증하지 않습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200704949 | 카디옥산주500밀리그램(덱스라족산) | 미황색의 동결건조 덩어리가 든 바이알 | 허가사항 문서 참조 (본문 미확인) |

## 안전성 고려사항

- **약물 상호작용**: 총 19건이 확인되었습니다.
  - **Major (10건)**: 생백신 및 생균 제제 계열입니다. 해당 약물은 Bacillus Calmette-Guérin(BCG), 홍역, 유행성이하선염, 풍진, 로타바이러스, 두창(Vaccinia), 장티푸스(생백신), 황열, 대상포진 백신(Varicella Zoster), Talimogene laherparepvec입니다.
  - **Moderate (9건)**: Doxorubicin, Doxorubicin(리포좀), Dimethyl fumarate, Diroximel fumarate, Monomethyl fumarate, 아데노바이러스 4형 백신 항원, Bifidobacterium longum infantis, Lactobacillus acidophilus, 콜레라 생백신(Vibrio cholerae CVD 103-HgR)입니다.

경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
경화성 담관염에 대한 임상시험과 문헌이 전혀 없고, 기전 연결도 추측 수준입니다. 현재는 모델 예측만 있는 L5 단계이므로 추가 개발을 진행할 근거가 부족합니다.

**진행하려면 필요한 것:**
- 허가사항(MFDS 첨부문서)의 적응증, 경고, 금기 정보 확보
- DrugBank 등에서 상세 작용 기전(MOA) 확보
- 경화성 담관염과 철 의존적 산화 스트레스(페롭토시스) 사이의 연관성에 대한 전임상 근거 탐색
- 관련 임상시험 및 문헌 재검색

---

### 참고: 다른 예측 적응증 (요약)

이번 보고서는 최상위 예측(경화성 담관염)을 중심으로 작성했습니다. 나머지 예측은 아래와 같습니다.

- **방광염(Cystitis, 10위)**: 유일하게 L4(전임상·기전 수준)로 평가되었습니다. 페롭토시스가 사이클로포스파미드 유발 출혈성 방광염과 간질성 방광염에 관여한다는 전임상 문헌이 있습니다. 다만 Dexrazoxane을 직접 검증한 연구는 확인되지 않았고, 화학요법 유발 또는 페롭토시스 관련 방광 손상에 한정된 가설 단계입니다. 감염성 방광염에는 해당하지 않습니다.
- **기관지염, 파라티푸스, 결막염, 후두개염, 복막염, 후두염, 요로감염, 신우신염**: 모두 L5이며 Hold입니다. Dexrazoxane에 항균 작용이 없고 골수억제·면역억제 특성이 있어 감염성 질환과는 기전상 맞지 않으며, TxGNN 모델(딥러닝)이 관련 질환 간에 학습한 유사성이 반영된 결과일 가능성이 높습니다. 복막염에서 검색된 문헌 2편은 치료 효과를 뒷받침하지 않으며 키워드가 우연히 일치한 것으로 보입니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

