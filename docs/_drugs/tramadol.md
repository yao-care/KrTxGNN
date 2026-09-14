---
layout: default
title: Tramadol
parent: 僅模型預測 (L5)
nav_order: 691
evidence_level: L5
indication_count: 10
---

# Tramadol
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

# Tramadol: 통증에서 골관절염(Osteoarthritis)으로

> **참고**: TxGNN 예측 순위 1위는 "osteoarthritis susceptibility"(골관절염 유전적 감수성)였으나, 이는 치료 가능한 임상 실체가 아닌 유전적 위험 표지자(OMIM식 감수성 노드)이며 뒷받침하는 근거도 사망률 관련 안전성 문헌 1편뿐이라 보고 대상에서 제외했습니다. 대신 실질적 임상 근거가 풍부한 **순위 2 "osteoarthritis"**를 이 보고서의 핵심 예측으로 다룹니다.

## 한 문장 요약

Tramadol은 중추성 아편유사제/SNRI 이중기전을 가진 진통제입니다.
TxGNN 모델은 **골관절염(Osteoarthritis)**에 효과가 있을 것으로 예측하며,
현재 **50건 이상의 임상시험**과 **20편 이상의 문헌**(ACR 가이드라인, Cochrane 체계적 고찰 포함)이 이를 뒷받침합니다.
다만 사망률·골절 위험 증가와 관련된 관찰연구 안전성 신호도 함께 보고되어 있어 주의가 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (한국 허가 정보 미확보 — Tramadol은 일반적으로 중등도~중증 통증에 사용되는 아편유사 진통제) |
| 예측 신규 적응증 | 골관절염 (Osteoarthritis) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L1 (완료된 Phase 3 RCT 다수) |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Tramadol은 μ-opioid 수용체에 대한 약한 효능제 작용과 세로토닌·노르에피네프린 재흡수 억제(SNRI) 작용을 동시에 갖는 이중기전 중추성 진통제입니다. 이 기전은 골관절염의 만성 통증 조절에 직접 대응하는 약리학적 표적으로, 실제로는 완전히 새로운 "재창출" 가설이라기보다 이미 임상적으로 광범위하게 활용되고 있는 진통 옵션입니다.

