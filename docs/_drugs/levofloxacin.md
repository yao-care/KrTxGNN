---
layout: default
title: Levofloxacin
parent: 僅模型預測 (L5)
nav_order: 439
evidence_level: L5
indication_count: 10
---

# Levofloxacin
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

# Levofloxacin: 세균 감염증에서 점상 상피성 각결막염으로

## 한 문장 요약

Levofloxacin은 플루오로퀴놀론계 항생제로 다양한 세균 감염증 치료에 널리 사용되어 온 약물입니다(한국 허가 자료는 현재 확인되지 않음). TxGNN 모델은 **점상 상피성 각결막염(Punctate Epithelial Keratoconjunctivitis)**에 효과가 있을 수 있다고 예측했으나, 관련 임상시험은 전무하고 문헌도 치료 효과를 평가하지 않은 발병 보고 1편뿐이어서 근거가 매우 제한적입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 자료 없음 (플루오로퀴놀론계 항생제, 세균 감염증 전반에 사용) |
| 예측 신규 적응증 | 점상 상피성 각결막염 (Punctate Epithelial Keratoconjunctivitis) |
| TxGNN 예측 점수 | 99.92% |
| 근거 수준 | L4 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Levofloxacin은 플루오로퀴놀론계 항생제로, 세균의 DNA 자이레이스/토포아이소머라제 IV를 저해하여 항균 작용을 나타내며, 세균성 결막염 등 세균 감염증에는 실제로 사용되고 있습니다.

다만 점상 상피성 각결막염은 주로 바이러스 또는 미포자충(microsporidia) 감염이 원인인 경우가 많아, 세균을 표적으로 하는 Levofloxacin의 기전이 직접 적용되기 어렵습니다. 첨부된 문헌(PMID 30055152)도 대만 수영장 오염과 관련된 미포자충성 각결막염 발생(outbreak) 사례 보고일 뿐, Levofloxacin의 치료 효과를 평가한 연구가 아닙니다. 세균 중복감염이 동반된 경우에 한해 간접적 관련성이 있을 수 있으나, 이 예측을 직접 뒷받침하는 기전적·임상적 근거는 부족합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | 발병 보고/증례군 (Tier 3) | American Journal of Ophthalmology | 대만 수영장 오염과 관련된 미포자충성 각결막염 집단 발병 보고. Levofloxacin 치료 효과는 평가하지 않음 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
관련 임상시험이 전무하고, 유일한 문헌은 치료 효과를 다루지 않은 발병 역학 보고에 불과합니다. 또한 해당 질환의 주요 원인(바이러스, 미포자충)이 Levofloxacin의 항균 기전과 직접 부합하지 않아, 현 단계에서 재창출을 진행할 근거가 부족합니다.

**진행하려면 필요한 것:**
- 한국(TFDA 상당) 허가사항의 경고·금기 정보 확보 (현재 Blocking 등급 자료 공백, DG001)
- DrugBank 등에서 상세 작용기전(MOA) 확인 (High 등급 자료 공백, DG002)
- 세균성 각결막염 한정 적응증 여부에 대한 별도 문헌 검토
- DDI 데이터베이스 재조회 (현재 조회 결과 not_found)

**참고:** 이번 Evidence Pack에는 동일 약물에 대해 더 강한 근거를 가진 예측 후보도 존재합니다 — 예: 다발골수종(monoclonal gammopathy) 예측은 TEAMM Phase 3 RCT(PMID 31668592) 등 20편의 문헌이, 패혈성 페스트(septicemic plague) 예측은 미국 FDA Animal Rule 승인 근거(L2, Proceed with Guardrails)가 뒷받침합니다. 필요 시 해당 후보들에 대해 별도 보고서 생성을 권장합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

