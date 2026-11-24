---
layout: default
title: Aminocaproic Acid
parent: 모델 예측만 (L5)
nav_order: 58
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Aminocaproic Acid: 예측 신규 적응증 중증 비증식성 당뇨망막병증 (Severe Nonproliferative Diabetic Retinopathy) (근거 수준 L5). 기존 적응증: 눈의 피로, 결막충혈, 수영 후 눈의 불쾌감 또는 먼지나 땀이 눈에 들어갔을 때, 자외선 및 기타광선에 의한 눈의 염증 등"
monitor_inn: "AMINOCAPROIC ACID"
predicted_indications: ["severe nonproliferative diabetic retinopathy"]
---

# Aminocaproic Acid
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

## Aminocaproic Acid: 눈 피로·결막충혈에서 중증 비증식성 당뇨망막병증으로
{: .text-alpha }

## 한 문장 요약

Aminocaproic acid는 한국에서 점안액·세안액 성분으로 허가되어 눈의 피로, 결막충혈 등에 사용되고 있습니다.
TxGNN 모델은 **중증 비증식성 당뇨망막병증(Severe Nonproliferative Diabetic Retinopathy)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**으로 모델 예측만 존재합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 눈의 피로, 결막충혈, 수영 후 눈의 불쾌감 또는 먼지나 땀이 눈에 들어갔을 때, 자외선 및 기타광선에 의한 눈의 염증 등 |
| 예측 신규 적응증 | 중증 비증식성 당뇨망막병증 (Severe Nonproliferative Diabetic Retinopathy) |
| TxGNN 예측 점수 | 0.9927 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Aminocaproic Acid 처방 정보(Prescribing Information)의 “Clinical Pharmacology” 항목에 따르면(비공식 번역): “아미노카프로산의 섬유소용해 억제 효과는 주로 플라스미노겐 활성화인자의 억제를 통해, 그리고 그보다 적은 정도로 항플라스민 활성을 통해 나타나는 것으로 보인다.” 영어 원문: "The fibrinolysis-inhibitory effects of aminocaproic acid appear to be exerted principally via inhibition of plasminogen activators and to a lesser degree through antiplasmin activity." ([DailyMed: aminocaproic acid prescribing information, Kesin Pharma Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5e5ebfcb-c3a2-1fcf-e063-6394a90a356a), 버전 2026-11-09; 확인일 2026-11-19). 일반적으로 aminocaproic acid는 라이신 유사체인 항섬유소용해제로, 플라스미노겐 활성화와 플라스민 활성을 억제하는 것으로 알려져 있습니다.

이 성질로부터 두 가지 가설을 세울 수 있습니다. 첫째, 섬유소용해와 관련된 유리체·망막 출혈을 줄일 가능성이 있습니다. 둘째, 플라스민이 매개하는 세포외기질 재형성과 혈관 투과성을 조절할 가능성이 있습니다. 다만 이는 입증되지 않은 가설입니다.

반대로 항섬유소용해 및 혈전 촉진 작용이 당뇨성 미세혈관 병변에서 망막 혈관 폐색과 허혈을 악화시킬 수 있다는 이론적 안전성 우려도 있습니다. 또한 현재 허가된 적응증(눈 피로, 결막충혈, 눈 세정 등)은 당뇨망막병증과 직접적인 관련이 없습니다. 높은 예측 점수에도 불구하고 이는 모델 기반 예측일 뿐입니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201708185 | 일양투아이블루점안액 | 무색 투명한 플라스틱 용기에 든 무색 투명한 점안액 | 일양약품(주) | — | 유효 |
| 202201175 | 프렌즈아이드롭케어점안액(1회용) | 무색투명한 플라스틱 용기에 든 무색 투명한 점안액 | 제이더블유중외제약(주) | — | 유효 |
| 199000583 | 청나점안액 | 무색투명한 액이 담청색 투명한 플라스틱용기에 든 점안제 | (주)바이넥스 | — | 유효 |
| 202302477 | 눈앤큐점안액 | 투명한 용기에 들어있는 무색내지 미황색의 투명한 수용성점안제 | 한미약품(주) | — | 유효 |
| 201507771 | 아이봉씨세안액 | 무색투명한 액이 무색투명한 플라스틱 용기에 든 액제 | 동아제약(주) | — | 유효 |

위 표는 허가 최소 20건 중 5건입니다.

<!-- licenses:end -->

허가에는 설파메톡사졸 등 다른 유효성분이 함께 표시된 점안제(아이케어점안액, 옵트클린점안액)도 있습니다. 허가 건수와 상태는 빠른 개요와 위 표에 있습니다.

<!-- review:begin kr-lic-20261124b-aminocaproic_acid-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “전체 18건이 모두 단일 성분 제제이며 유효 상태입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 이 약의 허가에는 다른 유효성분이 함께 들어 있는 복합제도 있으며, 허가 건수는 자료와 맞지 않아 빠른 개요와 표를 가리키도록 고쳤습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124b-aminocaproic_acid-1 -->

## 안전성 고려사항

- **약물 상호작용**: 데이터가 확인된 상호작용은 총 75건입니다. 이 중 중등도(Moderate) 수준은 **alteplase**, **anistreplase** 등 혈전용해제와의 병용이며, 나머지 상당수는 등급이 확인되지 않았습니다(morphine, omeprazole, simvastatin, acetylsalicylic acid 등).
- **지식 그래프 기반 금기 질환** (허가사항이 아닌 TxGNN 지식 그래프 기준): 신장 질환, 요관 농양, 간 질환, 담낭 질환, 파종성 혈管내 응고(DIC), 전격성 자반증, 후천성 전격성 자반증, 혈전성 질환.

허가사항의 경고 및 금기 내용은 확인되지 않았으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 높지만 뒷받침하는 임상시험과 문헌이 전혀 없는 L5 단계입니다. 또한 혈전성 질환이 지식 그래프상 금기로 나타나, 당뇨성 미세혈관 병변에서 허혈을 악화시킬 수 있다는 이론적 안전성 우려가 있습니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기) 확보 및 파싱: 안전성 1차 검토에 필수
- 상세한 약물 작용 기전(MOA) 데이터 확보
- 당뇨망막병증에서의 항섬유소용해제 관련 전임상 및 문헌 조사
- 점안 투여 시 전신 노출과 망막 도달 가능성에 대한 투여 경로 적합성 평가
- 당뇨망막병증 환자의 혈전·허혈 위험에 대한 안전성 검토

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: aminocaproic acid prescribing information, Kesin Pharma Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5e5ebfcb-c3a2-1fcf-e063-6394a90a356a) |
| 2026-11-24 | 단일제·복합제 구분: “전체 18건이 모두 단일 성분 제제이며 유효 상태입니다.” → 자료 기준으로 수정(건수는 빠른 개요와 표) | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

