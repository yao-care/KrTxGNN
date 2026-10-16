---
layout: default
title: Betamethasone
parent: 모델 예측만 (L5)
nav_order: 143
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Betamethasone: 예측 신규 적응증 원형탈모증 (Alopecia Areata) (근거 수준 L5). 기존 적응증: 2차 감염된 알레르기성 또는 염증성 피부질환(습진, 접촉피부염, 지루피부염, 아토피피부염, 광피부염, 만성단순태선, 간찰진…"
---

# Betamethasone
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

# Betamethasone: 2차 감염된 알레르기성·염증성 피부질환에서 원형탈모증으로

## 한 문장 요약

Betamethasone은 강력한 글루코코르티코이드로, 한국에서는 2차 감염된 알레르기성 또는 염증성 피부질환과 1도 화상 치료에 허가되어 있습니다.
TxGNN 모델은 **원형탈모증(Alopecia Areata)**에 효과가 있을 수 있다고 예측하며, 현재 **6건의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다.
다만 임상시험 대부분은 betamethasone을 대조약으로 사용했거나 소규모 연구여서, 근거의 직접성에는 한계가 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 2차 감염된 알레르기성 또는 염증성 피부질환(습진, 접촉피부염, 지루피부염, 아토피피부염, 광피부염, 만성단순태선, 간찰진, 박탈피부염, 가려움, 건선), 1도 화상 |
| 예측 신규 적응증 | 원형탈모증 (Alopecia Areata) |
| TxGNN 예측 점수 | 99.97% |
| 근거 수준 | L2 (※ 아래 참고) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 |
| 권장 결정 | Proceed with Guardrails |

※ 완료된 Phase 2 시험(NCT06786689, 60명)이 1건 있어 L2로 판정했습니다. 다만 이 시험은 비교 연구이며 대규모 Phase 3 RCT는 확인되지 않았습니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 확보되지 않았습니다. 알려진 정보에 따르면 betamethasone은 강력한 글루코코르티코이드이며, 염증성·알레르기성 피부질환에서 효능이 입증되어 있어 면역 매개 모발 질환에도 적용될 수 있습니다.

원형탈모증은 모낭의 면역 특권이 무너지면서 T세포가 모낭을 공격하는 자가면역 질환입니다(IFN-γ/JAK-STAT 신호 관여). Betamethasone은 이 T세포 매개 면역 반응을 억제할 수 있어, 기존의 염증성 피부질환 적응증과 면역·염증 억제라는 공통 기전을 갖습니다. 국소 도포, 병변 내 주사, 경구 미니펄스 요법은 원형탈모증에서 이미 확립된 코르티코스테로이드 치료 방식과도 일치합니다.

그러나 근거 대부분은 betamethasone을 활성 대조약으로 쓴 연구이거나 소규모·이질적인 용법의 연구입니다. Betamethasone 자체를 주 평가 대상으로 한 대규모 Phase 3 RCT는 확인되지 않았습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT06786689](https://clinicaltrials.gov/study/NCT06786689) | Phase 2 | 완료 | 60 | 중등도~중증 원형탈모증에서 주 1회 azathioprine 펄스 vs betamethasone 경구 미니펄스 비교 |
| [NCT02350023](https://clinicaltrials.gov/study/NCT02350023) | Phase 4 | 완료 | 50 | 국소 원형탈모증에서 latanoprost vs 국소 코르티코스테로이드(betamethasone) 무작위 비교 |
| [NCT05803070](https://clinicaltrials.gov/study/NCT05803070) | 해당 없음 | 불명 | 59 | 국소 원형탈모증에서 cetirizine 1% vs betamethasone valerate 0.1% 효능·안전성 비교 |
| [NCT06087796](https://clinicaltrials.gov/study/NCT06087796) | Phase 1 | 불명 | 60 | pentoxifylline·metformin 겔 vs betamethasone valerate 0.1% 크림 비교 |
| [NCT07696585](https://clinicaltrials.gov/study/NCT07696585) | 해당 없음 | 모집 예정 | 60 | metformin 30%·simvastatin 2%·betamethasone valerate 0.1% 국소 치료(결과 없음, betamethasone 단독 효과 분리 불가) |
| [NCT04207931](https://clinicaltrials.gov/study/NCT04207931) | Phase 4 | 모집 중 | 250 | 중심원심성 흉터성 탈모증 치료 결과 비교(원형탈모증과 다른 질환으로 간접적 근거) |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | 네트워크 메타분석 | Cochrane Database Syst Rev | 면역억제제, 모발 성장 촉진제, 접촉 면역요법 등 원형탈모증 치료법 비교 |
| [39393548](https://pubmed.ncbi.nlm.nih.gov/39393548/) | 2025 | RCT | J Am Acad Dermatol | 복합 betamethasone의 마이크로니들 경피 전달(병변 내 주사의 통증 완화 목적) |
| [34400956](https://pubmed.ncbi.nlm.nih.gov/34400956/) | 2021 | RCT | Iran J Pharm Res | 중증 원형탈모증에서 경구 betamethasone 펄스, methotrexate, 병용요법의 이중맹검 위약대조 비교 |
| [40510104](https://pubmed.ncbi.nlm.nih.gov/40510104/) | 2025 | RCT | Cureus | 60명 대상 경구 cyclosporine vs betamethasone 미니펄스 비교 |
| [36257912](https://pubmed.ncbi.nlm.nih.gov/36257912/) | 2022 | RCT | Dermatol Ther | latanoprost vs minoxidil, betamethasone 및 병용요법의 이중맹검 무작위 비교 |
| [32594786](https://pubmed.ncbi.nlm.nih.gov/32594786/) | 2022 | RCT | J Dermatolog Treat | 국소 원형탈모증에서 병변 내 betamethasone vs triamcinolone의 환자 내 무작위 비교 |
| [28521549](https://pubmed.ncbi.nlm.nih.gov/28521549/) | 2018 | 비교 시험 | J Dermatolog Treat | 국소 latanoprost vs minoxidil 및 betamethasone valerate 비교 |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | 리뷰 | Dermatol Pract Concept | 원형탈모증 코르티코스테로이드 펄스 요법의 효능, 재발률, 부작용 고찰 |
| [40519428](https://pubmed.ncbi.nlm.nih.gov/40519428/) | 2025 | 임상 연구 | Cureus | 중등도~중증 원형탈모증에서 경구 betamethasone 미니펄스의 효능·안전성 평가 |
| [27746635](https://pubmed.ncbi.nlm.nih.gov/27746635/) | 2016 | 비교 연구 | Ann Dermatol | 경구 cyclosporine vs betamethasone 미니펄스 비교 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200003434 | 레스톤크림 | 크림제 | 2차 감염된 알레르기성 또는 염증성 피부질환(습진, 접촉피부염, 지루피부염, 아토피피부염, 광피부염, 만성단순태선, 간찰진(피부스침증), 박탈피부염... |
| 199601054 | 쎄실크림 | 크림제 | 2차 감염된 알레르기성 또는 염증성 피부질환(습진, 접촉피부염, 지루피부염, 아토피피부염, 광피부염, 만성단순태선, 간찰진(피부스침증), 박탈피부염... |
| 200003982 | 아몰지에이크림 | 크림제 | 2차 감염된 알레르기성 또는 염증성 피부질환(습진, 접촉피부염, 지루피부염, 아토피피부염, 광피부염, 만성단순태선, 간찰진(피부스침증), 박탈피부염... |
| 200902987 | 쎄레톤크림 | 크림제 | 2차 감염된 알레르기성 또는 염증성 피부질환(습진, 접촉피부염, 지루피부염, 아토피피부염, 광피부염, 만성단순태선, 간찰진(피부스침증), 박탈피부염... |
| 199302063 | 셀톤크림 | 크림제 | 2차 감염된 알레르기성 또는 염증성 피부질환(습진, 접촉피부염, 지루피부염, 아토피피부염, 광피부염, 만성단순태선, 간찰진(피부스침증), 박탈피부염... |

이 외에도 정제(경구제) 허가 다수가 있으나(예: 신일베타메타손정), 허가 적응증 본문은 별도 문서로만 제공되어 위 표에서는 제외했습니다. 일부 제품은 수출용입니다.

## 안전성 고려사항

- **약물 상호작용**: 총 100건의 상호작용이 조회되었으며, 이 중 주요 항목은 다음과 같습니다.
  - **Major(중대)**: Adalimumab
  - **Moderate(중등도)**: Zidovudine, Isotretinoin, Acarbose, Acebutolol, Acetazolamide, Ketorolac, Nifedipine, Ibuprofen, Ethinylestradiol, Albiglutide, Aldesleukin, Alefacept, Alemtuzumab, Fluvoxamine, Fosamprenavir 등
  - **Minor(경미)**: Formoterol, Salbutamol
- **지식그래프 기반 금기 관련 질환**(허가 문서가 아닌 모델 지식그래프 기준): 고혈압, 간질, 고혈당, 홍역, 울혈성 심부전, 단순포진 각막염, 뇌하수체 기능저하증 및 관련 성장호르몬 결핍 질환군 등. 실제 금기는 허가사항으로 확인해야 합니다.

경고 및 금기 등 허가사항 기반 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
원형탈모증에서 betamethasone의 국소·병변 내·경구 미니펄스 사용을 다룬 완료된 Phase 2 시험과 다수의 RCT·비교 연구가 있고, 코르티코스테로이드의 면역 억제 기전이 이 질환에 부합합니다. 다만 betamethasone을 주 평가 대상으로 한 대규모 Phase 3 RCT가 없고, 다수 연구가 대조약 사용이거나 소규모여서 조건부 진행이 적절합니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기) 확인 및 안전성 검토: 현재 허가 문서 기반 안전성 데이터가 없어 이 항목이 가장 시급합니다.
- 상세한 약물 작용 기전(MOA) 데이터 보강
- 투여 경로 결정(국소, 병변 내, 경구 미니펄스)과 해당 경로의 한국 허가 제형 확인
- 경구 미니펄스 장기 사용 시 부작용 및 재발률 모니터링 계획(고혈압, 고혈당 등 기저질환자 주의)
- Betamethasone 단독 효과를 평가하는 대규모 대조 시험 또는 체계적 문헌고찰

**기타 예측 적응증 참고:** 2~10순위 예측(알로페시아 뮤시노사, 휴지기 탈모, 모낭염 데칼반스, 특발성 스테로이드 감수성 신증후군 등)은 임상시험이 없고 문헌도 매우 제한적이어서(L3~L5) 현재는 보류(Hold) 수준입니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

