---
layout: default
title: Thiopental
parent: 僅模型預測 (L5)
nav_order: 675
evidence_level: L5
indication_count: 10
---

# Thiopental
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

# Thiopental: 마취 유도제에서 난치성 두개내압 상승(Intracranial Hypertension)으로

## 한 문장 요약

Thiopental은 초단시간 작용 바르비투르산염으로, 전신마취 유도 및 신경외과적 응급 처치에 사용되어 온 약물입니다. TxGNN 모델은 뇌대사율(CMRO2)과 뇌혈류를 낮추는 기전을 통해 **난치성 두개내압 상승(Intracranial Hypertension)**에 효과가 있을 것으로 예측하며, 실제로 Pentobarbital과 직접 비교한 **Phase 3 RCT 1건**과 **20편 이상의 문헌**이 이를 뒷받침합니다. 같은 병태생리 범주에 속하는 가성뇌종양(Pseudotumor Cerebri, 특발성 두개내압 상승)도 가장 높은 예측 점수(99.99%)를 받았으나, 이쪽은 직접적 임상 근거가 아직 부족합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 자료 없음 (한국 미시판; 문헌상 전신마취 유도제·신경외과 응급용으로 사용) |
| 예측 신규 적응증 | 두개내압 상승 (Intracranial Hypertension) — 관련 적응증: 가성뇌종양(최고 예측 점수) |
| TxGNN 예측 점수 | 99.98% (두개내압 상승) / 99.99% (가성뇌종양) |
| 근거 수준 | L1 (두개내압 상승) |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

현재 DrugBank 기반 상세 MOA 데이터는 확보되지 않았습니다. 다만 근거 문헌에 따르면 Thiopental은 초단시간 작용 바르비투르산염으로, GABA-A 수용체를 증강시켜 뇌대사율과 뇌혈류를 감소시킵니다. 이 기전을 이용한 "바르비투르 혼수(barbiturate coma)"는 외상성 뇌손상, 뇌출혈, 전격성 간부전 등에서 발생하는 난치성 두개내압 상승의 표준 2차·3차 치료법으로 수십 년간 임상 실무에서 사용되어 왔습니다.

가성뇌종양(특발성 두개내압 상승) 역시 병태생리학적으로 "두개내압 상승"과 동일 범주에 속하므로, 이론상 같은 기전을 적용할 수 있습니다. 다만 현재 문헌은 대부분 외상·뇌졸중·간부전에 의한 이차성 두개내압 상승을 다루고 있으며, 원인 불명(특발성) 사례에 대한 직접적 근거는 아직 확인되지 않았습니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00622570](https://clinicaltrials.gov/study/NCT00622570) | Phase 3 | 중단(Terminated) | 44 | 외상성 뇌손상에 의한 난치성 두개내압 상승에서 Pentobarbital vs Thiopental 직접 비교(중도 종료되었으나 직접 근거) |
| [NCT04488874](https://clinicaltrials.gov/study/NCT04488874) | Phase 3 | 완료 | 50 | 개두술 중 뇌 이완 목적 고장성 젖산나트륨 평가 (Thiopental 직접 관련성 낮음) |
| [NCT03123302](https://clinicaltrials.gov/study/NCT03123302) | N/A | 완료 | 977 | MRI 진정 마취 후 합병증 관찰연구 (Thiopental 직접 관련성 낮음) |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [18759980](https://pubmed.ncbi.nlm.nih.gov/18759980/) | 2008 | RCT/대조비교 | Critical Care | 외상성 뇌손상 난치성 두개내압 상승에서 Pentobarbital 대비 Thiopental의 두개내압 조절 효과 우위 |
| [15756405](https://pubmed.ncbi.nlm.nih.gov/15756405/) | 2005 | 예비 보고 (n=20) | Neurocirugia | Pentobarbital vs Thiopental 효과 비교 예비 결과 |
| [7189982](https://pubmed.ncbi.nlm.nih.gov/7189982/) | 1980 | 대조연구 | Anesth Analg | 개두술 중 급성 두개내압 상승 조절: Lidocaine vs Thiopental |
| [2759548](https://pubmed.ncbi.nlm.nih.gov/2759548/) | 1989 | 코호트 | Hepatology | 전격성 간부전 합병 두개내압 상승에서 Thiopental 주입 치료 |
| [37676578](https://pubmed.ncbi.nlm.nih.gov/37676578/) | 2023 | 관찰연구 (n=891) | Neurosurgical Review | 동맥류성 지주막하출혈에서 Thiopental + 감압개두술 최종 단계 치료의 기능적 회복 평가 |
| [18983702](https://pubmed.ncbi.nlm.nih.gov/18983702/) | 2008 | 논평 | Critical Care | 외상성 뇌손상 두개내압 상승 치료에서 바르비투르산염 사용의 쟁점 논의 |
| [18066523](https://pubmed.ncbi.nlm.nih.gov/18066523/) | 2008 | Review | Intensive Care Med | 외상성 뇌손상 난치성 두개내압 상승과 2차 치료(과호흡, 바르비투르, 감압개두술) |
| [17167826](https://pubmed.ncbi.nlm.nih.gov/17167826/) | 2006 | Review | World J Gastroenterol | 전격성 간부전에서 뇌부종·두개내압 상승의 병태생리와 관리 |
| [10213432](https://pubmed.ncbi.nlm.nih.gov/10213432/) | 1999 | 시뮬레이션 연구 | J Neurosurg Anesthesiol | Thiopental, Propofol, Etomidate의 마취 유도 시 두개내압 변화 비교 |
| [1844198](https://pubmed.ncbi.nlm.nih.gov/1844198/) | 1991 | 대조연구 (n=122) | Agressologie | 외상성 뇌손상에서 Mannitol 대비 Thiopental의 뇌관류압·EEG 효과 |

---

## 한국 시판 정보

현재 한국에는 Thiopental 허가 제품이 없습니다(미시판, 허가증 0건).

---

## 안전성 고려사항

주요 경고, 금기, 약물상호작용에 대한 데이터가 현재 확보되지 않았습니다(TFDA 등 규제기관 첨부문서 미확보). 바르비투르 혼수 요법은 임상 실무상 저혈압, 면역억제, 심근억제 등의 위험이 알려져 있으므로, 실제 적용 전 최신 첨부문서 및 전문가 자문을 통한 별도 안전성 평가가 반드시 필요합니다.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
두개내압 상승에 대해서는 Pentobarbital과의 직접 비교 Phase 3 RCT(조기 종료되었으나 유효한 직접 근거)와 수십 년간의 "바르비투르 혼수" 임상 실무 경험이 존재하여, 기전적·임상적 근거가 충분한 수준입니다. 다만 가성뇌종양을 포함해 이번 평가에서 함께 예측된 나머지 후보들(trichotillomania, frontal lobe epilepsy, Prinzmetal angina, migraine disorder, absence epilepsy, Tourette syndrome 등)은 근거 수준이 L4~L5에 그쳐, 대부분 Hold 또는 추가 연구가 필요한 단계입니다.

**진행하려면 필요한 것:**
- TFDA(또는 한국 식약처) 첨부문서 확보를 통한 안전성 정보 보완 (Blocking, S1 안전성 초평가 필수 선행 조건)
- DrugBank 등을 통한 상세 작용기전(MOA) 확인
- 신경중환자의학·마취과 전문가 자문을 통한 바르비투르 혼수 프로토콜 검토
- 가성뇌종양(특발성 두개내압 상승)에 특이적인 전임상·임상 근거 추가 수집
- 저혈압·면역억제 등 barbiturate coma 고유 부작용에 대한 모니터링 계획 수립
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

