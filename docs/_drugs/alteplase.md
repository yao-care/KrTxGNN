---
layout: default
title: Alteplase
parent: 모델 예측만 (L5)
nav_order: 49
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Alteplase: 예측 신규 적응증 후하벽 심근경색 (Posteroinferior Myocardial Infarction) (근거 수준 L5). 기존 적응증: 허가 적응증 텍스트 없음 (허가증에 PDF 링크만 수록, 허가사항 참조 필요)"
monitor_inn: "ALTEPLASE"
predicted_indications: ["heparin cofactor 2 deficiency", "congenital coronary artery anomaly", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "thrombophilia", "coronary stenosis"]
---

# Alteplase
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **9** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 약사 평가 보고서

</div>

# Alteplase: 급성 심근경색 등 혈전성 질환에서 후하벽 심근경색으로

## 한 문장 요약

Alteplase는 조직 플라스미노겐 활성화제(tPA)로, 한국에서 허가된 혈전용해제입니다. 허가 적응증 원문은 이번 데이터에 텍스트로 포함되어 있지 않습니다.
TxGNN 모델은 **후하벽 심근경색(posteroinferior myocardial infarction)**에 효과가 있을 수 있다고 예측하지만, 이 질환에 특화된 **임상시험과 문헌은 0건**입니다. 예측 점수는 모델 예측에 불과합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 텍스트 없음 (허가증에 PDF 링크만 수록, 허가사항 참조 필요) |
| 예측 신규 적응증 | 후하벽 심근경색 (Posteroinferior Myocardial Infarction) |
| TxGNN 예측 점수 | 99.79% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Alteplase는 피브린 특이적 조직 플라스미노겐 활성화제로, 관상동맥 혈전을 용해하여 심근 관류를 회복시킵니다.

후하벽 심근경색은 심근경색의 하위 유형입니다. 혈전성 관상동맥 폐색을 용해한다는 기전상, 적용 가능성은 있습니다. 다만 높은 TxGNN 점수는 상위 질환인 심근경색의 영향을 받았을 가능성이 크며, 이 하위 유형에 특화된 근거는 제공되지 않았습니다.

같은 점수대의 다른 후보로 후외측 심근경색(99.79%), 중격 심근경색(99.77%)이 있으며 모두 유사한 한계를 가집니다. 이 중 문헌이 일부 있는 후보(중격 심근경색, 혈전성 소인, 관상동맥 협착)는 아래 보충 정보에 정리했습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

### 보충: 다른 예측 적응증의 근거

데이터에는 상위 예측 외에 근거가 있는 후보가 있어 참고용으로 요약합니다.

| 예측 적응증 | 점수 | 근거 수준 | 근거 요약 |
|------------|------|----------|---------|
| 중격 심근경색 | 99.77% | L4 | 증례 보고 1건, alteplase 후기 혈전용해 후 좌심실 기능 연구(1996), 부탄 ACS 코호트(2025). 모두 중격 심근경색에 특화되지 않음 |
| 혈전성 소인 (Thrombophilia) | 99.43% | L4 | Phase 2 임상시험 [NCT05540834](https://clinicaltrials.gov/study/NCT05540834) (모집 중, 70명, 점탄성 검사 기반 tPA 용량 설정, 혈전성 소인과의 연관성 불명확) 및 증례 보고 다수 |
| 관상동맥 협착 | 99.14% | L3 | 안정 시 흉통 환자 대상 alteplase vs 위약 이중맹검 RCT ([8299637](https://pubmed.ncbi.nlm.nih.gov/8299637/), 1993), 불안정 협심증 병변 직접 투여 연구 ([8721695](https://pubmed.ncbi.nlm.nih.gov/8721695/), 1996) 등 |

이 후보들의 근거도 대부분 오래되었거나 증례 수준이며, 급성 관동맥 증후군 중심이라 기존 적응증과 겹칩니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199504213 | 액티라제주사50밀리그램(알테플라제) | 주사제 (바이알, 첨부용제 포함) | 허가사항 참조 |
| 199806573 | 액티라제주사20밀리그램(알테플라제) | 주사제 (바이알, 첨부용제 포함) | 허가사항 참조 |

두 제품 모두 한국베링거인겔하임(주)가 허가를 보유합니다.

## 안전성 고려사항

**약물 상호작용**: 총 100건이 조회되었으며, 그중 상위 20건이 데이터에 포함되어 있습니다. 출혈 위험 증가와 관련된 항혈전·항응고·항혈소판 계열이 많습니다.

- **Major**: Fondaparinux, Apixaban, Anisindione, Abciximab, Acalabrutinib, Deferasirox, Ibritumomab tiuxetan, Tositumomab (I-131 포함)
- **Moderate**: Acetylsalicylic acid, Ibuprofen, Ketorolac(안과용 포함), Fluvoxamine, Fosinopril, Aminocaproic acid, Aprotinin, Dexfenfluramine, Fenfluramine, Sibutramine

그 외 경고·금기 정보는 허가사항을 참조하세요. 특히 임신·산후기 환자 등 출혈 위험이 높은 집단은 신중한 평가가 필요합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
후하벽 심근경색에 대한 예측은 모델 점수만 있고 임상시험·문헌이 없는 L5 수준입니다. 기존 급성 심근경색 사용과 기전이 겹쳐 신규 적응증으로서의 가치도 불분명합니다.

**진행하려면 필요한 것:**
- 한국 허가사항(경고, 금기, 적응증 원문) 확보 및 분석
- 작용 기전 데이터 확보 (DrugBank 조회)
- 후하벽 심근경색 하위 유형에 특화된 임상 근거 탐색, 또는 기존 심근경색 적응증과의 차별성 검토
- 근거가 상대적으로 있는 후보(혈전성 소인, 관상동맥 협착)에 대한 추가 검토 및 출혈 위험 평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

