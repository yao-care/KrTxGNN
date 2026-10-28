---
layout: default
title: Albendazole
parent: 높은 근거 (L1-L2)
nav_order: 31
evidence_level: L2
indication_count: 3
last_modified_at: 2026-10-28
description: "Albendazole: 예측 신규 적응증 포충증 (Alveolar echinococcosis) (근거 수준 L5). 기존 적응증: 회충, 요충, 십이지장충, 편충, 아메리카 구충, 분선충의 감염 및 이들 혼합감염의 치료"
monitor_inn: "ALBENDAZOLE"
predicted_indications: ["alveolar echinococcosis", "coenurosis", "Cestode infectious disease"]
---

# Albendazole
{: .fs-9 }

근거 수준: **L2** | 예측 적응증: **3** 건
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

## Albendazole: 장내 선충 감염에서 포충증(알veolar echinococcosis)으로
{: .text-alpha }

## 한 문장 요약

Albendazole은 회충, 요충, 십이지장충, 편충, 구충, 분선충 감염 치료에 사용되어 온 구충제입니다.
TxGNN 모델은 **포충증(알veolar echinococcosis, 다포조충증)**에 효과가 있을 수 있다고 예측하며, 이 질환에 대해 **3건의 임상시험**과 **20편의 문헌**이 확인되었습니다.
이 중 Phase 2 시험 1건(완료, 194명)이 직접 근거이며, 세계보건기구 비공식 작업반(WHO-IWGE) 전문가 합의에서도 표준 치료로 권고됩니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 회충, 요충, 십이지장충, 편충, 아메리카 구충, 분선충의 감염 및 이들 혼합감염의 치료 |
| 예측 신규 적응증 | 포충증 (Alveolar echinococcosis) |
| TxGNN 예측 점수 | 0.9997 |
| 근거 수준 | L2 (완료된 Phase 2 시험 1건; 무작위·대조 설계 여부는 시험 기록 확인 필요) |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 20건 (모두 단일제, 유효) |
| 권장 결정 | Proceed with Guardrails |

참고: 같은 약물에서 예측된 다른 적응증은 다음과 같습니다.
- 코에누루스증(coenurosis, 점수 0.9983): 근거 수준 L1. 다만 연결된 시험은 대부분 신경낭미충증 시험이며 진짜 코에누루스증에 대한 직접 시험 근거는 제한적입니다.
- 조충 감염성 질환(Cestode infectious disease, 점수 0.9974): 근거 수준 L3. 여러 조충 질환을 아우르는 포괄적 분류입니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 DrugBank 기준으로는 확보되지 않았습니다. 다만 이 보고서를 위해 정리된 자료에 따르면, albendazole은 벤즈이미다졸 계열 약물로 기생충의 beta-tubulin에 결합해 미세소관 중합을 억제하고 포도당 흡수를 방해합니다. 이 기전은 이미 허가된 선충 감염 적응증과 동일합니다.

