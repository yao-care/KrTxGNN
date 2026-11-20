---
layout: default
title: Meloxicam
parent: 모델 예측만 (L5)
nav_order: 499
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-20
description: "Meloxicam: 예측 신규 적응증 말단중간이형성증, Hunter-Thompson형 (acromesomelic dysplasia… (근거 수준 L5). 기존 적응증: 1. 통증과 운동실조를 수반하는 골관절염(퇴행관절염)의 급성악화시 단기간의 증상치료 2. 류마티스관절염의…"
monitor_inn: "MELOXICAM"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "rheumatoid nodulosis", "WHIM syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Meloxicam
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **8** 건
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

## Meloxicam: 비스테로이드 소염진통제에서 말단중간이형성증 헌터-톰슨형으로
{: .text-alpha }

## 한 문장 요약

Meloxicam은 COX-2 선호적 비스테로이드 소염진통제(NSAID)로, 한국에서 20건의 허가를 받아 시판 중입니다.
TxGNN 모델은 **말단중간이형성증, Hunter-Thompson형(acromesomelic dysplasia, Hunter-Thompson type)**에 효과가 있을 수 있다고 예측하지만, 이 예측을 지지하는 **임상시험은 0건, 문헌도 0편**이며 모델 예측만 존재합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 통증과 운동실조를 수반하는 골관절염(퇴행관절염)의 급성악화시 단기간의 증상치료 2. 류마티스관절염의 증상치료 3. 강직척추염의 증상치료 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200402675/EE)) |
| 예측 신규 적응증 | 말단중간이형성증, Hunter-Thompson형 (acromesomelic dysplasia, Hunter-Thompson type) |
| TxGNN 예측 점수 | 0.9992 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Meloxicam 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “멜록시캄은 진통, 항염 및 해열 특성을 갖는다. Zybic™의 작용 기전은 다른 NSAID와 마찬가지로 완전히 밝혀지지 않았으나, 사이클로옥시게나제(COX-1 및 COX-2)의 억제를 포함한다.” 영어 원문: "Meloxicam has analgesic, anti-inflammatory, and antipyretic properties. The mechanism of action of Zybic™, like that of other NSAIDs, is not completely understood but involves inhibition of cyclooxygenase (COX-1 and COX-2)." ([DailyMed: Zybic (meloxicam) prescribing information, Redmont Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a1c2d65f-ebb1-48bf-8fa1-c216f7d570ec), 버전 2026-09-25; 확인일 2026-11-19). 알려진 정보에 따르면 Meloxicam은 COX-2 선호적 NSAID로, 프로스타글란딘 매개 염증과 통증을 줄이는 약물입니다.

헌터-톰슨형 말단중간이형성증은 CDMP1/GDF5 기능상실 변이로 골격 발달이 저해되는 희귀 유전질환입니다. Meloxicam은 GDF5/BMP 신호전달이나 연골 형성과 알려진 연관성이 없습니다. 따라서 높은 예측 점수는 TxGNN 모델(딥러닝)에서 나온 값으로, 모델이 관련 질환 사이에서 학습한 유사성을 반영할 수 있을 뿐 생물학적 근거는 아닙니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200900845 | 모빅캡슐15밀리그램 (한국베링거인겔하임) | 경질캡슐 | 허가 문서 링크로만 제공됨 |
| 200402675 | 메록스캄캡슐15밀리그램 (한미약품) | 경질캡슐 | 허가 문서 링크로만 제공됨 |
| 200400387 | 메로빅캡슐 (셀트리온제약) | 경질캡슐 | 허가 문서 링크로만 제공됨 |
| 201903234 | 멜로그린캡슐7.5밀리그램 (시어스제약) | 경질캡슐 | 허가 문서 링크로만 제공됨 |
| 201207083 | 류멜캡슐15밀리그램 (한림제약) | 경질캡슐 | 허가 문서 링크로만 제공됨 |

위 5건 외에도 총 20건의 허가가 모두 유효하며, 전부 캡슐제 단일제입니다(7.5mg 및 15mg).

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 대부분 중등도(Moderate)입니다. 주요 항목은 다음과 같습니다.
  - 코르티코스테로이드: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide
  - 아스피린(acetylsalicylic acid)
  - 혈당강하제: metformin, glimepiride, chlorpropamide
  - 메살라진, 발살라자이드
  - 아미노글리코사이드 및 글리코펩타이드: vancomycin, kanamycin
  - 칼륨 제제 및 장정결제
  - 경미(Minor) 수준: linaclotide
- **지식 그래프 기반 금기 관련 질환** (허가 문서가 아닌 모델 지식 그래프 기준): 고혈압, 신장질환, 울혈성 심부전, 위염, 활동성 소화성 궤양, 심근경색, 뇌졸중, 뇌혈관질환, 혈액응고질환, 빈혈, 당뇨병 등 심혈관·신장·위장관 관련 질환이 포함됩니다.

허가사항의 경고 및 금기 항목은 이번 데이터에 포함되어 있지 않으므로 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
최상위 예측인 Hunter-Thompson형 말단중간이형성증은 모델 점수만 높을 뿐 임상시험과 문헌이 없고, Meloxicam과의 기전적 연결고리도 확인되지 않습니다. 상위 10개 예측 모두 근거 수준 L5(1건은 L4 수준의 간접 근거)로, 현재로서는 재창출 진행을 뒷받침하기 어렵습니다.

**진행하려면 필요한 것:**
- 허가 문서에서 허가 적응증, 경고, 금기 정보 확보 (안전성 선별의 선행 조건)
- DrugBank 등에서 Meloxicam의 작용 기전(MOA) 데이터 확보
- 생물학적으로 타당한 6위(척추관절병증)와 8위(연소성 특발성 관절염) 후보에 대해 NSAID 계열 근거(임상시험, 체계적 문헌고찰)를 별도로 수집하여 재평가
- 골격 이형성증 계열 예측(1~5위, 10위)은 네트워크 근접성 인공물 가능성이 크므로 우선순위에서 제외 검토

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Zybic (meloxicam) prescribing information, Redmont Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a1c2d65f-ebb1-48bf-8fa1-c216f7d570ec) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

