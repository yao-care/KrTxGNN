---
layout: default
title: Trastuzumab Emtansine
parent: 僅模型預測 (L5)
nav_order: 696
evidence_level: L5
indication_count: 10
---

# Trastuzumab Emtansine
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

# Trastuzumab emtansine (T-DM1): HER2 양성 유방암에서 유방암 정상유사아형(Normal-like Subtype)으로

## 한 문장 요약

Trastuzumab emtansine(T-DM1)은 HER2를 표적으로 하는 항체-약물 접합체로, HER2 양성 유방암 치료에 사용되어 온 약물입니다.
TxGNN 모델은 **유방암 정상유사아형(Normal Breast-like Subtype)**에 효과가 있을 수 있다고 예측하지만,
현재 이를 뒷받침하는 근거는 **관련성 낮은 임상시험 1건**뿐이며 **관련 문헌은 없습니다.**

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | HER2 양성 유방암 (Evidence Pack에는 데이터 없음 — 일반 공개 정보 기준) |
| 예측 신규 적응증 | 유방암 정상유사아형 (Normal Breast-like Subtype of Breast Carcinoma) |
| TxGNN 예측 점수 | 99.82% |
| 근거 수준 | L4 |
| 한국 시판 현황 | 미출시 (한국 내 시판 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다(DrugBank MOA 조회 필요 — Data Gap). 알려진 정보에 따르면, Trastuzumab emtansine(T-DM1)은 HER2를 표적으로 하는 단클론항체 트라스투주맙에 세포독성 물질 DM1(메이탄신 유도체, 미세소관 억제제)을 결합한 항체-약물 접합체(ADC)입니다. HER2 양성 유방암 세포에 선택적으로 결합해 세포독성 약물을 전달하는 방식으로 작용합니다.

그러나 정상유사아형(Normal-like subtype)은 본질적으로 이질성이 높고 HER2 발현이 일관되지 않은 아형으로, 전형적인 HER2 구동 종양이 아닙니다. 현재 기전 가설은 약한 편이며, 단지 다른 HER2 양성 유방암 아형과 병리학적 배경을 공유한다는 이유로 TxGNN이 높은 점수를 부여한 것으로 보입니다. 즉, 기전상 직접적인 적용 근거는 부족합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT06348134](https://clinicaltrials.gov/study/NCT06348134) | Phase 2 | 모집중 | 74 | 나이지리아 HER2 양성 유방암 여성 대상 수술 전후 항HER2 치료 유효성·안전성 평가 — normal-like 아형 특이적 설계 아니며 대상군 정의 불일치 |

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (HER2 표적 항체-약물접합체, 세포독성 페이로드 DM1 탑재) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | CBC(혈소판 수치 포함), 간기능 검사 |
| 취급 방호 | 세포독성 의약품 취급 규정 준수 필요 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (한국 허가사항 경고/금기/DDI 정보 모두 미확보 — Blocking 데이터 갭)

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
정상유사아형에 특화된 임상시험은 1건(Phase 2, 모집중)뿐이며 대상군 정의가 맞지 않고(나이지리아 HER2+ 전체 대상, normal-like 특이적 아님), 관련 문헌은 전무합니다. 기전적으로도 이 아형은 HER2 발현이 비일관적이어서 T-DM1의 표적 기전과 직접 연결되지 않습니다.

**참고:** 동일 Evidence Pack 내 다른 예측 적응증인 프로게스테론 수용체 양성/음성 유방암(rank 2, 3)은 Phase 3 RCT를 포함한 L1 수준 근거를 보유하고 있어 상대적으로 유망합니다. 다만 이는 HER2 양성 유방암이라는 기존 승인 적응증 내 아형 검증에 가까우며, 진정한 의미의 신규 질환 재창출은 아닙니다.

**진행하려면 필요한 것:**
- 한국(MFDS) 허가사항의 경고·금기 정보 확보 (Blocking 데이터 갭, DG001)
- DrugBank MOA 상세 데이터 확보 (DG002)
- 정상유사아형에 특이적인 HER2 발현 프로파일 및 반응 예측 바이오마커 연구
- normal-like 아형 특이적 임상시험 또는 문헌 확보 (현재 관련성 낮은 시험 1건뿐)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

