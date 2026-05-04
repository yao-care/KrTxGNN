---
layout: default
title: Cyclofenil
parent: 僅模型預測 (L5)
nav_order: 189
evidence_level: L5
indication_count: 10
---

# Cyclofenil
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

# Cyclofenil: 배란 유도에서 Prinzmetal 협심증으로

## 한 문장 요약

Cyclofenil은 선택적 에스트로겐 수용체 조절제(SERM) 계열 약물로, 역사적으로 무월경 및 배란 장애 치료에 사용되었으나 현재 한국 내 허가 이력이 없습니다.
TxGNN 모델은 **Prinzmetal 협심증(변이형 협심증)**에 효과가 있을 수 있다고 예측하며,
이를 지지하는 임상시험 및 문헌 근거가 **전혀 없는** 상태입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 이력 없음 (SERM 계열; 역사적으로 배란 유도에 사용) |
| 예측 신규 적응증 | Prinzmetal 협심증 (Prinzmetal angina) |
| TxGNN 예측 점수 | 99.97% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Cyclofenil은 선택적 에스트로겐 수용체 조절제(SERM) 계열 약물입니다. 에스트로겐 수용체(ERα/ERβ)는 관상동맥 혈관 평활근세포에 광범위하게 분포하며, ER 활성화는 산화질소(NO) 생성, 칼슘 이온 통로 조절 및 혈관 긴장도에 영향을 미칩니다. 이 기전에 근거하여, Cyclofenil의 ER 조절 작용이 관상동맥 경련(coronary artery spasm)을 억제할 수 있다는 이론적 가설이 성립합니다.

다만 이 기전 추론은 일반적인 SERM 계열 문헌에서 도출된 것이며, **Cyclofenil 자체의 혈관 약리학은 직접 연구된 바 없습니다.** Cyclofenil의 조직 선택적 활성 프로필이 혈관 평활근에서 작용제(agonist)로 작용할지 길항제(antagonist)로 작용할지 현재 불명확하며, 이는 혜택-위험 방향을 예측하기 어렵게 만드는 주요 불확실성입니다.

이번 Evidence Pack에서 Prinzmetal 협심증 외에도 총 10개의 신규 적응증이 예측되었습니다. OCD(Rank 3), 불면증(Rank 5), 허혈성 뇌졸중 감수성(Rank 4), 뇌경색(Rank 10) 등은 SERM의 중추신경계·혈관계 ER 조절 기전과 연결되는 탐색적 가설을 포함합니다. 그러나 **Rank 6~9(schizotypal/paranoid/histrionic/schizoid 인격장애)는 TxGNN 점수가 완전히 동일(0.9992)** 하여 지식 그래프 위상 인공 결과(KG topology artifact)로 해석되며, 독립적인 약리 예측으로 간주하기 어렵습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
임상시험 및 문헌 근거가 전무(L5)하며, Cyclofenil 자체의 혈관 약리 데이터도 부재합니다. 기전적 가설은 일반 SERM 계열 문헌에서 간접 추론된 수준에 그치므로, 추가 전임상 근거 없이는 연구 진행을 권장하기 어렵습니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 상세 데이터 확보 (DrugBank API 조회를 통한 DG002 해소)
- 안전성 정보 확보 (허가사항 PDF 파싱을 통한 경고·금기 데이터 — DG001 해소)
- Cyclofenil의 관상동맥 혈관 평활근 ER 아형(ERα/ERβ) 선택성 및 작용 방향 검증 (전임상 수준)
- 관상동맥 경련 동물 모델에서의 효과 탐색 연구 설계
- Rank 6~9 인격장애 군집 예측은 KG topology artifact로 확인되어 추가 연구 대상에서 제외 권고
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

