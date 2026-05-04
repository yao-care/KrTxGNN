---
layout: default
title: Danazol
parent: 僅模型預測 (L5)
nav_order: 193
evidence_level: L5
indication_count: 10
---

# Danazol
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

# Danazol: 자궁내막증에서 유방 섬유낭종성 질환으로

## 한 문장 요약

Danazol은 17α-에티닐테스토스테론 유도체로, 자궁내막증과 유전성 혈관부종 치료에 사용되는 합성 스테로이드입니다.
TxGNN 모델은 **유방 섬유낭종성 질환(Breast Fibrocystic Disease)**에 효과가 있을 것으로 예측하며, 현재 **4건의 임상시험**과 **19편의 문헌**이 이 방향을 지지합니다.
Danazol은 미국 FDA에서 유방 섬유낭종성 질환에 이미 허가된 약물이나 한국에는 미상장 상태로, 국내 도입 가능성이 주목됩니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 자궁내막증 (국제 허가 기준) |
| 예측 신규 적응증 | 유방 섬유낭종성 질환 (Breast Fibrocystic Disease) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L2 |
| 한국 시판 현황 | ✗ 미상장 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용기전 데이터가 DrugBank에서 확보되지 않았습니다. 알려진 정보에 따르면, Danazol은 17α-에티닐테스토스테론에서 유래한 합성 스테로이드로, 강력한 항성선자극호르몬(antigonadotropin) 및 항에스트로겐 활성을 가집니다. FSH와 LH의 분비를 억제하여 난소의 에스트로겐 생성을 감소시키고, 안드로겐 수용체에 직접 결합하여 에스트로겐 의존성 조직의 이상 증식을 억제합니다.

유방 섬유낭종성 질환은 에스트로겐 우세 및 프로게스테론 결핍에 의해 유방 기질과 선포(acini)의 과증식이 초래되는 상태입니다. 자궁내막증과 유방 섬유낭종성 질환은 모두 에스트로겐 의존성 질환으로, Danazol의 항에스트로겐·항성선자극호르몬 기전이 두 적응증에 공통적으로 적용됩니다.

