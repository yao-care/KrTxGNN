---
layout: default
title: Prednisolone
parent: 모델 예측만 (L5)
nav_order: 624
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Prednisolone: 예측 신규 적응증 원형탈모증 (Alopecia Areata) (근거 수준 L5). 기존 적응증: 염증성 피부질환, 지루성 피부염"
monitor_inn: "Prednisolone"
predicted_indications: ["alopecia areata", "alopecia mucinosa", "telogen effluvium", "Quinquaud's folliculitis decalvans", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia antibody deficiency", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions", "prolapse of lacrimal gland", "idiopathic steroid-sensitive nephrotic syndrome"]
---

# Prednisolone
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

# Prednisolone: 염증성 피부질환에서 원형탈모증으로

## 한 문장 요약

Prednisolone은 글루코코르티코이드 계열 약물로, 한국에서 염증성 피부질환 등에 사용되도록 허가되어 있습니다.
TxGNN 모델은 **원형탈모증(Alopecia Areata)**에 효과가 있을 수 있다고 예측하며, 이 방향을 지지하는 **문헌 20편**이 확인되었습니다. 다만 등록된 임상시험은 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 염증성 피부질환, 지루성 피부염 |
| 예측 신규 적응증 | 원형탈모증 (Alopecia Areata) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L2 (잠정) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 9건 |
| 권장 결정 | Proceed with Guardrails |

> 참고: 근거 수준 L2는 잠정적입니다. 가장 강력한 문헌(PMID 15692475, 위약 대조 경구 pulse prednisolone 시험)의 시험 단계, 규모, 결과를 직접 확인하지 못했습니다. 또한 이 보고서의 판정 규칙(완료된 Phase 2/3 RCT 1건)을 엄격히 적용하면 등록된 임상시험이 없어 더 낮은 수준이 될 수 있습니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Prednisolone은 광범위한 항염 및 면역억제 작용을 가진 글루코코르티코이드이며, 염증성 피부질환에서의 사용이 허가되어 있어 기전상 원형탈모증에도 적용 가능할 수 있습니다.

원형탈모증은 T세포가 매개하는 자가면역 질환으로, 모낭의 면역 특권이 붕괴되어 발생합니다. Prednisolone은 T세포 활성화와 염증성 사이토카인을 억제하므로 이 병리 기전을 직접 겨냥합니다. 문헌에서도 경구 pulse 스테로이드가 TNF-α 수치를 변화시켜 작용할 가능성이 제시되었습니다(PMID 30294905).

