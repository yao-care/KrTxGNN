---
layout: default
title: Cyclophosphamide
parent: 높은 근거 (L1-L2)
nav_order: 226
evidence_level: L1
indication_count: 5
---

# Cyclophosphamide
{: .fs-9 }

근거 수준: **L1** | 예측 적응증: **5** 건
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

# Cyclophosphamide：조혈모세포이식 전처리（대만 미승인）→ 골수성 백혈병 (Myeloid Leukemia)

## 한 문단 요약

Cyclophosphamide는 DNA 알킬화제로서 전 세계적으로 혈액종양 화학요법 및 조혈모세포이식(HSCT) 전처리에 광범위하게 사용되고 있으나, 현재 대만에는 상시 허가가 없습니다. TxGNN 모델은 이 약물이 **골수성 백혈병(Myeloid Leukemia)**에 대한 치료 잠재력을 갖고 있음을 예측하며, 예측 점수는 **99.47%**에 달합니다. 현재 이 예측 방향을 지지하는 **10개 이상의 임상시험**(여러 완료된 Phase 2/3 시험 포함) 및 **20개의 문헌**(체계적 네트워크 메타분석 포함)이 있습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 없음(대만 미승인; 전 세계: 림프종, 유방암, 자가면역질환, HSCT 전처리) |
| 예측 신규 적응증 | 골수성 백혈병(Myeloid Leukemia) |
| TxGNN 예측 점수 | 99.47% |
| 근거 등급 | L1 |
| 대만 상시 현황 | ✗ 미승인 |
| 허가 건수 | 0건 |
| 권장 의사결정 | Proceed with Guardrails |

---

## 이 예측이 합리적인 이유는?

Cyclophosphamide는 전약물(prodrug)로서 간의 CYP450 효소계에 의해 활성화된 후, 그 활성 대사물인 phosphoramide mustard가 DNA 쌍나선과 공유 가교결합(cross-linking)을 형성하여 DNA 복제 및 전사를 방해하며, 빠르게 증식하는 악성세포에 강력한 살상작용을 발휘합니다. 현재 대만에는 상시 허가가 없지만, Cyclophosphamide는 전 세계 급성 골수성 백혈병(AML) 치료에서 불가결한 역할을 하고 있습니다.

AML 치료 체계에서 Cyclophosphamide는 두 가지 핵심 기능을 수행합니다. 첫째, **골수제거성 전처리 방안(Myeloablative Conditioning, MAC)**의 핵심 성분으로서 — BuCy(Busulfan + Cyclophosphamide)는 동종 조혈모세포이식 전의 표준 전처리 방안이며, 환자 자신의 조혈계를 완전히 제거하여 공여자 모세포의 효과적인 이식을 보장합니다. 둘째, **이식후 환인산 화학요법(Post-Transplant Cyclophosphamide, PTCy)**로서 그 동종 반응성 T세포의 선택적 소진이라는 독특한 면역 메커니즘을 활용하여 현재 가장 주목받는 GVHD 예방 전략이 되었으며, 이 메커니즘은 다수의 대규모 무작위대조시험에서 충분히 검증되었습니다.

