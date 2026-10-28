---
layout: default
title: Magnesium Lactate
parent: 모델 예측만 (L5)
nav_order: 493
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Magnesium Lactate: 예측 신규 적응증 무통성 전신 비만세포증 (Smouldering systemic mastocytosis) (근거 수준 L5). 기존 적응증: 확인 불가 (허가 정보에 적응증 본문 없이 외부 문서 링크만 제공됨)"
monitor_inn: "MAGNESIUM LACTATE"
predicted_indications: ["Smouldering systemic mastocytosis", "systemic mastocytosis", "lymphoadenopathic mastocytosis with eosinophilia", "bacterial arthritis", "peptic esophagitis", "ankylosing spondylitis", "gout", "gastrin secretion abnormality", "rheumatoid vasculitis", "inflammatory spondylopathy"]
---

# Magnesium Lactate
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

## Magnesium Lactate: 기존 적응증 정보 미확인에서 비만세포증(Smouldering Systemic Mastocytosis)으로
{: .text-alpha }

## 한 문장 요약

Magnesium Lactate(젖산마그네슘)는 마그네슘 보충제/제산제 계열 성분으로, 한국에서는 수출용 장용성 필름코팅정으로 허가되어 있습니다.
TxGNN 모델은 **무통성 전신 비만세포증(Smouldering Systemic Mastocytosis)**에 효과가 있을 수 있다고 예측하지만(예측 점수 0.9978), 이를 뒷받침하는 **임상시험은 0건**, **문헌도 0편**입니다.
현재로서는 모델 예측만 존재하는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 정보에 적응증 본문 없이 외부 문서 링크만 제공됨) |
| 예측 신규 적응증 | 무통성 전신 비만세포증 (Smouldering systemic mastocytosis) |
| TxGNN 예측 점수 | 0.9978 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Magnesium Lactate는 마그네슘 보충제/제산제 유형의 성분이며, KIT 유전자 변이(D816V)로 유발되는 비만세포 증식에는 알려진 작용이 없습니다.

기존 적응증과 신규 적응증 사이에서 확립된 기전적 연관성은 확인되지 않았습니다. 높은 TxGNN 점수(0.9978)는 TxGNN 모델(딥러닝)이 산출한 계산상 예측일 뿐이며, 모델이 관련 질환 사이에서 학습한 유사성을 반영할 수 있으나 생물학적 근거는 아닙니다. 임상시험이나 문헌으로 검증되지 않았습니다.

참고로 같은 약물에 대해 예측된 다른 후보(전신 비만세포증, 림프절병증성 비만세포증, 세균성 관절염, 강직성 척추염, 통풍 등)도 모두 근거 수준 L5입니다. 그중 소화성 식도염과 가스트린 분비 이상은 제산 작용을 통한 약한 가설적 연관성만 있습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200403927 | 엠지비정(수출용) | 미백색의 타원형의 장용성 필름코팅정 | 적응증 본문 없음 (허가 문서 링크만 제공) |

## 안전성 고려사항

- **지식 그래프 기반 금기 연관 질환** (허가 문서가 아닌 TxGNN 지식 그래프의 약물-질환 금기 관계 기준): 신장 질환, 요관 농양(pyoureter), 설사성 질환

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
모든 예측 적응증이 L5(모델 예측만 존재)이며, 임상시험과 문헌 근거가 전혀 없습니다. 작용 기전 데이터와 허가 적응증 정보도 확보되지 않아 기전적 타당성을 평가할 수 없습니다.

**진행하려면 필요한 것:**
- 허가 문서(MFDS 첨부문서)에서 적응증, 경고, 금기 정보 확보
- DrugBank 등에서 작용 기전(MOA) 데이터 확보
- 비만세포증과의 기전적 연관성을 뒷받침하는 전임상 또는 임상 근거 탐색
- 약물 상호작용 정보 확인 (현재 조회 결과 없음)
- 신장 질환 환자 등 지식 그래프상 금기 연관 질환에 대한 안전성 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

