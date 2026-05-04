---
layout: default
title: Desonide
parent: 僅模型預測 (L5)
nav_order: 207
evidence_level: L5
indication_count: 10
---

# Desonide
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

# Desonide: 염증성 피부질환에서 아토피 습진으로

## 한 문장 요약

Desonide는 저효능 비불소화 외용 코르티코스테로이드(Class VI)로, 국제적으로 경증~중등도 아토피 피부염 치료에 사용되어 왔으나 한국에서는 현재 허가된 제품이 없습니다.
TxGNN 모델은 **아토피 습진(Atopic Eczema)**에 효과가 있을 수 있다고 예측하며,
현재 **9건의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 미허가 (등록 데이터 없음) |
| 예측 신규 적응증 | 아토피 습진 (Atopic Eczema) |
| TxGNN 예측 점수 | 99.96% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Desonide는 피부 각질형성세포 및 면역세포의 글루코코르티코이드 수용체(GR)에 결합하여 NF-κB/AP-1 전사 경로를 억제합니다. 이를 통해 아토피 습진의 핵심 병인인 Th2 사이토카인(IL-4, IL-13, IL-31, TSLP)의 발현을 하향 조절하고, 혈관 수축 및 항히스타민 효과를 동시에 발휘합니다. 즉, Th2 주도 염증 반응과 피부 장벽 손상이라는 아토피 습진의 두 가지 핵심 병리 기제를 직접 표적으로 합니다.

Desonide는 제6등급(Class VI) 저효능 스테로이드로 분류되어, HPA 축 억제 및 피부 위축 위험이 최소화됩니다. 이는 만성 경과를 밟는 아토피 습진에서 장기 유지 치료가 필요한 영아 및 소아 환자에게 특히 유리한 안전성 프로파일을 제공합니다. 미국 FDA는 Desonate® 겔 0.05% 제형을 생후 3개월 이상 소아를 포함한 아토피 피부염 치료제로 정식 승인한 바 있습니다.

