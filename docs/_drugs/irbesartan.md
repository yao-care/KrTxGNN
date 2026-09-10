---
layout: default
title: Irbesartan
parent: 僅模型預測 (L5)
nav_order: 406
evidence_level: L5
indication_count: 4
---

# Irbesartan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Irbesartan: 고혈압에서 악성 고혈압성 신장질환(Malignant Hypertensive Renal Disease)으로

## 한 문장 요약

Irbesartan은 안지오텐신 II 수용체 차단제(ARB) 계열 약물로, 고혈압 및 당뇨병성 신증 치료에서의 신장보호 효과로 알려져 있습니다.
TxGNN 모델은 **악성 고혈압성 신장질환**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 **임상시험이나 문헌은 확인되지 않았습니다** — 모델 예측 단독 근거 단계입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (Evidence Pack 내 미제공, ARB 계열로 고혈압/당뇨병성 신증에 사용된 것으로 알려짐) |
| 예측 신규 적응증 | 악성 고혈압성 신장질환 (Malignant Hypertensive Renal Disease) |
| TxGNN 예측 점수 | 99.31% |
| 근거 수준 | L5 (모델 예측만 있음, 임상시험·문헌 없음) |
| 한국 시판 현황 | 미상시 (시판되지 않음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 확보되지 않았습니다. 다만 Irbesartan은 안지오텐신 II 수용체 차단제(ARB)로서, 고혈압 및 당뇨병성 신증에서의 신장보호 효과(예: IDNT 시험이 구축한 기전적 근거)로 약리학적으로 알려져 있습니다.

악성 고혈압성 신장질환은 RAAS(레닌-안지오텐신-알도스테론계) 과활성화로 인한 신혈관 손상이 핵심 병태생리이므로, AT1 수용체를 차단하는 ARB가 기전상 적용될 가능성은 이론적으로 있습니다.

다만 이 연관성은 약리학적 일반 지식에 기반한 추론이며, 본 Evidence Pack에서는 이 특정 적응증을 직접 뒷받침하는 임상시험이나 문헌이 확인되지 않았습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 한국 시판 정보

현재 한국(현지)에 허가된 제품이 없습니다 (미상시, 허가증 0건).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
근거 수준이 L5(모델 예측만 존재)이며, 관련 임상시험과 문헌이 전혀 확인되지 않았습니다. 또한 작용 기전(MOA)과 국내 허가사항(경고·금기) 데이터가 모두 확보되지 않아 안전성 초기 평가(S1) 진입이 불가능한 상태입니다.

**진행하려면 필요한 것:**
- TFDA(관할 규제기관) 공식 사이트에서 허가사항(경고/금기) PDF 확보 및 파싱 — 안전성 초기 평가의 선행 조건 (Blocking)
- DrugBank API를 통한 상세 작용 기전(MOA) 데이터 확인
- 악성 고혈압성 신장질환 관련 임상시험/문헌 재검색 (현재 검색 결과 0건)
- 국내 시판 여부 확인 및 허가 현황 갱신
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

