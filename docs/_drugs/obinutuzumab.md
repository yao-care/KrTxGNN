---
layout: default
title: Obinutuzumab
parent: 僅模型預測 (L5)
nav_order: 318
evidence_level: L5
indication_count: 3
---

# Obinutuzumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Obinutuzumab: 만성 림프구성 백혈병(CLL)/여포성 림프종에서 CD20 양성 혈액암 세부 적응증 확장으로

## 한 문장 요약

Obinutuzumab는 제2형 항 CD20 단클론항체로, 해외에서는 만성 림프구성 백혈병(CLL)과 여포성 림프종(Follicular Lymphoma) 치료에 이미 사용되어 온 약물이나 국내에는 아직 허가·시판되지 않았습니다.
TxGNN 모델은 **여포성 림프종**에 대해 99.18%의 예측 점수와 함께 **50건의 임상시험**, **19편의 문헌**으로 뒷받침되는 강한 재확인 근거를 제시하며, 이와 별도로 CLL/SLL의 두 가지 분자 세부 아형(생식중심-전 단계, IGHV 체세포 고빈도돌연변이형)에 대해서도 99.21%의 높은 예측 점수를 보이나 이 두 아형은 현재 실증 자료(임상시험·문헌)가 전혀 확인되지 않은 순수 모델 예측 단계입니다.

> ⚠️ 이 보고서는 3개의 예측 적응증을 포함한 "multi" 형태의 Evidence Pack을 기반으로 작성되었으며, 근거 수준이 서로 크게 다른 예측들을 함께 다룹니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 만성 림프구성 백혈병(CLL), 여포성 림프종(FL) — *해외 승인 이력 (임상시험 기록 내 확인됨), 국내 허가 없음* |
| 예측 신규 적응증 (주요) | 여포성 림프종 (Follicular Lymphoma) — 기존 글로벌 승인 적응증에 대한 재확인 성격 |
| 추가 예측 적응증 | CLL/SLL 분자 세부 아형 2건 (생식중심-전 단계형, IGHV 체세포고빈도돌연변이형) |
| TxGNN 예측 점수 | 여포성 림프종 99.18% / CLL·SLL 세부 아형 2건 각 99.21% |
| 근거 수준 | 여포성 림프종 **L1** / CLL·SLL 세부 아형 2건 **L5** |
| 한국 시판 현황 | 미상시 (시판되지 않음) |
| 허가증 수 | 0건 |
| 권장 결정 | 여포성 림프종: **Proceed with Guardrails** / CLL·SLL 세부 아형 2건: **Hold** |

---

## 이 예측이 타당한 이유는?

DrugBank의 상세 작용기전(MOA) 필드는 현재 Data Gap 상태이나, Evidence Pack 내 임상시험·문헌 데이터에는 기전 관련 정보가 충분히 포함되어 있습니다.

Obinutuzumab는 제2형(Type II), 당쇄공학적으로 개조된 인간화 항 CD20 IgG1 단클론항체입니다. CD20은 B세포 표면에 발현되는 표지자로, Obinutuzumab는 이를 표적으로 하여 항체의존세포독성(ADCC), 항체의존 식세포작용(ADCP), 그리고 직접적인 B세포 사멸을 유도합니다. 실제로 여러 문헌(PMID 28324270, 28276536)에서는 Rituximab(1세대 항 CD20 항체) 대비 Obinutuzumab의 ADCC 및 직접세포사멸 효과가 더 강력하다고 보고하고 있습니다.

여포성 림프종과 만성 림프구성 백혈병/소림프구성 림프종(CLL/SLL)은 모두 CD20 양성 B세포 악성종양이라는 공통 병리기전을 공유합니다. Evidence Pack 내 NCT02877550 시험 요약에는 "Obinutuzumab는 chlorambucil과 병용하여 미치료 CLL 치료에, bendamustine 병용 후 유지요법으로서 FL 치료에 이미 승인되어 있다"는 내용이 명시되어 있어, 여포성 림프종에 대한 예측은 사실상 기존 승인 사실을 재확인하는 성격이 강합니다.

반면 CLL/SLL의 두 분자 세부 아형(생식중심-전 단계형, IGHV 체세포고빈도돌연변이형)은 CD20 발현이라는 기전적 근거는 동일하게 성립하지만, 이는 임상 진단명이 아니라 분자유전학적 세분류 수준의 질병 개체명입니다. 이로 인해 ClinicalTrials.gov·PubMed의 자유 텍스트 검색어와 매칭되지 않아 실증 자료가 전혀 확보되지 못한 것으로 판단됩니다.

