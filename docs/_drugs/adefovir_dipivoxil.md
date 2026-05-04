---
layout: default
title: Adefovir Dipivoxil
parent: 僅模型預測 (L5)
nav_order: 25
evidence_level: L5
indication_count: 10
---

# Adefovir Dipivoxil
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

# Adefovir Dipivoxil: 한국 미허가 → B형 간염 바이러스 감염 치료 도입 평가

---

## 한 문장 요약

Adefovir Dipivoxil(DB00718)은 HBV DNA 중합효소를 억제하는 뉴클레오타이드 유사체 항바이러스제로, 전 세계적으로 만성 B형 간염 치료제(Hepsera®)로 허가되어 있으나 **한국에서는 현재 미허가** 상태입니다.
TxGNN 모델은 10가지 적응증을 예측했으나, 심층 분석 결과 순위 1위(만성 C형 간염)를 포함한 대부분이 지식그래프 인접 효과로 인한 가성 양성으로 판별되었으며, **B형 간염 바이러스 감염(순위 6위, 근거 수준 L1)**이 유일하게 임상적으로 유효한 후보임이 확인되었습니다.
한국인 만성 HBV 환자를 직접 대상으로 한 Phase 4 임상시험(n=104) 및 대규모 시판 후 조사(n=4,393)를 포함하여 **10건 이상의 완료된 Phase 3 RCT**와 **20편 이상의 문헌**이 이 방향을 강력히 지지합니다.

> ⚠️ **TxGNN 예측 해석 주의**: 순위 1위 '만성 C형 간염'은 HCV-HBV 인접 노드 효과로 인한 **가성 양성**입니다. 수집된 임상시험 9건 모두가 HBV 연구로 오분류되었으며, HCV에 대한 기전적 근거가 전혀 없습니다. 본 보고서는 근거 수준 L1을 기록한 **B형 간염(순위 6위)**을 주요 평가 대상으로 합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 미허가 (글로벌 기준: 만성 B형 간염) |
| 예측 신규 적응증 (최우선 근거) | B형 간염 바이러스 감염 (Hepatitis B Virus Infection) |
| TxGNN 예측 점수 | 99.87% (전체 10위 중 6위) |
| 근거 수준 | L1 (완료된 Phase 3 RCT 다수) |
| 한국 시판 현황 | ✗ 미상시 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## TxGNN 전체 예측 순위 개요

| 순위 | 적응증 | TxGNN 점수 | 근거 수준 | 결정 | 비고 |
|------|--------|-----------|-----------|------|------|
| 1 | 만성 C형 간염 바이러스 감염 | 99.97% | L4 | Hold | 기전 불일치, 임상시험 전부 HBV 연구로 오분류 |
| 2 | HIV 감염 | 99.95% | L2 | Hold | 역사적 탐색, 신독성으로 개발 포기 |
| 3 | 신경발달장애 (감소된 피질 백질 등) | 99.91% | L5 | Hold | 임상시험 0건·문헌 0편, 기전 연결 없음 |
| 4 | 고양이 후천성 면역결핍증 (FIV) | 99.91% | L5 | Hold | 동물 질환, 인간 약물 재창출 범위 외 |
| 5 | 원숭이 면역결핍 바이러스 감염 (SIV) | 99.91% | L4 | Hold | 동물 질환, HIV→SIV 그래프 인접 효과 |
| **6** | **B형 간염 바이러스 감염** | **99.87%** | **L1** | **Proceed with Guardrails** | **글로벌 허가 적응증, 한국 도입 검토 대상** |
| 7 | C형 간염 바이러스 감염 | 99.74% | L4 | Hold | 기전 불일치, 유일 관련 시험 WITHDRAWN |
| 8 | E형 간염 바이러스 감염 (HEV) | 99.53% | L5 | Hold | 기전 불일치 (RNA 바이러스) |
| 9 | 동물 바이러스성 간염 | 99.52% | L4 | Research | 동물 질환 (인간 적용 불가) |
| 10 | A형 간염 바이러스 감염 (HAV) | 99.52% | L5 | Hold | 기전 불일치 (RNA 바이러스) |

---

## 이 예측이 타당한 이유는?

Adefovir Dipivoxil은 아데포비르(PMEA)의 경구용 전구약물로, 체내에서 두 단계의 인산화를 거쳐 활성형인 **아데포비르 이인산(adefovir diphosphate)**으로 전환됩니다. 이 활성형은 내인성 dATP와 경쟁적으로 **HBV DNA 중합효소(역전사효소 활성)**를 억제하며, 바이러스 DNA에 통합된 후 사슬 종결을 유발합니다. HBV는 역전사 단계를 포함하는 독특한 DNA 복제 과정을 거치므로 뉴클레오타이드 유사체의 효과적인 표적이 됩니다.

Adefovir는 야생형 HBV뿐 아니라 **라미부딘 내성 YMDD 변종**에도 효과적입니다. 이는 라미부딘(3TC) 치료 실패 환자의 구제 요법으로 임상적 가치가 높으며, 전 세계 HBV 가이드라인에서 역사적으로 중요한 위치를 차지해 왔습니다. 미국 FDA는 2002년 Hepsera®(10mg/day)를 만성 HBV 치료에 승인했습니다.

