---
layout: default
title: Susoctocog Alfa
parent: 중등도 근거 (L3-L4)
nav_order: 654
evidence_level: L3
indication_count: 10
---

# Susoctocog Alfa
{: .fs-9 }

근거 수준: **L3** | 예측 적응증: **10** 건
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

# Susoctocog Alfa: 후천성 혈우병 A에서 후천성 응고인자 결핍으로

## 한 문장 요약

Susoctocog alfa(Obizur®)는 재조합 돈유래(porcine) Factor VIII 제제로, 해외에서는 자가항체로 인한 **후천성 혈우병 A(Acquired Hemophilia A)** 치료제로 승인되어 있으나 한국에는 아직 출시되지 않았습니다.
TxGNN 모델은 **후천성 응고인자 결핍(Acquired Coagulation Factor Deficiency)**에도 효과가 있을 것으로 예측하며, 이는 기존 적응증과 기전적으로 사실상 동일한 질환 범주입니다. 현재 **문헌 9편**(코호트·실제임상 연구 다수 포함)이 이 방향을 지지합니다.

> 참고: TxGNN은 총 10개의 후보 적응증을 제시했으나, 이 중 8개(혈소판 방출장애, pseudo-von Willebrand disease, Glanzmann thrombasthenia, Scott syndrome, 콜라겐 수용체 결함, 선천성 혈소판감소증, 선천성 XIII인자 결핍, 아데노신탈아미노효소 결핍)는 FVIII 경로와 기전적 연관성이 없다고 평가되어(L5, Hold) 본 보고서에서 제외했습니다. 아래 내용은 실제 근거평가가 완료된 후보(L3, Proceed with Guardrails)를 중심으로 작성했습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 후천성 혈우병 A (해외 승인, 한국 미출시) |
| 예측 신규 적응증 | 후천성 응고인자 결핍 (Acquired Coagulation Factor Deficiency) |
| TxGNN 예측 점수 | 99.64% |
| 근거 수준 | L3 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

현재 DrugBank에 상세 작용기전(MOA) 데이터가 등록되어 있지 않습니다(Data Gap). 다만 확보된 문헌에 따르면, Susoctocog alfa는 B-도메인이 제거된 재조합 돈유래 Factor VIII 제제로, 사람 FVIII에 대한 자가항체와의 교차반응성이 낮아 후천성 혈우병 A 환자에서 FVIII 활성을 직접 보충하는 방식으로 작용합니다(PMID 27098420).

후천성 혈우병 A는 자가항체가 FVIII를 중화시켜 발생하는 "후천성 응고인자 결핍"의 대표적 아형입니다. 따라서 TxGNN이 예측한 신규 적응증은 새로운 질환이라기보다, 별도 질병 어휘 체계상 상위/유사 개념으로 기존 적응증을 재확인한 것에 가깝습니다. FVIII 대체요법 기전이 그대로 적용 가능하며, 이는 rank 4 "hemophilia" 후보의 기전 설명과도 일치합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT06461533](https://clinicaltrials.gov/study/NCT06461533) | N/A | 모집 중 | 25 | 일본 내 후천성 혈우병 A(AHA) 출혈 치료를 위한 susoctocog alfa 정맥주사 사용 실태조사(전수감시) |

※ "후천성 응고인자 결핍" 명칭으로 직접 등록된 임상시험은 없으며, 동일 질환군으로 분류되는 후천성 혈우병 A(AHA) 관련 시험을 참고로 제시합니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [27098420](https://pubmed.ncbi.nlm.nih.gov/27098420/) | 2016 | Review (Tier1) | Drugs | 후천성 혈우병 A 승인 근거가 된 다국가 2/3상 시험(n=28) 포함 종합 리뷰; 유효하고 내약성 양호 |
| [40812597](https://pubmed.ncbi.nlm.nih.gov/40812597/) | 2025 | Cohort/PK (Tier2) | J Thromb Haemost | FVIII 활성 정밀 조절을 위한 약동학 기반 용량 전략 |
| [39245591](https://pubmed.ncbi.nlm.nih.gov/39245591/) | 2024 | Review (Tier2) | La Revue de médecine interne | 후천성 혈우병 최신 진단·치료 지견 업데이트 |
| [32698943](https://pubmed.ncbi.nlm.nih.gov/32698943/) | 2020 | Cohort n=9 (Tier2) | Blood Transfusion | 이탈리아 고령 환자 9례 실사용 경험; 효과·안전성 확인 |
| [39158833](https://pubmed.ncbi.nlm.nih.gov/39158833/) | 2024 | Cohort (Tier2) | Int J Hematol | 일본인 대상 2/3상 개방표지 연구(NCT04580407), 초기 200 U/kg 용량 |
| [37584309](https://pubmed.ncbi.nlm.nih.gov/37584309/) | 2023 | Cohort, 시판후 안전성 (Tier2) | Haemophilia | 실제 임상 안전성·유효성 비개입 연구 |
| [41436689](https://pubmed.ncbi.nlm.nih.gov/41436689/) | 2025 | Case Report (Tier3) | CEN Case Reports | 혈액투석 카테터 출혈 환자에서 susoctocog alfa+emicizumab 병용 성공 |
| [34011555](https://pubmed.ncbi.nlm.nih.gov/34011555/) | 2023 | Case Report (Tier3) | Eur J Hosp Pharm | COVID-19 병발 환자에서 고위험 출혈 치료 사례 |
| [35501873](https://pubmed.ncbi.nlm.nih.gov/35501873/) | 2022 | Case Report (Tier3) | J Med Case Rep | 루푸스 항응고인자 동반 후천성 혈우병 A 사례 |

---

## 한국 시판 정보

한국에는 현재 허가된 제품이 없습니다 (미출시, 허가증 0건).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (경고, 금기, 약물상호작용 데이터 미확보 — TFDA/MFDS 수준 라벨 정보 확보가 Blocking 과제로 남아 있음)

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
"후천성 응고인자 결핍"은 기존 해외 승인 적응증인 후천성 혈우병 A와 기전적으로 동일한 질환 범주이며, 여러 코호트·실제임상 연구(문헌 9편, Tier 1-2 다수)가 이를 뒷받침합니다. 다만 한국에는 허가·시판 이력이 없고, 안전성 라벨(경고/금기/DDI) 정보가 확보되지 않아 신중한 접근이 필요합니다.

**진행하려면 필요한 것:**
- 한국 식약처 허가 가능성 검토 및 안전성 라벨(경고·금기·DDI) 확보 — 현재 Blocking Data Gap (DG001)
- 상세 작용기전(MOA) 데이터 보강 — DrugBank API 조회 필요 (DG002)
- "후천성 응고인자 결핍" 단독 명칭의 전향적 임상 데이터 확보 (현재는 AHA 명칭 하 연구에 의존)
- 희귀질환 의약품 특성상 콜드체인·투약 프로토콜 확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