PMID 28649033은 Danazol이 섬유낭종성 유방 세포(Mcf10A)의 미토콘드리아 대사를 직접 변화시킨다는 세포 수준의 기전 근거를 제시하며, 단순 호르몬 억제 이상의 작용이 존재함을 시사합니다. Danazol은 미국 FDA에서 1980년대에 유방 섬유낭종성 질환 적응증을 취득하였으며, 이는 TxGNN 모델 예측의 타당성을 강력히 뒷받침합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00744276](https://clinicaltrials.gov/study/NCT00744276) | Phase 2 | 완료 | 60 | 유방 섬유낭종성 질환 관련 통증 환자에서 국소 도포 Danazol 3개 용량 vs. 위약의 안전성·적정 용량 탐색 (무작위 이중맹검 다기관 위약대조) |
| [NCT01105793](https://clinicaltrials.gov/study/NCT01105793) | Phase 2 | 완료 | 20 | 중등도~중증 주기성 유방통 환자에서 외용 FP1198(danazol 제제)의 안전성 및 초기 임상 활성 평가 (개방표지 다기관) |
| [NCT02002403](https://clinicaltrials.gov/study/NCT02002403) | Phase 2 | 완료 | 34 | 저용량 경구 DMI-5207(danazol)의 당뇨병성 황반부종 효능·안전성 평가; 저용량 Danazol 제형 가능성 탐색에 참고 (무작위 이중맹검 위약대조) |
| [NCT04873102](https://clinicaltrials.gov/study/NCT04873102) | Phase 2 | 모집 중 | 10 | 간경변 환자의 혈구감소증에서 Danazol 600mg/일 안전성·효능 평가 (섬유낭종성 질환과 직접 관련 없음, 참고용) |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [3074777](https://pubmed.ncbi.nlm.nih.gov/3074777/) | 1988 | RCT | Aust NZ J Obstet Gynaecol | Danazol 200mg 1일 2회 vs. 위약 무작위 이중맹검(n=80); 유방 통증·압통·결절·낭종 모두 유의미하게 개선 |
| [6594009](https://pubmed.ncbi.nlm.nih.gov/6594009/) | 1984 | 임상 시리즈 | Acta Obstet Gynecol Scand (Suppl) | 중증 섬유낭종성 유방 질환·주기성 유방통 환자 대상 Danazol 치료 및 장기 추적 관찰 (Hjørring 프로젝트) |
| [7386553](https://pubmed.ncbi.nlm.nih.gov/7386553/) | 1980 | 임상 연구 | Am J Obstet Gynecol | 양성 유방질환 130명에 Danazol 100~400mg/일 투여; 약 2/3에서 결절 소실, 48개월 추적 |
| [28649033](https://pubmed.ncbi.nlm.nih.gov/28649033/) | 2017 | 기초과학 | Breast | Danazol이 섬유낭종성 유방 세포(Mcf10A)의 미토콘드리아 대사를 직접 변화시킴 — 세포 기전의 직접 근거 |
| [7041729](https://pubmed.ncbi.nlm.nih.gov/7041729/) | 1982 | 약물 리뷰 | Ann Intern Med | Danazol 작용기전 및 낭종성 유방 질환에 대한 FDA 승인 배경 검토 |
| [3511705](https://pubmed.ncbi.nlm.nih.gov/3511705/) | 1986 | 리뷰 | Am J Obstet Gynecol | 섬유낭종성 유방 질환 병태생리·임상 양상 및 Danazol 포함 치료 전략 |
| [3314435](https://pubmed.ncbi.nlm.nih.gov/3314435/) | 1987 | 리뷰 | Am Fam Physician | 섬유낭종성 유방 질환 관리 지침; methylxanthine 감소 및 Danazol 치료 권고 |
| [16444894](https://pubmed.ncbi.nlm.nih.gov/16444894/) | 2005 | 리뷰 | J Reprod Med | 유방통(mastalgia) 관리 종합 검토; Danazol이 효과적 치료 선택지로 포함 |
| [2404118](https://pubmed.ncbi.nlm.nih.gov/2404118/) | 1990 | 리뷰 | J Reprod Med | 섬유낭종성 유방 질환 호르몬 치료; Danazol 효능 및 다수 임상 연구 결과 요약 |
| [395520](https://pubmed.ncbi.nlm.nih.gov/395520/) | 1979 | 초기 임상시험 | Postgrad Med J | 섬유낭종성 유방 질환 임상 양상과 Danazol 치료의 초기 임상 경험 보고 |

---

## 한국 시판 정보

한국 식품의약품안전처(MFDS) 등록 허가 이력이 없습니다 (허가증 0건).

> 참고: Danazol은 미국 FDA에서 자궁내막증, 유방 섬유낭종성 질환, 유전성 혈관부종 치료에 허가된 약물입니다. 한국 내 상장을 위해서는 MFDS 허가 신청 절차가 필요합니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> **문헌에서 확인된 약물 상호작용 주의 사항:** PMID 18691993에서 Danazol 600mg/일과 Lovastatin 40mg/일 병용 투여 시 횡문근융해증(rhabdomyolysis) 및 췌장염이 보고되었습니다. 스타틴 계열 약물과의 병용 시 근육 증상 모니터링이 필요합니다.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
유방 섬유낭종성 질환에서의 Danazol 효능은 미국 FDA 허가 및 완료된 Phase 2 RCT(NCT00744276)를 포함한 다수의 임상 근거로 확립되어 있어, 한국 내 도입을 위한 근거 수준이 충분합니다. 다만 한국 MFDS 허가 자료가 전무하여 규제 절차 준비가 선행되어야 합니다.

**진행하려면 필요한 것:**
- 상세한 작용기전(MOA) 데이터 확보 (DrugBank API 조회)
- MFDS 허가 신청을 위한 FDA/국제 허가 자료 및 핵심 임상 데이터 정리
- TFDA 仿單 PDF 기반 경고·금기 사항 수집 (현재 DG001 데이터 갭)
- 한국인 대상 브릿지 스터디 또는 실사용 데이터 검토 가능성 평가
- 병용 금기 약물(스타틴 계열 등) 약물 상호작용 데이터 공식 수집
- 투여 경로별(경구/국소) 안전성 모니터링 계획 수립
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

