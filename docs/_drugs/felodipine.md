---
layout: default
title: Felodipine
parent: 僅模型預測 (L5)
nav_order: 317
evidence_level: L5
indication_count: 7
---

# Felodipine
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

# Felodipine: 적응증 정보 부재에서 프린츠메탈 협심증으로

## 한 문장 요약

Felodipine은 다이하이드로피리딘(DHP)계 칼슘채널차단제이며, 한국 내 허가·시판 이력이 없어 원 적응증 데이터는 확인되지 않습니다.
TxGNN은 7개의 후보 적응증을 예측했는데, 그중 **프린츠메탈 협심증(Prinzmetal's Angina)**만 실질적인 임상 근거를 갖추고 있습니다 —
TxGNN 예측 점수 **99.07%**와 함께 felodipine을 직접 투여한 **RCT 4건을 포함한 문헌 9편**이 이를 뒷받침합니다. 나머지 6개 후보는 근거가 없거나(L5) 기전상 모순이 있어 이번 보고서에서 제외했습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (한국 허가 이력 없음, MOA 데이터도 미확인) |
| 예측 신규 적응증 | 프린츠메탈 협심증 (Prinzmetal Angina) |
| TxGNN 예측 점수 | 99.07% |
| 근거 수준 | L2 |
| 한국 시판 현황 | ✗ 미판매 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

DrugBank 상 공식 MOA 데이터는 확인되지 않았습니다(데이터 갭). 다만 확보된 문헌들은 felodipine이 DHP계 칼슘채널차단제로서 혈관평활근의 L-type 칼슘통로를 억제해 관상동맥 경련(vasospasm) 경향을 감소시킨다는 점을 일관되게 보여줍니다.

프린츠메탈 협심증은 병태생리학적으로 관상동맥 경련이 핵심이므로, CCB의 항경련 작용과 기전상 직접 연결됩니다. 실제로 1988~1995년 사이 다수의 이중맹검 대조군 연구가 felodipine을 nifedipine·위약과 비교해 허혈 발작 빈도 및 ST 분절 변화 감소를 확인했으며, 이는 TxGNN 예측 스코어와 별개로 독립적인 실증 근거입니다.

참고로 TxGNN이 가장 높은 점수를 부여한 후보(불명 다인성 폐고혈압, 폐질환/저산소 관련 폐고혈압 등)는 문헌·임상시험이 전무하거나(L5), 오히려 저산소성 폐혈관 수축 억제로 V/Q 불일치를 악화시킬 우려가 있어 임상 가이드라인상 권장되지 않는 기전 모순을 보였습니다. 따라서 이번 보고서는 근거 수준이 가장 높은 프린츠메탈 협심증을 대표 후보로 선정했습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록(ClinicalTrials.gov/ICTRP)이 없습니다. 아래 문헌 근거는 임상시험 등록 이전 시기(1988~1995년)에 수행된 대조군 연구입니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [1746458](https://pubmed.ncbi.nlm.nih.gov/1746458/) | 1991 | RCT | Am J Cardiol | Felodipine 1일 1회 vs nifedipine 1일 4회, 프린츠메탈 협심증 30명 대상 24시간 홀터 비교 |
| [8013514](https://pubmed.ncbi.nlm.nih.gov/8013514/) | 1994 | RCT | Eur Heart J | Felodipine 서방정이 ergonovine 유발 심근허혈을 예방(변이형 협심증 14명) |
| [7744087](https://pubmed.ncbi.nlm.nih.gov/7744087/) | 1995 | RCT | Eur Heart J | 안정형 운동유발 협심증에서 felodipine vs nifedipine vs 위약, 24시간 항협심증 효과 비교 |
| [2909138](https://pubmed.ncbi.nlm.nih.gov/2909138/) | 1989 | Clinical Trial | Am J Cardiol | 변이형 협심증에서 과호흡 유발 허혈 발작에 대한 felodipine 효과 |
| [7728649](https://pubmed.ncbi.nlm.nih.gov/7728649/) | 1995 | Review | Can J Cardiol | 협심증 치료에서 CCB의 역할 고찰, felodipine 중심 |
| [14689111](https://pubmed.ncbi.nlm.nih.gov/14689111/) | 2003 | Review | Herz | 칼슘길항제 감별 치료 전략 개관 |
| [3345765](https://pubmed.ncbi.nlm.nih.gov/3345765/) | 1988 | Case Series | Eur Heart J | 프린츠메탈 협심증에서 운동유발 간헐적 협심증 및 ST 분절 상승 사례 |
| [19052677](https://pubmed.ncbi.nlm.nih.gov/19052677/) | 2008 | Case Report | Can J Cardiol | 관상동맥 경련 유발 다형성 심실빈맥 사례 |
| [15222138](https://pubmed.ncbi.nlm.nih.gov/15222138/) | 2004 | Case Report | Orvosi Hetilap | Nicergoline 유발 프린츠메탈 협심증 사례 |

---

## 한국 시판 정보

Felodipine은 현재 한국 내 허가된 품목이 없습니다 (허가증 0건, 미판매).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
- 프린츠메탈 협심증은 CCB의 고전적 적응증이며, felodipine을 직접 사용한 이중맹검 RCT 4건이 효능을 뒷받침합니다.
- 다만 근거 문헌이 모두 1988~1995년 소규모 연구로, 현대적 대규모 RCT나 임상시험 등록은 없습니다.
- 안전성(경고·금기·DDI)과 MOA 공식 데이터가 모두 확보되지 않아(DG001: Blocking, DG002: High) 안전성 초기평가(S1) 단계 자체가 불가능한 상태입니다.
- 한국 내 시판 이력이 없어 실제 도입 시 별도 허가 경로 확인이 필요합니다.

**진행하려면 필요한 것:**
- TFDA/식약처 등재 여부 확인 및 공식 경고·금기 자료 확보 (DG001, Blocking — 안전성 초기평가 선행조건)
- DrugBank MOA 공식 문헌 확보 (DG002)
- 최신 DDI 데이터베이스 재조회 (현재 not_found)
- 현행 협심증 치료 가이드라인 대비 최신 근거 문헌 업데이트 필요 (기존 근거가 1990년대 중심)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

