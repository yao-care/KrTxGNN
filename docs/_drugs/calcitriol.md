---
layout: default
title: Calcitriol
parent: 僅模型預測 (L5)
nav_order: 163
evidence_level: L5
indication_count: 7
---

# Calcitriol
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

# Calcitriol: 원 적응증(비타민D 결핍) 재확인 및 부갑상선기능저하증 등 희귀 대사질환 적응증 확장 가능성

## 한 문장 요약

Calcitriol(활성형 비타민D3, 1,25-dihydroxyvitamin D3)은 DrugBank에 등재된 약물로, 한국에는 아직 허가·시판 이력이 확인되지 않았습니다.
TxGNN 모델은 **obsolete vitamin D deficiency**(온톨로지상 폐기된 코드명의 비타민D 결핍증)에 가장 높은 점수(**99.96%**)로 연관된다고 예측했으나, 현재 이를 뒷받침하는 **임상시험이나 문헌은 0건**이며, 이 예측 자체가 약물의 원래 약리 기전과 사실상 동일한 개념일 가능성이 있어 엄밀한 의미의 재창출로 보기 어렵습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (한국 미시판, DrugBank 원 적응증 정보 미수집) |
| 예측 신규 적응증 | obsolete vitamin D deficiency (폐기된 온톨로지 용어의 비타민D 결핍증) |
| TxGNN 예측 점수 | 99.96% |
| 근거 수준 | L4 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails (아래 유의사항 참조) |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 확보되지 않았습니다. 다만 알려진 약리학적 사실에 따르면, Calcitriol은 비타민D의 활성형 대사산물 그 자체이며 VDR(vitamin D receptor)에 직접 작용합니다.

1위로 예측된 "obsolete vitamin D deficiency"는 이름에 포함된 "obsolete"(폐기됨)라는 표현에서 알 수 있듯, 질병 온톨로지 상 이미 병합·폐기된 용어입니다. 즉 이 예측은 Calcitriol의 **원래 약리 목적(비타민D 결핍 치료)을 다시 확인한 것**에 가까우며, 전형적인 의미의 "노후 약물의 새로운 적응증 발굴"과는 성격이 다릅니다. TxGNN 점수가 극도로 높게(99.96%) 나온 것도 약물-질병 간 개념적 중첩이 크기 때문으로 해석할 수 있습니다.

한편 같은 예측 목록에는 기전적으로 더 실질적인 후보들이 포함되어 있습니다. 부갑상선기능저하증(3위)에서는 PTH 결핍으로 신장의 1α-hydroxylase 활성이 저하되어 활성형 비타민D 생성이 안 되는데, Calcitriol이 이 대사 단계를 우회하여 직접 보충할 수 있다는 점에서 국제적으로 이미 표준 치료로 쓰이고 있습니다. 유전성 저인산혈성 구루병(7위) 역시 유사한 기전으로 인산염 보충제와 병용되는 표준 요법입니다. 이 두 후보는 데이터셋에 구체적 임상시험·문헌이 색인되어 있지 않을 뿐, 임상적으로는 이미 정립된 사용례입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다. (obsolete vitamin D deficiency 및 나머지 6개 예측 적응증 모두 ClinicalTrials.gov·ICTRP 조회 결과 0건)

## 문헌 근거

현재 관련 문헌이 없습니다. (PubMed 조회 결과 전체 예측 적응증에서 0건)

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

※ 참고: 한국 규제기관의 경고/금기 자료 및 약물상호작용(DDI) 데이터가 현재 확보되지 않은 상태이며(DDI 조회 결과 not_found), 이 중 규제기관 라벨 자료 누락은 **Blocking 등급 데이터 갭**으로 분류되어 있어 안전성 초기 평가(S1) 단계 진입 자체가 보류되고 있습니다.

## 기타 예측 적응증 (참고)

이번 Evidence Pack에는 rank 1 외에 6개의 추가 예측 적응증이 포함되어 있습니다. 모두 임상시험·문헌 근거는 0건이며, 기전적 타당성 평가만 반영된 순수 모델 예측 수준입니다.

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 | 권장 결정 | 비고 |
|------|------------|-----------|----------|----------|------|
| 2 | Renal tubular acidosis | 99.93% | L5 | Hold | 산염기 조절이 핵심 기전이라 Calcitriol의 직접 연관성 약함 |
| 3 | Familial isolated hypoparathyroidism (PTH 분비 장애) | 99.81% | L4 | Proceed with Guardrails | 국제적으로 이미 표준 대체요법에 해당, 기전 관련성 높음 |
| 4 | Acromesomelic dysplasia, Campailla-Martinelli type | 99.79% | L5 | Hold | 골격 발달 유전질환, 직접 치료 근거 없음 |
| 5 | Craniofacial conodysplasia | 99.78% | L5 | Hold | 극희귀 두개안면 골화 질환, 치료 근거 없음 |
| 6 | Dahlberg-Borer-Newcomer syndrome | 99.76% | L5 | Hold | 사지단축 이형성증 계열, 치료 근거 없음 |
| 7 | Hereditary hypophosphatemic rickets | 99.28% | L4 | Proceed with Guardrails | 인산염 보충과 병용하는 국제 표준요법과 기전 일치 |

## 결론 및 다음 단계

**결정: Proceed with Guardrails (제한된 조건 하에 진행)**

**사유:**
1위 예측("obsolete vitamin D deficiency")은 온톨로지 폐기 용어로 인해 사실상 Calcitriol의 원래 약리 목적을 재확인한 것에 가까워, 독자적인 "재창출" 근거로 삼기에는 부적절합니다. 반면 3위(가족성 부갑상선기능저하증)와 7위(유전성 저인산혈성 구루병)는 국제 임상에서 이미 정립된 표준 치료 기전과 직접 일치하므로, 데이터셋에 임상시험·문헌이 색인되지 않았음에도 실질적 근거 강도가 더 높습니다.

**진행하려면 필요한 것:**
- 한국 식약처(MFDS) 허가사항·경고문 확보 — 현재 Blocking 등급 데이터 갭(DG001)으로 안전성 초기 평가(S1) 진입이 막혀 있음
- DrugBank MOA 상세 정보 확보(DG002)
- "obsolete vitamin D deficiency" 용어의 실제 매핑/동의어 관계 확인 (원 적응증과의 중복 여부 판정)
- 3위·7위 적응증에 대한 임상시험·문헌 재검색 (표준 치료임에도 현재 데이터셋에서 0건으로 나타나는 것은 검색 누락 가능성을 시사)
- 약물상호작용(DDI) 데이터베이스 재조회 (현재 not_found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

