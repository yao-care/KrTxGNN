---
layout: default
title: Lanadelumab
parent: 모델 예측만 (L5)
nav_order: 423
evidence_level: L5
indication_count: 10
---

# Lanadelumab
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

# Lanadelumab: 적응증 데이터 없음에서 C1 억제제 결핍증(유전성 혈관부종)으로

## 한 문장 요약

Lanadelumab(DrugBank ID: DB14597)은 국내에 아직 허가·시판되지 않은 약물로, 원 승인 적응증에 대한 허가증 데이터가 확보되지 않았습니다. TxGNN 모델은 **C1 억제제 결핍증(C1 Inhibitor Deficiency, 유전성 혈관부종·HAE)**에 효과가 있을 것으로 예측하며, 현재 **22건의 임상시험**과 **20편의 문헌**이 이 방향을 강하게 지지합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (국내 허가증 미확보) |
| 예측 신규 적응증 | C1 억제제 결핍증 (C1 Inhibitor Deficiency / 유전성 혈관부종) |
| TxGNN 예측 점수 | 99.996% (예측 순위 240위) |
| 근거 수준 | L2 (완료된 3상 RCT 1건 확인) |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

Lanadelumab 자체의 작용기전(MOA) 필드는 데이터 공백 상태이지만, 확보된 문헌 근거에서 기전 정보를 확인할 수 있습니다. 문헌(PMID 30267321)에 따르면 Lanadelumab은 혈장 칼리크레인(plasma kallikrein)을 억제하는 완전 인간화 단일클론항체입니다.

C1 억제제 결핍증(HAE)의 병태생리는 SERPING1 유전자 변이로 인한 C1-INH(=C1 억제제) 기능 저하 또는 결핍이며, 이로 인해 혈장 칼리크레인 활성이 조절되지 못하고 과도한 브래디키닌 생성으로 혈관부종이 발생합니다(PMID 30539362). 즉, Lanadelumab의 칼리크레인 억제 기전은 HAE의 핵심 병리 경로를 직접 표적으로 하므로, TxGNN의 예측은 이미 알려진 약리 기전과 정확히 부합합니다.

