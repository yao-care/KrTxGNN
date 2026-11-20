---
layout: default
title: Oxymetholone
parent: 모델 예측만 (L5)
nav_order: 571
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
description: "Oxymetholone: 예측 신규 적응증 지루성 피부염 (Seborrheic Dermatitis) (근거 수준 L5). 기존 적응증: 재생불량성 빈혈, 골수섬유증에 의한 골수의 소모상태"
monitor_inn: "OXYMETHOLONE"
predicted_indications: ["seborrheic dermatitis"]
---

# Oxymetholone
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

## Oxymetholone: 적혈구 생성 부전 빈혈에서 지루성 피부염으로
{: .text-alpha }

## 한 문장 요약

Oxymetholone은 경구용 동화-안드로겐 스테로이드로, 한국에서는 허가증상 적응증 원문이 문서 링크로만 확인되며, 일반적으로 적혈구 생성 부전에 의한 빈혈 치료에 사용되는 약물입니다.
TxGNN 모델은 **지루성 피부염(Seborrheic Dermatitis)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 **임상시험은 0건**, **문헌도 0편**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 재생불량성 빈혈, 골수섬유증에 의한 골수의 소모상태 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198300174/EE)) |
| 예측 신규 적응증 | 지루성 피부염 (Seborrheic Dermatitis) |
| TxGNN 예측 점수 | 0.9905 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

ChEMBL(EMBL-EBI)에 등록된 Oxymetholone의 작용 기전(비공식 번역): “안드로겐 수용체 작용제” 영어 원문: "Androgen Receptor agonist" ([ChEMBL CHEMBL1200585 (oxymetholone): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1200585), CC BY-SA 3.0; 확인일 2026-11-19). 알려진 정보에 따르면 Oxymetholone은 안드로겐 수용체에 작용하는 경구용 동화-안드로겐 스테로이드이며, 적혈구 생성 부전에 의한 빈혈 치료에 사용됩니다.

안드로겐이 피지선 활동을 조절하고, 지루성 피부염이 피지 및 Malassezia 관련 염증과 연관된다는 점에서 연결 고리를 추정해 볼 수는 있습니다. 그러나 이는 검증되지 않은 가설입니다. 오히려 안드로겐은 일반적으로 피지 분비를 늘리므로, 이 논리대로라면 증상 악화 가능성을 시사합니다.

높은 예측 점수는 임상 데이터가 아니라 TxGNN 모델(딥러닝)이 관련 질환 간에 학습한 유사성을 반영했을 가능성이 크며, 생물학적 근거를 의미하지는 않습니다. 기존 적응증과의 유사성 평가도 아직 이루어지지 않았습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 198300174 | 셀트리온옥시메톨론정 | 흰색 ~ 유백색의 원형 정제 | 허가 문서 링크로만 제공되어 본문 확인 불가 |

## 안전성 고려사항

- **약물 상호작용**: 상호작용 69건이 조회되었으며, 그중 주요 항목은 다음과 같습니다.
  - **Major**: Carfilzomib
  - **Moderate**: Hydrocortisone, Triamcinolone, Dexamethasone, Betamethasone, Budesonide 등 코르티코스테로이드, Asparaginase 제제, Brentuximab vedotin, Cyclosporine, Chlorpropamide, Clofarabine, Cannabidiol 등
- **지식 그래프 기반 금기 관련 질환** (허가사항 문구가 아닌 모델 지식 그래프 기준): 간부전·간질환, 신장질환, 신증후군, 울혈성 심부전 등 심혈관질환, 죽상경화증, 관상동맥질환, 전립선암, 여성 유방암, 양성 전립선비대증, 당뇨병 및 당뇨병성 케톤산증, 혈액응고질환, 악성종양의 체액성 고칼슘혈증, 담낭질환, 간자반병(peliosis hepatis), 저알파지단백혈증 등

허가사항의 경고 및 금기 정보는 이번 자료에서 확인되지 않았으므로 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 근거는 TxGNN 점수(0.9905)뿐이며, 임상시험과 문헌 근거가 전혀 없습니다. 또한 안드로겐이 피지 분비를 늘린다는 점에서 기전상 치료 효과보다 악화 가능성이 더 시사되고, 지식 그래프상 금기 질환도 많아 현 단계에서는 진행하기 어렵습니다.

**진행하려면 필요한 것:**
- MFDS 허가사항(경고·금기·적응증)의 확보 및 분석
- DrugBank 등에서 상세 작용 기전(MOA) 데이터 확보
- 안드로겐과 지루성 피부염의 관계에 대한 문헌 검토 및 전임상·기전 근거 확보
- 투여 경로(경구제 vs. 피부 적용 필요성) 적합성 평가
- 기존 적응증과 신규 적응증 간 유사성 분석

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [ChEMBL CHEMBL1200585 (oxymetholone): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1200585) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

