---
layout: default
title: Gadoteridol
parent: 모델 예측만 (L5)
nav_order: 369
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Gadoteridol: 예측 신규 적응증 골관절염 감수성 (osteoarthritis susceptibility) (근거 수준 L5). 기존 적응증: MRI 조영제(진단 목적). 허가 적응증 원문은 이 보고서에 사용한 데이터에서 텍스트로 확인되지 않음"
monitor_inn: "Gadoteridol"
predicted_indications: ["osteoarthritis susceptibility", "osteoarthritis", "rheumatoid arthritis", "brachyolmia", "hemoglobinopathy", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "congestive heart failure", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "myosclerosis"]
---

# Gadoteridol
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

# Gadoteridol: MRI 조영에서 골관절염으로

## 한 문장 요약

Gadoteridol은 가돌리늄 기반 MRI 조영제로, 원래 진단 영상 검사에 사용되는 약물입니다.
TxGNN 모델은 **골관절염 감수성(osteoarthritis susceptibility)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 **임상시험은 0건**, **문헌은 0편**입니다. 다만 같은 계열의 예측인 골관절염(osteoarthritis)과 류마티스 관절염에서는 영상 진단 연구 문헌이 있으나, 치료 효과를 시사하는 근거는 아닙니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | MRI 조영제(진단 목적). 허가 적응증 원문은 이 보고서에 사용한 데이터에서 텍스트로 확인되지 않음 |
| 예측 신규 적응증 | 골관절염 감수성 (osteoarthritis susceptibility) |
| TxGNN 예측 점수 | 98.90% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Gadoteridol은 비이온성 가돌리늄 킬레이트 조영제이며, 질병 자체를 조절하는 약리 활성은 확인되지 않았습니다.

골관절염 감수성은 유전적 소인과 관련된 개념으로, 조영제가 이를 변화시킬 수 있다는 기전적 연결 고리는 발견되지 않았습니다. 높은 예측 점수는 지식 그래프 구조에서 비롯된 인공적 결과일 가능성이 큽니다.

참고로 순위 2위인 골관절염(점수 98.76%)과 3위인 류마티스 관절염(점수 98.66%)에서는 문헌이 있으나, 모두 Gadoteridol을 **영상 진단 도구**로 사용한 연구입니다. 즉 치료 재창출이 아니라 기존 진단 용도의 연장입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

1순위 예측(골관절염 감수성)에 대한 관련 문헌은 없습니다. 참고로 2순위(골관절염)와 3순위(류마티스 관절염) 예측에서 확인된 문헌 중 주요 항목은 다음과 같습니다. 모두 진단 영상 연구이며 치료 효과 근거가 아닙니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [37593815](https://pubmed.ncbi.nlm.nih.gov/37593815/) | 2024 | 생체 외 영상 연구 | J Orthop Res | 삼중 조영 CT(Gadoteridol 포함)로 무릎 연골 분절 및 생체역학 특성 평가 |
| [39622931](https://pubmed.ncbi.nlm.nih.gov/39622931/) | 2024 | 개념 증명 영상 연구 | Sci Rep | 광자계수 CT와 이중 조영으로 소 연골 내 조영제 확산 및 생체역학 상관성 평가 |
| [33692379](https://pubmed.ncbi.nlm.nih.gov/33692379/) | 2021 | 생체 외 영상 연구 | Sci Rep | 이중 조영 광자계수 CT로 관절 연골 건강 평가 |
| [32767676](https://pubmed.ncbi.nlm.nih.gov/32767676/) | 2021 | 생체 외 확산 연구 | J Orthop Res | 연골 구성 성분이 양이온성·비이온성 조영제 확산에 미치는 영향 |
| [32525582](https://pubmed.ncbi.nlm.nih.gov/32525582/) | 2020 | 생체 외 영상 연구 | J Orthop Res | 이중 조영 CT가 단일 조영보다 연골을 더 일찍 특성화 |
| [8689824](https://pubmed.ncbi.nlm.nih.gov/8689824/) | 1996 | 임상 영상 용량 연구 | Clin Radiol | 류마티스 관절염 환자 19명에서 0.1 vs 0.3 mmol/kg 용량 비교, 고용량이 활막 조영 증강에 유리 |
| [9010087](https://pubmed.ncbi.nlm.nih.gov/9010087/) | 1996 | 임상 영상 용량 연구 | Br J Rheumatol | 류마티스 활막 조영에서 용량 간 유의한 차이 확인 |
| [8867431](https://pubmed.ncbi.nlm.nih.gov/8867431/) | 1996 | 임상 진단 영상 연구 | Der Radiologe | 류마티스성 관절 변화의 MR 진단에서 Gadoteridol과 Gd-DTPA 비교 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201103760 | 프로핸스주(가도테리돌) | 바이알 주사액(무색~미황색 투명한 액) | 허가사항 참조 |
| 201103761 | 프로핸스주프리필드시린지(가도테리돌) | 프리필드시린지 주사액(무색~미황색 투명한 액) | 허가사항 참조 |

## 안전성 고려사항

- **약물 상호작용**: 총 19건이 확인되었으며, 모두 중등도(Moderate)입니다. 상호작용 약물은 모두 베타차단제입니다. 주요 항목은 다음과 같습니다.
  - 전신 투여제: Acebutolol, Atenolol, Betaxolol, Bisoprolol, Carvedilol, Nebivolol, Nadolol, Labetalol, Metoprolol, Pindolol, Propranolol, Sotalol, Timolol, Esmolol
  - 안과용제: Betaxolol, Timolol, Carteolol, Levobunolol, Metipranolol

경고 및 금기 등 그 밖의 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 높지만(98.90%) 1순위 예측에 대한 임상시험과 문헌이 전혀 없고 기전적 연결 고리도 확인되지 않아 모델 예측만 존재하는 L5 수준입니다. 골관절염과 류마티스 관절염 관련 문헌은 모두 진단 영상 용도로, 치료 재창출 근거가 되지 못합니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기) 확보: 식약처 허가 문서 확인 필요
- 작용 기전(MOA) 데이터 확보: DrugBank 조회
- 조영제가 골관절염 질환 경과에 영향을 준다는 전임상 또는 임상 근거
- 치료 목적이 아닌 진단 보조 용도(연골 평가 등)로 가치를 평가할지 방향 재설정
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

