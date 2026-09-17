---
layout: default
title: Rifabutin
parent: 높은 근거 (L1-L2)
nav_order: 600
evidence_level: L1
indication_count: 10
---

# Rifabutin
{: .fs-9 }

근거 수준: **L1** | 예측 적응증: **10** 건
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

# Rifabutin: 결핵/MAC 감염 관리에서 HIV 감염 관리로

## 한 문장 요약

> Rifabutin은 리파마이신(rifamycin) 계열 항생제로, 원래 결핵(TB) 치료와 HIV 환자의 Mycobacterium avium complex(MAC) 감염 예방·치료에 사용되어 왔습니다.
> TxGNN 모델은 **HIV 감염(HIV infectious disease)**에 효과가 있을 수 있다고 예측하며,
> 현재 **10건 이상의 임상시험**(Phase 3 RCT 포함, n=720·n=400 등)과 **다수의 문헌**이 이 방향을 뒷받침합니다. 다만 이는 HIV 바이러스 자체가 아닌 **HIV 환자의 기회감염 관리**에 대한 근거임을 유의해야 합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 결핵(TB) 치료 및 HIV 환자의 MAC(Mycobacterium avium complex) 감염 예방·치료 (한국 공식 허가 데이터 없음) |
| 예측 신규 적응증 | HIV 감염 (HIV infectious disease) — 실질적으로는 HIV 환자의 기회감염 관리 |
| TxGNN 예측 점수 | 99.88% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Rifabutin은 반합성 리파마이신(rifamycin) 계열 항생제로, 세균의 DNA 의존성 RNA 폴리머라제(rpoB)를 표적하여 저해함으로써 *Mycobacterium tuberculosis* 및 MAC에 살균 효과를 나타냅니다. 다만 HIV 바이러스 자체를 직접 억제하는 항바이러스제는 아닙니다.

HIV 감염 환자에서 Rifabutin의 실제 가치는 다음 세 가지입니다: (1) HIV 양성 환자의 MAC 균혈증 예방·치료, (2) TB/HIV 동시감염 치료, (3) Rifampicin 대비 CYP3A4 유도 작용이 약해 항레트로바이러스제(특히 단백분해효소 억제제·INSTI 계열)와 병용 시 약물 상호작용이 상대적으로 적다는 점입니다. 즉 예측된 적응증명 "HIV infectious disease"는 HIV 바이러스에 대한 직접적 항바이러스 효과가 아니라, **HIV 환자에서의 분감균(mycobacterial) 기회감염 관리**를 의미하는 것으로 해석해야 합니다.

