---
layout: default
title: Dapsone
parent: 僅模型預測 (L5)
nav_order: 194
evidence_level: L5
indication_count: 1
---

# Dapsone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# DAPSONE: 나병에서 폐포자충증으로

## 한 문장 요약

Dapsone은 1940년대부터 사용된 항균·항염증 약물로, 나병(한센병) 치료의 핵심 성분으로 알려져 있으나 한국에서는 현재 허가되어 있지 않습니다.
TxGNN 모델은 **폐포자충증(Pneumocystosis)**에 효과가 있을 수 있다고 예측하며,
현재 **14건의 임상시험**과 **19편의 문헌**이 이 방향을 강력히 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 나병(한센병), 피부 염증 질환 (한국 미허가) |
| 예측 신규 적응증 | 폐포자충증 (Pneumocystosis) |
| TxGNN 예측 점수 | 99.73% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

공식 DrugBank MOA 데이터는 현재 수집되지 않았으나, 문헌에 따르면 Dapsone은 **dihydropteroate synthetase(DHPS)**를 억제하여 *Pneumocystis jirovecii*의 엽산 합성 경로를 차단하는 것으로 알려져 있습니다(PMID: 9675476). 이는 설폰아마이드계 항균제와 동일한 기전으로, trimethoprim과 병용 시 상승 효과를 나타내며 이것이 dapsone/TMP 병용 요법의 근거입니다.

나병(*Mycobacterium leprae* 감염)과 폐포자충증 모두 세포 매개 면역이 저하된 숙주에서 발생하는 기회감염입니다. Dapsone의 항균 및 항염증 이중 작용은 두 질환 모두에서 관련성을 가지며, 특히 HIV 감염자나 면역억제 치료를 받는 환자에서 *P. jirovecii*에 대한 강력한 항균 활성이 확인되어 있습니다.

