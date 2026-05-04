---
layout: default
title: Cyanocobalamin
parent: 僅模型預測 (L5)
nav_order: 188
evidence_level: L5
indication_count: 1
---

# Cyanocobalamin
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

# Cyanocobalamin: 비타민 B12 결핍에서 바이오틴 대사 질환으로

## 한 문장 요약

Cyanocobalamin은 비타민 B12의 약학적 형태로, 원래 비타민 B12 결핍 및 악성 빈혈 치료에 사용되었습니다.
TxGNN 모델은 **바이오틴 대사 질환(Biotin Metabolic Disease)**에 효과가 있을 수 있다고 예측하며,
현재 **15건의 임상시험**과 **20편의 문헌**이 검색되었으나, 해당 적응증에 대한 직접적인 치료 근거는 아직 부족합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 정보 없음 (한국 미허가) |
| 예측 신규 적응증 | 바이오틴 대사 질환 (Biotin Metabolic Disease) |
| TxGNN 예측 점수 | 99.60% |
| 근거 수준 | L4 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Cyanocobalamin(비타민 B12)과 바이오틴(비타민 B7)은 **프로피온산(propionate) 대사 경로**를 연속적으로 공유합니다. 바이오틴 의존성 효소인 Propionyl-CoA carboxylase가 propionyl-CoA를 methylmalonyl-CoA로 전환하면, 이어지는 단계에서 methylmalonyl-CoA → succinyl-CoA 전환에 adenosylcobalamin(B12의 보조효소 형태)이 필수적으로 관여합니다. 즉, 두 비타민은 동일한 대사 축에서 순차적으로 작용합니다.

바이오틴 대사 질환(biotinidase deficiency 또는 holocarboxylase synthetase deficiency)에서는 프로피온산이 축적되며, 이로 인해 B12 의존성 메틸말론산 대사가 이차적으로 교란될 수 있습니다. Baumgartner(2013, PMID:23622402)는 cobalamin과 biotin을 '비타민 반응성 대사 질환' 범주에 함께 기술하며 공동 치료 가능성을 시사합니다. 1991년 Barshop 등(PMID:1909779)의 임상 연구에서도 B12 반응성 메틸말론산혈증(MMA) 환자군에서 cyanocobalamin 보충이 프로피온산 대사에 직접적 영향을 미침을 보고한 바 있습니다.

다만, 바이오틴 대사 질환의 1차 치료는 바이오틴 보충이며, Cyanocobalamin이 해당 적응증에서 독립적인 임상 효능을 보여주는 전향적 연구는 현재까지 존재하지 않습니다. TxGNN 점수 0.9960은 지식 그래프/딥러닝 모델의 예측값으로, 대사 경로의 연결성을 반영할 뿐 임상적 검증을 의미하지 않습니다.

---

## 임상시험 근거

