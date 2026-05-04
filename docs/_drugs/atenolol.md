---
layout: default
title: Atenolol
parent: 僅模型預測 (L5)
nav_order: 92
evidence_level: L5
indication_count: 9
---

# Atenolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Atenolol: 고혈압·협심증에서 후하벽 심근경색으로

## 한 문장 요약

Atenolol은 Beta-1 선택적 아드레날린 수용체 차단제로, 고혈압 및 협심증 치료에 국제적으로 널리 사용되는 약물입니다.
TxGNN 모델은 **후하벽 심근경색(Posteroinferior Myocardial Infarction)**에 효과가 있을 수 있다고 예측하며,
현재 **1편의 문헌**이 이 방향을 지지합니다 (등록 임상시험 없음).

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 고혈압, 협심증 (국제 기준; 현지 시판 미허가) |
| 예측 신규 적응증 | 후하벽 심근경색 (Posteroinferior Myocardial Infarction) |
| TxGNN 예측 점수 | 99.87% |
| 근거 수준 | L3 |
| 시판 현황 | ✗ 미허가 (허가증 0건) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 부재합니다. 알려진 정보에 따르면, Atenolol은 Beta-1 선택적 아드레날린 수용체 차단제(cardioselective beta-blocker)로, 심박수 감소·심근 수축력 저하·심실벽 응력 감소를 통해 심근 산소 소모량을 줄이는 것이 핵심 작용입니다.

후하벽 심근경색은 주로 우측 관상동맥(RCA) 또는 좌회선지(LCX) 폐색으로 발생합니다. Beta-1 선택성은 이 영역의 심근 보호 및 이차 예방에 이론적 근거를 제공하며, 특히 우측 관상동맥 지배 구역에서의 심박수 저하로 인한 산소 공급·소비 비율 개선 효과가 기대됩니다.

Beta-1 차단제는 심근경색 후 표준 이차 예방 치료제로 이미 임상에서 활용되고 있습니다. 그러나 '후하벽'이라는 특정 MI 아형에 특화된 독립 임상 근거는 부재하며, 이는 기전상 일반적인 MI 후 베타차단제 사용 근거를 공유하는 수준에 머뭅니다.

---

## 임상시험 근거

