---
layout: default
title: Granisetron
parent: 모델 예측만 (L5)
nav_order: 394
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-20
description: "Granisetron: 예측 신규 적응증 조증 양극성 정동장애 (manic bipolar affective disorder) (근거 수준 L5). 기존 적응증: (주사제) 성인 - 화학요법, 방사선요법으로 인한 구역 및 구토 - 수술 후 구역 및 구토 소아(2세…"
monitor_inn: "GRANISETRON"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "acute contagious conjunctivitis", "angioedema", "allergic urticaria", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "bronchitis", "cold urticaria", "conjunctivitis"]
---

# Granisetron
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

## Granisetron: 구토 억제에서 조증 양극성 정동장애로
{: .text-alpha }

## 한 문장 요약

Granisetron은 선택적 5-HT3 수용체 길항제로, 한국에서 주사제·정제·경피흡수제로 허가되어 시판 중입니다(허가된 적응증 원문은 이번에 정리된 데이터에서 확인되지 않았습니다).
TxGNN 모델은 **조증 양극성 정동장애(manic bipolar affective disorder)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 **임상시험은 0건**, **문헌도 0편**입니다.
따라서 이 예측은 모델 점수에만 의존하는 가설 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | (주사제) 성인 - 화학요법, 방사선요법으로 인한 구역 및 구토 - 수술 후 구역 및 구토 소아(2세 이상) - 화학요법으로 인한 구역 및 구토 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201109302/EE)) |
| 예측 신규 적응증 | 조증 양극성 정동장애 (manic bipolar affective disorder) |
| TxGNN 예측 점수 | 0.9962 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 8건 / 전체 9건) |
| 허가증 수 | 9건 (유효 8건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Granisetron 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “그라니세트론은 선택적 5-하이드록시트립타민 3(5-HT 3 ) 수용체 길항제로서, 5-HT 1, 5-HT 1A, 5-HT 1B/C, 5-HT 2를 포함한 다른 세로토닌 수용체, 알파 1-, 알파 2- 또는 베타-아드레날린 수용체, 도파민-D 2, 또는 히스타민-H 1, 벤조디아제핀, 피크로톡신 또는 오피오이드 수용체에 대해서는 친화도가 거의 또는 전혀 없다. 5-HT 3 형 세로토닌 수용체는 말초에서는 미주신경 말단에, 중추에서는 최후구역의 화학수용체 방아쇠 영역에 위치한다.” 영어 원문: "Granisetron is a selective 5-hydroxytryptamine 3 (5-HT 3 ) receptor antagonist with little or no affinity for other serotonin receptors, including 5-HT 1, 5-HT 1A, 5-HT 1B/C, 5-HT 2; for alpha 1-, alpha 2-, or beta-adrenoreceptors; for dopamine-D 2; or for histamine-H 1; benzodiazepine; picrotoxin or opioid receptors. Serotonin receptors of the 5-HT 3 type are located peripherally on vagal nerve terminals and centrally in the chemoreceptor trigger zone of the area postrema." ([DailyMed: Sustol (granisetron) prescribing information, Heron Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f7c7ffdd-8270-4030-bc1e-a1cb28a6de56), 버전 2026-04-30; 확인일 2026-11-19). 알려진 정보에 따르면 granisetron은 선택적 5-HT3 수용체 길항제이며, 단일 성분 제제로 8건이 유효하게 허가되어 있습니다.

조증에는 세로토닌과 도파민 조절 이상이 관여하는 것으로 알려져 있습니다. 5-HT3 길항 작용이 중뇌변연계 회로의 도파민 분비를 조절할 수 있다는 추측이 있어, 기전상 접근 가능성은 있습니다.

다만 이 연결 고리는 가설일 뿐이며 임상시험이나 문헌으로 검증되지 않았습니다. 근거는 TxGNN 예측 점수(0.9962)뿐입니다.

### 참고: 다른 예측 적응증

TxGNN은 아래 질환도 예측했으나, 모두 임상시험과 문헌 근거가 없는 L5 수준이며 권장 결정은 Hold입니다.

| 순위 | 질환 | 예측 점수 | 기전적 타당성 |
|-----|------|----------|-------------|
| 2 | 투렛 증후군 | 0.9952 | 도파민·세로토닌 이상과 관련되어 생물학적으로 그럴듯하나 입증되지 않음 |
| 7 | 발모벽 | 0.9923 | 강박 스펙트럼 장애로 세로토닌이 관여하며 그럴듯하나 입증되지 않음 |
| 5 | 알레르기성 두드러기 | 0.9932 | 가려움·비만세포 신호와 간접적이고 약한 연관 |
| 9 | 한랭 두드러기 | 0.9910 | 세로토닌 기여 가능성이 있으나 약함 |
| 4 | 혈관부종 | 0.9936 | 히스타민·브래디키닌 경로에 직접 작용하지 않아 추측 수준 |
| 3 | 급성 전염성 결막염 | 0.9949 | 뚜렷한 기전적 연결 없음, 네트워크 근접성에 따른 인공적 결과로 추정 |
| 10 | 결막염 | 0.9909 | 뚜렷한 기전적 연결 없음 |
| 6 | 신원성 항이뇨 부적절 증후군 | 0.9932 | V2 수용체 변이 질환으로 5-HT3와 무관, 이 점수는 TxGNN 모델(딥러닝)이 학습한 관련 질환 간 유사성을 반영할 수 있으며 생물학적 근거는 아님 |
| 8 | 기관지염 | 0.9918 | 뚜렷한 기전적 근거 없음 |

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201109302 | 카비그라니세트론주 | 주사제(앰플) | 허가사항 참조 |
| 201101800 | 카이세론주 | 주사제(앰플) | 허가사항 참조 |
| 200108802 | 카이트릴주 | 주사제(앰플) | 허가사항 참조 |
| 200108800 | 카이트릴정 1mg | 필름코팅정 | 허가사항 참조 |
| 200605345 | 카니트론주 | 주사제(앰플) | 허가사항 참조 |

이 밖에 카니트론정 1mg, 산쿠소패취(경피흡수제), 그라트릴주가 허가되어 있어 총 8건입니다.

## 안전성 고려사항

- **금기(지식그래프 기반 참고 정보, 허가 라벨 아님)**: QT 연장 증후군, 가족성 QT 연장 증후군, 칼륨 결핍증, 돌연 심장정지, 심장 전도 질환과 연관된 금기 관계가 지식그래프에 있습니다.
- **약물 상호작용**: 총 100건이 조회되었으며, 그중 일부를 아래에 정리했습니다.
  - **Major**: Fentanyl, Dextromethorphan, Tramadol, Alfentanil, Almotriptan, Sumatriptan, Amiodarone, Amisulpride, Amitriptyline, Anagrelide
  - **Moderate**: Abametapir, Abiraterone, Dihydrocodeine, Codeine, Famotidine, Formoterol, Adenosine, Salbutamol, Alfuzosin, Propofol
  - QT 연장 약물 및 세로토닌 작용 약물과의 병용에 특히 주의가 필요합니다.

그 외 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
조증 양극성 정동장애에 대한 예측은 TxGNN 점수(0.9962)에만 의존하며, 임상시험과 문헌이 모두 없는 L5 수준입니다. 또한 허가 라벨의 안전성 정보와 작용 기전 데이터가 없어 안전성 검토 단계로 진행할 수 없습니다.

**진행하려면 필요한 것:**
- 식약처(MFDS) 허가사항 확보 및 분석 (경고·금기·허가 적응증)
- DrugBank 등에서 상세 작용 기전(MOA) 데이터 확보
- 조증 및 5-HT3 길항제에 대한 전임상·임상 문헌 검색
- QT 연장 위험과 정신과 약물(항정신병약, 삼환계 항우울제 등) 병용 시 안전성 평가
- 투여 경로 적합성 검토 (현재 미확인)

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Sustol (granisetron) prescribing information, Heron Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f7c7ffdd-8270-4030-bc1e-a1cb28a6de56) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

