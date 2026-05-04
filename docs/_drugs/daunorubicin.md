---
layout: default
title: Daunorubicin
parent: 僅模型預測 (L5)
nav_order: 198
evidence_level: L5
indication_count: 10
---

# Daunorubicin
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

# Daunorubicin: 급성 골수성 백혈병에서 급성 림프모구성 백혈병으로

---

## 한 문장 요약

Daunorubicin은 대표적인 안트라사이클린계 항암제로, 약리학적으로 급성 골수성 백혈병(AML) 치료의 핵심 성분으로 잘 알려져 있으나 현재 한국 MFDS 허가 이력은 없습니다.
TxGNN 모델은 **급성 림프모구성/림프구성 백혈병(Acute Lymphoblastic/Lymphocytic Leukemia, ALL)**에 효과가 있을 수 있다고 예측(예측 점수: **99.82%**)하며,
현재 **다수의 완료된 대규모 Phase 3 임상시험**이 ALL에서의 안트라사이클린 기반 치료를 뒷받침하고 있어 근거 수준은 **L1**에 해당합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 허가 이력 없음 (약리학적 기존 사용: 급성 골수성 백혈병) |
| 예측 신규 적응증 | 급성 림프모구성/림프구성 백혈병 (ALL) |
| TxGNN 예측 점수 | 99.82% |
| 근거 수준 | L1 |
| 한국 시판 현황 | 미상시 |
| 허가증 수 | 0건 |
| 권장 결정 | Go |

---

## 이 예측이 타당한 이유는?

Daunorubicin은 안트라사이클린계 항생제로, DNA 이중나선에 삽입(intercalation)되어 **Topoisomerase II를 억제**함으로써 DNA 복제 및 전사를 방해하고 암세포의 자멸사를 유도합니다. 더불어 활성산소종(ROS) 생성을 통한 추가적인 세포독성 효과도 발휘합니다. 본 Evidence Pack에 상세한 MOA 데이터가 기재되어 있지 않으나, 이 기전은 문헌상 수십 년간 축적된 근거를 가진 확립된 사실입니다.

AML과 ALL은 공통적으로 빠르게 증식하는 미성숙 조혈세포에서 기원하는 급성 백혈병입니다. 안트라사이클린계 약물은 분열 중인 세포에 강력한 세포독성을 나타내므로, AML에 효과적인 Daunorubicin이 ALL 세포에도 동일한 기전으로 작용할 수 있습니다. 두 질환 모두 빠른 세포 분열이 핵심 병리이므로 기전상 연관성이 매우 높습니다.

