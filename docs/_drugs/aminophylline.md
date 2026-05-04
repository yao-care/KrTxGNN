---
layout: default
title: Aminophylline
parent: 僅模型預測 (L5)
nav_order: 57
evidence_level: L5
indication_count: 10
---

# Aminophylline
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

# Aminophylline: 기관지 경련에서 편두통으로

---

## 한 문장 요약

Aminophylline은 메틸잔틴 계열의 기관지 확장제로, 국제적으로는 기관지 경련·천식 치료에 사용되어 왔으나 대만에서는 현재 허가된 시판 제품이 없습니다.
TxGNN 모델은 **편두통(Migraine Disorder)**에 효과가 있을 수 있다고 예측하며,
현재 임상시험 등록은 없으나 **6편의 문헌**이 아데노신 수용체 길항 기전을 통한 치료 가능성을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 대만 허가 이력 없음 (국제적으로 기관지 경련·천식 치료에 사용) |
| 예측 신규 적응증 | 편두통 (Migraine Disorder) |
| TxGNN 예측 점수 | 99.88% |
| 근거 수준 | L4 |
| 대만 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, Aminophylline은 테오필린(theophylline)과 에틸렌다이아민(ethylenediamine)의 복합체이며, 주요 약리 활성은 테오필린에 의해 매개됩니다. 포스포다이에스터라제(PDE) 억제와 **아데노신 수용체(A1/A2A) 길항**이 대표적인 작용 기전으로 알려져 있습니다.

편두통의 병태생리에서 아데노신은 핵심적 역할을 담당합니다. 아데노신이 과도하게 축적되면 두개내 혈관 확장, 삼차신경 감작, 중추 통각 전달 증강이 유발되어 편두통 발작을 촉발합니다. Aminophylline이 A1/A2A 수용체를 차단함으로써 이 병태 과정에 직접 개입할 수 있습니다. 실제로 같은 메틸잔틴 계열인 카페인이 진통 협력 효과를 발휘하는 것으로 임상적으로 인정받고 있어, 기전상 평행 지지 근거를 제공합니다.

가장 직접적인 문헌인 PMID 38059379(2023, *Pain Management*)는 aminophylline의 아데노신 수용체 길항 기전이 편두통을 포함한 통증에서 강력한 치료 효과를 발휘할 수 있음을 직접 검토하고 있습니다. 다만 해당 문헌은 관찰 사례 기반의 리뷰에 머물며, 전향적 임상시험은 현재까지 등록된 바 없어 근거 수준은 L4에 그칩니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|------|------|------|---------|
| [38059379](https://pubmed.ncbi.nlm.nih.gov/38059379/) | 2023 | Review/Clinical Study | Pain Management | Aminophylline의 아데노신 수용체 길항 기전이 편두통·통증에서 강력한 치료 효과를 제공할 수 있음; 경막 후 두통 관찰 사례 포함 |
| [34308528](https://pubmed.ncbi.nlm.nih.gov/34308528/) | 2022 | Case Report | Journal of Nuclear Cardiology | 레가데노손(A2A 수용체 작용제) 투여 후 반신마비 편두통 발생; aminophylline으로 역전 성공—아데노신-편두통 기전 연결고리 시사 |
| [7728647](https://pubmed.ncbi.nlm.nih.gov/7728647/) | 1995 | Case Report | Canadian Journal of Cardiology | 아데노신 과잉 효과에 의한 증후군 X 증례; 아데노신이 혈관성 두통 반응에 관여함을 시사 |
| [219563](https://pubmed.ncbi.nlm.nih.gov/219563/) | 1979 | In Vitro | Stroke | 아데닌 화합물이 두개내 동맥만 선택적으로 확장(두개외 혈관에는 미작용); 편두통의 선택적 두개내 혈관 확장에 대한 생물학적 기전 근거 제공 |
| [14168418](https://pubmed.ncbi.nlm.nih.gov/14168418/) | 1964 | Expert Opinion | Aggiornamenti clinicoterapeutici | 내과적 두통에 관한 초기 임상 기술 |
| [5540199](https://pubmed.ncbi.nlm.nih.gov/5540199/) | 1971 | Pharmaceutical Study | The Practitioner | 좌약 제형 관련 기술 (직접적 편두통 근거 미약) |

---

## 대만 시판 정보

대만 내 Aminophylline 허가 제품이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
아데노신 수용체 길항 기전과 편두통 병태생리 간의 이론적 연결은 생물학적으로 타당하나, 전향적 임상시험이 전무하고 현재 근거가 케이스 리포트와 리뷰 문헌(L4) 수준에 그칩니다. 약물 안전성 정보(경고·금기)도 현재 확보되지 않아 1차 안전성 평가를 진행할 수 없는 상태입니다.

**진행하려면 필요한 것:**
- TFDA 허가사항 PDF 확인을 통한 경고 및 금기 정보 확보 (Blocking 데이터 갭 해소)
- DrugBank API를 통한 상세 MOA 및 안전성 프로파일 검토
- Aminophylline 편두통 치료에 관한 소규모 탐색적 임상시험 설계 가능성 검토
- 같은 계열인 카페인 대비 효능·안전성 차별성 분석

> **참고:** TxGNN 예측 순위 7위인 **폐동맥 고혈압(Pulmonary Hypertension)**은 동일 Evidence Pack 내에서 근거 수준 L3으로 훨씬 강력한 임상 지지를 보유합니다 (완료된 Phase 1 임상시험 [NCT01530464](https://clinicaltrials.gov/study/NCT01530464) 포함, 20편 문헌, 권장 결정: Research Question). 해당 적응증에 대한 별도 평가 보고서 작성을 권장합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

