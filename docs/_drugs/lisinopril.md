---
layout: default
title: Lisinopril
parent: 모델 예측만 (L5)
nav_order: 480
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Lisinopril: 예측 신규 적응증 후하벽 심근경색 (posteroinferior myocardial infarction) (근거 수준 L5). 기존 적응증: 확인 불가 (허가 적응증 텍스트 대신 허가 문서 링크만 수록됨)"
monitor_inn: "LISINOPRIL"
predicted_indications: ["pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "Braddock syndrome", "chronic pulmonary heart disease", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome"]
---

# Lisinopril
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

## Lisinopril: 고혈압 등 기존 적응증에서 후하벽 심근경색으로
{: .text-alpha }

## 한 문장 요약

Lisinopril은 ACE 억제제 계열 약물로, 한국에서 허가를 받아 시판 중입니다. 다만 이번 데이터에서 허가 적응증 본문은 확인되지 않았습니다.
TxGNN 모델은 **후하벽 심근경색(posteroinferior myocardial infarction)**에 효과가 있을 수 있다고 예측하지만, 이 질환에 대한 **임상시험과 문헌은 각각 0건**입니다.
따라서 현재 근거는 모델 예측에 한정됩니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 적응증 텍스트 대신 허가 문서 링크만 수록됨) |
| 예측 신규 적응증 | 후하벽 심근경색 (posteroinferior myocardial infarction) |
| TxGNN 예측 점수 | 99.90% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Lisinopril은 ACE(안지오텐신 전환효소) 억제제로, 레닌-안지오텐신계(RAS)를 차단합니다. 이는 심근경색 후 심실 리모델링을 줄이고 생존율을 개선하는 데 쓰이는 기전이어서, 심근경색 하위 유형에도 생물학적으로 적용 가능할 수 있습니다.

다만 이번 데이터에는 후하벽이라는 특정 부위에 대한 임상시험이나 문헌이 없습니다. 또한 심근경색 후 일반적인 사용은 이미 기존 허가 범위에 포함될 수 있어, 뚜렷한 재창출 신호로 보기 어렵습니다. 같은 점수를 받은 후측벽 심근경색도 상황이 같습니다.

참고로 상위 10개 예측 중 근거가 가장 많은 것은 **만성 폐성심(chronic pulmonary heart disease)**입니다. 이 질환에 대해 Lisinopril 관련 소규모 임상 연구 2편이 있어 근거 수준이 L3로 평가되었습니다(아래 참고).

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 후하벽 심근경색에 대한 관련 문헌이 없습니다.

**참고: 다른 예측 적응증의 주요 문헌**

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [17047621](https://pubmed.ncbi.nlm.nih.gov/17047621/) | 2006 | 임상 연구(소규모·비대조 추정) | Kardiologiia | 허혈성 심질환과 COPD를 동반한 심부전 환자에서 Lisinopril 10 mg/일이 폐고혈압을 완화하고 우심실 수축기능과 이완기 충만을 개선 (만성 폐성심 예측) |
| [14524095](https://pubmed.ncbi.nlm.nih.gov/14524095/) | 2003 | 임상 연구(소규모·비대조 추정) | Probl Tuberk Bolezn Legk | 만성 폐성심 환자에서 Lisinopril 치료 (초록 없음) |
| [39018146](https://pubmed.ncbi.nlm.nih.gov/39018146/) | 2024 | 증례 보고 | JPMA | 심근경색 후 심실중격 파열 환자에서 ACE 억제제와 코엔자임 Q10 보조 치료 (중격 심근경색 예측, 직접 근거로 보기 어려움) |
| [20852161](https://pubmed.ncbi.nlm.nih.gov/20852161/) | 2010 | 증례 보고 | Am J Health Syst Pharm | Tizanidine과 Lisinopril 병용 시 중증 저혈압 및 서맥 (안전성 신호) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199002095 | 현대제스트릴정10밀리그램(리시노프릴) | 엷은 적갈색의 원형 정제 | 허가 적응증 텍스트 미확인 (허가 문서 링크만 수록) |

## 안전성 고려사항

허가사항의 경고 및 금기 정보는 이번 데이터에 포함되지 않았으므로 허가사항을 참조하세요. 아래는 보조 자료에서 확인된 내용입니다.

- **지식그래프 기반 금기 관련 질환** (허가 문서가 아닌 TxGNN 지식그래프 기준): 신장 질환, 간 질환, 췌장염, 담낭 질환, 혈관부종(후천성·유전성·ACE 억제제 유발 포함), 전신홍반루푸스, 당뇨병 및 당뇨병성 케톤산증, 칼륨 결핍, 호중구감소증, 무과립구증, 대동맥 판막 협착, 저혈압 질환, 부갑상선기능항진증, 간성 혼수 및 간성 뇌병증, 결합조직 질환, 뼈 질환 등
- **약물 상호작용**: 조회된 상호작용은 100건이며, 이 중 **주요(Major)** 등급은 다음과 같습니다.
  - 구연산칼륨(Potassium citrate)
  - 중탄산칼륨(Potassium bicarbonate)
- **중등도(Moderate) 상호작용 예시**: 코르티코스테로이드(hydrocortisone, dexamethasone, betamethasone 등), 당뇨병 치료제(metformin, SGLT2 억제제, DPP-4 억제제 등), 아스피린, 모르핀, 부프로피온
- **개별 문헌 신호**: Tizanidine 병용 시 저혈압·서맥 위험
- **신혈관성 고혈압 관련**: 양측 신동맥 협착에서 급성 신기능 저하 위험

## 결론 및 다음 단계

**결정: Hold**

**사유:**
후하벽 심근경색 예측은 TxGNN 점수(99.90%)만 있고 임상시험과 문헌이 모두 없어 근거 수준이 L5입니다. 심근경색 후 ACE 억제제 사용은 이미 확립된 용도여서, 하위 유형 예측만으로는 새로운 재창출 가치를 판단하기 어렵습니다.

**진행하려면 필요한 것:**
- 한국 허가 적응증 및 경고·금기 정보 확보 (MFDS 허가사항 PDF 분석)
- 상세 작용 기전 데이터 확보 (DrugBank 조회)
- 후하벽 심근경색이 기존 허가 범위(심근경색 후 사용)에 이미 포함되는지 검토
- 대안으로 근거가 더 있는 만성 폐성심 예측을 우선 검토하되, 소규모 비대조 연구뿐이므로 대조 임상연구 설계 필요
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

