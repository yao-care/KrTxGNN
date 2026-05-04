---
layout: default
title: Benzoyl Peroxide
parent: 僅模型預測 (L5)
nav_order: 134
evidence_level: L5
indication_count: 4
---

# Benzoyl Peroxide
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

# Benzoyl Peroxide: 여드름에서 여드름 켈로이드(Acne Keloidalis Nuchae)로

---

## 한 문장 요약

Benzoyl Peroxide(BPO)는 *Cutibacterium acnes* 억제 및 각질 용해 작용을 통해 여드름을 치료하는 국소 외용 항균제입니다.
TxGNN 모델은 4개의 피부 적응증을 새롭게 예측하였으며, 이 중 **여드름 켈로이드(Acne Keloidalis Nuchae, AKN)**가 기전적 연관성이 가장 높은 후보로 선별되었습니다.
현재 **1건의 임상시험**과 **2편의 문헌**이 간접적으로 이 방향을 지지하나, 직접 근거는 아직 없습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 여드름 (Acne Vulgaris) |
| 예측 신규 적응증 | 여드름 켈로이드 (Acne Keloidalis Nuchae) |
| TxGNN 예측 점수 | 99.06% |
| 근거 수준 | L4 |
| 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 전체 예측 적응증 요약

이번 Evidence Pack은 4개 적응증을 동시 평가한 다중 후보 보고서입니다. 상위 3개는 근거 부재 및 기전 비합리성으로 Hold가 권장되며, 4번째 적응증인 여드름 켈로이드만이 간접 근거 및 기전적 연결고리를 보유합니다.

| 순위 | 예측 적응증 | TxGNN 점수 | 임상시험 | 문헌 | 근거 수준 | 결정 |
|------|------------|------------|---------|-----|---------|------|
| 1 | 외음부 역전성 모낭각화증 (Vulvar Inverted Follicular Keratosis) | 99.92% | 0건 | 0편 | L5 | Hold |
| 2 | 2-HEMA 감작 (2-Hydroxyethyl Methacrylate Sensitization) | 99.43% | 0건 | 0편 | L5 | Hold |
| 3 | 만성 위축성 피부염 (Acrodermatitis Chronica Atrophicans) | 99.17% | 0건 | 0편 | L5 | Hold |
| **4** | **여드름 켈로이드 (Acne Keloidalis Nuchae)** | **99.06%** | **1건** | **2편** | **L4** | **Research Question** |

---

## 이 예측이 타당한 이유는?

BPO는 강력한 산화성 과산화 반응을 통해 *C. acnes*를 억제하고 각질을 용해하는 국소 외용제입니다. DrugBank에 상세 MOA 데이터가 현재 누락되어 있으나, BPO의 두 가지 핵심 기전(모낭 내 세균 부하 감소 + 각전 형성 억제)은 임상적으로 폭넓게 확립되어 있습니다.

**여드름 켈로이드(AKN)**의 병리 기전은 만성 모낭 염증 → 섬유모세포 과활성화 → 비정상 콜라겐 침착의 연쇄 과정입니다. BPO는 두 가지 경로로 이 상류(upstream) 과정에 개입할 가능성이 있습니다: ① *C. acnes* 감소를 통해 TLR2/TLR4 매개 염증 신호를 억제하고, ② 각질 용해를 통해 모낭 개구부 폐쇄를 예방하여 물리적 염증을 차단합니다. 다만, 하류 켈로이드 형성 경로(TGF-β1/SMAD)에 대한 직접 작용은 없어 예방적 역할 또는 병용 요법으로서의 가능성이 보다 현실적입니다.

나머지 3개 예측 적응증은 기전적 근거가 없습니다. 외음부 역전성 모낭각화증은 세균·염증이 아닌 양성 종양성 병변이며, 2-HEMA 감작은 BPO가 오히려 피부 장벽 손상을 통해 감작을 **악화**시킬 위험이 있어 반적응증(contraindication concern)에 해당합니다. 만성 위축성 피부염은 *Borrelia burgdorferi*에 의한 전신 감염으로, 국소 BPO로는 심부 감염 조직에 도달할 수 없습니다. 세 예측 모두 지식 그래프 내 '모낭 관련 질환' 노드의 위상학적 근접성에서 비롯된 것으로 판단됩니다.

---

## 임상시험 근거

아래는 **여드름 켈로이드(Acne Keloid)** 적응증 검색 결과입니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT07015931](https://clinicaltrials.gov/study/NCT07015931) | Phase 1/2 | 완료 | 23 | 피츠패트릭 III-V형 경증 여드름에서 레티노산 0.025% vs. 아다팔렌 0.1% 비교. BPO 미포함이나 켈로이드 형성 등 여드름 후유증(post-acne sequelae) 평가를 포함함 |

> **주의**: 이 시험은 BPO를 직접 평가하지 않습니다 (관련성 등급: C). AKN을 주요 목적으로 한 BPO 임상시험은 현재 등록된 것이 없습니다.

---

## 문헌 근거

아래는 **여드름 켈로이드(Acne Keloid)** 적응증 검색 결과입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [39090034](https://pubmed.ncbi.nlm.nih.gov/39090034/) | 2024 | 임상 연구 | Dermatology Online Journal | 흑인 소아 여드름 환자(n=77) 후향적 분석. 켈로이드 형성 및 색소침착 고빈도 확인, 치료 패턴 기술 |
| [21034705](https://pubmed.ncbi.nlm.nih.gov/21034705/) | 2010 | 리뷰 | Actas Dermo-Sifiliograficas | 가성 모낭염(Pseudofolliculitis Barbae) 종합 리뷰. 모낭염증성 피부 질환의 임상 특성 및 병인 배경 정보 제공 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
4개의 예측 적응증 전체에 걸쳐 BPO를 직접 평가한 임상 근거가 없으며, 상위 3개 적응증은 기전적 합리성도 결여되어 있습니다. 여드름 켈로이드(AKN)는 모낭 염증 상류 억제라는 간접적 기전 연결고리가 있어 향후 탐색 가치가 있으나, 현 단계에서 진행을 정당화할 충분한 근거는 없습니다.

**진행하려면 필요한 것 (AKN 우선순위):**
- BPO를 직접 평가한 AKN 대상 파일럿 또는 전임상 연구 데이터 확보
- BPO 상세 작용 기전(MOA) 보완 (DrugBank API 조회)
- MFDS 허가사항을 통한 안전성·경고·금기 정보 확인
- 2-HEMA 감작 예측의 경우 반적응증 가능성에 대한 추가 안전성 검토 필요
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

