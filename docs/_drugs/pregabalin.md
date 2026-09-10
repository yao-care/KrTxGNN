---
layout: default
title: Pregabalin
parent: 僅模型預測 (L5)
nav_order: 574
evidence_level: L5
indication_count: 6
---

# Pregabalin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# PREGABALIN: 신경병증성 통증에서 편두통 예방으로

## 한 문장 요약

Pregabalin은 원래 신경병증성 통증 및 부분 발작 치료에 사용되는 약물입니다.
TxGNN 모델은 여러 적응증을 예측했으나, 그중 **편두통(Migraine Disorder)**이
**1건의 관련 Phase 3 임상시험**과 **20편의 문헌**으로 가장 근거가 풍부합니다.
다만 핵심 확증 시험이 조기 종료되어 추가 검증이 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (한국 미시판) |
| 예측 신규 적응증 | 편두통 (Migraine Disorder) |
| TxGNN 예측 점수 | 99.47% |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미상장 (한국 미시판) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold (Research Question) |

> ⚠️ 이 약물은 현재 한국에 정식 허가·시판되고 있지 않습니다. TFDA 원본 데이터가 대만 기준으로 작성된 Evidence Pack이며, 한국 허가 현황은 별도 확인이 필요합니다.

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 확보되지 않았습니다 (Data Gap - DrugBank MOA 조회 필요). 다만 문헌 근거에 따르면, Pregabalin은 전위작동 칼슘통로(voltage-gated calcium channel)의 α2δ 소단위에 결합하여 흥분성 신경전달물질 방출을 억제하는 약물로 알려져 있습니다.

이 기전은 편두통의 핵심 병태생리인 피질확산억제(cortical spreading depression, CSD) 및 중추 감작(central sensitization)과 직접 연관됩니다. 전임상 연구(PMID 28223480, 37924146)에서 Pregabalin이 CSD 발생 역치를 높이고 피질하부 구조로의 전파를 억제함이 확인되었습니다. 소아 편두통 예방에서 Pregabalin과 valproate/propranolol을 비교한 여러 RCT도 존재하나, 성인 대상 핵심 Phase 3 확증시험(NCT00447369)은 등록 중단(WITHDRAWN)되어 실질적 유효성 데이터를 얻지 못했습니다.

나머지 4개 예측 적응증(tendinitis, idiopathic granulomatous myositis, myositis fibrosa, inclusion body myositis, migraine with brainstem aura)은 임상시험 근거가 없거나(L5) 통증 완화 기전에 대한 간접적 추론에 그쳐(L4), 편두통 대비 근거 수준이 현저히 낮습니다.

---

## 임상시험 근거

### 편두통 (Migraine Disorder) — Rank 1 근거 수준

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00447369](https://clinicaltrials.gov/study/NCT00447369) | Phase 3 | **중단됨(WITHDRAWN)** | 70 | Pregabalin vs sodium valproate 편두통 예방 비교 — 결과 미산출, 핵심 증거 공백 |
| [NCT02747940](https://clinicaltrials.gov/study/NCT02747940) | Phase 4 | 완료 | 200 | 만성 편두통/섬유근육통 뇌 신호 연구 (간접 관련) |
| [NCT02670161](https://clinicaltrials.gov/study/NCT02670161) | Phase 4 | 모집 중(초청 대상) | 3300 | 신경과 10대 질환 EMR 기반 실용적 임상연구 (간접 관련) |

### 기타 예측 적응증
- **Tendinitis, Myositis 관련 3건**: 현재 관련 임상시험 등록이 없습니다.
- **Migraine with brainstem aura**: 현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

### 편두통 (Migraine Disorder) — 우선순위 상위 문헌

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [39388181](https://pubmed.ncbi.nlm.nih.gov/39388181/) | 2024 | Review | JAMA Network Open | 소아 편두통 예방약물 네트워크 메타분석 |
| [37637787](https://pubmed.ncbi.nlm.nih.gov/37637787/) | 2023 | RCT | Iran J Child Neurol | Pregabalin vs sodium valproate 소아 편두통 예방 비교 RCT |
| [26024701](https://pubmed.ncbi.nlm.nih.gov/26024701/) | 2015 | RCT | Acta Med Iran | Propranolol vs pregabalin 소아 편두통 예방 RCT |
| [23797674](https://pubmed.ncbi.nlm.nih.gov/23797674/) | 2013 | Review | Cochrane Database Syst Rev | 항간질약(gabapentin/pregabalin/topiramate/valproate 제외) 편두통 예방 체계적 고찰 |
| [23797675](https://pubmed.ncbi.nlm.nih.gov/23797675/) | 2013 | Review | Cochrane Database Syst Rev | Gabapentin/pregabalin 편두통 예방 Cochrane 리뷰 |
| [19935409](https://pubmed.ncbi.nlm.nih.gov/19935409/) | 2010 | Cohort | Clin Neuropharmacol | 만성 편두통에서 pregabalin 개방표지 연구 |
| [21479703](https://pubmed.ncbi.nlm.nih.gov/21479703/) | 2011 | Cohort | J Headache Pain | Pregabalin 편두통 예방 효능·내약성 3개월 추적 연구 |
| [25669613](https://pubmed.ncbi.nlm.nih.gov/25669613/) | 2015 | Cohort | Int J Clin Pharmacol Ther | Pregabalin의 편두통 중추 감작 완화 효과 |
| [28223480](https://pubmed.ncbi.nlm.nih.gov/28223480/) | 2017 | Preclinical | PNAS | Pregabalin이 피질확산억제(CSD) 및 피질하 전파를 억제함을 생체영상으로 입증 |
| [37924146](https://pubmed.ncbi.nlm.nih.gov/37924146/) | 2023 | Preclinical | Molecular Brain | 만성 pregabalin 투여가 가족성 반신마비 편두통 모델에서 확산성 탈분극을 방지 |

---

## 한국 시판 정보

한국 시판 정보가 없습니다 (`market_status: 미상장`, `total_licenses: 0`).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> 참고: 이 Evidence Pack의 안전성 데이터는 미확보 상태(Data Gap DG001, Blocking)이며, S1 안전성 초평가 진입이 불가한 상태입니다. TFDA 원본 자료의 경고/금기 사항 확보가 선행되어야 합니다.

---

## 결론 및 다음 단계

**결정: Hold (Research Question)**

**사유:**
편두통 적응증은 CSD 억제라는 기전적 타당성과 다수의 소아 대상 RCT·코호트 연구가 존재하지만, 성인 대상 핵심 Phase 3 확증시험(NCT00447369)이 중단되어 결정적 유효성 근거가 없습니다(L2 수준). 나머지 4개 예측 적응증(건염, 근염 계열)은 문헌·임상 근거가 거의 전무하여(L4~L5) 현 단계에서 진행이 부적절합니다. 또한 안전성 데이터(TFDA 경고/금기)가 확보되지 않아 Blocking 데이터 공백이 존재합니다.

**진행하려면 필요한 것:**
- TFDA(또는 국내 식약처) 공식 허가사항 확보 — 경고, 금기, 약물상호작용 (DG001, Blocking)
- DrugBank API를 통한 상세 작용 기전(MOA) 확인 (DG002, High)
- 성인 대상 편두통 예방 Phase 2/3 RCT 신규 기획 검토 (기존 시험 중단으로 인한 공백 해소)
- 한국 내 실제 허가·시판 현황 별도 조사 (현 Evidence Pack은 대만 기준 데이터로 추정됨)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

