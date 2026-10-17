---
layout: default
title: Clotrimazole
parent: 모델 예측만 (L5)
nav_order: 230
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Clotrimazole: 예측 신규 적응증 여드름 (Acne) (근거 수준 L5). 기존 적응증: 피부사상균, 효모 곰팡이, 기타 진균에 의한 피부진균증(백선, 어루러기, 피부칸디다증, 칸디다성 외음염 및 칸디다성 귀두염)…"
monitor_inn: "CLOTRIMAZOLE"
predicted_indications: ["acne (disease)"]
---

# Clotrimazole
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **3** 건
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

# Clotrimazole: 피부·질 진균증에서 급성 여드름(Acne)으로

## 한 문장 요약

Clotrimazole은 아졸계 항진균제로, 원래 피부진균증(백선, 어루러기, 피부칸디다증)과 칸디다성 질염 치료에 사용되었습니다.
TxGNN 모델은 상위 예측 질환으로 **여드름(Acne)**을 제시하며(예측 점수 99.86%), 이를 직접 뒷받침하는 근거는 **1건의 임상시험**(3제 복합제, 중단 상태)뿐이고 문헌은 없습니다.
참고로 2순위 예측인 외음질염(vulvovaginitis)은 이미 허가된 적응증이며 임상시험 12건과 문헌 20편이 있어, 새로운 재창출이라기보다 모델 예측의 타당성을 확인해 주는 사례입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 피부사상균, 효모 곰팡이, 기타 진균에 의한 피부진균증(백선, 어루러기, 피부칸디다증, 칸디다성 외음염 및 칸디다성 귀두염), 중복감염된 피부질환, 코리네박테륨에 의한 홍색음선 |
| 예측 신규 적응증 | 여드름 (Acne) |
| TxGNN 예측 점수 | 99.86% |
| 근거 수준 | L4 (여드름 기준, 직접 근거 매우 제한적) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 |
| 권장 결정 | Hold (여드름) |

> 참고: 2순위 예측인 외음질염(점수 99.59%)은 근거 수준 L1, 권장 결정 Proceed with Guardrails이나 기허가 적응증입니다. 3순위 위축성 질염(점수 99.46%)은 근거 수준 L5, Hold입니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Clotrimazole은 아졸계 항진균제로, 진균의 CYP51(lanosterol 14-alpha-demethylase)을 억제해 에르고스테롤 합성을 막고 진균 세포막을 손상시킵니다. 이는 칸디다 감염에 대한 효능을 설명합니다.

여드름과의 연관성은 간접적입니다. Malassezia나 *Cutibacterium acnes*에 대한 작용, 국소 염증 완화 가능성이 거론되지만, 여드름에서의 직접적인 기전 근거나 임상 근거는 없습니다. 높은 TxGNN 점수는 계산상 예측일 뿐입니다.

외음질염 예측은 칸디다성 질염이라는 기허가 적응증과 일치합니다. 비칸디다성 외음질염(세균성 질증, 트리코모나스증 등)에는 효과를 기대하기 어렵습니다. 위축성 질염은 에스트로겐 결핍이 주원인이어서 기전상 뚜렷한 연관이 없으며, 이차 칸디다 감염 시 증상 완화에 그칠 수 있습니다.

## 임상시험 근거

**여드름 (1순위 예측)**

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | 중단(Suspended) | 80 | Beclomethasone + Gentamicin + Clotrimazole 3제 복합 크림의 오염 피부염 대상 비교 효능 평가. 결과 없음, 스테roid·항생제 성분이 교란 요인 |

