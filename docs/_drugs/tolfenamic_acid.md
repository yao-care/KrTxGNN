---
layout: default
title: Tolfenamic Acid
parent: 僅模型預測 (L5)
nav_order: 684
evidence_level: L5
indication_count: 10
---

# Tolfenamic Acid
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

Using systematic approach to synthesize the Evidence Pack into the standard report format — no coding/debugging skill applies here, this is a direct content-generation task per the detailed prompt already provided.

---

# 톨페남산(Tolfenamic Acid): NSAID 계열 진통·소염제에서 두통 질환(편두통)으로

## 한 문장 요약

톨페남산은 프로스타글란딘 생합성을 억제하는 NSAID(펜아메이트계) 계열 약물로, 해외 문헌상 류마티스 관절염 및 편두통 치료에 사용된 역사가 있습니다(국내 허가 이력은 없음). TxGNN 모델은 **두통 질환(Headache Disorder)**에 효과가 있을 것으로 예측하며(예측 점수 99.74%), 현재 **20편의 문헌**(다수의 이중맹검 RCT 포함)이 이 방향을 지지합니다. 다만 국내 미출시 상태이며 안전성 자료(경고·금기·DDI)가 전무해 별도 확인이 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 국내 허가 정보 없음 (해외 문헌상 NSAID 계열 진통·소염제로 사용) |
| 예측 신규 적응증 | 두통 질환 (Headache Disorder) |
| TxGNN 예측 점수 | 99.74% |
| 근거 수준 | L2 (다수의 완료된 이중맹검 RCT, 단 현대적 Phase 표기 이전 시대 연구) |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

DrugBank의 공식 작용 기전(MOA) 필드는 현재 데이터 갭 상태이나, 수집된 문헌 자체에서 기전 정보를 확인할 수 있습니다. 톨페남산은 안트라닐산 유도체(펜아메이트계) NSAID로, "프로스타글란딘 생합성을 강력히 억제하는" 약물로 여러 논문에서 설명되며(PMID 6984358), 류코트리엔 생합성 억제 작용도 보고되어 있습니다(PMID 7816786).

편두통 병태생리에는 프로스타글란딘이 혈관 확장·부종·통각과민을 매개하는 것으로 알려져 있으며(PMID 7816790), 이는 톨페남산의 PG 억제 기전과 직접적으로 연결됩니다. 실제로 톨페남산은 1970~1990년대 북유럽(핀란드·덴마크)에서 Clotam이라는 상품명으로 급성 편두통 치료제 및 예방요법으로 널리 사용된 이력이 있어, TxGNN의 예측은 새로운 가설이라기보다 이미 확립된 약리학적 근거를 정확히 재발견한 결과로 볼 수 있습니다.

류마티스 관절염(rank 3)에서도 같은 COX 억제 기전으로 다수의 RCT가 보고되어 있어, 톨페남산의 핵심 약리 범주(NSAID)와 두통 질환 적응증 사이의 기전적 연결성은 비교적 견고합니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [9563211](https://pubmed.ncbi.nlm.nih.gov/9563211/) | 1998 | RCT | Headache | 이중맹검 무작위 병렬군 연구, 톨페남산과 경구 수마트립탄의 급성 편두통 치료 효과가 유사함을 확인 |
| [12474702](https://pubmed.ncbi.nlm.nih.gov/12474702/) | 2002 | RCT | Medicina (Kaunas) | 톨페남산 300mg vs 피조티펜, 192명 대상 전향적 이중맹검 병렬군 예방요법 비교 |
| [7976233](https://pubmed.ncbi.nlm.nih.gov/7976233/) | 1994 | RCT | Acta Neurol Scand | 76명 대상 무작위 이중맹검 교차 연구, 톨페남산과 프로프라놀롤의 편두통 예방 효과 비교 |
| [2375249](https://pubmed.ncbi.nlm.nih.gov/2375249/) | 1990 | RCT | Acta Neurol Scand | 무작위 이중맹검 교차 연구, 톨페남산과 아세트아미노펜의 편두통 급성기 효과 비교 |
| [3727918](https://pubmed.ncbi.nlm.nih.gov/3727918/) | 1986 | RCT | Acta Neurol Scand | 31명 대상 무작위 이중맹검 교차 연구, 톨페남산·프로프라놀롤·위약의 편두통 예방 효과 비교, 두 약물 모두 위약 대비 유의한 발작 감소 |
| [89390](https://pubmed.ncbi.nlm.nih.gov/89390/) | 1979 | RCT | Lancet | 20명 대상 이중맹검 교차 연구, 톨페남산이 에르고타민과 동등한 효과를 보이며 구역 등 부작용이 더 적음 |
| [7051739](https://pubmed.ncbi.nlm.nih.gov/7051739/) | 1982 | RCT | Acta Neurol Scand | 31명 대상 이중맹검 교차 위약대조 연구, 톨페남산이 발작 횟수·기간·중증도 모두에서 위약보다 유의하게 우수 |
| [6394143](https://pubmed.ncbi.nlm.nih.gov/6394143/) | 1984 | RCT | Cephalalgia | 톨페남산, 메토클로프라미드, 카페인 및 병용요법의 편두통 발작 치료 효과 비교 |
| [6984358](https://pubmed.ncbi.nlm.nih.gov/6984358/) | 1982 | RCT | Cephalalgia | 톨페남산과 카페인·메토클로프라미드·피리독신 병용요법의 급성 편두통 60회 발작 치료 결과 |
| [6691890](https://pubmed.ncbi.nlm.nih.gov/6691890/) | 1984 | Crossover PK | Br J Clin Pharmacol | 편두통 발작 및 메토클로프라미드가 톨페남산 흡수에 미치는 영향을 교차연구로 평가 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> ⚠️ 참고: 경고·금기·DDI 데이터가 모두 확보되지 않았으며(TFDA/국내 첨부문서 미수집), 이는 안전성 초기평가(S1) 진입을 막는 Blocking 등급 데이터 갭입니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
편두통 적응증에 대한 효능 근거(다수의 완료된 이중맹검 RCT, 총 20편 문헌)는 견고하나, 국내 첨부문서 기반 경고·금기·DDI 정보가 전무하여 안전성 초기평가(S1)에 진입할 수 없는 Blocking 데이터 갭이 존재합니다. 한국 내 시판 이력도 전혀 없어(허가 0건) 국내 도입 전 규제·안전성 검토가 선행되어야 합니다.

**진행하려면 필요한 것:**
- TFDA/국내 첨부문서 원문 확보 및 경고·금기 사항 파싱 (DG001, Blocking)
- DrugBank API를 통한 상세 작용 기전(MOA) 데이터 확보 (DG002)
- 약물상호작용(DDI) 데이터베이스 재조회 (현재 not_found 상태)
- 편두통 적응증에 대한 최신 등록 임상시험(ClinicalTrials.gov/ICTRP) 유무 확인
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

