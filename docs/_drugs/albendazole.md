---
layout: default
title: Albendazole
parent: 僅模型預測 (L5)
nav_order: 30
evidence_level: L5
indication_count: 3
---

# Albendazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Albendazole: 장내 기생충 감염증에서 폐포성 에키노코쿠스증으로

## 한 문장 요약

Albendazole은 회충·구충·편충·촌충 등 광범위한 기생충 감염 치료에 사용되는 벤즈이미다졸계 구충제로, WHO 필수의약품 목록에 등재된 확립된 항기생충제입니다.
TxGNN 모델은 **폐포성 에키노코쿠스증(Alveolar Echinococcosis)**에 효과가 있을 것으로 예측하며,
현재 **5건의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 장내 기생충 감염증 (구충제; WHO 필수의약품 목록 등재) |
| 예측 신규 적응증 | 폐포성 에키노코쿠스증 (Alveolar Echinococcosis) |
| TxGNN 예측 점수 | 99.97% |
| 근거 수준 | L2 |
| 한국 시판 현황 | ✗ 미허가 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Albendazole은 광범위 벤즈이미다졸계 항기생충제로, **기생충의 β-tubulin에 선택적으로 결합**하여 미세소관 중합을 억제하고 세포 분열을 차단합니다. 동시에 포도당 흡수를 저해하여 기생충의 에너지(ATP) 생산을 고갈시킵니다. 이 이중 작용 기전은 폐포성 에키노코쿠스증의 원인 기생충인 *Echinococcus multilocularis*에 직접 작용합니다.

폐포성 에키노코쿠스증(AE)은 *E. multilocularis* 유충의 간 내 의종양성(pseudotumoral) 발달로 인한 치명적인 기생충 질환입니다. 치료하지 않으면 감염 후 10~15년 내 치명률이 100%에 근접하는 것으로 알려져 있습니다. Albendazole은 수술이 불가능한 환자에 대한 장기 경구 투여 요법으로 WHO 및 EATG(유럽 에키노코쿠스증 치료그룹) 가이드라인에서 공식 권고되고 있으며, 수술 전후 보조 요법으로서도 강력한 문헌 근거가 있습니다.

