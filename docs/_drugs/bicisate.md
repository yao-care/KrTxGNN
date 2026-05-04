---
layout: default
title: Bicisate
parent: 僅模型預測 (L5)
nav_order: 140
evidence_level: L5
indication_count: 10
---

# Bicisate
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

# Bicisate: 뇌 관류 영상 진단에서 골관절염으로

## 한 문장 요약

Bicisate(ECD, Ethyl Cysteinate Dimer)는 친지성 중성 아민 복합체로, 혈뇌장벽을 통과한 뒤 뉴런 내 에스테라제에 의해 분해·축적되는 특성을 이용한 **뇌 관류 SPECT 영상 진단제**입니다.
TxGNN 모델은 **골관절염(Osteoarthritis)**에 효과가 있을 수 있다고 예측하나,
현재 이를 지지하는 **임상시험 및 관련 문헌이 전혀 없으며**, 모델 예측만 존재합니다(L5).

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 뇌 관류 SPECT 영상 진단 |
| 예측 신규 적응증 | 골관절염 (Osteoarthritis) |
| TxGNN 예측 점수 | 98.42% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 수집되지 않았습니다. 알려진 정보에 따르면, Bicisate는 반시스테인 다이에스터 구조의 친지성 소분자로, 정맥 투여 후 혈뇌장벽을 신속히 통과합니다. 뇌 세포 내 에스테라제에 의해 친수성 복합체로 전환되어 뇌 조직에 체류하는 이 특성을 이용해, 방사성 동위원소(⁹⁹ᵐTc)와 표지한 형태로 뇌 혈류량 측정을 위한 SPECT 영상에 사용됩니다. 즉, 이 약물의 본질은 **영상 진단용 방사성 의약품**이며 치료 기전이 없습니다.

골관절염의 핵심 병리는 연골 세포 사멸, 세포외기질(ECM) 분해, 활막 염증 및 뼈 리모델링으로 구성됩니다. Bicisate의 뇌 혈류 추적 기전과 이들 병리 사이에는 어떠한 기전적 교점도 존재하지 않습니다. 예측 점수가 높게 나타난 것은 지식 그래프 내 근골격계 질환 노드 간의 **위상적 유사성(topological proximity)에 의한 위음성 연관(false association)**일 가능성이 높습니다.

주목할 점은 상위 10개 예측 적응증 중 간 관련 질환 3종(hepatopulmonary syndrome, idiopathic copper-associated cirrhosis, early-onset familial noncirrhotic portal hypertension)의 TxGNN 점수가 소수점 10자리까지 완전히 동일(0.9737175703048706)하다는 사실입니다. 이는 독립적 예측이 아닌 **그래프 클러스터링 아티팩트(graph clustering artifact)**의 전형적 징표이며, 이번 Evidence Pack 전체 예측의 신뢰도를 낮춥니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

> **참고**: 2순위 예측 적응증(류마티스 관절염)에서 4편의 문헌이 검색되었으나, 전부 Tc-99m ECD를 이용한 **뇌 SPECT 진단 연구**(Sjögren 증후군, 섬유근육통의 뇌혈류 측정)입니다. Bicisate를 류마티스 관절염 치료에 사용한 근거는 아니며, Sjögren 증후군이 RA와 합병할 수 있다는 공병 네트워크를 통해 TxGNN이 위관련성을 생성한 것으로 해석됩니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
모든 예측 적응증에서 임상시험 및 직접 문헌 근거가 전무하고(근거 수준 L5), Bicisate는 치료 기전이 없는 방사성 영상 진단제로서 골관절염을 비롯한 어떤 예측 질환과도 합리적인 기전 연결고리가 없습니다. 또한 다수 예측에서 확인된 완전 동일 점수는 모델 아티팩트를 강하게 시사합니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 상세 데이터 수집 (DrugBank API 조회로 DG002 해소)
- 한국 허가사항 경고·금기 정보 수집 (DG001 해소)
- 약물 고유 특성(뇌 혈류 영상 추적)을 활용한 **신경계 적응증 방향**으로의 재탐색 고려 (예: 뇌졸중 진단 보조, 치매 진단 보조 등)
- TxGNN 예측 점수의 클러스터링 아티팩트 여부를 확인하기 위한 모델 해석 가능성(explainability) 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

