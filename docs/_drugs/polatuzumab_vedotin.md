---
layout: default
title: Polatuzumab Vedotin
parent: 僅模型預測 (L5)
nav_order: 560
evidence_level: L5
indication_count: 1
---

# Polatuzumab Vedotin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Polatuzumab Vedotin: 미분류에서 HER2 양성 유방암으로

## 한 문장 요약

Polatuzumab vedotin은 항CD79b 항체약물접합체(ADC)로, 원래 미만성 거대 B세포 림프종(DLBCL) 치료에 사용됩니다. TxGNN 모델은 **HER2 양성 유방암(HER2 positive breast carcinoma)**에 효과가 있을 수 있다고 예측했으나, 현재 이를 지지하는 **임상시험이나 문헌 근거는 전혀 없습니다**.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 자료 없음 (한국 미허가) |
| 예측 신규 적응증 | HER2 양성 유방암 (HER2 positive breast carcinoma) |
| TxGNN 예측 점수 | 99.34% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미상시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, Polatuzumab vedotin은 CD79b(B세포 수용체 복합체 구성 성분)를 표적으로 하는 항체약물접합체이며, B림프구에 특이적으로 발현하는 이 항원을 통해 세포독성 페이로드를 전달합니다. 이 기전은 DLBCL(미만성 거대 B세포 림프종) 치료에 근거를 두고 있습니다.

반면 HER2 양성 유방암의 병인은 HER2/ERBB2 신호전달 경로의 과활성화이며, CD79b/B세포 수용체 신호전달 경로와는 알려진 기전상 중첩이나 상호작용이 없습니다. TxGNN이 제시한 높은 점수(99.34%)는 지식그래프 내에서 종양학 약물과 종양 적응증 간의 위상학적 유사성을 반영했을 가능성이 높으며, 실제 기전적 연관성을 의미하지 않습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 세포독성

Polatuzumab vedotin은 항체약물접합체(ADC) 계열의 세포독성 항종양제입니다.

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (항체약물접합체, anti-CD79b ADC) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | CBC, 간기능, 말초신경병증 증상 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 점수는 높지만 이를 뒷받침하는 임상시험이나 문헌이 전무하며, 기존 적응증(DLBCL)과 예측 적응증(HER2 양성 유방암) 간에 알려진 기전적 연관성이 없습니다. 안전성 정보(경고, 금기, 약물상호작용)도 모두 확보되지 않아 초기 안전성 평가(S1)조차 진행할 수 없는 상태입니다.

**진행하려면 필요한 것:**
- TFDA(대만) 또는 국내 허가사항의 경고/금기 정보 확보 (Blocking 데이터 갭)
- DrugBank API를 통한 상세 작용 기전(MOA) 확인
- HER2 양성 유방암과 CD79b/ADC 기전 간 연관성을 뒷받침할 전임상 또는 기전 연구
- 관련 임상시험 및 문헌 근거 축적 여부 지속 모니터링
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

