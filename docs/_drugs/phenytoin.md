---
layout: default
title: Phenytoin
parent: 모델 예측만 (L5)
nav_order: 600
evidence_level: L5
indication_count: 3
monitor_inn: "PHENYTOIN"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
last_modified_at: 2026-10-31
description: "Phenytoin: 예측 신규 적응증 삼차신경 신생물 (trigeminal nerve neoplasm) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201106874/EE"
---

# Phenytoin
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

## Phenytoin: 나트륨 채널 차단 항경련제 → 삼차신경 신생물 (trigeminal nerve neoplasm)
{: .text-alpha }

## 한 문장 요약

Phenytoin은 전압 의존성 나트륨 채널을 차단하는 항경련제 계열의 약물입니다.
TxGNN 모델은 **삼차신경 신생물(trigeminal nerve neoplasm)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 연구한 임상시험은 **0건**, 문헌도 **0편**입니다. 검색된 2편의 문헌은 삼차신경통과 Sturge-Weber 증후군을 다루고 있어 이 예측을 뒷받침하지 않습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201106874/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198500605/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198100305/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/197500285/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/197000104/EE;  |
| 예측 신규 적응증 | 삼차신경 신생물 (trigeminal nerve neoplasm) |
| TxGNN 예측 점수 | 0.9999 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 7건 / 전체 7건) |
| 허가증 수 | 7건 (유효 7건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 데이터베이스에 기록되어 있지 않습니다. 일반적으로 Phenytoin은 전압 의존성 나트륨 채널을 차단하여 과흥분된 신경 세포막을 안정화하는 약물로 알려져 있으며, 신경성 통증이나 발작을 줄이는 데 사용될 수 있습니다.

그러나 종양을 직접 겨냥하는 항종양 기전은 알려져 있지 않습니다. 높은 예측 점수는 삼차신경통이나 Sturge-Weber 증후군과 같은 인접 질환과의 연관성에서 비롯되었을 가능성이 큽니다. 따라서 삼차신경 신생물에 대한 기전상 타당성은 현재로서는 낮습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

삼차신경 신생물을 직접 다룬 문헌은 없습니다. 아래 2편은 인접 질환을 다룬 문헌으로, 이 예측을 지지하지 않습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurother | 삼차신경통의 내과적·외과적 치료 개관 (신생물 아님) |
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | An Esp Pediatr | Sturge-Weber 증후군 14례의 임상 특성과 치료 반응 (신생물 아님) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201106874 | 제일제약페니토인나트륨주50mg/mL(수출용) | 무색 투명한 액이든 갈색앰플주사제 | 적응증 텍스트 미기록 |
| 198500605 | 명인페니토인정100밀리그램 | 흰색 원형의 정제 | 적응증 텍스트 미기록 |
| 198100305 | 삼진페니토인나트륨주사100밀리그램 | 무색투명한 액이 충진된 갈색앰플제 | 적응증 텍스트 미기록 |
| 197500285 | 환인히단토인정(페니토인) | 백색원형의 정제 | 적응증 텍스트 미기록 |
| 197000104 | 부광페니토인캡슐100밀리그램 | 백색의 캅셀내 백색분말 | 적응증 텍스트 미기록 |

## 안전성 고려사항

- **약물 상호작용**: 데이터에 총 100건의 상호작용이 기록되어 있습니다. 주요 항목은 대부분 중등도(Moderate)이며 Acarbose, Famotidine, Ranitidine, Doxycycline, Hydrocortisone, Metformin, Pioglitazone, Bupropion, Aprepitant, Morphine, Omeprazole, Dexamethasone, Metronidazole 등이 포함됩니다. Acetylsalicylic acid는 경미한(Minor) 수준입니다.

그 외 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
삼차신경 신생물을 직접 연구한 임상시험이나 문헌이 없고, 알려진 항종양 기전도 없어 근거 수준은 L5입니다. 높은 예측 점수는 삼차신경통 등 인접 질환과의 연관성에서 비롯된 것으로 보입니다.

**진행하려면 필요한 것:**
- 삼차신경 신생물에서 Phenytoin의 효과를 직접 평가한 전임상 또는 임상 연구
- 상세한 약물 작용 기전(MOA) 데이터와 종양 관련 기전 연결성 분석
- 허가사항(경고, 금기)의 확보 및 안전성 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