TxGNN 예측 점수 99.73%는 이미 국제 진료 현장에서 확립된 임상적 사용을 모델이 정확히 포착한 결과로 해석됩니다. Dapsone을 이용한 PCP 예방 및 치료는 ECIL-5 가이드라인, CDC 권고안 등 주요 국제 지침에 2차 선택 옵션으로 이미 명시되어 있으며, 이는 한국에서의 허가 신청을 위한 충분한 국제 근거가 존재함을 시사합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00000640](https://clinicaltrials.gov/study/NCT00000640) | Phase 3 | 완료 | 290 | AIDS 환자의 경등~중등도 PCP에서 Dapsone/TMP vs 클린다마이신/프리마퀸 vs TMP/SMX 3방향 비교 |
| [NCT00000802](https://clinicaltrials.gov/study/NCT00000802) | Phase 3 | 완료 | 700 | TMP/설폰아마이드 불내성 HIV 감염자(CD4 ≤200)에서 Dapsone vs Atovaquone PCP 예방 효능·안전성 비교 |
| [NCT00000991](https://clinicaltrials.gov/study/NCT00000991) | Phase 3 | 완료 | 600 | CD4 <200 HIV 감염자에서 3가지 항-PCP 예방 요법(Dapsone 포함) + AZT 비교 |
| [NCT00001028](https://clinicaltrials.gov/study/NCT00001028) | Phase 3 | 완료 | 400 | TMP/설폰아마이드 불내성 고위험 HIV 감염자에서 에어로졸 펜타미딘 vs Dapsone PCP 예방 비교 |
| [NCT00002283](https://clinicaltrials.gov/study/NCT00002283) | N/A | 완료 | N/A | AIDS 환자 첫 번째 PCP 에피소드에서 Dapsone + trimethoprim vs TMP/SMX 치료 효과·부작용 비교 |
| [NCT00002043](https://clinicaltrials.gov/study/NCT00002043) | N/A | 완료 | N/A | 구강 아구창 또는 털 백반증 동반 ARC 환자에서 PCP 1차 예방용 Dapsone 100mg vs 50mg 용량 비교 |
| [NCT02550080](https://clinicaltrials.gov/study/NCT02550080) | Phase 4 | 불명 | 3,130 | Dapsone 투여 전 HLA-B\*1301 유전자 사전 스크리닝의 Dapsone 과민 증후군(DHS) 예방 임상 유용성 평가 |
| [NCT00002120](https://clinicaltrials.gov/study/NCT00002120) | Phase 1 | 완료 | 20 | AIDS 환자 중등~중증 PCP에서 Trimetrexate + Dapsone + Leucovorin vs TMP/SMX 안전성 및 약동학 평가 |
| [NCT04328688](https://clinicaltrials.gov/study/NCT04328688) | N/A | 완료 | 30 | 고형장기이식 후 PCP 환자에서 TMP-SMX 실패 시 Dapsone 등 대안 치료제 안전성 예비 조사 |
| [NCT05077150](https://clinicaltrials.gov/study/NCT05077150) | N/A | 완료 | 168 | 동종 조혈모세포이식(allo-HSCT) 후 폐포자충증 위험 인자·발생 시기·PCR 진단 활용 환자-대조군 연구 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [38583518](https://pubmed.ncbi.nlm.nih.gov/38583518/) | 2024 | Systematic Review/NMA | Clin Microbiol Infect | HIV 감염자 PCP 예방 요법 네트워크 메타분석: Dapsone 기반 요법의 효능·안전성을 TMP-SMX, 에어로졸 펜타미딘, Atovaquone과 체계적 비교 |
| [39732393](https://pubmed.ncbi.nlm.nih.gov/39732393/) | 2025 | Systematic Review/NMA | Clin Microbiol Infect | HIV 감염자 PCP 치료 요법 네트워크 메타분석: TMP-SMX 표준 치료 확인, Dapsone 포함 대안 요법 효능 체계적 검토 |
| [27550992](https://pubmed.ncbi.nlm.nih.gov/27550992/) | 2016 | 임상 가이드라인 | J Antimicrob Chemother | ECIL-5 가이드라인: 혈액암 및 HSCT 환자 PCP 예방에 TMP/SMX 1차 권고, Dapsone을 대안 약물로 명시(A-II 등급) |
| [33870843](https://pubmed.ncbi.nlm.nih.gov/33870843/) | 2021 | Review | Expert Opin Pharmacother | *P. jirovecii* 종합 검토: 위험 인자, 진단, 예방(Dapsone 2차 예방 옵션 포함), 치료 전략 |
| [8018144](https://pubmed.ncbi.nlm.nih.gov/8018144/) | 1993 | RCT | Am J Med | CD4 <250 HIV 감염자에서 에어로졸 펜타미딘 vs Dapsone의 PCP 및 톡소플라스마 뇌염 예방 무작위 비교 |
| [8605054](https://pubmed.ncbi.nlm.nih.gov/8605054/) | 1995 | 임상연구 | AIDS | HIV 감염자 PCP/톡소플라스마 1차 예방 3종 요법 비교: 에어로졸 펜타미딘, TMP/SMX, Dapsone-피리메타민의 효능·안전성·생존율 평가 |
| [9675476](https://pubmed.ncbi.nlm.nih.gov/9675476/) | 1998 | Review | Clin Infect Dis | Dapsone의 PCP 예방·치료 활용 종합 검토: DHPS 억제 기전, 약동학(경구 흡수율 70~80%), 임상 근거 요약 |
| [18971152](https://pubmed.ncbi.nlm.nih.gov/18971152/) | 2008 | Review | J Formos Med Assoc | PCP 개요(대만 관점): *P. jirovecii* 균류 재분류, 진단, 치료(TMP/SMX 1차, Dapsone 대안) |
| [19879509](https://pubmed.ncbi.nlm.nih.gov/19879509/) | 2009 | Review | Paediatr Respir Rev | 소아 PCP 종합 검토: 위험군(림프계 악성종양, HIV, 이식), 진단, TMP/SMX 1차·Dapsone 대안 치료 |
| [1727534](https://pubmed.ncbi.nlm.nih.gov/1727534/) | 1992 | Review | Med Clin North Am | 폐포자충증 종합 검토: HIV 시대 PCP의 예방·치료 가능성 확립, 예방 시작 시점 및 Dapsone 역할 기술 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. 한국에서 현재 미허가 약물이므로, FDA 또는 EMA 공식 처방 정보(prescribing information)를 통해 경고, 금기, 부작용 정보를 확인하시기 바랍니다.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
PCP 예방 및 치료에서 Dapsone의 효능은 4건의 완료된 Phase 3 임상시험과 국제 진료 가이드라인(ECIL-5)에 의해 **L1** 수준으로 확립되어 있습니다. 그러나 한국에서는 현재 미허가 상태이므로 식약처(MFDS) 허가 절차가 필요하며, 메트헤모글로빈혈증 및 Dapsone 과민 증후군(DHS) 등 임상적으로 중요한 안전성 이슈에 대한 모니터링 체계를 사전에 구축하여야 합니다.

**진행하려면 필요한 것:**
- 공식 작용 기전(MOA) 데이터 확보 (DrugBank API 조회 필요)
- 한국 식약처 허가 신청을 위한 국제 임상 데이터 패키지 구성 (Phase 3 RCT 결과 포함)
- 안전성 모니터링 계획 수립: CBC 및 메트헤모글로빈 수치 정기 모니터링, HLA-B\*1301 사전 스크리닝 도입 여부 검토
- 경고·금기·부작용 정보 별도 수집 (FDA/EMA 공식 문서 기반 한국어 정리)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

