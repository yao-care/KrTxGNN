---
layout: default
title: Romiplostim
parent: 僅模型預測 (L5)
nav_order: 288
evidence_level: L5
indication_count: 10
---

# Romiplostim
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

# Romiplostim: 면역성 혈소판감소증(ITP)에서 혈소판 1차 방출 장애(Primary Release Disorder of Platelets)로

## 한 문장 요약

Romiplostim(Nplate®)은 트롬보포이에틴 수용체 효능제(TPO-RA)로, FDA 및 EMA에서 만성 면역성 혈소판감소증(ITP) 치료제로 허가되어 사용되어 왔습니다.
TxGNN 모델은 **혈소판 1차 방출 장애(Primary Release Disorder of Platelets)**를 최우선 신규 적응증으로 예측하며, 혈소판 관련 출혈 질환 10종으로의 재창출 가능성을 제시합니다.
이 중 **혈소판형 출혈 장애(Platelet-type Bleeding Disorder, Rank 8)**에서 **8건의 임상시험**(Phase 3 RCT 2건 포함)이 확인되어 최고 수준의 근거(L1)를 형성하며, 재창출 기회가 가장 명확합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 면역성 혈소판감소증 (ITP) — FDA/EMA 허가; 한국 미허가 |
| 예측 신규 적응증 | 혈소판 1차 방출 장애 (Primary Release Disorder of Platelets) |
| TxGNN 예측 점수 | 99.9998% |
| 근거 수준 | L4 (Rank 1 기준) / L1 (Rank 8 기준 — 최고 근거 적응증) |
| 한국 시판 현황 | ✗ 미허가 (未上市) |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails (Rank 8) / Research Question (Rank 1, 4, 9) |

---

## 예측 적응증 전체 개요

> 이 보고서는 **복수 적응증(multi)** 평가입니다. TxGNN이 예측한 10개 적응증의 근거 수준과 기전 타당성을 함께 제시합니다.

| Rank | 질환명 | TxGNN 점수 | 근거 수준 | 기전 타당성 | 권장 결정 |
|------|--------|-----------|---------|-----------|---------|
| 1 | Primary Release Disorder of Platelets | 99.9998% | L4 | 중간 (TPO-RA 기전 연관성) | Research Question |
| 2 | Pseudo-von Willebrand Disease | 99.9998% | L5 | 낮음 (GPIb 구조 결함 → 소비성 감소) | Hold |
| 3 | Glanzmann Thrombasthenia | 99.9995% | L5 | 매우 낮음 (GPIIb/IIIa 기능 결함) | Hold |
| 4 | Fetal & Neonatal Alloimmune Thrombocytopenia | 99.9873% | L4 | 중간 (ITP 유사 기전, 태아 안전성 미확인) | Research Question |
| 5 | Scott Syndrome | 99.9666% | L5 | 없음 (PS 외반 기능 결함, 수량과 무관) | Hold |
| 6 | Hemorrhagic Disorder (Constitutional Thrombocytopenia) | 99.9529% | L5 | 낮음 (c-MPL 경로 온전성 불확실) | Hold |
| 7 | Bleeding Diathesis (Collagen Receptor Defect) | 99.9508% | L4 | 낮음 (GPVI/GPIa 기능 결함) | Hold |
| **8** | **Platelet-type Bleeding Disorder** | **99.9319%** | **L1** | **높음 (ITP 핵심 기전 직접 대응)** | **Proceed with Guardrails** |
| 9 | Autosomal Dominant Macrothrombocytopenia | 99.8807% | L4 | 중간 (c-MPL 신호 경로 보존 가능) | Research Question |
| 10 | Ehlers-Danlos Syndrome, Fibronectinemic Type | 99.8452% | L5 | 없음 (혈관 구조 결함, 혈소판 수와 무관) | Hold |

---

## 이 예측이 타당한 이유는?

Romiplostim은 트롬보포이에틴(TPO)을 모방하는 Fc-펩타이드 융합 단백질로, c-MPL(TPO 수용체)에 결합하여 JAK2/STAT5 신호 경로를 활성화합니다. 이 과정에서 골수 내 거핵세포(megakaryocyte)의 증식과 분화가 촉진되어 전혈소판 형성(proplatelet formation) 및 혈소판 방출이 증가합니다. ITP에서 이미 검증된 이 기전은 본질적으로 혈소판 **수량 부족**을 보상하는 방향으로 작용합니다.

