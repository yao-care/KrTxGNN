---
layout: default
title: Docetaxel
parent: 僅模型預測 (L5)
nav_order: 226
evidence_level: L5
indication_count: 10
---

# Docetaxel
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

# Docetaxel: 국내 미등록에서 여성 유방암으로

## 한 문장 요약

> Docetaxel은 미세소관 안정화 기전을 통해 암세포의 세포 분열을 억제하는 탁산(taxane) 계열 세포독성 항암제로, 국제적으로 다양한 고형암 치료에 광범위하게 사용되고 있으나 현재 국내에는 허가된 제품이 없습니다.
> TxGNN 모델은 **여성 유방암(Female Breast Carcinoma)**에 효과가 있을 것으로 예측하며,
> 현재 **50건의 임상시험**과 **20편의 문헌**이 이 방향을 강력히 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 국내 허가 없음 |
| 예측 신규 적응증 | 여성 유방암 (Female Breast Carcinoma) |
| TxGNN 예측 점수 | 99.90% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✗ 미등록 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Docetaxel은 탁산(taxane) 계열의 준합성 세포독성 항암제입니다. 핵심 작용 기전은 **미세소관(microtubule) 안정화**로, 미세소관 중합체의 해중합(depolymerization)을 억제하여 세포 주기를 G2/M기에 정지시키고 세포사멸(apoptosis)을 유도합니다. 이는 빠르게 증식하는 암세포에서 특히 강력하게 발휘되며, Paclitaxel에 비해 미세소관 결합 친화도가 약 2배 높아 세포독성이 더 강한 것으로 알려져 있습니다.

여성 유방암 세포는 증식 지수가 높아 미세소관 표적 약물에 대한 감수성이 높습니다. 이 기전적 연관성은 조기 유방암 및 전이성 유방암 모두에서 다수의 대규모 Phase 3 RCT를 통해 직접 검증되었습니다. EC→Docetaxel 순차 보조요법, TAC(Docetaxel+Doxorubicin+Cyclophosphamide) 3제 방안, TC(Docetaxel+Cyclophosphamide) 방안 등이 국제 표준 치료로 확립되어 있으며, HER2 양성 유방암에서는 TCH(Docetaxel+Carboplatin+Trastuzumab) 방안이 핵심 표준 요법으로 사용됩니다.