실제로 국제 표준 ALL 치료 프로토콜인 **BFM, GMALL, DFCI, COG** 프로토콜 등 다수의 지침에서 Daunorubicin이 유도화학요법의 구성 성분으로 포함되어 있습니다. NCT01540812 프로토콜은 성인 ALL 치료에서 "daunorubicin 용량 감량"을 직접 언급하고 있으며, NCT01990807는 고위험 소아 ALL 공고화학요법에 Daunorubicin(D)을 명시적으로 포함합니다. TxGNN의 높은 예측 점수는 이미 임상에서 확립된 근거를 지식 그래프가 재확인한 결과로 해석할 수 있으며, 이는 모델의 높은 예측 신뢰도를 방증합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01190930](https://clinicaltrials.gov/study/NCT01190930) | Phase 3 | 모집 종료(진행 중) | 9,350 | 표준위험 B-ALL 소아·청소년 대상 위험도 적응형 복합화학요법 비교 연구 |
| [NCT02883049](https://clinicaltrials.gov/study/NCT02883049) | Phase 3 | 모집 종료(진행 중) | 5,949 | 고위험 B-ALL 소아 대상 복합화학요법; Ph-like TKI 민감 변이 층 포함 |
| [NCT01117441](https://clinicaltrials.gov/study/NCT01117441) | Phase 3 | 완료 | 6,136 | 소아·청소년 ALL 대상 국제 협력 치료 프로토콜(AIEOP-BFM ALL 2009), 복합화학요법 비교 |
| [NCT00002514](https://clinicaltrials.gov/study/NCT00002514) | Phase 3 | 완료 | 1,929 | ALL 1차 완전관해 달성 후 자가/동종 줄기세포이식 vs. 강화 표준화학요법 무작위 비교 |
| [NCT00613457](https://clinicaltrials.gov/study/NCT00613457) | Phase 3 | 완료 | 2,039 | 소아 ALL 복합화학요법 비교 연구(AIEOP LLA 2000), 최적 유도화학요법 규명 |
| [NCT01540812](https://clinicaltrials.gov/study/NCT01540812) | N/A | 완료 | 418 | 성인 고위험 ALL 치료 최적화; PEG-ASP 도입 및 **daunorubicin 용량 조정** 명시 포함 |
| [NCT01990807](https://clinicaltrials.gov/study/NCT01990807) | Phase 4 | 알 수 없음 | 20 | 소아 고위험 ALL 공고화학요법에 **Daunorubicin(D)** 명시적 포함 (VCR + Dauno + L-Asp + Dexa 병용) |
| [NCT01230983](https://clinicaltrials.gov/study/NCT01230983) | Phase 3 | 완료 | 573 | T세포 ALL 및 림프모구성 림프종 강화치료; Dexrazoxane 병용 및 고용량 MTX 여부 무작위 배정 |
| [NCT02042690](https://clinicaltrials.gov/study/NCT02042690) | Phase 3 | 완료 | 131 | 표준위험 성인 ALL(18~39세) 1차 완전관해 후 반일치 HSCT vs. 화학요법 비교 |
| [NCT00671034](https://clinicaltrials.gov/study/NCT00671034) | Phase 3 | 완료 | 166 | 고위험 ALL에서 calaspargase pegol vs. pegaspargase 복합화학요법 비교 |

---

## 문헌 근거

현재 해당 적응증(ALL)에 대한 관련 PubMed 문헌이 수집되지 않았습니다.

---

## 한국 시판 정보

현재 한국 MFDS에 등록된 Daunorubicin 허가 이력이 없습니다.

---

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 — 안트라사이클린계 (Topoisomerase II 억제제 / DNA 삽입제) |
| 골수억제 위험 | **고도** — 호중구감소증, 혈소판감소증, 빈혈 빈번 발생; G-CSF 예방적 사용 고려 |
| 심독성 위험 | **고도** — 누적 용량 의존적 심근병증·울혈성 심부전; 최대 누적 용량 관리 필수 |
| 구토 유발성 등급 | 중등도~고도 |
| 모니터링 항목 | CBC (분획 포함), 심초음파/좌심실박출률(LVEF), 간기능, 신기능, 요산, 전해질 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필수 (보호장갑·가운·마스크 착용, 밀폐 시스템 사용 권장) |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Go**

**사유:**
Daunorubicin의 ALL 치료 활성은 TxGNN 예측 이전에 이미 수십 년간 국제 표준 치료 프로토콜(BFM, GMALL, DFCI, COG 등)에 확립된 근거(L1)를 가지고 있으며, 완료된 대규모 Phase 3 임상시험(최대 n=9,350) 다수가 이를 뒷받침합니다. TxGNN 99.82%의 높은 예측 점수는 기존 임상 근거의 타당성을 재확인하는 결과입니다.

**진행하려면 필요한 것:**
- DrugBank MOA 데이터 보완 (DG002: 기전 분석 고도화를 위해 DrugBank API 조회)
- 한국 MFDS 허가사항 정보 확보 및 허가 신청 경로 검토 (DG001: 현재 미상시)
- 심독성 모니터링 프로토콜 수립 (누적 용량 한계 설정, 기저 심기능 평가 포함)
- 한국 내 Daunorubicin 제품 공급 가능성 및 도입 경로 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

