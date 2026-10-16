---
layout: default
title: Insulin Degludec
parent: 모델 예측만 (L5)
nav_order: 424
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Insulin Degludec: 예측 신규 적응증 제1형 당뇨병 (type 1 diabetes mellitus) (근거 수준 L5). 기존 적응증: 허가 적응증 본문은 이번 자료에 텍스트로 수록되어 있지 않아 확인할 수 없습니다(허가증 3건…"
---

# Insulin Degludec
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **6** 건
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

# Insulin Degludec: 기존 당뇨병 치료에서 제1형 당뇨병으로

## 한 문장 요약

Insulin degludec은 초지속형 기저 인슐린 유사체로, 한국에서 당뇨병 치료제로 허가·시판되고 있습니다.
TxGNN 모델은 **제1형 당뇨병(type 1 diabetes mellitus)**에 효과가 있을 것으로 예측하며, 이 예측을 뒷받침하는 **임상시험 40여 건**과 **문헌 19편**이 확인되었습니다.
다만 제1형 당뇨병은 이 약의 기존 용도와 사실상 같은 영역이므로, 엄밀한 의미의 재창출이라기보다 기존 적응증을 재확인한 결과에 가깝습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문은 이번 자료에 텍스트로 수록되어 있지 않아 확인할 수 없습니다(허가증 3건, 식약처 허가사항 문서 링크만 제공). |
| 예측 신규 적응증 | 제1형 당뇨병 (type 1 diabetes mellitus) |
| TxGNN 예측 점수 | 99.44% |
| 근거 수준 | L1 (완료된 Phase 3 RCT 다수) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 3건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 이번 자료에 없습니다. 알려진 정보에 따르면 Insulin degludec은 인슐린 수용체에 결합하여 부족한 내인성 인슐린을 대체하고 혈당을 낮추는 기저 인슐린 유사체입니다.

제1형 당뇨병은 인슐린이 절대적으로 결핍된 질환이므로, 이 약의 작용 방식이 질환의 병태생리와 직접 일치합니다. 따라서 TxGNN의 높은 예측 점수는 이미 확립된 사용을 반영한 것으로 해석됩니다.

참고로 같은 모델이 예측한 다른 후보(자가면역성 난소염, 옵시스모이형성증, 티아민 반응성 기능장애 증후군, 강직 인간 증후군 등)는 임상시험과 문헌이 전혀 없는 근거 수준 L5로, 모두 보류(Hold) 수준입니다. 이들은 제1형 당뇨병과의 동반 질환 연관성이나 신호 전달 경로의 간접적 유사성에서 나온 계산상의 예측으로 보입니다.

## 임상시험 근거

제1형 당뇨병 관련 임상시험이 다수 등록되어 있으며, 이 중 대표적인 10건을 정리했습니다. 완료된 Phase 3 시험이 여러 건 포함되어 있습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02034513](https://clinicaltrials.gov/study/NCT02034513) | Phase 3 | 완료 | 501 | SWITCH 1: 제1형 당뇨병에서 degludec과 glargine의 안전성·효능 비교(교차 시험) |
| [NCT05463744](https://clinicaltrials.gov/study/NCT05463744) | Phase 3 | 완료 | 692 | 주 1회 기저 인슐린 efsitora와 degludec 비교 |
| [NCT02500706](https://clinicaltrials.gov/study/NCT02500706) | Phase 3 | 완료 | 1108 | 성인에서 degludec 병용 시 속효성 인슐린 aspart와 NovoRapid 비교 |
| [NCT02670915](https://clinicaltrials.gov/study/NCT02670915) | Phase 3 | 완료 | 834 | 소아·청소년에서 degludec 병용 시 속효성 aspart와 NovoRapid 비교 |
| [NCT01835431](https://clinicaltrials.gov/study/NCT01835431) | Phase 3 | 완료 | 362 | 소아·청소년에서 degludec/aspart와 detemir 병용요법 비교 |
| [NCT00978627](https://clinicaltrials.gov/study/NCT00978627) | Phase 3 | 완료 | 548 | degludec/aspart 복합제와 detemir + aspart 비교(BOOST T1) |
| [NCT01569841](https://clinicaltrials.gov/study/NCT01569841) | Phase 3 | 완료 | 24 | 지속혈당측정으로 degludec과 glargine의 혈당 조절 비교 |
| [NCT04075513](https://clinicaltrials.gov/study/NCT04075513) | Phase 4 | 완료 | 343 | Toujeo(glargine 300 U/ml)와 Tresiba(degludec)의 혈당 목표 범위 및 변동성 비교 |
| [NCT03838783](https://clinicaltrials.gov/study/NCT03838783) | Phase 4 | 불명 | 30 | 운동량이 많은 환자에서 degludec과 인슐린 펌프 병용 요법 평가 |
| [NCT00612040](https://clinicaltrials.gov/study/NCT00612040) | Phase 2 | 완료 | 178 | degludec 두 제형과 glargine을 기저-식사 인슐린 요법으로 비교 |

이 외에도 약력학·약동학 중심의 Phase 1 시험, 한국 시판 후 조사(NCT03416855, 768명) 등 실제 사용 환경 연구가 다수 등록되어 있습니다. 일부 Phase 3 시험(NCT03740919, NCT03952130 등)은 degludec이 배경 기저 인슐린으로 쓰인 시험이어서 이 약 자체를 검증한 것은 아닙니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [39270686](https://pubmed.ncbi.nlm.nih.gov/39270686/) | 2024 | RCT | Lancet | QWINT-5: 성인 제1형 당뇨병에서 주 1회 efsitora와 degludec의 효능·안전성 비교(비열등성 Phase 3) |
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT | Lancet | ONWARDS 6: 주 1회 icodec과 매일 degludec의 기저-식사 요법 비교 |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT: 임신한 제1형 당뇨병 여성에서 degludec과 detemir 비교 |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | 체계적 문헌고찰/메타분석 | Clin Ther | degludec과 다른 장시간 작용 기저 인슐린의 효능·내약성 비교 |
| [33662147](https://pubmed.ncbi.nlm.nih.gov/33662147/) | 2021 | 체계적 문헌고찰 | Cochrane Database Syst Rev | 제1형 당뇨병에서 (초)장시간 작용 인슐린 유사체 평가 |
| [40627908](https://pubmed.ncbi.nlm.nih.gov/40627908/) | 2025 | 체계적 문헌고찰/메타분석 | J Diabetes Complications | degludec과 efsitora의 효능·안전성 비교 |
| [35476308](https://pubmed.ncbi.nlm.nih.gov/35476308/) | 2022 | 체계적 문헌고찰 | Int J Clin Pharm | 제1형 당뇨병에서 degludec U100과 glargine U300의 간접 비교 |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | 네트워크 메타분석 | Value Health | 성인 제1형 당뇨병의 기저 인슐린 요법별 상대적 효능·안전성 |
| [40903851](https://pubmed.ncbi.nlm.nih.gov/40903851/) | 2025 | 무작위 대조 시험 | Diabetes Obes Metab | 당뇨병성 케톤산증에서 degludec 조기 병용 효과 평가 |
| [23620200](https://pubmed.ncbi.nlm.nih.gov/23620200/) | 2013 | Review | Drugs | degludec 및 degludec/aspart의 당뇨병 치료 활용 개관 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201401271 | 리조덱플렉스터치주100단위/밀리리터 | 주사제(펜형, 무색 투명한 액) | 식약처 허가사항 문서 참조 |
| 201401272 | 트레시바플렉스터치주 100단위/밀리리터(인슐린데글루덱) | 주사제(펜형, 무색 투명한 액) | 식약처 허가사항 문서 참조 |
| 201905977 | 줄토피플렉스터치주 | 프리필드 펜형 주사제 | 식약처 허가사항 문서 참조 |

3건 모두 노보노디스크제약(주)의 유효한 단일제 허가입니다.

## 세포독성

해당 없음(항종양약이 아님)이므로 이 섹션은 생략합니다.

## 안전성 고려사항

- **약물 상호작용**: 상호작용 조회 결과 100건이 확인되었으며, 대부분 중등도(Moderate)입니다. 대표적으로 다음과 같은 약물이 있습니다.
  - 베타 작용제·교감신경 작용제: phenylephrine, pseudoephedrine, epinephrine, salbutamol, formoterol
  - 베타 차단제: acebutolol
  - 다른 항당뇨제: metformin, pioglitazone, alogliptin, albiglutide
  - 호르몬제·기타: estradiol, levonorgestrel, norethisterone, hydrocortisone, hydrochlorothiazide, doxycycline, alpelisib, ethanol
  - 경미(Minor) 수준: 국소 hydrocortisone, 국소 alclometasone

경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
제1형 당뇨병에서 degludec을 직접 평가한 완료된 Phase 3 RCT(SWITCH 1 등)와 다수의 체계적 문헌고찰이 있어 근거는 충분합니다. 다만 이는 기존 용도의 재확인이며, 허가 적응증 본문과 안전성 정보가 이번 자료에 없어 확인이 필요합니다.

**진행하려면 필요한 것:**
- 식약처 허가사항 문서(3건)에서 허가 적응증, 경고, 금기 사항 확보 및 제1형 당뇨병 허가 범위 확인
- 상세한 작용 기전(MOA) 데이터 보완
- 저혈당 위험 관리 계획과 병용약물 상호작용(특히 베타 작용제·다른 항당뇨제) 모니터링 방안
- 자가면역성 난소염 등 다른 예측 후보는 근거가 없으므로 보류하고, 추가 연구 없이는 진행하지 않음
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

