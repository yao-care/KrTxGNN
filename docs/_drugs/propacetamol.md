---
layout: default
title: Propacetamol
parent: 僅模型預測 (L5)
nav_order: 580
evidence_level: L5
indication_count: 10
---

# Propacetamol
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

# Propacetamol: 진통·해열제에서 편두통으로

## 한 문장 요약

Propacetamol은 파라세타몰(아세트아미노펜)의 정맥주사용 전구약물로, 원래 통증 및 발열 완화 목적으로 사용되어 왔습니다.
TxGNN 모델은 **편두통(Migraine Disorder)**에 효과가 있을 수 있다고 예측하며,
현재 관련 임상시험 등록은 없으나 **RCT 1편을 포함한 문헌 3편**이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 통증·발열 (정맥주사용 진통해열제, 파라세타몰 전구약물) |
| 예측 신규 적응증 | 편두통 (Migraine Disorder) |
| TxGNN 예측 점수 | 99.68% |
| 근거 수준 | L3 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 확보되지 않았습니다. 다만 알려진 약리학적 정보에 따르면, Propacetamol은 체내에서 에스터라아제에 의해 가수분해되어 아세트아미노펜(파라세타몰)으로 전환되는 전구약물입니다.

아세트아미노펜은 중추신경계에서 COX 효소를 억제하고 하행 세로토닌성 억제 경로를 활성화하는 중추성 진통·해열 기전을 가지며, 이는 급성 두통·편두통 발작의 증상 완화에 국제 진료지침에서 흔히 활용되는 기전입니다.

기존의 진통·해열 적응증과 편두통 급성기 증상 관리는 통증 조절이라는 공통 치료 목표를 공유하므로, 기전상 재창출 가능성이 합리적으로 뒷받침됩니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [25002083](https://pubmed.ncbi.nlm.nih.gov/25002083/) | 2014 | RCT | European Journal of Internal Medicine | 급성 편두통 발작에서 정맥주사용 propacetamol hydrochloride의 효과 평가, 트립탄 제제 대비 위장관 부작용이 적은 대안으로 제시 |
| [14679670](https://pubmed.ncbi.nlm.nih.gov/14679670/) | 2003 | Review | Therapie | 난치성 성인 편두통 관리 전반을 다루며, 부적절한 용량·지연 치료 등 치료 실패 요인을 분석 |
| [31804357](https://pubmed.ncbi.nlm.nih.gov/31804357/) | 2019 | Case Report | Medicine | 뇌졸중형 두통(thunderclap headache)을 동반한 가역적 뇌혈관수축증후군 증례, 편두통과의 감별진단 논의 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
편두통 적응증에 대해 RCT 1건을 포함한 문헌적 근거(L3)가 존재하며, 아세트아미노펜의 중추성 진통 기전이 급성 편두통 발작 치료와 기전상 부합합니다. 다만 임상시험 등록이 전무하고 근거의 양이 제한적이므로 신중한 접근이 필요합니다.

**진행하려면 필요한 것:**
- 상세한 작용 기전(MOA) 데이터 (DrugBank API 조회 필요, DG002)
- 허가사항 경고·금기·약물상호작용 정보 (TFDA/한국 규제기관 자료, DG001 — Blocking)
- 편두통 적응증에 특화된 전향적 임상시험 설계 및 등록
- 한국 내 시판 여부 및 허가 현황 재확인 (현재 미시판)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

