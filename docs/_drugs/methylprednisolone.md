---
layout: default
title: Methylprednisolone
parent: 중등도 근거 (L3-L4)
nav_order: 475
evidence_level: L3
indication_count: 10
---

# Methylprednisolone
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

# Methylprednisolone: 전신 코르티코스테로이드 치료에서 원형탈모증으로

## 한 문장 요약

Methylprednisolone은 강력한 전신 글루코코르티코이드로, 다양한 염증성·자가면역 질환에 광범위하게 사용되어 온 약물입니다(허가상 기존 적응증 상세 정보는 확보되지 않음).
TxGNN 모델은 **원형탈모증(Alopecia Areata)**에 효과가 있을 것으로 예측하며, 현재 **1건의 Phase 4 임상시험**과 **20편의 문헌**(코호트 연구·체계적 문헌고찰 다수 포함)이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (허가 정보 미확보 — 전신 글루코코르티코이드로서 염증성/자가면역질환 전반에 사용) |
| 예측 신규 적응증 | 원형탈모증 (Alopecia Areata) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L3 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터(DrugBank MOA)는 확보되지 않았습니다. 다만 methylprednisolone은 잘 알려진 합성 글루코코르티코이드로, T세포 활성화 억제 및 국소 염증 반응 차단을 통해 항염·면역억제 효과를 나타냅니다.

원형탈모증은 T세포가 매개하는 자가면역 반응이 모낭을 공격하여 발생하는 질환입니다. Methylprednisolone의 면역억제 기전은 이 병태생리와 직접적으로 맞닿아 있으며, 실제로 고용량 mega-pulse methylprednisolone 요법은 이미 피부과 임상 실무에서 중증·난치성 원형탈모증 치료 옵션으로 사용되고 있어 TxGNN 예측의 기전적 타당성을 뒷받침합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01167946](https://clinicaltrials.gov/study/NCT01167946) | Phase 4 | 완료 | 42 | 중증 난치성 원형탈모증 환자에서 고용량 경구 mega-pulse methylprednisolone의 안전성·유효성 평가 |
| [NCT01017510](https://clinicaltrials.gov/study/NCT01017510) | N/A | 불명 | 20 | 원형탈모증 병변 내 스테로이드 주입 시 DERMOJET(무침) vs 일반 주사기 투여법 비교 |

검색된 나머지 16건은 주로 baricitinib·sirolimus 등 다른 약물의 전신홍반루푸스(SLE) 시험으로, methylprednisolone 및 원형탈모증과 직접 관련성이 낮아 제외했습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [35986630](https://pubmed.ncbi.nlm.nih.gov/35986630/) | 2022 | Retrospective | Dermatologic Therapy | 광범위 원형탈모증에서 methylprednisolone 단독 vs MTX 병용요법 후향적 비교 |
| [32270396](https://pubmed.ncbi.nlm.nih.gov/32270396/) | 2020 | Systematic Review | Dermatology and Therapy | Cyclosporine ± 전신 코르티코스테로이드 병용요법 체계적 문헌고찰 |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | Dermatology Practical & Conceptual | 원형탈모증에서 코르티코스테로이드 pulse therapy의 유효성 및 이상반응 종설 |
| [25566921](https://pubmed.ncbi.nlm.nih.gov/25566921/) | 2015 | Cohort/Case series | Indian J Dermatol Venereol Leprol | 중증 원형탈모증에서 정맥 methylprednisolone pulse therapy |
| [18608727](https://pubmed.ncbi.nlm.nih.gov/18608727/) | 2008 | Cohort | J Dermatolog Treat | Cyclosporine + methylprednisolone 병용요법의 중증 원형탈모증 치료 효과 |
| [36865845](https://pubmed.ncbi.nlm.nih.gov/36865845/) | 2022 | Retrospective | Indian J Dermatol | Steroid pulse therapy 반응의 성별 차이 후향적 연구 |
| [28378336](https://pubmed.ncbi.nlm.nih.gov/28378336/) | 2017 | Review | Int J Dermatology | 전두형·전신형 원형탈모증 치료법 종설 |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Cohort (소아) | Pediatric Dermatology | 소아 원형탈모증에서 pulse dose corticosteroid 용법·용량 문헌고찰 |
| [30745958](https://pubmed.ncbi.nlm.nih.gov/30745958/) | 2019 | Cohort | Open Access Maced J Med Sci | 중증 원형탈모증에서 methotrexate + mini-pulse methylprednisolone 병용 효과 |
| [22426909](https://pubmed.ncbi.nlm.nih.gov/22426909/) | 2012 | Cohort | Saudi Med J | 중증 난치성 원형탈모증에서 경구 mega-pulse methylprednisolone의 안전성·유효성 |

(위 10편 외 10편의 추가 문헌이 존재하며 대부분 유사한 pulse therapy 코호트/증례 연구입니다.)

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
다수의 후향적 코호트 연구와 종설(20편)이 methylprednisolone pulse therapy의 중등도~중증 원형탈모증 치료 효과를 일관되게 지지하며, 이미 피부과 임상 실무에서 활용되고 있는 치료법입니다. 다만 Phase 3 RCT가 없어 근거 수준은 L3(관찰 연구/문헌고찰 수준)에 머뭅니다.

**진행하려면 필요한 것:**
- TFDA(현지 규제기관) 공식 라벨의 경고·금기사항 확보 — 현재 Blocking 등급 데이터 갭으로 안전성 초기 평가(S1) 진행 불가
- DrugBank 등에서 상세 작용기전(MOA) 데이터 확보
- 한국 내 허가·수입 경로 확인 (현재 시판 허가 0건)
- 원형탈모증 적응증에 특화된 전향적 RCT 설계 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

