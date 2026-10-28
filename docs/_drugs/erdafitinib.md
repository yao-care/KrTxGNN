---
layout: default
title: Erdafitinib
parent: 모델 예측만 (L5)
nav_order: 316
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Erdafitinib: 예측 신규 적응증 폐고혈압 (Pulmonary Hypertension) (근거 수준 L5). 기존 적응증: 허가 적응증 원문 텍스트는 확인되지 않았습니다(허가증 링크만 제공됨). 허가사항 참조 필요"
monitor_inn: "Erdafitinib"
predicted_indications: ["pulmonary hypertension", "kyphoscoliotic heart disease", "amenorrhea (disease)", "rheumatoid arthritis", "amyotrophic lateral sclerosis", "brachydactyly-syndactyly syndrome"]
---

# Erdafitinib
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **6** 건
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

## Erdafitinib: 기존 적응증에서 폐고혈압으로
{: .text-alpha }

## 한 문장 요약

Erdafitinib은 FGFR(섬유아세포성장인자 수용체) 1~4를 억제하는 키나제 억제제로, 한국에서 단일제 정제 3종(발베사정)으로 허가되어 시판 중입니다. TxGNN 모델은 **폐고혈압(Pulmonary Hypertension)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 **임상시험과 문헌은 없습니다**. 따라서 모델 예측만 존재하는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 원문 텍스트는 확인되지 않았습니다(허가증 링크만 제공됨). 허가사항 참조 필요 |
| 예측 신규 적응증 | 폐고혈압 (Pulmonary Hypertension) |
| TxGNN 예측 점수 | 0.9938 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 3건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 확보되지 않았습니다. 알려진 정보에 따르면 erdafitinib은 pan-FGFR(FGFR1-4) 티로신 키나제 억제제입니다. FGF/FGFR 신호전달은 폐혈관 리모델링과 평활근·내피세포 증식에 관여하는 것으로 보고되어 있어, 생물학적으로 일정한 연결 가능성이 있습니다.

다만 이 연결은 가설 수준입니다. 이 적응증을 직접 뒷받침하는 임상시험이나 문헌이 없고, 높은 TxGNN 점수(0.9938)는 계산 모델의 예측일 뿐입니다. 또한 FGFR 억제의 계열 독성인 고인산혈증 등이 해당 환자군에서 문제가 될 수 있습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202204247 | 발베사정3밀리그램(얼다피티닙) | 노란색 양면 볼록 원형 필름코팅 정제 | 허가사항 참조 |
| 202204249 | 발베사정5밀리그램(얼다피티닙) | 갈색 양면 볼록 원형 필름코팅 정제 | 허가사항 참조 |
| 202204248 | 발베사정4밀리그램(얼다피티닙) | 주황색 양면 볼록 원형 필름코팅 정제 | 허가사항 참조 |

세 제품 모두 (주)한국얀센의 단일제이며 현재 유효한 허가입니다.

## 안전성 고려사항

**약물 상호작용**: 상호작용 조회 결과 총 100건이 확인되었으며, 주요 항목은 다음과 같습니다.

- **Major**: Cholecalciferol, Dexamethasone, Calcium Phosphate, Calcifediol, Calcitriol, Calcium acetate, Clarithromycin, Magnesium oxide, Magnesium sulfate, Magnesium chloride
- **Moderate**: Metformin, Loperamide, Saxagliptin, Eliglustat, Empagliflozin, Linagliptin, Naldemedine, Naloxegol, Prucalopride, Rifaximin

그 밖의 경고·금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
폐고혈압 예측은 FGFR 신호전달에 근거한 가설적 연결만 있고 임상시험과 문헌이 전혀 없는 L5 단계입니다. 허가사항의 안전성 정보와 기전 데이터도 확인되지 않아 진행 판단을 내리기 어렵습니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기·적응증) 확보 및 안전성 검토
- 상세한 작용 기전(MOA) 데이터 확보
- FGFR 신호전달과 폐혈관 리모델링의 연관성을 보여주는 전임상 연구
- 고인산혈증 등 FGFR 억제 계열 독성이 폐고혈압 환자에게 미치는 영향 평가
- 폐고혈압에 대한 관련 임상시험 또는 문헌 근거 확보
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

