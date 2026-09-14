---
layout: default
title: Trabectedin
parent: 僅模型預測 (L5)
nav_order: 689
evidence_level: L5
indication_count: 1
---

# Trabectedin
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

# Trabectedin: 연조직육종·난소암에서 유방암으로

## 한 문장 요약

> Trabectedin은 해면동물유래 항암제로, 해외에서는 연조직육종 2차 치료제 및 백금 민감성 재발 난소암(PLD 병용)으로 사용되어 왔으나 **한국에는 아직 허가되지 않았습니다**.
> TxGNN 모델은 **여성 유방암(Female Breast Carcinoma)**에 효과가 있을 수 있다고 예측하며,
> 현재 **2건의 임상시험**과 **20편 이상의 문헌**(그중 다수가 유방암 특이적 Phase 1/2 임상 데이터 포함)이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 연조직육종(2차 치료), 백금 민감성 재발 난소암(PLD 병용) — *해외 승인, 한국 미승인* |
| 예측 신규 적응증 | 여성 유방암 (Female Breast Carcinoma) |
| TxGNN 예측 점수 | 99.73% |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미상영 (미승인) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Trabectedin은 DNA minor groove alkylating agent로, transcription-coupled nucleotide excision repair(TC-NER)를 억제하고 상동재조합(homologous recombination) 관련 전사 조절을 교란시켜 **BRCA1/2 결손 또는 HR-deficient 종양세포에 선택적 세포독성**을 나타냅니다.

이 기전은 이미 승인된 적응증인 연조직육종, 백금 민감성 재발 난소암과 동일한 기전적 기반을 공유하며, HR-deficiency는 유방암(특히 BRCA1/2 생식세포 변이 보유 유방암, 삼중음성유방암 일부)에서도 흔히 관찰되는 특성입니다. 실제로 다수의 문헌에서 BRCA1/2 변이 보유 전이성 유방암 환자를 대상으로 한 Phase 2 임상시험 결과가 보고되어 있어, 기전 연장 추론을 넘어 일부 임상적 근거까지 확보된 상태입니다.

다만 유방암에 특이적인 수용체·경로 표적 근거는 아직 명확하지 않으며, 현재까지의 근거는 BRCA/HR-deficiency라는 공통 분모를 통한 간접적 연결에 가깝습니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00786838](https://clinicaltrials.gov/study/NCT00786838) | Phase 2 | 완료 | 76 | 진행성 고형암 환자에서 trabectedin의 QT/QTc 간격 영향을 평가한 단일맹검·다기관·위약대조 시험 |
| [NCT03470805](https://clinicaltrials.gov/study/NCT03470805) | Phase 2 | 완료 | 9 | 재발성 난소암에서 trabectedin-PLD 반응 후 olaparib 유지요법 평가 — trabectedin은 유도치료 단계로만 포함되어 간접적 근거 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [27266804](https://pubmed.ncbi.nlm.nih.gov/27266804/) | 2016 | RCT (Phase 2) | Clin Breast Cancer | 호르몬수용체 양성/HER2 음성 진행성 유방암에서 XPG 유전자 발현에 따른 trabectedin 효능 평가 |
| [24692579](https://pubmed.ncbi.nlm.nih.gov/24692579/) | 2014 | Phase 2 (국제) | Ann Oncol | BRCA1/2 생식세포 변이 전이성 유방암 환자 대상 최초 class Phase 2 시험, 효능·안전성 확인 |
| [25239225](https://pubmed.ncbi.nlm.nih.gov/25239225/) | 2014 | 다기관 무작위 Phase 2 | Clin Breast Cancer | 안트라사이클린·탁산 치료 후 진행성 유방암에서 두 가지 투여요법 비교 |
| [19114300](https://pubmed.ncbi.nlm.nih.gov/19114300/) | 2009 | Phase 1 (RCT) | Eur J Cancer | 진행성 연조직육종·유방암에서 trabectedin+doxorubicin 병용 약동학 연구 |
| [27710871](https://pubmed.ncbi.nlm.nih.gov/27710871/) | 2016 | Review | Cancer Treat Rev | BRCA 결손 환자에서 화학요법 옵션으로서의 trabectedin 정리 |
| [26592307](https://pubmed.ncbi.nlm.nih.gov/26592307/) | 2016 | Review | Expert Opin Investig Drugs | 유방암 치료제로서의 trabectedin 전반적 리뷰, 종양미세환경 조절 기전 포함 |
| [33185631](https://pubmed.ncbi.nlm.nih.gov/33185631/) | 2020 | Review | Drugs Today | 난소암·유방암·연조직육종에서의 trabectedin 활용 정리 |
| [23792433](https://pubmed.ncbi.nlm.nih.gov/23792433/) | 2013 | Preclinical | Toxicol Lett | MCF-7(HER2-/ER+), MDA-MB-453(HER2+/ER-) 유방암 세포주에서 trabectedin의 아포토시스 유도 확인 |
| [24941346](https://pubmed.ncbi.nlm.nih.gov/24941346/) | 2014 | Preclinical | Eur Cytokine Netw | 인간 유방암 세포 및 HUVEC에서 trabectedin의 항혈관신생 효과 확인 |
| [39777457](https://pubmed.ncbi.nlm.nih.gov/39777457/) | 2025 | Preclinical | Cancer Immunol Res | 삼중음성유방암(TNBC)에서 IL-12와 병용 시 골수유래억제세포 감소를 통한 항종양 효과 증대 |

---

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 화학요법제 (해양유래 tetrahydroisoquinoline alkaloid, DNA alkylating agent) |
| 골수억제 위험 | 중등도~고도 — 문헌 보고에 따르면 Grade 3-4 호중구감소증 약 50%, 혈소판감소증 약 20%에서 관찰 |
| 구토 유발성 등급 | 문헌상 명확한 등급 데이터 없음 — 허가사항 참조 필요 |
| 모니터링 항목 | CBC(호중구·혈소판 포함), 간기능(간독성 보고 있음), 신기능 |
| 취급 방호 | 세포독성 항암제 취급 규정(개인보호구, 폐기물 처리 등) 준수 필요 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. 현재 한국 내 허가 자료가 없어 국내 경고·금기·약물상호작용 정보를 확인할 수 없습니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
BRCA/HR-deficiency 기전을 매개로 한 유방암 적용 근거는 Phase 2 임상시험 다수(특히 BRCA1/2 변이 보유 전이성 유방암 대상)로 뒷받침되어 L2 수준의 근거를 확보했습니다. 그러나 한국에는 현재 허가·시판 이력이 전혀 없고, 사용설명서(경고·금기) 데이터가 완전히 결측되어 있어 S1 안전성 초기 평가 진입이 불가능한 **Blocking 등급 데이터 갭**이 존재합니다.

**진행하려면 필요한 것:**
- 규제기관 공식 사용설명서(PI) 확보 및 경고·금기·약물상호작용 정보 보완 (Blocking)
- 한국 내 허가 여부 및 향후 허가 신청 전략 검토
- 유방암 특이적 바이오마커(BRCA1/2, HR-deficiency) 기반 환자 선별 기준 정립
- Phase 3 수준의 무작위 대조시험 데이터 확보 (현재 Phase 2 수준에 머물러 있음)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

