---
layout: default
title: Proxyphylline
parent: 僅模型預測 (L5)
nav_order: 585
evidence_level: L5
indication_count: 10
---

# Proxyphylline
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

# Proxyphylline: 적응증 미상에서 심장질환(Heart Disease)으로

## 한 문장 요약

Proxyphylline의 기존 적응증과 작용 기전(MOA) 자료는 현재 확보되지 않았습니다.
TxGNN 모델은 **심장질환(Heart Disease)**에 효과가 있을 수 있다고 예측했으나(예측 점수 99.99%),
이를 뒷받침하는 임상시험이나 문헌은 **전혀 없으며**, 순수하게 모델 예측에만 의존하는 상태입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (원 적응증 정보 미확보) |
| 예측 신규 적응증 | 심장질환 (Heart Disease) |
| TxGNN 예측 점수 | 99.99% (rank 660) |
| 근거 수준 | L5 (모델 예측만, 실제 연구 없음) |
| 한국 시판 현황 | 미상장 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. Proxyphylline의 DrugBank ID, 약리 분류, 원 적응증 정보가 모두 미확보 상태이며, 이로 인해 기존 적응증과 예측된 심장질환 사이의 기전적 연관성을 분석할 근거가 없습니다.

TxGNN 모델은 지식그래프 상의 연결 패턴만으로 99.99%라는 높은 점수를 부여했지만, 이는 실제 약리학적 타당성을 보장하지 않습니다. 상위 10개 예측 적응증 중 9개(선천성 심장기형, 염색체 이상 증후군, 안면 발달 이상 등)는 임상시험·문헌 증거가 전무하며, 유일하게 문헌이 존재하는 8순위 예측(fucoglycosan 합성 장애)조차 1977년의 복방약물(Proxyphylline이 포함된 3성분 복합제) 연구 1편에 불과해 단일 약물의 직접 증거로 보기 어렵습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

*(참고: 8순위 예측 적응증에 한해 1977년 복합제 연구 1편[PMID [192249](https://pubmed.ncbi.nlm.nih.gov/192249/)]이 존재하나, 1순위 예측(심장질환)과는 무관합니다.)*

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (TFDA 라벨 및 DrugBank 자료 미확보로 경고·금기·상호작용 정보 확인 불가)

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 신규 적응증(심장질환)을 포함한 상위 10개 예측 전부가 임상시험·문헌 근거 없이 모델 점수(L5)에만 의존하고 있습니다. 또한 원 적응증, MOA, TFDA 허가 정보가 모두 결여되어 있어 S1 안전성 초기 평가 단계에 진입할 수 없는 상태(Blocking data gap)입니다.

**진행하려면 필요한 것:**
- TFDA 원 허가국 사용설명서(경고/금기) 확보 (DG001, Blocking)
- DrugBank API를 통한 작용 기전(MOA) 확인 (DG002, High)
- 심장질환 적응증에 대한 최소 1건 이상의 전임상 또는 임상 문헌 확보
- 위 자료 확보 전까지 본 후보물질은 평가 파이프라인에서 보류 권장
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

