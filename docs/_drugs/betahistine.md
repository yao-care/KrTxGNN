---
layout: default
title: Betahistine
parent: 僅模型預測 (L5)
nav_order: 136
evidence_level: L5
indication_count: 10
---

# Betahistine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Betahistine: 전정성 현기증 (해외 허가)에서 周邊性眩暈으로

## 한 문장 요약

Betahistine은 히스타민 유사체로, 유럽·일본 등에서 메니에르병 및 전정성 현기증 치료의 1차 약물로 허가되어 있으나 **한국에는 현재 미허가·미판매** 상태입니다.
TxGNN 모델은 총 10개 적응증을 예측했으며, 가장 강력한 임상 근거를 보유한 **周邊性眩暈(Peripheral Vertigo)**(근거 수준 L1)을 핵심 재창출 후보로 제시합니다.
현재 **2건의 직접 Betahistine 임상시험**(총 433명 등록)과 **Cochrane 체계적 문헌고찰 2건·메타분석 2건을 포함한 10편의 고품질 문헌**이 이를 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 전정성 현기증·메니에르병 (해외 허가, 한국 미허가) |
| 핵심 예측 적응증 | 周邊性眩暈 (Peripheral Vertigo) |
| TxGNN 예측 점수 | 98.07%¹ |
| 근거 수준 | **L1** (Phase 2 완료 RCT + Cochrane 메타분석 2건 이상) |
| 한국 시판 현황 | ✗ 미판매 |
| 한국 허가증 수 | 0건 |
| 권장 결정 | **Proceed with Guardrails** |

> ¹ TxGNN 최고 점수 적응증은 하지불안증후군(98.51%, 순위 1위)이나 임상 근거 전무(L5, Hold)로 본 보고서는 근거 최우수 적응증인 周邊性眩暈(순위 6위)을 핵심 분석 대상으로 선정합니다.

### 전체 예측 적응증 요약

| 순위 | 적응증 | TxGNN 점수 | 근거 수준 | 임상시험 | 문헌 | 권장 결정 |
|------|--------|-----------|---------|:-------:|:----:|---------|
| 1 | 하지불안증후군 | 98.51% | L5 | 0 | 0 | Hold |
| 2 | 활성 달팽이관-전정 메니에르병 | 98.34% | L4 | 0 | 0 | Research Question |
| 3 | 활성 전정성 메니에르병 | 98.34% | L2 | 0 | 19 | Proceed with Guardrails |
| 4 | 활성 달팽이관성 메니에르병 | 98.34% | L4 | 0 | 2 | Research Question |
| 5 | 이경화증 | 98.19% | L5 | 0 | 0 | Hold |
| **6** | **周邊性眩暈 ★** | **98.07%** | **L1** | **4** | **20** | **Proceed with Guardrails** |
| 7 | 노인성 난청 | 97.93% | L5 | 0 | 0 | Hold |
| 8 | 양성 발작성 체위성 현기증 (BPPV) | 97.78% | L2 | 4 | 20 | Research Question |
| 9 | Kir6.2 결핍 상염색체 열성 고인슐린혈증 | 97.77% | L5 | 0 | 0 | Hold |
| 10 | 가족성 고인슐린혈증성 저혈당 | 97.32% | L5 | 0 | 0 | Hold |

★ 본 보고서 핵심 분석 대상

---

## 이 예측이 타당한 이유는?

이번 DrugBank 쿼리에서 Betahistine의 공식 MOA 데이터는 수집되지 않았습니다. 그러나 기존 임상 문헌(PMID 11700150, PMID 24177346)을 통해 두 가지 핵심 기전이 확립되어 있습니다.

**① H3 수용체 역효현제(inverse agonist) 작용**: 전정핵(vestibular nuclei) 시냅스 전 히스타민 방출을 탈억제하여 전정 대償(vestibular compensation)을 가속하고, 현기증 발작의 빈도와 강도를 감소시킵니다. 이 경로는 「H3 억제 → 히스타민 방출 증가 → 전정핵 흥분-억제 균형 회복」으로 요약됩니다.

