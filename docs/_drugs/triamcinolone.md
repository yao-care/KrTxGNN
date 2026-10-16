---
layout: default
title: Triamcinolone
parent: 모델 예측만 (L5)
nav_order: 761
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Triamcinolone: 예측 신규 적응증 원형탈모증 (Alopecia Areata) (근거 수준 L5). 기존 적응증: 미란(짓무름) 또는 궤양을 수반하는 난치성 구내염 및 설염에 의한 염증의 완화"
---

# Triamcinolone
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

# Triamcinolone: 구내염·설염에서 원형탈모증으로

## 한 문장 요약

Triamcinolone은 합성 글루코코르티코이드로, 한국에서는 미란 또는 궤양을 수반하는 난치성 구내염 및 설염의 염증 완화 등에 사용되어 왔습니다.
TxGNN 모델은 **원형탈모증(Alopecia Areata)**에 효과가 있을 수 있다고 예측하며, 현재 **18건의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다.
다만 임상시험은 대부분 소규모이며, Phase 3 시험은 포함되어 있지 않습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 미란(짓무름) 또는 궤양을 수반하는 난치성 구내염 및 설염에 의한 염증의 완화 |
| 예측 신규 적응증 | 원형탈모증 (Alopecia Areata) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L1 (아래 참고) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 |
| 권장 결정 | Proceed with Guardrails |

> **근거 수준에 대한 유의점:** 이 보고서에 정리된 시험은 Phase 2, Phase 4, 비분류(NA)뿐이며, 완료된 Phase 3 RCT는 없습니다. 위 판정 규칙을 엄격히 적용하면 L1 조건(완료된 Phase 3 RCT 2건 이상)에는 해당하지 않습니다. L1은 네트워크 메타분석과 다수의 무작위 비교연구에서 triamcinolone이 표준 치료 기준(comparator)으로 쓰인다는 점을 반영한 평가이며, 엄격한 기준으로는 L2~L3 수준으로 보는 것이 보수적입니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 없습니다. 알려진 정보에 따르면 triamcinolone은 강력한 글루코코르티코이드로, 면역 반응과 염증을 억제합니다. 한국에서는 구내염·설염 등의 염증 완화를 위한 정제, 연고, 페이스트, 주사제 등으로 허가되어 있습니다.

원형탈모증은 모낭의 면역 특권이 무너지면서 T세포(IFN-γ, CD8+ NKG2D+ T세포 침윤)가 모낭을 공격하는 자가면역 질환입니다. 구내염·설염과 원형탈모증은 모두 국소 염증 및 면역 매개 병태라는 공통점이 있어, 항염증·면역억제 작용을 가진 corticosteroid가 기전상 적용될 수 있습니다.