DrugBank 기반 공식 MOA 데이터는 현재 확보되지 않았습니다(Data Gap). 다만 위 기전은 다수의 완료된 Phase 3 임상시험과 수십 편의 문헌에서 일관되게 지지되고 있어, 예측의 기전적 타당성은 높다고 판단됩니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00002080](https://clinicaltrials.gov/study/NCT00002080) | NA | 완료 | N/A | HIV 양성 환자에서 MAC 균혈증 예방을 위한 Rifabutin 일일 투여 요법 평가 |
| [NCT00002122](https://clinicaltrials.gov/study/NCT00002122) | Phase 3 | 완료 | 720 | Azithromycin·Rifabutin 단독/병용 요법의 HIV 환자 MAC 감염 예방 효능 비교(RCT) |
| [NCT00001047](https://clinicaltrials.gov/study/NCT00001047) | Phase 3 | 완료 | 400 | Clarithromycin + Ethambutol + Rifabutin/Clofazimine 4개 치료군 비교, AIDS 환자의 파종성 MAC 질환 치료 |
| [NCT03478033](https://clinicaltrials.gov/study/NCT03478033) | NA | 불명 | 230 | HIV/폐결핵 동시감염 환자에서 Rifampicin 대 Rifabutin 기반 표준요법의 효능·안전성 전향적 비교 |
| [NCT01259219](https://clinicaltrials.gov/study/NCT01259219) | Phase 1 | 불명 | 40 | Kaletra(LPV/RTV) 병용 시 소아 HIV 감염환자에서 Rifabutin 용량-PK-안전성 탐색 |
| [NCT00018083](https://clinicaltrials.gov/study/NCT00018083) | NA | 불명 | N/A | HIV/TB 동시감염 환자에서 Nelfinavir-Rifabutin 약물상호작용 집중 PK 연구 |
| [NCT00001023](https://clinicaltrials.gov/study/NCT00001023) | NA | 완료 | 91 | HIV 감염환자에서 Rifabutin/Clarithromycin, Rifabutin/Azithromycin 병용 안전성·내약성·PK 평가 |
| [NCT00651066](https://clinicaltrials.gov/study/NCT00651066) | Phase 2 | 완료 | 47 | 베트남 TB/HIV 동시감염 환자에서 ART 병용 시 Rifabutin PK 평가(Rifampicin 대체 가능성 탐색) |
| [NCT01663168](https://clinicaltrials.gov/study/NCT01663168) | Phase 2 | 불명 | 140 | LPV/r 2차 ART 복용 중인 HIV 감염 성인·청소년에서 Rifabutin 용량별 독성·PK 평가(EARNEST 하위연구) |
| [NCT01894776](https://clinicaltrials.gov/study/NCT01894776) | Phase 1 | 완료 | 15 | Rifabutin이 Maraviroc PK에 미치는 영향 평가(DDI 연구) |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [23828580](https://pubmed.ncbi.nlm.nih.gov/23828580/) | 2013 | 체계적 문헌고찰/메타분석 | Cochrane Database Syst Rev | Rifamycin(Rifabutin 포함) vs Isoniazid의 잠복결핵 예방 효능 비교 |
| [31139825](https://pubmed.ncbi.nlm.nih.gov/31139825/) | 2019 | 코호트(안전성/효능) | J Antimicrob Chemother | LPV/r 기반 ART 중인 TB/HIV 동시감염 소아에서 Rifabutin 안전성·효능 평가 |
| [33294914](https://pubmed.ncbi.nlm.nih.gov/33294914/) | 2021 | 코호트(PK/안전성) | J Antimicrob Chemother | LPV/r 2차 ART 병용 TB/HIV 동시감염 소아의 Rifabutin PK 및 안전성 |
| [25281400](https://pubmed.ncbi.nlm.nih.gov/25281400/) | 2015 | 코호트(PK/안전성) | J Antimicrob Chemother | LPV/r 병용 소아 HIV 감염환자에서 Rifabutin PK 및 단기 안전성 |
| [9459473](https://pubmed.ncbi.nlm.nih.gov/9459473/) | 1998 | 소규모 임상연구 | JAMA | Clarithromycin·Rifabutin의 HIV 환자 크립토스포리디움증 화학예방 가능성(HOPS 연구) |
| [21726477](https://pubmed.ncbi.nlm.nih.gov/21726477/) | 2009 | Review | BMJ Clin Evid | HIV 감염자의 결핵 치료 전반에 대한 근거 리뷰 |
| [28233512](https://pubmed.ncbi.nlm.nih.gov/28233512/) | 2017 | Review | Microbiol Spectr | HIV와 결핵의 상호작용 및 치료 전략 리뷰 |
| [7736687](https://pubmed.ncbi.nlm.nih.gov/7736687/) | 1995 | Review | Clin Pharmacokinet | Rifabutin의 임상 약동학, HIV+ 저CD4 환자에서의 MAC 예방 효능 근거 |
| [21406051](https://pubmed.ncbi.nlm.nih.gov/21406051/) | 2011 | Review | Infect Disord Drug Targets | HIV 유행 시대의 성인 활동성 결핵 관리 및 ART-항결핵제 상호작용 전반 리뷰 |
| [40310456](https://pubmed.ncbi.nlm.nih.gov/40310456/) | 2025 | Review | PNAS | 차세대 Rifamycin 계열의 분감균 감염 치료 전망 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> 한국 내 미시판 상태이며, TFDA/MFDS 급 공식 경고·금기·DDI 데이터가 아직 확보되지 않았습니다(Blocking Data Gap: DG001). 다만 임상시험 근거에서 반복적으로 확인되는 주요 약물상호작용으로 **CYP3A4 관련 항레트로바이러스제(단백분해효소 억제제, INSTI 계열)와의 상호작용**, 그리고 **포도막염(uveitis)** 등 안과적 이상반응이 보고되고 있어(예: PMID 8967681, 30217608), 공식 허가사항 확보 시 우선 확인이 필요합니다.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
HIV 환자의 MAC 균혈증 예방·치료 및 TB/HIV 동시감염 치료에 대해서는 Phase 3 RCT(NCT00002122, n=720; NCT00001047, n=400)를 포함한 강력한 임상 근거(L1)가 존재합니다. 다만 "HIV infectious disease"라는 예측 라벨은 HIV 바이러스에 대한 직접적 항바이러스 효과가 아니라 **HIV 환자의 분감균 기회감염 관리**를 의미하므로, 적응증 정의를 명확히 좁혀 진행해야 합니다.

**진행하려면 필요한 것:**
- MFDS(한국 식약처) 허가사항 확보 — 경고/금기 정보 (현재 Blocking 상태, DG001)
- DrugBank 기반 공식 MOA 데이터 확보 (DG002)
- 한국 내 시판·허가 현황 확인 (현재 미시판, 0건)
- 적응증 라벨을 "HIV 감염" 대신 "HIV 환자의 MAC/TB 기회감염 예방·치료"로 재정의하여 임상 의미 명확화
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

