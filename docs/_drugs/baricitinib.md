---
layout: default
title: Baricitinib
parent: 僅模型預測 (L5)
nav_order: 122
evidence_level: L5
indication_count: 2
---

# Baricitinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Baricitinib: 한국 미허가에서 결손성 소안구증-근위절 이형성 증후군으로

---

## 한 문장 요약

Baricitinib은 JAK1/JAK2 억제제로, 해외에서 류마티스 관절염 등 자가면역 질환 치료에 사용되고 있으나 현재 한국에는 시판 허가 이력이 등록되어 있지 않습니다.
TxGNN 모델은 **결손성 소안구증-근위절 이형성 증후군(Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome)**에 효과가 있을 수 있다고 예측하였으나,
현재 이를 지지하는 **임상시험 및 문헌 근거가 전무**합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (한국 미허가) |
| 예측 신규 적응증 | 결손성 소안구증-근위절 이형성 증후군 (Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome) |
| TxGNN 예측 점수 | 99.94% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

공식 작용 기전(MOA) 데이터는 본 Evidence Pack에 포함되어 있지 않습니다. 그러나 기전 분석 자료에 따르면, Baricitinib은 **JAK1/JAK2를 억제하여 STAT1/STAT3 인산화를 조절**하는 JAK 억제제로, 자가면역 및 염증성 질환에서 사이토카인 신호 전달을 차단하는 방식으로 작용합니다. 눈 신생혈관 측면에서 JAK-STAT 경로가 VEGF와 간접적으로 관련된다는 점은 알려져 있습니다.

그러나 **결손성 소안구증-근위절 이형성 증후군**은 배아기 시각컵(optic cup) 폐쇄 결함에 기인한 **선천성 발달 기형**으로, PAX2·STRA6·GDF3·SOX2 등의 유전자 돌연변이가 주된 원인입니다. 이 질환의 병태생리는 염증이 아닌 배아 발달 프로그램의 이상에 해당하며, 근위절 이형성증 역시 BMP/FGFR 골격 발달 경로와 연관된 발달성 유전 결함입니다. JAK 억제와 이 질환들 사이에는 명확한 약리적 연결 고리가 없습니다.

TxGNN이 높은 점수를 부여한 것은 지식 그래프(KG) 내 공유 노드(공병증 또는 약물-유전자 간접 연관)에 기인한 것으로 추정되며, 이 예측이 직접적인 치료 기전을 반영한다고 보기 어렵습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 한국 시판 정보

현재 한국에 등록된 Baricitinib 허가증이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
이 예측은 L5 수준으로, TxGNN 모델 예측만 존재하며 임상시험 및 문헌 근거가 전무합니다. 대상 질환이 선천성 발달 기형으로, 성숙한 면역세포의 JAK-STAT 통로를 억제하는 Baricitinib과의 기전적 연결이 극히 미약하여 재창출 가능성이 낮습니다.

**진행하려면 필요한 것:**
- Baricitinib 공식 MOA 데이터 확보 (DrugBank API 조회, DG002 해소)
- 한국·해외 허가 현황 확인 (MFDS, FDA, EMA 교차 검토, DG001 해소)
- 희귀 유전 질환 전문가 검토를 통한 기전 타당성 평가
- 대상 질환의 병태생리와 JAK-STAT 경로 간 연관성 추가 조사
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