**외음질염 (2순위 예측, 기허가 적응증) — 주요 시험**

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00755053](https://clinicaltrials.gov/study/NCT00755053) | Phase 3 | 완료 | 466 | 질 칸디다증에서 Clotrimazole 질삽입제(ovule) 500 mg vs 질정 500 mg 비열등성 평가 |
| [NCT00313131](https://clinicaltrials.gov/study/NCT00313131) | Phase 3 | 완료 | 1524 | 서아프리카 질 분비물 여성에서 단회 tinidazole+fluconazole vs 장기 metronidazole+clotrimazole |
| [NCT06835361](https://clinicaltrials.gov/study/NCT06835361) | Phase 2/3 | 모집 중 | 264 | Clotrimazole+Lactulose 복합제 vs Clotrimazole 단일제 (칸디다성 질염) |
| [NCT03115073](https://clinicaltrials.gov/study/NCT03115073) | Phase 2/3 | 완료 | 84 | ProF-001(Candiplus®) 용량 반응 평가, 1% clotrimazole 질 크림 대조 |
| [NCT02242695](https://clinicaltrials.gov/study/NCT02242695) | Phase 4 | 완료 | 150 | Dequalinium chloride vs clotrimazole 100 mg 질정 비교 |
| [NCT02180828](https://clinicaltrials.gov/study/NCT02180828) | Phase 4 | 완료 | 240 | 중증 외음질 칸디다증에서 clotrimazole 질정 vs fluconazole |
| [NCT04699240](https://clinicaltrials.gov/study/NCT04699240) | Phase 4 | 완료 | 140 | 재발성 외음질 칸디다증에서 clotrimazole 질정에 Lactobacillus 병용 |
| [NCT03599323](https://clinicaltrials.gov/study/NCT03599323) | 해당 없음 | 완료 | 1033 | Empecid L 크림(clotrimazole 1%) 시판 후 안전성 조사 |
| [NCT03005353](https://clinicaltrials.gov/study/NCT03005353) | Phase 2/3 | 완료 | 100 | 쿠민 씨앗 추출물 질좌제 시험 (clotrimazole은 대조로 추정) |
| [NCT03024502](https://clinicaltrials.gov/study/NCT03024502) | Phase 1/2 | 불명 | 90 | 프로폴리스(EPP-AF) 점막부착 젤 vs clotrimazole 크림 |

**위축성 질염 (3순위 예측):** 현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

**여드름:** 현재 관련 문헌이 없습니다.

**외음질염 (2순위 예측) — 주요 문헌**

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [3895960](https://pubmed.ncbi.nlm.nih.gov/3895960/) | 1985 | RCT | Am J Obstet Gynecol | 칸디다성 외음질염에서 clotrimazole 500 mg 단회 vs 100 mg 6일 투여 효능·내약성 비교 (199명) |
| [30565745](https://pubmed.ncbi.nlm.nih.gov/30565745/) | 2019 | RCT | Mycoses | 재발성 외음질 칸디다증에서 프로바이오틱스·락토페린 유지요법 |
| [40855225](https://pubmed.ncbi.nlm.nih.gov/40855225/) | 2025 | RCT | AAPS PharmSciTech | Voriconazole 탑재 spanlastics의 외음질 칸디다증 임상 평가 |
| [2644595](https://pubmed.ncbi.nlm.nih.gov/2644595/) | 1989 | 이중맹검 무작위 연구 | Obstet Gynecol | 재발성 칸디다 질염에서 clotrimazole 500 mg 질좌제 주 1회 2주 투여 시 42명 중 38명(90.4%) 임상 관해 |
| [32992877](https://pubmed.ncbi.nlm.nih.gov/32992877/) | 2020 | 체계적 문헌고찰 | Pharmaceuticals | 외음질 칸디다증에서 clotrimazole 45년 이상의 임상 경험 요약 |
| [24863842](https://pubmed.ncbi.nlm.nih.gov/24863842/) | 2014 | Review | J Appl Microbiol | Clotrimazole의 과거·현재·미래: 항진균 작용과 약제로서의 활용 |
| [41350226](https://pubmed.ncbi.nlm.nih.gov/41350226/) | 2025 | Cohort | Pharmacoepidemiol Drug Saf | 임신 첫 3개월 국소 항진균제 노출과 주요 선천 기형 위험 (일본 청구 데이터) |
| [39432168](https://pubmed.ncbi.nlm.nih.gov/39432168/) | 2024 | 후향 분석 | Mycopathologia | 중증 외음질 칸디다증 1,303예에서 clotrimazole·fluconazole 요법 비교, 3회 투여가 효능 향상 |
| [40886781](https://pubmed.ncbi.nlm.nih.gov/40886781/) | 2025 | 전임상/in vitro | Pharmacol Res | 아졸계 항진균제가 사람 태반 모델의 스테로이드 생성에 영향 |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Review | J Womens Health | 재발성 외음질 칸디다증에 대한 붕산 요법의 임상 근거 |

**위축성 질염:** 현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 198400401 | 카마졸크림 | 백색 크림제 | 피부사상균, 효모 곰팡이, 기타 진균에 의한 피부진균증(백선, 어루러기, 피부칸디다증, 칸디다성 외음염 및 칸디다성 귀두염), 상기 진균류에 중복감염된 피... |
| 201508135 | 로마졸질정100mg | 질정제 | 칸디다성 질염 |
| 200008589 | 카네스텐1질정 | 질정 | 칸디다성 질염 |
| 199906850 | 카네스텐크림 | 크림 | 피부사상균, 효모 곰팡이, 기타 진균에 의한 피부진균증(백선, 어루러기, 피부칸디다증, 칸디다성 외음염 및 칸디다성 귀두염), 상기 진균류에 중복감염된 피... |
| 201506002 | 카네덤플러스크림 | 크림제 | 염증, 가려움 및 습진 등의 임상증상을 수반하는 피부 진균증(백선, 피부 칸디다증, 어루러기) |

## 안전성 고려사항

- **지식그래프 기반 금기 관련 질환** (허가사항 문구가 아닌 모델 지식그래프 기준): 부신피질 기능저하증, 애디슨병, 피부 위축, 모세혈관 확장증, 모세혈관 질환, 유전성 출혈성 모세혈관확장증, 말초혈관질환, 간헐적 파행, 말초동맥질환
- **약물 상호작용**: 총 100건 보고. 주요(Major) 상호작용으로 Fentanyl, Alfentanil, Hydrocodone, Amiodarone이 확인됩니다. 중등도(Moderate)로는 Paclitaxel, Abemaciclib, Acalabrutinib, Nifedipine, Amlodipine, Apixaban, Alprazolam, Aprepitant, Estradiol, Levonorgestrel, Norethisterone 등이 있습니다. 국소·질내 투여 시 전신 흡수는 낮지만 병용약 확인이 필요합니다.
- **임신 관련**: 임신 첫 3개월 국소 아졸 노출의 선천 기형 위험, 아졸계의 태반 스테로이드 생성 영향이 문헌에서 검토 대상으로 제기되었습니다.

허가사항의 경고 및 금기 문구는 이번 데이터에 포함되지 않았으므로 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Hold (여드름)**

**사유:**
여드름 예측은 TxGNN 점수가 높지만 직접적인 기전·임상 근거가 없습니다. 유일한 시험은 스테로이드·항생제가 포함된 3제 복합제 대상이며 중단 상태로 결과가 없어 clotrimazole 고유의 효과를 판단할 수 없습니다. 외음질염은 기허가 적응증으로 근거가 충분하여(근거 수준 L1) Proceed with Guardrails이나 신규 재창출은 아닙니다. 위축성 질염은 근거가 없어 Hold입니다.

**진행하려면 필요한 것:**
- 여드름에 대한 clotrimazole 단독 효과를 평가하는 전임상 또는 소규모 탐색 임상시험
- 작용 기전(MOA) 데이터 확보 및 여드름 병태와의 연결 분석
- 허가사항의 경고·금기 정보 확보 후 안전성 검토
- 외음질염 관련: 비칸디다성 질염 제외, 임신 중 사용 안전성, 병용약 상호작용 관리 지침 마련
- 여드름 적응증의 경우 국소 제형 적합성 확인(현재 경로 호환성 평가 미완료)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

