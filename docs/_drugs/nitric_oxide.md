---
layout: default
title: Nitric Oxide
parent: 僅模型預測 (L5)
nav_order: 310
evidence_level: L5
indication_count: 10
---

# Nitric Oxide
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

# 산화질소(Nitric Oxide): 한국 미허가 상태에서 폐동맥 고혈압(PAH) 치료 후보로

## 한 문장 요약

Nitric Oxide(DrugBank DB00435)는 한국에 허가된 제품이 없는 물질로, 원래 적응증 데이터 자체가 확보되어 있지 않습니다.
TxGNN 모델이 제시한 10개 예측 적응증 중 상위 5개(순위 1~5)는 검토 결과 기전적 근거가 없는 **모델 잡음(noise)**으로 판정되었고, 실제로 의미 있는 근거가 확인된 것은 **폐동맥 고혈압(Pulmonary Arterial Hypertension, PAH)** 계열 적응증 5건(순위 6~10)입니다.
이 중 가장 근거가 강한 것은 순위 7 **폐동맥 고혈압** 그 자체로, **50건의 임상시험**과 **20편의 문헌**이 NO-sGC-cGMP 경로를 통한 기전적 타당성을 뒷받침합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (한국 미허가 약물, 원 적응증 데이터 미확보) |
| 예측 신규 적응증 | 폐동맥 고혈압 (Pulmonary Arterial Hypertension) |
| TxGNN 예측 점수 | 99.41% |
| 근거 수준 | L2 |
| 한국 시판 현황 | ✗ 미상장 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails (단, 아래 차단 사유 해소 선행 필요) |

> ⚠️ **차단 사유(Blocking)**: 이번 Evidence Pack에는 "한국 규제기관 경고문/금기 정보 결측(DG001)"이 Blocking 등급으로 표시되어 있으며, 이는 안전성 초기평가(S1) 진입 자체를 막는 항목입니다. 아래 결론에서 상세히 설명합니다.

---

## 왜 순위 1이 아니라 순위 7을 대표 적응증으로 선정했는가?

이 Evidence Pack(v4, multi-candidate)은 TxGNN 예측 순위 1~10을 모두 제공하며, 각 항목에 자체 기전 타당성 평가(`repurposing_rationale`)가 포함되어 있습니다. 이를 그대로 반영해 아래와 같이 선별했습니다.

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 | 권장 | 판정 |
|------|------------|-----------|----------|------|------|
| 1 | 치아/치주 결손 동반 기형 증후군 | 99.57% | L5 | Hold | **잡음** — 단일 질병이 아닌 Orphanet 증후군 분류명, NO 치료 관련 문헌 전무 |
| 2 | 다모증 (Hypertrichosis) | 99.56% | L4 | Hold | **잡음** — 간접적 ROS/과산화질산 관련 문헌 1편뿐, NO 치료 기전 없음 |
| 3 | Ambras형 전신 다모증 | 99.55% | L5 | Hold | **잡음** — 근거 전무 |
| 4 | Dandy-Walker 기형 동반 증후군 | 99.53% | L5 | Hold | **잡음** — 근거 전무 |
| 5 | 고립성 유전성 모간 이상 | 99.49% | L5 | Hold | **잡음** — 근거 전무 |
| 6 | 폐동정맥 기형 (PAVM) | 99.41% | L3 | Research Question | 실질적 기전 연관 — iNO가 PAVM 속발성 저산소증/폐고혈압에 실제 사용됨 |
| **7** | **폐동맥 고혈압 (PAH)** | **99.41%** | **L2** | **Proceed with Guardrails** | **최상위 근거 — 이번 보고서의 핵심 대상** |
| 8 | 선천성 심장병 동반 PAH | 99.41% | L3 | Research Question | 기전 연관 있으나 시험 대부분 하류 약물(PDE5 억제제 등) 대상 |
| 9 | 만성 용혈성 빈혈 동반 PAH | 99.29% | L4 | Research Question | 강한 기전 연관(용혈로 인한 NO 소모)이나 NO 직접 시험 부재 |
| 10 | 주혈흡충증 동반 PAH | 99.29% | L4 | Hold | 기전적 개연성만 있고 NO 직접 근거 없음 |

순위 1~5는 TxGNN 임베딩 유사도로 인해 높은 점수를 받았을 뿐, 실제 임상/문헌 근거가 전혀 없는 **가양성(false positive) 신호**로 판정되어 제외했습니다. 아래 상세 근거는 **순위 7 (폐동맥 고혈압)** 을 중심으로 제시하며, 순위 6·8·9는 같은 질환군의 하위 집단으로서 보조 근거로 함께 다룹니다.

---

## 이 예측이 타당한 이유는?

