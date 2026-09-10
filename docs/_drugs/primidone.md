---
layout: default
title: Primidone
parent: 僅模型預測 (L5)
nav_order: 576
evidence_level: L5
indication_count: 10
---

# Primidone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Primidone: 간질(뇌전증)에서 삼차신경 종양(Trigeminal Nerve Neoplasm)으로

## 한 문장 요약

Primidone은 GABA 증강 기전을 가진 오래된 항경련제로, 간질(부분발작·전신강직간대발작) 치료에 사용되어 왔습니다. TxGNN 모델은 최고 점수(99.99%)로 **삼차신경 종양(Trigeminal Nerve Neoplasm)**을 예측했지만, 이를 뒷받침하는 임상시험이나 문헌은 전혀 없으며, 전문가 검토 결과 지식그래프 상 "trigeminal" 노드 간 인접 효과로 인한 노이즈일 가능성이 높습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 간질(뇌전증) — 국내 허가자료는 없으며, 문헌(PMID 3925335 등)을 통해 확인됨 |
| 예측 신규 적응증 | 삼차신경 종양 (Trigeminal Nerve Neoplasm) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L5 (임상시험·문헌 근거 없음) |
| 한국 시판 현황 | 미상영 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 Primidone의 상세 작용 기전(MOA) 데이터는 확보되지 않았습니다. 다만 근거 자료 내 문헌을 통해 알려진 정보에 따르면, Primidone은 전압개폐 나트륨 채널 억제 및 GABA성 신경전달 증강 작용을 가진 광범위 항경련제이며, 간에서 phenobarbital과 PEMA로 대사됩니다.

그러나 삼차신경 종양과의 연관성은 근거가 매우 약합니다. 제공된 기전 분석에 따르면 "삼차신경 종양 억제와 관련된 알려진 약리 경로가 없으며", TxGNN의 높은 점수는 지식그래프 상 "trigeminal" 노드가 삼차신경통(trigeminal neuralgia) 등 인접 적응증과 embedding을 공유하기 때문에 발생한 근접 효과(proximity artifact)일 가능성이 크다고 평가됩니다. 즉 실제 약리학적 연결이 아닐 가능성이 높습니다.

참고로 동일 근거팩 내 다른 예측 후보 중에서는 **반사성 간질(audiogenic seizures, 청각 유발 발작)**이 상대적으로 더 설득력 있는 기전을 갖고 있습니다 — audiogenic seizure 모델은 항경련제 스크리닝에 고전적으로 쓰이는 동물 모델이며, primidone이 실제로 이 모델에서 시험된 문헌(PMID 184518)이 존재합니다. 다만 이 역시 임상시험 수준의 근거는 없습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 참고: 전체 예측 후보 비교

동일 근거팩에 포함된 상위 10개 예측 후보를 비교하면 다음과 같습니다. 대부분 반사성 간질(reflex epilepsy) 계열이며 임상시험 근거는 전무합니다.

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 | 권장 |
|------|-----------|-----------|----------|------|
| 1 | 삼차신경 종양 | 99.99% | L5 | Hold |
| 2 | Thinking seizures | 99.99% | L4 | Research Question |
| 3 | Audiogenic seizures | 99.99% | L3 | Research Question |
| 4 | Eating seizures | 99.99% | L4 | Hold |
| 5 | Orgasm-induced seizures | 99.99% | L5 | Hold |
| 6 | Micturition-induced seizures | 99.99% | L4 | Research Question |
| 7 | Startle epilepsy | 99.99% | L4 | Research Question |
| 8 | Reading seizures | 99.99% | L4 | Research Question |
| 9 | 삼차신경통(Trigeminal neuralgia) | 99.98% | L4 | Research Question |
| 10 | Beta-ketothiolase deficiency | 99.96% | L5 | Hold |

TxGNN 점수는 상위 10개 후보가 사실상 동일 수준(99.96~99.99%)으로, 순위 간 실질적 변별력이 낮습니다. 이 중 근거가 가장 두터운 것은 3순위 **Audiogenic seizures**(L3, 동물모델+인체 개별사례 다수)입니다.

---

## 한국 시판 정보

현재 한국 내 허가 정보가 없습니다 (미상영, 허가증 0건).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> ⚠️ 참고: TFDA(식약처) 수준의 경고/금기 정보 확보가 **차단(Blocking) 수준의 데이터 공백**으로 분류되어 있어, 이 상태로는 안전성 초기 평가(S1) 단계 진입이 불가능합니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
1순위 예측인 삼차신경 종양은 임상시험·문헌 근거가 전무하고(L5), 자체 기전 분석에서도 "실제 약리 연결이 아닌 그래프 노이즈"로 평가되어 근거팩 신뢰도가 낮습니다. 상위 10개 후보 전체를 보아도 가장 근거가 두터운 audiogenic seizures조차 L3(동물모델·개별사례)에 그쳐 임상적 가설 검증 단계(S2)를 넘어서지 못합니다. 또한 이 약물은 한국 미상영 상태이며, TFDA 수준 안전성 자료 확보가 차단(Blocking) 데이터 공백으로 지정되어 있어 안전성 초기 평가조차 진행할 수 없습니다.

**진행하려면 필요한 것:**
- TFDA 공식 안전성 자료(경고/금기) 확보 — 현재 Blocking 데이터 공백
- Primidone의 상세 작용 기전(MOA) 데이터 확보 (DrugBank API 재조회 등)
- 삼차신경 종양 예측이 실제 기전인지 판별할 전임상 검증 연구
- (대안 경로 검토 시) audiogenic seizures/반사성 간질 계열에 대한 전향적 임상 가설 설계
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

