---
layout: default
title: Folic Acid
parent: 僅模型預測 (L5)
nav_order: 337
evidence_level: L5
indication_count: 1
---

# Folic Acid
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

# Folic Acid: 엽산 결핍증에서 비오틴 대사 질환으로

## 한 문장 요약

Folic acid(엽산, DrugBank DB00158)는 일반적으로 엽산 결핍 및 관련 빈혈 예방·치료에 사용되는 수용성 비타민입니다. TxGNN 모델은 **비오틴 대사 질환(Biotin Metabolic Disease)**에 효과가 있을 수 있다고 예측하며(예측 점수 99.49%, 전체 순위 8,659위), 현재 **13건의 임상시험**과 **20편의 문헌**이 확보되어 있으나 대부분 일반적 비타민 보충 연구이며 이 적응증에 특화되어 직접 검증한 연구는 아직 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 엽산 결핍증 예방·치료 (일반 약리학적 용도; 이번 Evidence Pack에는 등록된 허가 적응증 데이터 없음) |
| 예측 신규 적응증 | 비오틴 대사 질환 (Biotin Metabolic Disease) |
| TxGNN 예측 점수 | 99.49% (전체 순위 8,659위 — 점수는 높지만 절대 순위는 낮아 변별력은 제한적) |
| 근거 수준 | L4 (전임상/기전 연구) |
| 한국 시판 현황 | ✗ 미상장 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 없습니다(Data Gap). 다만 알려진 정보에 따르면 엽산은 비오틴과 마찬가지로 세포 대사 반응(1탄소 전이, 카르복실화 반응 등)의 필수 보조인자로 작용하는 수용성 비타민이며, 두 물질 모두 "비타민 반응성 대사질환(vitamin-responsive metabolic disorder)" 범주에서 함께 논의되는 경우가 많습니다.

