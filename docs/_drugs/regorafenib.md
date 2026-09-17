---
layout: default
title: Regorafenib
parent: 모델 예측만 (L5)
nav_order: 596
evidence_level: L5
indication_count: 10
---

# Regorafenib
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 약사 평가 보고서

</div>

# Regorafenib: 대장직장암·GIST·간세포암에서 지방육종(Liposarcoma)으로

## 한 문장 요약

Regorafenib은 원래 전이성 대장직장암, 위장관 기질종양(GIST), 간세포암 치료에 사용되는 경구용 다중키나아제 억제제입니다(문헌 근거 기반, 한국 허가 정보 없음). TxGNN 모델은 **지방육종(Liposarcoma)**에도 효과가 있을 것으로 예측(점수 99.76%)했지만, 실제로 이 가설을 직접 검증한 **2건의 완료된 Phase 2 RCT(REGOSARC, SARC024)**는 오히려 지방육종에서 효과가 없다는 **음성 결과**를 보고했습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 전이성 대장직장암, GIST, 간세포암 (해외 승인 기준, 문헌 인용; 한국 허가 정보 없음) |
| 예측 신규 적응증 | 지방육종 (Liposarcoma) |
| TxGNN 예측 점수 | 99.76% |
| 근거 수준 | L2 (완료된 Phase 2 RCT 존재하나 결과는 음성) |
| 한국 시판 현황 | 미상판 (허가 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 이 예측이 타당한 이유는?

공식 MOA 데이터(DrugBank)는 현재 확보되지 않았습니다(데이터 갭 DG002 — DrugBank API 재조회 필요). 다만 수집된 문헌(PMID 30069758, 24756792)에 따르면 Regorafenib은 VEGFR1-3, TIE2, PDGFR-β, FGFR 등 혈관신생 관련 키나아제와 KIT, RET, RAF 등 종양성 수용체 타이로신 키나아제를 표적으로 하는 경구용 다중키나아제 억제제이며, 이 기전으로 대장직장암·GIST·간세포암에 이미 승인되어 있습니다.

지방육종을 포함한 비지방세포성 연조직육종(soft tissue sarcoma)에서는 혈관신생이 종양 진행의 핵심 경로로 알려져 있어, 이론적으로는 regorafenib의 항혈관신생 기전이 적용될 수 있다는 가설이 성립합니다. 그러나 이 가설을 직접 검증한 두 건의 Phase 2 RCT에서 상반된 결과가 나왔습니다: REGOSARC 시험(PMID 27751846)은 평활근육종·활막육종 등 **비지방세포성** 육종에서는 효과를 확인했지만 **지방육종에서는 효과가 없었고**, SARC024 시험(PMID 32701199)도 지방육종 코호트에서 "regorafenib의 통상적 사용을 지지하지 않는다"고 결론지었습니다. TxGNN의 높은 점수는 "육종"이라는 큰 범주 내 유사성에서 기인한 것으로 추정되며, 지방육종이라는 세부 서브타입 특이성은 반영하지 못한 것으로 보입니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다. (지방육종 특이적으로 수집된 clinical_trials 항목 없음. 단, 아래 문헌에 인용된 REGOSARC/SARC024 시험은 ClinicalTrials.gov에 등록되어 있으나 소화관 종양 전반 코호트로 구성되어 본 evidence pack의 clinical_trials 필드에는 포함되지 않음)

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [27751846](https://pubmed.ncbi.nlm.nih.gov/27751846/) | 2016 | RCT (Phase 2) | Lancet Oncol | REGOSARC 본 시험: 비지방세포성 육종에서 PFS 개선, 지방육종은 효과 확인 안 됨 |
| [32701199](https://pubmed.ncbi.nlm.nih.gov/32701199/) | 2020 | RCT (Phase 2) | The Oncologist | SARC024 지방육종 코호트: regorafenib의 통상적 사용을 지지하지 않음 |
| [29902612](https://pubmed.ncbi.nlm.nih.gov/29902612/) | 2018 | RCT 추적분석 | Eur J Cancer | REGOSARC cross-over 후 분석, 지방육종 제외 재확인 |
| [28295221](https://pubmed.ncbi.nlm.nih.gov/28295221/) | 2017 | RCT 사후분석 | Cancer | Q-TWiST 분석, 비지방세포성 육종에서 임상적 이익 확인 |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | 시험 프로토콜 | BMC Cancer | REGOSARC 시험 설계 및 배경 |
| [29931504](https://pubmed.ncbi.nlm.nih.gov/29931504/) | 2018 | Review | Targeted Oncology | 육종 치료에서 regorafenib 역할 개관 |
| [40975452](https://pubmed.ncbi.nlm.nih.gov/40975452/) | 2025 | Review | Crit Rev Oncol Hematol | 진행성 연조직육종 1차 치료 후 유지요법 개관 |
| [33290314](https://pubmed.ncbi.nlm.nih.gov/33290314/) | 2021 | 후향적 연구 | Anti-cancer Drugs | Anlotinib 연구, regorafenib 등 TKI를 비교 대상으로 언급 |
| [26266019](https://pubmed.ncbi.nlm.nih.gov/26266019/) | 2015 | 사례 보고 | Rare Tumors | Ewing 육종에서 pazopanib 반응례, SARC024 설계 근거로 인용 |

---

## 한국 시판 정보

한국 내 허가된 제품이 없습니다 (미상판).

---

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (다중키나아제 억제제: VEGFR1-3, TIE2, PDGFR-β, FGFR, KIT, RET, RAF 억제, 문헌 PMID 30069758) |
| 골수억제 위험 | 저 (수집된 문헌에서 골수억제 관련 서술 없음; 주된 독성은 피부·간·심혈관계) |
| 구토 유발성 등급 | 저 (경구 TKI 계열 특성) |
| 모니터링 항목 | 간기능(LFT, PMID 23981115), 혈압(PMID 36583425), 손발피부반응(PMID 23700287), 구강 이상반응(PMID 26403941) |
| 취급 방호 | 경구 표적치료제로 전통적 세포독성 항암제 수준의 특별 방호는 불필요하나, 기관 표준 취급 지침 준수 권장 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (한국 허가사항 부재로 주요 경고·금기·DDI 자료 모두 확보되지 않음 — 데이터 갭 DG001, Blocking)

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
지방육종 적응증을 직접 검증한 2건의 완료된 Phase 2 RCT(REGOSARC, SARC024)가 모두 음성 결과를 보고했으며, TxGNN의 높은 예측 점수는 육종이라는 상위 범주 유사성에서 비롯된 것으로 서브타입 특이성을 반영하지 못한 것으로 판단됩니다. 또한 한국 내 허가 정보와 안전성 자료(경고/금기)가 완전히 결여되어(DG001, Blocking) 안전성 초기 평가(S1) 진입조건도 충족하지 못합니다.

**진행하려면 필요한 것:**
- TFDA/한국 식약처 허가사항(경고·금기) 확보 (DG001 해소)
- DrugBank MOA 상세 데이터 확보 (DG002 해소)
- 지방육종이 아닌 평활근육종·활막육종 등 REGOSARC에서 양성 신호가 확인된 서브타입으로 재평가
- 한국 내 정식 허가 신청 여부 및 시장 진입 전략 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

