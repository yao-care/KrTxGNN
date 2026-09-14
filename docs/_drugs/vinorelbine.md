---
layout: default
title: Vinorelbine
parent: 僅模型預測 (L5)
nav_order: 723
evidence_level: L5
indication_count: 10
---

# Vinorelbine
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

# Vinorelbine: 비소세포폐암(NSCLC)에서 유잉육종으로

## 한 문장 요약

Vinorelbine은 미세관 억제 기전의 빈카 알칼로이드 계열 세포독성 항암제로, 문헌상 비소세포폐암(NSCLC) 등 고형암 화학요법에 표준적으로 사용되어 왔습니다. TxGNN 모델은 **유잉육종(Ewing sarcoma)**에도 효과가 있을 것으로 예측하며, 현재 **4건의 임상시험**(직접 관련성 높은 시험 2건 포함)이 이 방향을 지지합니다. 관련 문헌은 아직 확보되지 않았습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 비소세포폐암(NSCLC) 등 (근거자료 내 문헌 기준; 한국 허가자료 없음) |
| 예측 신규 적응증 | 유잉육종 (Ewing sarcoma) |
| TxGNN 예측 점수 | 99.999% |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 DrugBank 기준 상세 작용기전(MOA) 데이터는 확보되지 않았습니다. 다만 수집된 근거자료에 따르면, Vinorelbine은 미세관(microtubule) 동역학을 억제하여 세포분열의 M기를 차단하는 세포독성 항암제로, 증식 속도가 빠른 소아·청소년기 소원형세포육종(small round cell sarcoma) 계열인 유잉육종에도 기전상 적용될 근거가 있습니다.

실제로 Vinorelbine+Cyclophosphamide 병용요법은 재발/불응성 소아 육종(횡문근육종, 유잉육종, 골육종, 신경모세포종 등)에 대해 소아종양학 협력체계에서 이미 비허가(off-label) 방식으로 사용되어 온 조합이며, 완료된 Phase 2 단독요법 시험(NCT00003234)에서도 재발/불응성 소아 악성종양에 대한 활성이 확인된 바 있어 TxGNN 예측의 임상적 타당성을 뒷받침합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00180947](https://clinicaltrials.gov/study/NCT00180947) | Phase 2 | 상태 불명 | 210 | Vinorelbine+Cyclophosphamide 병용요법의 항종양 활성 평가 — 횡문근육종·연조직육종·유잉육종·골육종·신경모세포종·수모세포종 등 불응성/재발 고형종양 대상 |
| [NCT00003234](https://clinicaltrials.gov/study/NCT00003234) | Phase 2 | 완료 | 50 | 재발/불응성 소아 악성종양(유잉육종 포함)에서 Vinorelbine 단독요법의 유효성 평가 |
| [NCT05999994](https://clinicaltrials.gov/study/NCT05999994) | Phase 2 | 모집 중 | 105 | CAMPFIRE 소아/청년 암 마스터 프로토콜 — 신약 개발 시 개별 하위연구가 추가되는 공통 임상시험 플랫폼(간접 관련) |
| [NCT06451302](https://clinicaltrials.gov/study/NCT06451302) | N/A | 모집 종료(진행 중) | 100 | 중국 내 소아 유잉육종 위험도별 치료의 성과·안전성 평가 — 전향적 다기관 관찰 코호트(비개입 연구) |

## 문헌 근거

현재 관련 문헌이 없습니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 화학요법제 (Vinca alkaloid 계열, 미세관 억제제) |
| 골수억제 위험 | 중~고 — 근거자료 내 문헌(PMID 9535205)에서 Vinorelbine 병용요법의 용량제한독성이 골수억제로 보고됨 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | CBC(백혈구·호중구·혈소판 분획), 간기능 |
| 취급 방호 | 세포독성 항암제 취급 규정(주사 조제 시 방호구 등) 준수 필요 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
완료된 Phase 2 단독요법 시험(NCT00003234)과 병용요법 시험(NCT00180947)이 재발/불응성 소아 육종군(유잉육종 포함)에서 Vinorelbine의 활성을 뒷받침하며, 소아종양학계의 기존 off-label 사용 패턴과도 부합합니다. 다만 유잉육종에 특이적인 Phase 3 확증시험이 없고, 한국 내 허가·시판 이력이 전무하며, TFDA 수준의 경고/금기 정보(DG001, Blocking)와 상세 MOA 데이터(DG002, High)가 아직 확보되지 않아 안전성 초기평가(S1)를 통과하지 못한 상태입니다.

**진행하려면 필요한 것:**
- TFDA 등 규제기관 공식 경고·금기 정보 확보 (DG001, Blocking — S1 안전성 초평가 필수 선행조건)
- DrugBank 기반 상세 작용기전(MOA) 데이터 확보 (DG002)
- 유잉육종 특이적 Phase 2/3 확증 임상시험 또는 전향적 코호트 자료 추가 확보
- 소아 환자군 대상 골수억제 등 독성 모니터링 계획 수립
- 한국 내 수입/허가 경로 검토 (현재 미출시, 허가증 0건)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

