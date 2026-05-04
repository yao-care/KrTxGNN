---
layout: default
title: Apixaban
parent: 僅模型預測 (L5)
nav_order: 76
evidence_level: L5
indication_count: 10
---

# Apixaban
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

# Apixaban: 심방세동/정맥혈전색전증에서 폐동맥고혈압으로

## 한 문장 요약

Apixaban은 비판막성 심방세동 환자의 뇌졸중 예방 및 정맥혈전색전증(VTE) 치료·예방에 사용되는 선택적 Factor Xa 억제제(직접 경구 항응고제)입니다.
TxGNN 모델은 총 10개의 신규 적응증을 예측하였으며, 근거 수준이 가장 높은 **폐동맥고혈압(Pulmonary Hypertension)**에서는 Phase 2 RCT 프로토콜을 포함한 **8건의 임상시험**과 **19편의 문헌**이 Apixaban의 치료 가능성을 지지합니다.
반면, TxGNN 예측 상위 3개를 차지한 편두통 계열 적응증(Rank 1·2·5)에는 Apixaban 투여 후 증상 악화를 보고한 안전성 신호가 존재하므로 별도 주의가 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 비판막성 심방세동 뇌졸중 예방, 심부정맥혈전증(DVT) 및 폐색전증(PE) 치료·예방 |
| 최우선 신규 적응증 | 폐동맥고혈압 (Pulmonary Hypertension, Rank 8) |
| TxGNN 예측 점수 | 98.13% (폐동맥고혈압) / 99.02% (편두통 Rank 1) |
| 근거 수준 | L3 (폐동맥고혈압 기준) |
| 한국 시판 현황 | ✗ 미상장 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails (폐동맥고혈압) |

> **본 보고서는 10개 예측 적응증을 다루는 다중 후보 평가입니다.** TxGNN 점수 최상위는 편두통(Rank 1)이지만, 임상 근거 수준이 가장 높은 폐동맥고혈압(Rank 8)을 주요 검토 대상으로 삼습니다.

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 Evidence Pack에 포함되어 있지 않습니다. 공지된 정보에 따르면, Apixaban은 혈액 응고 과정에서 활성화 Factor Xa(FXa)를 직접 억제하여 트롬빈 생성과 혈전 형성을 차단하는 직접 경구 항응고제(DOAC)이며, 기존 비타민K 길항제(와파린)의 주요 대안으로 자리잡고 있습니다.

폐동맥고혈압(PH)과 Apixaban의 연관성은 세 가지 기전 층위로 설명됩니다. 첫째, **만성혈전색전성 폐고혈압(CTEPH)** 아형에서는 항응고 치료가 표준 요법의 핵심으로, 실제 CTEPH 환자 50명을 대상으로 FXa 억제제의 anti-Xa 활성을 확인한 코호트 연구(PMID 39468095)를 비롯해 DOACs가 VKA를 대체하는 임상 근거가 축적되고 있습니다. 둘째, **전신경화증 관련 폐동맥고혈압(PAH-SSc)**에서는 FXa 억제 → 트롬빈 생성 감소 → PAR-1/PAR-4 비활성화 → 혈관 평활근 증식·리모델링 억제의 기전 경로가 제안되며, 이를 직접 검증하는 Phase 2 RCT 프로토콜(SPHInX 연구, PMID 27932335)이 설계되었습니다. 셋째, 원위 폐정맥 혈전에 대해 Apixaban이 성공적으로 혈전을 소실시킨 증례(PMID 40959672)도 보고되어 있습니다.

**류마티스 관절염(RA, Rank 4)** 역시 주목할 만한 연구 과제입니다. 쥐 모델에서 Apixaban이 FXa → JAK2/STAT3 및 MAPK 경로 차단을 통해 활막 세포 증식을 억제하는 항관절염 효과를 나타냈다는 전임상 기전 연구(PMID 32141012)가 있으나, 현재 임상시험 근거는 전무합니다.

---

## 임상시험 근거

