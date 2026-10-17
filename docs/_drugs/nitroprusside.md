---
layout: default
title: Nitroprusside
parent: 모델 예측만 (L5)
nav_order: 550
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Nitroprusside: 예측 신규 적응증 편두통 (migraine disorder) (근거 수준 L5). 기존 적응증: 허가 적응증 문구 확인 불가 (허가 문서 링크만 확인됨)"
monitor_inn: "nitroprusside"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "alopecia", "congenital hypotrichosis milia", "diffuse alopecia areata", "hypotrichosis simplex of the scalp", "migraine with or without aura, susceptibility to", "pulmonary hypertension", "benign prostatic hyperplasia (disease)", "kyphoscoliotic heart disease"]
---

# Nitroprusside
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

# Nitroprusside: 고혈압성 응급 치료에서 편두통으로

## 한 문장 요약

Nitroprusside(나이트로프레스주)는 한국에서 주사제로 허가된 혈관확장제입니다. 원래는 혈압 조절 목적으로 사용되었으며, 정확한 허가 적응증 문구는 이번 데이터에서 확인되지 않았습니다.
TxGNN 모델은 **편두통(migraine disorder)**에 효과가 있을 수 있다고 예측하지만, 임상시험은 **0건**이고 문헌 20편은 대부분 전임상 연구 또는 인체 생리 연구입니다. 특히 이 약은 편두통을 치료하기보다 유발하는 모델에 쓰이는 약물이어서, 근거가 예측을 지지한다고 보기 어렵습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 문구 확인 불가 (허가 문서 링크만 확인됨) |
| 예측 신규 적응증 | 편두통 (migraine disorder) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L4 (전임상·기전 연구 수준) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 nitroprusside는 일산화질소(NO) 공여체로, 가용성 구아닐산 고리화효소를 활성화해 cGMP를 높이고 혈관을 확장시킵니다.

NO와 CGRP 신호전달은 모두 편두통 병태생리와 관련이 있습니다. 그러나 NO 공여체는 편두통 유사 발작을 **유발**하는 것으로 알려져 있습니다. 실제로 이번 문헌 중 다수가 nitroprusside를 편두통 동물 모델의 유발 물질로 사용했습니다. 따라서 이 연관성은 치료 근거라기보다 경로 관련성 신호 또는 유발 모델에 가깝습니다. 높은 TxGNN 점수는 NO/cGMP 생물학에서의 네트워크 근접성을 반영했을 가능성이 큽니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [39988876](https://pubmed.ncbi.nlm.nih.gov/39988876/) | 2025 | 전임상(마우스) | Cephalalgia | CBD와 THC 병용이 CGRP, SNP, 피질 확산성 탈분극으로 유발한 편두통 유사 행동을 완화 (SNP는 유발 물질) |
| [38215227](https://pubmed.ncbi.nlm.nih.gov/38215227/) | 2024 | 전임상(마우스) | Cephalalgia | CGRP 수용체 길항이 편두통 모델의 멀미 지표를 감소 |
| [36697259](https://pubmed.ncbi.nlm.nih.gov/36697259/) | 2023 | 전임상 | J Neurosci | NO 공여체 유발 편두통 모델에서 퍼옥시나이트라이트가 행동 반응과 삼차신경 흥분성에 기여 |
| [36299248](https://pubmed.ncbi.nlm.nih.gov/36299248/) | 2023 | 전임상(마우스) | Brain | MNK1/2가 편두통 모델의 안와 주위 과민과 통각과민 프라이밍에 기여 |
| [21122149](https://pubmed.ncbi.nlm.nih.gov/21122149/) | 2010 | 횡단 연구(인체) | BMC Neurol | 편두통 환자의 내피 기능 평가 (치료 효과 아님) |
| [19528518](https://pubmed.ncbi.nlm.nih.gov/19528518/) | 2009 | 인체 생리 연구 | Neurology | 편두통 환자에서 혈관 평활근 세포 기능 이상 |
| [18384419](https://pubmed.ncbi.nlm.nih.gov/18384419/) | 2008 | 인체 생리 비교 | Cephalalgia | 편두통 환자와 대조군의 말초 미세순환에서 CGRP·NO 반응 비교 |
| [16396667](https://pubmed.ncbi.nlm.nih.gov/16396667/) | 2006 | 인체 생리 연구 | Cephalalgia | 편두통 환자 10명과 대조군의 NO·CGRP에 대한 전완 혈관 반응 비교 |
| [11921057](https://pubmed.ncbi.nlm.nih.gov/11921057/) | 2002 | 기전 연구 | Ann Neurol | NO 공여체가 iNOS 발현을 증가시키며 NF-κB가 편두통 치료 표적이 될 가능성 |
| [6745825](https://pubmed.ncbi.nlm.nih.gov/6745825/) | 1984 | 임상 보고 | Fortschr Med | 편두통에 쓰는 에르고타민 중독의 혈관 연축을 nitroprusside로 치료 (편두통 자체 치료 아님) |

위 10편 외에 전임상 연구와 주제와 거리가 있는 연구도 포함되어 있습니다. 가장 큰 한계는 nitroprusside가 편두통을 치료한다는 직접 근거가 없다는 점입니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200803322 | 나이트로프레스주(니트로푸루시드나트륨) | 갈색 바이알에 들어있는 주홍색의 투명한 액 (주사제) | 허가 문서 참조 (한국화이자제약) |

## 안전성 고려사항

- **약물 상호작용**: 총 58건이 확인되었으며, 표시된 항목은 모두 중등도입니다. 주요 항목은 다음과 같습니다.
  - 코르티코스테로이드: hydrocortisone, prednisolone, prednisone, dexamethasone, betamethasone, triamcinolone, budesonide
  - SGLT2 억제제: canagliflozin, dapagliflozin, empagliflozin, ertugliflozin
  - 기타: bupropion, morphine, opium, dronabinol, nabilone, promethazine, amifostine, sapropterin, iodide I-123

경고와 금기 등 그 밖의 안전성 정보는 허가사항을 참조하세요. 문헌에서는 전신 저혈압과 시안화물 독성 위험이 이 약의 사용을 제한하는 요인으로 언급됩니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
편두통에 대한 임상시험이 없고, 문헌은 전임상 및 인체 생리 연구 위주입니다. 또한 nitroprusside는 편두통 유발 물질로 알려져 있어 치료 가설과 방향이 반대입니다.

**참고: 다른 예측 적응증**
- **폐고혈압**(근거 수준 L3): 혈관확장 기전이 직접 관련되며, 주술기 흡입 혈관확장제 비교 연구 등이 있습니다. 다만 소규모·주술기 연구 위주이고 전신 저혈압과 시안화물 독성 한계가 있어 후속 연구 질문 수준입니다.
- **편두통 관련 질환**(뇌줄기 조짐 편두통, 편두통 감수성): L4, Hold.
- **양성 전립선 비대증**(L4, Hold), **탈모 관련 질환과 후만측만성 심장질환**(L5, Hold): 직접 근거가 없습니다.

**진행하려면 필요한 것:**
- 허가 적응증 원문과 경고·금기 등 허가사항 확보 (현재 안전성 선별 불가)
- 상세한 약물 작용 기전(MOA) 데이터 보완
- 편두통에서 치료 효과를 시사하는 인체 데이터 (현재는 유발 모델 근거만 있음)
- 신규 적응증 우선순위를 폐고혈압으로 재검토하고, 흡입 투여 등 투여 경로 타당성과 안전성 평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

