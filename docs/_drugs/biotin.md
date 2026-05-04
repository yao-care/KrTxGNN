---
layout: default
title: Biotin
parent: 僅模型預測 (L5)
nav_order: 143
evidence_level: L5
indication_count: 2
---

# Biotin
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

# BIOTIN: 영양 보충에서 소화불량(Dyspepsia)으로

---

## 한 문장 요약

BIOTIN(비오틴, Vitamin B7)은 다양한 효소의 보조인자(cofactor)로 작용하는 수용성 비타민으로, 주로 영양 결핍 보충 목적으로 알려져 있습니다.
TxGNN 모델은 **소화불량(Dyspepsia)**에 효과가 있을 수 있다고 예측(점수 99.43%)하였으나,
현재 직접 관련 임상시험은 없으며 **7편의 문헌** 중 대부분이 간접적 연관성만 보여, 근거 수준은 매우 낮습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 없음 (대만 미허가) |
| 예측 신규 적응증 | 소화불량 (Dyspepsia) |
| TxGNN 예측 점수 | 99.43% |
| 근거 수준 | L5 |
| 대만 시판 현황 | ✗ 미상시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 BIOTIN의 상세한 작용 기전 데이터(MOA)가 확보되지 않은 상태입니다. 알려진 생화학적 역할에 의하면, Biotin은 **피루브산 카르복실화효소(pyruvate carboxylase), 아세틸-CoA 카르복실화효소** 등 다수 카르복실화효소의 보조인자로서 에너지 대사, 지방산 합성, 포도당 신생합성에 관여합니다.

소화불량과의 기전적 연결 가설은 다음과 같습니다: Biotin이 장관 점막 상피세포의 에너지 대사와 지방산 합성을 지원함으로써 위장관 점막 완전성(mucosal integrity)을 유지하는 데 기여할 수 있다는 이론적 추론입니다. 그러나 이 기전 연결은 현재 **직접적인 실험 또는 임상 데이터로 뒷받침되지 않은 가설 수준**에 머물러 있습니다.

기존 적응증(영양 보충)과 소화불량의 유사성 측면에서, 비오틴 결핍 시 소화기 증상이 동반될 수 있다는 증례 보고가 존재하지만, 이는 결핍 교정과 소화불량 치료를 직접 동일시할 수 없습니다. 현 단계에서 TxGNN 예측의 생물학적 타당성은 낮으며, 추가 기전 연구가 선행되어야 합니다.

---

## 임상시험 근거

아래 두 건의 시험이 검색되었으나, **모두 Biotin 및 소화불량과의 직접적 관련성이 없는 것으로 평가(Grade C)**됩니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT05389813](https://clinicaltrials.gov/study/NCT05389813) | Phase 2/3 | UNKNOWN | 150 | 복강경 담낭절제술 등 4종 수술 후 통증 조절을 위해 Oxycodone vs Pregabalin을 비교한 시험. Biotin 및 소화불량 모두 무관. |
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | 완료 | 99 | 비만대사수술 후 환자에서 경피패치를 통한 비타민 흡수 관찰 연구. Biotin이 비타민 혼합물에 포함될 수 있으나, 소화불량 치료 목적이 아님. |

> ⚠️ **주의**: 위 두 건은 모두 소화불량에서 Biotin의 효능을 평가한 시험이 아닙니다. 적응증 관련 임상시험은 사실상 없는 것으로 판단됩니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [25384804](https://pubmed.ncbi.nlm.nih.gov/25384804/) | 2014 | Cohort/Interventional | Minerva Gastroenterol Dietol | H. pylori 치료 후 기능성 소화불량 환자에서 알긴산나트륨, 파파야, 생강 등 복합 보충제(Biotin 포함 가능성) 투여 효과 평가. Biotin 단독 효과는 불분명. |
| [15863846](https://pubmed.ncbi.nlm.nih.gov/15863846/) | 2005 | Case Report | J Dermatology | 소화불량 진단을 받아 아미노산 분유만 섭취한 생후 5개월 영아에서 비오틴 결핍 발생 사례. 소화불량과 비오틴의 연관성은 우연적 공존. |
| [21695955](https://pubmed.ncbi.nlm.nih.gov/21695955/) | 2011 | Review/Interventional | Exp Clin Gastroenterology | 항생제 치료 중인 기관지폐 질환 환자에서 Inulin, Oligofructose, Biotin 등을 포함한 복합 보충제(Stimbifid)의 장내 미생물 교정 효과 평가. 소화불량 직접 연구 아님. |
| [25110039](https://pubmed.ncbi.nlm.nih.gov/25110039/) | 2014 | Observational | Int J Mol Med | 과민성 장 증후군(IBS) 환자에서 위 전정부 내분비 세포 변화 관찰. Biotin 무관. |
| [24891930](https://pubmed.ncbi.nlm.nih.gov/24891930/) | 2014 | Observational | World J Gastrointest Endoscopy | IBS 환자에서 위 산분비 점막 내분비 세포 유형 연구. Biotin 무관. |
| [11304845](https://pubmed.ncbi.nlm.nih.gov/11304845/) | 2001 | Observational | J Clin Pathology | H. pylori 연관 위염에서 IL-10의 역할 연구. Biotin 무관. |
| [10354275](https://pubmed.ncbi.nlm.nih.gov/10354275/) | 1999 | Observational | Kidney International | IgA 신증에서 소장 점막 염증 및 스트레스 단백질 연구. Biotin 무관. |

> ⚠️ **주의**: 7편 중 Biotin과 소화불량을 직접 연결하는 연구는 없으며, 대부분은 간접적 언급 또는 무관한 주제입니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
Biotin과 소화불량 사이의 연관성을 직접 지지하는 임상시험 및 문헌이 존재하지 않으며, TxGNN 모델의 예측만이 근거의 전부인 L5 수준입니다. 기전적 연결 가설은 이론적으로 제시 가능하나 실험 데이터가 없어 현 단계에서 재창출 타당성을 지지하기 어렵습니다.

**진행하려면 필요한 것:**
- Biotin의 상세 작용 기전(MOA) 데이터 확보 (DrugBank API 조회)
- 대만/한국 허가 사항 및 안전성 정보(경고, 금기) 확보
- Biotin이 위장관 점막 기능에 미치는 영향을 탐색한 전임상(in vitro/in vivo) 연구 검토
- 소화불량 관련 Biotin 직접 연구 또는 복합제 내 Biotin 역할을 규명한 문헌 추가 탐색
- TxGNN 예측 순위(9,320위)가 매우 낮다는 점을 감안, 상위 예측 적응증으로 우선순위 재검토 권고
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

