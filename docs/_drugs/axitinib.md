---
layout: default
title: Axitinib
parent: 僅模型預測 (L5)
nav_order: 108
evidence_level: L5
indication_count: 10
---

# Axitinib
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

# Axitinib: 진행성 신세포암에서 신경모세포종 연관 신세포암 등 10개 희귀 아형으로

> **다중 적응증 팩** — 본 보고서는 TxGNN이 예측한 10개 적응증 전체를 다룹니다 (Candidate ID: TW-DB06626-multi)

---

## 한 문장 요약

Axitinib(INLYTA)은 VEGFR-1/2/3 선택적 억제제로, 전 세계적으로 진행성 신세포암(RCC) 치료에 사용되는 경구 표적항암제입니다.
TxGNN 모델은 **신경모세포종 연관 신세포암(Rank 1)** 을 포함한 **10개의 신규 적응증**을 예측하였으며, 이 중 **신장암(Rank 6)** 에 대해서는 **50건의 임상시험**과 **20편의 문헌**이 복수의 Phase 3 RCT를 포함하는 L1 수준의 강력한 근거를 지지합니다.
한국 의약품 데이터베이스에서는 현재 허가 이력이 확인되지 않았습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 진행성 신세포암 (글로벌 허가 기준; 한국 허가 미확인) |
| 최상위 예측 신규 적응증 | 신경모세포종 연관 신세포암 (Rank 1) |
| TxGNN 예측 점수 | 99.90% (Rank 1) |
| 근거 수준 | L5 (Rank 1) / 최고 L1 (Rank 6) |
| 한국 시판 현황 | ✗ 미시판 (허가증 미확인) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold (Rank 1) / Proceed with Guardrails (Rank 4, 6, 9) |

---

## 이 예측이 타당한 이유는?

상세한 작용 기전(MOA) 데이터가 현재 확보되지 않은 상태입니다. 알려진 정보에 따르면, Axitinib은 혈관내피성장인자 수용체(VEGFR-1/2/3)를 선택적으로 억제하는 경구 2세대 타이로신 키나아제 억제제(TKI)로, 기존 TKI 대비 약 10배 높은 VEGFR 선택성을 가지며 이를 통해 종양 혈관신생을 차단합니다.

예측된 10개 적응증 중 Rank 1~6은 모두 신세포암 스펙트럼에 속합니다. 투명세포 RCC의 VHL 유전자 변이→HIF-α 축적→VEGF 과발현 경로가 Axitinib의 핵심 표적이며, TFE3 융합 아형(Rank 2)에서도 VEGF 관련 유전자 전사가 활성화되는 것으로 알려져 있습니다. 소아 RCC(Rank 4)는 성인보다 Xp11.2/TFE3 전위 아형 비율이 현저히 높아 VEGFR 억제 전략의 생물학적 합리성이 있습니다. KEYNOTE-426 및 JAVELIN Renal 101의 Phase 3 RCT는 Axitinib 기반 면역병용요법이 진행성 RCC 일선 표준치료임을 확립하였습니다.

반면 Rank 10(가족성 자발성 기흉)은 결합 조직 이상에 의한 비종양성 질환으로 VEGFR 억제와의 생물학적 연관성이 거의 없으며, Rank 8(혈관지방종) 역시 양성 병변으로 Axitinib의 위험-편익비가 불리합니다. 두 적응증 모두 지식 그래프의 위상학적 노이즈 예측으로 분류됩니다.

---

## 전체 예측 적응증 요약

