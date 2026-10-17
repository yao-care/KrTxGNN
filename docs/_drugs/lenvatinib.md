---
layout: default
title: Lenvatinib
parent: 모델 예측만 (L5)
nav_order: 468
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Lenvatinib: 예측 신규 적응증 지방육종 (Liposarcoma) (근거 수준 L5). 기존 적응증: 허가증 문서 링크만 확인되고 본문 텍스트는 확보되지 않았습니다"
monitor_inn: "Lenvatinib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "angiolipoma", "familial spontaneous pneumothorax", "endocrine-cerebro-osteodysplasia syndrome"]
---

# Lenvatinib
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

# Lenvatinib: 다중 키나제 억제 항암제에서 지방육종으로

## 한 문장 요약

Lenvatinib은 VEGFR, FGFR 등을 억제하는 다중 키나제 억제제로, 한국에서 렌비마캡슐로 시판되고 있습니다.
TxGNN 모델은 **지방육종(Liposarcoma)**에 효과가 있을 수 있다고 예측하며, 현재 **1건의 임상시험**과 **4편의 문헌**이 이 방향을 지지합니다. 다만 직접 근거는 단일군 Phase Ib/II 시험 1건뿐입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증 문서 링크만 확인되고 본문 텍스트는 확보되지 않았습니다 |
| 예측 신규 적응증 | 지방육종 (Liposarcoma) |
| TxGNN 예측 점수 | 99.51% |
| 근거 수준 | L2 (단일군 Phase Ib/II 1건 기준이며 무작위 대조시험은 아님) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

Lenvatinib은 VEGFR1-3, FGFR1-4, PDGFRα, RET, KIT를 억제하는 다중 키나제 억제제입니다. 종양 혈관신생과 FGFR/PDGFR 신호를 차단해 육종에서도 항종양 효과를 낼 가능성이 있습니다. 다만 상세한 작용 기전 항목은 현재 수집된 데이터에 없어, 위 내용은 예측 근거 설명에 기재된 기전 정보에 따른 것입니다.

지방육종 치료에서는 미세소관 억제제인 eribulin과의 병용이 보완적 기전을 가질 것으로 설명됩니다. 또한 분화형·탈분화형 지방육종에서 증폭되는 CDK4에 관한 전임상 연구도 추가 병용 가능성을 시사합니다. 그러나 lenvatinib 자체와의 직접 연결은 간접적이므로 해석에 주의가 필요합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03526679](https://clinicaltrials.gov/study/NCT03526679) | Phase 1/2 | 완료 | 30 | 수술 불가능하거나 전이성인 지방성 육종·평활근육종에서 lenvatinib + eribulin 병용의 안전성과 효능을 평가한 단일군 시험(LEADER) |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [36129471](https://pubmed.ncbi.nlm.nih.gov/36129471/) | 2022 | Phase Ib/II 단일군 시험 | Clin Cancer Res | 진행성 지방육종·평활근육종에서 lenvatinib + eribulin의 안전성과 효능 평가 (LEADER 시험) |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | 전임상 리뷰 | Anticancer Res | Eribulin을 작용 기전이 다른 항암제와 병용했을 때의 전임상 항종양 활성 |
| [39103896](https://pubmed.ncbi.nlm.nih.gov/39103896/) | 2024 | 전임상/바이오마커 연구 | Exp Hematol Oncol | 연부조직육종에서 CDK4의 예후 바이오마커 역할과 탈분화형 지방육종에서 CDK4 억제의 시너지 효과 |
| [34326745](https://pubmed.ncbi.nlm.nih.gov/34326745/) | 2021 | 증례 보고 | Case Rep Oncol | 폐 전이 탈분화형 지방육종 환자가 개별화 치료(표적치료, 수술, 항암화학요법)로 종양 크기가 뚜렷이 감소한 사례 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201507059 | 렌비마캡슐4밀리그램(렌바티닙메실산염) | 캡슐 (상·하부 주황색, 흰색~미색 과립 충진) | 허가증 문서 링크로만 제공되어 본문 확인 불가 |
| 201507057 | 렌비마캡슐10밀리그램(렌바티닙메실산염) | 캡슐 (상부 주황색·하부 노란색, 흰색~미색 과립 충진) | 허가증 문서 링크로만 제공되어 본문 확인 불가 |

두 제품 모두 한국에자이(주)가 제조하며 유효한 단일제입니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (다중 키나제 억제제) |
| 골수억제 위험, 구토 유발성 등급, 모니터링 항목, 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 주요 항목은 다음과 같습니다.
  - **Major**: Dolasetron, Cisapride
  - **Moderate**: Famotidine, Loperamide, Clarithromycin, Levofloxacin, Palonosetron, Granisetron, Naltrexone 및 여러 하제 계열(Bisacodyl, Lactulose, Magnesium hydroxide 등)
  - **Minor**: Metronidazole

주요 경고와 금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
지방육종에 대해서는 완료된 단일군 Phase Ib/II 시험 1건(n=30)이 있고, 무작위 대조 근거나 lenvatinib 단독 효능 근거는 없습니다. 또한 허가사항의 경고·금기 정보가 확보되지 않아 안전성 검토를 진행할 수 없습니다.

**진행하려면 필요한 것:**
- 식약처 허가증(허가사항) PDF를 내려받아 기존 적응증, 경고, 금기 정보 확보
- 상세한 작용 기전(MOA) 데이터 보강
- LEADER 시험의 반응률, 무진행생존기간, 이상반응 등 결과 데이터 확인
- Lenvatinib 단독 효과와 eribulin 병용 효과를 구분할 수 있는 근거 또는 무작위 시험
- Major 상호작용 약물(dolasetron, cisapride)에 대한 병용 관리 방안 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

