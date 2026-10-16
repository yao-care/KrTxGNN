---
layout: default
title: Pegteograstim
parent: 모델 예측만 (L5)
nav_order: 583
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Pegteograstim: 예측 신규 적응증 심실중격 동맥류 (Interventricular septum aneurysm) (근거 수준 L5). 기존 적응증: 허가 적응증 본문 정보 없음 (허가증에는 문서 링크만 기재)"
monitor_inn: "PEGTEOGRASTIM"
predicted_indications: ["interventricular septum aneurysm", "heart disease", "Laubry-Pezzi syndrome", "Jeune syndrome situs inversus", "Pierre Robin syndrome associated with a chromosomal anomaly", "partial deletion of the long arm of chromosome 22", "genetic syndromic Pierre Robin syndrome", "disorder of fucoglycosan synthesis", "pulmonary valve disease", "partial deletion of the long arm of chromosome 7"]
---

# Pegteograstim
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 약사 평가 보고서

</div>

# Pegteograstim: 호중구감소증 예방에서 심실중격 동맥류로

## 한 문장 요약

Pegteograstim은 장기 지속형 G-CSF(과립구 집락자극인자) 제제로, 한국에서 주사제로 시판되고 있습니다.
TxGNN 모델은 **심실중격 동맥류(interventricular septum aneurysm)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험은 0건**, **직접 관련 문헌도 0편**입니다.
따라서 현재 이 예측은 모델 예측 수준에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문 정보 없음 (허가증에는 문서 링크만 기재) |
| 예측 신규 적응증 | 심실중격 동맥류 (Interventricular septum aneurysm) |
| TxGNN 예측 점수 | 99.38% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Pegteograstim은 페그화된 필그라스팀 계열의 장기 지속형 G-CSF로, 호중구 생성을 촉진합니다.

심실중격 동맥류는 심장의 구조적 이상으로, G-CSF가 이를 변화시킬 수 있는 경로는 확인되지 않았습니다. 높은 TxGNN 점수는 지식 그래프상의 연관성에서 비롯된 결과로 보이며, 생물학적 근거에 기반한 예측으로 보기 어렵습니다.

참고로 같은 약물의 다른 예측 질환 중 상위 10개 모두 근거 수준이 L5이며, 대부분 선천성 구조 이상 또는 염색체 이상 질환입니다. 이들 역시 기전적 연결고리가 확인되지 않았습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201403786 | 뉴라펙프리필드시린지주(페그테오그라스팀) | 프리필드시린지 주사제 (무색 투명한 용액) | 허가증 문서 링크만 제공되어 적응증 요약 불가 |

제조사는 (주)녹십자입니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
심실중격 동맥류에 대한 임상시험과 문헌이 전혀 없고, 기전적 연결고리도 확인되지 않아 점수가 높더라도 지식 그래프에 의한 인위적 결과일 가능성이 큽니다.

**진행하려면 필요한 것:**
- 허가 적응증 및 경고·금기 정보 확보 (허가사항 PDF 내려받아 분석)
- 작용 기전(MOA) 데이터 보완 (DrugBank 조회)
- 심장 질환 영역에서 G-CSF의 효과를 평가한 임상 또는 전임상 근거
- 다른 예측 질환 중 근거가 있는 후보가 있는지 재검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