문헌 근거(PMID 23622402 등)는 코발라민·엽산·비오틴·비타민 B1·E 결핍이 공통적으로 신경학적·대사적 이상을 유발하며, 일부 선천성 대사이상 환자는 특정 비타민 대량 투여에 반응한다는 점을 보여줍니다. 이는 엽산이 비오틴 대사 경로와 보조인자 네트워크를 공유할 가능성을 시사하지만, 엽산이 비오틴 대사 질환 자체를 직접 치료한다는 임상적 근거는 아직 확인되지 않았습니다. TxGNN 예측은 이러한 "보조인자 대사 질환군" 내 근접성에서 기인한 것으로 추정되며, 순위(8,659위)가 낮은 점을 고려할 때 확증적 근거로 보기는 이릅니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT05687474](https://clinicaltrials.gov/study/NCT05687474) | N/A | 완료 | 6,824 | 신생아 유전체 스크리닝(Baby Detect)으로 비오틴 대사 질환 포함 126종의 치료 가능 유전질환 조기 발견 프로그램 |
| [NCT01173315](https://clinicaltrials.gov/study/NCT01173315) | Phase 2 | 완료 | 75 | 2형 당뇨병 환자에서 비타민·미네랄 보충이 신경병증/신증 지표에 미치는 영향 평가 |
| [NCT04586348](https://clinicaltrials.gov/study/NCT04586348) | Phase 4 | 진행 중(모집 중단) | 794 | 임산부 요오드 보충 감소가 소아 인지발달에 미치는 영향(RCT) |
| [NCT01643187](https://clinicaltrials.gov/study/NCT01643187) | Phase 2 | 불명 | 1,000 | 영양불량 소아에서 강화식품 개입, 혈청 엽산 등 미량영양소 지표 평가 |
| [NCT04312152](https://clinicaltrials.gov/study/NCT04312152) | N/A | 불명 | 200 | 자폐스펙트럼/Phelan-McDermid 증후군 환자 대상 코엔자임Q10+비타민B/E 대사 지지요법 교차 RCT |
| [NCT00572741](https://clinicaltrials.gov/study/NCT00572741) | N/A | 완료 | 39 | 자폐증의 산화스트레스 및 대사이상에 대한 표적 영양 개입 |
| [NCT03444155](https://clinicaltrials.gov/study/NCT03444155) | N/A | 완료 | 30 | 천연 vs 합성 비타민 B 복합체의 생체이용률 비교 |
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | 완료 | 99 | 비만대사수술 후 경피 비타민 흡수 및 결핍 발생률 관찰 |
| [NCT01474486](https://clinicaltrials.gov/study/NCT01474486) | N/A | 완료 | 40 | 울혈성 심부전 환자 대상 다중 미량영양소 개입의 실행 가능성 평가 |
| [NCT01558193](https://clinicaltrials.gov/study/NCT01558193) | N/A | 완료 | 202 | 다중비타민/미네랄 보충이 충동성 및 공격성에 미치는 영향 |

> 참고: 위 시험 중 비오틴 대사 질환을 직접 치료 대상으로 설계한 시험은 없으며, NCT05687474(신생아 스크리닝)를 제외하면 대부분 일반 비타민 보충 연구입니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Review | Handbook of Clinical Neurology | 코발라민·엽산·비오틴·비타민 B1/E 반응성 대사질환의 병태생리 및 보조인자 기전 정리 |
| [30557456](https://pubmed.ncbi.nlm.nih.gov/30557456/) | 2019 | Review | Movement Disorders | 치료 가능한 선천성 대사이상에서 나타나는 운동장애, 비타민 반응성 질환 포함 |
| [958746](https://pubmed.ncbi.nlm.nih.gov/958746/) | 1976 | Review | Pediatric Clinics of North America | 비타민 대량요법에 반응하는 아미노산대사이상(Megavitamin-responsive aminoacidopathies) |
| [779426](https://pubmed.ncbi.nlm.nih.gov/779426/) | 1976 | Review | Advances in Human Genetics | 비타민 반응성 유전성 대사질환 개관 |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review | Acta Vitaminologica et Enzymologica | 대사질환에서 비타민의 병인적 역할(흡수장애/대사이상/비타민의존증후군) |
| [16343871](https://pubmed.ncbi.nlm.nih.gov/16343871/) | 2006 | Review | Archives de Pédiatrie | 신생아 뇌전증과 선천성 대사이상의 연관성, 비타민 반응성 질환 포함 |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Review | Int J Mol Sci | 비타민 B12 결핍과 신경계 손상 기전; 비오틴·엽산 대사 경로와의 보조인자 관계 언급 |
| [6396715](https://pubmed.ncbi.nlm.nih.gov/6396715/) | 1984 | Review | Progress in Food & Nutrition Science | 비오틴 등 영양소 결핍이 세포성 면역에 미치는 영향 |
| [14989256](https://pubmed.ncbi.nlm.nih.gov/14989256/) | 2004 | Review | Archives of Biochemistry and Biophysics | 엽산·B12 등 미량영양소 결핍이 DNA 손상을 유발하는 기전("대사 튠업" 개념) |
| [41692080](https://pubmed.ncbi.nlm.nih.gov/41692080/) | 2026 | Review | Clinics in Dermatology | 비오틴 포함 B군 비타민의 세포대사 및 피부과적 역할 개관 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
현재 Evidence Pack에는 TFDA(또는 국내 규제기관) 허가사항/경고·금기 정보가 완전히 결여되어 있고(DG001, Blocking 등급 — S1 안전성 초평가 진입 자체가 불가능), 작용기전(MOA) 데이터도 없습니다(DG002, High). 임상근거 또한 비오틴 대사 질환을 직접 표적으로 한 시험이 전무하고, 문헌은 기전적 연관성을 시사하는 리뷰 수준(L4)에 머물러 있어, 현 단계에서 진행 여부를 판단할 만큼 근거가 충분하지 않습니다.

**진행하려면 필요한 것:**
- 엽산의 허가 라벨(경고/금기/DDI) 확보 — 공식 소스에서 다운로드 및 파싱 (DG001 해소)
- DrugBank API 등을 통한 상세 작용기전(MOA) 데이터 확보 (DG002 해소)
- 비오틴 대사 질환 환자 대상 엽산 보충의 직접적 임상 데이터(사례보고 또는 관찰연구) 추가 확인
- TxGNN 예측 순위(8,659위)에 대한 재검토 — 동일 점수대의 상위 예측 적응증과 비교하여 특이도 평가
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