| 순위 | 적응증 | TxGNN 점수 | 근거 수준 | 임상시험 | 문헌 | 권장 결정 |
|------|--------|-----------|---------|---------|-----|---------|
| 1 | 신경모세포종 연관 신세포암 | 99.90% | L5 | 0건 | 0편 | **Hold** |
| 2 | Xp11.2 전위/TFE3 융합 신세포암 | 99.90% | L3 | 1건 | 2편 | Research Question |
| 3 | 미분류 신세포암 | 99.90% | L3 | 2건 | 0편 | Research Question |
| 4 | 소아 신세포암 | 99.87% | L2 | 2건 | 2편 | **Proceed with Guardrails** |
| 5 | 지방육종 | 99.87% | L4 | 0건 | 1편 | Research Question |
| **6** | **신장암 (Renal carcinoma)** | **99.85%** | **L1** | **50건** | **20편** | **Proceed with Guardrails** |
| 7 | 난소 점액성 지방육종 | 99.84% | L5 | 0건 | 0편 | **Hold** |
| 8 | 혈관지방종 | 99.83% | L5 | 0건 | 0편 | **Hold** |
| 9 | 집합관암 | 99.81% | L3 | 1건 | 20편 | **Proceed with Guardrails** |
| 10 | 가족성 자발성 기흉 | 99.78% | L5 | 0건 | 0편 | **Hold** |

---

## 임상시험 근거

### Rank 1 — 신경모세포종 연관 신세포암

현재 관련 임상시험 등록이 없습니다.

---

