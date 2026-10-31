---
layout: default
title: Ambrisentan
parent: 모델 예측만 (L5)
nav_order: 53
evidence_level: L5
indication_count: 5
monitor_inn: "AMBRISENTAN"
predicted_indications: ["pulmonary arteriovenous malformation (disease)", "malformation syndrome with odontal and/or periodontal component", "hypotrichosis simplex of the scalp", "hypertrichosis (disease)", "syndrome with a Dandy-Walker malformation as major feature"]
last_modified_at: 2026-10-31
description: "Ambrisentan: 예측 신규 적응증 폐동정맥 기형 (pulmonary arteriovenous malformation (disease)) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200902796/EE"
---

# Ambrisentan
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **5** 건
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

## Ambrisentan: 엔도텔린 A 수용체 길항제 → 폐동정맥 기형 (pulmonary arteriovenous malformation (disease))
{: .text-alpha }

## 한 문장 요약

Ambrisentan은 엔도텔린 A 수용체 길항제 계열의 약물입니다.
TxGNN 모델은 **폐동정맥 기형(pulmonary arteriovenous malformation (disease))**에 효과가 있을 수 있다고 예측하지만, 현재 등록된 임상시험은 **0건**이며 직접 관련된 문헌도 없고 **1편의 증례 보고**(유전성 출혈성 모세혈관확장증 환자의 폐동맥 고혈압)만 간접적으로 관련됩니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200902796/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200902797/EE |
| 예측 신규 적응증 | 폐동정맥 기형 (pulmonary arteriovenous malformation (disease)) |
| TxGNN 예측 점수 | 0.9941 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 데이터베이스에 기록되어 있지 않습니다. 다만 ambrisentan은 일반적으로 엔도텔린 A 수용체를 선택적으로 차단하여 혈관을 이완시키는 약물로 알려져 있습니다.

폐동정맥 기형은 유전성 출혈성 모세혈관확장증(HHT)에서 흔히 나타나며, ENG/ACVRL1 신호 이상에 따른 혈관신생 조절 이상이 관여합니다. 제시된 유일한 문헌은 HHT 환자에서 발생한 폐동맥 고혈압 증례로, 기형 자체가 아닌 관련된 별개의 질환을 다룹니다. 높은 예측 점수는 폐동맥 고혈압/HHT와의 네트워크상 근접성에서 비롯된 것으로 보입니다.

기형 자체를 치료한다는 기전적 근거는 약합니다. 오히려 혈관 확장이 단락(shunt)을 악화시킬 가능성도 이론적으로 있습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [33969094](https://pubmed.ncbi.nlm.nih.gov/33969094/) | 2021 | 증례 보고 | World J Clin Cases | HHT 환자에서 발생한 폐동맥 고혈압 사례와 가족 유전자 분석. 폐동정맥 기형 자체를 다루지는 않음 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200902796 | 볼리브리스정5밀리그램(암브리센탄) | 연한 분홍색의 볼록한 정사각형 정제 | 허가 문서 링크만 기록되어 있음 |
| 200902797 | 볼리브리스정10밀리그램(암브리센탄) | 진한 분홍색의 볼록한 달걀형 정제 | 허가 문서 링크만 기록되어 있음 |

## 안전성 고려사항

- **약물 상호작용**: 100건이 조회되었으며, 주요 항목은 다음과 같습니다.
  - 중등도: Canagliflozin, Dapagliflozin, Empagliflozin, Ertugliflozin, Eliglustat, Naltrexone
  - 경미: Clarithromycin, Miconazole, Omeprazole
  - 등급 미상: Calcitriol, Pantoprazole, Doxycycline, Morphine, Metformin, Simvastatin 등

안전성 정보는 그 밖에는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
폐동정맥 기형을 직접 연구한 임상시험이나 문헌이 없어 모델 예측만 존재하는 상태입니다(L5). 기전상 근거도 약하고 혈관 확장에 따른 단락 악화 가능성도 배제할 수 없습니다.

**진행하려면 필요한 것:**
- 폐동정맥 기형을 직접 대상으로 한 전임상 또는 임상 연구 근거
- 상세한 작용 기전 데이터 확보
- 허가사항(경고·금기)의 확인 및 안전성 검토
- 단락 악화 위험에 대한 기전적·임상적 평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

