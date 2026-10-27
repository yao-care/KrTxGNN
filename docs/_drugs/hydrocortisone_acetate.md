---
layout: default
title: Hydrocortisone Acetate
parent: 모델 예측만 (L5)
nav_order: 403
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Hydrocortisone Acetate: 예측 신규 적응증 원형탈모증 (Alopecia Areata) (근거 수준 L5). 기존 적응증: 습진, 땀띠, 피부 가려움, 알레르기 피부질환, 화상, 동상"
monitor_inn: "HYDROCORTISONE ACETATE"
predicted_indications: ["alopecia areata", "telogen effluvium", "alopecia mucinosa", "Quinquaud's folliculitis decalvans", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia antibody deficiency", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions", "seborrheic keratosis"]
---

# Hydrocortisone Acetate
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

## Hydrocortisone Acetate: 습진·피부 염증에서 원형탈모증으로
{: .text-alpha }

## 한 문장 요약

Hydrocortisone acetate는 글루코코르티코이드 계열의 약물로, 한국에서는 습진, 땀띠, 피부 가려움, 알레르기 피부질환, 화상, 동상 치료에 사용되어 왔습니다.
TxGNN 모델은 **원형탈모증(Alopecia Areata)**에 효과가 있을 수 있다고 예측하며, 현재 **1건의 임상시험**과 **2편의 문헌**이 관련되어 있습니다. 다만 임상시험에서 hydrocortisone은 저역가 대조약으로 쓰였기 때문에 효능을 직접 입증한 근거는 아닙니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 습진, 땀띠, 피부 가려움, 알레르기 피부질환, 화상, 동상 |
| 예측 신규 적응증 | 원형탈모증 (Alopecia Areata) |
| TxGNN 예측 점수 | 99.94% |
| 근거 수준 | L1 (설계상 Phase 3 RCT 1건이나, 효능 입증은 아님. 아래 설명 참조) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 7건 |
| 권장 결정 | Hold |

> **근거 수준 관련 참고:** 완료된 Phase 3 RCT가 1건 있으나 L1 기준(≥2건)에는 못 미치며, 이 시험은 hydrocortisone을 시험 대상이 아닌 비교 대조약으로 사용했습니다. 따라서 실질적인 근거 수준은 L1보다 낮게 보는 것이 타당하며, 데이터 파일상의 L1 표기는 시험 설계만 반영한 것입니다.

## 이 예측이 타당한 이유는?

현재 이 보고서를 위해 수집된 데이터에는 상세한 작용 기전 정보가 없습니다. 알려진 정보에 따르면 hydrocortisone은 항염증 및 면역억제 작용을 가진 글루코코르티코이드이며, 한국에서는 외용 연고·크림 단일제로 허가되어 있습니다.

원형탈모증은 모낭의 면역 특권이 무너지면서 T세포가 매개하는 자가면역 반응이 일어나는 질환입니다. 따라서 국소 염증을 억제하는 스테로이드는 기전상 적용 가능성이 있으며, 외용 및 병변 내 주사 코르티코스테로이드는 이 질환에서 확립된 치료 계열입니다.

그러나 hydrocortisone은 저역가 스테로이드로, clobetasol 같은 고역가 제제보다 효과가 떨어지는 것으로 일반적으로 간주됩니다. 즉 기전의 타당성은 있으나 실제 효능은 제한적일 가능성이 높습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | 완료 | 41 | 소아 원형탈모증에서 clobetasol propionate 0.05% 크림과 hydrocortisone 1% 크림을 비교한 무작위 대조시험. hydrocortisone은 저역가 대조약이며, 제공된 자료만으로는 효능 결론을 확인할 수 없음 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [4755919](https://pubmed.ncbi.nlm.nih.gov/4755919/) | 1973 | 증례 보고 | Przeglad dermatologiczny | 중증 원형탈모증에서 hydrocortisone acetate 현탁액의 병변 내 피하 주사 치료 (초록 없음) |
| [153470](https://pubmed.ncbi.nlm.nih.gov/153470/) | 1979 | Review | MMW, Munchener medizinische Wochenschrift | 피부질환 국소 치료 전반의 진보를 다룬 리뷰. 원형탈모증에 대한 직접적 근거는 제한적 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200401051 | 이보드람연고 | 연고 | 습진, 땀띠, 피부 가려움, 알레르기 피부질환, 화상, 동상 |
| 200500434 | 더마큐연고 | 연고 | 습진, 땀띠, 피부 가려움, 알레르기 피부질환, 화상, 동상 |
| 200100584 | 쎄레마일드연고 | 연고 | 습진, 땀띠, 피부 가려움, 알레르기 피부질환, 화상, 동상 |
| 200600468 | 세린드연고 | 연고 | 습진, 땀띠, 피부 가려움, 알레르기 피부질환, 화상, 동상 |
| 201602246 | 클리마일드연고 | 연고 | 습진, 땀띠, 피부 가려움, 알레르기 피부질환, 화상, 동상 |

이 외에 수출용 크림 제품(서울히드로코르티손아세테이트크림1%)과 더마스킨연고 등 총 7건의 허가가 유효합니다.

## 안전성 고려사항

- **금기 질환 (지식그래프 기반 참고 정보, 허가사항 아님)**: 고혈압, 간질, 위궤양, 신장질환, 간질환, 담낭질환, 고혈당, 홍역, 단순포진 각막염, 뇌하수체 기능저하증 및 관련 성장호르몬 결핍 질환 등이 지식그래프상 금기로 연결되어 있습니다. 이는 주로 전신 투여 코르티코스테로이드의 특성을 반영한 것일 수 있으므로, 외용제에 그대로 적용되는지는 허가사항으로 확인해야 합니다.

경고, 금기, 약물 상호작용에 대한 허가사항 기반 정보는 확인되지 않았으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
원형탈모증에 대한 유일한 Phase 3 시험은 hydrocortisone을 저역가 대조약으로 사용했고 효능을 입증하지 못했습니다. 기전상 가능성은 있으나 고역가 스테로이드보다 효과가 낮을 것으로 예상되어, 현재 근거만으로는 진행하기 어렵습니다. 또한 허가사항의 경고·금기 정보를 확인하지 못해 안전성 검토를 시작할 수 없습니다.

**진행하려면 필요한 것:**
- 허가사항(첨부문서)의 경고 및 금기 정보 확보
- 상세한 작용 기전(MOA) 데이터 확보
- NCT01453686의 결과 데이터를 확인하여 hydrocortisone 군의 실제 반응률 파악
- 원형탈모증에서 hydrocortisone 단독 효능을 평가한 추가 임상 근거 (또는 고역가 스테로이드와의 비교 근거)
- 두피 적용 시 외용제 제형·투여 경로 적합성 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

