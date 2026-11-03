---
layout: default
title: Clozapine
parent: 모델 예측만 (L5)
nav_order: 231
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-03
monitor_inn: "CLOZAPINE"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "trichotillomania", "bipolar disorder", "major affective disorder", "attention deficit-hyperactivity disorder", "attention deficit hyperactivity disorder, inattentive type", "Malan overgrowth syndrome"]
description: "Clozapine: 예측 신규 적응증 조증 양극성 정동장애 (manic bipolar affective disorder) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201804185/EE"
---

# Clozapine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **8** 건
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

## Clozapine: 조증 양극성 정동장애 (manic bipolar affective disorder)
{: .text-alpha }

## 한 문장 요약

Clozapine은 도파민·세로토닌·무스카린·아드레날린·히스타민 수용체를 폭넓게 차단하는 비정형 항정신병약입니다. TxGNN 모델은 **조증 양극성 정동장애(manic bipolar affective disorder)**에 효과가 있을 수 있다고 예측합니다(예측 점수 0.9995). 이 질환을 직접 다룬 완료된 2상 이중맹검 시험 **1건**과 임상 관련 문헌 다수가 이 방향을 지지하지만, 시험 규모는 작습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201804185/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200307798/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201804474/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201309789/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200307799/EE;  |
| 예측 신규 적응증 | 조증 양극성 정동장애 (manic bipolar affective disorder) |
| TxGNN 예측 점수 | 0.9995 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 6건 / 전체 6건) |
| 허가증 수 | 6건 (유효 6건) |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 수집되어 있지 않습니다. 다만 알려진 약리 특성으로는 D2/D4, 5-HT2A, 무스카린, 아드레날린, 히스타민 수용체에 대한 길항 작용이 있습니다. 이러한 광범위한 수용체 프로파일이 항조증 및 기분안정 효과에 기여할 수 있다고 봅니다. 특히 기존 치료에 반응하지 않거나 부작용으로 약을 견디지 못하는 조증 환자에게 의미가 있을 수 있습니다.

이 가설은 임상 근거로 뒷받침됩니다. 치료저항성 조증에서 clozapine을 평가한 2상 이중맹검 시험이 완료되었습니다. 또한 양극성 장애에서 clozapine의 효능과 이상반응을 검토한 체계적 문헌고찰·메타분석이 있습니다.

다만 근거는 소규모 시험(42명)과 문헌고찰에 의존합니다. 대규모 확증 시험은 아직 확인되지 않았습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00029458](https://clinicaltrials.gov/study/NCT00029458) | Phase 2 | 완료 | 42 | 치료저항성 조증에서 clozapine의 안전성과 효능을 평가한 이중맹검 시험(2002~2005). 병태생리 연구를 병행했으며, 직접 관련성은 높으나 규모가 작음 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [32182485](https://pubmed.ncbi.nlm.nih.gov/32182485/) | 2020 | 체계적 문헌고찰/메타분석 | J Psychiatr Res | 양극성 장애에서 clozapine의 임상 효능과 이상반응 평가 |
| [25346322](https://pubmed.ncbi.nlm.nih.gov/25346322/) | 2015 | 체계적 문헌고찰 | Bipolar Disord | 치료저항성 양극성 장애에서 clozapine의 효능과 안전성 평가 |
| [41192460](https://pubmed.ncbi.nlm.nih.gov/41192460/) | 2025 | 코호트/메타분석 | Lancet Psychiatry | 여러 정신질환에서 clozapine과 다른 항정신병약의 효과·안전성 비교 |
| [33719158](https://pubmed.ncbi.nlm.nih.gov/33719158/) | 2021 | 리뷰 | Bipolar Disord | 양극성 장애에서 clozapine에 대해 현재까지 알려진 내용과 향후 과제 |
| [16432528](https://pubmed.ncbi.nlm.nih.gov/16432528/) | 2006 | 리뷰 | Mol Psychiatry | 급성 조증·우울 삽화 및 유지치료에서의 불충분한 반응과 치료저항성 양극성 장애 관리 |
| [11280956](https://pubmed.ncbi.nlm.nih.gov/11280956/) | 2001 | 리뷰 | Bull Menninger Clin | 치료저항성 양극성 장애의 새로운 약물치료. 근거 대부분이 증례 보고·증례 연구 수준 |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | 리뷰 | Acta Psychiatr Scand | 양극성 조증의 근거 기반 치료 옵션과 기분안정제·항정신병약 선택 |
| [10682225](https://pubmed.ncbi.nlm.nih.gov/10682225/) | 2000 | 증례 시리즈/리뷰 | Clin Neuropharmacol | 전기경련요법과 clozapine 병용 36례 검토. 67%가 병용 치료로 이득을 보았고 대부분 안전했으며, 이상반응은 16.6% |
| [41262335](https://pubmed.ncbi.nlm.nih.gov/41262335/) | 2025 | 모델 기반 연구 | Drug Des Devel Ther | 양극성 장애에서 clozapine의 약물 상호작용과 개별화 용량 설계 |

## 한국 시판 정보

한국에는 단일 성분 clozapine 허가증 6건이 모두 유효 상태로 시판 중입니다. 아래는 주요 5건입니다. 허가 적응증은 허가사항 문서 링크로만 제공되어 요약하지 않았으며, 해당 문서를 참조하시기 바랍니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201804185 | 클자핀정50밀리그램 | 황색의 원형 정제 | 허가사항 문서 참조 |
| 200307798 | 클로자릴정25밀리그램 | 황색의 원형 정제 | 허가사항 문서 참조 |
| 201804474 | 클자핀정200밀리그램 | 황색의 장방형 정제 | 허가사항 문서 참조 |
| 201309789 | 클자핀정100밀리그램 | 황색의 원형정제 | 허가사항 문서 참조 |
| 200307799 | 클로자릴정100밀리그램 | 황색의 원형 정제 | 허가사항 문서 참조 |

## 안전성 고려사항

- **약물 상호작용**: 이번 보고서에 수집된 자료에서 100건의 상호작용이 확인되었습니다. 주요(Major) 등급은 다음과 같습니다.
  - Bupropion
  - Morphine
  - Potassium citrate
- 중등도(Moderate) 등급에는 혈당강하제(Metformin, Pioglitazone, Alogliptin 등), 항콜린제(Atropine, Hyoscyamine, Glycopyrronium), H2 차단제·프로톤펌프억제제(Famotidine, Cimetidine, Omeprazole) 등이 포함됩니다.

주요 경고와 금기 등 그 밖의 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
- 조증 양극성 정동장애를 직접 다룬 완료된 2상 이중맹검 시험과 양극성 장애 대상 체계적 문헌고찰·메타분석이 있어, 근거 수준은 L2입니다.
- 다만 시험 규모가 작고 확증 3상 결과가 없으므로, 치료저항성 환자로 제한하는 등 안전장치가 필요합니다.

**진행하려면 필요한 것:**
- 허가사항의 경고·금기 정보 확인 (현재 수집되지 않음)
- 작용 기전 데이터 보완
- 혈액학적 모니터링(절대호중구수, ANC), 대사·심장 모니터링, 경련 위험 관리 계획
- 치료저항성 조증 환자로 한정한 적용 기준 설정
- 더 큰 규모의 무작위 대조 시험 근거 확보

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

