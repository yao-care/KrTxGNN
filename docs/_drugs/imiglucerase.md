---
layout: default
title: Imiglucerase
parent: 중등도 근거 (L3-L4)
nav_order: 389
evidence_level: L4
indication_count: 10
---

# Imiglucerase
{: .fs-9 }

근거 수준: **L4** | 예측 적응증: **10** 건
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

# Imiglucerase: 고셰병에서 헐러 증후군으로

## 한 문장 요약

Imiglucerase(DB00053)는 재조합 glucocerebrosidase 제제로, 원래 **고셰병(Gaucher disease)** 치료에 사용되는 효소대체요법제입니다.
TxGNN 모델은 **헐러 증후군(Hurler syndrome)**에 효과가 있을 수 있다고 예측(점수 99.52%)했으나, 이를 뒷받침하는 임상시험은 없고 헐러 증후군을 직접 다루지 않는 개괄적 리뷰 문헌 2편만 존재합니다. 평가 결과 이 예측은 기전적 근거가 약해 **보류(Hold)**를 권장합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 고셰병 (Gaucher disease) — 한국 허가 정보 없음 |
| 예측 신규 적응증 | 헐러 증후군 (Hurler syndrome, MPS I형) |
| TxGNN 예측 점수 | 99.52% |
| 근거 수준 | L4 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 확보되지 않았습니다. 다만 근거 자료 내 다른 항목들의 기전 분석에 따르면, imiglucerase는 재조합 인간 glucocerebrosidase로서 GBA 유전자 결함으로 인한 glucocerebroside 축적(고셰병)을 표적으로 하는 효소대체요법제입니다.

헐러 증후군은 MPS I형으로, 원인 유전자는 IDUA(α-L-iduronidase 결핍)이며 imiglucerase가 보충하는 glucocerebrosidase와는 완전히 별개의 효소/기질 체계입니다. 실제 MPS I(헐러 증후군)의 승인된 효소대체요법제는 laronidase이며, imiglucerase가 아닙니다.

따라서 이 예측은 TxGNN 지식그래프 내에서 "리소좀 축적질환(lysosomal storage disease)"이라는 상위 범주의 근접성 때문에 발생한 결과일 가능성이 높고, 실질적인 기전적 연관성은 확인되지 않습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [20534487](https://pubmed.ncbi.nlm.nih.gov/20534487/) | 2010 | Review | PNAS | PET 영상을 이용한 ERT 평가 개괄 리뷰. 고셰병·파브리병·헐러 증후군 등 여러 리소좀 축적질환을 함께 언급하나, 헐러 증후군에 대한 imiglucerase 특이적 효능 자료는 아님 |
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Review | La Revue de médecine interne | 리소좀 축적질환 전반의 효소대체요법 개괄 리뷰. imiglucerase는 고셰병 맥락에서만 언급됨 |

## 한국 시판 정보

한국 내 허가 정보가 없습니다 (미시판, 허가증 0건).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (한국 라벨 경고·금기·상호작용 데이터 미확보 — TFDA/식약처 원문 확인 필요)

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 헐러 증후군은 imiglucerase의 표적 효소(glucocerebrosidase) 경로와 무관한 별개 질환(IDUA 결핍)으로, 기전적 타당성이 낮습니다.
- 이를 뒷받침하는 임상시험이 전무하고, 문헌 2편도 헐러 증후군 특이적 효능 자료가 아닙니다.
- 참고로 이번 평가 대상 10개 예측 후보 중 실제 견고한 근거(L1, 완료된 Phase 3/4 시험 다수)를 가진 항목은 "lysosomal storage disease with skeletal involvement"인데, 이는 imiglucerase의 **기존 승인 적응증인 고셰병 자체**를 가리키는 것으로 판단되며 새로운 재창출 후보가 아닙니다.

**진행하려면 필요한 것:**
- 헐러 증후군에 대한 imiglucerase 관련 전임상/기전 데이터 확보
- 작용 기전(MOA) 상세 데이터 (DrugBank API 조회 필요, DG002)
- 안전성 정보 확보를 위한 허가사항(라벨) 원문 확인 (DG001, Blocking)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

