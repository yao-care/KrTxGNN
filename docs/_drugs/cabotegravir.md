---
layout: default
title: Cabotegravir
parent: 僅模型預測 (L5)
nav_order: 159
evidence_level: L5
indication_count: 5
---

# Cabotegravir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Cabotegravir: HIV 감염증에서 류마티스 관절염으로

## 한 문장 요약

Cabotegravir는 HIV-1 통합효소 억제제(INSTI) 계열의 항레트로바이러스제로, HIV-1 감염 치료 및 노출 전 예방(PrEP)에 사용됩니다.
TxGNN 모델은 **류마티스 관절염(Rheumatoid Arthritis)**에 효과가 있을 수 있다고 예측하나,
현재 이를 지지하는 임상시험이나 문헌 근거는 **전무**합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | HIV-1 감염 치료 및 노출 전 예방(PrEP) |
| 예측 신규 적응증 | 류마티스 관절염 (Rheumatoid Arthritis) |
| TxGNN 예측 점수 | 99.45% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Cabotegravir는 HIV-1 복제 과정 중 통합효소(integrase)의 스트랜드 전이(strand transfer) 단계를 차단하는 INSTI 계열 약물입니다. 장기 지속형 주사제(Cabenuva: cabotegravir + rilpivirine 복합제) 및 PrEP 단독 제제(Apretude)로 활용됩니다. 다만 현재 이 Evidence Pack에는 상세 작용 기전(MOA) 데이터가 확인되지 않아, 이하 분석은 제한적임을 먼저 밝힙니다.

류마티스 관절염(RA)과의 기전적 연결은 주로 **인간 내인성 레트로바이러스(HERV)** 가설에 근거합니다. HERV가 RA를 비롯한 자가면역질환에서 촉염증(pro-inflammatory) 역할을 할 수 있으며, INSTI 계열 약물이 이론적으로 HERV의 통합효소 활성을 억제함으로써 면역 과활성화를 완화할 수 있다는 추론입니다.

그러나 이 가설은 현재 **순수한 추론 수준**에 그칩니다. 체외(in vitro) 실험이나 동물 실험을 통한 검증이 이루어진 바 없으며, Cabotegravir의 항HERV 활성 역시 임상적으로 확인된 바 없습니다. 따라서 이번 예측은 지식 그래프 내 노드 구조적 인접성에서 비롯된 것으로, 생물학적 개연성은 현 시점에서 매우 낮은 수준으로 평가됩니다.

---

## 임상시험 근거

현재 Cabotegravir와 류마티스 관절염에 관한 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 Cabotegravir와 류마티스 관절염에 관한 관련 문헌이 없습니다.

---

## 한국 시판 정보

Cabotegravir는 현재 한국에 허가된 제품이 없습니다 (허가증 수: 0건).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
류마티스 관절염에 대한 임상시험 및 문헌 근거가 전혀 없는 L5 수준의 모델 예측에 불과하며, HERV 가설에 근거한 기전적 연결도 전임상 단계의 검증조차 이루어지지 않았습니다. 추가로, 이번 Evidence Pack에 포함된 상위 5개 예측 모두 동일하게 L5/Hold 판정을 받았으며, 어떤 적응증에도 지지 근거가 존재하지 않습니다.

**진행하려면 필요한 것:**
- Cabotegravir의 상세 작용 기전(MOA) 데이터 확보 (DrugBank API 조회)
- HERV와 RA 간 기전적 연결에 대한 체외 또는 동물 실험 근거 탐색
- 항레트로바이러스제(특히 INSTI 계열)와 자가면역질환 간 연관성을 다룬 관찰 연구 문헌 검토
- 한국 식약처(MFDS) 허가 현황 및 안전성 정보(경고, 금기) 확인
- TFDA 허가사항 PDF 다운로드 및 경고·금기 데이터 보완 (DG001 해소)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