현재 DrugBank 기준 상세 작용 기전(MOA) 데이터는 확보되어 있지 않습니다(Data Gap, High 등급). 다만 Evidence Pack에 포함된 기전 분석에 따르면:

Nitric Oxide는 흡입 시 폐혈관 평활근의 **가용성 구아닐산고리화효소(sGC)-cGMP 경로**를 직접 활성화하여 선택적 폐혈관 확장을 일으키는 것으로 알려져 있습니다. 폐동맥 고혈압(PAH)의 핵심 병태생리 중 하나가 바로 내피세포의 내인성 NO 생성 저하로 인한 혈관 수축과 혈관벽 재형성이며, 현재 PAH 표준 치료제인 PDE5 억제제(실데나필)와 riociguat 모두 이 NO-sGC-cGMP 경로의 하류에서 작용합니다.

즉, NO 자체는 이 경로의 최상류 신호 분자이므로 기전상 PAH에 직접 작용할 개연성이 매우 높습니다. 실제로 흡입 NO(iNO)는 이미 임상 현장에서 급성 폐혈관 반응성 검사(vasoreactivity test), 심장수술 주변기 및 신생아 지속성 폐고혈압(PPHN) 치료에 표준적으로 사용되고 있어, 이번 예측은 순수 모델 추정이 아니라 기존 임상 관행과도 부합합니다. 다만 만성·장기 흡입 투여로 확장하려면 전달장치의 안전성 및 내약성 문제가 관건으로 남아 있습니다.

관련 적응증인 폐동정맥 기형(순위 6)에서도 iNO는 우좌 단락으로 인한 저산소혈증 개선에 실제 사용된 사례가 문헌으로 확인되며, 만성 용혈성 빈혈 동반 PAH(순위 9)에서는 용혈로 인한 유리 헤모글로빈이 혈장 NO를 소거(scavenging)한다는 기전이 명확히 보고되어 있어, NO 보충 치료의 이론적 타당성을 뒷받침합니다.

---

