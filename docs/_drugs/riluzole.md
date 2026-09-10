---
layout: default
title: Riluzole
parent: 僅模型預測 (L5)
nav_order: 603
evidence_level: L5
indication_count: 10
---

# Riluzole
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

# Riluzole: 미확인 기존 적응증에서 근위축성측삭경화증(ALS) 감수성으로

## 한 문장 요약

Riluzole은 나트륨 채널 차단 및 시냅스전 글루탐산 방출 억제를 통해 신경보호 효과를 나타내는 약물로, 이번 Evidence Pack에는 한국 내 허가·기존 적응증 데이터가 확인되지 않습니다(미출시).
TxGNN 모델은 총 **10개의 신규 적응증 후보**를 예측했으나, 그중 9건은 기전적 개연성이 낮거나 근거가 전무한 초희귀 선천성 질환이었고, 유일하게 **근위축성측삭경화증(ALS) 감수성(susceptibility)**에서만 **20편의 문헌 근거**가 확인되어 임상적으로 의미 있는 신호로 판단됩니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (한국 허가 정보 미확인, Data Gap) |
| 예측 신규 적응증 | 근위축성측삭경화증 감수성 (Amyotrophic Lateral Sclerosis, susceptibility to) |
| TxGNN 예측 점수 | 99.98% (rank 798) |
| 근거 수준 | L3 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

> 참고: TxGNN 원점수 기준 1위 예측(bilateral parasagittal parieto-occipital polymicrogyria, 99.99%)은 기전 개연성이 극히 낮고 임상 근거가 전무해(L5, Hold) 대표 후보로 채택하지 않았습니다. 대신 이번 팩에서 **유일하게 실제 문헌 근거가 확인된 후보(rank 8)**를 대표 적응증으로 선정했습니다. 아래 "이 예측이 타당한 이유는?" 참조.

---

## 이 예측이 타당한 이유는?

구조화된 MOA 필드는 Data Gap 상태이지만, 첨부된 문헌(PMID 9178165, 19593125, 20942785, 22646982 등)에 따르면 riluzole은 **나트륨 채널을 차단하고 시냅스전 글루탐산 방출을 억제**하여 운동신경세포의 흥분독성(glutamate excitotoxicity)을 억제하는 기전을 가진 것으로 반복적으로 보고되어 있습니다.

기존 적응증 정보 역시 이번 Evidence Pack의 한국 허가 데이터베이스에는 등록되어 있지 않지만(0건, 미출시), 문헌에서는 riluzole이 "ALS에 대해 입증된 효능을 가진 유일한 치료제"로 지속적으로 언급되고 있어(PMID 20942785, 22646982, 19593125), 이미 다른 관할권에서 ALS 표준치료로 자리잡고 있음을 시사합니다.

이번에 TxGNN이 "신규"로 예측한 **근위축성측삭경화증 감수성(susceptibility)**은 온톨로지상 별도 질병 노드로 분류되어 있으나, 실질적으로는 ALS 본체와 동일한 질병 스펙트럼입니다. 즉 이 예측은 완전히 새로운 발견이라기보다, 모델이 이미 알려진 약물-질병 관계를 정확히 포착했음을 보여주는 **양성대조(positive control) 성격**이 강합니다.

**전체 10개 예측 후보 개요 (참고):**

