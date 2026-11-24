---
layout: default
title: Lipegfilgrastim
parent: 모델 예측만 (L5)
nav_order: 479
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-24
description: "Lipegfilgrastim: 예측 신규 적응증 혈소판 일차 분비 장애 (primary release disorder of platelets) (근거 수준 L5). 기존 적응증: 고형암 및 악성 림프종에 대한 세포독성 화학요법을 투여 받는 성인 및 2세 이상 소아 환자의 중증…"
monitor_inn: "LIPEGFILGRASTIM"
predicted_indications: ["primary release disorder of platelets", "severe nonproliferative diabetic retinopathy", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "diabetic retinopathy"]
---

# Lipegfilgrastim
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **5** 건
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

## Lipegfilgrastim: 호중구감소증 치료제에서 혈소판 분비 장애로
{: .text-alpha }

## 한 문장 요약

Lipegfilgrastim은 페그화(pegylated) G-CSF 유사체로, 호중구 생성을 촉진하는 약물입니다. TxGNN 모델은 **혈소판 일차 분비 장애(primary release disorder of platelets)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험과 문헌은 현재 0건**이며 모델 예측만 존재합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 고형암 및 악성 림프종에 대한 세포독성 화학요법을 투여 받는 성인 및 2세 이상 소아 환자의 중증 호중구감소증 기간 감소 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202401533/EE)) |
| 예측 신규 적응증 | 혈소판 일차 분비 장애 (primary release disorder of platelets) |
| TxGNN 예측 점수 | 0.9993 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

ChEMBL(EMBL-EBI)에 등록된 Lipegfilgrastim의 작용 기전(비공식 번역): “과립구 집락 자극 인자 수용체 효능제”. 영어 원문: "Granulocyte colony stimulating factor receptor agonist" ([ChEMBL CHEMBL4594230 (lipegfilgrastim): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL4594230), CC BY-SA 3.0; 확인일 2026-11-19). 알려진 정보에 따르면 Lipegfilgrastim은 G-CSF 수용체를 통해 호중구 계열의 증식과 분화를 촉진하는 페그화 G-CSF 유사체입니다.

그러나 이 기전과 혈소판 과립 방출 또는 분비 결함 사이에는 확립된 연관성이 없습니다. 이 점수는 TxGNN 모델(딥러닝)에서 나온 것으로, 생물학적 근거라기보다 모델이 관련 질환들 사이에서 학습한 유사성을 반영한 것일 수 있습니다. 따라서 이 예측은 가설 수준으로만 해석해야 합니다.

### 참고: 다른 예측 후보

| 순위 | 예측 질환 | TxGNN 점수 | 근거 수준 | 비고 |
|------|---------|-----------|----------|------|
| 2 | 중증 비증식성 당뇨망막병증 | 0.9991 | L5 | G-CSF가 혈관신생 세포를 동원할 가능성이 있어 망막 질환에서는 안전성 우려도 있음 |
| 3 | 가성 폰빌레브란트병 | 0.9991 | L5 | 혈소판 GPIb-alpha 기능 획득 결함으로, 기전적 연결 고리가 없음 |
| 4 | 글란츠만 혈소판무력증 | 0.9991 | L5 | 인테그린 αIIbβ3 결함으로, 기전적 연결 고리가 없음 |
| 5 | 당뇨망막병증 | 0.9975 | L5 | 2순위와 동일한 추측성 연관 및 안전성 우려 |

모든 후보에서 임상시험과 문헌 근거가 없습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 202401533 | 롱퀵스바이알주(리페그필그라스팀) | 무색투명한 액이 무색투명한 바이알에 든 주사제 | (주)한독테바 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202401533/EE) | 유효 |
| 201505171 | 롱퀵스프리필드주(리페그필그라스팀) | 무색투명한 액이 무색투명한 프리필드시린지에 든 주사제 | (주)한독테바 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201505171/EE) | 유효 |

<!-- licenses:end -->

두 제품 모두 (주)한독테바 제조입니다(허가 건수와 상태는 빠른 개요와 위 표 참조).

<!-- review:begin kr-lic-20261124c-lipegfilgrastim-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “두 제품 모두 (주)한독테바 제조이며, 단일 성분 제제로 현재 유효한 상태입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 이 사이트 자료의 성분란에는 일치한 성분만 기록되어 허가 품목별 단일 성분·복합 성분 여부를 확인할 수 없으므로, 단일·복합 표기를 빼고 건수는 쓰지 않고 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-lipegfilgrastim-1 -->

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

다만 당뇨망막병증 관련 예측에 대해서는, G-CSF가 혈관신생을 촉진하는 세포를 동원할 가능성이 이론적으로 제기되어 있어 망막 질환에서의 안전성 문제를 별도로 검토해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측은 모델 점수에만 의존하며(L5), 임상시험과 문헌 근거가 전혀 없습니다. 또한 Lipegfilgrastim의 기전과 예측된 혈소판 질환 사이에 알려진 생물학적 연결 고리가 없습니다.

**진행하려면 필요한 것:**
- 허가사항(경고, 금기, 적응증)의 확보 및 분석: 식약처 허가증 PDF 기반
- 상세한 약물 작용 기전(MOA) 데이터 확보
- 예측 질환과의 기전적 연관성을 뒷받침하는 전임상 또는 문헌 근거
- 투여 경로 적합성 평가
- 당뇨망막병증 계열 후보를 검토할 경우 망막 혈관신생 관련 안전성 평가

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 (2026-11-20 수정, 이전 판은 기록에 보존) | [ChEMBL CHEMBL4594230 (lipegfilgrastim): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL4594230) |
| 2026-11-24 | 단일·복합 표기: “두 제품 모두 (주)한독테바 제조이며, 단일 성분 제제로 현재 유효한 상…” → 확인할 수 없는 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

