---
layout: default
title: Clofarabine
parent: 僅模型預測 (L5)
nav_order: 177
evidence_level: L5
indication_count: 10
---

# Clofarabine
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

# CLOFARABINE: 소아 급성 림프모구성 백혈병에서 골수성 백혈병으로

---

## 한 문장 요약

Clofarabine은 제2세대 퓨린 뉴클레오시드 유사체로, FDA에서 소아(1~21세) 재발/불응성 급성 림프모구성 백혈병(ALL) 치료에 가속승인을 받은 항종양제입니다.
TxGNN 모델은 **골수성 백혈병(Myeloid Leukemia)**에도 효과가 있을 수 있다고 예측하며,
현재 **50건의 임상시험**과 **20편의 문헌**이 이 방향을 강력히 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 미허가 (FDA 승인: 소아 재발/불응성 급성 림프모구성 백혈병) |
| 예측 신규 적응증 | 골수성 백혈병 (Myeloid Leukemia) |
| TxGNN 예측 점수 | 99.88% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✗ 미시판 (미허가) |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Clofarabine은 퓨린 뉴클레오시드 유사체로, 두 가지 핵심 기전을 통해 항종양 효과를 발휘합니다. ① 리보뉴클레오타이드 환원효소(RNR)를 억제하여 세포 내 dNTP 공급을 차단하고, ② DNA 중합효소 α를 직접 저해하여 DNA 복제를 종료시킵니다. 나아가 미토콘드리아 막 무결성을 교란해 세포 사멸(apoptosis)을 유도합니다. 이 이중 억제 기전은 전 세대 약물인 fludarabine 및 cladribine에 비해 효소 불활성화에 대한 내성이 높아 임상적으로 더 우수한 안정성을 제공합니다.

소아 ALL과 AML은 모두 고증식성 조혈 악성 세포에서 비롯된 혈액종양으로, 세포주기 의존적 DNA 합성 억제에 공통적으로 취약합니다. ALL에서 입증된 Clofarabine의 기전은 AML에도 동일하게 적용되며, 실제로 AML 세포에서 dNTP 고갈과 세포 사멸 유도가 확인됩니다. 두 질환 모두 빠른 분열 속도와 DNA 복구 기전 과부하라는 공통 취약점을 공유합니다.

