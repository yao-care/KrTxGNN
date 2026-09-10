---
layout: default
title: Midazolam
parent: 僅模型預測 (L5)
nav_order: 478
evidence_level: L5
indication_count: 1
---

# Midazolam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Midazolam: 마취 유도·진정에서 불면증으로

## 한 문장 요약

Midazolam은 단시간형 벤조디아제핀 계열 약물로, 현재 주로 마취 유도 및 처치 시 진정 목적으로 사용됩니다. TxGNN 모델은 **불면증(Insomnia)**에 효과가 있을 수 있다고 예측하며(예측 점수 99.74%), 1980~90년대에 수행된 **4건의 RCT**와 **32건의 관련 임상시험**, **11편의 문헌**이 이 방향과 관련이 있으나, 한국(대만)에는 허가된 제품이 없고 안전성 라벨 데이터가 없어 초기 연구 단계에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정식 허가 데이터 없음 (일반적으로 마취 유도 및 처치 시 진정에 사용) |
| 예측 신규 적응증 | 불면증 (Insomnia) |
| TxGNN 예측 점수 | 99.74% |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

공식 DrugBank MOA 필드는 데이터 갭이나, 예측 근거 자료에는 기전 설명이 포함되어 있습니다. Midazolam은 단시간형 벤조디아제핀(benzodiazepine) 계열 약물로, GABA-A 수용체에 양성 알로스테릭 조절을 가하여 염소이온 통로의 개방 빈도를 증가시키고, 이를 통해 진정·최면·항불안·순행성 기억상실 작용을 나타냅니다. 이 기전은 수면 유도 가능성을 이론적으로 뒷받침합니다.

다만 반감기가 매우 짧고(1.5~2.5시간), 의존·남용 위험이 높아 현재 주요 승인 적응증은 마취 유도 및 처치 시 진정이며, 만성 불면증 치료제로는 사용되지 않습니다. 즉 약리 기전상으로는 타당하지만 임상 적용성은 제한적인 전형적 사례로 평가됩니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT06407518](https://clinicaltrials.gov/study/NCT06407518) | NA | 모집 중 | 280 | 수면장애/불안이 있는 대장암 수술 환자에서 수술 전 경구 midazolam 투여가 수술 후 통증에 미치는 영향 평가 |
| [NCT02142595](https://clinicaltrials.gov/study/NCT02142595) | Phase 4 | 완료 | 111 | 경요도 전립선 절제술 환자에서 dexmedetomidine vs midazolam 진정이 수술 후 수면의 질에 미치는 영향 비교 |
| [NCT01966315](https://clinicaltrials.gov/study/NCT01966315) | N/A | 중단 | 5 | 기계환기 중환자실 환자 대상 24시간 수면다원검사로 dexmedetomidine vs midazolam 수면의 질·양 비교, 섬망 발생률도 비교 |
| [NCT00826553](https://clinicaltrials.gov/study/NCT00826553) | Phase 1 | 중단 | 6 | 기계환기 환자에서 α2 작용제(dexmedetomidine) vs GABA 작용제(midazolam 계열) 진정이 수면 단계·총 수면시간에 미치는 영향(수면다원검사) 비교 |
| [NCT00744380](https://clinicaltrials.gov/study/NCT00744380) | NA | 완료 | 23 | 내외과 중환자실에서 발관을 앞둔 환자의 벤조디아제핀 진정을 dexmedetomidine으로 전환하는 것의 유용성·안전성·비용 평가 (기존 midazolam 진정과 비교) |
| [NCT04082767](https://clinicaltrials.gov/study/NCT04082767) | Phase 3 | 불명 | 120 | 중증 소아 인공호흡 환자에서 dexmedetomidine vs midazolam 진정 효과 및 초조·섬망 관련 이상반응 비교 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [6138072](https://pubmed.ncbi.nlm.nih.gov/6138072/) | 1983 | RCT | British Journal of Clinical Pharmacology | 신경근육질환에 의한 불면증 환자 30명 대상 이중맹검시험. Midazolam 15mg과 Vesparax를 비교, midazolam이 유효한 최면제이며 내약성이 더 우수하고 숙취 효과가 없었음 |
| [2121802](https://pubmed.ncbi.nlm.nih.gov/2121802/) | 1990 | RCT | Journal of Clinical Psychopharmacology | 만성 불면증 환자 대상 14일간 flurazepam과 midazolam 투여 후 수면·수행능력·혈중농도를 비교한 다기관 무작위 이중맹검 연구 |
| [6120704](https://pubmed.ncbi.nlm.nih.gov/6120704/) | 1981 | RCT | Arzneimittel-Forschung | 경증~중등도 불면증 환자 75명 대상 경구 midazolam(10~30mg) 용량설정 다기관 시험, 효능과 내약성 평가 |
| [2229461](https://pubmed.ncbi.nlm.nih.gov/2229461/) | 1990 | RCT | Journal of Clinical Psychopharmacology | 만성 불면증 환자 대상 14일간 flurazepam·midazolam 사용에 관한 다기관 연구 요약본 (PMID 2121802의 동반 논문) |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Review | Acta Psychiatrica Scandinavica Supplementum | 최면제 임상 사용에 관한 총설. 다양한 약동학적 프로파일을 가진 벤조디아제핀계 최면제(midazolam 포함)의 적응증별 선택 기준 논의 |

## 한국 시판 정보

한국(대만) 내 허가된 Midazolam 제품 정보가 없습니다 (미시판, 허가증 0건).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (주요 경고·금기·약물상호작용 데이터 모두 확보되지 않았으며, TFDA 라벨 데이터는 Blocking 등급 데이터 갭으로 분류되어 있습니다.)

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 한국(대만)에 허가된 제품이 없어 시판 근거 자체가 부재하며, TFDA 라벨 경고/금기 데이터가 Blocking 등급 데이터 갭으로 안전성 초기평가(S1)에 진입할 수 없습니다.
- 벤조디아제핀 특성상 반감기가 짧고 의존·남용 위험이 높아, 기전상 수면 유도는 타당하나 만성 불면증 장기 치료제로서의 적합성은 제한적입니다.
- 관련 임상시험 대부분(NCT02142595, NCT01966315, NCT00826553, NCT00744380, NCT04082767 등)이 불면증 치료 자체가 아닌 수술 전후·중환자실 진정 맥락에서 수면의 질을 부수적으로 평가한 연구이며, 직접적인 만성 불면증 치료 목적의 근래 임상시험은 확인되지 않았습니다.

**진행하려면 필요한 것:**
- TFDA(또는 한국 MFDS) 허가 라벨의 경고·금기사항 확보 (DG001 해소)
- DrugBank 작용기전(MOA) 상세 데이터 확보 (DG002 해소)
- 약물상호작용(DDI) 데이터 재조회
- 만성 불면증 환자를 대상으로 한 현대적 전향적 임상시험 설계 (현재 근거는 대부분 1980~90년대 소규모 연구 또는 수술·중환자 맥락)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

