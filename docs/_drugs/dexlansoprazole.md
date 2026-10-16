---
layout: default
title: Dexlansoprazole
parent: 모델 예측만 (L5)
nav_order: 272
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Dexlansoprazole: 예측 신규 적응증 활동성 소화성 궤양 (Active Peptic Ulcer Disease) (근거 수준 L5). 기존 적응증: 허가증에 적응증 원문이 아닌 허가사항 문서 링크만 제공되어 구체적 적응증 텍스트는 확인할 수 없음 (허가사항 참조)"
---

# Dexlansoprazole
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

# Dexlansoprazole: 위산 관련 질환에서 활동성 소화성 궤양으로

## 한 문장 요약

Dexlansoprazole은 위벽세포의 H+/K+-ATPase(양성자 펌프)를 억제하는 프로톤 펌프 억제제(PPI)로, 한국에서 위산 관련 질환 치료제로 시판되고 있습니다.
TxGNN 모델은 **활동성 소화성 궤양(active peptic ulcer disease)**에 효과가 있을 수 있다고 예측하며, 현재 **2건의 Phase 3 임상시험**과 **3편의 문헌**이 이 방향을 간접적으로 지지합니다.
다만 이 예측은 PPI 계열에 이미 알려진 용도와 가까워서, 엄밀한 의미의 재창출이라기보다 계열 효과에 가까운 사용입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에 적응증 원문이 아닌 허가사항 문서 링크만 제공되어 구체적 적응증 텍스트는 확인할 수 없음 (허가사항 참조) |
| 예측 신규 적응증 | 활동성 소화성 궤양 (Active Peptic Ulcer Disease) |
| TxGNN 예측 점수 | 99.999% |
| 근거 수준 | L1 (다만 임상시험 대부분이 미란성 식도염 대상이라 궤양에 대한 직접 근거는 제한적) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 4건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 없습니다. 알려진 정보에 따르면 dexlansoprazole은 lansoprazole의 거울상 이성질체(R-enantiomer)로 PPI 계열에 속하며, 위벽세포의 H+/K+-ATPase를 비가역적으로 차단하여 위산 분비를 억제합니다.

소화성 궤양은 위산에 의존하는 질환이어서, 강력하고 지속적인 위산 억제는 궤양 치유의 표준 기전입니다. 따라서 활동성 소화성 궤양은 PPI 계열의 전형적인 적응증이며, 기전상 적용 가능성이 높습니다.

주의할 점은 두 가지입니다. 첫째, 연계된 Phase 3 시험은 제목상 미란성 식도염 치유 및 유지가 주된 평가변수로 보이므로, 궤양 치유 자체를 직접 입증하는 근거는 아닙니다. 둘째, 기전 데이터가 비어 있어 기전 연결은 PPI 계열 지식에 의존합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00251719](https://clinicaltrials.gov/study/NCT00251719) | Phase 3 | 완료 | 2054 | 미란성 식도염 치유에서 dexlansoprazole MR 60/90 mg vs lansoprazole 30 mg (8주) |
| [NCT00251693](https://clinicaltrials.gov/study/NCT00251693) | Phase 3 | 완료 | 2038 | 동일한 용량 설계의 미란성 식도염 치유 시험 |

두 시험 모두 대규모 RCT로 산 억제 효능과 안전성을 뒷받침하지만, 궤양 치유 평가변수에 대해서는 간접적입니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | 체계적 문헌고찰/네트워크 메타분석 | Am J Gastroenterol | LA 분류 C/D 중증 식도염 치유에서 P-CAB와 PPI의 효능·안전성 비교 |
| [18821474](https://pubmed.ncbi.nlm.nih.gov/18821474/) | 2008 | Review | Curr Opin Investig Drugs | dexlansoprazole 서방형 제제의 개발 현황 및 역류성 식도염 치료 |
| [36150104](https://pubmed.ncbi.nlm.nih.gov/36150104/) | 2022 | 전임상/기전 연구 | J Chin Med Assoc | PPI에 의한 V-ATPase 억제 및 소포체 스트레스 유도 기전 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201802449 | 덱시라졸캡슐60밀리그램 (유한양행) | 경질캡슐 (과립 충전) | 허가사항 문서 참조 |
| 201207344 | 덱실란트디알캡슐60밀리그램 (한국다케다제약) | 경질캡슐 (과립 충전) | 허가사항 문서 참조 |
| 201207343 | 덱실란트디알캡슐30밀리그램 (한국다케다제약) | 경질캡슐 (과립 충전) | 허가사항 문서 참조 |
| 201802450 | 덱시라졸캡슐30밀리그램 (유한양행) | 경질캡슐 (과립 충전) | 허가사항 문서 참조 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 확인되었으며, 주요 항목은 다음과 같습니다.
  - Major: acalabrutinib, atazanavir
  - Moderate: fosamprenavir, foscarnet, fostamatinib, furosemide, gefitinib, hydrochlorothiazide, bosutinib, bumetanide, amphotericin B, amikacin, ampicillin 등
  - Minor: acetylsalicylic acid, axitinib, brivaracetam, cyanocobalamin
- **지식그래프 기반 금기 질환 (허가사항 아님)**: 간질환, 담낭질환, 골다공증, 폐경 후 골다공증, 골절. 허가사항 문구가 아니라 지식그래프에서 도출된 정보이므로 허가사항과 대조가 필요합니다.

허가사항의 경고 및 금기 정보는 별도로 확인해야 합니다.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
활동성 소화성 궤양은 PPI 계열의 표준 적응증이고 dexlansoprazole은 대규모 Phase 3 RCT에서 산 억제 효능과 안전성이 확인되었습니다. 다만 해당 시험들은 미란성 식도염이 평가변수여서 궤양 치유에 대한 직접 근거는 제한적입니다.

**진행하려면 필요한 것:**
- MFDS 허가사항(경고·금기·적응증) 확인 및 분석 (현재 안전성 선별을 진행하지 못하는 핵심 공백)
- 상세한 약물 작용 기전(MOA) 데이터 확보
- 등록된 Phase 3 시험의 평가변수 확인으로 궤양 치유 직접 근거 여부 검증
- 100건의 약물 상호작용 중 Major 항목(acalabrutinib, atazanavir 등) 병용 관리 계획
- PPI 장기 사용 위험(골절·골다공증 등)에 대한 모니터링 계획

---

### 참고: 기타 예측 적응증 (TxGNN 상위 10위 중)

- **십이지장궤양, 위궤양**: 근거 수준 L1, Proceed with Guardrails. 연계된 Phase 3 시험은 마찬가지로 식도염 대상이며, 진행 중인 Phase 4 시험(NCT07344506, H. pylori 제균, 942명)이 궤양 결과와 가장 직접 관련되지만 아직 결과가 없습니다.
- **위공장 궤양**: L3, Research Question. 유일한 시험(NCT04423588)은 참여자 0명으로 철회되었습니다.
- **소화성 궤양 천공, 위십이지장염, 십이지장 폐쇄, 십이지장위 역류, 무산증, 가죽병 위(linitis plastica)**: L5, Hold. 임상 근거가 없고 모델 점수에만 의존합니다. 특히 무산증은 PPI의 약리 효과와 반대되므로 제외가 권장됩니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

