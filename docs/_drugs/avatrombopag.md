---
layout: default
title: Avatrombopag
parent: 僅模型預測 (L5)
nav_order: 104
evidence_level: L5
indication_count: 10
---

# Avatrombopag
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

# Avatrombopag: 면역성 혈소판감소증에서 거대혈소판감소증으로

## 한 문장 요약

Avatrombopag는 트롬보포이에틴 수용체(c-Mpl)에 결합하는 소분자 TPO 수용체 작용제(TPO-RA)로, 혈소판 생성을 자극하여 만성 면역성 혈소판감소증(ITP) 및 만성 간질환 관련 혈소판감소증 치료에 사용됩니다. TxGNN 모델은 **거대혈소판감소증 동반 이첨판 역류증(Marcothrombocytopenia with Mitral Valve Insufficiency)**을 최우선 예측 적응증으로 제시하나, 직접 지지하는 임상시험 및 문헌이 전혀 없는 상태입니다. 10개 예측 중 5개가 ALS 관련 질환으로 집중되어 있어 지식 그래프 구조 효과에 의한 위양성 패턴이 강하게 의심됩니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 만성 면역성 혈소판감소증(ITP), 만성 간질환 시술 전 혈소판감소증 (대만 미허가, 전 세계 승인 기준) |
| 예측 신규 적응증 (1순위) | 거대혈소판감소증 동반 이첨판 역류증 (Marcothrombocytopenia with Mitral Valve Insufficiency) |
| TxGNN 예측 점수 | 99.995% |
| 근거 수준 | L4 |
| 대만 시판 현황 | ✗ 미상시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Avatrombopag는 TPO 수용체(c-Mpl)에 비펩타이드성으로 결합하여 거핵세포의 증식 및 분화를 촉진하는 소분자 화합물입니다. 작용 기전 상세 데이터가 이번 Evidence Pack에 누락되어 있으나, 동일 계열 약물(엘트롬보팍, 로미플로스팀)의 자료 및 허가 기전을 근거로 간접 추론이 가능합니다. 핵심은 **혈소판 수량 부족**에 작용하는 기전으로, 혈소판 형태 이상이나 기능 결함에는 원칙적으로 효과가 제한됩니다.

1순위 예측인 거대혈소판감소증(Marcothrombocytopenia)은 MYH9, GP1BA 등 유전자 결함으로 인한 거대 혈소판 형성 질환입니다. TPO-RA는 혈소판 계수를 높일 수 있으나, 혈소판 형태 및 기능 이상을 근본적으로 교정하지는 못합니다. 이첨판 역류증 동반이라는 심혈관 합병증 역시 추가적인 안전성 평가 변수입니다. 2순위(정상 혈소판을 동반한 유전성 혈소판감소증)는 수량만 감소하는 유형으로, TPO-RA 기전 적용 가능성이 상대적으로 높으며 엘트롬보팍의 Phase 2 탐색 시험 선례가 있습니다.

**주요 품질 경고:** 10개 예측 중 5개(5·7·8·9·10순위)가 ALS 및 관련 운동신경원 질환으로 집중되어 있으며, TPO-RA 기전과 ALS 병태생리 사이에는 직접 연관이 없습니다. 이는 KG 내 혈소판 관련 노드와 운동신경원 질환 노드 사이의 그래프 인접 효과에 의한 구조적 위양성으로 판단됩니다. 4순위 Dense granule disease 역시 혈소판 기능 결함(수량 문제 아님)으로 기전 불일치에 해당합니다.

---

## 전체 예측 평가

| 순위 | 질환명 | TxGNN 점수 | 근거 수준 | 기전 타당성 | 권장 |
|------|--------|-----------|---------|-----------|------|
| 1 | Marcothrombocytopenia with Mitral Valve Insufficiency | 99.995% | L4 | 간접 — TPO-RA로 혈소판 수 증가 가능하나 형태 이상 교정 불가 | Hold |
| 2 | Hereditary Thrombocytopenia with Normal Platelets | 99.995% | L4 | 간접 — 수량 부족 유형에 기전 일치, 동일 계열 Phase 2 선례 있음 | Hold |
| 3 | Transient Neonatal Thrombocytopenia | 99.995% | L5 | 약한 이론적 가능성, 신생아 안전성 데이터 전무, 자한성 질환으로 개입 효익 불확실 | Hold |
| 4 | Dense Granule Disease | 99.995% | L5 | **기전 불일치** — 혈소판 기능(치밀과립) 결함이며 TPO-RA는 수량에만 작용 | Hold |
| 5 | Amyotrophic Lateral Sclerosis | 99.993% | L5 | **KG 구조 위양성** — TPO-RA와 운동신경원 퇴행 사이 직접 기전 없음 | Hold |
| 6 | Bilateral Parasagittal Parieto-Occipital Polymicrogyria | 99.992% | L5 | **KG 구조 위양성** — 뇌 구조 발달 기형, 혈소판 경로와 무관 | Hold |
| 7 | Lower Motor Neuron Syndrome with Late-Adult Onset | 99.992% | L5 | **KG 구조 위양성** — ALS 하위 그래프 파급 효과 | Hold |
| 8 | ALS, Susceptibility To | 99.991% | L5 | **KG 구조 위양성** — ALS 주노드와 점수 사실상 동일, 노드 중복 | Hold |
| 9 | Mills Syndrome | 99.991% | L5 | **KG 구조 위양성** — 전 세계 보고 100건 미만의 ALS 희귀 변이형 | Hold |
| 10 | Monomelic Amyotrophy | 99.990% | L5 | **KG 구조 위양성** — 물리적 경추 압박이 원인, ALS 분류 노드 오배치 | Hold |

---

## 임상시험 근거

현재 Avatrombopag와 1순위 예측 적응증(Marcothrombocytopenia with Mitral Valve Insufficiency)에 관한 등록 임상시험이 없습니다.

---

## 문헌 근거

현재 Avatrombopag와 1순위 예측 적응증에 관한 관련 문헌이 없습니다.

---

## 대만 시판 정보

대만에 등록된 Avatrombopag 허가증이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
최우선 예측 적응증에 대한 직접 임상 근거(임상시험·문헌)가 전무하고, 대만 시판 이력이 없으며, MOA 공식 데이터도 부재합니다. 더불어 10개 예측 중 절반 이상(6건)이 KG 구조 위양성으로 판단되어 이번 예측 세트의 전반적 신뢰도가 낮습니다.

**진행하려면 필요한 것:**
- DrugBank API에서 Avatrombopag 공식 MOA 및 부작용 데이터 확보 (DG002 해소)
- TFDA/MFDS 허가 현황 및 仿單(허가 전문) 다운로드 후 경고·금기 항목 확인 (DG001 해소)
- 2순위 예측(유전성 혈소판감소증)에 대한 **엘트롬보팍** 동일 계열 임상 문헌 우선 검토 — 직접 근거로의 전환 가능성 평가
- Avatrombopag의 전 세계 허가 현황(ITP, CLD 관련 시술 전 혈소판감소증) 문서화하여 기존 적응증 섹션 보완
- ALS 관련 5개 예측에 대한 KG 노드 구조 점검을 통해 위양성 필터링 로직 개선 권고
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