실제로 임상시험 데이터를 보면 이 예측은 순수한 신규 가설이라기보다, 이미 다수 국가(일본, 중국, 미국, 유럽 등)에서 승인·사용 중인 적응증으로 보이며 근거 축적이 매우 두텁습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02586805](https://clinicaltrials.gov/study/NCT02586805) | Phase 3 | 완료 | 125 | HELP Study: 위약대조 이중맹검 RCT, HAE 장기예방 효과·안전성을 입증한 피벗 연구 |
| [NCT02741596](https://clinicaltrials.gov/study/NCT02741596) | Phase 3 | 완료 | 212 | HELP Study Extension: 공개표지 장기 안전성·유효성 추적 |
| [NCT04070326](https://clinicaltrials.gov/study/NCT04070326) | Phase 3 | 완료 | 21 | SPRING: 2~12세 소아 대상 약동학·안전성·발작예방 효과 평가 |
| [NCT04180163](https://clinicaltrials.gov/study/NCT04180163) | Phase 3 | 완료 | 12 | 일본인 HAE(I/II형) 환자 대상 공개표지 유효성·안전성 평가 |
| [NCT04444895](https://clinicaltrials.gov/study/NCT04444895) | Phase 3 | 완료 | 73 | 정상 C1-INH 비히스타민성 혈관부종 환자 장기 안전성·유효성 평가 |
| [NCT05460325](https://clinicaltrials.gov/study/NCT05460325) | Phase 3 | 완료 | 20 | 중국인 HAE 환자 대상 26주 투여 안전성 평가 |
| [NCT04130191](https://clinicaltrials.gov/study/NCT04130191) | N/A | 완료 | 140 | ENABLE: 최대 3년 전향적 관찰연구, 실제임상에서 발작률 감소 확인 |
| [NCT03845400](https://clinicaltrials.gov/study/NCT03845400) | N/A | 완료 | 168 | EMPOWER: 미국·캐나다 관찰연구, 치료 전후 HAE 발작률 비교 |
| [NCT02093923](https://clinicaltrials.gov/study/NCT02093923) | Phase 1 | 완료 | 38 | 다회투여 상승용량 연구, HAE 환자 대상 안전성·내약성·PK 평가 |
| [NCT01923207](https://clinicaltrials.gov/study/NCT01923207) | Phase 1 | 완료 | 32 | 단회투여 상승용량 연구, 건강 성인 대상 최초 인체 안전성 평가 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [30480729](https://pubmed.ncbi.nlm.nih.gov/30480729/) | 2018 | RCT | JAMA | 위약 대비 Lanadelumab 투여군에서 HAE 발작 빈도 유의하게 감소 (HELP Study 본 논문) |
| [34287942](https://pubmed.ncbi.nlm.nih.gov/34287942/) | 2022 | 추적연구(RCT 연장) | Allergy | HELP OLE: 12세 이상에서 장기 안전성·유효성 확인 |
| [39508959](https://pubmed.ncbi.nlm.nih.gov/39508959/) | 2024 | 체계적 문헌고찰 | Clin Rev Allergy Immunol | 장기예방요법(LTP) 중 발생하는 HAE 발작 특성 분석 |
| [30539362](https://pubmed.ncbi.nlm.nih.gov/30539362/) | 2019 | Review | BioDrugs | 전임상·1상 자료 종합, 칼리크레인 억제 기전과 초기 안전성 정리 |
| [32187470](https://pubmed.ncbi.nlm.nih.gov/32187470/) | 2020 | Review | NEJM | 유전성 혈관부종(HAE) 전반에 대한 임상 개관 |
| [30267321](https://pubmed.ncbi.nlm.nih.gov/30267321/) | 2018 | Review | Drugs | Lanadelumab 최초 글로벌 승인 리뷰, 작용기전 및 개발 경과 요약 |
| [35079346](https://pubmed.ncbi.nlm.nih.gov/35079346/) | 2022 | Review | Clin Transl Allergy | C1 억제제 장기예방요법에 대한 임상 고려사항·가이드라인 리뷰 |
| [37898409](https://pubmed.ncbi.nlm.nih.gov/37898409/) | 2024 | Review | J Allergy Clin Immunol | 아시아태평양 지역 C1-INH 결핍 HAE 질병부담 리뷰 |
| [39701274](https://pubmed.ncbi.nlm.nih.gov/39701274/) | 2025 | 관찰연구 | JACI In Practice | 다국가 실제임상 관찰연구(INTEGRATED), 실사용 효과 평가 |
| [31721602](https://pubmed.ncbi.nlm.nih.gov/31721602/) | 2019 | Review | Expert Rev Clin Immunol | Lanadelumab의 HAE 발작예방 기전 및 임상적 활용 전문가 리뷰 |

## 한국 시판 정보

현재 국내 미출시 상태이며, 확보된 허가증은 0건입니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (주요 경고, 금기, 약물상호작용 데이터 모두 미확보 상태이며, 약물상호작용 조회 결과도 없음)

## 결론 및 다음 단계

**결정: Hold**

**사유:**
칼리크레인 억제 기전과 HAE 병태생리 간 연관성이 명확하고, 완료된 3상 RCT(HELP Study)를 포함해 다수의 임상시험·실제임상 데이터로 뒷받침되는 강한 근거(L2)를 보유하고 있습니다. 다만 국내 허가증·안전성 라벨(TFDA 등)이 전혀 확보되지 않아 S1 안전성 초평가 단계로 진입할 수 없는 **차단(Blocking) 등급 데이터 공백**이 존재합니다.

**진행하려면 필요한 것:**
- 국내(또는 참조국) 허가사항/仿單 확보 및 경고·금기사항 파싱
- DrugBank API를 통한 상세 작용기전(MOA) 데이터 확보
- 국내 시판·수입 경로 및 허가 신청 현황 확인
- 약물상호작용(DDI) 데이터베이스 재조회
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

