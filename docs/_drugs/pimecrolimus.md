---
layout: default
title: Pimecrolimus
parent: 僅模型預測 (L5)
nav_order: 553
evidence_level: L5
indication_count: 4
---

# Pimecrolimus
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Pimecrolimus: 아토피 피부염에서 지루성 피부염으로

## 한 문장 요약

Pimecrolimus는 국소 calcineurin 억제제로, 원래 **아토피 피부염** 치료제로 개발되어 해외에서 승인·사용되고 있습니다.
TxGNN 모델은 **지루성 피부염(Seborrheic Dermatitis)**에도 효과가 있을 수 있다고 예측하며,
현재 **1건의 완료된 Phase 2 임상시험(113명)**과 **다수의 체계적 문헌고찰 및 RCT**가 이 방향을 지지합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 내 허가 자료 없음 (해외 승인 적응증: 아토피 피부염) |
| 예측 신규 적응증 | 지루성 피부염 (Seborrheic Dermatitis) |
| TxGNN 예측 점수 | 99.73% |
| 근거 수준 | L2 (완료된 Phase 2 RCT 1건 확보) |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 이 데이터베이스에는 상세한 작용 기전(MOA) 정보가 등록되어 있지 않습니다. 다만 공개된 약리학 정보에 따르면, Pimecrolimus는 국소 calcineurin 억제제로서 T세포 활성화를 억제하고 IL-2, IFN-γ 등 염증성 사이토카인의 방출을 차단합니다. 스테로이드와 달리 피부 위축 등의 부작용이 없어 장기 사용에 적합하다는 특징이 있습니다.

지루성 피부염은 *Malassezia* 효모균이 유발하는 만성 염증성 피부질환으로, 병태생리학적으로 아토피 피부염과 유사한 T세포·사이토카인 매개 염증 반응을 공유합니다. 실제로 문헌에서는 Pimecrolimus가 이미 아토피 피부염의 표준 국소 항염증제로 확립되어 있음을 확인할 수 있어(PMID 25557211 등), 이 기전이 지루성 피부염에도 적용될 수 있다는 근거가 됩니다.

특히 지루성 피부염 치료의 기존 표준 요법인 국소 스테로이드는 장기 사용 시 부작용 위험이 있어, 스테로이드 대체제로서 calcineurin 억제제 계열의 재창출 시도가 임상적으로 활발히 이루어지고 있습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00403559](https://clinicaltrials.gov/study/NCT00403559) | Phase 2 | 완료 | 113 | 지루성 피부염 치료에서 Elidel(Pimecrolimus)의 효과를 평가한 4주 무작위·이중맹검·활성대조 병행군 시험 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [22142161](https://pubmed.ncbi.nlm.nih.gov/22142161/) | 2012 | RCT 체계적 문헌고찰 | Expert Rev Clin Pharmacol | Pimecrolimus 1% 크림이 지루성 피부염에서 스테로이드·항진균제와 유사한 효능을 보이며 내약성이 우수함을 확인 |
| [23715821](https://pubmed.ncbi.nlm.nih.gov/23715821/) | 2013 | RCT | Ir J Med Sci | Sertaconazole 2% 크림 대비 Pimecrolimus 1% 크림의 지루성 피부염 치료 효과 비교 |
| [34910320](https://pubmed.ncbi.nlm.nih.gov/34910320/) | 2022 | RCT | Clin Exp Dermatol | 안면 지루성 피부염 환자에서 Pimecrolimus 1% vs Sertaconazole 2% 크림의 무작위 맹검 비교 |
| [36072203](https://pubmed.ncbi.nlm.nih.gov/36072203/) | 2022 | 체계적 문헌고찰 | Cureus | 안면 지루성 피부염에서 Pimecrolimus의 유효성과 안전성에 관한 RCT 체계적 문헌고찰 |
| [18677657](https://pubmed.ncbi.nlm.nih.gov/18677657/) | 2009 | RCT (개방형) | J Dermatolog Treat | Ketoconazole 2% 크림 대비 Pimecrolimus 1% 크림의 개방형·무작위·전향적 비교 연구 |
| [20000875](https://pubmed.ncbi.nlm.nih.gov/20000875/) | 2010 | 개방표지 연구 | Am J Clin Dermatol | 난치성 안면 지루성 피부염에서 Pimecrolimus 1% 크림의 개방표지 연구, 효과적이고 내약성 양호 |
| [28589618](https://pubmed.ncbi.nlm.nih.gov/28589618/) | 2018 | 임상연구 | J Cosmet Dermatol | 안면 지루성 피부염에서 Pimecrolimus 1% 크림의 투여 요법(regimen)별 비교 |
| [19255921](https://pubmed.ncbi.nlm.nih.gov/19255921/) | 2009 | 추적관찰 연구 | J Dermatolog Treat | 지루성 피부염에서 Pimecrolimus의 평균 완치·관해 기간 및 부작용 프로파일 추적관찰 |
| [19391059](https://pubmed.ncbi.nlm.nih.gov/19391059/) | 2010 | 추적관찰 연구 | J Dermatolog Treat | 재발성 지루성 피부염에서 Pimecrolimus 반복 사용의 유효성·안전성 탐색 |
| [15700745](https://pubmed.ncbi.nlm.nih.gov/15700745/) | 2004 | 임상연구 | Drugs Exp Clin Res | 안면 및 상반신 지루성 피부염에서 Pimecrolimus 1% 크림의 유효성·내약성·안전성 평가 |

## 한국 시판 정보

현재 한국 내 허가된 제품이 없습니다 (미출시, 허가증 0건).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> ⚠️ 참고: 허가사항(경고·금기) 및 상세 작용기전(MOA) 데이터가 현재 확보되지 않아, 안전성 초기 평가(S1) 단계 진입이 제한된 상태입니다.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
지루성 피부염에 대해 완료된 Phase 2 RCT 1건과 다수의 체계적 문헌고찰·RCT가 일관되게 유효성을 지지하며(근거 수준 L2), Pimecrolimus의 기존 확립된 항염증 기전(아토피 피부염 적응증)과 병태생리학적 연관성이 높습니다. 다만 국내 미출시 상태이며 안전성 핵심 자료(경고·금기)가 아직 확보되지 않아 가드레일 하에 진행이 필요합니다.

**진행하려면 필요한 것:**
- TFDA(또는 해당 규제기관) 허가사항의 경고·금기 사항 확보 (Blocking 데이터 갭)
- DrugBank 등에서 상세 작용기전(MOA) 데이터 확보
- 국내 허가·시판 여부 확인 및 도입 경로 검토
- 약물상호작용(DDI) 데이터 재조회
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

