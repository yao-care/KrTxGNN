---
layout: default
title: Bimatoprost
parent: 모델 예측만 (L5)
nav_order: 147
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Bimatoprost: 예측 신규 적응증 탈모증 (Alopecia) — 1순위 예측은 근거 없음으로 근거가 가장 풍부한 항목 선택 (근거 수준 L5). 기존 적응증: 허가증에 적응증 원문이 제공되지 않아 확인 불가 (허가사항 문서 참조 필요)"
monitor_inn: "Bimatoprost"
predicted_indications: ["malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "genetic alopecia", "pulmonary arteriovenous malformation (disease)"]
---

# Bimatoprost
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

# Bimatoprost: 녹내장·안압 조절에서 탈모증으로

## 한 문장 요약

Bimatoprost는 프로스타마이드 F2α 유사체로, 한국에서 점안액(간포트, 루미간)으로 허가되어 사용되고 있습니다.
TxGNN 모델은 **탈모증(Alopecia)**에 효과가 있을 수 있다고 예측하며, 현재 **11건의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다.
다만 Phase 3 확증 시험은 없고, 근거는 Phase 2 시험 중심입니다.

> 참고: TxGNN 점수가 가장 높은 예측은 "치아 요소를 동반한 기형 증후군"(99.997%)이지만 임상시험과 문헌이 전혀 없는 모델 예측일 뿐입니다. 그래서 실제 근거가 가장 풍부한 **탈모증(8순위)**을 중심으로 평가했습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에 적응증 원문이 제공되지 않아 확인 불가 (허가사항 문서 참조 필요) |
| 예측 신규 적응증 | 탈모증 (Alopecia) — 1순위 예측은 근거 없음으로 근거가 가장 풍부한 항목 선택 |
| TxGNN 예측 점수 | 99.99% (탈모증 기준; 1순위 예측은 99.997%) |
| 근거 수준 | L2 (탈모증 항목 기준; 완료된 Phase 2 시험 다수, Phase 3 없음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Proceed with Guardrails (연구 질문 단계) |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Bimatoprost는 프로스타마이드 F2α 유사체이며, 안압 하강 효과로 녹내장 및 고안압증 치료에 사용됩니다. 이 설명은 허가 문서가 아닌 일반적인 약리학적 지식과 문헌 초록에 근거한 것입니다.

이 약은 모낭의 프로스타마이드/FP 수용체 경로에 작용하여 성장기(anagen)를 연장하고 모낭 크기와 모발 수를 늘리는 것으로 알려져 있습니다. 녹내장 치료 중 속눈썹이 길어지는 부작용이 관찰되면서 속눈썹 저모증 적응증이 해외에서 승인되었고, 이후 두피 탈모로 연구가 확장되었습니다.

다만 이 기전은 모낭 자극에 한정됩니다. 원형탈모증 같은 자가면역성 탈모의 병인은 해결하지 못하므로 효과가 제한적일 수 있습니다. 또한 표준 치료인 minoxidil과의 상대적 효능은 이번 데이터로는 확인되지 않습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01325337](https://clinicaltrials.gov/study/NCT01325337) | Phase 2 | 완료 | 307 | 남성 안드로겐성 탈모에서 3가지 용량 vs 위약 및 minoxidil 5% |
| [NCT01325350](https://clinicaltrials.gov/study/NCT01325350) | Phase 2 | 완료 | 306 | 여성형 탈모에서 3가지 용량 vs 위약 및 minoxidil 2% |
| [NCT01904721](https://clinicaltrials.gov/study/NCT01904721) | Phase 2 | 완료 | 244 | 남성 안드로겐성 탈모에서 안전성 및 효능 평가 |
| [NCT01023841](https://clinicaltrials.gov/study/NCT01023841) | Phase 4 | 완료 | 71 | 소아 속눈썹 소실/저모증에서 bimatoprost 0.03% vs 위약 |
| [NCT02170662](https://clinicaltrials.gov/study/NCT02170662) | Phase 2 | 완료 | 33 | 안드로겐 의존성 모낭에 대한 두피 모발 성장 효과 |
| [NCT05600673](https://clinicaltrials.gov/study/NCT05600673) | Phase 1/2 | 완료 | 30 | 원형탈모증에서 CO2 분획 레이저와 bimatoprost 0.03% 병용 |
| [NCT01189279](https://clinicaltrials.gov/study/NCT01189279) | Phase 1 | 완료 | 42 | 신규 제형의 안전성, 내약성, 약동학 |
| [NCT00187577](https://clinicaltrials.gov/study/NCT00187577) | 해당 없음 | 완료 | 14 | 원형탈모증 환자의 속눈썹 성장에서 latanoprost와 bimatoprost 비교 |
| [NCT02848300](https://clinicaltrials.gov/study/NCT02848300) | Phase 1 | 완료 | 11 | 남성 안드로겐성 탈모 두피의 국소 약동학 및 내약성 |
| [NCT02676310](https://clinicaltrials.gov/study/NCT02676310) | Phase 1 | 중단 | 53 | 남성 안드로겐성 탈모에서 용량 증량 안전성·내약성·약동학 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [28264599](https://pubmed.ncbi.nlm.nih.gov/28264599/) | 2017 | Review | Expert Opin Investig Drugs | 속눈썹, 눈썹, 두피 탈모에 대한 bimatoprost 치료 고찰 |
| [38794131](https://pubmed.ncbi.nlm.nih.gov/38794131/) | 2024 | Review | Pharmaceuticals (Basel) | 안과 영역에서 모발 성장까지 bimatoprost의 활용 범위 |
| [29854658](https://pubmed.ncbi.nlm.nih.gov/29854658/) | 2018 | Review | Indian Dermatol Online J | 피부과 영역(속눈썹·눈썹 탈모, 백반증)에서의 bimatoprost |
| [35278027](https://pubmed.ncbi.nlm.nih.gov/35278027/) | 2022 | 전향적 공개 연구 | Dermatol Ther | 전신·전두 원형탈모증 환자의 속눈썹 소실에 대한 국소 bimatoprost 효과 평가 |
| [37089845](https://pubmed.ncbi.nlm.nih.gov/37089845/) | 2023 | 비무작위 공개 임상시험 | Indian Dermatol Online J | 두피 원형탈모증에서 bimatoprost vs clobetasol 비교 |
| [40252129](https://pubmed.ncbi.nlm.nih.gov/40252129/) | 2025 | 임상 연구 | Arch Dermatol Res | 원형탈모증에서 CO2 분획 레이저와 bimatoprost 병용 효과 |
| [23104985](https://pubmed.ncbi.nlm.nih.gov/23104985/) | 2013 | 전임상/임상 보고 | FASEB J | 프로스타마이드 계열 약물이 두피 탈모 치료에 새로운 접근이 될 가능성 |
| [27377163](https://pubmed.ncbi.nlm.nih.gov/27377163/) | 2016 | 증례 보고 | Pediatr Dermatol | 스테로이드 저항성 소아 두피 원형탈모증에서 국소 bimatoprost로 성공적 치료 |
| [25601618](https://pubmed.ncbi.nlm.nih.gov/25601618/) | 2015 | Review | J Am Acad Dermatol | 프로스타글란딘 F2α 유사체의 속눈썹 외 대체 임상 활용 |
| [33631058](https://pubmed.ncbi.nlm.nih.gov/33631058/) | 2021 | 체계적 문헌고찰·네트워크 메타분석 | Dermatol Ther | 원형탈모증 치료법 비교 및 순위화 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200805356 | 간포트점안액(1회용), 간포트점안액 | 점안제 (다회용/일회용) | 허가사항 문서 참조 (적응증 원문 미제공) |
| 201007673 | 루미간점안액0.01% (비마토프로스트) | 점안제 | 허가사항 문서 참조 (적응증 원문 미제공) |

두 제품 모두 한국애브비(주)의 단일 성분 제제이며 유효 상태입니다.

## 안전성 고려사항

- **약물 상호작용**: 66건이 조회되었으나 모두 위험 등급이 확인되지 않았습니다(등급 미상). 조회된 항목에는 calcitriol, metformin, omeprazole, prednisone, simvastatin, morphine 등이 포함됩니다.
- **지식 그래프 기반 금기 관련 질환** (허가 문서가 아닌 모델 지식 그래프 기준): 간 질환, 담낭 질환, 포도막염, 홍채 질환, 모양체 질환, 범포도막염, 황반부종, 낭포황반부종, 홍채염.

그 외 경고 및 금기 사항은 허가사항을 참조하세요. 허가증 상의 경고·금기 정보가 확보되지 않은 상태입니다.

## 결론 및 다음 단계

**결정: Proceed with Guardrails (연구 질문 단계)**

**사유:**
탈모증에서는 남성·여성 안드로겐성 탈모를 대상으로 한 대규모(n=244~307) 완료된 Phase 2 시험이 여러 건 있고, 속눈썹 저모증은 해외에서 승인되었습니다. 그러나 Phase 3 확증 시험이 없고 minoxidil 대비 효능도 확인되지 않아, 확정적 권고보다는 연구 질문 단계로 판단합니다.

**진행하려면 필요한 것:**
- 허가증의 적응증, 경고, 금기 원문 확보 (현재 안전성 선별을 진행할 수 없는 차단 수준의 데이터 공백)
- 상세한 작용 기전 데이터 (DrugBank 조회)
- 두피 탈모에 대한 Phase 2 결과의 구체적 효능 수치 확인 및 Phase 3 설계 검토
- 두피 적용 제형 및 투여 경로 적합성 검토 (현재 한국 허가는 점안제뿐)
- 포도막염, 황반부종 병력 환자 등 금기 가능 집단에 대한 안전성 모니터링 계획

**기타 예측에 대한 참고:**
TxGNN 상위권의 기형 증후군류(치아 기형 증후군, Dandy-Walker 기형 증후군), Ambras형 다모증, 폐동맥 정맥기형은 기전적 연관성이 없거나 근거가 전무하여 **Hold**를 권고합니다. 특히 Ambras형 다모증은 과도한 모발 성장 질환이어서 모발 성장 촉진제의 방향과 반대입니다. 두피 저모증, 선천성 저모증, 미만성 원형탈모증은 간접적 근거만 있어 후속 연구 과제로 분류됩니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

