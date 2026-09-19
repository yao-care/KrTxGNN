---
layout: default
title: Glycyrrhizic Acid
parent: 모델 예측만 (L5)
nav_order: 364
evidence_level: L5
indication_count: 10
---

# Glycyrrhizic Acid
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

# Glycyrrhizic acid：무승인 적응증 → 류마티스 관절염

## 한 문장 요약

Glycyrrhizic acid（감초산）는 감초 뿌리에서 추출한 천연 삼중환 배당체로, 현재 대만에는 승인된 약품 허가증이 없습니다. TxGNN 모델은 총 10개의 새로운 적응증을 예측했으며, 그 중 **류마티스 관절염(Rheumatoid Arthritis)**이 가장 완전한 인체 연구 근거를 보유하고 있으며, 지지 문헌이 **20편**이고 **1개의 임상시험**이 진행 중이며, 모든 후보 중 근거 수준이 가장 높습니다(L3, 결정 단계 S2). 또한 **거대세포바이러스 감염**과 **폐동맥 고혈압**은 각각 5편 및 7편의 동물/임상 관찰 문헌으로 뒷받침됩니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 대만 무승인 적응증 |
| 예측 새 적응증 | 류마티스 관절염(Rheumatoid Arthritis) |
| TxGNN 예측 점수 | 97.82%(10개 예측 중 근거 최충실) |
| 근거 수준 | L3(관찰 연구 + 체계적 임상전 문헌) |
| 대만 시판 현황 | ✗ Not marketed |
| 허가증 수 | 0건 |
| 권장 결정 | Research Question |

---

## 이 예측이 타당한 이유는?

Glycyrrhizic acid는 감초(*Glycyrrhiza glabra* / *G. uralensis*)의 주요 활성 성분으로, 오환 삼중환 구조에 속하며 분자량은 822.93 Da입니다. 장내 미생물총의 작용으로 18β-glycyrrhetinic acid(18β-감초차산, GA)로 대사되며, 후자도 독립적인 약리활성을 가지고 있고 여러 동물 연구의 시험 성분이기도 합니다.

현재 관련 문헌에서 보고된 감초산의 주요 작용 기전은 다음을 포함합니다: ① **NF-κB 신호 통로**억제로 TNF-α, IL-1β, IL-6 등 친염증 사이토카인의 전사 감소; ② **HMGB1(High Mobility Group Box 1)** 단백질 길항으로 HMGB1–RAGE–NF-κB 신호축 차단; ③ **11β-HSD2(11β-히드록시코르티코이드 탈수소효소2)** 억제로 코르티솔-코르티코스테론 전환 균형 간섭; ④ JAK1/2–STAT3 통로 조절 효과 문헌 보고(탐색적 성격). 

류마티스 관절염의 병리 핵심은 친염증 사이토카인의 과도 활성화(TNF-α, IL-6 주도), 활액 섬유모세포(FLS)의 비정상 증식, 그리고 RANKL이 유도한 파골세포 과도 분화로 인한 골 침식입니다. 감초산의 다중 항염증 기전—NF-κB 억제, HMGB1 길항, JAK-STAT 조절, 파골세포 분화 억제—은 RA의 현존 약물의 주요 치료 표적과 높은 일치성을 보이며, 이러한 재이용 가설에 명확한 기전 연결을 제공합니다. 그러나 현재 다량의 문헌은 감초산을 복합제 성분 또는 약물 전달 운반체로 사용하고 있으며, 순수 감초산 단독 제제의 무작위 대조 임상시험이 부족하여 임상 전환 경로는 여전히 체계적 검증이 필요합니다.

---

## 모든 예측 적응증 개요

| 순위 | 질병 | TxGNN 점수 | 근거 수준 | 권장 | 비고 |
|------|------|-----------|---------|------|------|
| 1 | Multiple Endocrine Neoplasia | 99.28% | L5 | Hold | 유전성 다선체 종양, 직접 기전 없음 |
| 2 | Amenorrhea | 98.87% | L5 | Hold | 감초산은 월경 불규칙을 유발할 수 있는 것으로 알려짐, 부정적 효과 |
| 3 | Hypoalphalipoproteinemia | 98.48% | L5 | Hold | 지질 조절 기전 문헌 부족 |
| 4 | Infectious Bovine Rhinotracheitis | 98.39% | L5 | Hold | 수의학 질병, 인간 의료 범위 초과 |
| 5 | Malignant Catarrh | 98.39% | L5 | Hold | 반추동물 전염병, 인간 의료 범위 초과 |
| 6 | Cytomegalovirus Infection | 98.24% | L3 | Research Question | 항바이러스 기전 + 소아 임상 관찰 |
| 7 | Acne(Disease) | 98.18% | L4 | Research Question | 항염증 기전 + 1개 임상 중재 보고 |
| 8 | Kyphoscoliotic Heart Disease | 97.96% | L5 | Hold | 기계적 병인, 기전 연결 없음 |
| 9 | Pulmonary Hypertension | 97.91% | L3 | Research Question | HMGB1 기전 + 다수 동물 연구 |
| **10** | **Rheumatoid Arthritis** | **97.82%** | **L3** | **Research Question ★** | **근거 최충실, 1건 임상시험 + 20편 문헌** |

