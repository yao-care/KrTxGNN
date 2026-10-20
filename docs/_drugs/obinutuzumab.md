---
layout: default
title: Obinutuzumab
parent: 모델 예측만 (L5)
nav_order: 557
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Obinutuzumab: 예측 신규 적응증 생식중심 이전 CLL/SLL (pregerminal center chronic lymphocytic leukemia/smal… (근거 수준 L5). 기존 적응증: 허가 적응증 본문이 문서 링크로만 제공되어 구체적 내용을 확인할 수 없음 (CLL 등 B세포 악성종양 허가로 알려져 있음)"
---

# Obinutuzumab
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **3** 건
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

# Obinutuzumab: 만성 림프구성 백혈병에서 CLL/SLL 하위유형(생식중심 이전)으로

## 한 문장 요약

Obinutuzumab은 CD20을 표적으로 하는 당화 최적화 type II 항체로, B세포 악성종양 치료에 사용되며 CLL에서도 이미 허가된 약물로 알려져 있습니다.
TxGNN 모델은 **생식중심 이전 만성 림프구성 백혈병/소림프구성 림프종(pregerminal center CLL/SLL)**에 효과가 있을 수 있다고 예측합니다. 그러나 이 하위유형을 직접 다룬 **임상시험은 0건, 문헌도 0편**이어서 모델 예측만 있는 상태입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 문서 링크로만 제공되어 구체적 내용을 확인할 수 없음 (CLL 등 B세포 악성종양 허가로 알려져 있음) |
| 예측 신규 적응증 | 생식중심 이전 CLL/SLL (pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma) |
| TxGNN 예측 점수 | 99.21% |
| 근거 수준 | L4 (기전상 타당하나 이 하위유형에 대한 직접 연구 없음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 수집되지 않았습니다. 다만 Obinutuzumab은 CD20을 표적으로 하는 type II 당화 최적화 항체로 알려져 있습니다. 직접적인 세포 사멸 유도와 항체 의존성 세포독성(ADCC), 식세포작용(ADCP)을 통해 작용합니다. CLL/SLL 세포도 CD20을 발현하므로 기전상 적용 가능성은 충분합니다.

다만 이 예측은 이미 허가된 CLL 전체 적응증의 한 하위유형입니다. 따라서 진정한 의미의 약물 재창출이라기보다 기존 적응증의 세분화에 가깝습니다. 근거도 상위 질환(CLL)을 통한 간접 근거일 뿐, 이 하위유형만을 대상으로 한 연구는 없습니다.

같은 점수(99.21%)로 예측된 "면역글로불린 중쇄 가변부위 유전자 체세포 과돌연변이(IGHV mutated) CLL/SLL"도 같은 상황입니다. CD20은 IGHV 변이 여부와 관계없이 발현되므로 기전은 타당하지만, 하위유형 특이적 연구는 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201404311 | 가싸이바주(오비누투주맙, 유전자재조합) | 무색 바이알에 충전된 무색~연한 갈색 액상 주사제 | 허가 적응증 본문은 MFDS 문서 링크로만 제공됨 (제조사: 한국로슈) |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (항CD20 단클론항체) |
| 골수억제 위험 | 호중구감소증 등 혈구감소증 주의 필요 (구체적 빈도는 허가사항 참조) |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | CBC(분류 포함), 감염 징후, B형 간염 바이러스 상태, 투여 관련 반응 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **주의 위험(가드레일)**: 투여 관련 반응(infusion reaction), B형 간염 재활성화, 진행성 다초점 백질뇌병증(PML), 혈구감소증, 감염
- **약물 상호작용**: 총 81건이 확인되었습니다. 주요(Major) 등급은 다음과 같습니다.
  - Deferiprone
  - Samarium (153Sm) lexidronam
  - Adalimumab
  - Baricitinib
  - Certolizumab pegol
  - Cladribine
  - Clozapine

  Moderate 등급으로는 Alemtuzumab, Azathioprine, Anakinra, Zidovudine, Chloramphenicol, 일부 생백신·불활화 백신 등이 있습니다. 면역억제제와 골수억제제는 병용 시 특히 주의가 필요합니다.

허가사항의 경고·금기 세부 내용은 허가사항을 참조하세요.

## 참고: 같은 약물의 다른 예측 적응증 (3순위, 여포성 림프종)

이 약물에는 근거가 풍부한 **여포성 림프종(Follicular Lymphoma)** 예측도 있습니다 (TxGNN 점수 99.18%, 근거 수준 L1, 권고 Proceed with Guardrails).

- 다만 Obinutuzumab은 이미 여포성 림프종에 허가되어 있습니다. 이 항목은 새로운 재창출이 아니라 기존 적응증을 확인하는 성격입니다.
- 이 약물의 임상시험은 총 40건이 넘으며, 아래는 대표 시험입니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT05100862](https://clinicaltrials.gov/study/NCT05100862) | Phase 3 | 진행 중(모집 종료) | 799 | 재발/불응성 FL에서 zanubrutinib+항CD20 항체 vs lenalidomide+rituximab 비교 |
| [NCT03817853](https://clinicaltrials.gov/study/NCT03817853) | Phase 4 | 완료 | 114 | 미치료 진행성 FL에서 Obinutuzumab 단축 주입(SDI)의 안전성 평가 |
| [NCT02871219](https://clinicaltrials.gov/study/NCT02871219) | Phase 2 | 완료 | 96 | 미치료 FL에서 Obinutuzumab+lenalidomide |
| [NCT00825149](https://clinicaltrials.gov/study/NCT00825149) | Phase 1 | 완료 | 137 | CD20+ FL에서 Obinutuzumab과 CHOP/FC/bendamustine 병용의 안전성·효능 |

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [29856692](https://pubmed.ncbi.nlm.nih.gov/29856692/) | 2018 | RCT (GALLIUM) | J Clin Oncol | 미치료 FL에서 Obinutuzumab이 rituximab보다 무진행 생존 기간을 유의하게 연장하였으며, 화학요법 종류에 따른 효능·안전성 분석 |
| [37404773](https://pubmed.ncbi.nlm.nih.gov/37404773/) | 2023 | RCT (GALLIUM 최종) | HemaSphere | 미치료 FL/MZL에서 Obinutuzumab 기반 vs rituximab 기반 면역화학요법 최종 결과 |
| [37506346](https://pubmed.ncbi.nlm.nih.gov/37506346/) | 2023 | RCT (ROSEWOOD) | J Clin Oncol | 재발/불응성 FL에서 zanubrutinib+Obinutuzumab vs Obinutuzumab 단독 비교 |
| [31296423](https://pubmed.ncbi.nlm.nih.gov/31296423/) | 2019 | 2상 단일군 (GALEN) | Lancet Haematol | 재발/불응성 FL에서 Obinutuzumab+lenalidomide의 활성과 안전성 |
| [28976863](https://pubmed.ncbi.nlm.nih.gov/28976863/) | 2017 | 1차 치료 연구 | N Engl J Med | 미치료 진행성 FL에서 Obinutuzumab 기반 vs rituximab 기반 화학요법 비교 |

## 결론 및 다음 단계

**결정: Hold** (생식중심 이전 CLL/SLL 하위유형 기준)

**사유:**
기전상 타당하고 TxGNN 점수도 높지만, 이 하위유형을 직접 다룬 임상시험과 문헌이 없어 모델 예측에 그칩니다. 또한 CLL 전체는 이미 허가된 적응증이므로, 하위유형만 별도로 평가할 임상적 실익이 크지 않습니다.

**진행하려면 필요한 것:**
- 허가 적응증 본문 확인 (MFDS 허가 문서를 내려받아 CLL 허가 여부와 범위 확인)
- 허가사항의 경고·금기 내용 확보 (현재 안전성 심사를 진행할 수 없는 상태)
- 상세 작용 기전 데이터 보완 (DrugBank 조회)
- 이 하위유형을 포함한 CLL 임상시험·문헌의 하위군 분석 데이터 확인
- 여포성 림프종은 기존 허가 적응증의 근거 확인 수준이며, 투여 관련 반응, B형 간염 재활성화, PML, 혈구감소증, 감염에 대한 모니터링 계획이 필요합니다. 병용요법은 레지멘별로 개별 검증해야 합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

