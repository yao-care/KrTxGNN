---
layout: default
title: Dexamethasone
parent: 僅模型預測 (L5)
nav_order: 211
evidence_level: L5
indication_count: 10
---

# Dexamethasone
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

# Dexamethasone: 염증성·자가면역 질환에서 원형 탈모증으로

---

## 한 문장 요약

Dexamethasone은 강력한 합성 당질코르티코이드(glucocorticoid)로, 염증성 질환·알레르기·자가면역 질환 등 광범위한 영역에서 전 세계적으로 사용되는 표준 치료제입니다.
TxGNN 모델은 **원형 탈모증(Alopecia Areata)**에 효과가 있을 수 있다고 예측하며,
현재 **등록 임상시험은 없으나 20편의 문헌**이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 항염증·자가면역 질환 (당질코르티코이드) |
| 예측 신규 적응증 | 원형 탈모증 (Alopecia Areata) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L2 |
| 시판 현황 | ✗ 미상장 (허가 정보 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

원형 탈모증(AA)은 CD8+ T 세포가 모낭의 면역 특권 구역을 공격하는 T 세포 매개 자가면역 질환입니다. IFN-γ/IL-15 신호 축이 핵심 발병 기전으로, 자가 반응성 면역세포가 모낭을 이물질로 인식·파괴하면서 비반흔성 탈모가 진행됩니다.

Dexamethasone은 당질코르티코이드 수용체(GR)를 통해 NF-κB 경로를 억제하고, IFN-γ 및 IL-2를 하향 조절하며, 자가 반응성 T 세포와 비만세포(mast cell)의 활성화를 직접 차단합니다. 이는 AA의 핵심 병리 기전을 정면으로 표적하는 것으로, FDA 승인을 받은 JAK 억제제(baricitinib, ritlecitinib)와 동일한 IFN-γ 하위 신호 경로에 작용한다는 점에서 기전적 타당성이 높습니다.

임상 실무에서는 **"Mini-Pulse 요법"**(주 2회 경구 5 mg, 연속 이틀 투여)이 주기적 면역 억제와 전신 부작용(HPA 축 억제, 혈당 상승 등) 사이의 균형을 유지하는 실용적 프로토콜로 인도, 스페인, 스위스 등 다수 국가에서 활용되고 있습니다. JAK 억제제 접근이 불가능하거나 금기인 환자군에서 유효한 대안적 치료 전략으로 근거가 축적 중입니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

(ClinicalTrials.gov 및 ICTRP 검색 결과: 0건)

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [39042154](https://pubmed.ncbi.nlm.nih.gov/39042154/) | 2024 | Systematic Review / Network Meta-analysis | Archives of Dermatological Research | 중증 AA(SALT ≥50%)에서 전신 스테로이드·JAK 억제제·접촉면역요법 효능 비교; PRISMA 기반 네트워크 메타분석으로 치료 우위 평가 |
| [36086930](https://pubmed.ncbi.nlm.nih.gov/36086930/) | 2022 | RCT | Dermatologic Therapy | 소아 중증 AA(n=30)에서 저용량 Dexamethasone 경구 미니펄스 vs DPCP 접촉 감작 무작위 공개 비교 임상시험 |
| [35330017](https://pubmed.ncbi.nlm.nih.gov/35330017/) | 2022 | Prospective Cohort | Journal of Clinical Medicine | 실제 임상 환경에서 AA 환자 대상 경구 미니펄스 코르티코스테로이드의 효능·안전성 평가; 반응 예측 인자 분석 |
| [36070222](https://pubmed.ncbi.nlm.nih.gov/36070222/) | 2022 | Prospective Cohort | Dermatologic Therapy | 중등도~중증 AA에서 경구 Dexamethasone 미니펄스 다기관 연구; 유럽에서 승인 치료가 없는 환자군 대상 |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Clinical Review | Pediatric Dermatology | 소아 AA 치료에서 펄스 용량 코르티코스테로이드 요법의 용량 및 투여 프로토콜, 부작용 문헌 고찰 |
| [31579982](https://pubmed.ncbi.nlm.nih.gov/31579982/) | 2019 | Prospective Clinical Study | Dermatologic Therapy | 중증 소아 AA(n=73)에서 1일 vs 3일 정맥 Dexamethasone 펄스 비교; 50% 이상 모발 재성장 달성 반응률 평가 |
| [26179196](https://pubmed.ncbi.nlm.nih.gov/26179196/) | 2015 | Prospective Long-term Study | Dermatologic Therapy | 소아·청소년 AA 65명에서 경구 Dexamethasone 펄스 + 국소 코르티코스테로이드 병용 장기 추적(중앙값 96개월) |
| [41872082](https://pubmed.ncbi.nlm.nih.gov/41872082/) | 2026 | Retrospective Chart Review | European Journal of Dermatology | 중증 AA(n=19)에서 baricitinib + 국소 스테로이드 후 비반응자에 Dexamethasone 펄스 구제요법 단계적 적용의 실제 임상 경험 |
| [41243342](https://pubmed.ncbi.nlm.nih.gov/41243342/) | 2025 | Observational / Case Series | Journal of Dermatological Treatment | JAK 억제제 사용 불가 환경에서 Dexamethasone 경구 미니펄스로 중증 AA 지속 관해 달성 사례 및 집중 문헌 고찰 |
| [16707886](https://pubmed.ncbi.nlm.nih.gov/16707886/) | 2006 | Comparative Study | Dermatology (Basel) | 광범위 AA에서 세 가지 전신 코르티코스테로이드 요법의 효능, 재발률, 부작용 비교 |

---

## 시판 정보

현재 데이터 수집 범위에서 허가 정보가 확인되지 않습니다 (등록 허가증 0건).

> **참고**: Dexamethasone은 WHO 필수의약품 목록에 포함된 전 세계적으로 광범위하게 허가된 약물입니다. 본 데이터 수집 범위의 한계로 인해 허가 정보가 누락되었을 수 있으므로, 실제 적용 전 해당 국가 규제 기관(MFDS, FDA, EMA 등)의 허가 현황을 별도로 확인하시기 바랍니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
원형 탈모증에 대한 Dexamethasone Mini-Pulse 요법은 네트워크 메타분석(1건)과 무작위 대조 임상시험(1건), 복수의 전향적 코호트 연구(4건 이상)로 L2 수준의 근거를 보유하고 있으며, 기전적 타당성도 IFN-γ 경로를 통해 명확히 설명됩니다. 다만 ClinicalTrials.gov 등록 임상시험이 없고 장기 표준화 프로토콜이 부재하여 추가 구조화가 필요합니다.

> **주목할 만한 추가 발견**: 이번 Evidence Pack에서 TxGNN Rank 9에 해당하는 **腱鞘炎(Tenosynovitis)**은 Rank 1(원형 탈모증)보다 임상 근거가 더 풍부합니다 — Phase 4 완료 RCT 1건 포함 4건의 등록 임상시험, 문헌 13편. 코르티코스테로이드 국소 주사가 방아쇠 손가락(trigger finger), De Quervain 腱鞘炎에서 표준 1차 치료로 활용되는 임상적으로 성숙한 영역이며, 별도 검토를 권장합니다.

**진행하려면 필요한 것:**
- 상세 작용 기전(MOA) 문서화 (DrugBank 데이터 보완)
- TFDA/MFDS 허가사항 및 안전성 경고·금기 정보 수집
- Mini-Pulse 요법 표준화 프로토콜 정의 (용량·투여 기간·반응 평가 기준·중단 기준)
- 장기 전신 코르티코스테로이드 부작용 모니터링 계획 수립 (골밀도 감소, 혈당 상승, 감염 위험, HPA 축 억제)
- JAK 억제제 접근 불가 환자군 대상 적절한 환자 선별 기준 정의
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

