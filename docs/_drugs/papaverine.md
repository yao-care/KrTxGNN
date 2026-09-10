---
layout: default
title: Papaverine
parent: 僅模型預測 (L5)
nav_order: 534
evidence_level: L5
indication_count: 10
---

# Papaverine
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

# Papaverine: 혈관 경련 완화용 혈관확장제에서 말초동맥질환으로

## 한 문장 요약

Papaverine은 벤질이소퀴놀린 계열의 오래된 혈관확장제로, 문헌상 혈관 경련(vasospasm) 완화 및 동맥내 주사 시술 보조제로 널리 사용되어 온 약물입니다(단, 한국 내 정식 허가 자료는 확인되지 않음). TxGNN 모델은 **말초동맥질환(Peripheral Arterial Disease)**에 효과가 있을 수 있다고 예측하며, 현재 **3건의 임상시험**과 **20편의 문헌**이 관련되어 있으나, 이 적응증을 직접 입증하는 최근 완료 RCT는 확인되지 않았습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (한국 미시판; 문헌상 혈관 경련·말초순환장애 완화 목적의 전통적 사용만 확인됨) |
| 예측 신규 적응증 | 말초동맥질환 (Peripheral Arterial Disease) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L3 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 Papaverine의 상세 작용기전(MOA) 데이터는 확보되지 않았습니다(DrugBank ID 미확인). 다만 근거 팩에 포함된 문헌들을 종합하면, Papaverine은 평활근 이완 및 혈관확장 작용을 가진 약물로 오랫동안 임상 현장에서 활용되어 왔음을 알 수 있습니다. 예를 들어 동맥내 주사를 통한 혈류량 증가 효과(PMID 6103626, 884824), 급성 동맥폐쇄 환자의 말초 대·미세순환 개선(PMID 524688, 6252675), 관상동맥 및 뇌혈관 경련 완화(PMID 3661361, 8293164) 등 혈관계 전반에 걸친 혈관이완 작용이 반복적으로 보고되고 있습니다.

