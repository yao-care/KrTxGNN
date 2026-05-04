---
layout: default
title: Bacitracin
parent: 僅模型預測 (L5)
nav_order: 118
evidence_level: L5
indication_count: 10
---

# Bacitracin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Bacitracin: 외용 항균제에서 점상 상피 각결막염으로

## 한 문장 요약

Bacitracin은 그람 양성균의 세포벽 합성을 억제하는 외용 폴리펩타이드 계열 항생제로, 피부·안과·이비인후과 영역의 세균 감염 국소 치료에 전통적으로 활용되어 왔습니다.
TxGNN 모델은 예측 목록 10개 중 **점상 상피 각결막염(Punctate Epithelial Keratoconjunctivitis)**을 최고 점수 99.999%로 제시하나,
이를 직접 지지하는 임상시험 및 문헌이 현재 **존재하지 않습니다**.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 국내 미등재 (국제적으로 외용 항균제로 사용) |
| 예측 신규 적응증 | 점상 상피 각결막염 (Punctate Epithelial Keratoconjunctivitis) |
| TxGNN 예측 점수 | 99.999% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미등재 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 Bacitracin의 상세한 작용 기전(MOA) 데이터가 확보되지 않은 상태입니다. 일반적으로 알려진 바에 따르면, Bacitracin은 세균 세포벽 합성 과정에서 지질 운반체(bactoprenol pyrophosphate)와 결합하여 펩티도글리칸 전구체의 재생을 차단하는 폴리펩타이드 항생제입니다. 주요 항균 범위는 그람 양성균(S. aureus, Streptococcus spp.)에 국한되며, 그람 음성균에는 활성이 거의 없습니다. 흡수가 거의 되지 않아 전신 투여보다는 외용·국소 투여에 적합합니다.

점상 상피 각결막염(PEK)은 주로 아데노바이러스 감염 또는 알레르기·자가면역 기전에 의해 유발되는 안과 질환입니다. Bacitracin의 항균 기전은 바이러스 또는 면역 매개 병인에 적용되지 않으므로, 이차적 세균 감염이 동반된 경우를 제외하면 기전적 연관성이 매우 낮습니다. TxGNN의 높은 예측 점수(99.999%)는 안과 감염 범주에 대한 광범위한 지식 그래프 연결성을 반영할 가능성이 높으며, PEK에 대한 특이적 효능을 시사한다고 해석하기 어렵습니다.

단, 전체 예측 목록 중 **외이도염(Otitis externa, 4위)은 근거 수준 L3**으로, Bacitracin 포함 복방제(Nebacetin: Bacitracin + Neomycin)가 역사적으로 귀 부위 국소 감염 치료에 사용된 6편의 문헌이 존재합니다. 이 중 PMID 17503066은 이중맹검 무작위배정 임상비교연구로, 현재 Evidence Pack에서 가장 의미 있는 재창출 방향입니다.

---

## 임상시험 근거

현재 점상 상피 각결막염에 대한 Bacitracin 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 점상 상피 각결막염에 대한 관련 문헌이 없습니다.

> **참고 — 외이도염(4위, L3) 주요 문헌:** 예측 4위 적응증인 외이도염에 한하여 6편의 문헌이 존재하며, 아래 가장 관련성 높은 2편을 제시합니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|------|------|------|---------|
| [17503066](https://pubmed.ncbi.nlm.nih.gov/17503066/) | 2007 | 임상비교연구 | Eur Arch Otorhinolaryngol | 급성 외이도염 151명 대상 이중맹검 연구. Polymyxin B + Bacitracin 단독 연고 대 동일 성분 + Hydrocortisone acetate 병용 효과·안전성 비교. |
| [14048629](https://pubmed.ncbi.nlm.nih.gov/14048629/) | 1963 | 증례 관찰 | Z Laryngol Rhinol Otol | Nebacetin(Bacitracin 포함) 스틸 제형을 염증성·분비성 귀 질환 국소 치료에 적용한 임상 관찰. |

---

## 안전성 고려사항

안전성 정보는 제조사 제품 설명서 및 DrugBank를 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 1위 적응증인 점상 상피 각결막염에 대해 직접적인 임상시험 및 문헌 근거가 전무하며, 바이러스·면역 매개 병인 특성상 Bacitracin의 항균 기전이 이 적응증에 적합하지 않습니다. 전체 10개 예측 중 9개가 L5 수준(근거 없음)이고, 국내 미등재 약물이므로 진행 전 기초 데이터 확보가 선행되어야 합니다.

**진행하려면 필요한 것:**
- DrugBank API를 통한 작용 기전(MOA) 및 DrugBank ID 확보 (DG002 해소)
- 허가사항 문서를 통한 경고·금기 안전성 정보 파싱 (DG001 해소)
- **외이도염(Otitis externa, L3)** 대상 심층 임상시험 검색 및 Evidence Pack 업데이트 — 현재 예측 중 가장 실현 가능성 높은 방향
- 국내 Bacitracin 포함 복방제(예: Nebacetin) 허가 현황 별도 조회
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

