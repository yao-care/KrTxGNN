---
layout: default
title: Ropeginterferon Alfa-2B
parent: 僅模型預測 (L5)
nav_order: 290
evidence_level: L5
indication_count: 10
---

# Ropeginterferon Alfa-2B
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

# Ropeginterferon Alfa-2b: 진성 적혈구 증가증에서 Laubry-Pezzi 증후군으로

## 한 문장 요약

Ropeginterferon alfa-2b는 JAK-STAT 신호 경로를 억제하는 장시간 작용형 페길화 인터페론 제제로, 진성 적혈구 증가증(Polycythemia Vera, PV) 치료에 활용되는 약물입니다. TxGNN 모델은 **Laubry-Pezzi 증후군**(선천성 대동맥판 역류 + 심실중격결손)에 효과가 있을 수 있다고 예측하였으나, 현재 이를 지지하는 **임상시험이나 관련 문헌이 전무하며**, 기전상 연관성 또한 확인되지 않습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 진성 적혈구 증가증 (Polycythemia Vera; 문헌 기반, 한국 미허가) |
| 예측 신규 적응증 | Laubry-Pezzi 증후군 |
| TxGNN 예측 점수 | 99.93% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

상세한 작용 기전(MOA) 데이터가 현재 확보되어 있지 않습니다. 관련 문헌에 따르면, ropeginterferon alfa-2b는 **JAK-STAT 신호 경로를 억제**하여 JAK2V617F 돌연변이를 보유한 이상 조혈모세포의 과증식을 억제하고 면역 조절 효과를 발휘합니다. 이를 통해 골수증식성 종양(Myeloproliferative Neoplasm)의 일종인 진성 적혈구 증가증(PV)을 치료합니다.

**Laubry-Pezzi 증후군**은 선천성 대동맥판 역류에 심실중격결손이 동반되는 구조적 심장 기형입니다. 이 질환의 표준 치료는 외과적 교정이며, 약물 치료는 합병증 관리에 국한됩니다. JAK-STAT 억제 기전이나 인터페론의 면역 조절 효과가 선천성 심장 구조 결함에 영향을 미칠 수 있다는 근거는 현재 문헌에서 보고된 바 없습니다. 오히려 인터페론은 심장 독성(부정맥, 심근병증)이 알려진 부작용으로, 심장 질환 환자에게의 적용은 안전성 측면에서도 우려가 있습니다.

이번 예측 Top 10의 적응증 분포를 보면, Laubry-Pezzi 증후군 외에도 심실중격 동맥류, Pierre Robin 증후군(유전성/염색체 이상형), 7번 및 22번 염색체 장완 부분 결실, Jeune 증후군, 구강안면 열구 증후군, 폐동맥판 질환 등 **대부분 선천성 구조 기형 또는 유전 질환**으로 구성되어 있습니다. 이들은 모두 ropeginterferon alfa-2b의 알려진 기전 범주에서 벗어나며, TxGNN 모델의 그래프 기반 패턴 매칭 과정에서 발생한 예측으로 해석됩니다.

---

## 임상시험 근거

현재 Laubry-Pezzi 증후군에 대한 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 Laubry-Pezzi 증후군에 대한 관련 문헌이 없습니다.

> **⚠️ 데이터 품질 주의**: 예측 적응증 6위 「disorder of fucoglycosan synthesis」 항목에서 4편의 문헌이 조회되었으나, 이들은 모두 **진성 적혈구 증가증(PV) 연구**임이 확인되었습니다. 문헌 귀속 오류로 판단되며, 해당 적응증의 근거로 계산해서는 안 됩니다.
>
> | PMID | 연도 | 유형 | 저널 | 실제 주제 |
> |------|------|------|------|---------|
> | [33476571](https://pubmed.ncbi.nlm.nih.gov/33476571/) | 2021 | RCT | Lancet Haematology | 저위험 PV에서 ropeginterferon vs 사혈 비교 |
> | [32034662](https://pubmed.ncbi.nlm.nih.gov/32034662/) | 2020 | Review | Curr Hematol Malig Rep | PV 신규 치료 옵션 고찰 |
> | [40770048](https://pubmed.ncbi.nlm.nih.gov/40770048/) | 2025 | Cohort | Blood Cancer Journal | PV에서 NLR과 JAK2 억제 반응 간 연관성 |
> | [32814349](https://pubmed.ncbi.nlm.nih.gov/32814349/) | 2021 | Cohort | Blood | 생식계열 유전 인자가 PV IFN 치료 반응에 미치는 영향 |

---

## 한국 시판 정보

한국 내 ropeginterferon alfa-2b 허가 제품이 없습니다. (허가증 0건, 미출시)

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
Laubry-Pezzi 증후군은 선천성 심장 구조 기형으로, ropeginterferon alfa-2b의 JAK-STAT 억제 기전과 생물학적 연관성이 없습니다. 이를 지지하는 임상시험도 문헌도 존재하지 않으며, Top 10 예측 전체가 동일한 L5 / Hold 판정을 받아 현 단계에서 재창출 가능성이 낮습니다.

**진행하려면 필요한 것:**
- 한국 MFDS 허가 자료 및 경고/금기 사항 수집 (현재 차단 데이터 갭)
- DrugBank API를 통한 상세 MOA 데이터 확보
- 증거 수집 시스템의 문헌 귀속 오류 수정 (Rank 6 fucoglycosan 항목)
- 재창출 후보 재탐색 시 PV 관련 적응증(본태성 혈소판증가증, 골수섬유증, 진성 적혈구 증가증 합병증 등) 중심으로 별도 Evidence Pack 구성 권장
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