말초동맥질환(PAD)은 말초혈관의 협착·폐쇄로 인한 허혈성 질환으로, 혈류 개선을 위한 혈관확장이 치료 전략의 핵심입니다. Papaverine이 이미 급성 동맥폐쇄, 간헐성 파행(intermittent claudication), 말초허혈 등 인접 질환군에서 반복적으로 시험되어 온 이력(예: PMID 10485507의 PAD 약물치료 비교 연구, PMID 953493의 PAD 혈류역학 효과 연구)은 TxGNN 예측의 기전적 타당성을 뒷받침합니다. 다만 이러한 연구 다수가 1960~1990년대에 수행된 소규모 관찰연구 또는 학회 초록 수준이어서, 현대적 기준의 근거로는 제한적입니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT05562908](https://clinicaltrials.gov/study/NCT05562908) | N/A | 완료 | 165 | 관상동맥우회술(CABG)에서 내흉동맥 채취 방식(skeletonised vs pedicled) 비교 연구. Papaverine이 직접 개입 약물은 아니며 PAD와의 직접 관련성은 낮음 |
| [NCT06919289](https://clinicaltrials.gov/study/NCT06919289) | N/A | 완료 | 4 | 당뇨병성 말초신경병증 환자 대상 리도카인 vs Papaverine 신경차단 후 혈관 확장 반응(Phoenix Sign) 비교 파일럿 연구. 표본 극소수 |
| [NCT06014242](https://clinicaltrials.gov/study/NCT06014242) | N/A | 철회(등록 0명) | 0 | 중증하지허혈(CLI) 환자의 말초 미세혈관저항과 사지구제 예측 연구, 시작 전 철회됨 |

**참고**: 위 3건 모두 PAD 치료제로서 Papaverine의 유효성을 직접 검증하는 시험은 아닙니다. 신규 완료 RCT 부재.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [10485507](https://pubmed.ncbi.nlm.nih.gov/10485507/) | 1999 | 관찰연구(후향적) | Clinical Therapeutics | 미 국방부 의료체계 내 아스피린·pentoxifylline·papaverine·dipyridamole의 PAD 관련 처치·비용·결과 비교 |
| [953493](https://pubmed.ncbi.nlm.nih.gov/953493/) | 1976 | 학회 초록 | British Journal of Surgery | PAD 환자에서 Papaverine의 혈류역학적 효과 보고 |
| [5920879](https://pubmed.ncbi.nlm.nih.gov/5920879/) | 1966 | 학회 초록 | Surgical Forum | PAD 진단을 위한 Papaverine test 기술 소개 |
| [884824](https://pubmed.ncbi.nlm.nih.gov/884824/) | 1977 | 임상연구 | Circulation | 말초 죽상경화증 환자에서 대혈관 임피던스 측정, Papaverine 유발 혈관확장 반응 이용 |
| [6252675](https://pubmed.ncbi.nlm.nih.gov/6252675/) | 1980 | 비교임상연구 | Vestnik Khirurgii | 급성 동맥폐쇄 환자에서 Papaverine과 trental의 작용기전 비교, trental이 우세 |
| [524688](https://pubmed.ncbi.nlm.nih.gov/524688/) | 1979 | 임상연구 | Vestnik Khirurgii | 급성 동맥폐쇄 54예에서 Papaverine 정맥주사 후 대·미세순환 변화 관찰 |
| [1108646](https://pubmed.ncbi.nlm.nih.gov/1108646/) | 1975 | 리뷰 | Am J Hospital Pharmacy | 말초혈관질환 치료에 쓰이는 혈관확장제(Papaverine 포함) 종합 리뷰, 폐쇄성 질환에는 효과 근거 미흡 결론 |
| [6103626](https://pubmed.ncbi.nlm.nih.gov/6103626/) | 1980 | 임상연구 | Acta Chirurgica Scandinavica | 대퇴-슬와 정맥이식 재건술 중 Papaverine 투여로 그래프트 혈류 용량-의존적 증가 확인 |
| [31264661](https://pubmed.ncbi.nlm.nih.gov/31264661/) | 2019 | 증례보고 | Anatolian J Cardiology | 요골동맥 sheath entrapment(혈관경련) 해소 목적 Papaverine 사용 사례 |
| [4660397](https://pubmed.ncbi.nlm.nih.gov/4660397/) | 1972 | 임상연구 | Terapevticheskii Arkhiv | 관상동맥죽상경화 환자에서 Papaverine 투여 후 말초 동맥 순환 변화 관찰 |

---

## 한국 시판 정보

현재 한국에 허가된 Papaverine 제품 정보가 확인되지 않습니다(허가증 0건, 미시판 상태). 국내 도입 여부를 확인하려면 MFDS(식품의약품안전처) 허가 데이터베이스에서 별도 조회가 필요합니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (주요 경고, 금기, 약물상호작용에 대한 구조화된 데이터 없음)

> 참고: 근거 문헌 중 일부(PMID 32478401 등, 이번 evidence pack에는 미포함)는 Papaverine의 동맥내/해면체내 주사 시 음경지속발기증(priapism)·부정맥 등의 위험을 보고한 바 있어, 실제 진행 시 별도 안전성 자료 확보가 필요합니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
한국 내 허가·시판 이력이 전혀 없고 공식 안전성 자료(경고·금기)가 Blocking 수준으로 결여되어 있어 안전성 초기 평가(S1)를 진행할 수 없습니다. 또한 PAD 적응증에 대한 근거는 대부분 1960~1990년대의 소규모 관찰연구·학회 초록 수준(L3)에 머물러 있으며, 최근 완료된 RCT가 없어 근거 강도가 낮습니다.

**진행하려면 필요한 것:**
- DrugBank/MFDS를 통한 공식 MOA 및 약물 분류 정보 확보
- TFDA/MFDS 수준의 허가사항, 경고, 금기, DDI 정보 확보 (Blocking 데이터 갭 해소)
- PAD 적응증에 대한 최신 전향적 임상연구(가능하면 Phase 2/3 RCT) 존재 여부 재확인
- 동맥내·해면체내 주사 관련 문헌에서 보고된 부정맥, 음경지속발기증 등 안전 신호에 대한 정밀 검토
- 한국 내 원료의약품 수입·제조 현황 및 관련 법규 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

