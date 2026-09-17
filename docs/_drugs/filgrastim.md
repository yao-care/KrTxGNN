---
layout: default
title: Filgrastim
parent: 모델 예측만 (L5)
nav_order: 323
evidence_level: L5
indication_count: 10
---

# Filgrastim
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

# Filgrastim: 적응증 미상에서 혈소판 원발성 방출 장애로

## 한 문장 요약

Filgrastim은 재조합 인간 과립구 콜로니 자극인자(G-CSF)이며, 이번 Evidence Pack에는 한국 허가 정보와 기존 적응증 데이터가 없어 정확한 기존 용도를 확인할 수 없습니다.
TxGNN 모델은 **혈소판 원발성 방출 장애(Primary Release Disorder of Platelets)**에 효과가 있을 수 있다고 예측(점수 99.9976%)하지만, 현재 **14건의 임상시험**과 **1편의 문헌**이 발견되었을 뿐이며 이들 대부분은 질환 자체를 표적으로 한 근거가 아니라 조혈모세포이식의 지지요법(幹細胞동원) 맥락에서 filgrastim이 부수적으로 사용된 사례입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (한국 허가 이력 없음, licenses 0건) |
| 예측 신규 적응증 | 혈소판 원발성 방출 장애 (Primary Release Disorder of Platelets) |
| TxGNN 예측 점수 | 99.9976% (rank 168) |
| 근거 수준 | L4 (단, 아래 참조 — 질환 특이적 직접 근거는 부재) |
| 한국 시판 현황 | ✗ 미판매 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 Filgrastim의 상세한 작용 기전(MOA) 데이터는 확보되지 않았습니다(Data Gap, High severity — DrugBank 조회 필요).

다만 Evidence Pack에 포함된 기전 분석(repurposing rationale)에 따르면, Filgrastim은 G-CSF 수용체(G-CSFR)를 통해 과립구(호중구) 전구세포의 증식·분화 및 말초혈 조혈모세포 동원에 작용하는 약물로, 혈소판 생성이나 혈소판 과립(dense granule/α-granule) 방출 경로에 작용한다는 알려진 근거는 없습니다.

TxGNN의 높은 예측 점수는 "조혈모세포이식" 임상 맥락에서 filgrastim과 혈소판 관련 질환 노드가 함께 자주 등장하는 데이터 패턴(node co-occurrence)에서 기인했을 가능성이 높으며, 실제 기전적 연관성을 반영한 것이 아닐 수 있습니다. 즉, 이번 예측은 지식그래프 임베딩의 인공물(artifact)일 가능성을 배제할 수 없습니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02646098](https://clinicaltrials.gov/study/NCT02646098) | Phase 2 | 완료 | 64 | 외투세포/미만성거대B세포림프종 자가이식 시 CD34+ 선별 vs 비선별 비교. filgrastim은 줄기세포 동원 지지요법으로만 사용, 질환 직접 치료 근거 아님 (관련성 낮음) |
| [NCT04047628](https://clinicaltrials.gov/study/NCT04047628) | Phase 3 | 모집 중 | 156 | 치료저항성 재발형 다발경화증에서 자가조혈모세포이식 vs 최선 가용치료 비교. 혈소판 방출 장애와 직접 관련 없음 |
| [NCT01503918](https://clinicaltrials.gov/study/NCT01503918) | Phase 2 | 완료 | 124 | 중환자실 환자의 CMV 재활성화 항바이러스 예방. 이식 지지요법 맥락, 질환 무관 |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Phase 2 | 완료 | 60 | 고위험 재발성 소아 육종 이식 예비연구. 질환 직접 관련 없음 |
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Phase 1/2 | 완료 | 147 | 혈액암 비清髓 동종이식 연구. 질환 직접 관련 없음 |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Phase 1/2 | 모집 중 | 260 | 이식편대숙주병(GVHD) 예방 요법 최적 용량 연구, filgrastim 관련성 미평가 |
| [NCT04540120](https://clinicaltrials.gov/study/NCT04540120) | Phase 2 | 중단 | 49 | COVID-19 사이토카인 방출 증후군 치료제 연구, filgrastim 관련성 미평가 |
| [NCT01335932](https://clinicaltrials.gov/study/NCT01335932) | Phase 2 | 완료 | 160 | 급성 폐손상/호흡부전에서 CMV 재활성화 예방, filgrastim 관련성 미평가 |
| [NCT00923364](https://clinicaltrials.gov/study/NCT00923364) | Phase 2 | 완료 | 19 | GATA2 돌연변이 환자 감축강도 조혈모세포이식, filgrastim 관련성 미평가 |
| [NCT00354172](https://clinicaltrials.gov/study/NCT00354172) | Phase 2 | 중단 | 16 | 골수성백혈병 제대혈 이식 연구, filgrastim 관련성 미평가 |

※ 위 시험 중 사전 평가가 완료된 항목은 모두 "관련성 낮음(Grade C)"으로 분류되었으며, 나머지는 관련성 미평가(pending) 상태입니다. 질환을 직접 치료 목적으로 한 시험은 확인되지 않았습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [29770133](https://pubmed.ncbi.nlm.nih.gov/29770133/) | 2018 | Review | Frontiers in Immunology | 건강한 공여자 대상 G-CSF 매개 말초혈 줄기세포 동원 시 림프구 아형의 우선적 동원에 관한 리뷰. 혈소판 방출 장애에 대한 직접 근거는 아님 |

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 예측 점수(99.9976%)는 높지만, 발견된 임상시험 14건은 모두 조혈모세포이식의 지지요법 맥락에서 filgrastim이 사용된 사례일 뿐, 혈소판 원발성 방출 장애를 표적으로 한 근거가 아닙니다.
- G-CSF/G-CSFR 경로는 과립구 계열에 작용하며, 혈소판 생성·과립 방출 경로와의 알려진 기전적 연관성이 없습니다.
- 나머지 9개 예측 적응증(pseudo-von Willebrand disease, Glanzmann thrombasthenia, Scott syndrome 등) 역시 관련 임상시험·문헌이 전무하거나(L5) 유사한 기전 무관성이 확인되어, 전체 예측군의 신뢰도가 낮습니다.

**진행하려면 필요한 것:**
- Filgrastim 작용 기전(MOA) 데이터 확보 (DrugBank API 조회, High severity)
- 한국 허가사항의 경고·금기 정보 확보 (현재 Blocking 등급 Data Gap — S1 안전성 초평가 진행 불가)
- 혈소판 생성/방출 경로와 G-CSF 축의 직접적 연관성을 뒷받침할 전임상 또는 기전 연구
- 질환을 직접 표적으로 한 임상시험 등록 여부 지속 모니터링
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