---

## 임상시험 근거

*(주요 예측 적응증: 여포성 림프종 기준, 총 50건 중 관련성 상위 10건)*

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01332968](https://clinicaltrials.gov/study/NCT01332968) | Phase 3 | 완료 | 1,401 | GALLIUM 시험 — 미치료 진행성 무통성 비호지킨림프종에서 Obinutuzumab+화학요법이 Rituximab+화학요법 대비 우수한 효과를 보임 |
| [NCT03332017](https://clinicaltrials.gov/study/NCT03332017) | Phase 2 | 완료 | 217 | ROSEWOOD 시험 — 재발/불응성 FL에서 Zanubrutinib+Obinutuzumab vs Obinutuzumab 단독요법 비교 |
| [NCT01059630](https://clinicaltrials.gov/study/NCT01059630) | Phase 3 | 완료 | 413 | GADOLIN 유형 시험 — Rituximab 불응성 무통성 NHL에서 Bendamustine+Obinutuzumab 병용요법 평가 |
| [NCT02611323](https://clinicaltrials.gov/study/NCT02611323) | Phase 1b/2 | 완료 | 133 | 재발/불응성 FL에서 Obinutuzumab+Polatuzumab vedotin+Venetoclax 병용요법 평가 |
| [NCT05899621](https://clinicaltrials.gov/study/NCT05899621) | 실사용 연구 | 모집 중 | 332 | 미치료 FL 환자 대상 Obinutuzumab 기반 요법의 실사용 유효성·안전성 관찰 |
| [NCT03980171](https://clinicaltrials.gov/study/NCT03980171) | Phase 1b/2 | 활성(모집 종료) | 50 | 미치료 FL에서 Lenalidomide+Venetoclax+Obinutuzumab 병용요법 평가 |
| [NCT06961500](https://clinicaltrials.gov/study/NCT06961500) | Phase 2 | 모집 예정 | 133 | 신규 진단 FL(3A등급)에서 Obinutuzumab+CHOP vs Obinutuzumab+Bendamustine 비교 |
| [NCT06549335](https://clinicaltrials.gov/study/NCT06549335) | Phase 2 | 모집 예정 | 66 | 고위험 미치료 FL에서 Zanubrutinib+Obinutuzumab+Lenalidomide(ZGR) 병용요법 평가 |
| [NCT06108232](https://clinicaltrials.gov/study/NCT06108232) | Phase 2 | 모집 중 | 36 | 고종양부담 미치료 FL에서 Obinutuzumab+CC-99282 병용요법 평가 |
| [NCT05100862](https://clinicaltrials.gov/study/NCT05100862) | Phase 3 | 모집 중 | 780 | 재발/불응성 FL·변연부림프종에서 Zanubrutinib+Obinutuzumab vs Lenalidomide+Rituximab 비교 |

> CLL/SLL 분자 세부 아형 2건(생식중심-전 단계형, IGHV 체세포고빈도돌연변이형)에 대해서는 **현재 관련 임상시험 등록이 없습니다.**

---

## 문헌 근거

*(주요 예측 적응증: 여포성 림프종 기준, 총 19편 중 관련성 상위 10편, RCT 우선)*

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [28976863](https://pubmed.ncbi.nlm.nih.gov/28976863/) | 2017 | RCT | New England Journal of Medicine | 미치료 진행성 FL에서 Obinutuzumab 기반 화학요법이 Rituximab 기반 요법보다 우수함을 입증 |
| [29856692](https://pubmed.ncbi.nlm.nih.gov/29856692/) | 2018 | RCT | J Clinical Oncology | GALLIUM 시험 세부분석 — 병용 화학요법 종류에 따른 효능·안전성 영향 분석 |
| [37506346](https://pubmed.ncbi.nlm.nih.gov/37506346/) | 2023 | RCT | J Clinical Oncology | ROSEWOOD 시험 — 재발/불응성 FL에서 Zanubrutinib+Obinutuzumab 병용의 효능·안전성 평가 |
| [37404773](https://pubmed.ncbi.nlm.nih.gov/37404773/) | 2023 | RCT | HemaSphere | GALLIUM 시험 최종 결과 — Obinutuzumab 기반 요법의 장기 무진행생존 개선 확인 |
| [31296423](https://pubmed.ncbi.nlm.nih.gov/31296423/) | 2019 | RCT | Lancet Haematology | GALEN 시험 — 재발/불응성 FL에서 Obinutuzumab+Lenalidomide 병용요법의 활성·안전성 평가 |
| [31360086](https://pubmed.ncbi.nlm.nih.gov/31360086/) | 2017 | Review | Blood and Lymphatic Cancer | Obinutuzumab 단독·병용요법의 FL 치료 임상적 영향 종합 고찰 |
| [38660754](https://pubmed.ncbi.nlm.nih.gov/38660754/) | 2024 | Review | Turkish J Haematology | FL의 병기·예후·치료(신규진단 및 재발/불응성 포함) 최신 종합 고찰 |
| [28276536](https://pubmed.ncbi.nlm.nih.gov/28276536/) | 2016 | Review | Drugs of Today | CD20 표적 항체 개발 동향 중 Obinutuzumab의 위치와 기전적 우위 고찰 |
| [39830356](https://pubmed.ncbi.nlm.nih.gov/39830356/) | 2024 | Review | Frontiers in Pharmacology | 중국 내 FL 환자 대상 Obinutuzumab의 유효성·안전성·비용효과성 신속 고찰 |
| [35180337](https://pubmed.ncbi.nlm.nih.gov/35180337/) | 2022 | Review | Oncology (Williston Park) | FL의 현재 치료 및 신규 개발 중 치료제 동향 고찰 |

> CLL/SLL 분자 세부 아형 2건에 대해서는 **현재 관련 문헌이 없습니다.**

---

## 한국 시판 정보

**현재 국내에 허가된 Obinutuzumab 제품이 없습니다.** (시판 현황: 미상시, 허가증 0건)

---

## 세포독성 (항종양약)

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제/면역치료 — 제2형(Type II) 항 CD20 인간화 단클론항체 (고전적 세포독성 화학요법 아님) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 (Evidence Pack 내 구체적 등급 자료 없음) |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 (단클론항체 특성상 저위험군으로 분류되는 경우가 일반적이나, 본 팩에는 확정 자료 없음) |
| 모니터링 항목 | B세포 수, 면역글로불린 수치, 감염징후 — NCT04918940 시험 요약에 "장기간의 심각한 B림프구감소증, 저감마글로불린혈증 및 감염 위험 증가"가 명시되어 있어 이에 대한 정기 모니터링 필요 |
| 취급 방호 | 세포독성 화학요법 약물은 아니나, 정맥주사형 단클론항체 특성상 주입관련반응(IRR) 모니터링 체계 필요 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (Evidence Pack 내 주요 경고·금기·약물상호작용 자료는 모두 Data Gap이며, DDI 조회 결과도 확인되지 않음)

---

## 결론 및 다음 단계

**결정: 여포성 림프종 — Proceed with Guardrails / CLL·SLL 분자 세부 아형 2건 — Hold**

**사유:**
- 여포성 림프종은 Phase 3 GALLIUM 시험(N=1,401)을 포함한 다수의 완료·진행 중인 임상시험과 19편의 문헌(RCT 5편 포함)으로 뒷받침되며, 사실상 해외에서 이미 확립된 적응증을 재확인하는 성격으로 근거가 충분합니다.
- CLL/SLL의 두 분자 세부 아형은 CD20 표적 기전상 타당성은 있으나, 실증 자료(임상시험·문헌)가 전혀 확인되지 않은 순수 모델 예측(L5) 단계로, 임상적 의사결정에 사용하기에는 근거가 불충분합니다.

**진행하려면 필요한 것:**
- 국내(TFDA/식약처 등) 허가 신청을 위한 상세 작용기전(MOA) 자료 확보
- 허가사항상 경고·금기·약물상호작용 원문 확보 (현재 전 항목 Data Gap)
- CLL/SLL 분자 세부 아형에 대해서는 임상 진단명 수준으로의 매핑 재검토 및 추가 문헌/임상시험 검색 전략 보완 필요
- 여포성 림프종 적응증 확대 추진 시, 국내 환자 대상 실사용 데이터 또는 교량시험(bridging study) 검토 권장
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