다만 전신 스테로이드는 중단 후 재발이 흔하고 누적 부작용이 있으므로, 중증이거나 빠르게 진행하는 경우에 pulse 또는 단기 요법으로 제한하고 모니터링하는 것이 바람직합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [15692475](https://pubmed.ncbi.nlm.nih.gov/15692475/) | 2005 | RCT | J Am Acad Dermatol | 원형탈모증에서 위약 대조 경구 pulse prednisolone 요법 (초록상 기존 연구에 무작위·위약 대조 시험이 없었다고 언급) |
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | 네트워크 메타분석 | Cochrane Database Syst Rev | 면역억제제 등 원형탈모증 치료법 비교 |
| [30191561](https://pubmed.ncbi.nlm.nih.gov/30191561/) | 2019 | 체계적 문헌고찰 | Australas J Dermatol | 원형탈모증 전신 치료의 근거 수준이 제각각임을 평가 |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | Dermatol Pract Concept | 코르티코스teroid pulse 요법의 효능, 재발률, 부작용 |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Review | Pediatr Dermatol | 소아 원형탈모증의 pulse 스테로이드 용량과 투여 방식 |
| [21572877](https://pubmed.ncbi.nlm.nih.gov/21572877/) | 2009 | 코호트/임상연구 | Dermato-endocrinology | 중등도 용량 prednisolone pulse 요법; 초기 효과가 있으나 부작용으로 중단 사례 발생 |
| [28140540](https://pubmed.ncbi.nlm.nih.gov/28140540/) | 2017 | 코호트/증례 시리즈 | J Dtsch Dermatol Ges | 중증 소아 원형탈모증에서 고용량 후 저용량 순차 요법 |
| [26179196](https://pubmed.ncbi.nlm.nih.gov/26179196/) | 2015 | 장기 추적 연구 | Dermatol Ther | 소아 65명에서 경구 pulse와 국소 스테로이드 병용 요법 |
| [32779249](https://pubmed.ncbi.nlm.nih.gov/32779249/) | 2020 | 후향 연구 | J Eur Acad Dermatol Venereol | 만성 원형탈모증 138명에서 스테로이드 절감제의 지속률 |
| [41243342](https://pubmed.ncbi.nlm.nih.gov/41243342/) | 2025 | 증례 및 고찰 | J Dermatolog Treat | JAK 억제제를 쓸 수 없을 때 dexamethasone 경구 mini-pulse로 지속적 관해 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199602982 | 소론도정(프레드니솔론) | 정제 | 허가 문서 참조 |
| 200202872 | 피알디현탁시럽0.1%(프레드니솔론) | 시럽제 | 허가 문서 참조 |
| 202100035 | 덴탈필크림 | 크림제 | 허가 문서 참조 |
| 200200773 | 캄비손소프트크림 | 크림제 | 염증성 피부질환, 지루성 피부염에 사용합니다. |
| 200901008 | 태극프레드니솔론정5밀리그램(수출용) | 정제 | 허가 문서 참조 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건의 상호작용이 확인되었으며, 이 중 주요 항목은 다음과 같습니다.
  - **Major**: Adalimumab
  - **Moderate**: Zidovudine, Isotretinoin, Acarbose, Acetazolamide, Ketorolac, Ibuprofen, Nifedipine, Ethinylestradiol, Aldesleukin, Alemtuzumab 등
  - **Minor**: Formoterol, Salbutamol
- **지식 그래프상 금기 질환** (허가 문서가 아닌 모델 지식 그래프 기반): 고혈압, 간질, 고혈당, 울혈성 심부전, 헤르페스 각막염, 홍역, 포르피린증, 뇌하수체 기능저하증 등

그 밖의 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
원형탈모증에서 prednisolone의 기전적 타당성이 높고 위약 대조 RCT를 포함한 문헌이 있으나, 등록된 임상시험이 없고 핵심 RCT의 내용을 직접 검증하지 못했습니다. 재발과 전신 부작용 위험도 있어 조건부 진행이 적절합니다.

**진행하려면 필요한 것:**
- PMID 15692475 RCT의 설계, 규모, 결과 확인을 통한 근거 수준 확정
- 허가증 원문(MFDS)에서 경고, 금기, 적응증 정보 확보
- 상세한 작용 기전(MOA) 데이터 확보
- 중증 또는 급속 진행 환자로 제한한 pulse/단기 요법 프로토콜 및 부작용(감염, 고혈압, 혈당, 골 영향) 모니터링 계획
- 재발 관리 방안(스테로이드 절감제 등)

## 참고: 다른 예측 적응증

| 순위 | 예측 질환 | 근거 수준 | 권장 결정 | 비고 |
|------|---------|---------|---------|------|
| 2 | 알로페시아 뮤시노사 (모낭 점액증) | L4 | Hold | prednisolone이 아닌 cyclosporine 증례만 있음 |
| 3 | 휴지기 탈모 | L5 | Hold | 비염증성, 자연 회복성 질환으로 면역억제 근거 부족 |
| 4 | 탈모성 모낭염 (Quinquaud) | L4 | Hold | 병합요법 보고만 있어 prednisolone 단독 효과 불명 |
| 10 | 특발성 스테로이드 감수성 신증후군 | L1 | Proceed with Guardrails | 이미 표준 치료인 적응증으로, 대부분의 검색 문헌은 스테로이드 저항성 질환 대상 |

그 외 순위 5~9의 예측 질환은 근거가 없어 Hold로 판단되었습니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