TxGNN이 예측한 10개 질환은 지식 그래프에서 ITP와 인접한 혈소판 관련 출혈 장애들입니다. 기전적 타당성은 병태생리에 따라 크게 갈립니다. 혈소판 **수 감소**가 핵심인 질환(Rank 1 방출 장애, Rank 4 FNAIT, Rank 8 광의 ITP, Rank 9 선천성 거대혈소판감소증)은 TPO-RA 보상 치료의 논리가 성립합니다. 반면 GPIIb/IIIa 결핍(Glanzmann 혈소판무력증), PS 외반 이상(Scott 증후군), 콜라겐 수용체 결함처럼 **기능·구조 결함**이 주된 질환은 혈소판 수를 늘려도 결함을 해결하지 못하므로 기전 연결성이 약합니다.

**PMID 25682608** 연구는 이 연결의 핵심 단서를 제공합니다. ITP 환자의 자가항체가 거핵세포의 전혈소판 형성을 직접 억제한다는 것을 in vitro에서 확인하였으며, 이는 Rank 1 "혈소판 1차 방출 장애"의 병태생리(거핵세포 신호 → 방출 억제)에 TPO-RA 보상 증가가 합리적으로 개입할 수 있음을 시사합니다. 다만 이 근거는 전임상·기전 수준(L4)으로, 직접 임상 효능 데이터가 아직 없습니다.

---

## 임상시험 근거

