---
layout: default
title: Ibuprofen
parent: 僅模型預測 (L5)
nav_order: 306
evidence_level: L5
indication_count: 7
---

# Ibuprofen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Ibuprofen: 기존 적응증 정보 없음에서 Acromesomelic Dysplasia (Hunter-Thompson type)으로

## 한 문장 요약

Ibuprofen(DrugBank ID: DB01050)은 본 Evidence Pack에 원 적응증 및 작용 기전(MOA) 정보가 제공되지 않았으며, 한국에서도 현재 허가·시판 이력이 확인되지 않습니다. TxGNN 모델은 **Acromesomelic Dysplasia, Hunter-Thompson type**을 포함해 극희귀 골격/발달성 유전질환 7건을 유사한 고득점(약 99.6~99.7%)으로 예측했으나, 관련 임상시험·문헌은 전혀 확인되지 않았고, 예측 근거 자체도 기전적 연관성이 약하다고 평가되고 있습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (Taiwan/한국 허가 정보 및 DrugBank 원 적응증 데이터 미제공) |
| 예측 신규 적응증 | Acromesomelic Dysplasia, Hunter-Thompson type |
| TxGNN 예측 점수 | 99.74% (순위 5,336위) |
| 근거 수준 | L5 (모델 예측만 있음, 실제 연구 없음) |
| 한국 시판 현황 | 시판되지 않음 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 Ibuprofen의 상세 작용 기전(MOA) 데이터는 확보되지 않았습니다 (High severity Data Gap). 다만 Evidence Pack에 포함된 기전 검토(rationale) 내용에 따르면, Acromesomelic Dysplasia, Hunter-Thompson type은 **GDF5 유전자 돌연변이로 인한 연골 발육 부전**이며, 발달성·구조적 질환으로 염증성 질환에 해당하지 않습니다.

Ibuprofen은 COX 억제제로서, 이 질환에 동반될 수 있는 관절 통증이나 이차적 염증 증상에 대해 증상 완화 효과를 기대할 수는 있으나, 질환의 근본 병리인 골격 형태형성 신호 경로 이상과는 직접적인 기전적 연관성이 없습니다.

특히 나머지 6개 예측 적응증(brachyolmia-amelogenesis imperfecta syndrome, myosclerosis, brachyolmia, brachydactyly-syndactyly syndrome, pseudoachondroplasia, colobomatous microphthalmia-rhizomelic dysplasia syndrome) 역시 모두 골격·연골·발달성 희귀질환이며, 점수(99.60~99.71%)와 순위(5,336~7,310위)가 서로 근접해 있습니다. 이는 TxGNN 지식그래프 내에서 골격 발육부전 관련 질환 노드들이 서로 군집되어 있는 데서 비롯된 패턴일 가능성이 높으며, Ibuprofen에 대한 특이적 약리학적 연관성을 반영한 결과라고 보기는 어렵습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

(주요 경고, 금기, 약물상호작용 관련 데이터가 확보되지 않았으며, 이는 S1 안전성 초평가 진입을 막는 Blocking 등급 Data Gap으로 분류되어 있습니다.)

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 예측 신규 적응증 7건 모두 임상시험·문헌 근거가 전무한 L5 단계(모델 예측만 존재)이며, decision_stage도 최하위 단계인 S0에 머물러 있습니다.
- 원 적응증·MOA 데이터, 한국 시판/허가 정보, 안전성(경고·금기·DDI) 정보가 모두 확보되지 않아 근거 사슬 자체가 성립하지 않습니다.
- 예측된 질환들은 모두 극희귀 유전성 골격/발달 질환으로, 제시된 기전 서술 자체가 "직접적 기전 연관성 없음"을 명시하고 있어 재창출 가설로서의 타당성이 낮습니다.

**진행하려면 필요한 것:**
- TFDA/한국 규제기관 공식 라벨(허가사항 PDF) 확보를 통한 경고·금기·DDI 데이터 보완 (Blocking Data Gap 해소)
- DrugBank API 조회를 통한 Ibuprofen 원 적응증 및 상세 MOA 확보 (High Data Gap 해소)
- 상위 예측 질환에 대한 추가 문헌/전임상 검색 (현재 PubMed·ClinicalTrials.gov·ICTRP 조회 결과 0건 확인됨, 재조회 주기적 필요)
- 7개 예측이 실제 개별 기전 신호인지, 지식그래프 군집 아티팩트인지 구분하기 위한 정성적 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

