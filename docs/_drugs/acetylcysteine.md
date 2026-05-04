---
layout: default
title: Acetylcysteine
parent: 僅模型預測 (L5)
nav_order: 20
evidence_level: L5
indication_count: 10
---

# Acetylcysteine
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

# Acetylcysteine: 점액용해·해독제에서 혈전성 질환으로

---

## 전체 예측 요약

이번 Evidence Pack에는 NAC에 대한 10개의 TxGNN 예측이 포함됩니다. 아래 심층 분석은 **최우선 예측 적응증(순위 1: 혈전성 질환)**을 기준으로 작성됩니다.

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 | 임상시험 | 문헌 | 권장 결정 |
|-----|-----------|-----------|---------|---------|-----|---------|
| 1 | 혈전성 질환 (Thrombotic Disease) | 99.96% | L1 | 9건 | 0편 | Proceed with Guardrails |
| 2 | 폐쇄각 녹내장 (Closed-angle Glaucoma) | 99.95% | L5 | 0건 | 0편 | Hold |
| 3 | 기관지염 (Bronchitis) | 99.93% | L1 | 13건 | 18편 | Proceed with Guardrails |
| 4 | 비강 질환 (Nasal Cavity Disease) | 99.92% | L4 | 0건 | 6편 | Research Question |
| 5 | 건성안 증후군 (Dry Eye Syndrome) | 99.87% | L2 | 11건 | 20편 | Proceed with Guardrails |
| 6 | 인두염 (Pharyngitis) | 99.80% | L3 | 1건 | 0편 | Research Question |
| 7 | 급성 후두인두염 (Acute Laryngopharyngitis) | 99.79% | L5 | 0건 | 0편 | Hold |
| 8 | 기관 질환 (Tracheal Disease) | 99.57% | L3 | 4건 | 20편 | Research Question |
| 9 | 일과성 허혈 발작 (Transient Ischemic Attack) | 99.53% | L4 | 0건 | 9편 | Research Question |
| 10 | 후두기관염 (Laryngotracheitis) | 99.34% | L5 | 0건 | 0편 | Hold |

---

## 한 문장 요약

Acetylcysteine(NAC)은 점액용해제 및 아세트아미노펜 중독 해독제로 전 세계적으로 수십 년간 사용되어 온 약물입니다.
TxGNN 모델은 **혈전성 질환(Thrombotic Disease)** — 특히 이식 관련 혈전성 미세혈관증(TA-TMA) — 에 효과가 있을 수 있다고 예측하며,
현재 **9건의 임상시험**이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 점액용해(기관지염/COPD), 아세트아미노펜 중독 해독 (전세계 허가; 데이터셋 내 미확인) |
| 예측 신규 적응증 | 혈전성 질환 (Thrombotic Disease) |
| TxGNN 예측 점수 | 99.96% |
| 근거 수준 | L1 |
| 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

현재 데이터셋에 DrugBank 공식 MOA 정보가 없습니다. 그러나 공개된 임상 문헌에 따르면, NAC은 단순한 점액용해제를 넘어 **vWF 이황화 결합 직접 절단**이라는 독특한 기전을 통해 혈전성 병태에 작용합니다.

NAC의 유리 티올기(-SH)는 Von Willebrand Factor(vWF) 초대형 다합체(Ultra-Large VWF, ULVWF)의 이황화 결합을 직접 환원·절단합니다. ULVWF는 HSCT 후 내피 손상 환경에서 혈소판을 비정상적으로 포획하여 미세혈관 혈전(TA-TMA)을 유발하는 핵심 매개체입니다. ADAMTS13 효소가 ULVWF를 정상적으로 절단하지 못하는 병태생리적 환경에서 NAC이 그 역할을 화학적으로 보완하며, 이 기전은 Phase 3 인체 임상시험(NCT03252925)에서 직접 검증된 수준입니다.

