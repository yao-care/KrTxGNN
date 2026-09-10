---
layout: default
title: Fludarabine
parent: 僅模型預測 (L5)
nav_order: 328
evidence_level: L5
indication_count: 10
---

# Fludarabine
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

# Fludarabine: 만성 림프구성 백혈병에서 형질세포골수종(다발골수종)으로

## 한 문장 요약

Fludarabine은 퓨린 유사체 계열의 세포독성 항암제로, 문헌상 B세포 만성 림프구성 백혈병(CLL), 모세포백혈병(hairy cell leukemia), 무통성 림프종 치료에 사용되어 온 약물입니다. TxGNN 모델은 **형질세포골수종(Plasma Cell Myeloma, 다발골수종)**에 효과가 있을 수 있다고 예측하며, 현재 **50건 이상의 임상시험**과 **20편의 문헌**이 이 방향과 관련되어 있으나, 그중 상당수는 직접적 항골수종 치료가 아닌 이식/CAR-T 전처치(림프구 제거) 목적의 병용 사용임에 유의가 필요합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 허가 정보 없음 (문헌상 만성 림프구성 백혈병·모세포백혈병·무통성 림프종에 사용) |
| 예측 신규 적응증 | 형질세포골수종 (Plasma Cell Myeloma) |
| TxGNN 예측 점수 | 99.82% |
| 근거 수준 | L2 |
| 한국 시판 현황 | ✗ 미상 (미허가) |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Fludarabine은 퓨린 유사체로, 체내에서 F-ara-ATP로 인산화된 후 DNA 중합효소와 리보뉴클레오티드 환원효소를 억제하여 림프구(악성 형질세포 포함)에 세포독성을 나타내는 동시에 강력한 면역억제 작용을 가집니다.

형질세포골수종 영역에서 Fludarabine의 임상적 활용은 두 갈래로 나뉩니다. 첫째, 이종 조혈모세포이식(Flu/Melphalan, Flu/Bortezomib 등)의 전처치 화학요법으로서 이식편대종양효과(GVT)를 유도하는 역할이며, 둘째, BCMA/GPRC5D/FcRL5 표적 CAR-T 세포치료 전 림프구 제거(lymphodepletion) 용도로 광범위하게 사용됩니다. 다만 이 경우 실질적 항종양 효과는 이식편이나 CAR-T 세포에서 기인하며, Fludarabine 자체는 보조적 역할입니다.

