---
layout: default
title: Valproic Acid
parent: 모델 예측만 (L5)
nav_order: 715
evidence_level: L5
indication_count: 10
---

# Valproic Acid
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

Using no additional skill — this is a direct report-generation task fully specified by the user's prompt template, so I'll produce the Markdown report accordingly.

# Valproic Acid: 뇌전증에서 삼차신경 종양으로

## 한 문장 요약

Valproic Acid(VPA)는 GABA 신경전달 증강과 나트륨/T형 칼슘 채널 조절을 기전으로 하는 광범위 항경련제(broad-spectrum AED)로, 오랫동안 뇌전증(간질) 치료에 사용되어 왔습니다.
TxGNN 모델은 **삼차신경 종양(Trigeminal Nerve Neoplasm)**에 효과가 있을 수 있다고 예측했으나, 현재 이를 뒷받침하는 **임상시험은 0건**, **관련성 있는 문헌도 사실상 0편**(제시된 유일한 문헌은 대상 질환과 무관)입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 뇌전증(간질), 항경련제 (한국 허가 정보 없음) |
| 예측 신규 적응증 | 삼차신경 종양 (Trigeminal Nerve Neoplasm) |
| TxGNN 예측 점수 | 99.97% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미상영 (허가 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 VPA의 상세한 작용 기전(MOA) 데이터는 공식적으로 확보되지 않았습니다. 다만 근거 문헌들에 따르면 VPA는 GABA성 신경전달을 강화하고 흥분성 이온 전류를 조절하는 광범위 항경련제로, 뇌전증 치료의 표준 약물 중 하나로 오랫동안 사용되어 왔습니다. 또한 히스톤탈아세틸화효소(HDAC) 억제 작용이 있어 이론적으로는 항종양/항증식 잠재력이 거론되기도 합니다.

그러나 이번 예측 대상인 **삼차신경 종양**과는 직접적인 기전 연관성이 문헌상 확인되지 않습니다. 근거로 제시된 유일한 문헌(Sturge-Weber 증후군 증례 시리즈)은 삼차신경 종양을 전혀 다루고 있지 않으며, 내용상 완전히 다른 질환(안면 혈관종증)에 대한 보고입니다. 이는 TxGNN 예측 파이프라인 상에서 **질병명 오매핑(noisy label)**이 발생했을 가능성을 시사합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case Series | Anales españolas de pediatría | 스터지-웨버 증후군(Sturge-Weber syndrome) 14례에 대한 임상 특징 및 경과 보고. 삼차신경 종양과는 직접적 관련이 없음 |

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN은 99.97%의 높은 점수로 삼차신경 종양을 예측했으나, 이를 뒷받침하는 임상시험은 전무하고, 유일하게 매칭된 문헌도 대상 질환과 무관한 내용입니다. 기전 설명 자체도 "TxGNN 질병명 오매핑" 가능성을 명시하고 있어, 이 예측은 실질적 근거가 아닌 모델 아티팩트(noise)일 가능성이 높습니다.

**진행하려면 필요한 것:**
- 삼차신경 종양에 대한 VPA의 실제 전임상/기전 데이터 확보 (현재 전무)
- TxGNN 예측의 질병 라벨 재검증 — "trigeminal nerve neoplasm" 매핑 오류 여부 확인
- 작용기전(MOA) 데이터 보완 (DrugBank API 조회, DG002)
- 허가사항 경고·금기 정보 확보 — 현재 Data Gap으로 S1 안전성 초평가 진입 불가 (DG001, Blocking)
- 한국 허가/시판 현황 자료 확인 (현재 미상영, 허가증 0건)

**참고:** 동일 Evidence Pack 내 다른 후보 질환들(예: trigeminal neuralgia, reading seizures, audiogenic seizures, visual epilepsy)은 VPA의 항경련 기전과 직접 연관된 증례연구·리뷰급 문헌이 다수 확인되어(L3 수준), 삼차신경 종양보다 향후 검토 우선순위가 높은 것으로 판단됩니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

