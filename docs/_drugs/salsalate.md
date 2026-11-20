---
layout: default
title: Salsalate
parent: 모델 예측만 (L5)
nav_order: 684
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-15
monitor_inn: "SALSALATE"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia"]
description: "Salsalate: 예측 신규 적응증 말단중간이형성증 Hunter-Thompson형 (acromesomelic dysplasia, Hunter-Thompson type) (근거 수준 L5). 기존 적응증: 1. 주효능 효과 류마티양 관절염, 골관절염(퇴행성 관절질환) 2. 다음 질환에도 사용할 수 있다…"
---

# Salsalate
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

## Salsalate: 말단중간이형성증 Hunter-Thompson형 (acromesomelic dysplasia, Hunter-Thompson type)
{: .text-alpha }

## 한 문장 요약

Salsalate는 비아세틸화 살리실산염 계열 약물로, 한국에서 단일제 정제(수출용)로 허가되어 있습니다. TxGNN 모델은 **말단중간이형성증 Hunter-Thompson형(acromesomelic dysplasia, Hunter-Thompson type)**에 효과가 있을 수 있다고 예측하지만, 이를 지지하는 **임상시험은 0건, 문헌은 0편**이며 생물학적 타당성도 낮아 모델 예측 단계(L5)에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 주효능 효과 류마티양 관절염, 골관절염(퇴행성 관절질환) 2. 다음 질환에도 사용할 수 있다. 류마트열, 결합직염, 견관절주위염, 증후성 신경통, 요통, 두통, 치통, 월경통, 감기로 인한 발열 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200710658/EE)) |
| 예측 신규 적응증 | 말단중간이형성증 Hunter-Thompson형 (acromesomelic dysplasia, Hunter-Thompson type) |
| TxGNN 예측 점수 | 0.9992 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 허가되었으나 미시판 (수출용 허가만 유효: 1건 / 전체 1건) |
| 허가증 수 | 1건 (국내 0건 · 유효 0건 / 수출용 1건 · 유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Salsalate 처방 정보(Prescribing Information)의 “Clinical Pharmacology” 항목에 따르면(비공식 번역): “살리실산(살살레이트의 주요 대사체)은 시험관 내에서 프로스타글란딘 합성의 약한 억제제이지만, 살살레이트는 생체 내에서 프로스타글란딘 합성을 선택적으로 억제하는 것으로 보이며 1, 아스피린 2 및 인도메타신 3과 동등한 항염증 활성을 나타낸다. 아스피린과 달리 살살레이트는 혈소판 응집을 억제하지 않는다 4.” 영어 원문: "Although salicylic acid (the primary metabolite of salsalate) is a weak inhibitor of prostaglandin synthesis in vitro, salsalate appears to selectively inhibit prostaglandin synthesis in vivo 1, providing anti-inflammatory activity equivalent to aspirin 2 and indomethacin 3. Unlike aspirin, salsalate does not inhibit platelet aggregation 4." ([DailyMed: salsalate prescribing information, Amneal Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=213f0930-4a4a-4894-90b9-70c12daaa093), 버전 2024-10-30; 확인일 2026-11-19). 일반적으로 알려진 바에 따르면 Salsalate는 비아세틸화 살리실산염으로, NF-κB 억제, AMPK 활성화, 약한 COX 억제 작용을 가집니다.

Hunter-Thompson형 말단중간이형성증은 CDMP1/GDF5 기능상실 변이로 생기는 희귀 골격 질환입니다. Salsalate의 작용이 GDF5/BMP 신호 회복으로 이어질 만한 기전적 경로는 없습니다.

## 다른 예측 후보

상위 8개 예측은 모두 임상시험과 문헌 근거가 없습니다.

| 순위 | 예측 질환 | TxGNN 점수 | 근거 수준 | 평가 |
|-----|---------|-----------|---------|------|
| 1 | 말단중간이형성증 Hunter-Thompson형 | 0.9992 | L5 | 기전 연결 없음 |
| 2 | 단신증-법랑질형성부전 증후군 | 0.9991 | L5 | 기전 연결 없음 |
| 3 | 근경화증 (myosclerosis) | 0.9990 | L5 | 염증성 섬유화에 대한 이론적 가능성만 있음 |
| 4 | 안구결손 소안구증-근위부 단축 이형성 증후군 | 0.9989 | L5 | 발달 이상으로 기전 연결 없음 |
| 5 | 단신증 (brachyolmia) | 0.9989 | L5 | 유전적 원인을 다루지 못함 |
| 6 | 단지증-합지증 증후군 | 0.9989 | L5 | 선천 기형으로 출생 후 약물로 교정하기 어려움 |
| 7 | 가성연골무형성증 | 0.9978 | L5 | 염증과 ER 스트레스 관련 추측만 있으며 증상(관절통) 완화 가능성만 존재 |

다만 Salsalate는 표준 NSAID보다 COX 억제가 약하고 직접 근거도 없어, 계열 수준의 간접 추론에 의존합니다. 추가 검토 전에 문헌 조사가 필요합니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200710658 | 디살라트정750밀리그램(살살레이트)(수출용) | 백색 장방형의 필름코팅정 | 허가사항 PDF 링크로만 제공되어 요약 불가 |

## 안전성 고려사항

허가사항의 경고·금기 정보는 이 보고서용으로 수집된 자료에 없으므로 허가사항을 참조하세요.

- **지식 그래프 기반 금기 질환** (허가 문서가 아닌 TxGNN 지식 그래프 PrimeKG의 약물-질환 금기 연결 기준): 간부전·간질환, 신장질환, 담낭질환, 위염, 활동성 소화성 궤양, 위식도 역류질환, 식도염, 당뇨병, 당뇨병성 케톤산증, 혈액응고장애, 혈우병, 선천성 프로트롬빈 결핍, 비타민 K 결핍 출혈성 질환, 혈소판감소성 자반증, 빈혈, 심혈관질환·심장질환, 갑상선기능항진증(Graves병 포함), 비강 용종, 요관축농증.
- **약물 상호작용**: 조회된 상호작용은 총 100건이며, 그중 일부는 다음과 같습니다.
  - 중등도(Moderate): 코르티코스테로이드(hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), 메살라진, 발살라지드, 혈당강하제(chlorpropamide, glimepiride, repaglinide, 인슐린 아스파트·데글루덱·디터미르), 구연산칼륨, 피코설페이트, 폴리에틸렌글리콜(전해질 포함), 황산나트륨
  - 경미(Minor): 프로톤펌프억제제(rabeprazole, omeprazole, dexlansoprazole)

## 결론 및 다음 단계

**결정: Hold**

**사유:**
모든 예측 질환에 임상시험과 문헌 근거가 없으며, 상위 예측은 Salsalate의 약리와 기전상 연결되지 않습니다. 높은 TxGNN 점수만으로는 진행 근거가 부족합니다.

**진행하려면 필요한 것:**
- 허가사항 PDF에서 적응증, 경고, 금기 정보 확보
- DrugBank 등에서 상세 작용 기전(MOA) 데이터 확보

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: salsalate prescribing information, Amneal Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=213f0930-4a4a-4894-90b9-70c12daaa093) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

