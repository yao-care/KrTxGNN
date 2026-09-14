---
layout: default
title: Ustekinumab
parent: 僅模型預測 (L5)
nav_order: 714
evidence_level: L5
indication_count: 10
---

# Ustekinumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# 우스테키누맙: 건선에서 피부염으로

## 한 문장 요약

우스테키누맙(Ustekinumab)은 IL-12/IL-23 억제 기전의 생물학적제제로, 국내에는 아직 허가된 제품이 없습니다.
TxGNN 모델은 **피부염(Dermatitis)**에 효과가 있을 수 있다고 예측하며,
현재 **7건의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다. 다만 아토피피부염에서의 효능은
연구별로 결과가 엇갈려 추가 검증이 필요한 단계입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 건선, 건선성 관절염, 크론병, 궤양성 대장염 (해외 승인 기준; 국내 미허가, 출처: 문헌 PMID 36208443) |
| 예측 신규 적응증 | 피부염 (Dermatitis) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미상판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

DrugBank의 공식 MOA 기록은 현재 데이터 공백(Data Gap) 상태이지만, 수집된 문헌(PMID 27304428)에 따르면
우스테키누맙은 IL-12/IL-23의 공통 서브유닛인 p40을 표적으로 하는 인간 단클론항체(IgG1)로,
Th1·Th17·Th22 세포 활성화를 억제하는 기전을 가지며 주로 건선 치료에 사용되어 왔습니다.

건선과 아토피피부염(피부염의 대표 아형)은 모두 T세포 매개 만성 염증성 피부질환이라는 공통점이 있습니다.
건선은 Th1/Th17이 우세하고 아토피피부염은 전통적으로 Th2가 우세한 것으로 알려져 있으나,
최근 연구에서는 Th22 경로가 두 질환 모두에 관여한다는 점이 확인되면서 IL-12/23 억제제의 교차 적용
가능성이 제기되었습니다. 실제로 미국(PMID 27304428)과 일본(PMID 28338223)에서 각각 독립적인
Phase 2 무작위대조시험이 수행되며 이 기전적 가설을 임상적으로 검증한 바 있습니다.

