---
layout: default
title: Chlorprothixene
parent: 僅模型預測 (L5)
nav_order: 196
evidence_level: L5
indication_count: 10
---

# Chlorprothixene
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

# Chlorprothixene: 항정신병제에서 조증 양극성 정동장애로

## 한 문장 요약

Chlorprothixene(DrugBank DB01239)은 1959년 출시된 최초의 thioxanthene계 항정신병제로, 문헌상 정신병 및 조현병 치료에 사용되어 왔습니다(한국 허가 정보는 없음). TxGNN 모델이 예측한 상위 후보들 중 다수는 문헌·임상 근거가 전혀 없는 지식그래프 아티팩트로 판단되었으나, 순위 10위의 **조증 양극성 정동장애(Manic Bipolar Affective Disorder)**는 D2/D1 길항 기전과 유럽 임상 실무에서 수십 년간 축적된 사용 경험이 뒷받침하는 유일하게 실질적인 후보입니다. 현재 관련 **임상시험은 없으나 20편의 문헌**(코호트 연구 포함)이 이 방향을 지지합니다.

> ⚠️ TxGNN 예측 순위 1위인 "망막 이영양증"은 evidence pack 자체 평가에서 지식그래프 노드 공기(co-occurrence)로 인한 **허위 양성(false positive)**으로 판정되었기에(근거: 관련 문헌 15편 모두 본 약물을 언급하지 않는 독립적 안과 질환 사례보고), 본 보고서는 실질적 근거가 있는 조증 양극성 정동장애를 중심으로 작성했습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (한국 미시판, 원 적응증 데이터 미기재). 문헌상 thioxanthene계 항정신병제로 사용된 기록 있음(PMID 7367466) |
| 예측 신규 적응증 | 조증 양극성 정동장애 (Manic Bipolar Affective Disorder) |
| TxGNN 예측 점수 | 99.96% (모델 내 순위 1351위) |
| 근거 수준 | L3 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

현재 DrugBank 등에서 확인되는 상세 작용기전(MOA) 데이터는 없습니다([Data Gap], DG002). 다만 evidence pack에 포함된 기전 분석에 따르면, Chlorprothixene은 **D2/D1 도파민 수용체 길항제**이며 진정(sedative) 작용이 강한 것이 특징입니다. 이는 조증 삽화 치료에 쓰이는 전형적 항정신병제의 약리 기전과 일치합니다.

문헌 근거도 이를 뒷받침합니다. 1963년 발표된 비교 코호트 연구(PMID 14085189)는 이미 "조증 환자에서의 Chlorprothixene(Truxal) 치료"를 직접 다루고 있으며, 20년간의 사용 경험을 정리한 리뷰(PMID 7367466)는 542편의 임상 문헌·7,109명의 환자 데이터를 분석했습니다. 즉 이는 완전히 새로운 가설이라기보다, **유럽 임상 실무에서 이미 수십 년간 축적되어 온 사용 경험을 TxGNN이 재발견한 사례**에 가깝습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [35763976](https://pubmed.ncbi.nlm.nih.gov/35763976/) | 2022 | Cohort | Eur Neuropsychopharmacol | 핀란드 전국 코호트(리튬 중단 양극성장애 환자 4,052명)에서 기분안정제·항정신병제의 재입원 예방 효과 비교 |
| [14085189](https://pubmed.ncbi.nlm.nih.gov/14085189/) | 1963 | Cohort/Comparative | Acta Psychiatr Scand | 조증 환자에서 Chlorprothixene(Truxal) 치료와 타 치료법의 안정화 기간 비교 |
| [25907249](https://pubmed.ncbi.nlm.nih.gov/25907249/) | 2015 | Cohort | Eur Neuropsychopharmacol | 경계성 인격장애 입원환자 2,195명 대상 정신약물 처방 패턴 분석 |
| [27249081](https://pubmed.ncbi.nlm.nih.gov/27249081/) | 2016 | Cohort | J Clin Psychiatry | 대만 12년 건강보험 자료 기반, 조현병·기분장애 환자에서 1·2세대 항정신병제의 발작 위험 비교 |
| [7367466](https://pubmed.ncbi.nlm.nih.gov/7367466/) | 1980 | Review/Case series | Pharmakopsychiatrie | Chlorprothixene 도입 20년 문헌 801편(임상 542편) 리뷰, 환자 7,109명 분석 |
| [4471029](https://pubmed.ncbi.nlm.nih.gov/4471029/) | 1974 | Review | Acta Psychiatr Belg | Chlorprothixene와 clopentixol의 임상적 특성 개관 |
| [13719775](https://pubmed.ncbi.nlm.nih.gov/13719775/) | 1961 | Case series | Am J Psychiatry | 정신병성 우울증에서 Chlorprothixine(Taractan)과 isocarboxazid(Marplan) 병용 치료 |
| [14078687](https://pubmed.ncbi.nlm.nih.gov/14078687/) | 1963 | Case series | Acta Psychiatr Scand | Chlorprothixene 저항성 환자에서 haloperidol(Serenase) 사용례 |
| [13962407](https://pubmed.ncbi.nlm.nih.gov/13962407/) | 1963 | Case series | Applied Therapeutics | 정신과 증후군 전반에서 Chlorprothixene의 임상 경험 |
| [4890081](https://pubmed.ncbi.nlm.nih.gov/4890081/) | 1968 | Review | Prog Neurol Psychiatry | 정신과 약물치료 전반 개관 |

---

## 한국 시판 정보

현재 한국에서 허가된 제품이 없으며 시판되지 않습니다 (허가증 0건).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (주요 경고·금기·DDI 데이터 모두 미확보 — DG001, Blocking)

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
조증 양극성 정동장애 예측은 명확한 약리 기전(D2/D1 길항)과 수십 년간의 유럽 임상 사용 경험, 코호트 연구를 포함한 L3 수준 근거로 뒷받침됩니다. 다만 TxGNN 상위 예측 대다수(순위 1~9위)는 문헌 근거가 없거나 허위 양성으로 판정되어 이번 evidence pack 전체의 신뢰도는 낮으며, 한국 내 허가·안전성 정보 부재라는 **Blocking 등급 데이터 갭(DG001)**으로 인해 S1 안전성 초기평가 단계에 아직 진입할 수 없는 상태입니다.

**진행하려면 필요한 것:**
- 한국(또는 원산지) 규제기관의 허가사항·경고·금기 정보 확보 (DG001, Blocking — S1 안전성평가 필수 선행조건)
- DrugBank/1차 문헌을 통한 상세 작용기전(MOA) 데이터 보강 (DG002)
- 조증/양극성장애 대상 전향적 임상시험 또는 최신 체계적 문헌고찰 확인 (현재 관련 임상시험 등록 없음)
- 한국 내 시판 여부 및 규제 경로 검토 (현재 허가증 0건)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

