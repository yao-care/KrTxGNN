---
layout: default
title: Etravirine
parent: 僅模型預測 (L5)
nav_order: 307
evidence_level: L5
indication_count: 10
---

# Etravirine
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

# Etravirine: HIV-1 감염에서 유인원면역결핍바이러스(SIV) 감염으로

## 한 문장 요약

Etravirine(DrugBank DB06414)은 근거 자료 내 문헌상 HIV-1 치료경험 환자에서 사용되는 비핵산계 역전사효소 억제제(NNRTI)로 확인됩니다. TxGNN 모델은 **유인원면역결핍바이러스(SIV) 감염**에 효과가 있을 수 있다고 예측(점수 99.98%)했지만, 이를 뒷받침하는 근거는 **임상시험 0건, 관련성 낮은 전임상 문헌 1편**뿐이며, 해당 문헌조차 SIV나 etravirine을 직접 검증하지 않았습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음(공식 등재 정보 미확보) — 근거 자료 내 예측 근거 텍스트상 HIV-1 감염(치료경험 성인) 치료제로 언급됨 |
| 예측 신규 적응증 | 유인원면역결핍바이러스 감염 (Simian Immunodeficiency Virus Infection) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 확보되지 않았습니다(Data Gap). 다만 근거 자료의 예측 근거 설명에 따르면, SIV는 영장류 모델 바이러스로 HIV와 동일하게 역전사바이러스(retrovirus)에 속하며, 이론적으로 NNRTI 계열 약물이 종을 넘어선 억제 효과를 가질 가능성이 있다고 서술되어 있습니다.

그러나 이를 뒷받침하는 유일한 문헌은 나노입자 기반 항레트로바이러스 병용요법에 대한 체외(in vitro)/세포 수준 연구로, SIV 동물모델이나 etravirine 자체를 특이적으로 검증한 것이 아닙니다. 즉 기전상 가능성은 제시되나, SIV 감염에 대한 etravirine 특이적 검증은 이루어지지 않았습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [26529558](https://pubmed.ncbi.nlm.nih.gov/26529558/) | 2015 | 전임상(나노입자/체외) | Molecular Pharmaceutics | 나노입자 기반 항레트로바이러스 약물 병용요법이 세포-유리 및 세포-세포 간 HIV 전파를 상승적으로 억제함을 보고. SIV나 etravirine 특이적 검증은 포함되지 않음 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 신규 적응증(SIV 감염)에 대한 근거는 임상시험 0건, 종·약물 특이적이지 않은 전임상 문헌 1편뿐으로 L5(모델 예측만 존재) 수준입니다. 약물의 기존 적응증, 작용 기전(MOA), 한국 내 안전성 정보(경고·금기·DDI) 모두 확보되지 않아 초기 안전성 평가(S1) 진입 자체가 불가능한 상태입니다.

**진행하려면 필요한 것:**
- DrugBank API를 통한 상세 작용 기전(MOA) 확보
- 식약처(또는 원자료 출처) 등재 여부 확인 및 공식 적응증·경고문 확보
- SIV 동물모델 또는 세포주에서 etravirine 특이적 항바이러스 효력시험
- (참고) 동일 근거 자료 내 예측 순위 4위 "AIDS related complex", 5위 "congenital human immunodeficiency virus"는 etravirine 특이적 임상시험(NCT04630002, NCT00855335 등)이 존재하여 근거 수준이 L2로 더 높습니다. 우선순위 재검토 시 함께 고려할 가치가 있습니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

