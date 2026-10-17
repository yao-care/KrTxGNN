---
layout: default
title: Biperiden
parent: 모델 예측만 (L5)
nav_order: 150
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Biperiden: 예측 신규 적응증 소아 발병 파킨슨병 19A (juvenile onset Parkinson disease 19A) (근거 수준 L5). 기존 적응증: 파킨슨증 (허가 적응증 원문은 링크 형태로만 제공되어 구체적 문구는 확인되지 않음)"
monitor_inn: "Biperiden"
predicted_indications: ["Rasmussen subacute encephalitis", "myelitis", "PLA2G6-associated neurodegeneration", "transaldolase deficiency"]
---

# Biperiden
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

# Biperiden: 파킨슨증에서 소아 발병 파킨슨병 19A로

## 한 문장 요약

Biperiden은 중추 무스카린 M1 선택적 항콜린제로, 한국에서 파킨슨증 치료제로 시판되고 있습니다.
TxGNN 모델은 **소아 발병 파킨슨병 19A(juvenile onset Parkinson disease 19A)**에 효과가 있을 수 있다고 예측하지만, 현재 이 예측을 직접 지지하는 **임상시험은 0건, 문헌도 0편**입니다. 따라서 모델 예측 단계에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 파킨슨증 (허가 적응증 원문은 링크 형태로만 제공되어 구체적 문구는 확인되지 않음) |
| 예측 신규 적응증 | 소아 발병 파킨슨병 19A (juvenile onset Parkinson disease 19A) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 biperiden은 중추 무스카린 M1 선택적 항콜린제이며, 파킨슨증에서 선조체의 콜린성-도파민성 균형을 회복시켜 떨림과 근강직을 완화하는 것으로 이해됩니다.

소아 발병 파킨슨병 19A(PARK19A, DNAJC6 관련)는 파킨슨증 증상을 보이는 유전성 질환이므로, 증상 완화 측면에서는 기전상 적용 가능성이 있습니다. 다만 이는 파킨슨증 계열 전반에 대한 추정일 뿐입니다. 이 유전형에 대한 질환 특이적 데이터는 없습니다.

TxGNN 점수는 매우 높지만, 이는 일반적인 파킨슨증 계열과의 네트워크 근접성을 반영한 것으로 보는 것이 타당합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

예측 순위 1위 적응증(소아 발병 파킨슨병 19A)에 대한 관련 문헌이 없습니다.

참고로, 순위 2위 예측인 비정형 소아 파킨슨증과 관련하여 검색된 문헌은 아래 1편입니다. 이 문헌은 biperiden이나 소아 비정형 파킨슨증을 다루지 않으므로 간접적인 배경 정보로만 참고할 수 있습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [42656305](https://pubmed.ncbi.nlm.nih.gov/42656305/) | 2026 | 미분류 (파킨슨병 임상 관찰 추정) | Frontiers in neurology | 파킨슨병에서 레보도파로 떨림이 악화되는 드문 사례 보고. 빈도와 현상학적 특성이 불분명함 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 198501452 | 비페린정(비페리덴염산염)(수출용) | 백색의 원형 정제 | 허가 적응증 원문은 문서 링크로만 제공됨 |

## 안전성 고려사항

- **약물 상호작용**: 총 75건의 상호작용이 확인되었으며, 주요 항목은 다음과 같습니다.
  - **Major**: 염화칼륨(Potassium chloride), 시트르산칼륨(Potassium citrate)
  - **Moderate**: 다른 항콜린제 계열(Atropine, Hyoscyamine, Dicyclomine, Clidinium, Glycopyrronium, Mepenzolate, Methscopolamine, Propantheline), 오피오이드(Morphine, Opium, Loperamide, Eluxadoline), 칸나비노이드(Dronabinol, Nabilone), Metoclopramide, Pramlintide 등

그 외 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 점수는 매우 높지만 임상시험과 문헌이 전무하여 근거 수준이 L5(모델 예측만 존재)입니다. 또한 작용 기전과 허가 문서의 경고·금기 정보가 확보되지 않아 안전성 검토 단계로 넘어갈 수 없습니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기) 확보: 식약처 허가 문서를 내려받아 분석
- 작용 기전 데이터 확보: DrugBank 등에서 조회
- 소아 발병 파킨슨병 19A(DNAJC6 관련)에서 biperiden의 효과를 다룬 임상 또는 전임상 근거 탐색
- 소아 환자에서의 항콜린 부담(인지 기능 저하 등)과 안전성 평가
- 참고: 같은 예측 목록 중 라소무센 뇌염(Rasmussen), 척수염, 트랜스알돌라아제 결핍증은 기전상 연관성이 확인되지 않아 우선 검토 대상에서 제외하는 것이 바람직합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