**② H1 수용체 약한 효현제(weak agonist) 작용**: 달팽이관 및 전정 미세혈관(특히 혈관조 모세혈관)을 확장하여 내림프액 과압을 완화합니다. PMID 26139562는 H3 이형 수용체(heteroreceptor)가 Betahistine 유도 달팽이관 혈류 증가의 매개체임을 직접 증명했으며, PMID 28818391은 전모세혈관 주위세포(pericyte) 조절이 혈관 기전의 핵심임을 추가로 규명했습니다.

주변성 현기증은 달팽이관·반고리관·전정신경의 말초 병변에 기인하며, 위 두 기전은 이 병태생리와 직접적으로 연결됩니다. 2014년 Nauta 메타분석(PMID 23778722)은 12건의 이중맹검 RCT에서 betahistine이 위약 대비 유리한 치료 결과의 교차비를 유의하게 높임을 입증했고, 2018년 유럽 이비인후과학회 가이드라인(PMID 30256205)은 betahistine을 메니에르병 표준 1차 약물로 권고하고 있습니다. 한국 미허가 현황은 효능·안전성 문제가 아닌 허가 신청 미제출에 기인하는 것으로 추정되며, 이는 도입 기회 요인으로 해석됩니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|:--------:|---------|
| [NCT03908567](https://clinicaltrials.gov/study/NCT03908567) | Phase 2 | 완료 | 124 | AM-125(비강분무형 Betahistine) vs 위약 — 청신경 종양 수술 후 급성 주변성 현기증 치료 효능·안전성 평가(Proof-of-concept RCT). 本 적응증 최직접 전향적 RCT 근거. |
| [NCT01759251](https://clinicaltrials.gov/study/NCT01759251) | 관찰연구 | 완료 | 309 | Betaserc®(betahistine dihydrochloride) 상시판 후 관찰연구 — 전정성 현기증 치료 효과 및 투여 중단 후 경과 추적(러시아·우크라이나 실사용 데이터). |
| [NCT07075289](https://clinicaltrials.gov/study/NCT07075289) | Phase 4 | 완료 | 44 | Oral Lumbrokinase vs Betahistine mesylate(BPPV 무작위 비교) — 염증지표(IL-1β), 삶의 질, 증상 해소 평가. Betahistine 비교 대조약으로 사용된 직접 Phase 4 RCT. |
| [NCT05127694](https://clinicaltrials.gov/study/NCT05127694) | 해당없음 | 완료 | 30 | 급성 BPPV에서 약물치료(betahistine 포함 가능) vs 전정 재활치료 비교 — Betahistine이 표준 약물 치료군의 구성 요소로 간접 포함. |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|:---:|------|------|---------|
| [26797774](https://pubmed.ncbi.nlm.nih.gov/26797774/) | 2016 | Phase 3 RCT (BEMED Trial) | BMJ | 메니에르병 3군(고용량·저용량 betahistine·위약) 장기 비교 — 현기증 발작 빈도에서 군 간 통계적 유의 차이 없음; 적정 용량 불확실성 및 위약 효과 시사 |
| [36827524](https://pubmed.ncbi.nlm.nih.gov/36827524/) | 2023 | Cochrane 체계적 문헌고찰 | Cochrane Database | 메니에르병 전신 약물 치료(betahistine, 이뇨제, 항바이러스제, 스테로이드) 종합 검토 — 근거 불확실성 지적, betahistine 관련 데이터 포함 |
| [23778722](https://pubmed.ncbi.nlm.nih.gov/23778722/) | 2014 | 메타분석 (12 RCT) | Eur Arch Oto-Rhino-Laryngol | 12건 이중맹검 위약대조 RCT 메타분석 — betahistine의 전정성 현기증/메니에르병 치료 반응 교차비(OR) 유의하게 증가 확인 |
| [27327415](https://pubmed.ncbi.nlm.nih.gov/27327415/) | 2016 | Cochrane 체계적 문헌고찰 | Cochrane Database | 다양한 원인의 현기증에서 betahistine 대 위약 효과 비교 — 일부 긍정 결과 확인, 방법론적 이질성 지적 |
| [40070497](https://pubmed.ncbi.nlm.nih.gov/40070497/) | 2025 | 체계적 문헌고찰·메타분석 | World J Otorhinolaryngol | Epley 도수법 + betahistine vs Epley 단독 BPPV 치료 효과 메타분석 — betahistine 부가요법의 잔류 현기증 감소 효용 평가 |
| [30256205](https://pubmed.ncbi.nlm.nih.gov/30256205/) | 2018 | 유럽 임상 가이드라인 | J Int Adv Otol | 유럽 이비인후과학회 메니에르병 진단·치료 Position Statement — betahistine을 1차 표준 약물로 권고 |
| [26245698](https://pubmed.ncbi.nlm.nih.gov/26245698/) | 2015 | 임상 리뷰 | Acta Otolaryngol | 임상시험 및 메타분석 검토 — betahistine은 메니에르병, BPPV, 전정신경염 등 말초성 현기증에서 효과적이고 안전 |
| [32978116](https://pubmed.ncbi.nlm.nih.gov/32978116/) | 2022 | RCT | Braz J Otorhinolaryngol | 후반고리관 BPPV에서 betahistine 부가요법 무작위 대조시험 — 이석 치환술 후 betahistine 병용 효과 평가 |
| [16116833](https://pubmed.ncbi.nlm.nih.gov/16116833/) | 2005 | RCT | Acta Otorhinolaryngol Ital | 이석 해방술 ± betahistine 전향적 비교 연구(n=103) — 복위술·점진적 이석분산술과 betahistine 병용 효과 비교 |
| [6363584](https://pubmed.ncbi.nlm.nih.gov/6363584/) | 1984 | 이중맹검 위약대조 RCT | J Laryngol Otol | Betahistine dihydrochloride 12 mg TID 교차 연구(n=24, 6주×2구간) — 말초 전정 현기증에서 위약 대비 유의한 개선 확인 |

---

## 한국 시판 정보

Betahistine은 현재 **한국 미허가·미판매** 상태입니다. 허가된 제품이 없어 시판 목록을 제공할 수 없습니다.

> **참고**: Betahistine은 유럽(Serc®, BetaSerc® — Solvay Pharmaceuticals), 일본(Merislon® 6/12 mg — Eisai), 중국 등에서 메니에르병 및 전정성 현기증 적응증으로 허가·시판 중입니다. 한국에서의 미허가는 약물 효능·안전성 문제가 아닌 허가 신청 미제출에 기인하는 것으로 추정됩니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> **보완 필요**: 이번 Evidence Pack에 MFDS 허가사항 데이터(Data Gap DG001) 및 DrugBank MOA/경고 데이터(Data Gap DG002)가 포함되지 않았습니다. 개발 진행 전 유럽 의약품청(EMA) SmPC, DrugBank DB06698, 또는 Serc® 제품 정보를 통해 주요 경고·금기·약물 상호작용 정보를 반드시 보완하시기 바랍니다.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
周邊性眩暈(L1) 및 전정성 메니에르병(L2)에 대해 Phase 2/3 RCT, Cochrane 체계적 문헌고찰 2건, 12개 RCT 메타분석 등 강력한 국제 근거가 존재하며, 유럽 이비인후과학회 가이드라인이 betahistine을 표준 1차 치료로 권고하고 있습니다. 한국 미판매 현황은 개발·도입 기회를 시사합니다.

**진행하려면 필요한 것:**
- **[필수]** DrugBank DB06698에서 완전한 MOA 데이터 수집 (Data Gap DG002 해소)
- **[필수]** MFDS 허가사항 PDF 수집 및 경고·금기·약물 상호작용 분석 (Data Gap DG001 해소)
- 한국·아시아 환자 집단 대상 약동학(PK) 데이터 확인 및 인종 간 차이 평가
- MFDS 허가 신청 전략 수립 (EU/일본 기허가 데이터 준용 가능성 검토)
- **[진행 불가]** 하지불안증후군·이경화증·노인성 난청·고인슐린혈증 적응증(각 L5, Hold): 전임상 기전 연구부터 재평가 필요, 현 시점 개발 권고 불가
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