### Rank 2 — Xp11.2 전위/TFE3 융합 신세포암

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03595124](https://clinicaltrials.gov/study/NCT03595124) | Phase 2 | 모집 완료(진행 중) | 15 | Axitinib/Nivolumab 병용 vs. Nivolumab 단독 무작위 비교; TFE 전위 RCC 전 연령 대상. 절제 불가 또는 전이성 환자 포함. 결과 미공개(완료 예정 2026-11) |

---

### Rank 3 — 미분류 신세포암

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02156895](https://clinicaltrials.gov/study/NCT02156895) | 해당없음 | 완료 | 111 | INLYTA® 실제 임상 사용 시판 후 조사; 미분류 RCC 아형 포함 가능성 있음. 안전성·유효성 실세계 데이터 제공 |
| [NCT04033991](https://clinicaltrials.gov/study/NCT04033991) | 해당없음 | 완료 | 684 | 전이성/진행성 RCC에서 Sunitinib 1선→Axitinib 2선 순차치료 실세계 결과; MSKCC/IMDC 위험군별 PFS 분석 |

---

### Rank 4 — 소아 신세포암

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03595124](https://clinicaltrials.gov/study/NCT03595124) | Phase 2 | 모집 완료(진행 중) | 15 | Axitinib/Nivolumab vs. Nivolumab; 전 연령 TFE 전위 RCC 포함(소아·청소년·성인). 소아 대상 전향적 개입 시험 중 유일하게 Axitinib 직접 평가 |
| [NCT04510597](https://clinicaltrials.gov/study/NCT04510597) | Phase 3 | 모집 중 | 364 | 면역치료 기반 병용요법 ± 세포 감량 신절제술 비교(PROBE Trial); 전이성 RCC. 소아 포함 여부 확인 필요. Axitinib 포함 시 Phase 3 수준 근거 해당 |

---

### Rank 6 — 신장암 (주요 근거, 최상위 10건)

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04394975](https://clinicaltrials.gov/study/NCT04394975) | Phase 3 | **완료** | 421 | RENOTORCH: Toripalimab + Axitinib vs. Sunitinib 1선 무작위 비교; 중등~불량 위험군 진행성 RCC. OS/PFS 우월성 평가 |
| [NCT05738694](https://clinicaltrials.gov/study/NCT05738694) | Phase 3 | 모집 중 | 298 | Axitinib + PD-1 항체 신보조 병용 vs. 수술 단독; 고위험 재발 RCC 대상 무작위 대조. 1:1 배정 |
| [NCT04764487](https://clinicaltrials.gov/study/NCT04764487) | Phase 3 | 불명 | 178 | Axitinib/Pembrolizumab 1선 치료 중 웹 기반 추적관찰 도구(KidneyPRO) 효과 비교; 실제 치료 지속성 평가 |
| [NCT04387500](https://clinicaltrials.gov/study/NCT04387500) | Phase 2 | 모집 완료(진행 중) | 41 | Sintilimab + Axitinib; 푸마르산 수화효소 결핍(FH-deficient) RCC 1선 치료. 희귀 치명적 아형 단일군 연구 |
| [NCT06279403](https://clinicaltrials.gov/study/NCT06279403) | Phase 2 | 모집 예정 | 20 | Toripalimab + Axitinib 선행 치료 후 지연 세포 감량 신절제술; 전이성 ccRCC. MPR(<10% 잔존 종양) 1차 평가변수 |
| [NCT02579811](https://clinicaltrials.gov/study/NCT02579811) | Phase 2 | **완료** | 40 | PD-1/PD-L1 억제제 치료 후 Axitinib 개별화 용량 스케줄 연구; 부작용 기반 용량 최적화. 단일군 설계 |
| [NCT05808608](https://clinicaltrials.gov/study/NCT05808608) | Phase 1/2 | 모집 중 | 33 | AK104(PD-1/CTLA-4 이중 항체) + Axitinib; 특수 병리아형(ssRCC) 1선 치료. ORR/PFS 1차 평가변수 |
| [NCT01806064](https://clinicaltrials.gov/study/NCT01806064) | Phase 1/2 | 종료 | 173 | Axitinib + TRC105(항-CD105 항체) vs. Axitinib 단독; VEGF TKI 실패 후 진행성/전이성 RCC |
| [NCT05096390](https://clinicaltrials.gov/study/NCT05096390) | Phase 2 | 모집 중 | 72 | Axitinib ± Pembrolizumab; 유두상(Papillary) RCC 1선 치료. 비투명세포 아형 대상 다기관 연구 |
| [NCT03494816](https://clinicaltrials.gov/study/NCT03494816) | Phase 2 | **완료** | 24 | NAXIVA: Axitinib 신보조 치료로 정맥 종양 혈전 하강 평가(8주 투여); 정맥 침윤 RCC. 혈전 반응률 35% 보고 |

---

### Rank 9 — 집합관암

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT06211114](https://clinicaltrials.gov/study/NCT06211114) | Phase 2 | 모집 중 | 30 | 면역 관문 억제제 + Axitinib; 기치료 진행성 집합관암 효능·안전성 직접 평가. 이 희귀 아형을 대상으로 한 유일한 Axitinib 직접 개입 시험 |

---

## 문헌 근거

### Rank 2 — Xp11.2 전위/TFE3 융합 신세포암

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [36034832](https://pubmed.ncbi.nlm.nih.gov/36034832/) | 2022 | Case Report | Front Pharmacol | 32세 성인 Xp11.2 전위 RCC에서 camrelizumab + axitinib 치료 후 임상적 완전 반응 달성; TFE3 융합 RCC에서 VEGFR TKI + PD-1 억제제 병용 근거 첫 보고 |
| [36246795](https://pubmed.ncbi.nlm.nih.gov/36246795/) | 2022 | Case Report | World J Clin Cases | Xp11.2/TFE3 거대 신세포암(T3aN1M1) 다학제 치료(화학요법, 경동맥 화학색전술, 신절제술 병용) 경험 보고 |

---

### Rank 4 — 소아 신세포암

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [31012542](https://pubmed.ncbi.nlm.nih.gov/31012542/) | 2019 | Review | Pediatr Blood Cancer | 진행성 소아 신세포암 치료 데이터 검토; 표준치료 부재 확인, 성인 프로토콜 적용 근거·한계 논의. Axitinib 포함 TKI 활용 가능성 언급 |
| [26279736](https://pubmed.ncbi.nlm.nih.gov/26279736/) | 2015 | Case Report | Can Urol Assoc J | 12세 악성 상피형 혈관근지방종(EAML) 환자에서 sunitinib → everolimus → axitinib 순차 치료; 소아에서 axitinib 최초 사용 사례 보고. 성인 프로토콜 적용 가능성 시사 |

---

### Rank 5 — 지방육종

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [27822137](https://pubmed.ncbi.nlm.nih.gov/27822137/) | 2016 | 전임상 | Sarcoma | 점액성 지방육종 세포주에서 Axitinib 항혈관신생·항종양 활성 확인; VEGFR 표적 소분자 약물 중 Axitinib이 항종양 효과 보유. 임상시험 근거는 없으나 전임상 타당성 제시 |

---

### Rank 6 — 신장암 (상위 10편)

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [40750932](https://pubmed.ncbi.nlm.nih.gov/40750932/) | 2025 | Phase 3 RCT 5년 추적 | Nat Med | KEYNOTE-426 5년 분석: Pembrolizumab + Axitinib 진행성 ccRCC에서 OS/PFS 지속 우월성; 예측 바이오마커 탐색 분석 |
| [37872020](https://pubmed.ncbi.nlm.nih.gov/37872020/) | 2024 | Phase 3 RCT | Ann Oncol | RENOTORCH: Toripalimab + Axitinib vs. Sunitinib; 중등~불량 위험군 진행성 RCC 1선 치료, 면역 TKI 병용 전략 아시아 데이터 |
| [39706335](https://pubmed.ncbi.nlm.nih.gov/39706335/) | 2025 | Phase 3 RCT 최종 분석 | Ann Oncol | JAVELIN Renal 101 최종 분석: Avelumab + Axitinib vs. Sunitinib OS 최종 결과 보고 |
| [30779529](https://pubmed.ncbi.nlm.nih.gov/30779529/) | 2019 | Phase 3 RCT | NEJM | KEYNOTE-426 최초 보고: Pembrolizumab + Axitinib vs. Sunitinib 1선 OS·PFS·ORR 전 지표 우월성 확인 |
| [30779531](https://pubmed.ncbi.nlm.nih.gov/30779531/) | 2019 | Phase 3 RCT | NEJM | JAVELIN Renal 101: Avelumab + Axitinib vs. Sunitinib PFS 우월성; PD-L1 양성군 및 전체 집단 모두에서 효과 |
| [37500340](https://pubmed.ncbi.nlm.nih.gov/37500340/) | 2023 | Phase 3 RCT 43개월 추적 | Eur Urol | KEYNOTE-426 최종 프로토콜 분석(43개월 추적): 지속적 OS/PFS 이점 및 장기 안전성 확인 |
| [32895571](https://pubmed.ncbi.nlm.nih.gov/32895571/) | 2020 | Phase 3 RCT 바이오마커 분석 | Nat Med | JAVELIN Renal 101 바이오마커 분석(n=886): PD-L1·TMB와 무관하게 PFS 이점 관찰; FcγR 다형성 연관성 확인 |
| [33284113](https://pubmed.ncbi.nlm.nih.gov/33284113/) | 2020 | Phase 3 RCT 확장 추적 | Lancet Oncol | KEYNOTE-426 확장 추적 분석: OS·PFS 이점 지속 확인, 누적 부작용 데이터 제공 |
| [39362847](https://pubmed.ncbi.nlm.nih.gov/39362847/) | 2024 | Phase 2 코호트 | Signal Transduct Target Ther | NEOTAX: Toripalimab + Axitinib 신보조 치료 후 신절제술; 하대정맥 종양 혈전(IVC-TT) 하강률 개선 확인 |
| [29033542](https://pubmed.ncbi.nlm.nih.gov/29033542/) | 2017 | Review | Drug Des Dev Ther | Axitinib의 RCC 치료 내 설계·개발·위치 종합 검토; 2세대 TKI로서의 선택성·약동학·임상 위치 정리 |

---

### Rank 9 — 집합관암 (주요 4편)

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [35428926](https://pubmed.ncbi.nlm.nih.gov/35428926/) | 2022 | Review | Urologie | 집합관암(Bellini관 암) 현황 검토: nivolumab + axitinib + 방사선 병용 시 생존 연장 단일 사례 보고; cabozantinib 병행 가능성 논의 |
| [35773144](https://pubmed.ncbi.nlm.nih.gov/35773144/) | 2022 | 코호트 연구 | Urol Oncol | 전이성 집합관암 임상병리 특성·치료별 반응 및 예후 인자 분석; 면역 기반 요법 우월성 시사 |
| [30779529](https://pubmed.ncbi.nlm.nih.gov/30779529/) | 2019 | Phase 3 RCT | NEJM | KEYNOTE-426: RCC 일반 1선 치료 근거; 집합관암 아형 병용 전략 배경 참조 |
| [30779531](https://pubmed.ncbi.nlm.nih.gov/30779531/) | 2019 | Phase 3 RCT | NEJM | JAVELIN Renal 101: Avelumab + Axitinib 병용 배경 근거; 집합관암 치료 전략 맥락 참조 |

---

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 — VEGFR 선택적 TKI (비(非)세포독성 기전, 항혈관신생 작용) |
| 골수억제 위험 | **낮음** — 전통 세포독성 항암제 대비 현저히 낮음; 혈소판 감소 및 호중구 감소 드물게 보고 |
| 구토 유발성 등급 | **낮음** |
| 모니터링 항목 | 혈압(고혈압: 가장 흔한 이상반응, 약력학 바이오마커로도 활용), CBC, 간기능(AST/ALT/빌리루빈), 신기능(크레아티닌), 갑상선기능(TSH), 단백뇨(소변 검사 또는 spot urine protein:creatinine ratio) |
| 취급 방호 | 경구 표적치료제 — 표준 의약품 취급 절차 적용. 별도 세포독성 특수 방호 불필요 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails (Rank 4, 6, 9) / Research Question (Rank 2, 3, 5) / Hold (Rank 1, 7, 8, 10)**

**사유:**

신장암(Rank 6)은 KEYNOTE-426, JAVELIN Renal 101, RENOTORCH 등 여러 Phase 3 RCT가 Axitinib 기반 면역병용요법의 일선 치료 우월성을 확립한 L1 수준의 최강 근거를 보유합니다. 집합관암(Rank 9)은 NCT06211114가 직접 탐색 중이며, 단일 사례에서 임상적 이점이 보고된 바 있어 Proceed with Guardrails가 적합합니다. 소아 신세포암(Rank 4)은 NCT03595124 등 전향적 시험이 진행 중이고 성인 Phase 3 근거 외삽이 가능하나 소아 약동학·용량·장기 안전성 모니터링이 필수입니다. 반면 Rank 1(신경모세포종 연관 RCC)은 임상 근거가 전무하고 순수 그래프 위상 추론에 기반하며, Rank 7(난소 점액성 지방육종), Rank 8(혈관지방종), Rank 10(가족성 자발성 기흉)은 생물학적 타당성 또는 위험-편익비가 불충분합니다.

**진행하려면 필요한 것:**

- **한국 허가 현황 재확인**: MFDS 데이터베이스 직접 조회를 통한 Axitinib(INLYTA®) 등록 현황 확인 (현재 0건은 데이터 갭 가능성 있음)
- **작용 기전(MOA) 데이터 보완**: DrugBank API(DB06626) 조회로 공식 MOA 및 DrugBank categories 확보
- **허가사항 경고·금기 확인**: FDA/EMA/MFDS 허가사항 PDF 검토를 통한 안전성 프로파일(고혈압, 혈전색전증, 간독성 등) 완성
- **Rank 4 (소아 적용)**: NCT02164838(소아 Phase 1, 완료) 결과 확인으로 소아 최대내약용량(MTD) 및 권장 Phase 2 용량(RP2D) 검토 필수
- **Rank 9 (집합관암)**: NCT06211114 중간 결과 추적; nivolumab + axitinib 병용 실제 임상 사례 추가 수집
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

