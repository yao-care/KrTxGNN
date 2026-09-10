---
layout: default
title: Everolimus
parent: 僅模型預測 (L5)
nav_order: 308
evidence_level: L5
indication_count: 10
---

# Everolimus
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

# Everolimus: 기존 적응증 미상에서 지방육종(Liposarcoma)으로

## 한 문장 요약

Everolimus는 한국(대만) 허가 자료 및 원 적응증 정보가 현재 확보되지 않은 상태입니다.
TxGNN 모델은 **지방육종(Liposarcoma)**에 효과가 있을 수 있다고 예측하며,
현재 **1건의 임상시험(Phase 2, 진행 중)**과 **4편의 문헌**이 이 방향을 지지합니다.
다만 안전성 정보(경고·금기)가 전면적으로 결여되어 있어 임상적 판단에는 제약이 있습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (원 적응증·한국 허가 자료 미확보) |
| 예측 신규 적응증 | 지방육종 (Liposarcoma) |
| TxGNN 예측 점수 | 99.88% |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미출시 (허가 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 Everolimus의 상세한 작용 기전(MOA) 공식 데이터는 확보되지 않았습니다(Data Gap, DrugBank 조회 필요). 다만 근거로 제출된 문헌·임상시험 정보에 따르면 Everolimus는 mTORC1을 억제하는 mTOR 억제제로 작동하는 것으로 나타납니다.

거세포화된(dedifferentiated) 지방육종은 Akt-mTOR 및 MAPK 신호경로의 활성화가 흔히 관찰되는 것으로 보고되어 있습니다(PMID 26518767). 이는 mTORC1을 표적으로 하는 Everolimus가 이 질환에 기전적으로 작용할 가능성을 뒷받침합니다.

현재 CDK4 억제제인 ribociclib과 Everolimus를 병용하는 Phase 2 임상시험이 CDK4 증폭을 보이는 거세포화 지방육종 환자를 대상으로 진행 중이며, 이는 기전 기반의 병용 전략으로 해석됩니다. 다만 해당 시험은 아직 최종 결과가 공개되지 않은 상태입니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | 활성(모집 종료) | 48 | 진행성 거세포화 지방육종(DDL) 및 평활근육종(LMS) 환자에서 Ribociclib+Everolimus 병용요법의 항종양 효과를 평가하는 2개 기관, 2군 시험. Everolimus 2.5mg 병용, 아직 최종 유효성 데이터 미공개. |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase 2 시험 보고 | Clinical Cancer Research | 거세포화 지방육종 및 평활근육종에서 Ribociclib+Everolimus 병용의 SAR-096 Phase 2 결과. CDK4 억제(DDL)와 mTOR 억제(LMS)를 결합한 병용요법으로, 전임상에서 상승적 성장억제 효과가 확인되어 이를 임상적으로 검증. |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review (PDOX 모델) | Frontiers in Oncology | 환자유래 이종이식(PDOX) 마우스 모델을 이용해 CDK 억제제(palbociclib) 기반 병용요법의 유효성을 확인한 연구. 육종 치료에서 CDK 억제제의 가능성을 제시. |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | 기전/중개연구 | Tumour Biology | 거세포화 지방육종(DDLS) 99건 검체 분석에서 Akt-mTOR 및 MAPK 경로 활성화 확인. mTOR 억제제의 항종양 효과를 시험관 내에서 평가. |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | 전임상 병용연구 | Anticancer Research | Eribulin(진행성 유방암·지방육종 치료제)과 기전이 다른 항암제와의 병용 효과를 평가한 전임상 연구. |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 지방육종에 대한 핵심 근거인 NCT03114527이 아직 진행 중(활성, 모집 종료)이며 최종 유효성 결과가 공개되지 않았습니다.
- TFDA 수준의 경고·금기 정보가 전면 결여되어 있어(DG001, Blocking) 안전성 초기평가(S1) 자체가 불가능한 상태입니다.
- 한국 내 시판·허가 이력이 없어 규제 측면의 진입 경로도 확인되지 않았습니다.

**진행하려면 필요한 것:**
- DrugBank API를 통한 작용 기전(MOA) 및 약물 분류 데이터 확보
- TFDA(또는 해당 규제기관) 공식 허가사항(경고·금기·DDI) 확보
- NCT03114527 임상시험 완료 및 결과 공개 여부 추적
- 지방육종 적응증에 대한 추가 임상 근거(현재 1건뿐) 확충
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