실제로 병변 내 triamcinolone 주사는 국소적인 반상 원형탈모증의 오래된 1차 치료로 쓰이며, 여러 비교 시험에서 활성 대조약으로 사용됩니다. 이는 TxGNN 예측의 타당성을 뒷받침합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01898806](https://clinicaltrials.gov/study/NCT01898806) | Phase 4 | 조기 종료 | 11 | 경증~중등도 반상 원형탈모증에서 병변 내 triamcinolone 3가지 용량 vs 위약. 조기 종료로 검정력 부족 |
| [NCT01797432](https://clinicaltrials.gov/study/NCT01797432) | Phase 2 | 완료 | 14 | Restylane와 triamcinolone acetonide 병용 주사의 안전성·효능 |
| [NCT03535233](https://clinicaltrials.gov/study/NCT03535233) | Phase 4 | 완료 | 40 | 5% 미녹시딜+강력 국소 스테로이드 vs 병변 내 스테로이드 직접 비교 |
| [NCT03473600](https://clinicaltrials.gov/study/NCT03473600) | Phase 4 | 불명 | 40 | 냉동요법 vs 병변 내 corticosteroid 주사 |
| [NCT00484679](https://clinicaltrials.gov/study/NCT00484679) | Phase 2 | 완료 | 18 | 병변 내 triamcinolone(Kenalog-10)이 부신 기능에 미치는 영향 |
| [NCT01246284](https://clinicaltrials.gov/study/NCT01246284) | NA | 완료 | 5 | 병변 내 triamcinolone 농도별 효능·안전성 (이중맹검, 위약 대조) |
| [NCT04147845](https://clinicaltrials.gov/study/NCT04147845) | NA | 완료 | 60 | 분획 CO2 레이저 vs 마이크로니들링을 통한 triamcinolone 또는 PRP 경표피 전달 |
| [NCT04660786](https://clinicaltrials.gov/study/NCT04660786) | Phase 1/2 | 불명 | 40 | 병변 내 비타민 D3 vs 병변 내 corticosteroid |
| [NCT05278858](https://clinicaltrials.gov/study/NCT05278858) | Phase 4 | 조기 종료 | 3 | 소아 원형탈모증에서 무바늘 주입기를 이용한 병변 내 triamcinolone 내약성 |
| [NCT06327581](https://clinicaltrials.gov/study/NCT06327581) | NA | 모집 중 | 88 | 마이크로니들링과 젖산, 비타민 D3, triamcinolone 비교 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | 네트워크 메타분석 | Cochrane Database Syst Rev | 면역억제제, 모발 성장 자극제, 접촉 면역요법 등 원형탈모증 치료법 비교 |
| [36009377](https://pubmed.ncbi.nlm.nih.gov/36009377/) | 2022 | 체계적 문헌고찰/메타분석 | Biomedicines | 반상 원형탈모증의 1차 치료인 triamcinolone 대비 PRP 효과 검토 |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | Dermatol Pract Concept | corticosteroid 펄스 요법의 효능, 재발률, 부작용 |
| [26371098](https://pubmed.ncbi.nlm.nih.gov/26371098/) | 2015 | Review | Can Fam Physician | 원형탈모증 치료 요법과 결과 개요 |
| [33749975](https://pubmed.ncbi.nlm.nih.gov/33749975/) | 2022 | RCT | J Cosmet Dermatol | 국소성 원형탈모증에서 병변 내 methotrexate vs triamcinolone |
| [40736006](https://pubmed.ncbi.nlm.nih.gov/40736006/) | 2025 | RCT | J Cosmet Dermatol | 병변 내 methotrexate가 triamcinolone의 대안이 될 수 있는지 비교 |
| [36404886](https://pubmed.ncbi.nlm.nih.gov/36404886/) | 2022 | 비교 임상연구 | Int J Trichology | triamcinolone의 병변 내 주사 vs 마이크로니들링 전달 비교 |
| [41622601](https://pubmed.ncbi.nlm.nih.gov/41622601/) | 2026 | RCT | J Cosmet Dermatol | 병변 내 triamcinolone 단독 vs 냉동요법 병용 (환자 내 비교) |
| [27448451](https://pubmed.ncbi.nlm.nih.gov/27448451/) | 2017 | 후향 연구 | J Dermatol | 난치성 원형탈모증에 대한 근육 내 triamcinolone의 구제 요법 효능과 안전성 (27명) |
| [38076656](https://pubmed.ncbi.nlm.nih.gov/38076656/) | 2023 | 비교 연구 | J Clin Aesthet Dermatol | 병변 내 pentoxifylline vs triamcinolone |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200804589 | 아프타치정 | 정제(이중정) | 미란(짓무름) 또는 궤양을 수반하는 난치성 구내염 및 설염에 의한 염증의 완화 |
| 201600837 | 마스클린페이스트 | 페이스트 | 만성 박리성 치은염, 미란 또는 궤양을 수반하는 난치성 구내염 및 설염에 의한 염증의 완화 |
| 198500023 | 오라메디연고 | 연고 | 만성 박리성 치은염, 미란 또는 궤양을 수반하는 난치성 구내염 및 설염에 의한 염증의 완화 |
| 198300006 | 트리암주 | 주사제(현탁액) | 허가 적응증 텍스트는 허가 문서 참조 |
| 200501789 | 레더코트정 | 정제 | 허가 적응증 텍스트는 허가 문서 참조 |

## 세포독성

해당 없음(항종양약이 아님)으로 판단하여 이 섹션은 생략합니다.

## 안전성 고려사항

- **약물 상호작용**: 이 보고서에 정리된 데이터에서 상호작용이 총 100건 확인되었으며, 주요 항목은 다음과 같습니다.
  - **Major**: Adalimumab
  - **Moderate**: Zidovudine, Isotretinoin, Acarbose, Acebutolol, Acetazolamide, Ketorolac, Nifedipine, Ibuprofen, Ethinylestradiol, Butalbital, Albiglutide, Aldesleukin, Alemtuzumab, Aliskiren 등
  - **Minor**: Formoterol, Salbutamol
- **알려진 위험(제공된 예측 근거 기준)**: 국소 피부 위축, 색소 감소, 반복 또는 대용량 투여 시 전신 스테로이드 부작용

경고 및 금기 등 허가사항 상세 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
병변 내 triamcinolone은 국소적 원형탈모증의 확립된 1차 치료이며, 여러 무작위 비교연구와 메타분석에서 표준 치료 기준으로 활용됩니다. 다만 triamcinolone 자체의 효능을 확인하는 대규모 Phase 3 시험은 없고, 직접 관련된 시험은 소규모 또는 조기 종료된 경우가 많습니다.

**진행하려면 필요한 것:**
- 허가사항(경고, 금기)의 확인 및 분석. 안전성 선별을 진행하기 위한 필수 항목입니다.
- 작용 기전(MOA) 데이터 보완
- 한국 허가 제형 중 병변 내 주사 가능한 주사제의 원형탈모증 적응외 사용 근거 정리
- 피부 위축 등 국소 부작용과 전신 노출에 대한 모니터링 계획
- 검정력이 충분한 무작위 대조시험 또는 근거 수준 판정의 재검토

**참고(다른 예측 적응증):** 순위 2~10위의 예측 중 일부(예: 신증후군, 감염성 모낭염 계열의 Folliculitis decalvans)는 근거가 오래된 증례 위주이거나 증례 수준에 머물러 연구 과제 단계이며, 나머지는 근거가 없거나 기전 연관성이 낮아 보류(Hold)를 권고합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

