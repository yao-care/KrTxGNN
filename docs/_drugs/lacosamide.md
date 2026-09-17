---
layout: default
title: Lacosamide
parent: 모델 예측만 (L5)
nav_order: 419
evidence_level: L5
indication_count: 10
---

# Lacosamide
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

# Lacosamide: 뇌전증에서 양극성 정동장애 조증삽화로

## 한 문장 요약

Lacosamide(Vimpat®)는 원래 국소발작(부분발작) 뇌전증 치료제로 개발된 항경련제입니다.
TxGNN 모델은 **양극성 정동장애 조증삽화(Manic Bipolar Affective Disorder)**에 효과가 있을 수 있다고 예측하며,
현재 **1건의 3상 임상시험(모집 중)**과 **14편의 관련 문헌**이 이 방향을 뒷받침하지만, 아직 확증적 결과는 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 뇌전증(국소발작) — 한국 미시판으로 허가 자료 없음, 임상시험 문헌상 언급되는 국제 정보 기준 |
| 예측 신규 적응증 | 양극성 정동장애 조증삽화 (Manic Bipolar Affective Disorder) |
| TxGNN 예측 점수 | 99.96% |
| 근거 수준 | L3 (관찰 연구/후향적 코호트 수준) |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold (Research Question 단계) |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 확보되지 않았습니다(DrugBank 조회 결과 [Data Gap]).
다만 공개된 약리학 정보에 따르면, Lacosamide는 전위-개폐형 나트륨 채널(voltage-gated sodium channel)의
느린 불활성화(slow inactivation)를 선택적으로 증강시켜 신경세포의 과흥분을 억제하는 항경련제입니다.

같은 나트륨 채널 차단 기전을 가진 다른 항경련제(lamotrigine, carbamazepine 등)는 이미 임상에서
기분안정제(mood stabilizer)로 사용되고 있어, 기전상 유사한 방식으로 양극성장애에도 적용 가능할 수 있습니다.
또한 Lacosamide는 CRMP-2 단백질과 결합하는데, 이 단백질은 신경가소성 및 여러 정신질환 병리와 관련이
있다고 보고되어 있습니다(PMID 32693579). 다만 이는 추론적 연결이며 양극성장애에 특이적인 기전 증거는 아닙니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT07412132](https://clinicaltrials.gov/study/NCT07412132) | Phase 3 | 모집 중 | 40 | 양극성장애 I/II형의 중등도~중증 주요우울 삽화에서 1차/2차 약물치료에 Lacosamide를 부가요법으로 추가했을 때의 효능·안전성·내약성을 평가하는 무작위·이중맹검·병렬군 시험. 관찰연구 및 개방표지 연구에서 우울/조증 증상 개선 가능성이 시사된 데 근거함 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [30251375](https://pubmed.ncbi.nlm.nih.gov/30251375/) | 2018 | 후향적 코호트 | Psychiatry Clin Neurosci | 뇌전증이 없는 양극성장애 환자 대상, 30일간 Lacosamide 효과를 다른 항경련제 치료군과 후향적으로 비교 |
| [33666402](https://pubmed.ncbi.nlm.nih.gov/33666402/) | 2021 | 개방표지 파일럿 시험 | J Clin Psychopharmacol | 양극성 우울증에서 Lacosamide의 12주 개방표지 효능·안전성 평가 |
| [28845834](https://pubmed.ncbi.nlm.nih.gov/28845834/) | 2017 | 증례 보고 | Acta Biomed | PTSD 및 전두측두엽 뇌전증 동반 기분장애 환자에서 Lacosamide로 임상적 안정화 달성 |
| [30275630](https://pubmed.ncbi.nlm.nih.gov/30275630/) | 2018 | 증례 보고(이상반응) | Indian J Psychol Med | 양극성장애·뇌전증 동반 환자에서 Lacosamide로 유발된 호중구감소증 사례 |
| [32693579](https://pubmed.ncbi.nlm.nih.gov/32693579/) | 2020 | 리뷰(기전) | ACS Chem Neurosci | CRMP2 단백질의 신경퇴행성/정신질환 치료 표적 가능성 고찰 (Lacosamide-CRMP2 결합 기전의 근거) |
| [29253680](https://pubmed.ncbi.nlm.nih.gov/29253680/) | 2018 | 전향적 다기관 연구 | Epilepsy Behav | 국소발작 뇌전증 환자에서 Lacosamide가 우울·불안 증상에 미치는 영향 평가 |
| [29957667](https://pubmed.ncbi.nlm.nih.gov/29957667/) | 2018 | 리뷰 | Ther Drug Monit | 항경련제의 치료약물모니터링 개관, 통증·양극성장애 등 타 적응증 활용 언급 |
| [38304661](https://pubmed.ncbi.nlm.nih.gov/38304661/) | 2024 | 증례 보고 | Cureus | 뇌전증/비뇌전증발작 동반 양극성장애 I형 임신 환자의 복합 관리 사례 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold (Research Question 단계)**

**사유:**
가장 관련성 높은 3상 임상시험(NCT07412132)이 이제 막 모집을 시작한 소규모(n=40) 시험이며,
그 외 근거는 후향적 코호트와 개방표지 파일럿 연구 수준(L3)에 그칩니다. 안전성 자료(경고, 금기, DDI)도
전혀 확보되지 않은 상태(모두 [Data Gap]/not_found)라 임상 적용을 판단하기에는 이릅니다.

**진행하려면 필요한 것:**
- TFDA 사용상 주의사항/금기 확보 (data gap DG001, Blocking) — 미확보 시 S1 안전성 초기평가 자체가 불가
- DrugBank MOA 상세 정보 확보 (data gap DG002)
- NCT07412132 3상 시험 결과 발표 대기
- 약물상호작용(DDI) 데이터베이스 재조회 (현재 query_status: not_found)

---

**참고:** 이번 Evidence Pack에는 Lacosamide에 대해 10개의 예측 적응증이 포함되어 있는데,
TxGNN 점수 순위(1위)와 별개로 **5순위 편두통(migraine disorder)**이 실제로는 가장 강한 근거를 보유하고 있습니다
(L1 수준, 완료된 3상 RCT 다수 포함, 권장 결정 Proceed with Guardrails). 우선순위 재검토 시 참고하시기 바랍니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