(폐동맥고혈압 기준)

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03610217](https://clinicaltrials.gov/study/NCT03610217) | N/A | 상태 불명 | 400 | 시스템성 경화증(SSc) 실용 임상시험 — SSc는 PAH의 가장 흔한 속발 원인(~15%)으로, Apixaban 포함 항응고 전략 평가. 결과 데이터 확인 필요 |
| [NCT06370273](https://clinicaltrials.gov/study/NCT06370273) | Phase 3 | 모집 중 | 10,044 | TiLLI: 하지 고정 환자 VTE 약물 예방 비교 — PE 예방을 통한 CTEPH 진행 억제의 간접 근거 |
| [NCT02942407](https://clinicaltrials.gov/study/NCT02942407) | Phase 4 | 완료 | 154 | RENAL-AF: 혈액투석 합병 AF 환자에서 Apixaban vs 와파린 무작위 배정 — 신부전 합병 시 안전성 프로파일 |
| [NCT04234698](https://clinicaltrials.gov/study/NCT04234698) | N/A | 완료 | 2,076 | 콜롬비아 NVAF 환자 경구 항응고제 사용 패턴 관찰 연구 |
| [NCT05838664](https://clinicaltrials.gov/study/NCT05838664) | N/A | 완료 | 2,140,403 | SIFNOS: 프랑스 대규모 AF 후향 코호트 — 뇌졸중·주요 출혈·사망 결과 |
| [NCT03993119](https://clinicaltrials.gov/study/NCT03993119) | N/A | 완료 | 500 | 스페인 고령 NVAF 환자 NOAC 처방 패턴 횡단면 연구 |
| [NCT02706080](https://clinicaltrials.gov/study/NCT02706080) | N/A | 상태 불명 | 10 | 응급실 항혈전제 환자 등록 연구 — 표본 수 과소(n=10), 통계적 의미 제한적 |

> NCT03804125 (Phase IV 안전성 연구)는 WITHDRAWN(0명 납입)으로 데이터 없음. 분석에서 제외.

---

## 문헌 근거

(폐동맥고혈압 기준, 관련성 높은 순)

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [27932335](https://pubmed.ncbi.nlm.nih.gov/27932335/) | 2016 | Phase 2 RCT 프로토콜 | BMJ Open | **SPHInX 연구**: SSc 관련 PAH에서 Apixaban vs 위약 무작위대조시험 — Apixaban의 PAH 치료 직접 검증을 위한 핵심 근거 |
| [39468095](https://pubmed.ncbi.nlm.nih.gov/39468095/) | 2024 | 코호트 | Scientific Reports | CTEPH 50명에서 Apixaban·리바록사반·에독사반의 anti-Xa 활성 모니터링 — FXa 억제제의 CTEPH 실제 임상 사용 데이터 |
| [40023651](https://pubmed.ncbi.nlm.nih.gov/40023651/) | 2025 | RCT | Lancet | 고재발 위험 VTE에서 감량 vs 표준용량 DOAC 연장 치료 비열등성 시험 |
| [38910594](https://pubmed.ncbi.nlm.nih.gov/38910594/) | 2024 | Review | J Scleroderma Relat Disord | SSc에서 항응고 치료 재평가 — 혈관 손상·원위 혈전 기전과 DOACs 역할 고찰 |
| [29791520](https://pubmed.ncbi.nlm.nih.gov/29791520/) | 2018 | Review | Clinics (São Paulo) | CTEPH 치료에서 직접 경구 항응고제 사용 현황 분석 |
| [24875390](https://pubmed.ncbi.nlm.nih.gov/24875390/) | 2014 | RCT | Thrombosis Research | AMPLIFY 관련: 급성 DVT/PE에서 Apixaban 효능·안전성 — CTEPH 예방을 위한 적극 항응고의 근거 |
| [36335915](https://pubmed.ncbi.nlm.nih.gov/36335915/) | 2023 | RCT | Circulation | AXADIA-AFNET 8: 혈액투석 AF 환자에서 Apixaban vs Phenprocoumon |
| [38033089](https://pubmed.ncbi.nlm.nih.gov/38033089/) | 2024 | 임상지침 | Circulation | 2023 ACC/AHA/ACCP/HRS AF 진료 지침 — Apixaban 표준 권장 항응고제로 명시 |
| [40959672](https://pubmed.ncbi.nlm.nih.gov/40959672/) | 2025 | Case Report | Cureus | Apixaban으로 상행 대동맥 및 폐정맥 혈전 성공적 소실 증례 — 폐혈관 혈전에 대한 직접 효능 신호 |
| [36035947](https://pubmed.ncbi.nlm.nih.gov/36035947/) | 2022 | Review | Front Cardiovasc Med | 폐질환 환자에서 경구 항응고제(VKA·DOAC) 효과 비교 분석 |

---

## 전체 예측 적응증 종합 평가

TxGNN이 Apixaban에 대해 예측한 10개 적응증의 근거 및 안전성 종합 요약입니다.

| 순위 | 적응증 | TxGNN 점수 | 근거 수준 | 권장 결정 | 핵심 근거 / 비고 |
|------|--------|-----------|---------|---------|----------------|
| 1 | 편두통 장애 (Migraine Disorder) | 99.02% | L4 | Research Question | PFO-미세색전 이론 — 기전 간접적, 임상 데이터 부재 |
| 2 | 선조 있는/없는 편두통 (Susceptibility) | 98.92% | L4 | Hold ⛔ | **안전성 신호**: Apixaban 투여 후 편두통 선조 악화 (PMID 37582651) |
| 3 | 나병 (Leprosy) | 98.90% | L5 | Hold | 기전 연관성 없음, 지식 그래프 가양성 추정 |
| 4 | 류마티스 관절염 (RA) | 98.89% | L4 | Research Question | FXa→JAK2/STAT3 전임상 항관절염 데이터 (PMID 32141012) |
| 5 | 뇌간 선조 편두통 | 98.83% | L4 | Hold ⛔ | **안전성 신호**: 와파린 유효·Apixaban 무효 직접 비교 증례 (PMID 28960288) |
| 6 | 변이형 협심증 (Prinzmetal Angina) | 98.39% | L5 | Hold | 혈관 경련 기전, FXa 억제 직접 타깃 아님 |
| 7 | 단지-합지증 증후군 | 98.18% | L5 | Hold | 골격 발생 유전 질환, 응고계와 무관 |
| **8** | **폐동맥고혈압** | **98.13%** | **L3** | **Proceed with Guardrails ✓** | Phase 2 RCT 프로토콜(SPHInX) + CTEPH 코호트 |
| 9 | 결손 소안구증-근단형 이형성증 | 97.99% | L5 | Hold | 극희귀 선천성 질환, 시각산 신호와 응고계 교집합 없음 |
| 10 | 척추후측만증성 심장병 | 97.87% | L5 | Hold | WHO Group 3 PH 간접 연관 가능, 독립 근거 없음 |

---

## 한국 시판 정보

현재 한국에 허가된 Apixaban 제품이 없습니다 (등록 허가증: 0건).

> Apixaban은 미국(Eliquis®, BMS/Pfizer 공동), 유럽, 일본 등 주요국에서 비판막성 심방세동 뇌졸중 예방, DVT/PE 치료·예방 적응증으로 허가되어 있습니다. 한국 도입 시 식품의약품안전처 허가 절차 및 국민건강보험 급여 검토가 선행되어야 합니다.

---

## 안전성 고려사항

이번 Evidence Pack에 한국 허가사항 경고·금기 데이터가 포함되어 있지 않습니다. **반드시 Apixaban 허가사항을 참조하세요.**

**⚠️ 편두통 관련 안전성 신호**

증례 보고 2건이 편두통 환자에서 Apixaban 사용 시 주의를 요한다는 신호를 제공합니다.

- **PMID 37582651 (2023)**: Apixaban 시작 후 선조 있는 편두통 악화 사례 보고 및 문헌 고찰 — 직접 경구 항응고제와 편두통 증상 변화의 관계가 불분명하고 상반된 데이터가 존재함을 지적
- **PMID 28960288 (2017)**: 동일 환자에서 와파린 복용 중 12년간 편두통 완전 관해 → Apixaban 전환 3주 후 재발 → 와파린 재투여 수일 내 재관해. 와파린이 비타민K 의존성 단백질(Protein S → EPCR 조절)을 통한 추가 신경보호 효과를 지닐 가능성 제시

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails (폐동맥고혈압)**

**사유:**
10개 TxGNN 예측 중 폐동맥고혈압만이 Phase 2 RCT 프로토콜(SPHInX 연구, PMID 27932335), 실제 CTEPH 환자 코호트 데이터, 기전 연구를 아우르는 L3 수준의 근거를 보유합니다. CTEPH 아형에서는 DOACs의 VKA 대체 가능성이 임상적으로 인정되는 방향으로 근거가 축적되고 있으며, PAH-SSc에서는 FXa 억제의 혈관 리모델링 억제 기전이 이론적으로 타당합니다.

**진행하려면 필요한 것:**
- SPHInX 연구(PMID 27932335) 최종 결과 데이터 입수 및 검토 (현재 프로토콜만 확인됨)
- CTEPH, PAH-SSc, WHO Group 1/3/4 PH 아형별 층위 분석 수행
- Apixaban 상세 MOA 데이터 확보 (현재 High severity Data Gap)
- 한국 허가사항 경고·금기 안전성 검토 (현재 Blocking Data Gap — S1 진입 전 필수)
- 류마티스 관절염(RA) 연구 과제화: FXa→JAK2/STAT3 기전 임상 번역 연구 설계 타당성 검토
- 편두통 환자에서 Apixaban 투여 시 증상 변화 전향적 모니터링 계획 수립
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

