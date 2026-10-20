---
layout: default
title: Indomethacin
parent: 모델 예측만 (L5)
nav_order: 421
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Indomethacin: 예측 신규 적응증 소아특발성관절염 (Juvenile Idiopathic Arthritis, 예측 8위) (근거 수준 L5). 기존 적응증: 퇴행성 관절염(골관절염), 어깨관절주위염, 건(힘줄)·건초염(힘줄윤활막염), 건주위염, 상완골상과염(테니스 엘보우 등)…"
monitor_inn: "indomethacin"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "WHIM syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "brachyolmia", "myosclerosis", "juvenile idiopathic arthritis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "rheumatoid nodulosis"]
---

# Indomethacin
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

# Indomethacin: 근골격계 염증·통증에서 소아특발성관절염으로

## 한 문장 요약

Indomethacin은 비스테로이드성 소염진통제(NSAID)로, 한국에서는 퇴행성관절염, 어깨관절주위염, 건염·건초염, 근육통, 외상 후 종창·통증의 진통·소염에 사용됩니다(국내 허가 제형은 첩부제, 크림, 겔, 카타플라스마제, 캡슐).
TxGNN 모델은 상위 예측으로 희귀 골격 이형성 증후군 등을 제시했으나 이들은 근거가 전혀 없고, 문헌 근거가 있는 가장 의미 있는 예측은 **소아특발성관절염(Juvenile Idiopathic Arthritis)**(예측 순위 8위)입니다. 이 질환에는 **20편의 문헌**(대부분 오래된 종설)이 있으나 등록된 임상시험은 없습니다.

> 참고: TxGNN 점수 순위 1위(brachydactyly-syndactyly syndrome)는 문헌·임상시험 근거와 기전적 연관성이 모두 없어, 이 보고서는 근거가 존재하는 소아특발성관절염을 중심으로 평가합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 퇴행성 관절염(골관절염), 어깨관절주위염, 건(힘줄)·건초염(힘줄윤활막염), 건주위염, 상완골상과염(테니스 엘보우 등), 근육통, 외상 후 종창·동통의 진통·소염 |
| 예측 신규 적응증 | 소아특발성관절염 (Juvenile Idiopathic Arthritis, 예측 8위) |
| TxGNN 예측 점수 | 99.84% (소아특발성관절염 기준) / 1위 예측(brachydactyly-syndactyly syndrome) 99.97% |
| 근거 수준 | L3 (소아특발성관절염: 종설 및 소규모 이중맹검 시험 중심) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 10건 |
| 권장 결정 | Hold (소아특발성관절염은 후속 연구 질문으로 분류) |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, indomethacin은 비선택적 COX 억제제로 프로스타글란딘 매개 염증과 통증을 줄이며, 이것이 골관절염과 염증성 근골격계 질환에 허가된 근거입니다.

소아특발성관절염은 만성 활막염을 특징으로 하는 염증성 관절 질환이므로, 기존 적응증(관절염, 건염, 근육통의 소염·진통)과 약리학적으로 연결됩니다. 1978년 소아 만성 관절염 환자 30명 대상 이중맹검 교차시험에서 indomethacin은 안전하고 효과적인 진통·소염제로 평가되었고, 비교 약물보다 선호되었습니다.

다만 이는 새로운 재창출 발견이라기보다 증상 완화 목적의 NSAID 사용에 해당하며, 이후 다른 NSAID와 DMARD·생물학적제제로 대체되었습니다. 1993년 종설도 indomethacin이 다른 NSAID보다 효과가 더 낫지 않고 독성은 더 크다고 기술합니다.

반면 상위 예측 질환들(brachydactyly-syndactyly syndrome, colobomatous microphthalmia-rhizomelic dysplasia syndrome, acromesomelic dysplasia Hunter-Thompson type, WHIM syndrome, brachyolmia 등)은 유전성 골격 이형성 또는 면역결핍 질환으로, COX 억제의 소염 작용과 기전적 연관성을 뒷받침하는 데이터가 없습니다. 이 질환들의 높은 점수는 지식 그래프 기반 계산 예측일 뿐입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