다만 albendazole은 기생충 억제(parasitostatic) 효과만 있어 완치가 어렵고 장기 투여가 필요하며, 치료 중단 시 기생충이 다시 증식할 수 있다는 한계가 있습니다. 전 세계에서 30년 이상 임상 적용된 확립된 치료제임에도 한국에서는 현재 미허가 상태로, TxGNN의 고점수(99.97%) 예측은 이미 전 세계적으로 표준화된 이 치료의 국내 도입 필요성을 시사합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT07182305](https://clinicaltrials.gov/study/NCT07182305) | Phase 2 | 완료 | 194 | 키르기스스탄 조기 AE 환자 대상 albendazole 치료 RCT; 치명률 접근 100%인 AE에서 parasitostatic 치료 효과 직접 평가 (본 적응증 최고 등급 직접 임상근거) |
| [NCT02876146](https://clinicaltrials.gov/study/NCT02876146) | N/A | 완료 | 50 | Albendazole 치료 중인 간 AE 환자에서 기생충 생존력 판단 및 치료 중단 시점 결정을 위한 영상·혈액 바이오마커 탐색 전향적 연구 |
| [NCT06483880](https://clinicaltrials.gov/study/NCT06483880) | N/A | 불명 | 24 | 폐 낭성 에키노코쿠스증(CE) 절제술 후 보조 albendazole의 6개월 내 재발 감소 효과를 위약 대조 RCT로 평가 |
| [NCT05824442](https://clinicaltrials.gov/study/NCT05824442) | N/A | 진행 중 | 43 | AE·CE 포함 에키노코쿠스증 진단을 위한 신규 다중 정량 PCR 기술 평가; albendazole 치료 환자 포함 |
| [NCT07176598](https://clinicaltrials.gov/study/NCT07176598) | N/A | 완료 | 1 | 삼각근 원발성 근육 포충증 오진 증례; albendazole 치료 포함 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [19931502](https://pubmed.ncbi.nlm.nih.gov/19931502/) | 2010 | 전문가 합의 가이드라인 (WHO/EATG) | Acta Tropica | WHO-IWGE 전문가 합의; CE·AE 진단·치료·추적 기준 제시, albendazole 장기 요법 권고 포함 |
| [30760475](https://pubmed.ncbi.nlm.nih.gov/30760475/) | 2019 | 종합 리뷰 | Clinical Microbiology Reviews | 에키노코쿠스증의 21세기 유전체학·진단·치료 발전 현황 종합 고찰; 중국 고유병지역 현황 포함 |
| [39311470](https://pubmed.ncbi.nlm.nih.gov/39311470/) | 2024 | 리뷰 | Parasite (Paris) | AE 화학요법 현황 고찰; benzimidazole의 한계(간독성, 내성)와 신규 치료 옵션 탐색 |
| [36974024](https://pubmed.ncbi.nlm.nih.gov/36974024/) | 2022 | 리뷰 | 中國血吸蟲病防治雜誌 | AE 치료에서 albendazole 연구 진전 종합; 수술 불가 환자에서 질병 진행 억제 효과 정리 |
| [25526545](https://pubmed.ncbi.nlm.nih.gov/25526545/) | 2014 | 리뷰 | Parasite (Paris) | AE·CE 치료에서 albendazole·mebendazole 이외 신규 치료 후보물질 탐색 및 전임상 검토 |
| [40093668](https://pubmed.ncbi.nlm.nih.gov/40093668/) | 2025 | 리뷰 | World J Gastroenterol | 간 에키노코쿠스증 관리 현황; 완전 절제(근치적 간절제) 후 albendazole 보조요법 권고 |
| [39254012](https://pubmed.ncbi.nlm.nih.gov/39254012/) | 2024 | 리뷰 | Tidsskrift for den Norske laegeforening | AE 임상·영상·치료 특성 고찰; 비유행지역 수입 증례에서 albendazole 장기 투여 역할 |
| [34161992](https://pubmed.ncbi.nlm.nih.gov/34161992/) | 2021 | 리뷰 | Seminars in Liver Disease | 간 AE 병태생리·진단·albendazole 기반 치료 전략; 장기 생존율 및 예후 검토 |
| [34808118](https://pubmed.ncbi.nlm.nih.gov/34808118/) | 2022 | 리뷰 | Acta Tropica | CE·AE 비수술적 치료 신규 옵션 현황; albendazole·mebendazole이 현재 유일한 허가 비수술 치료제임을 재확인 |
| [38501660](https://pubmed.ncbi.nlm.nih.gov/38501660/) | 2024 | 약리 연구 | Antimicrobial Agents and Chemotherapy | 이차 간 AE 쥐 모델에서 albendazole 용해도 개선 제제(결정 분산계, HCl 복합체 등)의 약동학·약력학 비교 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 추가 예측 적응증

TxGNN은 albendazole의 추가 2개 적응증을 예측하였습니다.

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 | 권장 결정 | 비고 |
|------|-----------|-----------|---------|---------|------|
| 2 | 뇌우리충증 (Coenurosis) | 99.83% | L4 | Research Question | *Taenia multiceps/T. serialis* β-tubulin 상동성 기반 기전 유추; 직접 RCT 부재, 개별 증례 및 신경낭미충증 외삽 수준 |
| 3 | 조충성 감염증 (Cestode Infectious Disease) | 99.74% | L1 | Proceed with Guardrails | 신경낭미충증 등 다수 Phase 3 RCT 완료(NCT00283699 n=178, NCT00290823 n=110); albendazole 표준치료제로 확립 |

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
Phase 2 완료 RCT(NCT07182305, n=194)가 조기 폐포성 에키노코쿠스증 환자에서 albendazole의 치료 효과를 직접 평가하였으며, WHO/EATG 전문가 합의 가이드라인(PMID 19931502)과 20편의 지지 문헌이 이 적응증의 타당성을 강력히 뒷받침합니다. 전 세계 30년 이상 임상 사용 이력을 보유한 확립된 치료제이나, 한국에서는 현재 미허가 상태입니다.

**진행하려면 필요한 것:**
- 한국 식품의약품안전처(MFDS) 허가사항 확보를 통한 공식 경고·금기·이상반응 정보 검토 (**우선순위 높음: Blocking**)
- DrugBank API를 통한 상세 약물 작용 기전(MOA) 데이터 확보 (**High**)
- 한국 내 AE 유병률 및 환자 수 추정 (희귀질환 지정 가능성 및 급여 전략 검토)
- 장기 albendazole 투여 시 모니터링 프로토콜 수립 (간기능 검사, CBC 포함 혈구 분류, 전해질)
- 해외 허가 현황(일본 PMDA, 미국 FDA, EMA 등) 비교 분석을 통한 한국 허가 신청 전략 수립
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