---

## 임상시험 근거(류마티스 관절염)

| 시험번호 | 단계 | 상태 | 참가자 수 | 주요 발현 |
|---------|------|------|----------|---------|
| [NCT05788705](https://clinicaltrials.gov/study/NCT05788705) | Phase NA | UNKNOWN | 75 | 천연 JAK-STAT 억제제(Boswellic acid 및 감초산 관련 성분 포함)를 RA 보충 치료로서의 효능을 평가하며, 전통적 DMARDs(Methotrexate, 생물제제) 치료와 비교 |

> ⚠️ Phase NA는 이것이 비공식 분기의 탐색적 시험임을 나타내며; UNKNOWN 상태는 자료 업데이트 결여를 나타내므로, 완료 여부를 확인할 수 없어 근거 강도는 B급 관련성으로 제한됩니다.

---

## 문헌 근거(류마티스 관절염)

| PMID | 연도 | 유형 | 저널 | 주요 발현 |
|------|-----|------|------|---------|
| [26498361](https://pubmed.ncbi.nlm.nih.gov/26498361/) | 2016 | Narrative Review | Oncotarget | 감초산(GL) 및 감초차산(GA)의 COX-2/TxA2 통로를 통한 RA의 잠재적 치료 응용에 대한 체계적 종합 |
| [40220871](https://pubmed.ncbi.nlm.nih.gov/40220871/) | 2025 | Preclinical | J Controlled Release | Sinomenine–감초산 자기조립 나노 하이드로겔이 항염증 효과를 증강하고 RA 동물 모델 증상을 개선 |
| [38037139](https://pubmed.ncbi.nlm.nih.gov/38037139/) | 2023 | Preclinical | Chinese Medicine | 감초산 병용 망고스틴이 RA 활액 신생혈관을 광범위하게 억제하고 골 침식을 완화(동물 모델) |
| [35749826](https://pubmed.ncbi.nlm.nih.gov/35749826/) | 2022 | Preclinical | Phytomedicine | 감초산 + 망고스틴이 RA 에너지 대사 이상을 역전시키고 질병 중증도 개선(동물 모델) |
| [31476301](https://pubmed.ncbi.nlm.nih.gov/31476301/) | 2019 | Preclinical | Arch Biochem Biophys | 감초소 병용 PRP가 자식 및 산화 스트레스 기전을 통해 콜라겐 유도 RA 개선(래트 모델) |
| [33593531](https://pubmed.ncbi.nlm.nih.gov/33593531/) | 2021 | Preclinical | Carbohydrate Polymers | 감초산/Budesonide 핵-껍질 나노입자의 RA에 대한 협력 항염증 및 골 보호 효과 |
| [12761187](https://pubmed.ncbi.nlm.nih.gov/12761187/) | 2003 | In vitro | J Biochemistry | 감초산과 보체 C3의 결합 특성 및 CK-2에 대한 강효 억제(체외 기전 검증) |
| [38082504](https://pubmed.ncbi.nlm.nih.gov/38082504/) | 2024 | Mechanistic | Liver International | HMGB1 매개 Ferritinophagy의 MTX 간독성 작용(감초산 HMGB1 표적의 측면 검증) |

> 나머지 12편은 감초 성분을 함유한 한약 복합제(Shaoyao-Gancao-Fuzi 등)의 조직학 연구이며, 감초산은 단독 시험 성분이 아니므로 직접 적용 가능성이 제한되어 본 표에 포함되지 않았습니다.

---

## 주목할 만한 다른 예측 적응증

### 거대세포바이러스 감염(Cytomegalovirus Infection) — L3, Research Question

감초산은 직접적인 항바이러스 기전(바이러스 입자 조립 및 방출 방해)을 가지고 있으며, NF-κB 억제를 통해 CMV가 유발한 간 염증 반응을 완화합니다. 1990년대에 일본 소아과의 소규모 임상 관찰에서 SNMC(감초산을 함유한 정맥주사 제제)는 영유아 CMV 간염에서 개선 효과를 보였습니다.

| PMID | 연도 | 유형 | 주요 발현 |
|------|-----|------|---------|
| [8073426](https://pubmed.ncbi.nlm.nih.gov/8073426/) | 1994 | 임상관찰(소아과) | SNMC 정맥주사가 CMV 관련 영유아 간기능 이상에 명확한 개선(Tohoku J Exp Med) |
| [8193264](https://pubmed.ncbi.nlm.nih.gov/8193264/) | 1993 | 임상관찰(소아과) | 경구 감초산이 CMV 관련 영유아 간기능 이상 개선, 장기 추적 포함 |
| [8283138](https://pubmed.ncbi.nlm.nih.gov/8283138/) | 1994 | In vitro | 감초산이 U-937 및 MRC-5 세포에서 HCMV 바이러스 항원 발현 억제(직접 항바이러스 확인) |
| [20416218](https://pubmed.ncbi.nlm.nih.gov/20416218/) | 2010 | 임상(복합제) | 복합제 감초산 제제의 CMV 간염 아동에 대한 D-dimer 및 vWF 응혈 지표 연구 |

---

### 폐동맥 고혈압(Pulmonary Hypertension) — L3, Research Question

가장 강한 기전 경로: 감초산이 HMGB1을 억제하여 HMGB1–RAGE–NF-κB 신호축을 차단하고 폐혈관 염증 및 혈관 리모델링을 완화합니다. 대사산물인 18β-감초차산도 고산성 폐고혈압 래트 모델 자료를 보유하고 있습니다.

| PMID | 연도 | 유형 | 주요 발현 |
|------|-----|------|---------|
| [25420924](https://pubmed.ncbi.nlm.nih.gov/25420924/) | 2014 | 동물연구 | 감초산이 HMGB1을 억제하여 MCT 유도 PAH 및 폐혈관 리모델링을 현저히 완화(래트 모델) |
| [30517029](https://pubmed.ncbi.nlm.nih.gov/30517029/) | 2019 | 기전연구 | HMGB1의 PAH 발전에서의 필수성 기전 검증(감초산 주요 표적 확인) |
| [34419454](https://pubmed.ncbi.nlm.nih.gov/34419454/) | 2021 | 동물연구 | 18β-감초차산이 고산성 폐고혈압 래트의 대사체학적 보호 효과 |
| [7613529](https://pubmed.ncbi.nlm.nih.gov/7613529/) | 1995 | 동물연구 | 감초산 음용 투여가 래트 우심방압 및 폐혈관에 미치는 영향(최초의 직접 동물 자료) |

---

### 여드름(Acne) — L4, Research Question

감초산은 NF-κB 및 IL-1β/TNF-α 억제를 통해 *C. acnes*가 유발한 피지선 염증을 완화할 수 있습니다. 1개의 중문 임상 중재 보고(mesotherapy 경로)가 있습니다.

| PMID | 연도 | 유형 | 주요 발현 |
|------|-----|------|---------|
| [37036158](https://pubmed.ncbi.nlm.nih.gov/37036158/) | 2023 | 임상중재 | 복합제 감초산 mesotherapy 주입이 중등도 여드름 치료(n=75, J Cosmetic Dermatology) |
| [40020947](https://pubmed.ncbi.nlm.nih.gov/40020947/) | 2025 | 제제개발 | 감초산 자기조립 미셀이 Cryptotanshinone 여드름 치료의 투과성 및 항염증 효과 증강 |

---

## 대만 시판 정보

현재 대만에는 Glycyrrhizic acid(감초산)의 승인된 약품 허가증이 없으며, 총 허가증 수는 0건입니다.

> 보충: 일본 시장에는 SNMC(Stronger Neo-Minophagen C, 감초산 0.2% + 글리신 + 시스테인 함유)의 정맥주사 제제가 있으며, 만성 활동성 간염의 사용으로 승인되어 있어 참고 제제 규격으로 활용할 수 있습니다.

---

## 안전성 고려사항

안전성 정보는 허가 사항을 참조하시기 바랍니다.

> ⚠️ 중요 안전 신호: 문헌에 기재된 감초산은 11β-HSD2 억제를 통해 대량 또는 장기 섭취 시 **가성 원발성 알도스테론증(Pseudoaldosteronism)**을 유발할 수 있으며, 증상은 저칼륨혈증, 고혈압, 부종 및 혈장 알도스테론 저하를 포함합니다(PMID [39284704](https://pubmed.ncbi.nlm.nih.gov/39284704/)). 개별 차이가 현저하므로 전해질 모니터링이 필요합니다.

---

## 결론 및 다음 단계

**결정: Research Question(류마티스 관절염을 우선 연구 목표로)**

**근거:**
감초산은 RA에 대해 다중이고 상호 보완적인 항염증 기전(NF-κB 억제, JAK-STAT 조절, HMGB1 길항, 파골세포 분화 억제)을 보유하고 있으며, 문헌량이 가장 많고(20편), 1개의 탐색적 임상시험이 있으며, 모든 10개의 예측 적응증 중 근거가 가장 완전합니다. 거대세포바이러스 감염 및 폐동맥 고혈압도 각각 합리적인 기전 및 동물/임상 관찰 자료를 보유하고 있어 병렬 연구 문제로 활용할 수 있습니다.

**진행에 필요한 조건:**
- TFDA 안전성 자료 보완(DG001) 및 완전한 작용 기전 자료(DG002)
- 순수 감초산(복합제 제외)의 RA에 대한 체계적 동물 약효 연구(CIA 모델)
- 가성 원발성 알도스테론증 위험의 안전 용량 범위 확인, 약물 모니터링 계획 수립
- Phase 1 임상시험 설계로 인체 안전 용량 및 PK/PD 파라미터 확인
- 수의학 질병(순위 4, 5) 및 부정적 효과 적응증(순위 2 Amenorrhea)에 대한 공식 배제, 자원 집중

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

