---
layout: default
title: Delamanid
parent: 僅模型預測 (L5)
nav_order: 203
evidence_level: L5
indication_count: 10
---

# Delamanid
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

# Delamanid: 다제내성 결핵(MDR-TB)에서 소형 결핵(Bovine Tuberculosis)으로

## 한 문장 요약

Delamanid는 다제내성 결핵(MDR-TB) 치료를 위해 개발된 신형 항결핵제로, 유럽(EMA) 및 일본(PMDA)에서 승인되었으나 한국에는 아직 허가되지 않은 상태입니다. TxGNN 모델은 **소형 결핵(Bovine Tuberculosis, *Mycobacterium bovis* 감염)**에도 효과가 있을 수 있다고 예측하며, 현재 **1편의 문헌**이 관련 병원체의 특성 분석 근거를 제공합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 미허가 (유럽·일본: 다제내성 결핵 MDR-TB 치료) |
| 예측 신규 적응증 | 소형 결핵 (Bovine Tuberculosis, *M. bovis*) |
| TxGNN 예측 점수 | 99.91% |
| 근거 수준 | L4 (전임상/기전 연구) |
| 한국 시판 현황 | 미상시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 Evidence Pack에 상세한 작용 기전(MOA) 데이터가 포함되어 있지 않습니다. 알려진 문헌 정보에 따르면, Delamanid는 프로드러그(prodrug)로서 분지균 내 **deazaflavin 의존성 니트로환원효소(Ddn, *Rv3547* 유전자 산물)**에 의해 환원 활성화된 후, 분지균산(mycolic acid) 생합성 경로—특히 methoxy-mycolate 및 keto-mycolate—를 선택적으로 억제합니다. 이 기전은 활발히 복제 중인 균뿐 아니라 저산소 환경의 휴면기 균에도 부분적으로 작용하는 것으로 알려져 있습니다.

소형 결핵의 원인균인 *Mycobacterium bovis*는 *M. tuberculosis*와 99% 이상의 유전체 동일성을 공유하며, Delamanid의 활성화 효소(*Rv3547* 동형 유전자)와 표적 분지균산 합성 경로가 거의 동일하게 보존되어 있습니다. 여기에 중요한 임상적 고려사항이 있습니다. *M. bovis*는 표준 결핵 치료의 핵심 약물인 피라진아미드(PZA)에 **선천적 내성**을 가지고 있어 표준 6개월 방안(HRZE)을 그대로 적용할 수 없으며, 이로 인해 치료 선택지가 제한됩니다. 이러한 약물 선택지 제약 상황에서 Delamanid의 보충 사용은 기전적으로 합당한 가설이 됩니다.

그러나 인수공통 결핵(Zoonotic TB)은 개별 환자 치료보다 공중보건·방역 관리가 우선되는 분야입니다. 실질적인 개별 치료 수요는 *M. bovis* 감염이 발생한 HIV 감염자, 장기이식 환자 등 면역저하 환자군으로 한정될 가능성이 높습니다. 현재 직접적인 임상시험이나 증례 보고가 전혀 없어, 이 예측은 기전 가설 단계에 머물러 있습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [39487429](https://pubmed.ncbi.nlm.nih.gov/39487429/) | 2024 | Observational / Molecular Epidemiology | BMC Genomics | 인간 감염 *M. bovis* 분리주를 전장유전체시퀀싱(WGS)으로 분석하여 순환 유전형, 독성 및 항균제 내성 관련 유전체 특성 규명; Delamanid 활성화 관련 Rv3547 동형 유전자 상태 포함 가능성 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
*M. bovis*와 *M. tuberculosis*의 분지균산 합성 경로 동일성으로 기전적 타당성은 인정되나, 임상시험이 전무하고 직접적인 인체 효능 근거가 없습니다. 인수공통 결핵은 개인 치료보다 공중보건 관리가 우선되는 영역으로, 현 단계에서 소형 결핵 단독 적응증으로의 임상 개발 투자는 정당화되기 어렵습니다.

**진행하려면 필요한 것:**
- *M. bovis* 대상 Delamanid의 최소억제농도(MIC) 및 in vitro/in vivo 효능 전임상 데이터
- PZA 내성 *M. bovis* 감염 환자(특히 면역저하자)에 대한 후향적 증례 보고 또는 코호트 연구
- Delamanid 상세 MOA 및 안전성 데이터 (DrugBank API 조회, TFDA 仿單 PDF 수집 필요)
- 한국 내 인수공통 결핵 역학 현황 및 PZA 내성 *M. bovis* 감염 실제 의료 수요 파악

---

> **⚠️ 이 Evidence Pack의 추가 주목 예측**
>
> 동일 Evidence Pack(TW-DB11637-multi)에서 **Rank 2 예측인 비활성 결핵 / 잠복결핵(Inactive Tuberculosis)**이 훨씬 강력한 임상 근거를 보여줍니다. PHOENIx MDR-TB 시험(NCT03568383, Phase 3, 5,832명)이 MDR-TB 가족접촉자의 잠복결핵 예방 목적으로 Delamanid를 직접 평가 중이며, 근거 수준 **L1**, 권장 결정 **Proceed with Guardrails**로 분류됩니다. 이 적응증에 대한 별도 심층 보고서 작성을 권장합니다.

---

> *본 보고서는 연구 참고 목적으로만 작성되었으며, 의료 행위의 근거로 사용될 수 없습니다. 모든 예측 결과는 임상 검증이 필요합니다.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

