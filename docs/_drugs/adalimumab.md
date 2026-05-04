---
layout: default
title: Adalimumab
parent: 僅模型預測 (L5)
nav_order: 23
evidence_level: L5
indication_count: 6
---

# Adalimumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Adalimumab: 류마티스 관절염에서 류마티스 혈관염으로

## 한 문장 요약

Adalimumab은 TNF-α를 직접 중화하는 완전 인간화 단클론 항체로, 전 세계적으로 류마티스 관절염(RA), 강직성 척추염, 건선성 관절염 등 여러 자가면역 염증 질환에 승인된 생물학적 제제입니다.
TxGNN 모델은 **류마티스 혈관염(Rheumatoid Vasculitis)**에 효과가 있을 수 있다고 예측하며,
현재 **5건의 임상시험**과 **20편의 문헌**이 이 방향과 관련된 근거를 제공하고 있습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 류마티스 관절염 (글로벌 승인 기준; 국내 미등재) |
| 예측 신규 적응증 | 류마티스 혈관염 (Rheumatoid Vasculitis) |
| TxGNN 예측 점수 | 99.80% |
| 근거 수준 | L4 |
| 한국 시판 현황 | ✗ 미등재 |
| 허가증 수 | 0건 |
| 권장 결정 | Research Question |

---

## 이 예측이 타당한 이유는?

현재 공식 등재 작용 기전(MOA) 데이터는 수집되지 않았습니다. 알려진 정보에 따르면, Adalimumab은 TNF-α에 대한 완전 인간화 IgG1 단클론 항체로, TNF-α가 TNF 수용체(TNFR1·TNFR2)에 결합하는 것을 차단하여 NF-κB 염증 신호 경로를 하향 조절합니다. 이를 통해 활막 내 염증 사이토카인 연쇄 반응을 억제하고, 파골세포 매개 골 파괴를 감소시키는 효과가 다수의 Phase 3 RCT에서 확인되었습니다.

류마티스 혈관염(RV)은 류마티스 관절염(RA)에서 발생하는 가장 심각한 관절 외 합병증 중 하나로, RA 환자의 약 1% 미만에서 발생합니다. 병리 기전은 면역 복합체가 혈관벽에 침착되고 TNF-α가 과도하게 활성화되어 혈관내피세포와 혈관벽에 면역 손상을 일으키는 과정을 중심으로 합니다. 피부 궤사, 디지털 궤양, 말초 신경병증, 신장 침범 등 다양한 장기를 침범하며 상당한 이환율과 사망률을 동반합니다.

