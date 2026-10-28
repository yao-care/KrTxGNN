---
layout: default
title: Fluoxetine
parent: 모델 예측만 (L5)
nav_order: 360
evidence_level: L5
indication_count: 9
monitor_inn: "Fluoxetine"
predicted_indications: ["paranoid personality disorder", "histrionic personality disorder (disease)", "schizotypal personality disorder", "schizoid personality disorder", "benign paroxysmal torticollis of infancy", "agoraphobia", "manic bipolar affective disorder", "phobic disorder", "Ohdo syndrome and variants"]
last_modified_at: 2026-10-23
description: "Fluoxetine: 예측 신규 적응증 편집성 인격장애 (Paranoid Personality Disorder) (근거 수준 L5). 기존 적응증: 확인 불가 (허가증에 적응증 본문 없이 허가사항 PDF 링크만 있음)"
---

# Fluoxetine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **9** 건
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

## Fluoxetine: 기존 허가 적응증에서 편집성 인격장애(Paranoid Personality Disorder)로
{: .text-alpha }

## 한 문장 요약

Fluoxetine은 한국에서 단일 성분 제제로 다수 허가되어 시판 중인 약물입니다. 다만 이번 보고서에 사용된 데이터에는 허가 적응증의 본문이 없고 허가사항 PDF 링크만 있습니다.
TxGNN 모델은 **편집성 인격장애(Paranoid Personality Disorder)**에 효과가 있을 수 있다고 예측하며 예측 점수는 매우 높습니다(0.9992).
그러나 이 질환을 직접 다룬 임상시험은 없고, 문헌 7편도 대부분 다른 질환이나 인격장애 전반을 다루므로 **직접적인 근거는 확인되지 않습니다.**

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가증에 적응증 본문 없이 허가사항 PDF 링크만 있음) |
| 예측 신규 적응증 | 편집성 인격장애 (Paranoid Personality Disorder) |
| TxGNN 예측 점수 | 0.9992 |
| 근거 수준 | L5 (이 질환을 직접 연구한 임상시험·문헌 없음) |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가 건수 | 최소 20건 (단일 성분 품목허가, 목록은 일부일 수 있음) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 Fluoxetine은 세로토닌 재흡수를 억제하는 약물(SSRI)로 알려져 있습니다. 세로토닌 조절이 충동성, 불안, 동반 우울 증상에 영향을 줄 가능성은 있습니다.

그러나 편집성 인격장애 같은 A군(Cluster A) 인격장애의 핵심 증상이 SSRI의 확립된 치료 표적이라는 근거는 이번 데이터에서 확인되지 않습니다. 수집된 문헌은 대부분 경계성 인격장애, 동반 우울증, 기타 질환을 다루고 있습니다. A군 인격장애 약물치료 리뷰(PMID 29955451)도 Fluoxetine의 편집성 인격장애 효능을 입증하지는 않습니다.

따라서 이 예측은 높은 모델 점수에 비해 기전적·임상적 뒷받침이 부족한 계산 기반 예측으로 보아야 합니다. 이득이 있다 해도 동반 우울증을 통한 간접적인 효과일 가능성이 큽니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [29955451](https://pubmed.ncbi.nlm.nih.gov/29955451/) | 2016 | Review | The Mental Health Clinician | 편집성·분열성·분열형 인격장애를 포함한 A군 인격장애의 약물치료 리뷰. Fluoxetine의 편집성 인격장애 효능을 확립하지는 않음 |
| [36853245](https://pubmed.ncbi.nlm.nih.gov/36853245/) | 2023 | Review | JAMA | 경계성 인격장애 리뷰. 편집성 인격장애와 직접 관련 없음 |
| [12524634](https://pubmed.ncbi.nlm.nih.gov/12524634/) | 2003 | Cohort | Comprehensive Psychiatry | 우울증 환자 183명 대상 Fluoxetine·Nortriptyline 장기 치료 시험 중 경계성 인격장애 하위군 분석. 편집성 인격장애는 대상이 아님 |
| [12214786](https://pubmed.ncbi.nlm.nih.gov/12214786/) | 2002 | Review | Psychological Medicine | 우울증 외래환자에서 Fluoxetine 치료 전후 인격장애 진단 변화 평가. 우울 증상과의 관련성 중심 |
| [21371699](https://pubmed.ncbi.nlm.nih.gov/21371699/) | 2011 | Cohort | Comprehensive Psychiatry | 소아·청소년·성인 발병 우울증의 임상 특성 비교. 직접 관련성 낮음 |
| [17637578](https://pubmed.ncbi.nlm.nih.gov/17637578/) | 2000 | Cohort | CNS Spectrums | Clozapine으로 치료받는 편집형 조현병 환자의 사회불안과 병전 인격장애. 직접 관련성 낮음 |
| [26703328](https://pubmed.ncbi.nlm.nih.gov/26703328/) | 2016 | Review | J Dev Behav Pediatr | 다낭성 난소 증후군과 정신과 진단에 대한 사례 논의. 직접 관련성 낮음 |

## 한국 시판 정보

단일 성분 제제 허가가 최소 20건 확인되며, 전부 유효 상태입니다. 아래는 주요 5건이며 전체 목록은 일부일 수 있습니다. 허가 적응증은 본문 없이 허가사항 PDF 링크만 제공되어 요약할 수 없습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201907013 | 유니작캡슐20밀리그램 | 경질캡슐 | [허가사항 PDF 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201907013/EE) |
| 201500735 | 디프렌캡슐10mg | 캡슐 | [허가사항 PDF 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201500735/EE) |
| 201805198 | 플록센캡슐 | 경질캡슐 | [허가사항 PDF 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201805198/EE) |
| 199801099 | 푸로세틴캡슐 | 경질캡슐 | [허가사항 PDF 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199801099/EE) |
| 200700022 | 로랑캡슐10밀리그램 | 캡슐 | [허가사항 PDF 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200700022/EE) |

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 이 중 확인된 일부 항목은 다음과 같습니다.
  - **Major(중대)**: Bupropion, Lorcaserin, Diethylpropion, Dolasetron, Eliglustat, Palonosetron, Cisapride
  - **Moderate(중등도)**: Famotidine, Loperamide, Morphine, Acetylsalicylic acid(아스피린), Clarithromycin, Chlorpropamide 등

주요 경고와 금기 정보는 이번 데이터에 포함되어 있지 않으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 점수는 매우 높지만, 편집성 인격장애에서 Fluoxetine을 직접 평가한 임상시험이나 문헌이 없고 기전적 근거도 불충분합니다. 따라서 근거 수준은 L5이며, 현재 단계에서는 추가 개발을 진행할 수 없습니다.

**진행하려면 필요한 것:**
- 허가사항 PDF에서 기존 적응증, 경고, 금기 정보 확보 (현재 안전성 검토를 진행할 수 없는 상태)
- 작용 기전(MOA) 데이터 확보 (DrugBank 조회 등)
- 편집성 인격장애에서 Fluoxetine을 평가한 임상 연구 또는 체계적 문헌고찰 탐색
- 동일 데이터에서 근거가 상대적으로 더 많은 다른 예측 적응증(공포증, 광장공포증 등)과의 우선순위 비교
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

