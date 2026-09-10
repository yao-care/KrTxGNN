---
layout: default
title: Olaparib
parent: 僅模型預測 (L5)
nav_order: 518
evidence_level: L5
indication_count: 1
---

# Olaparib
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

# Olaparib: 난소암에서 유방암으로

## 한 문장 요약

Olaparib은 PARP1/2 억제제로, 임상시험 근거(NCT05078671)에 따르면 원래 백금 감수성 재발성 BRCA 변이 난소암·나팔관암·복막암의 유지요법으로 개발되었습니다.
TxGNN 모델은 **유방암(Female Breast Carcinoma)**에도 효과가 있을 것으로 예측하며,
현재 **50건 이상의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다. 특히 OlympiAD, OlympiA 등 다수의 완료된 Phase 3 무작위대조시험이 BRCA 변이 유방암에서의 효능을 이미 입증했습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 난소암 (BRCA 변이, 백금 감수성 재발성 유지요법) — 임상시험 요약(NCT05078671) 근거 |
| 예측 신규 적응증 | 유방암 (Female Breast Carcinoma) |
| TxGNN 예측 점수 | 99.09% |
| 근거 수준 | L1 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Olaparib은 PARP1/2(poly ADP-ribose polymerase) 억제제로, 단일가닥 DNA 손상 복구를 차단하고 복제분기점 붕괴를 유도합니다. BRCA1/2 생식세포계열 돌연변이로 상동재조합 복구(HRD)에 결함이 있는 종양세포에서는 이 억제 작용이 "합성치사(synthetic lethality)" 효과로 이어져 선택적으로 암세포를 사멸시킵니다.

BRCA1/2 변이는 난소암뿐 아니라 유방암의 대표적 발암 원인 중 하나이므로, 두 암종은 동일한 기전적 취약점을 공유합니다. 따라서 난소암에서 검증된 PARP 억제 기전이 BRCA 변이 유방암에도 직접 적용 가능하며, 이는 간접 추론이 아니라 기전상 직접적인 연관성입니다.

실제로 이 적응증은 이미 FDA·EMA에서 Lynparza®로 승인된 상태이며, Evidence Pack상 "미시판"은 한국 시장 내 미출시를 의미할 뿐 전 세계적 미승인을 뜻하지 않습니다. 이는 TxGNN 예측의 타당성을 뒷받침하는 강력한 정황입니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02282020](https://clinicaltrials.gov/study/NCT02282020) | Phase 3 | 완료 | 266 | gBRCA 변이 환자 대상 olaparib vs 의사 선택 화학요법 비교, 핵심 등록 근거 시험 |
| [NCT04330040](https://clinicaltrials.gov/study/NCT04330040) | Phase 4 | 완료 | 202 | 인도 환자 대상, 재발성 난소암 및 gBRCA1/2 변이 전이성 유방암에서 olaparib 실사용 데이터 |
| [NCT06580314](https://clinicaltrials.gov/study/NCT06580314) | Phase 3 | 모집 중 | 880 | BRCA1/2 변이·HRD+ 난소암에서 olaparib 유지요법 1년 vs 2년 비교(±bevacizumab) |
| [NCT01445418](https://clinicaltrials.gov/study/NCT01445418) | Phase 1 | 완료 | 103 | BRCA1/2 변이 유방암·난소암 및 삼중음성유방암에서 olaparib+carboplatin 병용 |
| [NCT01237067](https://clinicaltrials.gov/study/NCT01237067) | Phase 1 | 완료 | 77 | 유방암·난소암·자궁암·자궁경부암 등 여성암에서 olaparib+carboplatin PK/PD 연구 |
| [NCT02264678](https://clinicaltrials.gov/study/NCT02264678) | Phase 1/2 | 진행 중(모집 종료) | 357 | 고형암 대상 ceralasertib+olaparib 병용 안전성/PK 대규모 연구 |
| [NCT05498155](https://clinicaltrials.gov/study/NCT05498155) | Phase 2 | 진행 중(모집 종료) | 50 | BRCA 변이, HER2 음성 조기 유방암에서 olaparib 단독 및 durvalumab 병용 신보조요법 |
| [NCT06201234](https://clinicaltrials.gov/study/NCT06201234) | Phase 2 | 모집 중 | 176 | HR양성·HER2음성·gBRCA1/2 변이 진행성/전이성 유방암에서 olaparib+elacestrant 병용 |
| [NCT05358639](https://clinicaltrials.gov/study/NCT05358639) | Phase 1 | 진행 중(모집 종료) | 36 | 고등급 장액성 난소암 및 삼중음성유방암에서 olaparib+navitoclax 병용 |
| [NCT02418624](https://clinicaltrials.gov/study/NCT02418624) | Phase 1 | 완료 | 25 | BRCA1/2 변이 HER2음성 전이성 유방암 1차 치료에서 carboplatin-olaparib vs capecitabine |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | RCT | NEJM | OlympiA: BRCA1/2 변이 조기 유방암 보조요법에서 olaparib 1년 투여, 무침습질병생존율 유의 개선 |
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | RCT | Annals of Oncology | OlympiA 전체생존 분석, 고위험 조기 유방암 보조 olaparib 효과 확인 |
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | RCT | NEJM | OlympiAD: 생식세포 BRCA 변이 전이성 유방암에서 olaparib 항종양 활성 입증 |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | RCT | Annals of Oncology | OlympiAD 최종 전체생존 및 내약성 결과 |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | RCT | Eur J Cancer | OlympiAD 연장 추적관찰, 전체생존 및 안전성 재확인 |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | Phase 2 단일군 | J Clin Oncol | TBCRC 048: 체세포 BRCA1/2 및 기타 HR 관련 유전자 변이 전이성 유방암에서 olaparib 반응 평가 |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | Phase 2 병용 | Cancer Cell | I-SPY2: durvalumab+olaparib+paclitaxel 병용이 HER2음성 고위험 유방암 병리학적완전반응률 향상 |
| [38588696](https://pubmed.ncbi.nlm.nih.gov/38588696/) | 2024 | RCT | Nature | PARTNER: 생식세포 BRCA 야생형 삼중음성유방암 신보조요법에서 olaparib+화학요법 병용 |
| [33710534](https://pubmed.ncbi.nlm.nih.gov/33710534/) | 2021 | Review | Targeted Oncology | 유방암 치료에서 PARP 억제제(olaparib, talazoparib) 전반 개관 |
| [39791278](https://pubmed.ncbi.nlm.nih.gov/39791278/) | 2025 | Review | CA Cancer J Clin | PARP 억제제(olaparib 등)의 범종양(pan-tumor) 역할에 대한 종합 리뷰 |

---

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (PARP1/2 억제제, 합성치사 기전) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
OlympiAD, OlympiA 등 완료된 Phase 3 무작위대조시험이 BRCA 변이 유방암에서 olaparib의 효능과 안전성을 직접 입증했으며(근거 수준 L1), 해당 적응증은 이미 FDA·EMA에서 승인되어 있습니다. 다만 한국 내 허가·안전성 데이터가 없어 즉시 진행보다는 안전장치를 갖춘 진행이 적절합니다.

**진행하려면 필요한 것:**
- 한국 식약처(MFDS) 허가사항 및 경고·금기 정보 확보 (DG001, Blocking)
- DrugBank 등에서 상세 작용기전(MOA) 데이터 확인 (DG002, High)
- 한국 내 허가 신청 현황 및 시판 계획 파악
- 국내 환자 대상 약물상호작용 및 골수억제 모니터링 계획 수립
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