TxGNN 예측 점수 99.90%는 방대한 지식 그래프 기반 분석 결과로, n=2,778의 대규모 Phase 3 RCT를 포함한 50건의 임상시험과 20편의 고품질 문헌이 이를 강력히 뒷받침합니다. 근거 수준 L1로 임상적 타당성이 매우 높습니다. 단, 골수억제, 말초 신경병증, 림프부종 등 주요 독성(PMID 27997437)에 대한 관리 계획이 반드시 필요합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00003519](https://clinicaltrials.gov/study/NCT00003519) | Phase 3 | 완료 | 2,778 | 림프절 양성 또는 고위험 림프절 음성 유방암 보조치료에서 AT(Doxorubicin+Docetaxel) vs AC(Doxorubicin+Cyclophosphamide) 비교; 대규모 RCT로 Docetaxel 병용 방안 효능 직접 검증 |
| [NCT00129935](https://clinicaltrials.gov/study/NCT00129935) | Phase 3 | 완료 | 1,384 | HER2 음성 림프절 양성 유방암에서 EC→Docetaxel vs ET→Capecitabine 보조화학요법 직접 비교; Docetaxel 보조치료 효능 및 안전성 검증 |
| [NCT01354522](https://clinicaltrials.gov/study/NCT01354522) | Phase 3 | 완료 | 204 | HER2 음성 고위험 유방암에서 TAC(Docetaxel+Doxorubicin+Cyclophosphamide) vs TCX(+Capecitabine) 보조화학요법 비교 |
| [NCT00047255](https://clinicaltrials.gov/study/NCT00047255) | Phase 3 | 완료 | 263 | HER2 양성 진행성 유방암 1차 치료에서 Docetaxel+Trastuzumab vs Docetaxel+Carboplatin+Trastuzumab 효능 비교 |
| [NCT00005963](https://clinicaltrials.gov/study/NCT00005963) | Phase 2 | 완료 | 53 | 전이성 유방암 1차 치료로 Docetaxel+Carboplatin 병용 효능 및 안전성 평가 |
| [NCT00003953](https://clinicaltrials.gov/study/NCT00003953) | Phase 2 | 완료 | 39 | Stage II-IIIB 유방암에서 수술 전 용량 집약적 Doxorubicin→Docetaxel 신보조화학요법; 반응률 직접 평가 |
| [NCT02400567](https://clinicaltrials.gov/study/NCT02400567) | Phase 2 | 완료 | 125 | PAM50 기반 저/중간위험 Luminal 유방암에서 FEC→Docetaxel vs Letrozole+Palbociclib 신보조요법 무작위 비교 |
| [NCT00994968](https://clinicaltrials.gov/study/NCT00994968) | Phase 2 | 불명 | 49 | 유방암 신보조화학요법: AC 후 Docetaxel+S-1 순차 투여; 종양 축소 및 조직학적 반응 평가 |
| [NCT03076372](https://clinicaltrials.gov/study/NCT03076372) | Phase 1 | 불명 | 34 | EphA2 수용체 표적 Docetaxel 리포솜 나노제형(MM-310) 실체 종양(유방암 포함) 안전성 및 예비 효능 평가 |
| [NCT00063934](https://clinicaltrials.gov/study/NCT00063934) | Phase 1/2 | 종료됨 | 31 | 전이성/국소 진행성 유방암에서 Bcl-2 반의센스 G3139+Doxorubicin+Docetaxel 삼중 방안; Docetaxel이 핵심 화학요법 성분으로 포함 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [7595719](https://pubmed.ncbi.nlm.nih.gov/7595719/) | 1995 | 종합 리뷰 | J Clin Oncol | Docetaxel(Taxotere)의 전임상 및 임상 프로파일 종합 검토; 탁산 계열 항암제 근거 확립 |
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | Phase 3 RCT | J Clin Oncol | TC6(Docetaxel+Cyclophosphamide) vs TaxAC 방안 비교 (ABC Trials); 조기 유방암 보조치료 효능 비교 평가 |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | 리뷰 | Drug Ther Bull | Paclitaxel 및 Docetaxel의 유방암·난소암 임상 활성 검토; 탁산 계열 초기 임상 근거 |
| [26874836](https://pubmed.ncbi.nlm.nih.gov/26874836/) | 2017 | Phase 2 시험 | Breast Cancer | HER2+ 유방암에서 Docetaxel+Cyclophosphamide+Trastuzumab(HER-TC) 신보조화학요법 효능 및 내약성 평가 |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | 코호트 연구 | Anti-Cancer Drugs | Docetaxel 기반 화학요법과 유방암 관련 림프부종 연관성 평가; 주요 독성 모니터링 근거 제공 |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | Phase 1/2 시험 | Cancer | 국소 진행성/전이성 유방암 1차 치료로 Capecitabine+Docetaxel+Epirubicin(TEX) 3제 병용 효능 및 안전성 |
| [9364543](https://pubmed.ncbi.nlm.nih.gov/9364543/) | 1997 | Phase 2 시험 | Oncology | 전이성 유방암에서 Docetaxel+Vinorelbine 병용 임상 활성 보고; Docetaxel 단독 및 병용 효과 |
| [19856651](https://pubmed.ncbi.nlm.nih.gov/19856651/) | 2009 | Phase 1/2 시험 | Tumori | 앤트라사이클린 전처치 전이성 유방암에서 Docetaxel+Gemcitabine 주간 투여 용량 발굴 연구 |
| [19755993](https://pubmed.ncbi.nlm.nih.gov/19755993/) | 2009 | 중개 연구 | Br J Cancer | HER2+ 유방암에서 Trastuzumab+Docetaxel 기반 치료의 완전 병리학적 반응(pCR) 예측 바이오마커 분석 |
| [15585076](https://pubmed.ncbi.nlm.nih.gov/15585076/) | 2004 | Phase 2 시험 | Clin Breast Cancer | 국소 진행성 유방암에서 Docetaxel+Cisplatin 신보조화학요법 효능 평가; 완전 병리학적 반응률 보고 |

---

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (Taxane 계열; 미세소관 안정화 기전) |
| 골수억제 위험 | 고도 (호중구감소증이 주요 용량 제한 독성; 발열성 호중구감소증 위험 높음 → G-CSF 예방 투여 권장) |
| 구토 유발성 등급 | 저~중등도 (단독 투여 기준; 앤트라사이클린 병용 시 등급 상승 가능) |
| 모니터링 항목 | CBC (분류 포함), 간기능(ALT/AST/총 빌리루빈), 신기능, 말초 신경 기능, 체액 저류/부종, 과민반응 |
| 취급 방호 | 세포독성 약물 취급 지침 준수 필요 (준비·투여·폐기 시 방호 장비 착용) |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
여성 유방암에 대한 Docetaxel의 효능은 n=2,778을 포함한 다수의 대규모 Phase 3 RCT를 통해 국제적으로 확고히 검증되어 있으며, EC→T, TAC, TC, TCH 등 국제 표준 치료에 이미 포함되어 있습니다. 근거 수준 L1로 임상적 활용 타당성이 매우 높으나, 국내 미등록 상태이므로 정규 허가 절차가 선행되어야 합니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 상세 데이터 및 DrugBank ID 확보
- 식품의약품안전처(MFDS) 국내 허가 절차 검토 (신약 허가 신청 서류 준비)
- 국내 허가사항(첨부문서) 확보 및 경고·금기 사항 상세 검토
- 골수억제, 림프부종, 말초 신경병증에 대한 한국인 환자 모니터링 프로토콜 수립
- 약물 상호작용(DDI) 데이터베이스 재조회 및 주요 상호작용 목록화
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

