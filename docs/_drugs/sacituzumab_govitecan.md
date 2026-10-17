---
layout: default
title: Sacituzumab Govitecan
parent: 모델 예측만 (L5)
nav_order: 678
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Sacituzumab Govitecan: 예측 신규 적응증 약인성 골다공증 (drug-induced osteoporosis) (근거 수준 L5). 기존 적응증: 허가 적응증 본문이 데이터에 텍스트로 포함되어 있지 않고 식약처 허가 문서 링크만 제공됨 (허가사항 참조)"
monitor_inn: "Sacituzumab govitecan"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "diabetic cataract", "cortical cataract", "nuclear senile cataract", "senile cataract", "diabetes mellitus type 2 associated cataract", "craniostenosis cataract", "mature cataract"]
---

# Sacituzumab Govitecan
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

# Sacituzumab govitecan: 허가 적응증에서 약인성 골다공증으로

## 한 문장 요약

Sacituzumab govitecan(국내 제품명 트로델비주)은 Trop-2를 표적으로 하는 항체-약물 접합체(ADC)로, 한국에서 허가를 받아 시판 중입니다.
TxGNN 모델은 **약인성 골다공증(drug-induced osteoporosis)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 **임상시험은 0건**, **문헌은 0편**입니다.
따라서 이 예측은 모델 계산에만 근거한 가설 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 데이터에 텍스트로 포함되어 있지 않고 식약처 허가 문서 링크만 제공됨 (허가사항 참조) |
| 예측 신규 적응증 | 약인성 골다공증 (drug-induced osteoporosis) |
| TxGNN 예측 점수 | 99.78% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, Sacituzumab govitecan은 Trop-2 표적 항체에 토포이소머라제 I 억제제인 SN-38을 연결한 ADC이며, 세포독성 약물을 종양 세포에 전달하는 방식으로 작동합니다.

이 기전과 뼈 대사 사이에서 뚜렷한 연결고리는 확인되지 않습니다. 오히려 세포독성 항암화학요법은 골 소실과 관련되는 경우가 더 흔하며, 골다공증을 치료한다는 근거는 없습니다. TxGNN 점수(99.78%)는 지식 그래프 기반 예측일 뿐이며, 이를 뒷받침하는 임상 또는 문헌 근거가 없습니다.

참고로 예측 순위 상위 10개 중에는 당뇨망막병증(중증 비증식성 포함)과 여러 유형의 백내장이 다수 포함되어 있습니다. 백내장 하위 유형들은 점수가 동일하거나 거의 같아, 독립적인 근거가 아니라 그래프 내 유사 질환 군집의 영향일 가능성이 큽니다. 세포독성 ADC가 이런 만성 비종양성 안과 질환에 적합하다고 볼 근거도 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202301485 | 트로델비주(사시투주맙고비테칸) | 주사제 (동결건조 분말 바이알, 재구성 시 무색~황녹색 용액) | 허가사항 문서 참조 (식약처 허가 문서 링크로만 제공됨) |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 항체-약물 접합체 (토포이소머라제 I 억제제 SN-38 탑재) |
| 골수억제 위험 | 높음 (호중구감소증 등 골수억제 위험이 알려져 있음) |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | CBC(분류 포함) 등 혈액학적 검사, 간·신기능 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

## 안전성 고려사항

- **약물 상호작용**: 이번 보고서에 수집된 데이터에서 총 40건의 상호작용이 확인되었으며, 그중 일부를 아래에 정리합니다.
  - **주요(Major) 등급**: Deferiprone, Fostamatinib, Adalimumab, Apalutamide, Certolizumab pegol, Cladribine, Dacomitinib, Irinotecan, Leflunomide, Natalizumab, Nilotinib, Ozanimod
  - **중등도(Moderate) 등급**: Alefacept, Alemtuzumab, Anakinra, Canakinumab, Dimethyl fumarate, Lorlatinib, Ocrelizumab, Omacetaxine mepesuccinate
  - 이들 중 다수는 면역억제 또는 골수억제 약물이며, 병용 시 감염 및 혈구감소 위험이 커질 수 있습니다. 특히 같은 토포이소머라제 I 억제제 계열인 Irinotecan과의 병용은 주의가 필요합니다.

주요 경고와 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측된 신규 적응증(약인성 골다공증)에 대한 임상시험과 문헌이 전혀 없고, 근거 수준은 L5(모델 예측만 존재)입니다. 기전적 연결고리도 불분명하며 세포독성 ADC의 독성 프로파일이 비종양성 만성 질환에는 부적합해 보입니다.

**진행하려면 필요한 것:**
- 허가사항(경고, 금기, 적응증) 전문 확보: 식약처 허가 문서를 내려받아 분석
- 상세한 작용 기전(MOA) 데이터 확보: DrugBank 조회
- 골 대사와의 기전적 연관성을 뒷받침하는 전임상 근거
- 비종양성 질환에서의 이익-위험 평가 (골수억제, 호중구감소증 등 독성 대비)
- 투여 경로 적합성 검토 (현재 정맥 투여 주사제만 확인됨)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

