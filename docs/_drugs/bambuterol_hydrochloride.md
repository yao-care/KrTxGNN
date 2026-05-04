---
layout: default
title: Bambuterol Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 121
evidence_level: L5
indication_count: 0
---

# Bambuterol Hydrochloride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Bambuterol Hydrochloride: 평가 불가 (예측 데이터 없음)

## 한 문장 요약

Bambuterol Hydrochloride는 terbutaline의 전구약물(prodrug)로, 베타-2 아드레날린 수용체 효능제 계열의 기관지 확장제입니다.
이번 Evidence Pack에서는 **TxGNN 예측 적응증이 없으며**, 한국 시판 이력도 확인되지 않아 재창출 가능성 평가를 진행하기 어렵습니다.
데이터 수집 단계의 주요 공백이 해소되기 전까지 본 보고서는 **현황 진단 목적**으로만 활용할 수 있습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 이력 없음) |
| 예측 신규 적응증 | 없음 (TxGNN 예측 결과 없음) |
| TxGNN 예측 점수 | 해당 없음 |
| 근거 수준 | 평가 불가 |
| 한국 시판 현황 | 미상市 (허가 이력 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 이 예측이 타당한 이유는?

TxGNN 모델의 예측 결과가 제공되지 않아 신규 적응증에 대한 기전적 분석을 진행할 수 없습니다.

Bambuterol Hydrochloride는 선택적 베타-2 아드레날린 수용체 효능제인 terbutaline의 carbamate 전구약물로, 체내에서 가수분해되어 활성형으로 전환됩니다. 기관지 천식 및 만성 폐쇄성 폐질환(COPD) 등의 호흡기 질환 치료에 사용된 이력이 있으며, 장시간 작용형(long-acting) 경구 기관지 확장제로 개발된 약물입니다.

재창출 후보 평가를 위해서는 TxGNN 예측 파이프라인 재실행 및 DrugBank MOA 데이터 보완이 선행되어야 합니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

*(TxGNN 예측 적응증이 없어 증거 검색의 대상 질환을 특정할 수 없습니다.)*

---

## 문헌 근거

현재 관련 문헌이 없습니다.

*(TxGNN 예측 적응증이 없어 대상 질환 기반 문헌 검색을 수행할 수 없습니다.)*

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

*(DDI 조회 결과 없음, 경고/금기 데이터 미수집 상태입니다.)*

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 결과가 없고, 한국 내 허가 이력 및 안전성 정보가 모두 수집되지 않은 상태로, 재창출 가능성에 대한 판단 자체를 내리기 어렵습니다.

**진행하려면 필요한 것:**

- **[필수] TxGNN 예측 파이프라인 재실행**: Bambuterol Hydrochloride → DrugBank ID 매핑 후 예측 결과 생성
- **[필수] DrugBank API 조회**: MOA, 약물 카테고리, 독성 데이터 수집 (DG002 해소)
- **[필수] 허가사항 확인**: 경고, 금기, 주요 부작용 데이터 확보 (DG001 해소)
- **[권장] 한국(MFDS) 또는 해외 허가 이력 조회**: 원래 적응증 및 시판 현황 확인
- **[권장] PubMed 배경 문헌 검색**: 베타-2 효능제 계열의 재창출 사례 조사
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

