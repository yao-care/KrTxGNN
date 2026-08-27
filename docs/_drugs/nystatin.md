---
layout: default
title: Nystatin
parent: 僅模型預測 (L5)
nav_order: 317
evidence_level: L5
indication_count: 10
---

# Nystatin
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

# Nystatin: 칸디다증에서 외음질염(Vulvovaginitis)으로

## 한 문장 요약

Nystatin은 오래전부터 피부·점막의 칸디다(Candida) 진균 감염 치료에 사용되어 온 국소 항진균제입니다. TxGNN 모델은 **외음질염(Vulvovaginitis)**에도 효과가 있을 것으로 예측하며, 현재 등록된 관련 임상시험은 없지만 **20편의 문헌**이 이 방향을 지지합니다. 다만 이 예측은 완전히 새로운 가설이라기보다, Nystatin이 이미 임상 현장에서 오랫동안 사용해 온 용도(칸디다성 외음질염 치료)를 재확인하는 성격이 강합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 칸디다증(진균 감염) — 상세 승인 적응증 문구 자료 없음 |
| 예측 신규 적응증 | 외음질염 (Vulvovaginitis) |
| TxGNN 예측 점수 | 99.92% |
| 근거 수준 | L3 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 DrugBank 등에서 확보된 상세 작용 기전(MOA) 데이터는 없습니다. 다만 Evidence Pack 내 근거를 보면, Nystatin은 폴리엔(polyene)계 항진균제로서 *Candida albicans*의 세포막 완전성을 직접 파괴하는 방식으로 작용하는 것으로 알려져 있으며, 이는 병원체를 직접 표적하는 명확한 기전입니다.

외음질염은 세균성 질염 다음으로 흔한 질염 원인이며, 원인균의 85~90%가 *Candida albicans*입니다. 즉 기존에 알려진 칸디다증 치료 기전이 외음질염에도 그대로 적용되는 구조로, TxGNN 지식그래프 추론이라기보다는 실제 임상에서 이미 검증된 사용 패턴에 가깝습니다.

**참고:** Evidence Pack의 기전 근거(rationale)에도 "nystatin의 장기 임상 실무 용법이며, 완전히 새로운 노약재창출 가설은 아니다"라고 명시되어 있습니다. 따라서 이번 평가는 '신규 발견'보다는 '기존 용도의 재확인 및 근거 정리'로 이해하는 것이 정확합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [39771534](https://pubmed.ncbi.nlm.nih.gov/39771534/) | 2024 | Review | Pharmaceutics | 플루코나졸 내성 외음질염 관리 최신 동향, boric acid·nystatin·신규 항진균제 비교 |
| [25775428](https://pubmed.ncbi.nlm.nih.gov/25775428/) | 2015 | Review | BMJ Clinical Evidence | 외음질염 중 세균성 질염 다음으로 흔한 원인이 칸디다증(85~90%)임을 확인 |
| [21718579](https://pubmed.ncbi.nlm.nih.gov/21718579/) | 2010 | Review | BMJ Clinical Evidence | 칸디다성 외음질염 진단 및 치료 근거 정리 |
| [19454049](https://pubmed.ncbi.nlm.nih.gov/19454049/) | 2007 | Review | BMJ Clinical Evidence | 칸디다성 외음질염 역학 및 치료 근거 |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Review | J Women's Health | 재발성 외음질염에서 비-알비칸스 칸디다종의 항진균제 내성 증가 문제 |
| [20406393](https://pubmed.ncbi.nlm.nih.gov/20406393/) | 2011 | Cohort | Mycoses | 287건 칸디다 분리주 대상 fluconazole·nystatin 감수성과 임상 결과 상관성 분석 |
| [16047929](https://pubmed.ncbi.nlm.nih.gov/16047929/) | 2005 | Cohort/임상연구 | Ceska gynekologie | 질 nystatin 투여를 통한 혼합성 외음질염 진단 및 치료 평가 |
| [30359236](https://pubmed.ncbi.nlm.nih.gov/30359236/) | 2018 | 기전 연구(동물모델) | BMC Microbiology | Nystatin이 칸디다 감염에 대한 면역반응을 증강시키고 질 상피 초미세구조를 보호함을 확인 |
| [37023426](https://pubmed.ncbi.nlm.nih.gov/37023426/) | 2023 | 비교 연구 | J Infect Dev Ctries | 임신 중 외음질염에서 티트리오일과 nystatin의 억제 효과 비교 |
| [12228137](https://pubmed.ncbi.nlm.nih.gov/12228137/) | 2002 | Review | BMJ | 칸디다성 외음질염의 임상적 특징 및 표준 치료 정리 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
Nystatin의 외음질염(칸디다성) 치료 효과는 20편의 리뷰·코호트 문헌으로 뒷받침되지만, 이는 완전히 새로운 재창출 가설이 아니라 이미 임상에서 통용되는 용도의 재확인에 가깝습니다. 또한 한국에서는 현재 미시판 상태(허가증 0건)이므로, 임상적 타당성과 별개로 규제 측면의 진행 절차가 필요합니다.

**진행하려면 필요한 것:**
- 식약처(허가) 자료: 경고문·금기사항 확보 (현재 Blocking 데이터 갭)
- DrugBank 기반 상세 작용기전(MOA) 자료 보강 (현재 High 우선순위 데이터 갭)
- 한국 내 품목허가 신청 시 필요한 국내 임상/시판 계획 검토
- 약물상호작용(DDI) 데이터 추가 확인 (현재 조회 결과 없음)

---

**참고:** 같은 Evidence Pack에 포함된 나머지 예측 적응증(안와 부위 질환, 낭성 기형종, 척수 유피낭종, 폐경 후 위축성 질염, 비오틴 대사질환, 구각 누공, 하악골 방사선골괴사 등, 순위 2~10위)은 모두 임상시험·문헌 근거가 없고 기전상 연관성도 낮아 근거 수준 L5·**Hold**로 평가되었습니다. 이들은 TxGNN 임베딩 공간상의 간접 연결 가능성이 높아 추가 조사 우선순위가 낮습니다. 다만 순위 8위 "외음염(Vulvitis)"은 외음질염과 임상적으로 중첩되는 동일 계열 질환으로, 위 근거가 함께 적용될 수 있습니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