## 임상시험 근거 (폐동맥 고혈압)

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01165047](https://clinicaltrials.gov/study/NCT01165047) | Phase 2 | 완료 | 10 | GeNO Nitrosyl NO 전달장치의 안전성·내약성·성능 평가, RHC 중 흡입 NO가 가역적 PH 환자에서 PVR 감소시킴을 확인 |
| [NCT02725372](https://clinicaltrials.gov/study/NCT02725372) | Phase 3 | 조기종료 | 207 | Pulsed 흡입 NO vs 위약의 PAH 유효성·안전성·내약성 평가 (RCT, 조기종료) |
| [NCT02734953](https://clinicaltrials.gov/study/NCT02734953) | Phase 2 | 완료 | 10 | 흡입 NO가 PAH 환자의 침습적으로 측정한 폐혈관 지표(PVR)에 미치는 영향 평가 |
| [NCT02821156](https://clinicaltrials.gov/study/NCT02821156) | N/A | 완료 | 239 | EZ-KINOX 통합 흡입 NO 전달/모니터링 장치의 전향적 관찰연구 (PAH 및 PPHN 대상) |
| [NCT05757557](https://clinicaltrials.gov/study/NCT05757557) | Phase 1/2 | 완료 | 136 | DEFENDER — 전기화학 합성 NO의 심장수술 주변기 신장보호(급성신손상 예방) 효과 평가, 폐혈관 확장을 통한 산소화 개선 기전 |
| [NCT02000856](https://clinicaltrials.gov/study/NCT02000856) | N/A | 완료 | 15 | BEET PAH — 비트즙(질산염, NO 전구물질)이 PAH 환자에 미치는 효과 평가 (교차설계 RCT) |
| [NCT03267108](https://clinicaltrials.gov/study/NCT03267108) | Phase 3 | 조기종료 | 145 | REBUILD — 폐섬유증 관련 장기산소요법 환자에서 pulsed 흡입 NO 안전성·유효성 평가 |
| [NCT01728220](https://clinicaltrials.gov/study/NCT01728220) | Phase 2 | 완료 | 159 | INHALE 1 — COPD 동반 WHO Group 3 폐고혈압 환자 대상 pulsed 흡입 NO 용량결정 연구 |
| [NCT00041574](https://clinicaltrials.gov/study/NCT00041574) | Phase 2 | 조기종료 | 7 | 만성 심폐질환 환자에서 가정용 pulsed INOmax 요법 개발 및 methemoglobin 등 안전성 모니터링 |
| [NCT00848731](https://clinicaltrials.gov/study/NCT00848731) | Phase 1 | 완료 | 25 | 급성 폐색전증 환자에서 흡입 NO 치료의 안전성 및 호흡곤란 개선 평가 |

---

## 문헌 근거 (폐동맥 고혈압)

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [33773120](https://pubmed.ncbi.nlm.nih.gov/33773120/) | 2021 | RCT | The Lancet Respiratory Medicine | REPLACE 시험 — riociguat로 전환이 PDE5 억제제 유지요법 대비 PAH 환자에서의 효과 비교 |
| [32442078](https://pubmed.ncbi.nlm.nih.gov/32442078/) | 2020 | Review | Current Medicinal Chemistry | PAH에서 NO 경로의 병태기전, 바이오마커, 약물 표적 총설 |
| [23822809](https://pubmed.ncbi.nlm.nih.gov/23822809/) | 2013 | Review | Am J Respir Crit Care Med | PAH에서 NO 결핍과 내피기능장애의 역할 |
| [33836637](https://pubmed.ncbi.nlm.nih.gov/33836637/) | 2021 | Review | J Cardiovasc Pharmacol Ther | NO 및 프로스타사이클린 경로를 표적으로 한 PAH 병용요법 |
| [40341051](https://pubmed.ncbi.nlm.nih.gov/40341051/) | 2025 | Review | European Respiratory Journal | PAH의 새로운 경로(BMP/TGF-β 등)를 표적으로 하는 신약 개발 동향 |
| [38416633](https://pubmed.ncbi.nlm.nih.gov/38416633/) | 2024 | Meta-analysis | European Heart Journal | PAH 치료 경로(NO/프로스타사이클린/엔도텔린) 개인환자자료 네트워크 메타분석 |
| [39209476](https://pubmed.ncbi.nlm.nih.gov/39209476/) | 2024 | Guideline/Review | European Respiratory Journal | PAH 치료 알고리즘 — 4대 신호경로(엔도텔린, NO, 프로스타사이클린, BMP/액티빈) 정리 |
| [35412560](https://pubmed.ncbi.nlm.nih.gov/35412560/) | 2022 | Review | JAMA | 폐동맥 고혈압 진단 및 치료 총설 |
| [20051913](https://pubmed.ncbi.nlm.nih.gov/20051913/) | 2010 | Review | Journal of Hypertension | PAH에서 NO, 산화 스트레스, 염증의 상호작용 |
| [38054614](https://pubmed.ncbi.nlm.nih.gov/38054614/) | 2024 | 기술 연구 | Small | PAH 치료를 위한 흡입형 NO 전달 시스템(나노입자 기반) 개발 |

---

## 한국 시판 정보

현재 한국에 허가된 Nitric Oxide 제품이 없습니다 (`total_licenses: 0`, `market_status: 미상장`). 허가 정보 및 국내 유통 제품명, 제형 데이터가 전혀 존재하지 않습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> 참고: 이번 Evidence Pack은 "한국 규제기관 경고문/금기사항 결측(DG001)"을 **Blocking(차단)** 등급으로 명시하고 있으며, 이로 인해 안전성 초기평가(S1) 단계에 진입할 수 없는 상태입니다. DDI 조회 결과도 `not_found`로, 상호작용 데이터가 전혀 확보되지 않았습니다.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails (단, 안전성 데이터 확보 전까지 실행 보류)**

**사유:**
- 순위 7 "폐동맥 고혈압" 예측은 근거 수준 L2로, 완료된 Phase 2/3 임상시험과 20편의 문헌이 NO-sGC-cGMP 경로를 통한 기전적 타당성을 뒷받침하며, iNO는 이미 실제 임상에서 폐혈관 반응성 검사 및 급성기 치료에 사용되고 있어 재창출 가능성이 높습니다.
- 그러나 이번 Evidence Pack에서 "한국 규제 경고문/금기사항 결측(DG001)"이 **Blocking** 등급으로 지정되어 있어, 이 항목이 해소되기 전까지는 안전성 초기평가(S1) 자체를 진행할 수 없습니다. 따라서 과학적 타당성과 별개로 **실행은 보류(Hold)** 상태를 유지해야 합니다.
- 순위 1~5의 TxGNN 고득점 예측(치아/치주 결손 증후군, 다모증 등)은 기전적 근거가 전혀 없는 모델 잡음으로 판정되어 본 보고서에서 제외했습니다.

**진행하려면 필요한 것:**
- TFDA/한국 규제기관 공식 허가사항(경고, 금기) 확보 — 현재 Blocking 상태 해소 (최우선)
- DrugBank API를 통한 상세 작용 기전(MOA) 데이터 보강
- 만성·장기 흡입 투여 시 전달장치 안전성 및 methemoglobin혈증 등 모니터링 계획 수립
- 순위 6, 8, 9 (PAVM, 선천성 심장병 동반 PAH, 만성 용혈성 빈혈 동반 PAH)의 하위집단별 세부 검토 — 동일 질환군 내 우선순위 재평가에 활용 가능
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

