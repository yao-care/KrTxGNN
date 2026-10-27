---
layout: default
title: Rimegepant
parent: 모델 예측만 (L5)
nav_order: 656
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Rimegepant: 예측 신규 적응증 뇌줄기 조짐을 동반한 편두통 (Migraine with Brainstem Aura) (근거 수준 L5). 기존 적응증: 편두통 (한국 허가 문서에는 적응증 본문 대신 링크만 기재되어 있어…"
monitor_inn: "rimegepant"
predicted_indications: ["atrophoderma vermiculata", "ulerythema ophryogenesis", "heparin cofactor 2 deficiency", "antithrombin deficiency type 2", "factor 5 excess with spontaneous thrombosis"]
---

# Rimegepant
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **6** 건
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

## Rimegepant: 편두통에서 뇌줄기 조짐을 동반한 편두통으로
{: .text-alpha }

## 한 문장 요약

Rimegepant는 CGRP 수용체 길항제로, 원래 성인의 편두통 치료에 사용되는 약물입니다.
TxGNN 모델은 **뇌줄기 조짐을 동반한 편두통(Migraine with Brainstem Aura)**에 효과가 있을 수 있다고 예측합니다.
다만 이 아형만을 대상으로 한 임상시험은 없고, 편두통 전반을 다룬 **문헌 15편**이 간접적으로 뒷받침하는 수준입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 편두통 (한국 허가 문서에는 적응증 본문 대신 링크만 기재되어 있어, 문헌상 승인 적응증인 조짐 유무와 관계없는 편두통의 급성 치료 기준으로 기재) |
| 예측 신규 적응증 | 뇌줄기 조짐을 동반한 편두통 (Migraine with Brainstem Aura) |
| TxGNN 예측 점수 | 99.94% |
| 근거 수준 | L3 (아형 특이적 연구는 없고 편두통 전반에 대한 체계적 문헌고찰·메타분석이 있음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold (추가 연구 질문으로 유지) |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 이번 자료에 포함되어 있지 않습니다. 다만 문헌에 따르면 rimegepant는 CGRP(칼시토닌 유전자 관련 펩타이드) 수용체 길항제로, 조짐 유무와 관계없는 편두통의 급성 치료와 일화성 편두통의 예방 치료에 승인된 약물입니다.

뇌줄기 조짐을 동반한 편두통은 편두통의 한 아형으로, 삼차신경혈관계와 CGRP가 매개하는 병태생리를 공유합니다. 따라서 기전상 연관성은 강하다고 볼 수 있습니다.

그러나 확인된 문헌은 모두 편두통 전반을 대상으로 하며, 뇌줄기 조짐 환자만을 등록한 연구는 없습니다. 아형별 효과와 조짐 아형에서의 혈관 안전성은 아직 입증되지 않았고, 일반 편두통 근거를 외삽한 것임을 감안해야 합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

체계적 문헌고찰·메타분석과 3상 연구를 우선하여 10편을 정리했습니다. 모두 편두통 전반을 다룬 연구입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [42143245](https://pubmed.ncbi.nlm.nih.gov/42143245/) | 2026 | 체계적 문헌고찰/메타분석 | J Headache Pain | 성인 편두통 급성 치료에서 rimegepant 75 mg 단회 투여와 위약의 유효성·내약성 비교 |
| [41066271](https://pubmed.ncbi.nlm.nih.gov/41066271/) | 2025 | 3상 공개 라벨 | Cephalalgia | 중국 성인에서 급성 편두통 치료의 장기 안전성·효과 평가 |
| [41366286](https://pubmed.ncbi.nlm.nih.gov/41366286/) | 2025 | 4상 공개 라벨 | J Headache Pain | 일화성 편두통 예방을 위한 75 mg 매일 투여의 24주 안전성·내약성 평가 |
| [35790906](https://pubmed.ncbi.nlm.nih.gov/35790906/) | 2022 | 네트워크 메타분석 | J Headache Pain | 급성 편두통에서 lasmiditan과 rimegepant·ubrogepant의 상대 효능 비교 |
| [36739335](https://pubmed.ncbi.nlm.nih.gov/36739335/) | 2023 | Review | CNS Drugs | 급성 및 예방 치료에서 3상 시험상 위약보다 효과적임을 정리 |
| [38307667](https://pubmed.ncbi.nlm.nih.gov/38307667/) | 2024 | Review | Handbook of Clinical Neurology | 2세대 gepant(ubrogepant, rimegepant)의 승인 경과와 간독성 우려 정리 |
| [41574090](https://pubmed.ncbi.nlm.nih.gov/41574090/) | 2026 | 종단 MR 혈관조영 연구 | Brain Communications | 편두통 발작 중 rimegepant이 뇌·뇌외 동맥에 미치는 직접적 혈관 영향 평가 |
| [41652664](https://pubmed.ncbi.nlm.nih.gov/41652664/) | 2026 | 후향적 분석 | Headache | 청소년에서 허가 외 사용 시 내약성·효과 평가 |
| [32270407](https://pubmed.ncbi.nlm.nih.gov/32270407/) | 2020 | Review | Drugs | rimegepant ODT 최초 승인 개요 |
| [37904724](https://pubmed.ncbi.nlm.nih.gov/37904724/) | 2024 | 1상 | Clin Pharmacol Drug Dev | 고령자와 비고령 성인에서 약동학·안전성이 유사함 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202500678 | 너텍구강붕해정75밀리그램 (리메제판트황산염수화물) | 구강붕해정 | 적응증 본문 미확인 (허가 문서 링크만 제공됨) |

제조사는 한국화이자제약(주)입니다.

## 안전성 고려사항

- **약물 상호작용**: 이번 자료에서 총 57건이 확인되었습니다. 주요 항목은 다음과 같습니다.
  - **Major 등급**: Dexamethasone, Lumacaftor, Apalutamide
  - **Moderate 등급**: Aprepitant, Clarithromycin, Rolapitant, Sulfasalazine, Cobicistat, Eltrombopag, Ivacaftor, Chloramphenicol, Erythromycin, Fluconazole, Ketoconazole, Tacrolimus 등

  CYP3A4 관련 병용약이 많으므로 병용 시 주의가 필요합니다.
- **혈관 안전성**: 조짐 아형에서의 혈관 안전성은 아직 입증되지 않았습니다.

허가사항상의 경고 및 금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
기전상 연관성은 강하지만, 뇌줄기 조짐 아형을 대상으로 한 임상시험이나 문헌이 없고 근거는 편두통 전반에서 외삽한 것입니다. 현 단계에서는 추가 연구 질문으로 유지하는 것이 적절합니다.

**진행하려면 필요한 것:**
- 한국 허가 문서에서 적응증, 경고, 금기 확인 (현재 안전성 선별 진행을 막는 항목)
- 상세한 작용 기전(MOA) 데이터 보완
- 뇌줄기 조짐 편두통 환자를 대상으로 한 아형별 효과 근거
- 조짐 아형에서의 혈관 안전성 평가
- 주요 병용약(CYP3A4 관련 약물 등)에 대한 상호작용 관리 방안
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

