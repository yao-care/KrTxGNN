---
layout: default
title: Modafinil
parent: 모델 예측만 (L5)
nav_order: 525
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-04
monitor_inn: "MODAFINIL"
predicted_indications: ["insomnia (disease)"]
description: "Modafinil: 예측 신규 적응증 불면증 (insomnia (disease)) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200200234/EE"
---

# Modafinil
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **1** 건
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

## Modafinil: 불면증 (insomnia (disease))
{: .text-alpha }

## 한 문장 요약

Modafinil은 각성을 촉진하는 약물로, 한국에서 단일 성분 제제로 시판되고 있습니다.
TxGNN 모델은 **불면증(insomnia)**에 효과가 있을 수 있다고 예측하지만, 불면증 자체를 직접 다룬 근거는 충분하지 않아 근거 수준은 **L5**입니다.
관련 임상시험 2건 중 불면증 대상 시험(NCT00124384)은 결과가 공개되어 있지 않고, 문헌은 주로 주간 졸림이나 피로를 다룹니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200200234/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201104024/EE |
| 예측 신규 적응증 | 불면증 (insomnia (disease)) |
| TxGNN 예측 점수 | 0.9985 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 modafinil은 도파민 수송체 억제와 각성 관련 신경회로(히스타민, 오렉신, 글루타메이트)에 작용하는 각성 촉진제로 알려져 있습니다.

다만 각성을 높이는 작용은 불면증 치료의 목표(과각성 완화, 수면 개선)와 방향이 반대입니다. 따라서 기전상 불면증에 직접 적용할 근거는 약합니다. 0.9985라는 높은 점수는 수면-각성 질환 간의 데이터 상 근접성을 반영한 것일 가능성이 큽니다.

그나마 현실적인 관련 용도는 파킨슨병, 신경계 질환, 고령자 등에 동반되는 주간 졸림이나 수면-각성 장애로, 이는 불면증과는 다른 임상 표적입니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00124384](https://clinicaltrials.gov/study/NCT00124384) | Phase 4 | 완료 | 40 | 일차성 불면증에서 modafinil 단독 또는 인지행동치료(CBT-I)와 병용 시 주간 기능과 불면 중증도 변화를 평가. 공개된 결과 없음 |
| [NCT00626210](https://clinicaltrials.gov/study/NCT00626210) | Phase 4 | 종료 | 2 | 고령자의 수면/각성 장애에서 modafinil 평가. 2명만 등록되어 해석 가능한 결과 없음 |

## 문헌 근거

불면증 자체를 직접 연구한 문헌은 없습니다. 아래는 modafinil 또는 관련 수면 질환을 다룬 주요 문헌입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [18729534](https://pubmed.ncbi.nlm.nih.gov/18729534/) | 2008 | Review | Drugs | modafinil의 허가 및 연구 중인 용도를 무작위 대조시험 중심으로 고찰 |
| [24312590](https://pubmed.ncbi.nlm.nih.gov/24312590/) | 2013 | 체계적 문헌고찰/메타분석 | PLoS One | 신경계 질환에 동반된 피로와 주간 과도 졸림에 대한 modafinil의 효과와 안전성 평가 |
| [27010071](https://pubmed.ncbi.nlm.nih.gov/27010071/) | 2016 | 체계적 문헌고찰/메타분석 | Parkinsonism Relat Disord | 파킨슨병의 주간 졸림 및 수면 장애에 대한 약물 중재 검토 |
| [22021174](https://pubmed.ncbi.nlm.nih.gov/22021174/) | 2011 | 체계적 문헌고찰 | Mov Disord | 파킨슨병 비운동 증상 치료에 대한 근거 중심 검토 |
| [39535843](https://pubmed.ncbi.nlm.nih.gov/39535843/) | 2024 | Review | Expert Opin Pharmacother | 파킨슨병 수면 장애의 약물 및 비약물 관리 |
| [17181377](https://pubmed.ncbi.nlm.nih.gov/17181377/) | 2006 | Review | Drugs | 교대근무 수면장애의 질병 부담과 관리 방법 |
| [17060310](https://pubmed.ncbi.nlm.nih.gov/17060310/) | 2006 | 증례 시리즈 | Am J Hosp Palliat Care | 샤르코-마리-투스병 1A형 환자의 피로 감소 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200200234 | 프로비질정200밀리그램(모다피닐) | 백색 또는 거의 백색의 장방형 정제 | 허가 문서 참조 |
| 201104024 | 모다닐정200밀리그램(모다피닐) | 흰색 또는 거의 흰색의 장방형 정제 | 허가 문서 참조 |

## 안전성 고려사항

- **약물 상호작용**: 조회된 상호작용은 총 100건이며, 일부는 다음과 같습니다.
  - 중등도: Rabeprazole, Omeprazole, Esomeprazole, Dexamethasone, Eliglustat, Linagliptin, Cisapride
  - 경미: Hydrocortisone, Pioglitazone, Aprepitant, Triamcinolone, Betamethasone, Cimetidine, Clarithromycin 등

허가사항의 경고 및 금기 정보는 허가 문서를 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
불면증을 직접 지지하는 완료된 연구 결과가 공개되어 있지 않아 근거 수준은 L5입니다. 또한 각성 촉진이라는 약리 작용은 불면증 치료 방향과 상충하므로, 현재로서는 진행하기 어렵습니다.

**진행하려면 필요한 것:**
- 불면증 환자를 대상으로 한 무작위 대조 임상시험 결과 (특히 NCT00124384의 결과 공개 여부 확인)
- 작용 기전 데이터 확보 및 불면증과의 기전적 연관성 검토
- 허가사항(경고, 금기) 확인 및 안전성 평가
- 주간 졸림 등 불면증과 구분되는 임상 표적에 대한 별도 검토

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

