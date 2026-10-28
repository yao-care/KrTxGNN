---
layout: default
title: Ethanol
parent: 모델 예측만 (L5)
nav_order: 323
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Ethanol: 예측 신규 적응증 편두통 (Migraine Disorder) (근거 수준 L5). 기존 적응증: 수술 시 수술자 및 보건위생종사자의 손 소독"
monitor_inn: "ETHANOL"
predicted_indications: ["migraine disorder", "migraine with brainstem aura"]
---

# Ethanol
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **2** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 약사 평가 보고서

</div>

## Ethanol: 수술 시 손 소독에서 편두통으로
{: .text-alpha }

## 한 문장 요약

Ethanol은 원래 수술자 및 보건위생종사자의 손 소독에 사용되는 외용 소독제입니다.
TxGNN 모델은 **편두통(Migraine Disorder)**에 효과가 있을 수 있다고 예측하지만, 현재 관련 **임상시험은 0건**이며 수집된 문헌도 치료 효과가 아닌 **편두통 유발 요인**이나 유전자 연관성을 다룬 연구가 대부분입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 수술 시 수술자 및 보건위생종사자의 손 소독 |
| 예측 신규 적응증 | 편두통 (Migraine Disorder) |
| TxGNN 예측 점수 | 0.9929 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Ethanol은 외용 소독제로 허가된 단일 성분 제품이며, 손 소독 외에 치료 목적의 전신 사용 근거는 확인되지 않았습니다.

오히려 문헌은 반대 방향을 가리킵니다. Ethanol은 편두통의 알려진 유발 요인입니다. 전임상 연구(PMID 37101198)에서는 대사산물인 acetaldehyde가 Schwann 세포의 CGRP 수용체와 TRPA1을 통해 마우스의 안와 주위 기계적 이질통을 일으켰습니다. 또한 ATP 민감성 칼륨 채널 개방이 수막 통각수용체를 활성화한다는 연구(PMID 40785517)도 있습니다.

TxGNN 모델(딥러닝)의 높은 점수(0.9929)는 치료 효과보다는 모델이 관련 질환 간에 학습한 유사성을 반영했을 가능성이 높으며, 생물학적 근거를 의미하지 않습니다. 따라서 기전상 치료 적용 가능성을 뒷받침하는 근거는 현재 없습니다.

두 번째 예측인 **전조가 있는 뇌간형 편두통(Migraine with Brainstem Aura, 0.9914)**은 상위 개념인 편두통에서 점수가 이어진 것으로 보이며, 이 아형에 특화된 근거는 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

수집된 문헌 중 Ethanol 자체를 편두통 치료제로 평가한 연구는 없습니다. 관련성이 높은 문헌만 정리했습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [36373782](https://pubmed.ncbi.nlm.nih.gov/36373782/) | 2022 | Review | Headache | 알코올과 편두통의 복합적 관계를 고찰 |
| [37101198](https://pubmed.ncbi.nlm.nih.gov/37101198/) | 2023 | 전임상(동물) | J Biomed Sci | Acetaldehyde가 CGRP 수용체와 TRPA1을 통해 마우스에서 Ethanol 유발 이질통을 매개하며, 편두통 유발 기전과 관련 |
| [40785517](https://pubmed.ncbi.nlm.nih.gov/40785517/) | 2025 | 전임상(기전) | Cephalalgia | ATP 민감성 칼륨 채널 개방이 수막 통각수용체를 활성화 |
| [19486361](https://pubmed.ncbi.nlm.nih.gov/19486361/) | 2010 | 유전자 연관성 연구 | Headache | 알코올 탈수소효소(ADH2) 유전자형과 편두통 위험 연관성 조사 |
| [35063053](https://pubmed.ncbi.nlm.nih.gov/35063053/) | 2022 | 코호트 | Aerosp Med Hum Perform | 군 조종사의 편두통 병력과 결과 분석 |
| [29299688](https://pubmed.ncbi.nlm.nih.gov/29299688/) | 2018 | 유전자 연관성 연구 | J Neural Transm | GABA 수용체 유전자 다형성과 편두통 위험 |

그 외 수집된 문헌(sumatriptan 약동학, carisbamate 임상시험, pizotifen 경피 제형, menthol 외용 RCT, palmitoylethanolamide 연구 등)은 다른 약물·화합물에 관한 것이어서 Ethanol의 근거로 인정되지 않습니다. 특히 PMID 30177906은 이름에 'ethanol'이 들어 있을 뿐 다른 화합물입니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200410130 | 애바가드외용액 | 백색의 반투명 내지 불투명한 로션제 | 수술 시 수술자 및 보건위생종사자의 손 소독에 사용 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 확인되었습니다. 대부분 중등도(Moderate)이며, 주요 항목은 다음과 같습니다.
  - **Major**: Eluxadoline
  - **Moderate**: 당뇨병 치료제 계열(Acarbose, Albiglutide, Acetohexamide, Alogliptin, Canagliflozin, Chlorpropamide, Dapagliflozin, Dulaglutide, Empagliflozin 등), 항콜린제(Atropine, Clidinium, Dicyclomine), Acetylsalicylic acid, Bupropion, Dronabinol
  - **Minor**: Doxycycline, Cimetidine

주요 경고와 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 점수는 매우 높지만 임상시험이 없고, 문헌은 Ethanol을 편두통 치료제가 아닌 유발 요인으로 다루고 있어 근거 수준이 L5에 머뭅니다. 허가된 용도도 손 소독용 외용제여서 편두통 치료를 위한 약리학적 근거가 없습니다.

**진행하려면 필요한 것:**
- Ethanol이 편두통을 완화한다는 직접적인 전임상 또는 임상 근거
- 작용 기전(MOA) 데이터 확보
- 허가사항(MFDS 첨부문서)의 경고 및 금기 정보 확인
- 외용 소독제 제형과 편두통 치료에 필요한 투여 경로 간의 적합성 검토
- 편두통 유발 가능성을 고려한 안전성 평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

