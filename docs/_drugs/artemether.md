---
layout: default
title: Artemether
parent: 모델 예측만 (L5)
nav_order: 90
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Artemether: 예측 신규 적응증 후천성 혈관부종 (Acquired Angioedema) (근거 수준 L5). 기존 적응증: 말라리아 (허가 문구는 허가사항 원문 참조)"
monitor_inn: "ARTEMETHER"
predicted_indications: ["acquired angioedema", "Plasmodium falciparum malaria", "malaria", "angioedema", "hereditary angioedema", "nephrogenic syndrome of inappropriate antidiuresis", "acute contagious conjunctivitis", "scleroderma (disease)", "conjunctivitis", "renin-angiotensin-aldosterone system-blocker-induced angioedema"]
---

# Artemether
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

# Artemether: 말라리아에서 후천성 혈관부종으로

## 한 문장 요약

Artemether는 아르테미시닌 계열 약물로, 원래 말라리아 치료에 사용되며 한국에서는 수출용 정제로 허가되어 있습니다.
TxGNN 모델은 최상위 예측으로 **후천성 혈관부종(Acquired Angioedema)**을 제시했지만, 이 예측을 뒷받침하는 임상시험과 문헌은 **0건**입니다.
반면 2~3순위인 열대열 말라리아(*P. falciparum*)와 말라리아는 기존 적응증과 같은 질환이므로 신규 재창출이 아니며, 각각 **30건의 임상시험**과 **20편의 문헌**이 뒷받침합니다.

> **참고:** 한국 허가 적응증은 외부 링크로만 제공되어 구체적인 문구를 확인하지 못했습니다. 이 보고서의 "기존 적응증: 말라리아"는 약물 분류와 예측 결과에서 추정한 값입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 말라리아 (허가 문구는 허가사항 원문 참조) |
| 예측 신규 적응증 | 후천성 혈관부종 (Acquired Angioedema) |
| TxGNN 예측 점수 | 99.90% |
| 근거 수준 | L5 (후천성 혈관부종 기준) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Hold (후천성 혈관부종 기준) |

**다른 예측 결과 요약**

| 순위 | 예측 질환 | 점수 | 근거 수준 | 권장 결정 |
|-----|---------|------|---------|---------|
| 2 | 열대열 말라리아 | 99.77% | L1 | Proceed with Guardrails (기존 적응증) |
| 3 | 말라리아 | 99.63% | L1 | Proceed with Guardrails (기존 적응증) |
| 4~10 | 혈관부종, 유전성 혈관부종, 신인성 항이뇨 부적절 증후군, 급성 전염성 결막염, 경피증, 결막염, RAAS 차단제 유발 혈관부종 | 99.24~99.56% | L5 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 없습니다. 다만 Artemether는 아르테미시닌 유도체로, 기생충에 감염된 적혈구 안에서 헴 철(heme iron)이 endoperoxide 결합을 활성화해 자유라디칼을 만들고 기생충 단백질을 손상시키는 것으로 알려져 있습니다. 이 기전은 말라리아 치료에 직접 연결됩니다.

최상위 예측인 후천성 혈관부종은 브래디키닌 또는 보체 경로와 관련된 질환입니다. Artemether가 이 경로를 표적으로 한다는 근거는 현재 없어 기전상 연결고리가 확립되지 않았습니다. 99.9%라는 높은 점수는 지식 그래프 기반의 네트워크 예측일 뿐, 임상적 지지가 없습니다. 유전성 혈관부종, RAAS 차단제 유발 혈관부종 등 다른 혈관부종 계열도 같은 한계가 있습니다.

경피증은 아르테미시닌 유도체의 전임상 항섬유화·면역조절 보고가 다른 맥락에서 있으나, 이번 데이터에서 Artemether와 경피증을 잇는 근거는 확인되지 않았습니다.

## 임상시험 근거

### 후천성 혈관부종 (1순위 예측)

현재 관련 임상시험 등록이 없습니다.

### 열대열 말라리아 및 말라리아 (기존 적응증, 참고용)