검색된 15건의 임상시험 중 바이오틴 대사 질환에 대한 Cyanocobalamin의 직접 치료 효능을 평가한 시험은 없습니다. 관련성이 가장 높은 시험을 아래에 나열합니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02426775](https://clinicaltrials.gov/study/NCT02426775) | Phase 3 | 완료 | 33 | 프로피온산혈증(PA) 및 메틸말론산혈증(MMA) 환자 대상 Carglumic Acid(Carbaglu®) 장기 효능·안전성 무작위 다기관 비교 시험. 유기산혈증 대사 질환 군에 간접적 관련성 있음. |
| [NCT05687474](https://clinicaltrials.gov/study/NCT05687474) | N/A | 완료 | 6,824 | 신생아 유전체 스크리닝(Baby Detect): 126개 희귀 유전 질환 조기 발견 프로그램. 바이오틴 대사 질환 포함, 유병률 및 유행병학적 배경 데이터 제공. |
| [NCT03655223](https://clinicaltrials.gov/study/NCT03655223) | N/A | 모집 중(초청) | 30,000 | 신생아 희귀 질환 사전 증상 임상시험 촉진 프로그램(Early Check). 바이오틴 대사 질환 포함 희귀 질환 조기 진단 및 치료 연계. |
| [NCT01173315](https://clinicaltrials.gov/study/NCT01173315) | Phase 2 | 완료 | 75 | 제2형 당뇨 환자의 신경병증·신증에 대한 비타민·미네랄 복합 보충 RCT. 적응증이 당뇨 합병증으로 목표 적응증과 직접 일치하지 않음. |
| [NCT04312152](https://clinicaltrials.gov/study/NCT04312152) | N/A | 불명 | 200 | 자폐증 및 Phelan-McDermid 증후군 환자 대상 Q10 ubiquinol + 비타민 B/E 복합 대사 지지 치료 이중맹검 교차 RCT. 대사 지지 목적이나 목표 적응증과 직접 관련 없음. |
| [NCT05832190](https://clinicaltrials.gov/study/NCT05832190) | N/A | 중단 | 5 | 비만대사수술 전 섬유소+바이오틴 보충으로 장내 미생물 개선 연구. 바이오틴 직접 포함이나 n=5에서 조기 중단. |
| [NCT03444155](https://clinicaltrials.gov/study/NCT03444155) | N/A | 완료 | 30 | 천연 vs 합성 비타민 B 복합체 생체이용률 비교(교차설계). Cyanocobalamin 포함이나 소규모이며 바이오틴 대사 질환 대상 아님. |
| [NCT01474486](https://clinicaltrials.gov/study/NCT01474486) | N/A | 완료 | 40 | 울혈성 심부전 환자 대상 복합 미량영양소 완화 치료 타당성 연구. Cyanocobalamin 포함 복합제이나 목표 적응증과 무관. |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Narrative Review | Handbook of Clinical Neurology | Cobalamin과 biotin을 '비타민 반응성 대사 질환' 범주에 함께 기술. 코발라민·폴레이트 대사 이상 희귀 유전 질환의 진단 및 치료 체계 제시. |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Comparative Review | Int J Mol Sci | VitB12가 methylmalonyl-CoA → succinyl-CoA 전환(biotin 연계 경로) 및 메티오닌 합성에 보조인자로 작용함을 명시. 신경계에서의 분자·세포 기전 심층 분석. |
| [1909779](https://pubmed.ncbi.nlm.nih.gov/1909779/) | 1991 | 임상 연구 | Pediatric Research | 프로피온산혈증(PA)·메틸말론산혈증(MMA) 환자에서 1-13C-프로피온산 대사 연구. B12 반응성 MMA 환자 포함, cyanocobalamin과 propionate 대사 연결성 직접 확인. |
| [958746](https://pubmed.ncbi.nlm.nih.gov/958746/) | 1976 | Case Series/Review | Pediatric Clinics of North America | B군 비타민을 보조인자로 사용하는 아미노산 대사 이상에 대한 대용량 비타민 치료. 특정 효소 진단 후 보조인자 요법의 임상 근거 제시. |
| [11031989](https://pubmed.ncbi.nlm.nih.gov/11031989/) | 2000 | Review | Ryoikibetsu Shokogun Shirisu | 비타민 의존성 증후군의 분류·진단 기준 및 치료 원칙 검토. Cobalamin 의존성 효소 이상 포함. |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review | Acta Vitaminologica et Enzymologica | 대사 질환 병인에서 비타민의 역할(흡수 장애, 대사 이상, 비타민 의존성 증후군) 검토. B군 비타민의 선천성 대사 이상 관련성 총괄. |
| [6152513](https://pubmed.ncbi.nlm.nih.gov/6152513/) | 1983 | Review | Advances in Clinical Chemistry | 비타민 반응성 선천성 대사 이상 종합 검토. Cobalamin 반응성 질환 포함. |
| [7004517](https://pubmed.ncbi.nlm.nih.gov/7004517/) | 1980 | Review | Birth Defects Original Article Series | 대용량 비타민 요법에 의한 효소 기능 조절 기전 기술. B12 포함 보조인자 보충의 작용 원리 정리. |
| [36476407](https://pubmed.ncbi.nlm.nih.gov/36476407/) | 2023 | 동물 실험 | J Endocrinology | 암컷 쥐에서 비타민 B12 결핍이 포도당 불내성·인슐린 분비 지연·케토체 생성 촉진을 유발. B12 결핍과 대사 이상의 직접적 연관성을 동물 모델로 제시. |
| [4609643](https://pubmed.ncbi.nlm.nih.gov/4609643/) | 1974 | Review | Clinics in Endocrinology & Metabolism | 유기산 대사 이상의 선천성 오류 검토. 메틸말론산혈증 등 B12 관련 유기산혈증 진단·치료 포함. |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
검색된 임상시험 15건 및 문헌 20편 중 Cyanocobalamin을 바이오틴 대사 질환에 직접 적용한 전향적 치료 연구가 전무하며, 기전·리뷰 수준(L4)의 간접 근거만 존재합니다. 바이오틴 대사 질환의 1차 치료는 바이오틴 보충으로 확립되어 있고, 한국 내 허가·시판 현황도 없어 현 시점에서 추가 임상 개발을 결정하기에 근거가 불충분합니다.

**진행하려면 필요한 것:**
- Cyanocobalamin의 상세 작용 기전(MOA) 데이터 확보 (DrugBank API 조회, DG002 해소)
- 한국 및 국제 허가사항 상 안전성 정보(경고, 금기) 확보 (DG001 해소)
- 바이오틴 대사 질환(biotinidase deficiency, B12 반응성 MMA 등)에서 cyanocobalamin 보조 치료를 평가하는 전향적 파일럿 연구 계획 수립
- 유기산혈증·선천성 대사 이상 전문 임상의와의 자문을 통한 생물학적 타당성 재평가
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