이 타당성은 탄탄한 임상 증거로 뒷받침됩니다. Phase 3 무작위 임상시험(NCT01471444, n=256)에서 Fludarabine-Clofarabine 병용이 AML/MDS 이식 전처치에서 Fludarabine 단독 대비 효과를 평가했으며, Phase 1/2 무작위 연구(NCT01289457, n=282)에서는 CIA 방안(Clofarabine+Idarubicin+Cytarabine)이 AML 치료에서 FLAI 방안과 직접 비교되었습니다. 추가적으로 AML08 Phase 3 소아 연구(NCT00703820, n=324)와 CLARA 다기관 Phase 2 무작위 연구(NCT00932412, n=735)가 AML에서 Clofarabine의 임상적 역할을 다각도로 확인했습니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01471444](https://clinicaltrials.gov/study/NCT01471444) | Phase 3 | 완료 | 256 | AML/MDS에서 Fludarabine-Clofarabine+Busulfan vs. Fludarabine+Busulfan 이식 전처치 무작위 비교; 질환 조절 및 생존율 평가 (최고 등급 직접 근거) |
| [NCT01289457](https://clinicaltrials.gov/study/NCT01289457) | Phase 1/2 | 완료 | 282 | AML/고위험 MDS에서 CIA(Clofarabine+Idarubicin+Cytarabine) vs. FLAI 무작위 비교; 관해율 및 안전성 평가 |
| [NCT00703820](https://clinicaltrials.gov/study/NCT00703820) | Phase 3 | 완료 | 324 | 신규 AML 소아 환자에서 Clofarabine+Cytarabine vs. 표준 유도요법 무작위 비교; haploidentical NK세포 이식 병용 효과 탐색 |
| [NCT00932412](https://clinicaltrials.gov/study/NCT00932412) | Phase 2 | 완료 | 735 | 신규 AML 젊은 환자 대상 CLARA(Clofarabine+중용량 Cytarabine) vs. HDAC 공고요법 다기관 무작위 비교 |
| [NCT01794702](https://clinicaltrials.gov/study/NCT01794702) | Phase 1/2 | 완료 | 65 | 급성 백혈병에서 Decitabine 후 CIA 방안 투여; 최적 Clofarabine 용량 결정 및 AML 효능과 안전성 평가 |
| [NCT00863148](https://clinicaltrials.gov/study/NCT00863148) | Phase 2 | 완료 | 30 | 고위험 AML/MDS/ALL 성인 환자에서 CBT(Clofarabine+Busulfan IV+Thymoglobulin) 감소강도조건요법 다기관 비무작위 연구 |
| [NCT01295307](https://clinicaltrials.gov/study/NCT01295307) | Phase 2 | 완료 | 86 | 재발/불응성 AML에서 Clofarabine 구제요법; 이식 연결 가능 환자 도달률 및 독성 프로파일 평가 |
| [NCT02686593](https://clinicaltrials.gov/study/NCT02686593) | Phase 2 | 완료 | 50 | 재발/불응성 AML 1차 구제요법으로서 CLAM(Clofarabine+Cytarabine+Mitoxantrone); 높은 반응률 및 이식 연결 가능성 확인 |
| [NCT00088218](https://clinicaltrials.gov/study/NCT00088218) | Phase 2 | 완료 | 95 | 60세 이상 미치료 AML/고위험 MDS 환자에서 Clofarabine 단독 vs. Clofarabine+저용량 Ara-C 무작위 비교 |
| [NCT01457885](https://clinicaltrials.gov/study/NCT01457885) | Phase 2 | 완료 | 75 | 비관해 AML에서 CloBu4(Clofarabine+Busulfan×4) 골수파괴 이식 조건요법 다기관 단일군 연구 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [22957815](https://pubmed.ncbi.nlm.nih.gov/22957815/) | 2013 | Review | Leukemia & Lymphoma | AML에서 Clofarabine의 역할; RNR·DNA 중합효소 이중 억제 기전, 단독 및 병용요법(1차·구제) 효능 종합 검토 |
| [25457773](https://pubmed.ncbi.nlm.nih.gov/25457773/) | 2015 | Review | Crit Rev Oncol Hematol | 성인 AML에서 Clofarabine 단독·병용요법 개발 현황; 1차 및 2차 치료 프로토콜 체계적 검토 |
| [31246522](https://pubmed.ncbi.nlm.nih.gov/31246522/) | 2019 | RCT | J Clin Oncol | AML08 다기관 무작위 Phase 3; 소아 AML 유도요법에서 Clofarabine이 anthracycline/etoposide를 대체 가능함을 입증 |
| [32187883](https://pubmed.ncbi.nlm.nih.gov/32187883/) | 2020 | Clinical Trial | Cancer Medicine | R/R AML Phase 2: CLAM 방안(n=50) 높은 반응률과 이식 브리지 효과 확인; 표준 3+7 실패 환자 대상 |
| [31905904](https://pubmed.ncbi.nlm.nih.gov/31905904/) | 2019 | Clinical Study | Cancers | 젊은 AML 환자 CLARA 공고요법; SNP-array 기반 마이크로복합 핵형에서 재발자유생존(RFS) 유의한 개선 |
| [36336258](https://pubmed.ncbi.nlm.nih.gov/36336258/) | 2023 | Cohort | Transplant Cell Ther | 활성 골수성 악성 종양 환자에서 Clo/Bu4 골수파괴 조건요법; ≤70세에서 허용 가능한 독성 및 항백혈병 활성 확인 |
| [21182488](https://pubmed.ncbi.nlm.nih.gov/21182488/) | 2011 | Review | Curr Med Chem | AML 신규 약물(Clofarabine 포함) 약리 및 치료 활성 종합; 분자 표적 및 병용요법 전략 검토 |
| [19852733](https://pubmed.ncbi.nlm.nih.gov/19852733/) | 2009 | Review | Future Oncol | 성인 AML에서 Clofarabine; 단일제 활성, 병용요법 전략, 유도/공고 요법 미래 역할 전망 |
| [18756533](https://pubmed.ncbi.nlm.nih.gov/18756533/) | 2008 | Clinical Study | Cancer | R/R AML에서 Clofarabine+Cytarabine 및 Clofarabine+Idarubicin 병용요법 비교; 최적 병용 전략 탐색 |
| [31637757](https://pubmed.ncbi.nlm.nih.gov/31637757/) | 2020 | Clinical Study | Am J Hematol | AML 대상 Clofarabine+저용량 TBI 비골수파괴성 조건요법 Phase 1/2 다기관 연구; 6개월 재발률 개선 목표 확인 |

---

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (퓨린 뉴클레오시드 유사체) |
| 골수억제 위험 | 고위험 — 호중구감소증·혈소판감소증·빈혈이 거의 불가피하게 발생; AML 치료의 특성상 예상되는 독성 |
| 구토 유발성 등급 | 저~중등도 |
| 모니터링 항목 | CBC (분류 포함), 간기능 (ALT/AST/총빌리루빈), 신기능 (크레아티닌/eGFR), 전해질, 발열 및 감염 징후 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 (NIOSH 위험 약물 분류에 준하는 방호 조치 권장) |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
AML에서 Clofarabine의 효능을 지지하는 완료된 Phase 3 무작위 임상시험이 복수(NCT01471444 n=256, NCT00703820 n=324) 존재하고, 다수의 Phase 2 고품질 연구가 다양한 병용요법에서 활성을 확인하여 L1 수준의 근거가 확립되어 있습니다. 단, 한국 미허가 상태이므로 규제 절차 및 안전성 데이터 확보가 선행되어야 합니다.

**진행하려면 필요한 것:**
- 식약처(MFDS) 허가 절차 검토 및 수입 의약품 도입 가능성 확인 (현재 한국 미허가)
- FDA/EMA 허가사항(안전성 경고·금기·상호작용) 원문 확보 및 국문 검토
- DrugBank API를 통한 상세 작용 기전(MOA) 데이터 보완
- AML 분자유전학적 아형(FLT3, IDH1/2, NPM1, 핵형 등)별 반응 예측 데이터 검토
- 고령 환자·장기기능 저하 환자군에 대한 특화 모니터링 계획 수립
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

