---
layout: default
title: Brivaracetam
parent: 僅模型預測 (L5)
nav_order: 150
evidence_level: L5
indication_count: 10
---

# Brivaracetam
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

# Brivaracetam: 국소 발작에서 시각성 간질로

## 한 문장 요약

Brivaracetam(BRV)은 SV2A(시냅스 소포 단백질 2A)에 높은 친화력으로 결합하여 신경원의 과도한 방전을 억제하는 3세대 항전간제로, 미국·유럽 등에서 국소 발작(Focal Onset Seizures) 치료에 허가되어 있으나 한국에는 아직 시판되지 않습니다.
TxGNN 모델은 **시각성 간질(Visual Epilepsy)**에 효과가 있을 것으로 예측하며,
현재 임상시험 등록은 없으나 **19편의 문헌**이 이 방향을 간접적으로 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 국소 발작 (Focal Onset Seizures) — 미국 FDA·유럽 EMA 허가 기준, 한국 미허가 |
| 예측 신규 적응증 | 시각성 간질 (Visual Epilepsy) |
| TxGNN 예측 점수 | 99.51% |
| 근거 수준 | L3 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

시각성 간질(Visual Epilepsy)은 광민감성 간질(Photosensitive Epilepsy)과 후두엽 간질(Occipital Lobe Epilepsy)을 포괄하는 국소 간질의 아형입니다. 빛 자극이나 시각적 패턴이 후두엽 피질의 과도한 신경 방전을 촉발하며, 이는 국소 간질과 동일한 병태생리 기전을 공유합니다.

BRV는 SV2A에 levetiracetam보다 15~30배 높은 친화력으로 결합하고 혈뇌장벽 투과성도 뛰어나, 시냅스 소포의 과도한 신경전달물질 방출을 빠르게 억제합니다. 이 SV2A 조절 기전은 BRV의 허가 적응증인 국소 간질과 완전히 동일한 경로이며, 시각성 간질도 국소 간질의 연장선에 있으므로 기전상 적용 가능성이 충분합니다.

특히, 광민감성 모델(Photoparoxysmal Response, PPR)에서의 전임상 연구와 광민감성 간질 환자 대상 초기 임상 연구(PMID 17785672: Neurology 2007; PMID 32949370: CNS Drugs 2020 무작위 이중맹검 교차시험)에서 BRV가 PPR을 억제하는 효과가 직접 검증된 바 있습니다. 이는 TxGNN 예측의 생물학적 타당성을 뒷받침하는 핵심 근거입니다.

---

## 임상시험 근거

현재 시각성 간질(Visual Epilepsy)에 대한 Brivaracetam 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [38811492](https://pubmed.ncbi.nlm.nih.gov/38811492/) | 2024 | Narrative Review | Advances in Therapy | BRV 전임상 프로파일 및 임상 효능 종합 검토; SV2A 고친화성 결합, 광민감성 모델 전임상 데이터 포함 |
| [40568060](https://pubmed.ncbi.nlm.nih.gov/40568060/) | 2025 | Narrative Review | J Epilepsy Res | BRV 약리학·임상 효능·안전성 종합 분석; 고선택적 SV2A 결합 및 혈뇌장벽 신속 투과 특성 확인 |
| [31195850](https://pubmed.ncbi.nlm.nih.gov/31195850/) | 2019 | Systematic Review | Expert Rev Neurother | 국소 간질에서 BRV 효능·안전성 체계적 고찰; levetiracetam 대비 SV2A 친화력 15~30배 우수 확인 |
| [38576178](https://pubmed.ncbi.nlm.nih.gov/38576178/) | 2024 | Phase III RCT | Epilepsia Open | 아시아 성인 국소 발작 환자 대상 BRV Phase III 무작위 이중맹검 위약 대조 시험; 효능 및 안전성 확인 |
| [38970892](https://pubmed.ncbi.nlm.nih.gov/38970892/) | 2024 | Observational / Registry | Epilepsy & Behavior | 고령·청장년 간질 환자에서 BRV 효과 및 내약성 비교 (EXPERIENCE 연구 풀링 분석) |
| [39664134](https://pubmed.ncbi.nlm.nih.gov/39664134/) | 2024 | Systematic Review | Cureus | 성인·소아 간질 관리에서 BRV 역할, 이전 항전간제 전환 이유 및 효능 체계적 고찰 |
| [31937513](https://pubmed.ncbi.nlm.nih.gov/31937513/) | 2020 | Pooled Analysis | Epilepsy & Behavior | 국소 발작 보조요법으로 BRV 안전성·내약성 심층 풀링 분석 |
| [37483441](https://pubmed.ncbi.nlm.nih.gov/37483441/) | 2023 | Systematic Review / Meta-analysis | Front Neurol | 소아 간질에서 BRV 안전성·효능 체계적 고찰 및 메타분석 |
| [26165169](https://pubmed.ncbi.nlm.nih.gov/26165169/) | 2015 | Meta-analysis | Expert Opin Pharmacother | 부분 발작 보조요법으로 BRV 용량별 효능·안전성 메타분석; 위약 대비 유의한 발작 감소 확인 |
| [32120063](https://pubmed.ncbi.nlm.nih.gov/32120063/) | 2020 | Mechanistic Review | Neuropharmacology | 현행 항전간제 작용 기전 종합 고찰; SV2A를 통한 신경원 과흥분 억제 기전 상세 기술 |

---

## 한국 시판 정보

Brivaracetam은 현재 한국에 허가된 제품이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
시각성 간질은 BRV 허가 적응증인 국소 간질의 아형으로 기전적 타당성은 충분하나, 이 특정 적응증을 직접 대상으로 한 임상시험이 없으며 BRV 자체가 한국에 허가·시판되지 않아 현 단계에서는 탐색적 연구 질문으로 분류됩니다.

**진행하려면 필요한 것:**
- 한국 식품의약품안전처 허가 취득 선행 (미국 FDA/유럽 EMA 허가 자료 기반 신청 검토)
- 상세 작용 기전(MOA) 데이터 확보 (DrugBank DB05541 API 조회)
- 허가사항 경고·금기사항 정보 확인 (FDA/EMA 허가 사항 PDF 파싱)
- 광민감성 간질(Photosensitive Epilepsy) 특화 임상 연구 설계 검토
- 광민감성 모델(PPR) 관련 기존 데이터(PMID 17785672, 32949370)를 근거로 개념증명 연구 계획 수립

> **참고:** 10개 예측 적응증 중 **2위인 뇌전증 중첩증(Status Epilepticus)**은 근거 수준 L2, 권장 결정 **Proceed with Guardrails**로 평가됩니다. IV BRV의 SE 치료 효능을 직접 검증한 소아 대상 비교 임상시험(NCT07163572, N=152, 완료)이 존재하며, 2건의 체계적 문헌고찰(PMID 32278203, 31342405)을 포함한 20편의 문헌이 지지합니다. 한국 시판 허가 취득 후 SE 적응증 확장 연구를 우선 검토할 것을 권장합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