골수성 백혈병의 병리생리적 특징 — DNA 수선 경로의 고도 활성화 및 빠르게 분열하는 원시세포군 — 은 Cyclophosphamide의 DNA 알킬화 메커니즘과 높은 계약도를 갖습니다. 여러 완료된 Phase 2/3 시험(최대 431명의 무작위 Phase 3 시험 NCT03959241) 및 2023년 체계적 네트워크 메타분석(PMID 36357773)은 이 적응증에서 Cyclophosphamide의 유효성을 확인하여, TxGNN 예측이 충분하고 높은 등급의 임상 지지를 갖도록 합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 피험자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02744742](https://clinicaltrials.gov/study/NCT02744742) | Phase 2/3 | 완료 | 202 | 전향적 무작위대조시험으로 G-CSF+Decitabine+BuCy와 표준 BuCy 전처리 방안을 AML/MDS 속발 AML 동종모세포이식의 안전성 및 유효성으로 비교하며, 본 보고서의 최고 등급 직접 근거입니다. |
| [NCT03959241](https://clinicaltrials.gov/study/NCT03959241) | Phase 3 | 완료 | 431 | 다기관 무작위 Phase 3 시험(BMT CTN 1703)으로 Tac/MTX와 PTCy/Tac/MMF를 RIC allo-PBSCT의 GVHD 예방 전략으로 비교하며, Cyclophosphamide가 주요 평가 약물입니다. |
| [NCT00309842](https://clinicaltrials.gov/study/NCT00309842) | Phase 2 | 완료 | 213 | Cyclophosphamide/Fludarabine/TBI 골수제거성 전처리를 혈액악성종양 치료의 비혈연 제대혈 이식에 사용하여 213명의 대규모 안전성 데이터를 제공합니다. |
| [NCT00134017](https://clinicaltrials.gov/study/NCT00134017) | Phase 2 | 완료 | 142 | HLA 상합 혈연 및 혈연 골수이식에서 BuCy 전처리에 추가된 이식후 고용량 Cyclophosphamide를 GVHD 예방으로 사용하는 유효성을 평가합니다. |
| [NCT07249346](https://clinicaltrials.gov/study/NCT07249346) | Phase 2 | 모집 중 | 124 | 다기관 시험으로 저용량 이식후 Cyclophosphamide(25 mg/kg, +3일 & +4일)/ Tacrolimus/Ruxolitinib을 MAC allo-PBSCT의 GVHD 예방에서 직접 평가합니다. |
| [NCT00241358](https://clinicaltrials.gov/study/NCT00241358) | Phase 1/2 | 완료 | 92 | Cyclophosphamide가 포함된 전처리의 AMD3100 동원 모세포이식 방안을 혈액악성종양에서 안전성 및 유효성으로 평가합니다. |
| [NCT00809276](https://clinicaltrials.gov/study/NCT00809276) | Phase 1/2 | 완료 | 92 | Fludarabine/IV Busulfan 전처리 후 이식후 고용량 Cyclophosphamide 면역억제를 연구하여 골수이식후 GVHD 예방 효익을 평가합니다. |
| [NCT00723099](https://clinicaltrials.gov/study/NCT00723099) | Phase 2 | 완료 | 73 | Cyclophosphamide가 포함된 감량강도 전처리 비혈연 제대혈 이식으로 AML 동종이식 맥락에서 Cy의 응용을 지지합니다. |
| [NCT06532084](https://clinicaltrials.gov/study/NCT06532084) | Phase 2 | 모집 중 | 88 | 단기관 무작위시험으로 PTCy가 포함된 allo-HSCT 후 Sorafenib 유지 치료를 고위험 골수악성종양의 유효성으로 비교하여 현대 AML 이식 실행 데이터를 제공합니다. |
| [NCT00691015](https://clinicaltrials.gov/study/NCT00691015) | Phase 2 | 완료 | 48 | Sirolimus/Tacrolimus/Thymoglobulin을 비혈연 공여자 HCT의 GVHD 예방 방안(Cyclophosphamide 전처리 포함)으로 평가하여 비교 배경 데이터를 제공합니다. |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [36357773](https://pubmed.ncbi.nlm.nih.gov/36357773/) | 2023 | 체계적 검토 및 네트워크 메타분석 | Bone Marrow Transplantation | AML allo-HSCT 완전 관해 환자의 다양한 MAC 방안(BuCy 포함)의 유효성을 베이지안 네트워크 메타분석으로 비교하여 현재 최고 등급의 통합 근거를 제공합니다. |
| [40905088](https://pubmed.ncbi.nlm.nih.gov/40905088/) | 2026 | 전향적 등록연구 | Haematologica | MAC+PTCy GVHD 예방 이식을 받은 217명의 AML 환자의 유전학적 위험 분류 및 예후를 분석하며, 전체 2년 OS는 77%(95% CI: 71–83)에 달합니다. |
| [40434956](https://pubmed.ncbi.nlm.nih.gov/40434956/) | 2025 | 회고적 비교연구 | Future Oncology | AML allo-HSCT에서 표준 BuCy와 FluBu 골수제거성 전처리 방안을 직접 비교하여 유효성 동등성 및 독성 차이를 평가합니다. |
| [39939431](https://pubmed.ncbi.nlm.nih.gov/39939431/) | 2025 | 회고적 연구 | Bone Marrow Transplantation | 중고위험 AML(CR1)을 받는 1,823명 환자의 PTCy allo-HSCT에서 전처리 강도(MAC vs RIC)와 이식 후 관계를 분석합니다. |
| [40437709](https://pubmed.ncbi.nlm.nih.gov/40437709/) | 2025 | 회고적 연구 | European Journal of Haematology | 65세 이하 AML 환자가 ATG+PTCy+Cyclosporine GVHD 예방 방안을 받는 데 있어 RIC과 MAC이 생존에 미치는 영향을 평가합니다. |
| [38499049](https://pubmed.ncbi.nlm.nih.gov/38499049/) | 2024 | Phase 2 연구 보고서 | Transplant Immunology | 난치성 재발 AML allo-HSCT에서 Cladribine+BuCy 강화 전처리 방안의 유효성 및 안전성을 탐색하여 BuCy 기초 방안 강화 데이터를 제공합니다. |
| [38466265](https://pubmed.ncbi.nlm.nih.gov/38466265/) | 2024 | 회고적 연구 | Cytotherapy | 반상합 HCT(haplo-HCT with PTCy)로 AML을 치료하는 예후 인자를 분석하여 PTCy가 GVHD를 효과적으로 억제하면서 이식 항백혈병 효과를 유지함을 확인합니다. |
| [35955881](https://pubmed.ncbi.nlm.nih.gov/35955881/) | 2022 | 회고적 연구 | Int J Molecular Sciences | 소아 AML 상합 공여자 HSCT에서 PTCy를 GVHD 예방 전략으로 사용하는 첫 전문 연구로, 소아 안전성 및 유효성 데이터를 보충합니다. |
| [31628924](https://pubmed.ncbi.nlm.nih.gov/31628924/) | 2020 | 회고적 연구 | Hematology/Oncology and SCT | AML/MDS allo-HCT 골수제거성 전처리에서 BuCy와 BuFlu를 비교하여 생활 품질 영향에 초점을 맞춥니다. |
| [33325761](https://pubmed.ncbi.nlm.nih.gov/33325761/) | 2021 | 회고적 연구 | Leukemia & Lymphoma | AML 고백혈구혈증(≥50×10⁹/L) 또는 백혈구 침전증에서 고용량 Cyclophosphamide(60 mg/kg)의 세포감량 유효성(27례)을 보고하여 응급 상황에서의 응용 가치를 초기 확인합니다. |

---

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물(알킬화제, Alkylating Agent; 전약물, 간 CYP2B6/CYP3A4에 의해 활성화 필요) |
| 골수억제 위험 | **높음**(MAC 용량에서 골수제거는 예상 치료 효과; PTCy 용량에서도 여전히 중대하여 전혈구계산 밀접 모니터링 필요) |
| 구토 등급 | 중~고(정맥주사, 고용량 >750 mg/m²); 저~중(경구 또는 저용량 정맥주사) |
| 모니터링 항목 | 전혈구계산(백혈구 분류 포함), 간신기능(ALT/AST/Cr), 전해질, 소변 분석(혈뇨 포함, 출혈성 방광염 모니터링), 혈중요소질소 |
| 특수 처치 | 세포독성 약물 조작 및 폐기 규범 준수; 고용량 정맥주사 시 MESNA로 출혈성 방광염 예방; 충분한 수분화(≥3 L/day); G-CSF 및 수혈 지지 준비; 감염 징후 밀접 모니터링 |

---

## 안전성 고려사항

안전성 정보는 허가 설명서를 참조하시기 바랍니다.

---

## 결론 및 다음 단계

**의사결정: Proceed with Guardrails(조건부 추진)**

**근거:**
Cyclophosphamide를 골수성 백혈병(AML)에 사용하기 위한 임상 근거 등급은 높으며, 431명의 무작위 Phase 3 시험(NCT03959241, 완료), 202명의 Phase 2/3 시험(NCT02744742, 완료), 및 2023년 베이지안 체계적 네트워크 메타분석(PMID 36357773)을 포함하여 전체 근거 등급은 **L1**에 달합니다. 약물의 이중 응용 메커니즘(BuCy 골수제거성 전처리 및 PTCy GVHD 예방)은 메커니즘에서 명확하며 전 세계 다수의 골수이식 센터에서 광범위하게 검증되어 충분한 추진 조건을 갖춥니다.

**추진이 필요한 경우 필요한 사항:**
- TFDA 약품 설명서 경고 및 금기사항 완전 데이터 획득(현재 **Blocking Data Gap DG001**, S1 안전성 초평 차단)
- 완전한 작용 메커니즘(MOA) 데이터 보충(현재 **High 우선 Data Gap DG002**, mechanistic-link 분석 제한)
- 대만 AML 임상 치료 현황 및 기존 대체 방안(FluBu 등)의 비교 분석 평가
- 특정 고위험 족군(노령 환자, 신기능 부전, 기존 심장질환)의 안전성 모니터링 계획 수립
- 대만 상시 허가 신청을 고려하는 경우 완전한 TFDA 규제 전략 수립, 가교 시험 데이터 평가 및 약품 기술 문서 준비 포함

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

