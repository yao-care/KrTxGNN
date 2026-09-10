---
layout: default
title: Miglitol
parent: 僅模型預測 (L5)
nav_order: 479
evidence_level: L5
indication_count: 10
---

# Miglitol
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

이 작업은 주어진 템플릿에 따라 Evidence Pack으로부터 보고서를 생성하는 단순 콘텐츠 생성 작업으로, brainstorming/TDD/디버깅 등 프로세스 스킬이 적용되지 않습니다. 바로 보고서를 작성합니다.

데이터를 보면 TxGNN 예측 점수 상위 9건(stiff person syndrome, lipodystrophy 계열 등)은 임상시험·문헌 근거가 전무하며 evidence_level L5/Hold로, evidence pack 자체에 "당뇨병 동반질환 노드를 통한 간접 연결로 추정, 직접 기전 근거 없음"이라 명시되어 있습니다. 반면 순위 10위인 **제1형 당뇨병**만 실제 임상시험 1건(Phase 3)과 문헌 16편의 실질적 근거(L2, Proceed with Guardrails)를 갖추고 있어, 이를 대표 예측 적응증으로 채택해 보고서를 작성했습니다.

# Miglitol (미글리톨): 제2형 당뇨병에서 제1형 당뇨병 인슐린 병용요법으로

## 한 문장 요약

Miglitol(미글리톨)은 알파-글루코시다제 억제제로, 소장에서 이당류 분해를 늦춰 식후 혈당을 낮추는 기전으로 제2형 당뇨병 치료에 사용되어 온 약물입니다(단, 현재 한국 내 시판 허가 정보는 확인되지 않음). TxGNN 모델은 **제1형 당뇨병(Type 1 Diabetes Mellitus)**에서 인슐린 병용요법으로 효과가 있을 수 있다고 예측하며, 현재 **1건의 직접 관련 임상시험**과 **16편의 문헌**이 이 방향을 지지합니다.

> 참고: TxGNN 예측 점수 자체는 상위 9개 적응증(classic stiff person syndrome, 지방이영양증 계열 등)이 더 높았으나, 해당 항목들은 임상시험·문헌 근거가 전혀 없고(L5, Hold) evidence pack 상에서도 "당뇨병 동반질환 노드를 통한 지식그래프 간접 연결로 추정되며 직접적 약리 기전 근거는 없음"으로 명시되어 있어 이번 보고서에서는 제외했습니다. 실질적 근거를 갖춘 제1형 당뇨병 예측을 중심으로 평가합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 제2형 당뇨병 (식후 혈당 조절, α-glucosidase 억제제) — 국내 공식 허가 문서 기준 데이터 없음 |
| 예측 신규 적응증 | 제1형 당뇨병 (Type 1 Diabetes Mellitus) — 인슐린 병용요법 |
| TxGNN 예측 점수 | 99.60% |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

Miglitol은 α-glucosidase 억제제로, 소장 점막의 이당류 분해효소를 억제해 탄수화물의 흡수·분해를 지연시킴으로써 식후 혈당 상승을 완화합니다. 이 기전은 내인성 인슐린 분비에 의존하지 않는다는 점이 핵심입니다.

제1형 당뇨병 환자는 인슐린 치료를 받고 있음에도 식후 혈당 급상승이 잘 조절되지 않는 경우가 많습니다. Miglitol의 기전은 인슐린 분비 자극이 아니라 흡수 지연에 기반하므로, 인슐린이 거의 또는 전혀 분비되지 않는 제1형 당뇨병 환자에서도 이론적으로 작동 가능합니다. 실제로 1980년대부터 α-glucosidase 억제제를 인슐린 치료의 보조요법(adjunct)으로 병용한 다수의 임상 관찰 연구가 존재하며, 이는 기전적 타당성을 뒷받침합니다.