다만 실사용 데이터(PMID 33849369)에서는 "산발적 사례 보고에서 상반된 결과"가 관찰된다고 보고하고 있어,
기전적 타당성은 있으나 임상적 효능의 일관성은 아직 확립되지 않은 상태입니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01945086](https://clinicaltrials.gov/study/NCT01945086) | Phase 2 | 완료 | 79 | 일본인 중증 아토피피부염 환자 대상 위약대조 이중맹검 시험, 우스테키누맙 2용량 안전성·유효성 평가 |
| [NCT01806662](https://clinicaltrials.gov/study/NCT01806662) | Phase 2 | 완료 | 32 | 기존 치료에 반응 불충분한 만성 아토피피부염 환자 대상 무작위 파일럿 연구 |
| [NCT05535738](https://clinicaltrials.gov/study/NCT05535738) | Phase 2/3 | 모집 중 | 45 | 접촉피부염 모델(suction blistering)로 생물학적제제의 피부 염증 기전 연구 |
| [NCT02074982](https://clinicaltrials.gov/study/NCT02074982) | Phase 3 | 완료 | 676 | 중등도-중증 판상건선 환자에서 세쿠키누맙 대비 우스테키누맙의 16주 PASI 효능 비교 (CLEAR) |
| [NCT07352566](https://clinicaltrials.gov/study/NCT07352566) | Phase 4 | 모집 전 | 10 | 아토피피부염·건선 대상 FDA 승인 약물의 피부 내 미세투여 디바이스 시험 |
| [NCT07041112](https://clinicaltrials.gov/study/NCT07041112) | N/A | 완료 | 1000 | 피부건선(±건선성관절염) 환자의 생물학적제제 10년 생존율에 대한 유전·대사 위험인자 관찰연구 |
| [NCT01356758](https://clinicaltrials.gov/study/NCT01356758) | N/A | 완료 | 126 | 중증 건선 환자에서 생물학적제제 치료와 심혈관 위험 평가 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [27304428](https://pubmed.ncbi.nlm.nih.gov/27304428/) | 2017 | RCT | Experimental Dermatology | 중등도-중증 성인 AD 환자 33명 대상 Phase 2 이중맹검 위약대조 시험, 효능·안전성 평가 |
| [28338223](https://pubmed.ncbi.nlm.nih.gov/28338223/) | 2017 | RCT | British Journal of Dermatology | 일본인 중증 AD 환자 대상 Phase 2 무작위 위약대조 이중맹검 시험 |
| [33074565](https://pubmed.ncbi.nlm.nih.gov/33074565/) | 2021 | 체계적 문헌고찰/메타분석 | Allergy | 중등도-중증 AD 전신치료제에 대한 EAACI 가이드라인용 근거 평가 |
| [29098604](https://pubmed.ncbi.nlm.nih.gov/29098604/) | 2018 | 체계적 문헌고찰/메타분석 | American Journal of Clinical Dermatology | AD에서 생물학적제제의 유효성에 대한 체계적 고찰 |
| [29164954](https://pubmed.ncbi.nlm.nih.gov/29164954/) | 2018 | 체계적 문헌고찰 | Journal of Dermatological Treatment | 우스테키누맙의 AD 치료 효능·안전성에 대한 체계적 고찰 |
| [33849369](https://pubmed.ncbi.nlm.nih.gov/33849369/) | 2022 | 실사용 근거(관찰) | Journal of Dermatological Treatment | AD 환자에서 우스테키누맙의 실사용 유효성 분석, 산발적 사례에서 상반된 결과 보고 |
| [36208443](https://pubmed.ncbi.nlm.nih.gov/36208443/) | 2022 | 종설 | Dermatologic Therapy | 우스테키누맙의 허가 외(off-label) 사용에 대한 종합 고찰 |
| [39201826](https://pubmed.ncbi.nlm.nih.gov/39201826/) | 2024 | 서술적 종설 | Children (Basel) | 소아 원형탈모·건선·AD·화농성한선염에서 생물학적제제·표적치료제 고찰 |
| [35130397](https://pubmed.ncbi.nlm.nih.gov/35130397/) | 2021 | 종설 | Dermatology Online Journal | TNF-α 억제제 및 IL-12/23 억제제의 피부과 영역 허가 외 사용 고찰 |
| [37929636](https://pubmed.ncbi.nlm.nih.gov/37929636/) | 2024 | 증례보고 | Australasian Journal of Dermatology | 중증 크론병·중증 AD 환자에서 듀필루맙+우스테키누맙 병용요법 증례, 7개월 추적 관찰 시 상호간섭 없음 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
미국과 일본에서 독립적으로 수행된 2건의 Phase 2 무작위대조시험이 아토피피부염에서 우스테키누맙의
효능 신호를 뒷받침하지만, 실사용 데이터에서는 상반된 결과가 보고되고 있어(PMID 33849369) 효능의
일관성이 아직 확립되지 않았습니다. 또한 국내에는 현재 허가된 제품이 없고(미상판, 허가증 0건),
공식 MOA 문서 및 TFDA급 안전성 정보(경고·금기)가 모두 데이터 공백(Blocking) 상태입니다.

**진행하려면 필요한 것:**
- 한국 식약처(MFDS) 기준 안전성 라벨(경고·금기·상호작용) 확보 — 현재 Blocking 등급 데이터 공백
- DrugBank 등 공식 소스를 통한 MOA 문서화 — 현재 High 등급 데이터 공백
- 아토피피부염 대상 Phase 3 확증 시험 결과 확인 (현재까지 Phase 2 단계에 머물러 있음)
- 국내 도입 시 허가 신청 경로 및 시판 계획 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

