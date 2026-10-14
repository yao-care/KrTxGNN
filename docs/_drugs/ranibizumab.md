---
layout: default
title: Ranibizumab
parent: 모델 예측만 (L5)
nav_order: 643
evidence_level: L5
indication_count: 10
---

# Ranibizumab
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 약사 평가 보고서

</div>

# Ranibizumab: 안과 질환에서 중증 비증식성 당뇨망막병증으로

## 한 문장 요약

Ranibizumab은 항 VEGF(혈관내피성장인자) Fab 단편 약물로, 한국에서 안과용 주사제로 허가되어 시판되고 있습니다.
TxGNN 모델은 **중증 비증식성 당뇨망막병증(Severe Nonproliferative Diabetic Retinopathy)**에 효과가 있을 수 있다고 예측하며, 현재 **20편의 문헌**이 이 방향을 지지합니다. 다만 이 적응증과 직접 연결된 등록 임상시험은 이번 데이터에 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 데이터에 없음 (허가증 링크만 제공됨) |
| 예측 신규 적응증 | 중증 비증식성 당뇨망막병증 (Severe Nonproliferative Diabetic Retinopathy) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L1 (Port Delivery System의 Pavilion RCT 등 RCT 문헌 확인. 단, 시험 등록 정보는 별도 확인 필요) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 6건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 없습니다. 알려진 정보에 따르면 Ranibizumab은 VEGF-A를 중화하는 항체 Fab 단편입니다. 당뇨망막병증에서는 VEGF가 망막 혈관 투과성 증가와 신생혈관 형성을 일으키며, 병변이 있는 눈의 유리체와 혈청에서 VEGF 수치가 높게 나타납니다(PMID 36580154).

VEGF를 억제하면 혈관 누출이 줄고 당뇨망막병증 중증도 점수가 개선될 수 있습니다. 문헌에서는 RIDE/RISE 시험의 사후 분석, DRCR.net Protocol I, Port Delivery System 시험 등이 이를 뒷받침합니다. 일부 국가에서는 이미 당뇨망막병증에 승인되어 있어, 완전히 새로운 재창출이라기보다 승인 또는 승인에 근접한 사용에 가깝습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다. RIDE/RISE(NCT00473382/NCT00473330)와 Port Delivery System 시험은 문헌 제목과 초록을 통해서만 확인되므로, 시험 등록 정보는 별도 검증이 필요합니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | RCT | JAMA Ophthalmol | 황반부종 없는 비증식성 당뇨망막병증에서 Ranibizumab 포트 전달 시스템과 경과 관찰 비교(Pavilion) |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | RCT 사후 분석 | Clin Ophthalmol | RIDE/RISE 시험에서 당뇨망막병증 조기 호전 예측인자 |
| [36774994](https://pubmed.ncbi.nlm.nih.gov/36774994/) | 2023 | RCT 사후 분석(메타분석) | Ophthalmol Retina | 기저 당뇨망막병증 중증도와 당뇨황반부종 해소 시간의 관계 |
| [42219053](https://pubmed.ncbi.nlm.nih.gov/42219053/) | 2026 | 체계적 문헌고찰/메타분석 | Eur J Pharmacol | Ranibizumab 포트 전달의 지속성과 질병 조절 효과 |
| [33966556](https://pubmed.ncbi.nlm.nih.gov/33966556/) | 2021 | Review | Expert Opin Biol Ther | 당뇨망막병증에서 Ranibizumab 치료 효과 개관 |
| [40347224](https://pubmed.ncbi.nlm.nih.gov/40347224/) | 2025 | 체계적 문헌고찰 | Health Technol Assess | 당뇨망막병증에서 항 VEGF와 레이저 광응고 비교 및 경제성 분석 |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2025 | 체계적 문헌고찰/메타분석 | Health Technol Assess | 항 VEGF와 레이저 광응고 비교 |
| [40969370](https://pubmed.ncbi.nlm.nih.gov/40969370/) | 2025 | 코호트 | Front Endocrinol | 중증 비증식성 당뇨망막병증에서 항 VEGF+레이저 반응 예측 노모그램 |
| [36161830](https://pubmed.ncbi.nlm.nih.gov/36161830/) | 2022 | 연장 시험 분석 | BMJ Open Ophthalmol | RIDE/RISE 연장 시험에서 투여 빈도 감소 시 DRSS 변화 |
| [30234859](https://pubmed.ncbi.nlm.nih.gov/30234859/) | 2018 | 시험 분석 | Retina | DRCR.net Protocol I 5년 추적에서 당뇨망막병증 중증도 변화 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202203870 | 루센비에스주10밀리그램/밀리리터 (종근당) | 바이알 주사제 | 허가증 링크 참조 |
| 202202008 | 아멜리부주10밀리그램/밀리리터 (삼성바이오에피스) | 바이알 주사제 | 허가증 링크 참조 |
| 201607376 | 루센티스프리필드시린지 0.5mg/0.05mL (한국노바티스) | 프리필드시린지 | 허가증 링크 참조 |
| 202301618 | 루센비에스프리필드시린지 (종근당) | 프리필드시린지 | 허가증 링크 참조 |
| 202402591 | 아멜리부프리필드시린지 0.5mg/0.05mL (삼성바이오에피스) | 프리필드시린지 | 허가증 링크 참조 |

## 안전성 고려사항

- **지식그래프상 금기 질환**: 눈 감염성 질환, 결막염 (라벨 문구가 아닌 TxGNN 지식그래프의 약물-질환 금기 연결 기준)

그 밖의 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
당뇨망막병증에서 Ranibizumab의 효과를 뒷받침하는 RCT와 사후 분석, 체계적 문헌고찰이 풍부합니다. 다만 등록 임상시험 정보가 없고 허가사항 안전성 정보를 아직 확인하지 못했으므로 조건부로 진행합니다.

**진행하려면 필요한 것:**
- 한국 허가 적응증 본문과 경고·금기 정보 확인 (식약처 허가사항 PDF 확인)
- 작용 기전 데이터 보강 (DrugBank 조회)
- RIDE/RISE, Pavilion 등 핵심 시험의 등록 정보와 시험 단계 검증
- 눈 감염 및 결막염 활동기 환자 제외 등 투여 전 안과 안전성 점검 계획

**참고: 그 밖의 예측 적응증**
- 백내장 계열(성숙, 미성숙, 노년성 등)은 항 VEGF 기전과 관련이 없고 직접적 근거가 없어 보류(Hold)를 권장합니다. 피질 백내장 문헌에는 Ranibizumab 주사 후 수정체낭 차단 증후군 증례(PMID 38476863)가 있어 안전성 신호로만 참고할 수 있습니다.
- 신생아 출혈성 질환은 비타민 K 결핍성 응고장애로 기전상 연관이 없으며, 연결된 임상시험은 용어 유사성에 의한 오매핑으로 보여 보류를 권장합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