다음은 기존 적응증인 말라리아에 대한 대표 시험이며, 대부분 Artemether-lumefantrine 복합제 시험입니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00422084](https://clinicaltrials.gov/study/NCT00422084) | Phase 3 | 완료 | 1272 | 합병증 없는 열대열 말라리아에서 pyronaridine-artesunate와 Coartem(artemether-lumefantrine)을 이중맹검으로 비교 |
| [NCT00852423](https://clinicaltrials.gov/study/NCT00852423) | Phase 3 | 완료 | 3428 | 아프리카 임신부 말라리아에서 아르테미시닌 병용요법의 안전성·유효성 평가 |
| [NCT01082705](https://clinicaltrials.gov/study/NCT01082705) | Phase 3 | 완료 | 323 | 탄자니아 소아(6~59개월)에서 아르테미시닌 병용요법의 효능 평가 |
| [NCT00677833](https://clinicaltrials.gov/study/NCT00677833) | Phase 2/3 | 완료 | 361 | 아프리카 소아에서 azithromycin+chloroquine과 artemether-lumefantrine을 비교 |
| [NCT02637128](https://clinicaltrials.gov/study/NCT02637128) | Phase 4 | 완료 | 452 | 말라위에서 artemether-lumefantrine과 artesunate-amodiaquine의 생체 내 효능 평가 |
| [NCT01017770](https://clinicaltrials.gov/study/NCT01017770) | Phase 4 | 완료 | 340 | 부르키나파소에서 artemether-lumefantrine과 artesunate-amodiaquine을 무작위 비교 |
| [NCT00529867](https://clinicaltrials.gov/study/NCT00529867) | Phase 4 | 완료 | 267 | 케냐 소아에서 현탁액과 정제 제형의 효능 비교 |
| [NCT03453840](https://clinicaltrials.gov/study/NCT03453840) | Phase 4 | 완료 | 305 | HIV 감염 소아에서 연장 투여 요법의 약동·약력학 평가 |
| [NCT01103830](https://clinicaltrials.gov/study/NCT01103830) | Phase 1 | 완료 | 287 | Eurartesim과 Riamet(artemether-lumefantrine)의 QT/QTc 간격 영향 비교(심장 안전성) |
| [NCT05951595](https://clinicaltrials.gov/study/NCT05951595) | Phase 3 | 모집 중 | 1680 | 3제 병용요법(artemether-lumefantrine-amodiaquine)의 비열등성 평가 |

## 문헌 근거

### 후천성 혈관부종 (1순위 예측)

현재 관련 문헌이 없습니다.

### 말라리아 (기존 적응증, 참고용)

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [31210357](https://pubmed.ncbi.nlm.nih.gov/31210357/) | 2019 | Review (Cochrane) | Cochrane Database Syst Rev | 중증 말라리아에서 근주 artemether를 quinine 및 artesunate와 비교 |
| [25209020](https://pubmed.ncbi.nlm.nih.gov/25209020/) | 2014 | Review (Cochrane) | Cochrane Database Syst Rev | 중증 말라리아에서 근주 artemether의 효과 평가 |
| [22548983](https://pubmed.ncbi.nlm.nih.gov/22548983/) | 2012 | Review | Malaria Journal | 임신 중 artemether-lumefantrine의 안전성과 효능에 대한 체계적 문헌고찰 |
| [34983552](https://pubmed.ncbi.nlm.nih.gov/34983552/) | 2022 | Review | Malaria Journal | 아프리카 소아에서 DHA-piperaquine과 artemether-lumefantrine의 안전성을 비교한 메타분석 |
| [35271592](https://pubmed.ncbi.nlm.nih.gov/35271592/) | 2022 | 메타분석 | PloS One | 사하라 이남 아프리카에서 ACT 치료 효능 요약 |
| [22049029](https://pubmed.ncbi.nlm.nih.gov/22049029/) | 2011 | 통합분석 | Am J Trop Med Hyg | 7개 시험(성인 647명, 소아 1,332명)을 통합한 artemether-lumefantrine의 효능·안전성 분석 |
| [40138574](https://pubmed.ncbi.nlm.nih.gov/40138574/) | 2025 | Cohort | J Infect Dis | Artemether-lumefantrine 치료가 pfmdr1 복제 수 증가 균주를 선택함 |
| [40845863](https://pubmed.ncbi.nlm.nih.gov/40845863/) | 2026 | RCT (Phase 4) | Lancet Infect Dis | 우간다 소아에서 4종 ACT의 효능 비교 |
| [10496300](https://pubmed.ncbi.nlm.nih.gov/10496300/) | 1999 | Review | Clin Pharmacokinet | Artemether-lumefantrine의 약동·약력학 정리 |
| [11463111](https://pubmed.ncbi.nlm.nih.gov/11463111/) | 2001 | 임상시험 | Am J Trop Med Hyg | 태국에서 6회 투여 요법의 임상 효능과 약동학 평가 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202401012 | 루마트-이정(수출용) | 황색의 원형정제 | 허가사항 원문 참조 (외부 문서 링크로만 제공됨) |
| 202401013 | 루마트정(수출용) | 황색의 장방형정제 | 허가사항 원문 참조 (외부 문서 링크로만 제공됨) |

두 제품 모두 초당약품공업(주)의 단일 성분 제품이며 유효 상태입니다. 수출용 허가이므로 국내 처방 목적의 제품인지는 별도 확인이 필요합니다.

## 안전성 고려사항

- **금기(지식 그래프 기반)**: 허가 문서가 아니라 TxGNN 지식 그래프에서 도출한 항목으로, QT 연장 증후군(long QT syndrome), 가족성 QT 연장 증후군, 토르사드 드 푸앙(torsades de pointes), 칼륨 결핍증이 있습니다. 허가사항 확인이 필요합니다.
- **약물 상호작용**: 총 95건이 확인되었습니다. 이 중 주요(Major) 상호작용은 다음과 같습니다.
  - Clarithromycin
  - Cobicistat
  - Amprenavir
  - Apalutamide
  - Atazanavir
  - Boceprevir
- **중등도(Moderate) 상호작용 예**: Dexamethasone, Miconazole, Troglitazone, Deferasirox, Bosentan, Armodafinil 등이 있습니다. 상당수가 CYP3A4 관련 상호작용으로 보입니다.
- **QT 관련 주의**: 병용 제제의 QT/QTc 영향을 평가한 Phase 1 시험(NCT01103830)이 있어 심장 안전성 확인이 필요합니다.
- 허가사항상의 경고·금기 정보는 확보되지 않았으므로 허가사항 원문을 참조하세요.

## 결론 및 다음 단계

**결정: Hold** (후천성 혈관부종 등 비말라리아 신규 적응증 기준)

**사유:**
1순위 예측인 후천성 혈관부종은 TxGNN 점수가 99.9%로 높지만 임상시험과 문헌이 모두 없고 기전상 연결고리도 확립되지 않아 L5 수준에 머뭅니다. 4~10순위 예측도 모두 같은 상황입니다. 말라리아(2~3순위)는 L1 근거가 있으나 기존 적응증이므로 재창출이 아닙니다. 이 경우 내성 감시와 QT·약물 상호작용 관리를 전제로 한 Proceed with Guardrails가 적절합니다.

**진행하려면 필요한 것:**
- 허가사항 원문(경고, 금기, 적응증)을 내려받아 확보
- DrugBank에서 작용 기전(MOA) 데이터를 확보
- 혈관부종 계열 질환과 artemether의 기전 연관성에 대한 전임상 근거 확인
- 혈관부종 적응증으로 진행하려면 최소한 소규모 탐색 임상시험이나 전임상 연구 설계
- QT 연장 위험과 CYP3A4 관련 약물 상호작용을 포함한 안전성 모니터링 계획 수립
- 수출용 허가 제품의 국내 사용 가능 여부와 규제 경로 확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