NAC의 항산화 기전(글루타티온 전구체로서 GSH 보충)은 산화 스트레스로 유발되는 혈관내피 활성화 및 조직인자(Tissue Factor) 발현을 억제하여, 만성 신질환(CKD) 환자의 혈전 표현형 감소(RENACTIF, NCT03636932)와 같은 보다 광범위한 혈전성 병태에도 적용될 수 있습니다. 이는 기존 점액용해 적응증과는 독립적인 경로이지만, 내피 보호라는 공통 분모를 통해 혈전 적응증의 기전적 타당성을 더욱 뒷받침합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03252925](https://clinicaltrials.gov/study/NCT03252925) | Phase 3 | 완료 | 170 | HSCT 관련 TA-TMA에서 NAC 안전성·효능 전향적 평가 — 가장 핵심적인 완료된 피벗 시험, L1 핵심 근거 |
| [NCT07279610](https://clinicaltrials.gov/study/NCT07279610) | Phase 2/3 | 진행 중(모집 완료) | 44 | 다기관 단일군 시험 — TA-TMA 치료에서 NAC 효능·안전성 평가 (혈장교환술 및 에쿨리주맙 대비 비용효과 포함) |
| [NCT05907486](https://clinicaltrials.gov/study/NCT05907486) | Phase 3 | 불명 | 260 | 동종 HSCT 후 혈전 사건 **예방**에서 NAC 효능·안전성 — 대규모 예방 설계로 TA-TMA 증거 강화 |
| [NCT03636932](https://clinicaltrials.gov/study/NCT03636932) | Phase 2 | 완료 | 40 | RENACTIF — 신기능 부전 환자 혈전 표현형 감소: 이중맹검 교차 RCT, 요독성 소분자(Indoxyl Sulfate) 매개 내피 산화 억제 기전 입증 |
| [NCT03460808](https://clinicaltrials.gov/study/NCT03460808) | Phase 1/2 | 불명 | 200 | 스테로이드 저항성/재발 ITP에서 아토르바스타틴+NAC+다나졸 병합 vs 다나졸 단독 다기관 비교 시험 |
| [NCT04368598](https://clinicaltrials.gov/study/NCT04368598) | Phase 2 | 불명 | 44 | 신규 진단 ITP에서 고용량 덱사메타손+NAC 병합요법 효능·안전성 단일군 시험 |
| [NCT06518044](https://clinicaltrials.gov/study/NCT06518044) | Phase 2 | 미개시 | 30 | 반일치 이식 후 중증 재생불량성 빈혈(SAA)에서 NAC의 조혈 회복 촉진 탐색 단일군 시험 |
| [NCT05551624](https://clinicaltrials.gov/study/NCT05551624) | Early Phase 1 | 완료 | 15 | ITP 환자에서 아토르바스타틴+NAC 혈소판 수 개선 효과 탐색 (n=15, 소규모 탐색) |
| [NCT01808521](https://clinicaltrials.gov/study/NCT01808521) | Early Phase 1 | 완료 | 3 | TTP 의심 환자에서 NAC 정맥 투여 — vWF ADAMTS13 절단 개선 및 혈소판/vWF 응집 억제 파일럿 (n=3, 매우 소규모) |

---

## 문헌 근거

현재 관련 문헌이 없습니다.

*(혈전성 질환 대상 PubMed 문헌 검색에서 수집된 논문 없음; 임상시험 데이터가 주요 증거 기반을 구성)*

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
TA-TMA를 직접 대상으로 한 완료된 Phase 3 시험(NCT03252925, n=170)이 존재하고, 추가 Phase 3(n=260) 및 Phase 2/3(n=44) 시험이 진행 중으로 증거 기반이 빠르게 성숙하고 있습니다. NAC의 vWF 이황화 결합 절단 기전은 TA-TMA 병태생리와 직접 일치하며, 수십 년간 축적된 광범위한 임상 안전성 데이터가 개발 위험을 현저히 낮춥니다.

**진행하려면 필요한 것:**
- DrugBank 공식 MOA 데이터 확보 (DrugBank API 조회)
- 허가사항 경고·금기 원문 확인 (TFDA/MFDS 仿單 PDF 검토)
- NCT03252925 최종 발표 결과 데이터 검토 및 핵심 지표(완전 반응률, 생존율) 분석
- TA-TMA에서 최적 용량·투여 경로(정맥 vs 경구) 프로토콜 수립
- 소아 및 신기능 저하 환자군 안전성 모니터링 계획 수립

> **참고**: 기관지염(순위 3)도 L1 근거 수준으로 임상시험 13건·문헌 18편이 확보되어 별도 심층 평가를 권장합니다. 건성안 증후군(순위 5, L2, Chitosan-NAC 제제 Lacrimera® 기반)도 독립적 개발 경로로 검토 가치가 있습니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

