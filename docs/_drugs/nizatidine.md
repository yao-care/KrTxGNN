---
layout: default
title: Nizatidine
parent: 僅模型預測 (L5)
nav_order: 314
evidence_level: L5
indication_count: 7
---

# Nizatidine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Nizatidine: 미출시 약물에서 활동성 소화성궤양(Active Peptic Ulcer Disease) 치료제로

## 한 문장 요약

Nizatidine(DrugBank ID: DB00585)은 히스타민 H2 수용체 길항제(H2RA) 계열 약물이나, 현재 한국에는 허가 제품이 없어 국내 원 적응증 자료가 확보되지 않은 상태입니다.
TxGNN 모델은 **활동성 소화성궤양(Active Peptic Ulcer Disease)**에 효과가 있을 것으로 예측(점수 99.96%)하며, 등록된 임상시험은 없으나 **19편의 문헌**(이 중 3편은 완료된 RCT)이 이 방향을 뒷받침합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 자료 없음 (한국 미출시, 국내 허가 문서 미확보) |
| 예측 신규 적응증 | 활동성 소화성궤양 (Active Peptic Ulcer Disease) |
| TxGNN 예측 점수 | 99.96% |
| 근거 수준 | L1 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

현재 Evidence Pack에는 상세한 작용기전(MOA) 데이터가 확보되어 있지 않습니다. 다만 문헌 근거에 따르면 Nizatidine은 히스타민 H2 수용체 길항제(H2RA) 계열 약물로, 위벽세포의 H2 수용체를 차단하여 기저·야간·자극 유발 위산 분비를 억제하는 것으로 보고되어 있습니다(PMID 2905640, 8097411).

TxGNN이 예측한 신규 적응증인 '활동성 소화성궤양'은 사실 H2RA 계열 약물의 고전적·핵심 적응증입니다. 즉 이번 예측은 완전히 새로운 질환을 발굴했다기보다, Nizatidine이 해외에서 이미 폭넓게 검증된 본연의 치료 영역을 지식그래프가 정확히 재확인한 결과로 해석하는 것이 타당합니다.

한국 규제 자료상 Nizatidine은 현재 국내 허가 제품이 전무하고(미출시, 허가증 0건), 원 적응증에 대한 국내 공식 문서도 확보되지 않았습니다. 따라서 이번 평가는 '새로운 질환으로의 재창출'이라기보다 '이미 기전적으로 검증된 적응증에 대한 국내 도입 타당성 검토'에 가깝습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [1526089](https://pubmed.ncbi.nlm.nih.gov/1526089/) | 1992 | RCT | Clin Pharmacol Ther | 활동성 양성 위궤양 환자 대상, nizatidine 150mg BID/300mg 취침 시 vs 위약 8주 다기관 비교, 궤양 치유·증상 완화 효과 확인 |
| [2892259](https://pubmed.ncbi.nlm.nih.gov/2892259/) | 1987 | RCT | Scand J Gastroenterol Suppl | 치유된 십이지장궤양 513명 대상 1년 유지요법 연구, 재발률이 nizatidine군에서 위약군 대비 현저히 낮음(12개월 34% vs 64%) |
| [1982108](https://pubmed.ncbi.nlm.nih.gov/1982108/) | 1990 | RCT | Hepatogastroenterology | 활동성 위궤양 101명 대상, nizatidine(150mg BID/300mg 취침 시) vs ranitidine 150mg BID 8주 비교, 치유율 유사 |
| [9198292](https://pubmed.ncbi.nlm.nih.gov/9198292/) | 1997 | RCT | Zhonghua Yi Xue Za Zhi | 소화성궤양 환자 대상 clarithromycin 병용 H. pylori 박멸요법 평가 |
| [2905640](https://pubmed.ncbi.nlm.nih.gov/2905640/) | 1988 | Review | Drugs | Nizatidine의 약력학·약동학 특성 및 소화성궤양 치료 활용에 대한 예비 종설 |
| [2184124](https://pubmed.ncbi.nlm.nih.gov/2184124/) | 1990 | Review | Gastroenterol Clin North Am | 소화성궤양 내과적 치료 전반 개관, 신규 H2 차단제(nizatidine 등) 안전성·유효성 소개 |
| [8097411](https://pubmed.ncbi.nlm.nih.gov/8097411/) | 1993 | Review | Baillieres Clin Gastroenterol | 위산 분비 조절 기전(신경·호르몬·측분비) 및 억제 약리학 총설 |
| [2570656](https://pubmed.ncbi.nlm.nih.gov/2570656/) | 1989 | Cohort | Clin Pharmacol Ther | 2단계 위약대조 다기관 연구, nizatidine 150mg BID로 활동성 십이지장궤양 치유 및 재발 평가 |
| [7960687](https://pubmed.ncbi.nlm.nih.gov/7960687/) | 1994 | Cohort | Isr J Med Sci | 55명 대상 이중맹검 위약대조 연구, nizatidine이 십이지장궤양 치유 및 점막 염증 매개물질에 미치는 영향 평가 |
| [1974318](https://pubmed.ncbi.nlm.nih.gov/1974318/) | 1990 | Cohort | Medicina (Firenze) | 십이지장궤양 20명 대상, nizatidine과 misoprostol이 펩신 활성 및 위점막에 미치는 영향 비교 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

*(참고: DDI 조회 결과 없음, 주요 경고·금기 자료 미확보 — DG001 "TFDA 仿單警語/禁忌" Blocking 데이터 갭으로 등록되어 있습니다.)*

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
활동성 소화성궤양에 대해서는 1980~90년대 완료된 Phase급 RCT 3편을 포함해 총 19편의 문헌 근거가 축적되어 있어 근거 수준 L1으로 평가됩니다. 다만 한국에는 현재 허가 제품이 없고(미출시), 안전성 라벨링 정보(경고·금기·DDI)가 전혀 확보되지 않은 Blocking 수준의 데이터 갭(DG001)이 존재하여, 근거 자체는 강하지만 즉시 임상 사용을 권고하기는 어렵습니다. 나머지 6건의 예측 적응증(peptic ulcer perforation, gastrojejunal ulcer, duodenal obstruction, duodenogastric reflux, gastroduodenitis, multiple endocrine neoplasia)은 근거 수준 L2~L5로 rank 1 대비 낮아 이번 평가에서는 Hold 또는 추가 연구가 필요한 상태로 분류되었습니다.

**진행하려면 필요한 것:**
- 국내 허가용 안전성 자료(경고문, 금기, 약물상호작용) 확보 — DG001 Blocking 해소 필수
- DrugBank 등을 통한 공식 작용기전(MOA) 데이터 확인 — DG002 해소
- 국내 또는 가교 임상시험 데이터 확보 (현재 등록된 임상시험 없음)
- 정식 수입·허가 경로(신약 재심사 또는 자료제출의약품 등) 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

