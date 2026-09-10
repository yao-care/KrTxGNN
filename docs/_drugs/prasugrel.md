---
layout: default
title: Prasugrel
parent: 僅模型預測 (L5)
nav_order: 570
evidence_level: L5
indication_count: 10
---

# Prasugrel
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

# Prasugrel: 항혈소판제에서 폐고혈압으로

## 한 문장 요약

Prasugrel은 Evidence Pack 내 문헌에서 thienopyridine 계열 P2Y12 억제제(항혈소판제)로 언급되나, 공식 기존 적응증 및 작용기전 데이터는 확보되지 않았습니다.
TxGNN 모델은 **폐고혈압(Pulmonary Hypertension)**에 효과가 있을 수 있다고 예측(점수 99.88%)하지만, 첨부된 임상시험 2건과 문헌 2편 모두 prasugrel이나 폐고혈압과 직접 관련이 없어 **근거 불일치(mismatch)** 사례로 분류됩니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (한국 미시판, 허가 데이터 없음) |
| 예측 신규 적응증 | 폐고혈압 (Pulmonary Hypertension) |
| TxGNN 예측 점수 | 99.88% |
| 근거 수준 | L5 (실제 지지 연구 없음) |
| 한국 시판 현황 | 미판매 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

Prasugrel에 대한 공식 작용기전(MOA) 데이터는 현재 확보되지 않았습니다. 다만 Evidence Pack 내 다른 예측(편두통) 관련 문헌에서 "thienopyridine 계열 P2Y12 억제제"로 언급되어, 항혈소판제 계열임을 간접적으로 확인할 수 있습니다.

이론적으로는 혈소판 활성화와 국소 혈전 형성이 일부 폐고혈압의 혈관 리모델링 기전에 관여하므로, 항혈소판제가 이론적 효익을 가질 수 있다는 가설은 성립합니다. 그러나 제공된 임상시험과 문헌은 이 가설을 실제로 뒷받침하지 못합니다 — 하나는 심방세동 환자의 NOAC 사용 실태 관찰 연구, 다른 하나는 암 관련 혈전증 환자 선별 연구로, 둘 다 prasugrel 투여나 폐고혈압 치료와 직접적인 관련이 없습니다.

즉, TxGNN 알고리즘이 높은 예측 점수(99.88%)를 부여했음에도, 실제 검증 가능한 임상적·문헌적 근거는 이 예측을 뒷받침하지 못하는 **"고점수-저근거" 불일치 사례**입니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03993119](https://clinicaltrials.gov/study/NCT03993119) | N/A | 완료 | 500 | 스페인 고령 비판막성 심방세동 환자의 NOAC 사용 실태 관찰 연구 (prasugrel·폐고혈압 무관) |
| [NCT04846556](https://clinicaltrials.gov/study/NCT04846556) | N/A | 완료 | 300 | 암 관련 정맥혈전색전증 환자의 임상시험 적격성 후향적 분석 (prasugrel·폐고혈압 무관) |

⚠️ 두 시험 모두 관련성 등급 "C"(낮음)로 평가되었으며, prasugrel의 폐고혈압 치료 효능을 직접 검증하지 않습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Cohort | Curr Med Res Opin | PCI 시행 급성관동맥증후군 환자의 clopidogrel 순응도 관련 요인 분석 (폐고혈압 무관) |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Cohort | Kardiologiia | COVID-19 감염 전 만성질환 배경 약물치료가 치명적 결과에 미치는 영향 (폐고혈압 무관) |

두 문헌 모두 폐고혈압을 직접 다루지 않으며, prasugrel 단독 효능에 대한 데이터도 포함하지 않습니다.

## 한국 시판 정보

현재 한국에서 시판되는 prasugrel 허가 제품이 없습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (TFDA 라벨 데이터 미확보 — 아래 참고)

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 점수는 높으나, 제공된 임상시험 및 문헌 근거가 prasugrel-폐고혈압 관계와 직접적으로 연결되지 않는 명백한 불일치 사례입니다. 또한 한국 내 미시판 상태이며, 안전성 초기 평가(S1)에 필요한 TFDA 허가사항 경고/금기 정보가 Blocking 수준의 데이터 갭(DG001)으로 확보되지 않아 안전성 평가 자체가 불가능합니다.

**진행하려면 필요한 것:**
- TFDA(또는 원개발국 허가기관) 공식 라벨 PDF 확보 및 경고·금기 정보 파싱 (DG001, Blocking)
- DrugBank API를 통한 공식 작용기전(MOA) 데이터 확보 (DG002)
- prasugrel과 폐고혈압을 직접 다루는 전임상/임상 연구 확보
- 항혈소판제-폐혈관 리모델링 기전에 대한 메커니즘 연구

---

**참고:** 동일 Evidence Pack 내 **편두통(migraine disorder, rank 2)** 예측은 근거 수준 L4·S1(Research Question)로, thienopyridine 계열 약물(clopidogrel/prasugrel)이 卵円孔 미閉(PFO) 동반 편두통 환자에서 증상을 완화했다는 파일럿 연구 및 후향적 리뷰가 존재해 폐고혈압 예측보다 상대적으로 근거가 견고합니다. 별도 평가를 권장합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