소아특발성관절염 관련 주요 문헌입니다(총 20편 중 대표 10편).

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [362571](https://pubmed.ncbi.nlm.nih.gov/362571/) | 1978 | RCT | S Afr Med J | 소아 만성 관절염 30명 이중맹검 교차시험에서 ketoprofen과 indomethacin 모두 안전하고 효과적이었으며 indomethacin이 선호됨 |
| [1379157](https://pubmed.ncbi.nlm.nih.gov/1379157/) | 1992 | Review | Drugs | 소아 류마티스 관절염의 약물 치료 목표와 NSAID(indomethacin 포함) 사용 개관 |
| [1884567](https://pubmed.ncbi.nlm.nih.gov/1884567/) | 1991 | Review | Clin Pharmacokinet | 소아 관절염 치료 약물의 임상 약동학 |
| [8422565](https://pubmed.ncbi.nlm.nih.gov/8422565/) | 1993 | Review | Br J Rheumatol | 소아 류마티스 질환의 NSAID 사용; salicylate와 indomethacin은 효과가 더 낫지 않고 독성은 더 큼 |
| [19078081](https://pubmed.ncbi.nlm.nih.gov/19078081/) | 1996 | Review | J Clin Rheumatol | 소아 류마티스 전문의 조사에서 indomethacin 사용 비율 11% (naproxen 48%) |
| [28770976](https://pubmed.ncbi.nlm.nih.gov/28770976/) | 2017 | 체계적 문헌고찰 | Cochrane Database Syst Rev | 소아·청소년 만성 비암성 통증에 대한 NSAID |
| [4678956](https://pubmed.ncbi.nlm.nih.gov/4678956/) | 1972 | Review | JAMA | Indomethacin 개관 |
| [3659248](https://pubmed.ncbi.nlm.nih.gov/3659248/) | 1986 | 임상 연구 | Q J Med | 성인 발병 스틸병 45예의 임상·검사 소견과 치료 |
| [5632159](https://pubmed.ncbi.nlm.nih.gov/5632159/) | 1967 | 임상 보고 | Arzneimittel-Forschung | 소아 류마티스 관절염 및 스틸병에서 indomethacin 장기 치료 |
| [10870096](https://pubmed.ncbi.nlm.nih.gov/10870096/) | 1999 | 동물 연구 | Biopharm Drug Dispos | 어린 쥐에서 indomethacin과 methotrexate 병용 시 성장 억제 효과가 가산적임 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200401424 | 인타신첩부제(인도메타신) | 첩부제 | 퇴행성 관절염(골관절염), 어깨관절주위염, 건(힘줄)•건초염(힘줄윤활막염), 건주위염, 상완골(위팔뼈)상과염 (테니스엘보우 등)... |
| 201104878 | 인도메타캡슐(인도메타신) | 경질캡슐제 | 허가사항 참조 |
| 198601419 | 바이겔크림(인도메타신) | 크림제 | 퇴행성관절염(골관절염), 어깨관절주위염, 건ㆍ건초염, 건주위염, 상완골상과염(테니스 엘보우 등), 근육통, 외상후의 종창ㆍ동통의... |
| 200511327 | 단아팬에프카타플라스마(인도메타신) | 카타플라스마제 | 퇴행성관절염(골관절염), 어깨관절주위염, 건염(힘줄염)ㆍ건초염(힘줄윤활막염), 건(힘줄)주위염, 상완골(위팔뼈)상과염(테니스 엘보우 등)... |
| 201202208 | 반테린코와크리미겔 | 크림상 겔제 | 퇴행성관절염(골관절염), 어깨관절주위염, 건(힘줄)ㆍ건초염(힘줄윤활막염), 건주위염, 상완골상과염(테니스 엘보우 등), 근육통... |

## 안전성 고려사항

- **금기(지식 그래프 기반, 허가 문구 아님)**: 고혈압, 간질, 위궤양·십이지장궤양·활동성 소화성 궤양, 신장 질환, 간 질환, 혈소판감소증, 천식, 혈액응고 질환, 심근경색·관상동맥 혈전증 등 심혈관 질환, 궤양성 대장염·염증성 장질환, 괴사성 장염, 뇌내출혈, 감염성 질환 등이 금기 관계로 연결되어 있습니다. 정확한 금기는 허가사항을 확인해야 합니다.
- **약물 상호작용**: 총 252건이 확인되었습니다. 주요 중등도(Moderate) 상호작용은 다음과 같습니다.
  - 코르티코스테로이드: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide
  - 아스피린(acetylsalicylic acid)
  - 메살라진, balsalazide
  - 혈당강하제: metformin, glimepiride, chlorpropamide
  - 기타: aprepitant, 칼륨 제제(potassium citrate, potassium bicarbonate), 장 세척제(picosulfuric acid, polyethylene glycol)
  - 경미(Minor): famotidine, ranitidine, cimetidine, linaclotide
- **소아 성장 관련 참고**: 동물 연구에서 indomethacin과 methotrexate 병용 시 성장 억제가 가산적으로 나타났습니다. 소아 적용 시 고려가 필요합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 상위 예측 질환들(점수 99.8~99.97%)은 모두 희귀 유전성 질환으로 기전적 연관성과 임상 근거가 없습니다. 소아특발성관절염은 기전상 타당하고 역사적 사용 근거가 있으나, 증상 완화 수준의 오래된 문헌이 대부분이고 등록된 임상시험이 없으며 이미 다른 NSAID와 DMARD·생물학적제제로 대체되었습니다. 또한 허가사항의 경고·금기 정보가 확보되지 않아 안전성 심사를 진행할 수 없습니다.

**진행하려면 필요한 것:**
- 허가사항(첨부문서) 경고 및 금기 정보 확보 (현재 차단 수준의 데이터 공백)
- 상세한 약물 작용 기전(MOA) 데이터
- 소아특발성관절염에서 현행 표준치료 대비 indomethacin의 위치를 평가하는 최신 연구 또는 임상시험
- 국내 허가 제형이 주로 외용제이므로, 소아특발성관절염에 필요한 투여 경로(전신 투여)와의 적합성 검토
- 소아 대상 안전성(성장, 위장관, 신장, 심혈관) 평가 계획
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

