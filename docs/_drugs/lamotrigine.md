---
layout: default
title: Lamotrigine
parent: 모델 예측만 (L5)
nav_order: 456
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-25
description: "Lamotrigine: 예측 신규 적응증 삼차신경 종양 (trigeminal nerve neoplasm) (근거 수준 L5). 기존 적응증: 1. 간질(뇌전증) 1) 단독요법 및 부가요법 : 부분발작 및 전신 강직간대발작 2) 부가요법 :…"
monitor_inn: "LAMOTRIGINE"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia"]
---

# Lamotrigine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **2** 건
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

## 라모트리진: 뇌전증에서 삼차신경 종양으로
{: .text-alpha }

## 한 문장 요약

라모트리진(Lamotrigine)은 나트륨 채널을 차단하는 항경련제로, 원래 뇌전증 치료에 쓰이는 약입니다.
TxGNN 모델은 **삼차신경 종양(trigeminal nerve neoplasm)**에 효과가 있을 수 있다고 예측하지만, 이 적응증을 직접 뒷받침하는 **임상시험은 0건**이고 연결된 **문헌 2편**도 종양 치료와 무관합니다. 이 예측은 모델 점수만 있는 수준(L5)입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 간질(뇌전증) 1) 단독요법 및 부가요법 : 부분발작 및 전신 강직간대발작 2) 부가요법 : 레녹스-가스토 증후군에 의한 발작 2. 양극성 1형 장애 환자에서의 우울삽화의 재발 방지 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200706333/EE)) |
| 예측 신규 적응증 | 삼차신경 종양 (trigeminal nerve neoplasm) |
| TxGNN 예측 점수 | 0.9997 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Lamotrigine 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “라모트리진이 항경련 작용을 나타내는 정확한 기전은 알려져 있지 않다. 항경련 활성을 검출하기 위해 고안된 동물 모델에서, 라모트리진은 최대 전기충격(MES) 시험 및 펜틸렌테트라졸(scMet) 시험에서 발작 확산을 예방하는 데 효과적이었으며, 항뇌전증 활성에 대한 시각 및 전기 유발 후방전(EEAD) 시험에서 발작을 예방하였다.” 영어 원문: "The precise mechanism(s) by which lamotrigine exerts its anticonvulsant action are unknown. In animal models designed to detect anticonvulsant activity, lamotrigine was effective in preventing seizure spread in the maximum electroshock (MES) and pentylenetetrazol (scMet) tests, and prevented seizures in the visually and electrically evoked after-discharge (EEAD) tests for antiepileptic activity." ([DailyMed: Lamotrigine Kit (lamotrigine) prescribing information, OWP Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=474fb321-575c-4b97-9dbe-080061652ee4), 버전 2026-10-12; 확인일 2026-11-19). 알려진 정보에 따르면 라모트리진은 전압 의존성 나트륨 채널을 차단하고 글루탐산 방출을 줄여 신경 과흥분을 가라앉히는 항경련제입니다. 이 기전은 신경병증성 통증에는 적용될 수 있습니다.

다만 이 예측의 높은 점수는 TxGNN 모델(딥러닝)이 **삼차신경통(trigeminal neuralgia)** 등 관련 질환 사이에서 학습한 유사성을 반영한 것일 수 있으며, 생물학적 근거는 아닙니다. 삼차신경통은 신경의 과흥분성 질환이지 종양이 아닙니다. 라모트리진이 신생물에 작용한다는 근거는 없으며, 연결된 문헌 두 편도 삼차신경통과 해면상 기형(방사선 수술)을 다룬 것으로 종양 치료와는 무관합니다. 따라서 기전상의 타당성은 낮다고 판단합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurother | 삼차신경통의 내과적·외과적 치료 개관. 종양 치료가 아닌 신경통 관리에 관한 내용 |
| [30650431](https://pubmed.ncbi.nlm.nih.gov/30650431/) | 2018 | Case report | Stereotact Funct Neurosurg | 해면상 기형에 의한 삼차신경통을 감마나이프로 치료한 증례. 라모트리진·종양과 무관 |

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 200706333 | 라미아트정50밀리그램(라모트리진) | 엷은 황갈색의 정방형 정제 | (주)대웅제약 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200706333/EE) | 유효 |
| 200209641 | 라믹탈정25밀리그램,50밀리그램,100밀리그램(라모트리진) | 엷은 황갈색의 정방형 정제 | (주)글락소스미스클라인 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200209641/EE) | 유효 |
| 200603850 | 라믹탈츄어블정5밀리그램(라모트리진) | 흰색 내지 회백색의 장방형 정제 | (주)글락소스미스클라인 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200603850/EE) | 유효 |
| 201200435 | 테바라모트리진츄어블정50밀리그램 | 한 면에 50, 다른 면에 DLT가 새겨진 흰색의 원형 저작 또는 분산정 | (주)한독테바 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201200435/EE) | 유효 |
| 201001684 | 라모스탈정50밀리그램(라모트리진) | 엷은 황갈색의 사각형 정제 | 명인제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201001684/EE) | 유효 |

위 표는 허가 최소 20건 중 5건입니다.

<!-- licenses:end -->

## 안전성 고려사항

허가사항의 경고·금기 문구는 이번 자료에 포함되지 않았으므로 허가사항을 직접 참조하세요.

- **지식 그래프 기반 금기 관련 질환** (허가 문구가 아니라 TxGNN 지식 그래프의 약물-질환 금기 연결 정보): 불안장애, 신경증, 기분부전장애, 간질환, 담낭질환, 혈소판감소증, 호중구감소증, 무과립구증, 빈혈, 범혈구감소증, 재생불량성 빈혈, 비감염성 수막염
- **약물 상호작용**: 조회된 상호작용은 총 100건이며, 이 중 확인된 주요 항목은 다음과 같습니다.
  - 중등도(Moderate): 모르핀(리포솜 제형 포함), 아편, 드로나비놀, 나빌론, 메토클로프라미드, 오를리스타트
  - 경미(Minor): 메트포르민
  - 등급 미상: 글리메피리드, 로시글리타존, 오메프라졸, 판토프라졸 등

## 결론 및 다음 단계

**결정: Hold**

**사유:**
삼차신경 종양에 대한 임상시험이 없고, 연결된 문헌도 종양 치료와 무관해 모델 예측 외의 근거가 없습니다. 높은 점수는 TxGNN 모델(딥러닝)이 삼차신경통 등 관련 질환 사이에서 학습한 유사성을 반영한 것일 수 있으며, 생물학적 근거는 아닙니다.

**진행하려면 필요한 것:**
- 삼차신경 종양에서 라모트리진의 항종양 또는 증상 완화 효과를 직접 다룬 전임상·임상 근거
- 허가사항(경고·금기)과 허가 적응증 원문 확보
- 상세한 작용 기전 데이터

**참고:**
같은 모델이 예측한 **삼차신경통**(2위, 점수 0.9989)에는 완료된 임상시험 2건이 있습니다. NCT00203229는 위약 대조 이중맹검 추가요법 시험으로 20명이 참여했고, NCT00913107은 카바마제핀과 비교한 2/3상 시험으로 21명이 참여했습니다. 두 시험 모두 규모가 작습니다. 이 적응증은 유럽신경학회(EAN) 지침에서 대안·추가 요법으로 언급되므로, 재창출 검토는 삼차신경통 쪽에서 우선 진행하는 것이 합리적입니다.

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Lamotrigine Kit (lamotrigine) prescribing information, OWP Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=474fb321-575c-4b97-9dbe-080061652ee4) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

