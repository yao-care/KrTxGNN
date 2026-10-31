---
layout: default
title: Erythromycin
parent: 모델 예측만 (L5)
nav_order: 317
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-31
description: "Erythromycin: 예측 신규 적응증 점상 상피성 각결막염 (punctate epithelial keratoconjunctivitis) (근거 수준 L4). 기존 적응증: 확인 불가 (허가 적응증이 문서 링크로만 제공되어 구체적 내용을 확인할 수 없음)"
monitor_inn: "ERYTHROMYCIN"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "acute contagious conjunctivitis", "exposure keratitis", "lymphogranuloma venereum", "necrotizing ulcerative gingivitis"]
---

# Erythromycin
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **5** 건
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

## Erythromycin: 국소 제형 항생제에서 점상 상피성 각결막염으로
{: .text-alpha }

## 한 문장 요약

Erythromycin은 마크로라이드계 항생제로, 한국에서는 대화제약의 겔 제제(수출용)로 허가되어 있습니다.
TxGNN 모델은 **점상 상피성 각결막염(punctate epithelial keratoconjunctivitis)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 임상시험은 없고 간접적인 문헌이 **1편** 있을 뿐입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 적응증이 문서 링크로만 제공되어 구체적 내용을 확인할 수 없음) |
| 예측 신규 적응증 | 점상 상피성 각결막염 (punctate epithelial keratoconjunctivitis) |
| TxGNN 예측 점수 | 0.9989 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 erythromycin은 항균 및 항염 작용을 가진 마크로라이드계 항생제이며, 세균 50S 리보솜 소단위를 억제하는 것으로 알려져 있습니다. 안과에서는 국소 erythromycin이 안구 표면 감염과 안검염 관련 질환에 사용됩니다.

점상 상피성 각결막염은 안검염에 이차적으로 생기는 경우가 있어, 마크로라이드의 항균·항염 작용이 기전상 도움이 될 가능성이 있습니다. 다만 연결된 문헌은 소아 만성 안검각결막염의 진단과 치료를 다룬 리뷰 1편뿐이며, 이 질환 자체에 대한 직접적인 입증은 아닙니다. 매우 높은 TxGNN 점수는 어디까지나 모델 예측입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [11495307](https://pubmed.ncbi.nlm.nih.gov/11495307/) | 2001 | Review | Journal of Pediatric Ophthalmology and Strabismus | 소아 만성 안검각결막염의 병력, 증상, 임상 징후 및 치료를 설명 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199901996 | 퓨어겔(수출용)(수출명: ERYTACNE) | 전질이 고른 흰색~연한 노란색의 불투명한 겔 | 허가 적응증 본문은 제공되지 않음 (허가사항 참조) |

## 안전성 고려사항

- **약물 상호작용**: 데이터 조회 결과 총 100건이 확인되었으며, 주요 항목은 다음과 같습니다.
  - **Major**: Loperamide, Clarithromycin
  - **Moderate**: Famotidine, Hydrocortisone, Pioglitazone, Alosetron, Aprepitant, Triamcinolone, Dexamethasone, Betamethasone, Budesonide, Cimetidine 등
  - **Minor**: Amoxicillin
- **지식 그래프 기반 금기 질환**(허가 문서가 아닌 TxGNN 지식 그래프의 약물-질환 금기 연결): QT 연장 증후군(가족성 포함), torsades de pointes, 포르피린증, 신장 질환, 간 질환, 담낭 질환, 혈액 질환, 박탈성 피부염, *Clostridium difficile* 대장염, 중증 근무력증, 청각 장애 등. 이는 허가사항의 공식 금기가 아니므로 참고용입니다.

허가사항의 경고 및 금기는 허가 문서에서 확인해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
점상 상피성 각결막염에 대한 직접적인 임상시험이나 문헌이 없고, 간접적인 리뷰 1편만 있어 근거 수준은 L4입니다. 또한 허가 적응증과 경고·금기 정보를 확인하지 못해 안전성 검토 단계로 넘어갈 수 없습니다.

**진행하려면 필요한 것:**
- MFDS 허가사항(적응증, 경고, 금기) 문서 확보 및 분석
- 작용 기전(MOA) 데이터 보완 (DrugBank 조회)
- 점상 상피성 각결막염 또는 안검염 관련 안구 질환에서 erythromycin 국소 제형을 평가한 임상 연구 탐색
- 현재 허가 제형(수출용 겔)과 안과용 제형 간의 투여 경로 적합성 검토

---

**참고: 다른 예측 적응증 (TxGNN 점수 순)**

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 | 비고 |
|-----|-----------|-----------|---------|------|
| 2 | 급성 전염성 결막염 | 0.9955 | L5 | 임상시험·문헌 없음, 모델 예측만 존재 (Hold) |
| 3 | 노출성 각막염 | 0.9950 | L5 | 연결된 문헌이 대부분 무관 (Hold) |
| 4 | 성병성 림프육아종 (LGV) | 0.9905 | L4 | 클라미디아 감염에 대한 마크로라이드의 활성과 역사적 사용을 다룬 리뷰 다수. 1차 치료는 doxycycline이며 erythromycin은 대체 요법 (추가 연구 과제) |
| 5 | 괴사성 궤양성 치은염 | 0.9900 | L5 | 1950~80년대 오래된 보고뿐 (Hold) |
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