현재 후하벽 심근경색에 대한 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [3901170](https://pubmed.ncbi.nlm.nih.gov/3901170/) | 1985 | Small Crossover RCT (Single-blind) | La Revue de medecine interne | 후하벽 또는 전벽 한정 MI 후 4주째 잔류 허혈 징후 환자 23명에서 atenolol 200mg과 diltiazem 240mg의 항허혈 효과를 자전거 에르고미터 운동부하 검사로 비교; 컴퓨터 분석(Case-Marquette) 적용 |

---

## 전체 예측 적응증 요약

이 Evidence Pack은 총 9개 적응증을 예측합니다. TxGNN 점수는 유사하나, 실제 임상 근거 수준은 적응증별로 크게 다릅니다.

| 순위 | 적응증 | TxGNN 점수 | 근거 수준 | 임상시험 | 문헌 수 | 권장 |
|------|-------|-----------|---------|---------|--------|------|
| 1 | 후하벽 심근경색 | 99.87% | L3 | 0건 | 1편 | Hold |
| 2 | 후외측 심근경색 | 99.87% | L5 | 0건 | 0편 | Hold |
| 3 | 악성 고혈압성 신장 질환 | 99.85% | L5 | 0건 | 0편 | Hold |
| 4 | 악성 신혈관성 고혈압 | 99.85% | L4 | 0건 | 1편 | Hold |
| 5 | 다인성 폐고혈압 | 99.84% | L5 | 0건 | 0편 | Hold |
| 6 | 폐질환/저산소증 관련 폐고혈압 | 99.84% | L5* | 0건 | 20편* | Hold |
| 7 | 중격 심근경색 | 99.84% | L4 | 0건 | 1편 | Hold |
| 8 | Braddock 증후군 | 99.80% | L5 | 0건 | 0편 | Hold |
| **9** | **만성 폐성심 (Cor Pulmonale)** | **99.04%** | **L3** | **1건** | **15편** | **Research Question** |

> ※ 6번 적응증의 문헌 20편은 대부분 저산소증 일반 메커니즘 연구(뇌노화, 종양생물학 등)로, atenolol과의 직접 연관성이 없어 실질 근거 수준은 L5입니다.
>
> ⚠️ **만성 폐성심(9순위)**은 TxGNN 점수는 가장 낮으나, 9개 중 임상 근거가 가장 풍부합니다. 별도 심층 평가를 권장합니다.

---

## 만성 폐성심 추가 근거 (순위 9)

9개 적응증 중 직접적인 임상시험과 문헌이 가장 풍부한 만성 폐성심에 대한 근거입니다.

### 임상시험

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03278509](https://clinicaltrials.gov/study/NCT03278509) | Phase 4 | 모집 완료·진행 중 | 5,000 | MI 후 정상 심기능 환자에서 장기 beta-blocker 감량 여부 평가 (REDUCE-SWEDEHEART); 만성 폐성심이 주 입력 기준은 아니나, 심폐 질환 중복 환자에서의 안전성 간접 데이터 확보 가능 (관련성 등급 C) |

### 주요 문헌

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [31524](https://pubmed.ncbi.nlm.nih.gov/31524/) | 1978 | Clinical Study | Lille medical | 기도 폐쇄 만성 폐질환 환자에서 atenolol의 임상 효과 |
| [6673339](https://pubmed.ncbi.nlm.nih.gov/6673339/) | 1983 | Clinical Comparison | Vutreshni bolesti | COPD 합병 허혈성 심질환 30명에서 Falicard 및 Sectral(acebutolol) 병용 비교 |
| [15881093](https://pubmed.ncbi.nlm.nih.gov/15881093/) | 2005 | Clinical Study | Terapevticheskii arkhiv | 허혈성 심질환 + COPD 환자에서 장기 atenolol 투여 시 호흡기 장애 특성 평가 |
| [14520850](https://pubmed.ncbi.nlm.nih.gov/14520850/) | 2003 | Clinical Study | Terapevticheskii arkhiv | 당뇨·COPD 합병 수축기 고혈압에서 atenolol·metoprolol·bisoprolol 효능 및 안전성 비교 |
| [1686421](https://pubmed.ncbi.nlm.nih.gov/1686421/) | 1991 | Observational | Cardiologia | 만성 심부전 환자 15명에서 atenolol 50mg 1년 투여 후 박출률·운동 내성·신경호르몬 변화 평가 |
| [25350545](https://pubmed.ncbi.nlm.nih.gov/25350545/) | 2014 | Mechanistic Study | PloS ONE | 간헐적 저산소 쥐 모델에서 Beta-2 수용체 의존성 저산소성 폐혈관 수축 완화와 폐동맥고혈압 진행 억제 기전 |
| [28982831](https://pubmed.ncbi.nlm.nih.gov/28982831/) | 2017 | Observational | BMJ Open | 천식-COPD 중복 증후군(ACOS)과 관상동맥 질환·심부정맥·심부전 발생 위험 연관성 (모집단 기반 후향적 코호트) |
| [38700308](https://pubmed.ncbi.nlm.nih.gov/38700308/) | 2023 | Review | JAPI | 고혈압 일차 치료에서 beta-blocker의 역할 재검토; 허혈성 심질환·빈맥성 부정맥 동반 시 적응증 확인 |
| [30191469](https://pubmed.ncbi.nlm.nih.gov/30191469/) | 2018 | Retrospective Cohort | Cardiology and Therapy | 고혈압 환자에서 atenolol·metoprolol 대비 nebivolol의 심혈관 사건 입원 위험 비교 |
| [11219471](https://pubmed.ncbi.nlm.nih.gov/11219471/) | 2001 | RCT (26주) | Clinical Therapeutics | 경등~중등도 고혈압에서 telmisartan vs atenolol 효능·내약성 비교; 필요 시 hydrochlorothiazide 병용 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
후하벽 심근경색에 대한 직접 근거는 1985년 소규모 단일 맹검 교차 RCT 1편(n=23)에 불과하며, 현재 해당 특정 적응증에 대한 등록 임상시험이 없습니다. 기전적 타당성은 인정되나 독립 임상 근거가 부재하고, 현지 시판 허가도 확인되지 않아 추가 검증이 선행되어야 합니다.

**진행하려면 필요한 것:**
- 상세 작용 기전(MOA) 데이터 확보 (DrugBank API 조회로 해결 가능)
- 허가사항 안전성 정보 검토 (TFDA/MFDS 허가 PDF 다운로드 및 경고·금기 파싱)
- 현지 시판 허가 현황 재검토 (Atenolol은 글로벌 기준 허가 약물; 현지 데이터 부재 가능성 확인 필요)
- 후하벽 MI 특이 임상시험 직접 검색 (ClinicalTrials.gov에서 "posteroinferior" + "beta-blocker" 확장 쿼리)
- **만성 폐성심(9순위) 별도 심층 평가 강력 권장**: 임상시험 1건·문헌 15편으로 9개 적응증 중 근거 수준 최고; TxGNN 순위는 낮으나 실제 임상 활용 가능성이 더 높음
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