다만 이는 신규 적응증이라기보다 "인슐린 치료의 보조요법"에 가까운 포지셔닝이며, 최근 수십 년간 대규모 현대적 RCT가 이루어지지 않았다는 한계가 있습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00213109](https://clinicaltrials.gov/study/NCT00213109) | Phase 3 | 완료 | N/A | 인슐린 치료 중인 제1형 당뇨병 환자에서 Miglitol의 유효성 및 안전성을 평가한 공개 임상시험 |

**참고:** 검색된 나머지 6건(NCT02475499, NCT06449235, NCT02456428, NCT02476760, NCT01697592, NCT03492580)은 incretin계 약물·DPP-4 억제제·SGLT2 억제제 등 제2형 당뇨병 관련 시험으로, evidence pack 상 관련성 등급 C(miglitol과 무관 또는 검색 오매칭)로 평가되어 제외했습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [24843410](https://pubmed.ncbi.nlm.nih.gov/24843410/) | 2010 | Cohort/Clinical Study | Journal of diabetes investigation | 제1형 당뇨병 환자에서 miglitol과 인슐린 병용요법 효과 |
| [21869539](https://pubmed.ncbi.nlm.nih.gov/21869539/) | 2011 | Cohort/Clinical Study | Endocrine journal | 강화 인슐린요법 병용 시 miglitol이 혈당조절과 인크레틴 반응에 미치는 영향 |
| [2060451](https://pubmed.ncbi.nlm.nih.gov/2060451/) | 1991 | Clinical Trial | Diabetes care | 제1형 당뇨병에서 α-glucosidase 억제가 식후 혈당내성 및 인슐린 투여 시점에 미치는 영향 |
| [3130257](https://pubmed.ncbi.nlm.nih.gov/3130257/) | 1988 | Clinical Trial | European journal of clinical investigation | 인슐린 의존형 당뇨병에서 신규 α-glucosidase 억제제 2종의 장기 투여 효과 |
| [3286168](https://pubmed.ncbi.nlm.nih.gov/3286168/) | 1988 | Clinical Trial | Diabetes research and clinical practice | IDDM 환자에서 α-glucosidase 억제와 식전 인슐린 투여 시점 조절 |
| [2663321](https://pubmed.ncbi.nlm.nih.gov/2663321/) | 1989 | Clinical Trial | Diabetes research | Miglitol과 위약의 단일맹검 비교, 식후 고혈당 감소 확인 |
| [3311550](https://pubmed.ncbi.nlm.nih.gov/3311550/) | 1987 | Clinical Trial | Clinical pharmacology and therapeutics | 신규 α-glucosidase 억제제가 IDDM에서 식사 시 인슐린 요구량을 감소시킴 |
| [3277827](https://pubmed.ncbi.nlm.nih.gov/3277827/) | 1988 | Clinical Trial | Diabetes research and clinical practice | 인슐린 의존형 당뇨병 환자에서 신규 α-glucosidase 억제제 2종의 효과 |
| [2180090](https://pubmed.ncbi.nlm.nih.gov/2180090/) | 1990 | Clinical Trial | South African medical journal | IDDM 환자에서 glucosidase 억제의 식후 혈당 급상승 억제 효과 |
| [3520133](https://pubmed.ncbi.nlm.nih.gov/3520133/) | 1986 | Clinical Trial | Klinische Wochenschrift | IDDM 환자에서 신규 α-glucosidase 억제제 2종이 혈당조절에 미치는 효과 |

## 한국 시판 정보

Miglitol은 현재 한국 내 시판 허가 건수가 0건으로 확인되어(미시판), 제출된 허가 정보가 없습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
제1형 당뇨병 환자를 대상으로 한 Phase 3 공개 임상시험 1건과 1980~2010년대에 걸친 다수의 관찰·임상연구가 인슐린 병용요법으로서의 효과를 뒷받침하며, 기전(흡수 지연, 인슐린 비의존적)도 합리적입니다. 다만 최근 대규모 현대적 RCT가 부재하고, 국내 미시판 상태이며, 안전성·기전 데이터에 Blocking 등급의 갭이 있어 즉시 진행보다는 가드레일을 갖춘 진행이 적절합니다.

**진행하려면 필요한 것:**
- TFDA/식약처 등 규제기관의 공식 허가사항(경고, 금기, DDI) 확보 — Blocking 데이터 갭(DG001)
- DrugBank API를 통한 공식 MOA 데이터 확인 — High 데이터 갭(DG002)
- 최근 10년 내 대규모 RCT 부재 — 현대적 검증 임상시험 추가 필요
- 국내 미시판 상태이므로 신규 허가 신청 경로 및 인슐린 병용요법으로서의 적응증 확대 가능성 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