Adalimumab의 TNF-α 중화 기전은 RV의 혈관벽 염증 억제에 이론적으로 적용 가능합니다. 실제로 1건의 체계적 문헌 고찰(PMID 33058033)이 생물학적 제제의 RV 치료 가능성을 정리하고 있으며, 개별 증례에서 adalimumab이 디지털 혈관염을 호전시킨 사례(PMID 25133007)와 adalimumab 감량 후 혈관염이 악화된 사례(PMID 30773522)가 보고되어 약물의 혈관 보호 역할을 간접적으로 시사합니다. 다만, RV의 희귀성으로 인해 공식 Phase 2/3 RCT 데이터가 없어 근거 수준은 L4에 머물고 있습니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | UNKNOWN | 750,000 | 생물학적 제제 및 면역억제제로 단일 IMID(면역 매개 염증 질환) 치료 시 다른 IMID 발생 위험 평가; 혈관염은 IMID 범주에 포함되어 발병률·안전성 배경 데이터 제공 |
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | 완료 | 808 | 중국 RA 환자에서 생물학적 DMARD 사용 패턴 다기관 횡단면 연구; adalimumab 포함 생물학적 제제의 실제 처방 양상 및 인구통계 기술 |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | 완료 | 184 | 비생물학적 DMARD 또는 단일 생물학적 제제에 불충분한 반응을 보인 RA 환자에서 Tocilizumab의 임상 실제 효능·안전성 관찰 연구; adalimumab 이전 치료 실패군 포함 |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | 모집 전 | 80 | 류마티스 환자의 견관절 치환술 전 면역억제제 관리 전략 비교 (문헌 권고 기간 vs. 단축 중단); 혈관염 치료와의 직접 관련성 낮음 |
| [NCT05111743](https://clinicaltrials.gov/study/NCT05111743) | N/A | 완료 | 9,261 | 습성 노인 황반변성(AMD) 환자에서 Brolucizumab 실제 안전성 평가 후향적 코호트 연구; 본 적응증과 무관, 데이터 오분류 |

> ⚠️ 위 5건의 임상시험 중 류마티스 혈관염을 직접 평가한 시험은 없습니다. 모두 RA 또는 IMID 전반의 배경 정보를 간접적으로 제공하는 수준입니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Systematic Review | Clinical Rheumatology | PRISMA 기반 류마티스 혈관염에서 생물학적 제제 사용에 관한 체계적 문헌 고찰; TNF 억제제 포함 치료 근거 종합 — 본 예측의 가장 직접적 근거 |
| [34068884](https://pubmed.ncbi.nlm.nih.gov/34068884/) | 2021 | Review | Journal of Clinical Medicine | RA 관련 상공막염·공막염의 진단 및 관리 업데이트; TNF-α 매개 혈관 염증에서 adalimumab 포함 생물학적 제제의 역할 검토 |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Cohort/Pharmacovigilance | RMD Open | BSRBR-RA 레지스트리 기반, TNFi 치료 RA 환자에서 비생물학적 DMARD 대비 루푸스 및 혈관염 유사 사건 발생 위험 비교 |
| [37699653](https://pubmed.ncbi.nlm.nih.gov/37699653/) | 2024 | Cohort | Annals of the Rheumatic Diseases | HLA-DRB1 및 HLA-DQA1과 adalimumab 면역원성의 연관성 분석; RA 환자에서 항약물항체(ADA) 발생 예측 인자 탐색 |
| [25133007](https://pubmed.ncbi.nlm.nih.gov/25133007/) | 2014 | Case Report | Case Reports in Rheumatology | 15년 경과 RA 환자의 디지털 혈관염(괴사성 궤양)이 adalimumab 치료에 양호하게 반응한 증례; TNFi의 RV 치료 가능성 직접 시사 |
| [30773522](https://pubmed.ncbi.nlm.nih.gov/30773522/) | 2019 | Case Report | Internal Medicine (Tokyo) | 류마티스 혈관염 환자에서 adalimumab 감량 8개월 후 급성 폐고혈압 위기 발생; adalimumab의 혈관 보호 역할이 역설적으로 확인된 증례 |
| [28719435](https://pubmed.ncbi.nlm.nih.gov/28719435/) | 2018 | Case Report | American Journal of Dermatopathology | Adalimumab 시작 후 백혈구파쇄성 혈관염 및 피부 혈구탐식증 발생; TNFi 유발 역설적 혈관염(paradoxical vasculitis) 첫 보고 — 이상반응 감시 필요 |
| [36418100](https://pubmed.ncbi.nlm.nih.gov/36418100/) | 2023 | Case Report | Internal Medicine (Tokyo) | RA 치료 중 abatacept+adalimumab 병용 시 MPO-ANCA 연관 신장염 발생; tocilizumab 전환 후 개선 |
| [19482531](https://pubmed.ncbi.nlm.nih.gov/19482531/) | 2009 | Case Report | Nephrologie & Therapeutique | Adalimumab 치료 RA 환자에서 ANCA 연관 혈관염(MPO-ANCA 양성 급속 진행성 사구체신염) 발생 증례 보고 |
| [23559388](https://pubmed.ncbi.nlm.nih.gov/23559388/) | 2013 | Case Report | Clinical Rheumatology | 첫 번째 adalimumab 관련 항인지질 증후군(APS) 증례 및 TNF 억제제 관련 혈관염 문헌 고찰; 자가면역 유발 기전 논의 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Research Question**

**사유:**
류마티스 혈관염에 대한 Adalimumab의 기전적 타당성은 인정되나, 현재 근거는 체계적 문헌 고찰 및 증례 보고 수준(L4)에 머물러 있으며 직접적인 무작위 대조 시험 데이터가 없습니다. 더불어 TNFi가 역설적으로 혈관염을 유발한 사례도 문헌에 보고되어 있어, 이 약물의 단순한 재창출이 아닌 면밀한 임상 설계 하에 연구 과제로 접근해야 합니다.

**진행하려면 필요한 것:**
- Adalimumab 공식 작용 기전(MOA) 데이터 및 DrugBank 정보 확보
- 국내 허가사항 및 안전성 경고·금기 항목 (MFDS 공문서 확인)
- 류마티스 혈관염 대상 전향적 파일럿 코호트 연구 또는 국내 레지스트리 기반 후향적 분석 계획 수립
- 희귀 질환 특성상 국제 다기관 연구 협력 또는 희귀 질환 특례 연구 설계 검토
- TNFi 유발 역설적 혈관염(paradoxical vasculitis) 감시 체계 및 중단 기준 사전 정의
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