특히 주목할 점은, 한국에서 아직 정식 허가를 받지 않았음에도 불구하고 **한국인 만성 HBV 환자를 직접 대상으로 한 대규모 연구**가 이미 완료되어 있다는 것입니다. Phase 4 다기관 공개 연구(NCT01205165, n=104)와 시판 후 안전성 조사(NCT01329419, n=4,393)는 한국인 집단에서 Adefovir의 효능과 안전성을 실증적으로 확인해 주었습니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00095121](https://clinicaltrials.gov/study/NCT00095121) | Phase 3 | 완료 | 173 | 아동·청소년(2–17세) HBV 이중맹검 안위약 대조 RCT — 48주 치료 효능·안전성 확인, 핵심 허가 근거 시험 |
| [NCT00116805](https://clinicaltrials.gov/study/NCT00116805) | Phase 3 | 완료 | 266 | HBeAg 양성 HBV: Tenofovir vs Adefovir 이중맹검 두부 비교 — Tenofovir 우위 확인, 장기 480주 추적 데이터 포함 |
| [NCT01300234](https://clinicaltrials.gov/study/NCT01300234) | Phase 3 | 완료 | 512 | 중국인 HBV(HBeAg 양성·음성): TDF 300mg vs ADV 10mg 이중맹검 이중모의 — TDF 우위 확인, 240주 장기 안전성 데이터 |
| [NCT00531167](https://clinicaltrials.gov/study/NCT00531167) | Phase 4 | 완료 | 219 | 라미부딘 내성 HBV: Adefovir 추가 vs Entecavir 전환 비교 RCT — 내성 관리 전략 수립의 핵심 근거 |
| [NCT01329419](https://clinicaltrials.gov/study/NCT01329419) | PMS | 완료 | 4,393 | **한국인 HBV 환자 HEPSERA 시판 후 안전성 조사** — 가장 큰 규모의 한국인 실세계 안전성·효능 데이터 |
| [NCT01205165](https://clinicaltrials.gov/study/NCT01205165) | Phase 4 | 완료 | 104 | **한국인 만성 HBV 환자 Adefovir 12주·52주 항바이러스 효과 다기관 공개 연구** — KrTxGNN 핵심 재현 데이터 |
| [NCT02075294](https://clinicaltrials.gov/study/NCT02075294) | N/A | 완료 | 242 | 노인 HBV 환자: Adefovir vs Entecavir 효능·안전성 비교 — 고령 환자군 특이 데이터 |
| [NCT01480284](https://clinicaltrials.gov/study/NCT01480284) | Phase 3 | 완료 | 166 | 일본인 HBV NUC 미치료 환자: GSK548470(ADV 계열) vs Entecavir 비열등성 다기관 이중맹검 RCT |
| [NCT00023309](https://clinicaltrials.gov/study/NCT00023309) | Phase 2 | 완료 | 41 | 만성 HBV: 라미부딘+Adefovir 병용 vs Adefovir 단독 — 내성 극복 병용 전략 장기 근거 (2013년까지 추적) |
| [NCT01373684](https://clinicaltrials.gov/study/NCT01373684) | Phase 4 | 완료 | 90 | HBeAg 음성 HBV(NUC 치료 중): Peg-IFN alfa-2a 추가 시 HBsAg 감소 유도 여부 — Adefovir 배경 치료로 사용 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [14498759](https://pubmed.ncbi.nlm.nih.gov/14498759/) | 2003 | Systematic Review | Drugs | HBeAg 양성·음성 HBV에서 Adefovir 10mg/day가 조직학·바이러스학·생화학적 지표를 유의하게 개선함을 종합 확인 |
| [16904047](https://pubmed.ncbi.nlm.nih.gov/16904047/) | 2006 | Systematic Review | Health Technol Assess | Adefovir 및 PegIFN의 임상적 효과성과 비용효과성에 대한 HTA 체계적 문헌고찰 (영국) |
| [19607759](https://pubmed.ncbi.nlm.nih.gov/19607759/) | 2009 | Systematic Review | Health Technol Assess | 2006년 HTA 보고서의 업데이트 체계적 문헌고찰 및 경제성 평가 — 신규 데이터 반영 |
| [22226087](https://pubmed.ncbi.nlm.nih.gov/22226087/) | 2012 | Meta-analysis | Int J Infect Dis | 라미부딘 내성 HBV: Adefovir 단독 vs 라미부딘+Adefovir 병용 효능·내성 비교 메타분석 |
| [27977591](https://pubmed.ncbi.nlm.nih.gov/27977591/) | 2016 | Safety Cohort | Medicine | 장기 Adefovir 치료와 신기능 저하 관계 메타분석 — 신독성 위험인자 및 모니터링 기준 제시 |
| [15482214](https://pubmed.ncbi.nlm.nih.gov/15482214/) | 2004 | Clinical Review | Expert Rev Anti-Infect Ther | Adefovir 10mg/day HBV 치료 효과 — HBeAg 음성 HBV에서 3년 이상 효능 유지 데이터 포함 |
| [22242973](https://pubmed.ncbi.nlm.nih.gov/22242973/) | 2012 | Historical Review | Expert Opin Pharmacother | Adefovir의 HBV 치료 역사, 허가 경과, 현재 임상적 사용 현황 종합 |
| [14697813](https://pubmed.ncbi.nlm.nih.gov/14697813/) | 2003 | Review | Lancet | 전 세계 4억 명의 만성 HBV 감염 현황, 진단·치료 최신 동향 및 항바이러스제 개요 |
| [14749147](https://pubmed.ncbi.nlm.nih.gov/14749147/) | 2003 | Clinical Review | Clin Ther | Adefovir의 작용 기전, 약동학, HBV 임상시험 결과, 안전성 종합 정리 |
| [15500383](https://pubmed.ncbi.nlm.nih.gov/15500383/) | 2004 | Clinical Review | Expert Opin Pharmacother | HBeAg 양성·음성, 라미부딘 내성, 이식 전후 HBV 환자에서의 Adefovir 효능 및 라미부딘 대비 내성 프로필 |

---

## 한국 시판 정보

현재 한국 내 Adefovir Dipivoxil로 허가된 제품이 없습니다.

글로벌 기준으로 Hepsera®(Gilead Sciences, 10mg 경구 정제)가 미국 FDA(2002년 승인) 및 EMA에서 성인 만성 B형 간염 치료제로 허가되어 있으며, 일본 등 아시아 국가에서도 사용 중입니다. 한국에서의 대규모 시판 후 안전성 데이터(NCT01329419, n=4,393)와 Phase 4 임상 데이터(NCT01205165, n=104)는 존재하나, 정식 국내 허가는 이루어지지 않은 상태입니다.

---

## 안전성 고려사항

공식 한국 허가사항이 없어 처방 정보를 국내 규제 문서에서 확인할 수 없습니다. 글로벌 허가사항(Hepsera® US PI) 및 문헌 기반의 주요 안전성 정보를 아래에 요약합니다.

**신독성 (핵심 안전 우려)**
장기 투여(특히 5년 이상) 시 근위 세뇨관 기능 장애(Fanconi 증후군) 발생 위험이 있습니다. 혈청 크레아티닌 상승, 저인산혈증, 저인산혈증성 골연화증이 보고되었으며(PMID: 32289307), 기저 신기능 저하 환자에서 위험이 증가합니다. 메타분석(PMID: 27977591)은 신독성과 장기 Adefovir 치료 간의 용량-기간 의존적 관계를 확인하였습니다.

**HIV 고용량 독성 교훈**
HIV 유효 억제 용량(30–120mg/day)에서는 심각한 신독성이 발생하여 HIV 적응증 개발이 포기되었습니다. 현재 HBV 허가 용량(10mg/day)에서는 신독성 위험이 관리 가능한 수준이나, 정기 모니터링이 필수입니다.

**임신 중 사용**
동물 실험에서 배아독성 및 최기형성이 확인되었습니다. 임신 중 노출 시 임신 결과에 대한 인체 데이터가 제한적입니다(PMID: 32019360).

**권장 모니터링 항목**
- 신기능: 혈청 크레아티닌, eGFR, 혈청 인산 (치료 전 기저치 및 분기별 추적)
- 간기능: ALT, HBV DNA 정량, HBeAg/HBsAg 혈청 변환 여부

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
B형 간염 바이러스 감염에 대한 Adefovir Dipivoxil의 효능은 다수의 완료된 Phase 3 이중맹검 RCT를 통해 전 세계적으로 확립된 근거 수준 L1 약물입니다. 특히 한국인 환자를 대상으로 한 독자 데이터(시판 후 조사 n=4,393 + Phase 4 n=104)가 이미 존재하므로, 한국 도입을 위한 임상적 기반은 충분합니다. 다만, Tenofovir(TDF/TAF) 및 Entecavir 대비 신독성 프로필이 불리하여 현재 1차 선택약 지위는 어렵고, **라미부딘 내성 HBV 구제 요법** 또는 **TDF/ETV 불내약성 환자** 등 틈새 적응을 중심으로 한 전략이 현실적입니다.

**진행하려면 필요한 것:**
- 한국 MFDS(식품의약품안전처) 신약 허가 신청 타당성 검토 — TDF/ETV 대비 차별화 포지셔닝 전략 수립 필요
- TFDA 공식 허가사항(처방 정보) 확보 — 현재 주요 데이터 갭(DG001: 경고/금기 정보 부재)
- DrugBank 기반 공식 MOA 데이터 확인 (DG002)
- 장기 신기능 모니터링 프로토콜 수립 및 한국 환자 특이 신독성 위험인자 분석
- 국내 HBV 치료 가이드라인(대한간학회)과의 적합성 검토 및 급여 전략 설계
- 비용효과 분석 — 국내 HBV 표준치료(TDF/ETV)와의 비교 경제성 평가
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

