---
layout: default
title: Ibuprofen
parent: 모델 예측만 (L5)
nav_order: 409
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-24
description: "Ibuprofen: 예측 신규 적응증 말단중간형 이형성증, Hunter-Thompson형 (acromesomelic dysplasia… (근거 수준 L5). 기존 적응증: 류마티양 관절염, 연소성 류마티양 관절염, 골관절염(퇴행성 관절질환), 감기로 인한 발열 및 동통, 요통, 월경곤란증…"
monitor_inn: "IBUPROFEN"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Ibuprofen
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

## Ibuprofen: 류마티스 관절염·통증·발열에서 말단중간이형성증 헌터-톰슨형으로
{: .text-alpha }

## 한 문장 요약

Ibuprofen은 비선택적 COX 억제제(NSAID)로, 원래 류마티양 관절염, 골관절염, 감기로 인한 발열 및 동통, 요통, 생리통 등에 사용되었습니다.
TxGNN 모델은 **말단중간형 이형성증, Hunter-Thompson형(acromesomelic dysplasia, Hunter-Thompson type)**에 효과가 있을 수 있다고 예측하지만, 이를 지지하는 **임상시험은 0건**, **문헌도 0편**입니다.
기전상 연관성도 확인되지 않아 모델 예측 수준(L5)에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 류마티양 관절염, 연소성 류마티양 관절염, 골관절염(퇴행성 관절질환), 감기로 인한 발열 및 동통, 요통, 월경곤란증, 수술후 동통 등 |
| 예측 신규 적응증 | 말단중간형 이형성증, Hunter-Thompson형 (acromesomelic dysplasia, Hunter-Thompson type) |
| TxGNN 예측 점수 | 0.9974 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Ibuprofen 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “이부프로펜은 진통, 항염증 및 해열 특성을 가진다. CALDOLOR의 작용기전은 다른 NSAID와 마찬가지로 완전히 밝혀지지 않았으나, 시클로옥시게나제(COX-1 및 COX-2)의 억제가 관여한다.” 영어 원문: "Ibuprofen has analgesic, anti-inflammatory, and antipyretic properties. The mechanism of action of CALDOLOR, like that of other NSAIDs, is not completely understood but involves inhibition of cyclooxygenase (COX-1 and COX-2)." ([DailyMed: Caldolor (ibuprofen) prescribing information, Cumberland Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1eaa7790-f1a1-4f51-b10a-cbbaf033f684), 버전 2026-01-29; 확인일 2026-11-19). 알려진 정보에 따르면 Ibuprofen은 COX-1/COX-2를 비선택적으로 억제해 프로스타글란딘 합성을 줄이는 NSAID이며, 소염·진통·해열 효과로 통증과 염증성 질환에 쓰입니다.

반면 이 질환은 CDMP1/GDF5 유전자의 기능 상실 변이로 BMP 신호와 연골 형성이 손상되는 희귀 유전성 골격 이형성증입니다. Ibuprofen은 GDF5/BMP 경로에 작용하지 않으므로, 질환 자체를 변화시킬 만한 기전적 연결고리는 확인되지 않습니다.

TxGNN 점수가 매우 높은 것은 TxGNN 모델(딥러닝)이 관련 질환 간에 학습한 유사성을 반영한 결과일 수 있으며, 생물학적 근거를 의미하지는 않습니다. 기대할 수 있는 효과는 증상 완화 수준의 진통이며, 이는 이미 허가된 용도에 해당합니다.

참고로 같은 모델이 예측한 다른 후보(brachyolmia-amelogenesis imperfecta 증후군, myosclerosis, brachyolmia, brachydactyly-syndactyly 증후군, pseudoachondroplasia 등)도 모두 L5이며 임상시험과 문헌이 없습니다. 이 중 myosclerosis와 pseudoachondroplasia는 근육통·관절통 완화라는 간접적 가능성만 있고, 질환 경과를 바꾼다는 근거는 없습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 200001172 | 디퓨탭서방정(이부프로펜) | 흰색의 장방형 정제 | 동성제약(주) | — | 유효 |
| 201700729 | 이부로엔에스연질캡슐(이부프로펜) | 무색의 투명한 액이 든 연한 청록색의 투명한 달걀형 연질캡슐 | 코스맥스파마(주) | — | 유효 |
| 201604402 | 챔프이부펜시럽(이부프로펜) | 백색내지 미황색의 체리향 현탁성 시럽제 | 동아제약(주) | — | 유효 |
| 202302993 | 이지엔6이브정 | 밝은 분홍색의 원형 필름코팅정제 | (주)대웅제약 | — | 유효 |
| 202006761 | 이부스타플라스타(이부프로펜) | 이 약은 연한 노란색의 점착성물질을 연한 노란 분홍의 린트포에 도포하여… | 신신제약(주) | — | 유효 |

위 표는 허가 최소 20건 중 5건입니다.

<!-- licenses:end -->

## 안전성 고려사항

- **약물 상호작용**: 데이터에 100건의 상호작용이 있으며, 확인된 주요 항목은 다음과 같습니다.
  - **Major**: Acetylsalicylic acid(아스피린)
  - **Moderate**: 코르티코스테로이드(Betamethasone, Budesonide, Dexamethasone, Hydrocortisone), 설포닐우레아계 혈당강하제(Acetohexamide, Chlorpropamide, Glimepiride, Glipizide, Glyburide), Exenatide, Aprepitant, Balsalazide, Kanamycin, Levofloxacin, Fenfluramine, Dexfenfluramine
  - **Minor**: Famotidine, Ranitidine, Cimetidine
- **지식 그래프상 금기 관련 질환**(허가사항 문구가 아닌 모델 지식 그래프 기반): 고혈압, 간부전·간질환, 신장질환, 소화성 궤양, 염증성 장질환, 혈소판감소증, 혈액응고 장애, 뇌졸중·뇌혈관 질환, 심근경색, 당뇨병, 간질, 만성폐쇄성폐질환, 전신홍반루푸스 등

허가사항의 경고 및 금기 정보는 이번 데이터에 포함되어 있지 않으므로, 상세 내용은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 점수(0.9974)는 높지만 임상시험과 문헌이 전혀 없고, COX 억제와 GDF5/BMP 신호 결손 사이에 기전적 연결고리도 없습니다. 이 예측은 계산상의 산물로 판단되며, 증상 완화 목적의 진통 효과는 이미 허가된 적응증 범위입니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 데이터 보완 (DrugBank 조회)
- 허가사항(경고·금기) 확보: 현재 누락되어 안전성 선별 단계로 진행할 수 없음 (MFDS 허가사항 PDF 다운로드 및 분석)
- 이 질환에서 Ibuprofen의 효과를 시사하는 전임상·임상 근거 확보 (현재 없음)
- 필요하다면 증상 완화(통증 관리)로 목표를 한정한 별도의 평가

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Caldolor (ibuprofen) prescribing information, Cumberland Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1eaa7790-f1a1-4f51-b10a-cbbaf033f684) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