한편 문헌(PMID 17976186)에 따르면 골수종 세포주(RPMI8226)를 이용한 시험관 내·생체 내 연구에서 Fludarabine이 Akt 인산화 감소를 동반하며 골수종 세포 증식을 직접 억제한 것으로 보고되어, 순수 전처치 역할을 넘어선 직접적 기전상 개연성도 일부 존재합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01658319](https://clinicaltrials.gov/study/NCT01658319) | Phase 1 | 완료 | 20 | Fludarabine + Methoxyamine(TRC102) 직접 병용화학요법, 재발/불응성 혈액암(골수종 포함) 치료 목적 |
| [NCT01453101](https://clinicaltrials.gov/study/NCT01453101) | Phase 2 | 완료 | 54 | 골수종 이종이식 전처치(Fludarabine+Melphalan+Bortezomib) vs 기존 대조군 비교, 무진행생존 개선 가설 |
| [NCT01503242](https://clinicaltrials.gov/study/NCT01503242) | Phase 1 | 완료 | 15 | 90Y 표지 항체(BC8)+Fludarabine+TBI 병용 후 이종 PBSC 이식, 골수종 치료 |
| [NCT00578942](https://clinicaltrials.gov/study/NCT00578942) | Phase 2 | 완료 | 48 | Campath-1H 정제 비清髓性 이종이식, 골수종 포함 혈액암 장기 예후 추적 |
| [NCT00802568](https://clinicaltrials.gov/study/NCT00802568) | Phase 2 | 완료 | 48 | Fludarabine+Busulfan+ATG 감량강도 이종이식, 골수종 환자 대상 |
| [NCT01408563](https://clinicaltrials.gov/study/NCT01408563) | Phase 2 | 완료 | 33 | Fludarabine+Melphalan+저선량 TBI 이용 감량강도 이중 제대혈 이식(혈액암 포함) |
| [NCT06196255](https://clinicaltrials.gov/study/NCT06196255) | Phase 1/2 | 모집 중 | 20 | Anti-FcRL5 CAR-T 치료 전 Fludarabine+Cyclophosphamide 림프구 제거, 재발/불응 골수종 |
| [NCT07477912](https://clinicaltrials.gov/study/NCT07477912) | Phase 1/2 | 모집 중 | 30 | Anti-BCMA CAR-T 치료, Fludarabine 전처치 병용 추정, 성인 재발/불응 골수종 |
| [NCT06577025](https://clinicaltrials.gov/study/NCT06577025) | Phase 2 | 진행 중(모집 종료) | 43 | Cilta-cel/Tal-D/Tec-D 순차요법 후 신규 진단 골수종, 림프구 제거 전처치 문맥 |
| [NCT00006251](https://clinicaltrials.gov/study/NCT00006251) | Phase 1/2 | 완료 | 21 | Fludarabine+저선량 TBI+PBSC 이식, 혼합 조혈 키메리즘 유도(혈액암 전반) |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [17976186](https://pubmed.ncbi.nlm.nih.gov/17976186/) | 2007 | 전임상(in vitro/in vivo) | European Journal of Haematology | Fludarabine이 골수종 세포주(RPMI8226) 증식을 직접 억제, Akt 인산화 감소 동반 — 직접적 항골수종 활성의 핵심 근거 |
| [7781758](https://pubmed.ncbi.nlm.nih.gov/7781758/) | 1995 | 케이스 보고 | European Journal of Haematology | 형질세포백혈병에서의 Fludarabine 사용 사례 |
| [38483213](https://pubmed.ncbi.nlm.nih.gov/38483213/) | 2024 | Phase 1 | American Journal of Clinical Oncology | Bortezomib+Fludarabine+Melphalan(±전신골수조사) 이종이식 전처치, 고위험/재발 골수종 |
| [33784005](https://pubmed.ncbi.nlm.nih.gov/33784005/) | 2021 | Phase 1 | Clinical and Translational Medicine | Anti-BCMA CAR-T(Fludarabine 림프구 제거 병용), 재발/불응 골수종 및 형질세포백혈병 |
| [36690811](https://pubmed.ncbi.nlm.nih.gov/36690811/) | 2023 | Phase 1 | Nature Medicine | UNIVERSAL 시험, 동종 ALLO-715 BCMA CAR-T + ALLO-647 림프구 제거 전처치 |
| [39365257](https://pubmed.ncbi.nlm.nih.gov/39365257/) | 2025 | 코호트 | Blood | 실사용 환경 cilta-cel 치료 결과, 표준 림프구 제거 전처치 포함 |
| [37701906](https://pubmed.ncbi.nlm.nih.gov/37701906/) | 2023 | Phase 2 | Leukemia Research Reports | 분할용량 Busulfan+Fludarabine+PTCy 이종이식, 골수종/골수섬유증 |
| [17310135](https://pubmed.ncbi.nlm.nih.gov/17310135/) | 2007 | 후향적 코호트 | Bone Marrow Transplantation | Fludarabine+Treosulfan 저독성 전처치, 골수종 이종이식 34례 분석 |
| [37833271](https://pubmed.ncbi.nlm.nih.gov/37833271/) | 2023 | 후향 비교 | Blood Cancer Journal | Bendamustine vs Fludarabine/Cyclophosphamide 림프구 제거, BCMA CAR-T 치료 전 골수종 |
| [35333600](https://pubmed.ncbi.nlm.nih.gov/35333600/) | 2022 | 장기 추적 | Journal of Clinical Oncology | BCMA+CD19 이중 표적 CAR-T 장기 추적, 골수종 |

---

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 화학요법제 (퓨린 유사체 / 뉴클레오시드 유사체 — DNA 중합효소·리보뉴클레오티드 환원효소 억제) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | CBC(백혈구 분류 포함), 신기능, 종양융해증후군 관련 지표(종양 부담이 큰 경우) |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
전임상 직접 항골수종 활성 근거(PMID 17976186)와 Phase 1 병용화학요법(NCT01658319)이 존재하여 L2 수준의 근거를 확보했습니다. 다만 확인된 임상근거의 대다수는 Fludarabine을 이종이식 및 BCMA/FcRL5 CAR-T 치료의 전처치(림프구 제거)로 사용한 것으로, 직접적 단독 항골수종 요법으로서의 근거와는 구분하여 해석해야 합니다. 근연 적응증인 무증상 형질세포골수종(indolent plasma cell myeloma) 및 골수형성이상증후군(MDS)에서도 동일한 면역억제/전처치 기전의 L2 근거가 확인되어 전체적인 기전 개연성을 뒷받침합니다.

**진행하려면 필요한 것:**
- 작용기전(MOA) 상세 데이터 확보 (DG002, High 우선순위)
- 한국(TFDA 상당) 허가사항의 경고·금기·상호작용 정보 확보 (DG001, Blocking 우선순위 — 안전성 초기평가 진입 필수 조건)
- 직접적 항골수종 단독요법 근거와 이식/CAR-T 전처치 근거의 구분된 재평가
- 한국 내 허가·수입 현황 확인 (현재 미허가 상태)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

