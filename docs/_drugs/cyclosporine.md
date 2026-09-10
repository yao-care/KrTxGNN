---
layout: default
title: Cyclosporine
parent: 僅模型預測 (L5)
nav_order: 228
evidence_level: L5
indication_count: 7
---

# Cyclosporine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Cyclosporine: 면역억제(이식 거부반응 예방)에서 만성육아종병(상염색체 열성)으로

## 한 문장 요약

Cyclosporine은 일반적으로 장기·조혈모세포 이식 거부반응 예방 등 면역억제 목적으로 사용되는 약물입니다. TxGNN 모델은 **만성육아종병(Chronic Granulomatous Disease, 상염색체 열성형)**에 효과가 있을 수 있다고 예측하며, 현재 **1건의 임상시험(Phase 1, 완료)**과 **1편의 관련 문헌**이 이 방향을 뒷받침하지만, 근거 수준은 아직 낮은 단계입니다.

> ⚠️ 본 약물은 한국 내 허가 자료(적응증, 경고·금기)가 확보되지 않은 상태(TFDA 첨부문서 미확보, Blocking 등급 Data Gap)이므로, 아래 결론은 잠정적입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 자료 없음 (허가 적응증·라이선스 데이터 미확보. 일반적으로 알려진 용도는 이식 거부반응 예방 등 면역억제) |
| 예측 신규 적응증 | 만성육아종병 (Granulomatous Disease, Chronic, Autosomal Recessive) |
| TxGNN 예측 점수 | 99.68% (순위 6184위) |
| 근거 수준 | L4 (조기 임상시험/증례 수준, RCT 아님) |
| 한국 시판 현황 | 미시판 (未上市) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 확보되지 않았습니다. 다만 일반적으로 cyclosporine은 T세포 활성화를 억제하는 칼시뉴린 억제제 계열 면역억제제로 알려져 있으며, 동종 조혈모세포이식(HSCT) 시 이식편대숙주병(GvHD) 예방 목적으로 널리 병용되고 있습니다.

만성육아종병(CGD)은 NADPH 옥시다제 결함으로 인한 선천성 면역결핍질환으로, 근본적 완치법은 동종 조혈모세포이식입니다. 즉 cyclosporine이 CGD "치료제"로 직접 작용하는 것이 아니라, CGD 환자가 받는 이식 시술 과정에서 GvHD 예방을 위한 표준 병용 면역억제제로 사용되는 맥락에서 연관성이 나타난 것으로 해석됩니다. TxGNN 예측은 이러한 "이식 절차 동반 사용"이라는 간접적 연관성을 포착했을 가능성이 있으며, CGD 자체의 병태생리(면역세포 기능 이상)에 대한 직접적 기전 근거는 아직 확인되지 않았습니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01917708](https://clinicaltrials.gov/study/NCT01917708) | Phase 1 | 완료 | 10 | 비악성 질환(CGD 포함)으로 동종조혈모세포이식을 받는 소아·청소년에서 abatacept를 cyclosporine + mycophenolate mofetil과 병용해 GvHD 예방 효과 및 내약성을 평가한 단일군 연구. 2년간 추적 관찰. |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [22078471](https://pubmed.ncbi.nlm.nih.gov/22078471/) | 2012 | 후향적 코호트 | J Allergy Clin Immunol | 형제·비혈연 공여자 조혈모세포이식을 받은 만성육아종병(CGD) 환자에서 우수한 생존율을 보고. 이식 시 병용 면역억제(cyclosporine 등)의 안전성·유효성을 뒷받침. |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

(경고·금기·DDI 데이터가 확보되지 않았으며, TFDA 첨부문서 미확보는 Blocking 등급 Data Gap으로 안전성 초기 평가(S1) 진입이 불가한 상태입니다.)

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 최상위 예측 후보의 근거가 완료된 Phase 1 단일군 시험(비교군 없음) 1건과 후향적 코호트 문헌 1편에 불과해 L4 수준으로 낮으며, cyclosporine이 CGD를 직접 치료한다기보다 이식 시술의 병용 면역억제제로 사용된 맥락에 가깝습니다.
- 안전성 평가에 필수적인 첨부문서(경고·금기) 데이터가 Blocking 등급 Data Gap으로 미확보되어 있어 안전성 초기 평가(S1) 진입 자체가 불가능합니다.
- 해당 약물은 한국 내 미시판 상태(허가증 0건)로, 현지 규제 맥락에서의 적응증·용법 정보도 없습니다.
- 나머지 예측 후보(순위 3~7위)는 임상시험·문헌 근거가 전무한 L5 수준으로, 모두 Hold 판정이 이미 내려져 있습니다.

**진행하려면 필요한 것:**
- TFDA(또는 관련 규제기관) 첨부문서 원문 확보 및 파싱 (DG001, Blocking)
- DrugBank 등에서 상세 작용기전(MOA) 데이터 확보 (DG002, High)
- CGD 환자를 대상으로 cyclosporine 자체의 직접적 치료 효과를 평가하는 대조군 임상연구 확인
- DDI 데이터베이스 재조회 (현재 조회 결과 not_found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

