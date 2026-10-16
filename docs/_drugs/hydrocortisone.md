---
layout: default
title: Hydrocortisone
parent: 모델 예측만 (L5)
nav_order: 402
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Hydrocortisone: 예측 신규 적응증 원형탈모증 (Alopecia Areata) (근거 수준 L5). 기존 적응증: 습진ㆍ피부염군, 피부가려움, 벌레물린데"
monitor_inn: "HYDROCORTISONE"
predicted_indications: ["alopecia areata", "alopecia mucinosa", "telogen effluvium", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions", "alopecia universalis onychodystrophy vitiligo", "idiopathic steroid-sensitive nephrotic syndrome"]
---

# Hydrocortisone
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

# Hydrocortisone: 습진·피부염에서 원형탈모증으로

## 한 문장 요약

Hydrocortisone은 저용량 글루코코르티코이드로, 한국에서 습진·피부염군, 피부 가려움, 벌레 물림 등에 사용되어 왔습니다.
TxGNN 모델은 **원형탈모증(Alopecia Areata)**에 효과가 있을 수 있다고 예측하며, 현재 **1건의 임상시험**과 **20편의 문헌**이 연관되어 있습니다.
다만 유일한 임상시험에서 hydrocortisone 1%는 고역가 스테로이드(clobetasol)의 대조약이었으므로, hydrocortisone 자체의 효능을 뒷받침하는 근거는 약합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 습진ㆍ피부염군, 피부가려움, 벌레물린데 |
| 예측 신규 적응증 | 원형탈모증 (Alopecia Areata) |
| TxGNN 예측 점수 | 99.97% |
| 근거 수준 | L1 (설계 기준. 단, 완료된 Phase 3 RCT가 1건뿐이고 hydrocortisone이 대조약이어서 실질 근거는 이보다 낮음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 hydrocortisone은 항염·면역억제 작용을 가진 글루코코르티코이드이며, 피부 염증성 질환에서의 사용이 허가되어 있습니다.

원형탈모증은 T세포가 모낭을 공격하는 자가면역 질환입니다. 국소 면역 활동을 억제하는 스테로이드는 기전상 적용 가능성이 있습니다. 과거 문헌에도 hydrocortisone 병변 내 주사나 국소 도포를 시도한 보고가 다수 있습니다(1950~70년대 임상 보고).

그러나 직접 비교 시험에서 hydrocortisone 1%는 강력한 스테로이드인 clobetasol보다 효과가 떨어지는 약한 대조약이었습니다. 효과가 약물 역가에 좌우되므로, hydrocortisone 자체를 원형탈모증 치료제로 보는 근거는 약합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | 완료 | 41 | 소아 원형탈모증에서 clobetasol 0.05% 크림 vs hydrocortisone 1% 크림 무작위 비교. 소규모이며 hydrocortisone은 저역가 대조약 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [24226568](https://pubmed.ncbi.nlm.nih.gov/24226568/) | 2014 | RCT | JAMA Dermatology | 소아 원형탈모증에서 clobetasol 0.05%와 hydrocortisone 1%를 비교한 무작위 임상시험 |
| [13368875](https://pubmed.ncbi.nlm.nih.gov/13368875/) | 1956 | 증례 시리즈 | Medical Times | 원형탈모증에서 cortisone, hydrocortisone 및 유사체 치료 보고 |
| [13525930](https://pubmed.ncbi.nlm.nih.gov/13525930/) | 1958 | 리뷰 | J Med Soc N J | 원형탈모증 및 흔한 두피 질환 개관 |
| [13610145](https://pubmed.ncbi.nlm.nih.gov/13610145/) | 1958 | 증례 보고 | Der Hautarzt | hydrocortisone 피내 주사 후 원형탈모증에서 모발 재성장 |
| [15692503](https://pubmed.ncbi.nlm.nih.gov/15692503/) | 2005 | 증례 보고 | J Am Acad Dermatol | 선천성 원형탈모증 4례, 장기간 증상 소강기 관찰 |
| [24326563](https://pubmed.ncbi.nlm.nih.gov/24326563/) | 2013 | 전임상(마우스) | J Investig Dermatol Symp Proc | 원형탈모증 마우스 모델에서 PTH 유사체 치료 (hydrocortisone 직접 근거 아님) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200003008 | 케어스킨로션1% | 로션제 | 습진ㆍ피부염군, 피부가려움, 벌레물린데 |
| 200300822 | 하이로손크림 | 크림제 | 습진ㆍ피부염군, 피부가려움, 벌레물린데 |
| 200102618 | 락티손에이취씨현탁액1% | 현탁액제 | 습진ㆍ피부염군, 피부가려움, 벌레물린데 |
| 202002443 | 카네스졸플러스크림 | 크림 | 염증, 가려움 및 습진 등을 수반하는 피부 진균증(백선, 피부 칸디다증, 어루러기) |
| 200402651 | 하티손로션1% | 로션제 | 습진ㆍ피부염군, 피부가려움, 벌레물린데 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 주요 항목으로 adalimumab(Major), 그 외 isotretinoin, ibuprofen, ketorolac, nifedipine, ethinylestradiol, 여러 혈당강하제(acarbose, acetohexamide, albiglutide), 생백신 및 톡소이드 계열(Moderate) 등이 있습니다.
- **지식그래프 기반 금기 질환(허가 문구가 아닌 모델 지식그래프 기준)**: 고혈압, 간질, 위궤양, 신장 질환, 간 질환, 고혈당, 단순포진 각막염, 홍역, 사마귀, 뇌하수체 기능저하 관련 질환 등.

그 밖의 경고·금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
유일한 Phase 3 RCT에서 hydrocortisone 1%는 효능이 더 높은 clobetasol의 저역가 대조약이었고 표본(n=41)도 작아, 원형탈모증에 대한 hydrocortisone의 효능을 입증하지 못합니다. 기전상 타당성은 있으나 효과가 역가에 의존하므로, 더 강한 스테로이드가 이미 대안으로 존재하는 상황에서 재창출 우선순위는 낮습니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기) 확보 및 분석
- 작용 기전(MOA) 데이터 보완
- hydrocortisone 단독 효능을 평가하는 위약 대조 시험 또는 고역가 스테로이드 대비 비열등성 근거
- 두피 적용 시 경로·제형 적합성 검토

한편 같은 방향으로 예측된 다른 질환(알로페시아 뮤시노사, 휴지기 탈모 등)은 직접 근거가 없거나 연관성이 낮아(근거 수준 L4~L5) 모두 Hold로 판단됩니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