미국정형외과학회(AAOS) 가이드라인은 무릎 골관절염 환자에게 tramadol을 권고하고 있으며, 미국류마티스학회(ACR)/관절염재단(Arthritis Foundation) 2019 가이드라인도 NSAID와 함께 tramadol을 1차 치료 옵션으로 조건부 권고합니다. 즉, TxGNN의 예측은 이미 확립된 임상 실무와 일치하며, 이는 모델 예측의 타당성을 뒷받침하는 동시에 "신규성"보다는 "근거 재확인"의 성격이 강함을 시사합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04504812](https://clinicaltrials.gov/study/NCT04504812) | Phase 3 | 완료 | 1937 | 무릎 골관절염 통증 완화를 위한 단계적 치료전략 비교(오피오이드 의존도 감소 목적의 대규모 실용임상시험, tramadol 옵션 포함) |
| [NCT00348452](https://clinicaltrials.gov/study/NCT00348452) | Phase 3 | 완료 | 1000 | Tramadol HCl ER 100/200/300mg vs Celecoxib vs 위약, 무릎·고관절 골관절염 중등도-중증 통증에서 용량별 진통 효과 및 안전성 비교 |
| [NCT00833794](https://clinicaltrials.gov/study/NCT00833794) | Phase 3 | 완료 | 1028 | Tramadol 1일1회(OAD) vs 위약, 골관절염 통증 진통 효과·안전성·임상적 이익 평가 |
| [NCT00832416](https://clinicaltrials.gov/study/NCT00832416) | Phase 3 | 완료 | 565 | Tramadol 1일1회 100/200/300mg vs 위약, 무릎 골관절염 통증 4군 비교 |
| [NCT00950651](https://clinicaltrials.gov/study/NCT00950651) | Phase 3 | 완료 | 431 | Tramadol HCl/Contramid 1일1회 vs Tramadol SR 1일2회, 84일간 효능·안전성 비교 |
| [NCT00852917](https://clinicaltrials.gov/study/NCT00852917) | Phase 3 | 완료 | 552 | Tramadol 1일1회 100/200/300mg vs 위약, 7일 추적 포함 4군 비교 |
| [NCT01019265](https://clinicaltrials.gov/study/NCT01019265) | Phase 4 | 완료 | 170 | 부프레노르핀 경피패취(Norspan) vs 경구 Tramadol, 중등도-중증 골관절염 통증 비교 |
| [NCT00426647](https://clinicaltrials.gov/study/NCT00426647) | Phase 4 | 완료 | 120 | Norspan 패취 vs Tramadol, 고관절·무릎·요추 만성 중등도-중증 통증 동등성 시험 |
| [NCT01063842](https://clinicaltrials.gov/study/NCT01063842) | Phase 4 | 완료 | 250 | **한국** OA 환자 대상 Tramadol/Acetaminophen(Ultracet) titration 내약성 개선 다기관 연구 |
| [NCT03850587](https://clinicaltrials.gov/study/NCT03850587) | Phase 2 | 완료 | 261 | YYC301 vs 활성대조군, 무릎 골관절염 (tramadol 직접 비교 여부는 불명확) |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [31908149](https://pubmed.ncbi.nlm.nih.gov/31908149/) | 2020 | Guideline | Arthritis Care & Research | ACR/Arthritis Foundation 2019 골관절염 관리 가이드라인, tramadol을 조건부 1차 약물치료로 권고 |
| [31132298](https://pubmed.ncbi.nlm.nih.gov/31132298/) | 2019 | Cochrane SR | Cochrane Database Syst Rev | Tramadol의 골관절염 통증·기능 개선 효과 및 이상반응 프로파일 체계적 고찰 |
| [34251756](https://pubmed.ncbi.nlm.nih.gov/34251756/) | 2023 | SR/Network Meta-analysis | Arthritis Care & Research | 무릎·고관절 골관절염에서 Tramadol의 효능·안전성 네트워크 메타분석 |
| [17343302](https://pubmed.ncbi.nlm.nih.gov/17343302/) | 2007 | SR/Meta-analysis | J Rheumatol | Tramadol의 진통효과·기능·지속시간·안전성에 대한 체계적 고찰 |
| [22563589](https://pubmed.ncbi.nlm.nih.gov/22563589/) | 2012 | Guideline | Arthritis Care & Research | ACR 2012 손·고관절·무릎 골관절염 비약물/약물요법 권고안 |
| [30860559](https://pubmed.ncbi.nlm.nih.gov/30860559/) | 2019 | Cohort (안전성) | JAMA | **Tramadol 사용과 골관절염 환자의 전체원인 사망률 증가 연관성** — 중요 안전성 신호 |
| [39420382](https://pubmed.ncbi.nlm.nih.gov/39420382/) | 2024 | SR/Meta-analysis | Adv Rheumatol | Tramadol vs Codeine, 전체원인 사망률·심혈관질환 위험 비교(성향점수매칭 코호트 메타분석) |
| [38103456](https://pubmed.ncbi.nlm.nih.gov/38103456/) | 2024 | SR/Meta-analysis | Int J Orthop Trauma Nurs | Tramadol 사용과 고관절골절 위험의 연관성 체계적 고찰·메타분석 |
| [36414224](https://pubmed.ncbi.nlm.nih.gov/36414224/) | 2023 | Review | Osteoarthritis and Cartilage | 골관절염 약물치료 현황 및 권고사항 종합 리뷰 |
| [30415598](https://pubmed.ncbi.nlm.nih.gov/30415598/) | 2018 | SR (안전성) | J Orthop Surg (Hong Kong) | 고관절·무릎 골관절염 치료법의 안전성(사망률·중대 합병증) 체계적 비교 |

---

## 한국 시판 정보

한국(taiwan_regulatory 데이터 기준) 시판 허가 정보가 없습니다. `market_status`는 "미시판"으로 기록되어 있으며, 등록된 허가증도 0건입니다. 허가 절차 진행 시 별도의 규제 조사가 필요합니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> 다만 문헌 근거에서 확인된 바, JAMA(2019) 코호트 연구는 골관절염 환자의 tramadol 사용과 **전체원인 사망률 증가**의 연관성을 보고했으며, 2024년 메타분석에서는 **고관절골절 위험** 및 **codeine 대비 심혈관질환·사망률 위험**이 추가로 제기되었습니다. 이는 공식 허가사항 데이터는 아니지만 근거 평가 시 반드시 함께 고려해야 할 관찰연구 기반 안전성 신호입니다.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
골관절염에 대한 Tramadol의 효능은 다수의 완료된 Phase 3 RCT와 ACR/AAOS 가이드라인 권고로 뒷받침되어 근거 수준 L1에 해당합니다. 그러나 동일한 근거 기반(JAMA 코호트, 2024년 메타분석)에서 사망률·골절 위험 증가라는 상반된 안전성 신호가 함께 확인되어, 무조건적 진행보다는 안전장치를 동반한 진행이 타당합니다.

**진행하려면 필요한 것:**
- 한국 식약처(MFDS) 허가사항의 경고·금기·상호작용 정보 확보 (DG001, Blocking)
- DrugBank 등에서 상세 작용기전(MOA) 데이터 확보 (DG002, High)
- 사망률·골절 위험 관련 관찰연구의 인과관계 및 교란변수 평가 (S1 안전성 초평가 필수 선행 조건)
- 한국 내 실제 시판/허가 현황 재확인 및 허가 신청 전략 수립
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

