---
layout: default
title: Esomeprazole
parent: 僅模型預測 (L5)
nav_order: 295
evidence_level: L5
indication_count: 3
---

# Esomeprazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Esomeprazole: 위산 관련 질환에서 십이지장위역류(Duodenogastric Reflux)로

## 한 문장 요약

Esomeprazole은 프로톤펌프억제제(PPI) 계열 약물로, 국제적으로 소화성궤양·위식도역류질환(GERD)·H. pylori 감염 등 위산 관련 질환에 널리 사용되어 왔습니다(한국 내 공식 허가 적응증은 미확인). TxGNN 모델은 **십이지장위역류(Duodenogastric Reflux)**에 효과가 있을 수 있다고 예측했으나, 이를 뒷받침하는 자료는 관련 임상시험 0건, 문헌 1건(그마저도 해당 질환을 직접 다루지 않는 PPI 일반 리뷰)에 불과하며, 예측 근거 자체도 기전상 약하다고 평가됩니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 위산 관련 질환 (PPI 계열 – 소화성궤양, H. pylori 감염, GERD, NSAID 유발 위장병변 등; 한국 공식 허가 적응증 미확인) |
| 예측 신규 적응증 | 십이지장위역류 (Duodenogastric Reflux) |
| TxGNN 예측 점수 | 99.53% |
| 근거 수준 | L4 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 esomeprazole의 상세한 작용기전(MOA) 데이터는 확보되지 않았습니다(Data Gap). 다만 첨부된 문헌(PMID 18679668)에 따르면 PPI 계열 약물은 위벽세포의 H+/K+-ATPase를 억제하여 위산 분비를 감소시키며, 소화성궤양·H. pylori 감염·GERD·NSAID 유발 위장병변·Zollinger-Ellison 증후군 치료에 1차 선택약으로 사용됩니다.

그러나 이 기전을 십이지장위역류에 적용하는 데는 근본적인 한계가 있습니다. 십이지장위역류는 담즙·췌장액이 위로 역류하여 발생하는 것이 주된 병인이며, 위산 과다가 원인이 아닙니다. Esomeprazole은 위산 분비만 억제할 뿐 담즙 성분을 중화하거나 차단하는 작용은 없어, 이론적으로는 동반된 산 관련 증상 완화에만 제한적으로 기여할 수 있고 질환의 근본 원인을 치료하지는 못합니다. 즉 기전적 연관성이 약하며 직접적인 대인(對因) 치료로 보기 어렵습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | European Journal of Clinical Pharmacology | PPI 계열 약물의 임상 활용 및 약동학 개괄 리뷰. 소화성궤양, H. pylori 감염, GERD, NSAID 유발 위장병변, Zollinger-Ellison 증후군을 주요 적응증으로 소개하나, 십이지장위역류는 직접 다루지 않음 |

---

## 한국 시판 정보

한국에 등록된 허가가 없습니다 (미시판, 허가증 0건).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
근거 수준이 L4에 그치고, 관련 임상시험이 전무하며 유일한 문헌도 십이지장위역류를 직접 다루지 않습니다. 또한 repurposing 기전 분석 자체가 "담즙 역류가 주된 병인이므로 위산 억제만으로는 근본 치료가 어렵다"고 명시해 기전적 타당성이 약함을 지적하고 있습니다. TxGNN 점수(99.53%)가 높은 것은 지식그래프 임베딩상 인접 질환(예: 십이지장궤양)과의 유사성에 따른 결과일 가능성이 있어, 현 단계에서 적극적 진행은 권장하지 않습니다.

**진행하려면 필요한 것:**
- 십이지장위역류를 직접 대상으로 한 전임상/기전 연구 또는 임상 근거 확보
- Esomeprazole의 상세 MOA 데이터 보완 (DG002)
- 식약처(TFDA/MFDS) 허가사항상 경고·금기·DDI 정보 확보 — 안전성 초기평가(S1) 진입을 위한 필수 선행 조건 (DG001, Blocking)
- 한국 내 실제 시판/허가 현황 재확인
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