다포조충(*Echinococcus multilocularis*)의 유충(metacestode) 단계에도 같은 기전이 작용합니다. 다만 albendazole은 유충을 죽이는 살충 작용이 아니라 성장을 억제하는 정충(parasitostatic) 작용을 하므로, 수술이 어려운 환자에서는 장기 또는 평생 억제 치료가 필요할 수 있습니다. 포충증은 주로 간을 침범하며 악성 종양처럼 보이는 질환입니다. 수술이 가능하면 수술이 우선이고, 수술이 불가능하면 약물 치료가 표준입니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT07182305](https://clinicaltrials.gov/study/NCT07182305) | Phase 2 | 완료 | 194 | 키르기스스탄의 초기 포충증 환자 대상 albendazole 치료 시험. 약물·질환이 직접 일치하는 가장 강한 근거 |
| [NCT02876146](https://clinicaltrials.gov/study/NCT02876146) | 해당 없음 | 완료 | 50 | albendazole 치료 중인 간 포충증 환자의 기생충 생존성 및 추적 관찰 표지자 연구 (효능 시험 아님) |
| [NCT06483880](https://clinicaltrials.gov/study/NCT06483880) | 해당 없음 | 불명 | 24 | 폐 포충(낭성 echinococcosis) 절제 후 보조 albendazole 대 위약 무작위 시험. 질환형이 달라 간접 근거 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [19931502](https://pubmed.ncbi.nlm.nih.gov/19931502/) | 2010 | Review | Acta Trop | 낭성·포충증 진단, 치료, 추적 관찰에 대한 전문가 합의 |
| [30760475](https://pubmed.ncbi.nlm.nih.gov/30760475/) | 2019 | Review | Clin Microbiol Rev | 21세기 echinococcosis 진단·치료 발전 |
| [39254012](https://pubmed.ncbi.nlm.nih.gov/39254012/) | 2024 | Review | Tidsskr Nor Laegeforen | 포충증 개관. 광범위 수술 절제와 장기 약물 치료 병행 |
| [40093668](https://pubmed.ncbi.nlm.nih.gov/40093668/) | 2025 | Review | World J Gastroenterol | 간 echinococcosis 관리 현황 |
| [34161992](https://pubmed.ncbi.nlm.nih.gov/34161992/) | 2021 | Review | Semin Liver Dis | 간 포충증의 역학과 임상 양상 |
| [25526545](https://pubmed.ncbi.nlm.nih.gov/25526545/) | 2014 | Review | Parasite | albendazole·mebendazole 이후의 치료 옵션 탐색 |
| [10980173](https://pubmed.ncbi.nlm.nih.gov/10980173/) | 2000 | 관찰 연구 | J Antimicrob Chemother | 35명 대상 benzimidazole 장기 치료 성과 비교 (평균 39개월 추적) |
| [36974024](https://pubmed.ncbi.nlm.nih.gov/36974024/) | 2022 | 리뷰 | Zhongguo Xue Xi Chong Bing Fang Zhi Za Zhi | 수술이 어려운 환자에서 albendazole이 질병 진행을 늦출 수 있음 |
| [38501660](https://pubmed.ncbi.nlm.nih.gov/38501660/) | 2024 | 전임상 | Antimicrob Agents Chemother | 간 포충증 모델 쥐에서 albendazole 용해성 제제의 대사 및 약리 연구 |
| [39508157](https://pubmed.ncbi.nlm.nih.gov/39508157/) | 2024 | 리뷰 | Parasitology | 현재 치료는 albendazole에만 의존하며 살충 작용이 없고 중대한 이상반응 가능 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201507495 | 모아졸정 | 필름코팅정 | 회충, 요충, 십이지장충, 편충, 아메리카 구충, 분선충의 감염 및 이들 혼합감염의 치료 |
| 198701888 | 젠텔정400밀리그램 | 필름코팅정 | 회충, 요충, 십이지장충, 편충, 아메리카 구충, 분선충의 감염 및 이들 혼합감염의 치료 |
| 199300217 | 종근당알벤다졸정 | 필름코팅정 | 회충, 요충, 십이지장충, 편충, 아메리카 구충, 분선충의 감염 및 이들 혼합감염의 치료 |
| 200200858 | 알나졸정400밀리그램 | 필름코팅정 | 회충, 요충, 십이지장충, 편충, 아메리카 구충, 분선충의 감염 및 이들 혼합감염의 치료 |
| 202003237 | 제일알벤다졸정 | 필름코팅정 | 회충, 요충, 십이지장충, 편충, 아메리카 구충, 분선충의 감염 및 이들 혼합감염의 치료 |

전체 20건 중 대표 5건만 기재했습니다. 모두 경구 정제이며, 일부는 수출용입니다. 현재 한국 허가 적응증에는 포충증이 포함되어 있지 않습니다.

## 안전성 고려사항

- **주요 경고·금기**: 허가사항의 경고 및 금기 정보는 이번 데이터에서 확보되지 않았으므로 허가사항을 참조하세요.
- **지식 그래프 기반 금기 관련 질환**(허가 문서가 아닌 TxGNN 지식 그래프 기반): 간 질환, 담낭 질환, 호중구감소증, 무과립구증, 빈혈, 대적혈구성 빈혈, 범혈구감소증, 특발성 재생불량성 빈혈, 재생불량성 빈혈
- **약물 상호작용**: 총 96건이 확인되었습니다. 주요 예시는 다음과 같습니다.
  - 중등도: aprepitant, cobicistat, deferasirox, 방사성 요오드(I-123, I-131), fostamatinib, alemtuzumab, amprenavir, anagrelide, apalutamide, bendamustine, bexarotene, binimetinib, boceprevir, bosentan
  - 경미: cimetidine, dexamethasone, lidocaine, armodafinil
- **적용 시 권고 사항**: 장기 치료 시 간효소와 혈구 수 모니터링이 필요합니다.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
포충증에 대해 직접 일치하는 완료된 Phase 2 시험(194명)이 있고, albendazole은 국제 전문가 합의에서 표준 치료로 인정됩니다. 다만 허가사항 기반 안전성 정보가 없고 한국 허가 적응증에 포충증이 없어, 안전장치를 갖춘 진행이 적절합니다.

**진행하려면 필요한 것:**
- 식약처 허가사항(경고, 금기)을 확보하여 안전성 선별 수행
- DrugBank 등에서 상세 작용 기전(MOA) 데이터 보완
- NCT07182305의 무작위·대조 설계 여부 확인으로 L2 판정 검증
- 장기 투여 시 간효소와 혈구 수 정기 모니터링 계획, 간·담낭 질환 및 골수 억제 환자에 대한 사용 제한 검토
- 병용 약물의 상호작용(특히 CYP 관련 약물) 점검
- 한국 내 포충증 적응증 추가를 위한 허가 변경 경로 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