### Rank 1 — Primary Release Disorder of Platelets

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03820960](https://clinicaltrials.gov/study/NCT03820960) | N/A | 완료 | 10,039 | ITP 환자의 혈전 위험인자 평가 관찰연구. romiplostim 치료 간섭 없는 역학 연구로, 직접 치료 효능 데이터가 아닌 ITP 환자군 배경 데이터를 제공함 |

### Rank 4 — Fetal and Neonatal Alloimmune Thrombocytopenia

현재 관련 임상시험 등록이 없습니다.

### Rank 8 — Platelet-type Bleeding Disorder ★ 최고 근거 적응증 (L1)

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT05492409](https://clinicaltrials.gov/study/NCT05492409) | Phase 3 | 완료 | 160 | GNR-069(romiplostim 바이오시밀러) 대상 ITP Phase 3 장기 안전성·면역원성 연장 연구. ITP에서의 장기 안전성 데이터 확보 |
| [NCT03362177](https://clinicaltrials.gov/study/NCT03362177) | Phase 3 | 완료 | 165 | RECITE 연구: 위장관·췌장·대장직장암 환자의 옥살리플라틴 기반 화학요법 유발 혈소판감소증에 대한 romiplostim 무작위 이중맹검 위약대조 연구. 혈소판감소성 출혈 장애 직접 치료 효능 평가 |
| [NCT04638829](https://clinicaltrials.gov/study/NCT04638829) | Phase 4 | 완료 | 60 | 만성 ITP 환자에서 eltrombopag 또는 romiplostim에서 avatrombopag로 전환 시 90일간 안전성·내약성 다기관 개방형 연구. 실제 임상 환경(RWD) 안전성 데이터 제공 |
| [NCT02298075](https://clinicaltrials.gov/study/NCT02298075) | N/A | 완료 | 148 | 지속성·만성 pITP 환자에서 TPO-RA(eltrombopag·romiplostim) 중단 후 반응률 및 반응 지속 기간 후향적 연구. 장기 관리 및 중단 전략 데이터 |
| [NCT02335268](https://clinicaltrials.gov/study/NCT02335268) | Phase 2 | 완료 | 77 | MDS 저위험군(IPSS low/int-1) 혈소판감소증 환자에서 내인성 TPO 농도·수혈력을 통한 romiplostim 반응 예측 모델 전향적 검증 (EUROPE 시험) |
| [NCT02046291](https://clinicaltrials.gov/study/NCT02046291) | Phase 1 | 완료 | 21 | 제대혈 이식 후 혈소판 생착 실패(≥day +30) 환자 대상 weekly romiplostim 용량증량 안전성 연구. 이식 관련 적응증이지만 romiplostim 안전성 프로파일 확인 |
| [NCT02227576](https://clinicaltrials.gov/study/NCT02227576) | Phase 2 | 조기 종료 | 20 | 신경교모세포종 환자의 temozolomide 유발 혈소판감소증 예방 romiplostim 2차 예방 연구. 조기 종료로 근거 등급 한계 있음 |
| [NCT07321626](https://clinicaltrials.gov/study/NCT07321626) | Phase 1 | 모집 중 | 130 | 혈액암 환자 반일치 동종 조혈모세포이식 후 혈소판 재건 촉진 Romiplostim N01 무작위 대조 연구 (2027년 12월 완료 예정, 근거 아직 미성숙) |

### Rank 9 — Autosomal Dominant Macrothrombocytopenia

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

### Rank 1 — Primary Release Disorder of Platelets

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [25682608](https://pubmed.ncbi.nlm.nih.gov/25682608/) | 2015 | 기초/기전 | Haematologica | ITP 환자 혈청의 자가항체가 거핵세포의 전혈소판 형성(proplatelet formation) 및 혈소판 방출을 직접 억제함을 in vitro 확인. Rank 1 예측의 핵심 기전 근거 |
| [23594368](https://pubmed.ncbi.nlm.nih.gov/23594368/) | 2013 | Review | Br J Haematol | 거핵세포 성숙·혈소판 방출 전 과정 기전 종합 리뷰. TPO/c-MPL이 혈소판 계통의 일차 성장인자임을 확인하여 TPO-RA 치료 근거 배경 제공 |

### Rank 4 — Fetal and Neonatal Alloimmune Thrombocytopenia

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [34711622](https://pubmed.ncbi.nlm.nih.gov/34711622/) | 2021 | Case Report | BMJ Case Reports | 임신 9주부터 표준 치료에 불응하는 중증 ITP 환자에서의 치료 경과 증례. TPO-RA의 임신 중 사용 맥락 및 분만 전략 제공 (간접 근거) |
| [27605856](https://pubmed.ncbi.nlm.nih.gov/27605856/) | 2016 | Case Report | Asian J Transfusion Sci | 임신 중 난치성 ITP에서 eltrombopag 사용 증례. romiplostim을 포함한 TPO-RA의 임신 중 효능·안전성 데이터가 제한적임을 명시 |

### Rank 7 — Bleeding Diathesis due to Collagen Receptor Defect

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [21902682](https://pubmed.ncbi.nlm.nih.gov/21902682/) | 2011 | Cohort/Observational | Br J Haematol | TPO-RA 치료 ITP 환자(25명)에서 골수 세망섬유증 등급 증가 및 콜라겐-III 형성 혈청 마커 상승 관찰. 콜라겐 수용체 결함 치료 데이터가 아닌, TPO-RA 장기 투여 시 골수 부작용 모니터링 근거 |

### Rank 9 — Autosomal Dominant Macrothrombocytopenia

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [29090586](https://pubmed.ncbi.nlm.nih.gov/29090586/) | 2018 | 후향적 코호트 | Platelets | MYH9-RD(가장 흔한 상염색체 우성 거대혈소판감소증) 오스트레일리아 코호트 진단·치료 경험. c-MPL 경로 보존 시 TPO-RA 반응 가능성을 시사하지만 직접 romiplostim 효능 데이터 없음 |

---

## 한국 시판 정보

현재 식품의약품안전처(MFDS)에 등록된 Romiplostim 허가 내역이 없습니다.

> **참고**: Romiplostim(Nplate®, Amgen)은 FDA(2008), EMA(2009) 허가를 보유하며 ITP 치료에 사용되는 글로벌 의약품입니다. 한국 시장 진입을 위해서는 별도의 MFDS 품목허가 절차가 필요합니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> **추가 주의**: PMID 21902682 연구에서 TPO-RA 장기 투여 시 골수 세망섬유증 진행 가능성이 관찰되었습니다. Rank 8 적응증 실제 적용 시 정기적인 골수 모니터링 계획이 권장됩니다.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails (Rank 8 — Platelet-type Bleeding Disorder)**

**사유:**
Romiplostim은 ITP를 포함하는 광의의 혈소판형 출혈 장애에 대해 Phase 3 RCT 2건을 포함한 8건의 임상시험 근거를 보유하며, FDA·EMA 허가를 통해 임상적 유효성이 이미 검증된 약물입니다. 다만 한국 미허가 상태, 특수 집단(임산부·소아) 용법 제한, 장기 투여 시 골수 섬유화 위험에 대한 Guardrails 적용이 필수적입니다.

**개별 적응증 결정 요약:**

| 결정 | 적응증 |
|------|--------|
| Proceed with Guardrails | Rank 8 (Platelet-type Bleeding Disorder) |
| Research Question | Rank 1 (혈소판 방출 장애), Rank 4 (FNAIT), Rank 9 (선천성 거대혈소판감소증) |
| Hold | Rank 2, 3, 5, 6, 7, 10 — 기전 불일치 또는 근거 전무 |

**진행하려면 필요한 것:**

- **[DG001 해결]** MFDS/TFDA 허가사항 PDF 다운로드 및 경고·금기 항목 파악
- **[DG002 해결]** DrugBank API를 통한 Romiplostim 상세 MOA 데이터 보완
- 한국 MFDS 허가 도입 타당성 및 전략 검토 (품목허가 신청 경로 확인)
- Rank 1 (혈소판 방출 장애) 및 Rank 4 (FNAIT) 대상 전향적 임상 연구 설계 검토
- Rank 8 적응증에 대한 한국 내 현재 off-label 사용 현황 및 보험급여 상황 조사
- 장기 투여 안전성 모니터링 계획 수립 (CBC 및 골수 검사 주기 프로토콜)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