| Rank | 질병명 | 점수 | 근거수준 | 권장 결정 | 비고 |
|------|--------|------|---------|----------|------|
| 1 | 양측 두정후두 다소회뇌증 | 99.99% | L5 | Hold | 기전 무관, 노이즈 가능성 높음 |
| 2 | 축성 척추간엽이형성증 | 99.99% | L5 | Hold | 기전 무관 |
| 3 | 만발성 하위운동신경세포 증후군 | 99.99% | L5 | Research Question | MND 스펙트럼, 근거 없음 |
| 4 | 모발-망막색소변성-왜소증 증후군 | 99.99% | L5 | Hold | 기전 무관 |
| 5 | 치명적 관절만곡-전각세포병 증후군 | 99.99% | L5 | Hold | 선천성, 기전 상이 |
| 6 | 단일근위축증 (Hirayama병) | 99.99% | L5 | Research Question | MND 스펙트럼, 근거 없음 |
| 7 | Mills 증후군 | 99.98% | L5 | Research Question | MND 스펙트럼, 근거 없음 |
| **8** | **ALS 감수성** | **99.98%** | **L3** | **Proceed with Guardrails** | **유일한 문헌 근거 확보** |
| 9 | 상염색체 우성 미토콘드리아 근병증 | 99.98% | L5 | Hold | 대사질환, 기전 무관 |
| 10 | ALS 22형 | 99.98% | L5 | Research Question | ALS 아형, 독립 근거 없음 |

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [21128691](https://pubmed.ncbi.nlm.nih.gov/21128691/) | 2011 | Review | CNS Drugs | ALS에서 유일하게 승인된 riluzole이 생존기간을 경미하게 연장시킨다고 보고 |
| [20942785](https://pubmed.ncbi.nlm.nih.gov/20942785/) | 2010 | Review | CNS Neurol Disord Drug Targets | Riluzole이 ALS 치료에 이용 가능한 유일한 약물이며 생존을 2-3개월 연장 |
| [19593125](https://pubmed.ncbi.nlm.nih.gov/19593125/) | 2009 | Review | Curr Opin Neurol | 집중적 연구에도 불구하고 riluzole만이 입증된 효능을 가진 유일한 약물로 남아있음 |
| [22646982](https://pubmed.ncbi.nlm.nih.gov/22646982/) | 2011 | Review | Expert Opin Drug Discov | ALS 승인 치료제는 riluzole 단독이며 생존을 2-3개월 개선 |
| [20698807](https://pubmed.ncbi.nlm.nih.gov/20698807/) | 2011 | Review(역학) | Amyotroph Lateral Scler | Riluzole만이 생존 개선 효과가 있으나 그 효과는 미미하며, 임상시험 설계상 이질성 문제 논의 |
| [9178165](https://pubmed.ncbi.nlm.nih.gov/9178165/) | 1997 | Review | J Neurol | 글루탐산 흥분독성 가설과 운동신경세포 손상 기전 정리 |
| [16723044](https://pubmed.ncbi.nlm.nih.gov/16723044/) | 2006 | Review | Expert Rev Mol Med | ALS 병태생리(산화스트레스, 흥분독성, 미토콘드리아 기능장애 등) 및 치료 표적 제안 |
| [8061281](https://pubmed.ncbi.nlm.nih.gov/8061281/) | 1994 | 전임상 실험연구 | Neuroreport | Riluzole이 ALS 환자 뇌척수액(CSF) 유발 신경독성을 억제, 신경보호효과 직접 확인 |
| [31108504](https://pubmed.ncbi.nlm.nih.gov/31108504/) | 2019 | 전임상(iPSC) 실험연구 | Hum Mol Genet | ALS 환자유래 iPSC 운동신경세포에서 riluzole 관련 글루탐산성 신경전달 및 칼슘과부하 기전 규명 |
| [20942786](https://pubmed.ncbi.nlm.nih.gov/20942786/) | 2010 | Review | CNS Neurol Disord Drug Targets | ALS 진단·병인·치료표적 개관, riluzole의 위치 확인 |

---

## 한국 시판 정보

한국 내 허가/시판 정보가 확인되지 않았습니다 (미출시, 총 0건).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
ALS 감수성 적응증에 대해서는 다수의 리뷰 논문과 전임상/iPSC 연구가 riluzole의 항흥분독성 기전을 뒷받침하며, 이는 사실상 이미 알려진 ALS 표준치료와 동일한 질병 스펙트럼입니다. 다만 이번 팩에는 RCT 직접 근거가 포함되어 있지 않아 신중한 접근이 필요합니다. 나머지 9건의 예측 후보는 기전 개연성이 낮거나 근거가 전무하여 Hold 상태를 유지합니다.

**진행하려면 필요한 것:**
- 한국 내 허가/시판 현황 확인 (식약처 자료 크로스체크) — 현재 Blocking Data Gap
- 공식 허가사항(경고·금기·DDI) 확보 — 안전성 초기 평가(S1) 진입을 위한 필수 요건
- ALS 감수성 적응증에 대한 RCT 수준 근거 추가 확인
- 하위운동신경세포 질환 스펙트럼(단일근위축증, Mills 증후군, ALS 22형)은 기전적 개연성은 있으나 근거가 없어 추가 문헌/사례 조사 필요
- 나머지 5건의 초저품질 예측(선천성/발달성 질환)은 TxGNN 예측 잡음으로 판단, 별도 조치 불필요
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

