---
layout: default
title: Triamcinolone
parent: 僅模型預測 (L5)
nav_order: 701
evidence_level: L5
indication_count: 10
---

# Triamcinolone
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

# Triamcinolone: 염증성 질환에서 원형탈모증(Alopecia Areata)으로

## 한 문장 요약

Triamcinolone은 합성 당질부신피질호르몬(corticosteroid) 계열 약물로, 강력한 항염증·면역억제 작용을 통해 다양한 염증성·알레르기성 질환에 사용되어 온 약물입니다.
TxGNN 모델은 **원형탈모증(Alopecia Areata)**에 효과가 있을 수 있다고 예측하며,
현재 **23건의 임상시험**과 **20편의 문헌**이 이 방향을 뒷받침합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 코르티코스테로이드 계열 – 염증성/알레르기성 질환 (한국 허가 정보 없음) |
| 예측 신규 적응증 | 원형탈모증 (Alopecia Areata) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L1 |
| 한국 시판 현황 | 미판매 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 Evidence Pack에는 등록되어 있지 않습니다(Data Gap). 다만 Triamcinolone은 코르티코스테로이드 계열 약물로, 일반적으로 강력한 항염증·면역억제 효과를 통해 다양한 염증성 질환에 사용됩니다.

원형탈모증(AA)은 모낭 주변의 CD8+ T세포 침윤과 국소 염증반응으로 모낭의 면역 특권(immune privilege)이 붕괴되면서 발생하는 자가면역질환입니다. Triamcinolone은 이러한 염증반응과 T세포 침윤을 억제함으로써 모낭의 면역 특권을 회복시킬 수 있는 것으로 추정됩니다.

실제로 병변내 트리암시놀론 주사(Intralesional Triamcinolone, IL-TAC)는 이미 국제 피부과 진료지침에서 국소형 원형탈모증의 1차 표준치료로 자리잡고 있어, TxGNN 예측이 이론적 추정을 넘어 실제 임상 관행과 일치한다는 점을 뒷받침합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01898806](https://clinicaltrials.gov/study/NCT01898806) | Phase 4 | 종료 | 11 | 병변내 트리암시놀론 3가지 농도 대 위약 비교 다기관 RCT; 조기종료되었으나 핵심 직접 증거 |
| [NCT03473600](https://clinicaltrials.gov/study/NCT03473600) | Phase 4 | 불명 | 40 | 냉동요법 대 병변내 코르티코스테로이드(트리암시놀론) 주사 비교, 모발경 평가 |
| [NCT02467101](https://clinicaltrials.gov/study/NCT02467101) | NA | 불명 | 10 | 이마섬유화탈모증에서 병변내 코르티코스테로이드 이중맹검 위약대조 연구 |
| [NCT00484679](https://clinicaltrials.gov/study/NCT00484679) | Phase 2 | 완료 | 18 | 병변내 트리암시놀론(Kenalog-10)이 부신 기능에 미치는 영향 평가 |
| [NCT01246284](https://clinicaltrials.gov/study/NCT01246284) | NA | 완료 | 5 | 병변내 트리암시놀론 농도별 효능·안전성 이중맹검 위약대조 RCT |
| [NCT01797432](https://clinicaltrials.gov/study/NCT01797432) | Phase 2 | 완료 | 14 | Restylane 병용 병변내 트리암시놀론 주사의 효능/안전성(위축 부작용 감소 목적) |
| [NCT03535233](https://clinicaltrials.gov/study/NCT03535233) | Phase 4 | 완료 | 40 | 국소 미녹시딜+강력 국소스테로이드 대 병변내 트리암시놀론 주사 비교 RCT |
| [NCT04147845](https://clinicaltrials.gov/study/NCT04147845) | NA | 완료 | 60 | 프랙셔널 CO2 레이저 대 마이크로니들링을 이용한 트리암시놀론 경피 전달 비교 |
| [NCT06564805](https://clinicaltrials.gov/study/NCT06564805) | NA | 모집중 | 30 | 병변내 트리암시놀론(표준 1차 치료) 대 Candida albicans 항원 주사 비교 |
| [NCT05278858](https://clinicaltrials.gov/study/NCT05278858) | Phase 4 | 종료 | 3 | 소아 원형탈모증에서 니들프리 방식 병변내 트리암시놀론 전달 내약성 파일럿 연구 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | Network Meta-analysis | Cochrane Database Syst Rev | 원형탈모증 치료법(면역억제제·발모촉진제·접촉면역요법 등)에 대한 네트워크 메타분석 |
| [31843657](https://pubmed.ncbi.nlm.nih.gov/31843657/) | 2020 | RCT | J Am Acad Dermatol | 병변내 트리암시놀론 농도별 효능에 대한 체계적 문헌고찰 및 메타분석 |
| [36404886](https://pubmed.ncbi.nlm.nih.gov/36404886/) | 2022 | RCT | Int J Trichology | 병변내 주사 대 마이크로니들링을 통한 트리암시놀론 투여 효능 비교 |
| [39139085](https://pubmed.ncbi.nlm.nih.gov/39139085/) | 2024 | RCT | J Cosmet Laser Ther | 병변내 비타민 D3 대 병변내 트리암시놀론의 임상·피부경 비교 연구 |
| [24484438](https://pubmed.ncbi.nlm.nih.gov/24484438/) | 2014 | RCT/Cohort | Br J Dermatol | 병변내 트리암시놀론과 국소치료 효능 비교 비판적 평가(CAT) |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | Dermatol Pract Concept | 원형탈모증에서 코르티코스테로이드 펄스요법의 효능·부작용 리뷰 |
| [27448451](https://pubmed.ncbi.nlm.nih.gov/27448451/) | 2017 | Case series/Review | J Dermatol | 난치성 원형탈모증에서 근육내 트리암시놀론 구제요법의 가치 |
| [24761107](https://pubmed.ncbi.nlm.nih.gov/24761107/) | 2014 | Case report | J Cutan Aesthet Surg | 마이크로니들링과 트리암시놀론 병용으로 원형탈모증 치료 성공 사례 |
| [38634160](https://pubmed.ncbi.nlm.nih.gov/38634160/) | 2024 | 후향적 연구 | Skin Res Technol | 마이크로니들 미녹시딜+트리암시놀론 병용요법의 원형탈모증 치료 효과 |
| [33749975](https://pubmed.ncbi.nlm.nih.gov/33749975/) | 2022 | RCT | J Cosmet Dermatol | 국소 원형탈모증에서 병변내 메토트렉세이트 대 트리암시놀론 비교 RCT |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
병변내 트리암시놀론 주사(IL-TAC)는 이미 원형탈모증의 국제 표준 1차 치료로 널리 사용되고 있으며, RCT·네트워크 메타분석 등 다수의 문헌이 이를 뒷받침합니다(근거 수준 L1). 다만 한국 내 허가·시판 정보와 상세 MOA·안전성 데이터가 확보되지 않아 즉시 Go 결정을 내리기에는 보완이 필요합니다.

**진행하려면 필요한 것:**
- 한국 식약처(MFDS) 허가사항 및 경고·금기 정보 확보 (DG001, Blocking)
- DrugBank 등을 통한 상세 작용 기전(MOA) 데이터 확보 (DG002, High)
- 한국 내 시판 여부 및 병변내 주사 적응증 승인 현황 확인
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

