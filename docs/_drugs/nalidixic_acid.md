---
layout: default
title: Nalidixic Acid
parent: 중등도 근거 (L3-L4)
nav_order: 537
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-15
description: "Nalidixic Acid: 예측 신규 적응증 결막염 (Conjunctivitis) (근거 수준 L4). 기존 적응증: 허가 적응증이 문서 링크로만 제공되어 구체적인 내용을 확인할 수 없음"
monitor_inn: "NALIDIXIC ACID"
predicted_indications: ["conjunctivitis", "sclerosing cholangitis", "rheumatoid arthritis", "infectious otitis media"]
---

# Nalidixic Acid
{: .fs-9 }

근거 수준: **L4** | 예측 적응증: **4** 건
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

## Nalidixic Acid: 요로 감염에서 결막염으로
{: .text-alpha }

## 한 문장 요약

Nalidixic acid(날리딕스산)는 1세대 퀴놀론계 항균제로, 한국에서는 수출용 정제로 허가되어 있습니다. TxGNN 모델은 **결막염(conjunctivitis)**에 효과가 있을 수 있다고 예측하지만, 이 방향을 직접 지지하는 **임상시험은 0건**이며 **문헌 5편**도 모두 세균 분리·내성 연구여서 결막염 치료 효과를 뒷받침하지 못합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증이 문서 링크로만 제공되어 구체적인 내용을 확인할 수 없음 |
| 예측 신규 적응증 | 결막염 (Conjunctivitis) |
| TxGNN 예측 점수 | 99.83% |
| 근거 수준 | L4 |
| 한국 시판 현황 | ✓ 시판 중 (수출용) |
| 허가증 수 | 3건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 수집되지 않았습니다. 일반적으로 nalidixic acid는 세균의 DNA gyrase(topoisomerase II)와 topoisomerase IV를 억제하는 1세대 퀴놀론계 항균제로 알려져 있어, 감수성 그람음성균에 의한 세균성 결막염에 이론상 적용될 가능성은 있습니다.

그러나 현실적인 제약이 큽니다. 이후 개발된 불소퀴놀론계(ofloxacin, moxifloxacin 등)가 이미 안과 영역에서 더 나은 조직 투과성과 항균 범위를 제공합니다. Nalidixic acid는 내성률이 높고 조직 투과성도 낮습니다. 0.998이라는 높은 TxGNN 점수는 항균제 계열 간의 일반적 관계를 반영한 것일 가능성이 크며, 결막염에 특화된 근거를 의미하지는 않습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [17446289](https://pubmed.ncbi.nlm.nih.gov/17446289/) | 2007 | 미생물 특성 분석 | J Med Microbiol | 방글라데시 설사 환자에서 분리된 Shigella dysenteriae 신규 혈청형의 특성 분석 |
| [15824427](https://pubmed.ncbi.nlm.nih.gov/15824427/) | 2005 | 미생물 특성 분석 | J Med Microbiol | 설사 환자에서 분리된 Shigella boydii 잠정 혈청형 E16553의 분리 및 특성 분석 |
| [16914657](https://pubmed.ncbi.nlm.nih.gov/16914657/) | 2006 | 내성 감시 | J Med Microbiol | Shigella sonnei 분리주의 60% 이상이 nalidixic acid에 내성 |
| [9442487](https://pubmed.ncbi.nlm.nih.gov/9442487/) | 1997 | 플라스미드/내성 연구 | Microb Drug Resist | S. dysenteriae 1형 70-kb 플라스미드와 약제 내성·독력의 관련성 |
| [3206956](https://pubmed.ncbi.nlm.nih.gov/3206956/) | 1988 | 시험관/세균학 | Zh Mikrobiol Epidemiol Immunobiol | Yersinia 약독화 평가 기준으로서의 침습성과 세포독성 |

위 문헌은 모두 설사성 질환 관련 세균 연구이며, 결막염에 대한 nalidixic acid의 효과를 평가한 연구는 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200402887 | 나리디신정500밀리그람(날리딕스산)(수출용) | 보라색 장방형 필름코팅정제 | 허가사항 문서 참조 |
| 200501315 | 딕스정(날리딕스산)(수출용) | 보라색 장방형 필름코팅정 | 허가사항 문서 참조 |
| 200802869 | 영풍날리딕스산정500mg(수출용) | 보라색 장방형 필름코팅정제 | 허가사항 문서 참조 |

## 안전성 고려사항

- **약물 상호작용**: 데이터에서 총 100건의 상호작용이 확인되었으며, 주요(Major) 등급은 다음과 같습니다.
  - 코르티코스테로이드: hydrocortisone, triamcinolone, dexamethasone, betamethasone
  - bupropion
  - chlorpropamide
  - 그 외 acarbose, alogliptin, canagliflozin, dapagliflozin 등 당뇨병 치료제와 칼슘·구연산염 제제 등이 중등도(Moderate)로 확인됨
- **지식그래프 기반 금기 질환** (허가사항 문구가 아닌 모델 지식그래프 정보): 간질, 포르피린증, 간 질환, 담낭 질환, 건염, 말초신경병증, 중추신경계 질환, G6PD 결핍증, Clostridium difficile 대장염 등.

허가사항상의 경고 및 금기는 확보되지 않았으므로 허가사항을 직접 확인해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
결막염에 대한 임상시험이 없고, 문헌은 모두 설사성 병원체의 내성·특성 연구로 결막염과 직접 관련이 없습니다. 이미 안과 영역에서 더 우수한 불소퀴놀론계가 사용되고 있어 nalidixic acid를 결막염에 재창출할 근거와 이점이 부족합니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기·적응증) 원문 확보 (현재 안전성 검토를 진행할 수 없는 차단 수준의 데이터 공백)
- 상세한 작용 기전 데이터 확보
- 결막염 원인균에 대한 nalidixic acid의 시험관 내 감수성 및 안과 투여 시 조직 투과성 자료
- 기존 안과용 퀴놀론 대비 우월성 또는 차별성에 대한 근거
- 외용(점안) 제형 개발 가능성 검토 (현재 허가 제형은 경구 정제뿐)

**참고 — 다른 예측 적응증:** 경화성 담관염(L5), 류마티스 관절염(L5), 감염성 중이염(L4)도 예측되었으나, 모두 직접적인 임상 근거가 없어 Hold로 평가되었습니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

