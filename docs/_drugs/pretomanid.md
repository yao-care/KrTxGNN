---
layout: default
title: Pretomanid
parent: 모델 예측만 (L5)
nav_order: 627
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Pretomanid: 예측 신규 적응증 칸디다증 (Candidiasis) (근거 수준 L5). 기존 적응증: 허가증 원문 링크만 제공되어 구체적 문구 확인 불가 (문헌상 BPaL 요법의 광범위 약제내성·치료 불내성/비반응 다제내성 폐…"
monitor_inn: "Pretomanid"
predicted_indications: ["candidiasis", "leprosy", "coronary artery disease", "myocardial ischemia", "anomalous left coronary artery from the pulmonary artery", "HIV infectious disease", "oral candidiasis", "Bacteroidaceae infectious disease", "thrombocytopenia", "fascioliasis"]
---

# Pretomanid
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

# Pretomanid: 약제내성 결핵에서 칸디다증으로

## 한 문장 요약

Pretomanid는 니트로이미다졸계 항결핵제로, 한국에서 약제내성 결핵 치료에 허가된 약물입니다(허가증 원문은 링크로만 제공되어 세부 적응증 문구는 확인되지 않았습니다).
TxGNN 모델은 **칸디다증(Candidiasis)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**이며 항진균 기전 근거도 없습니다.
따라서 이 예측은 모델 점수만 있는 가설 수준(L5)입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증 원문 링크만 제공되어 구체적 문구 확인 불가 (문헌상 BPaL 요법의 광범위 약제내성·치료 불내성/비반응 다제내성 폐결핵) |
| 예측 신규 적응증 | 칸디다증 (Candidiasis) |
| TxGNN 예측 점수 | 99.69% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 이번 보고서에 편입되어 있지 않습니다. 알려진 정보에 따르면 Pretomanid는 니트로이미다졸 계열의 전구약물(prodrug)로, 결핵균의 Ddn 니트로환원효소에 의해 활성화되며 마이코박테리아에 특이적으로 작용합니다.

칸디다증은 진균 감염으로, Pretomanid에는 확립된 항진균 기전이 없습니다. 결핵균 특이적 활성화 경로를 고려하면 Candida와의 기전적 연결은 지지되지 않으며, 높은 예측 점수는 지식 그래프 구조에서 비롯된 결과일 가능성이 큽니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202106953 | 도브프렐라정200밀리그램(프레토마니드) | 정제 (흰색~미백색 타원형, 'M'/'P200' 각인) | 허가증 원문 링크로만 제공됨 |

## 안전성 고려사항

- **약물 상호작용**: 총 14건이 확인되었습니다.
  - **Major(주의 필요)**: Dexamethasone, Lumacaftor, Apalutamide, Dabrafenib, Mitotane, Lorlatinib, Enzalutamide
  - **Moderate**: Empagliflozin, Sitagliptin, Somatotropin, Somatrem, Baricitinib, Clofarabine, Methotrexate

허가사항의 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
칸디다증에 대한 임상시험과 문헌이 전무하고, Pretomanid가 마이코박테리아에 특이적인 약물이라 항진균 기전도 뒷받침되지 않습니다. 점수가 높아도 모델 예측만으로는 진행 근거가 부족합니다.

**진행하려면 필요한 것:**
- Candida 균주에 대한 시험관 내(in vitro) 항진균 감수성 데이터
- 허가사항(경고·금기)의 확인 및 정리
- 상세한 작용 기전(MOA) 데이터 확보

**참고: 다른 예측 적응증**
- 상위 10개 예측 중 근거가 가장 많은 것은 한센병(문헌 8편, L4)과 HIV 감염(임상시험 1건·문헌 20편, L4)입니다. 그러나 이 문헌들은 모두 약제내성 결핵(BPaL/BPaLM 요법)에 관한 것으로, 한센병이나 HIV 자체의 치료 근거가 아닙니다.
- 그 외(관상동맥질환, 심근허혈, 구강 칸디다증, 혈소판감소증, 간질증 등)는 모델 예측만 있고 근거가 없습니다. 혈소판감소증은 병용 약물인 linezolid의 알려진 이상반응으로, 치료 대상이 아니라 안전성 고려사항에 해당합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

