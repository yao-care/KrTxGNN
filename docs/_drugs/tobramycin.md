---
layout: default
title: Tobramycin
parent: 僅模型預測 (L5)
nav_order: 680
evidence_level: L5
indication_count: 10
---

# Tobramycin
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

# Tobramycin: 세균 감염증에서 점상 상피성 각결막염으로

## 한 문장 요약

Tobramycin은 그람음성균(특히 Pseudomonas aeruginosa)에 강한 활성을 지닌 아미노글리코사이드계 항생제로, 전신 감염, 낭포성 섬유증 폐감염, 안과·이과 국소 감염 등에 널리 사용되어 왔습니다. TxGNN 모델은 **점상 상피성 각결막염(Punctate Epithelial Keratoconjunctivitis)**에도 효과가 있을 것으로 예측하며(예측 점수 **99.99%**), 현재 이를 뒷받침하는 문헌은 **1편**이 확인되고 관련 임상시험은 등록되어 있지 않습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 세균 감염증(그람음성균, 특히 *Pseudomonas aeruginosa*) — 낭포성 섬유증 폐감염, 안과/이과 국소 감염 등 (한국 허가 자료 없음) |
| 예측 신규 적응증 | 점상 상피성 각결막염 (Punctate Epithelial Keratoconjunctivitis) |
| TxGNN 예측 점수 | 99.99% (rank 704) |
| 근거 수준 | L3 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

Tobramycin은 아미노글리코사이드계 항생제로, 세균의 30S 리보솜 소단위체에 결합하여 단백질 합성을 억제함으로써 살균 작용을 나타냅니다. 그람음성균, 특히 *Pseudomonas aeruginosa*에 대한 강한 항균력이 특징이며, 이 기전은 이미 임상에서 안과 영역에도 널리 적용되고 있습니다.

점상 상피성 각결막염은 세균성 안검-각결막염(blepharo-keratoconjunctivitis)의 한 형태로 발현되는 경우가 많으며, tobramycin을 포함한 항생제/스테로이드 복합 점안제(예: Tobradex, Zylet)가 이미 임상 현장에서 이러한 염증성 각결막 질환의 관리에 표준적으로 사용되고 있습니다. 따라서 이번 예측은 완전히 새로운 적응증이라기보다, **이미 확립된 안과 국소 사용의 근거를 보강하는 성격**에 가깝습니다 — 기전상 타당성은 높지만 '새로운' 적응증 확장이라기보다는 기존 임상 관행에 대한 근거 재확인으로 해석하는 것이 정확합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [17526462](https://pubmed.ncbi.nlm.nih.gov/17526462/) | 2007 | RCT (소규모 비교) | Advances in Therapy | Tobramycin 0.3%/Dexamethasone 0.1% vs Tobramycin 0.3%/Loteprednol 0.5% 비교 — blepharo-keratoconjunctivitis 환자 40안 대상 무작위, 병행군, 이중눈가림 시험으로 두 복합제제 모두 염증을 신속히 조절함 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
Tobramycin이 세균성 각결막염 관리에 기전적으로 타당하고 유사 복합제(Tobradex, Zylet)가 이미 임상에서 사용되고 있으나, 이 예측을 직접 뒷받침하는 임상시험이 없고 문헌도 소규모 RCT 1편에 그쳐 독자적 신규 적응증으로 추진하기에는 근거가 제한적입니다.

**진행하려면 필요한 것:**
- TFDA(한국 규제기관) 허가사항의 경고·금기 정보 확보 (현재 Blocking 데이터 갭)
- DrugBank 등을 통한 상세 작용기전(MOA) 데이터 확보 (현재 High 우선순위 데이터 갭)
- 점상 상피성 각결막염에 특화된 전향적 임상시험 또는 관찰연구 추가 확보
- 국내 시판 여부 및 안과용 제형 허가 현황 확인
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