한국에서는 허가된 Desonide 제품이 없으나, 다수의 Phase 3/4 임상시험과 RCT 문헌이 아토피 습진에서의 효능을 뒷받침하고 있습니다. 유사한 저효능 외용 스테로이드(hydrocortisone 1%)와 비교 시 동등 이상의 효능을 보이는 반면 전신 흡수율이 낮아, 한국 시장 도입 시 기존 외용 스테로이드 대비 경쟁 우위를 가질 수 있습니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00690833](https://clinicaltrials.gov/study/NCT00690833) | Phase 4 | 완료 | 41 | 다양한 연령대 AD 환자에서 Desonide (Desonate) 겔 0.05%의 효능 평가. FDA 승인 약물 직접 연구. |
| [NCT00828412](https://clinicaltrials.gov/study/NCT00828412) | Phase 4 | 완료 | 100 | 소아 중등도 AD에서 EpiCream 피부 장벽 유제와 Desonide 크림 0.05%의 안전성·효능 무작위 다기관 비교. |
| [NCT02286700](https://clinicaltrials.gov/study/NCT02286700) | Phase 3 | 불명 | 42 | 경증~중등도 AD에서 아미노산 보습 크림 vs. Desonide 크림의 피부 증상 개선 무작위 이중맹검 비교. |
| [NCT03386032](https://clinicaltrials.gov/study/NCT03386032) | Phase 3 | 완료 | 65 | SCORAD 기준 8주 AD 치료 크림의 임상 효과 평가. |
| [NCT02732314](https://clinicaltrials.gov/study/NCT02732314) | Phase 4 | 완료 | 53 | AD 환자 대상 신규 외용 제형의 효능 및 내약성 평가 (13주 무작위 이중맹검 병렬군 설계). |
| [NCT01779258](https://clinicaltrials.gov/study/NCT01779258) | Phase 3 | 완료 | 347 | 아동 AD 염증 병변 소실 후 보습제의 급성발작 예방 역할 확인. |
| [NCT03397979](https://clinicaltrials.gov/study/NCT03397979) | N/A | 완료 | 63 | 소아 AD에서 일 2회 vs. 주 2회 입욕(soak-and-seal) 방식의 효과 비교. |
| [NCT01467362](https://clinicaltrials.gov/study/NCT01467362) | Phase 3 | 완료 | 251 | 아동 AD 건조증에서 V0034CR01B 보습제의 효능 평가 (무작위 대조군 이중맹검). |
| [NCT07295678](https://clinicaltrials.gov/study/NCT07295678) | N/A | 미모집 | 44 | URGO FilmoCream Eczema + 표준 외용 스테로이드 병용 시 AD 증상 완화 효과 평가. |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [17373176](https://pubmed.ncbi.nlm.nih.gov/17373176/) | 2007 | RCT | J Drugs Dermatol | 소아 AD 환자에서 desonide 수화겔(hydrogel) 0.05%의 안전성 및 효능 확인. 알코올·계면활성제 무함유 Class VI 저효능 스테로이드 신제형 평가. |
| [7601950](https://pubmed.ncbi.nlm.nih.gov/7601950/) | 1995 | RCT | J Am Acad Dermatol | 소아 AD 치료에서 desonide 0.05% vs. hydrocortisone 1% 연고의 장기 안전성·효능 다기관 비교 임상. |
| [12121395](https://pubmed.ncbi.nlm.nih.gov/12121395/) | 2002 | RCT | Australas J Dermatol | 안면 지루성·아토피 피부염에서 desonide 0.05% 로션 vs. 대조제의 효능, 피부 내약성, 미용 수용성 3주 이중맹검 평가 (N=81). |
| [31551225](https://pubmed.ncbi.nlm.nih.gov/31551225/) | 2019 | RCT | Pak J Pharm Sci | 영아 습진 치료에서 MPS 연고 + desonide 연고 병용 vs. desonide 단독의 임상 효능 비교 (N=180). 병용군에서 우월한 치료 효과 확인. |
| [10930856](https://pubmed.ncbi.nlm.nih.gov/10930856/) | 2000 | RCT | Ann Dermatol Venereol | 소아 AD 치료에서 미세화 desonide 크림 0.1% vs. betamethasone 디프로피오네이트 크림 0.05%의 효능 및 혈장 코르티솔 영향 비교. |
| [18301804](https://pubmed.ncbi.nlm.nih.gov/18301804/) | 2008 | Review | Drugs Today | Desonide 폼 제형 종합 리뷰. 경증~중등도 AD에서 위약 대비 우월한 효과 확인. 소아·성인 모두에서 안전성 프로파일 양호. |
| [20514788](https://pubmed.ncbi.nlm.nih.gov/20514788/) | 2010 | Cohort | J Drugs Dermatol | AD 환자 순응도 프로그램에서 desonide 수화겔의 복약 순응도 및 초기 효능 평가. 우수한 환자 수용도 보고. |
| [39833071](https://pubmed.ncbi.nlm.nih.gov/39833071/) | 2025 | RCT | Medicine | 아동 AD에서 진정 보습 수복 크림 + desonide 병용 vs. desonide 단독 효능·안전성 비교 (N=37). 병용군에서 유지 치료 효과 확인. |
| [31424707](https://pubmed.ncbi.nlm.nih.gov/31424707/) | 2019 | Review | J Drugs Dermatol | 외용 코르티코스테로이드 폼 제형 효능·안전성 종합 리뷰. Desonide 포함 다수 약물 비교. 폼 제형의 순응도 개선 효과 강조. |
| [35986531](https://pubmed.ncbi.nlm.nih.gov/35986531/) | 2023 | 전임상/제형 | Curr Drug Deliv | Desonide 나노에멀션 겔의 경피 흡수 강화 약력학 및 안전성 전임상 평가. 기존 제형 대비 개선된 경피 전달 효율 입증. |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
Desonide는 미국 FDA 승인을 받은 아토피 피부염 치료제로, 다수의 Phase 3/4 완료 임상시험과 RCT 문헌(특히 소아 AD 대상)이 효능을 지지하며 근거 수준 L1에 해당합니다. 한국 시판 이력이 없어 국내 규제 검토가 필요하나, 국제 근거 기반의 허가 신청이 충분히 가능한 수준입니다.

**진행하려면 필요한 것:**
- 한국 식약처(MFDS) 허가를 위한 국내 임상 자료 또는 해외 허가 상호인정 검토
- DrugBank API를 통한 상세 작용 기전(MOA) 데이터 확보 (현재 Data Gap)
- MFDS 기준 경고·금기·약물 상호작용 등 안전성 정보 수집 (현재 Data Gap)
- HPA 축 억제 가능성에 대한 특이 안전성 모니터링 계획 수립 (특히 영아·소아 대상)
- 한국 소아 AD 환자 대상 소규모 브리지 임상 필요 여부 검토

---

> **⚠️ 면책 고지:** 본 보고서는 연구 참고 목적으로만 작성되었으며, 의료 조언을 구성하지 않습니다. 약물 재창출 후보는 임상 검증을 거친 후에만 적용될 수 있습니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

