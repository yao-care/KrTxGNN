---
layout: default
title: Mefenamic Acid
parent: 높은 근거 (L1-L2)
nav_order: 462
evidence_level: L2
indication_count: 8
---

# Mefenamic Acid
{: .fs-9 }

근거 수준: **L2** | 예측 적응증: **8** 건
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

# Mefenamic Acid: 경도~중등도 통증·염증성 질환에서 류마티스 관절염으로

## 한 문장 요약

Mefenamic acid(DrugBank DB00784)는 fenamate 계열 NSAID로, 국제적으로 경도~중등도 통증 및 염증성 질환에 사용되어 온 약물입니다. TxGNN 모델은 **류마티스 관절염(Rheumatoid Arthritis)**에 효과가 있을 것으로 예측(점수 99.73%)하며, 현재 등록된 임상시험은 없지만 **20편의 문헌**(1960~2018년대 RCT 다수 포함)이 이 방향을 지지합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 국내(한국) 허가 자료 없음 — 일반적으로 경도~중등도 통증/염증성 질환에 사용되는 NSAID 계열 |
| 예측 신규 적응증 | 류마티스 관절염 (Rheumatoid Arthritis) |
| TxGNN 예측 점수 | 99.73% |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미상장 (시판되지 않음) |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

상세 작용기전(MOA) 데이터는 현재 확보되어 있지 않습니다(High severity 데이터 갭). 다만 알려진 약리 분류에 따르면, mefenamic acid는 fenamate 계열 NSAID로 비선택적 COX-1/COX-2 억제 작용과 프로스타글란딘 수용체 길항 활성을 동시에 지니고 있습니다.

류마티스 관절염(RA)의 관절 활막 염증은 프로스타글란딘 매개 경로가 핵심적으로 관여하는데, mefenamic acid의 COX 억제 기전은 이 경로를 직접 표적으로 합니다. 실제로 ibuprofen, sulindac, flurbiprofen 등 이미 RA 치료에 사용되는 다른 NSAID와 동일한 기전이며, 1960~1970년대에 다수의 이중맹검 비교시험을 통해 RA 환자에서의 진통·항염 효과가 반복적으로 확인된 바 있습니다. 즉 이번 예측은 새로운 가설이라기보다, 이미 검증된 약리 경로가 지식그래프 임베딩을 통해 재확인된 사례에 가깝습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다(ClinicalTrials.gov, ICTRP 모두 0건).

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [373989](https://pubmed.ncbi.nlm.nih.gov/373989/) | 1979 | RCT | Current Medical Research and Opinion | RA 환자 24명 대상 mefenamic acid·sulindac·flurbiprofen 이중맹검 교차시험. 위약 대비 통증점수·관절압통·조조강직 모두 유의하게 개선 |
| [330287](https://pubmed.ncbi.nlm.nih.gov/330287/) | 1977 | RCT | The Journal of International Medical Research | RA 환자 40명, mefenamic acid vs ibuprofen 이중맹검 비교. 진통·항염 효과가 유의한 차이 없이 유사, 부작용도 경미하게 유사 |
| [796645](https://pubmed.ncbi.nlm.nih.gov/796645/) | 1976 | RCT | The Medical Journal of Australia | RA 환자 대상 mefenamic acid(1500mg/day) vs ibuprofen(1200mg/day) 이중맹검 교차시험. 효과 양호, 부작용은 대부분 위장관계로 경미 |
| [5920657](https://pubmed.ncbi.nlm.nih.gov/5920657/) | 1966 | 비교시험 | British Medical Journal | mefenamic acid·flufenamic acid를 aspirin·phenylbutazone과 비교한 RA 임상시험 |
| [4294443](https://pubmed.ncbi.nlm.nih.gov/4294443/) | 1967 | Cohort | Annals of the Rheumatic Diseases | RA에서 mefenamic acid의 효과를 관찰한 초기 임상연구 |
| [306128](https://pubmed.ncbi.nlm.nih.gov/306128/) | 1978 | Review | Scottish Medical Journal | RA 치료에서 mefenamic acid의 위치를 정리한 임상 리뷰 |
| [10439](https://pubmed.ncbi.nlm.nih.gov/10439/) | 1976 | 비교연구 | The Journal of Rheumatology | RA 환자 684명 대상 항류마티스 약물 10종(mefenamic acid 포함)의 진통 효과 평가 |
| [6039589](https://pubmed.ncbi.nlm.nih.gov/6039589/) | 1967 | 비교시험 | Annals of the Rheumatic Diseases | RA 외래환자 대상 mefenamic acid·flufenamic acid를 phenylbutazone·aspirin과 비교 평가 |
| [4890710](https://pubmed.ncbi.nlm.nih.gov/4890710/) | 1967 | RCT | Reumatismo | RA 치료에서 mefenamic acid의 이중맹검 임상 및 생화학적 대조 관찰(예비 보고) |
| [5676955](https://pubmed.ncbi.nlm.nih.gov/5676955/) | 1968 | Case Report | British Medical Journal | mefenamic acid 장기 복용 중 자가면역용혈성빈혈 3예 보고 — 약물 중단 후 회복(안전성 신호) |

## 한국 시판 정보

현재 한국에 등록된 허가 정보가 없습니다 (허가증 0건, 미상장).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
류마티스 관절염에 대한 mefenamic acid의 효능을 지지하는 다수의 초기 RCT(373989, 330287, 796645 등)가 존재하며 기전적 타당성도 높지만, 모두 1960~1970년대 소규모 연구로 현대적 임상시험 등록은 전무합니다. 또한 한국 내 허가·시판 이력과 안전성 라벨 데이터가 모두 부재하여, 안전성 초기 심사(S1) 단계 진입이 현재 차단되어 있습니다.

**진행하려면 필요한 것:**
- TFDA/식약처 등 규제기관의 최신 허가사항(경고, 금기, 부작용) 확보 — Blocking 등급 데이터 갭
- 상세 작용기전(MOA) 데이터 확보
- 현대적 기준에 따른 RA 적응증 재현 임상시험(또는 관찰연구) 설계 검토
- 자가면역용혈성빈혈 등 과거 보고된 안전성 신호에 대한 최신 약물감시 자료 확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

