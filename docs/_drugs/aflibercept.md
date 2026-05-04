---
layout: default
title: Aflibercept
parent: 僅模型預測 (L5)
nav_order: 27
evidence_level: L5
indication_count: 10
---

# Aflibercept
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

# Aflibercept: 신생혈관성 황반변성에서 내사시로

## 한 문장 요약

Aflibercept는 VEGF-A, VEGF-B 및 태반성장인자(PlGF)를 차단하는 재조합 융합단백질(VEGF Trap)로, 전 세계적으로 습성(신생혈관성) 황반변성·당뇨황반부종·망막정맥폐쇄 관련 황반부종 등 안과 질환과 전이성 대장직장암 치료에 사용됩니다.
TxGNN 모델은 **내사시(Esotropia)**에 효과가 있을 수 있다고 예측하나,
현재 이를 직접 지지하는 **임상시험 및 문헌이 전혀 없으며**, VEGF 경로와 내사시 사이의 기전적 연관성도 확립되어 있지 않습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 습성 황반변성, 당뇨황반부종, 망막정맥폐쇄 관련 황반부종, 전이성 대장직장암 (글로벌 허가; 대만 미승인) |
| 예측 신규 적응증 | 내사시 (Esotropia) |
| TxGNN 예측 점수 | 99.38% |
| 근거 수준 | L5 |
| 대만 시판 현황 | ✗ 미상시 (未上市) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 데이터베이스에 상세한 작용 기전(MOA) 데이터가 등록되어 있지 않습니다. 알려진 정보에 따르면, Aflibercept는 VEGF-A, VEGF-B 및 PlGF에 각각 결합하는 재조합 융합 수용체 단백질로, 이들 인자가 내인성 VEGFR에 결합하는 것을 경쟁적으로 차단합니다. 이를 통해 병적 신생혈관 형성 및 혈관 투과성 증가를 억제합니다. 유리체 내 주사 제형(Eylea)은 안과적 신생혈관 질환에, 정맥 주사 제형(ziv-aflibercept, Zaltrap)은 FOLFIRI와의 병용 항암요법에 각각 사용됩니다.

내사시(Esotropia)는 안구가 코 방향으로 편위되는 신경근육 협조 이상으로, VEGF 신호전달 경로와의 직접적 인과관계가 현재까지 확립되어 있지 않습니다. 일부 동물 모델에서 VEGF가 외안근 발달에 관여한다는 보고가 있으나, 이는 발달 단계의 생리적 역할이며 임상적 내사시의 병인으로 이어지는 명확한 경로는 문헌에서 지지되지 않습니다.

TxGNN의 고예측점수(0.994)는 Aflibercept의 주된 적용 영역이 안과 질환임에 따라, 지식 그래프 내 '안과 질환(Ophthalmic Disease)' 노드 간의 광의적 유사성 전파(non-specific proximity propagation)에서 비롯된 것으로 판단됩니다. 질병 특이적 VEGF 기전이 아닌, 그래프 구조상 노드 근접성 효과일 가능성이 높습니다.

---

## 임상시험 근거

현재 내사시(Esotropia)에 대한 Aflibercept 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 세포독성

Aflibercept의 정맥 주사 제형(ziv-aflibercept, Zaltrap)은 전이성 대장직장암 치료에 사용되는 항혈관신생 항암제입니다.

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 항혈관신생 표적치료제 (VEGF-A / VEGF-B / PlGF 삼중 차단; 직접 세포독성 없음) |
| 골수억제 위험 | 중등도 (호중구감소증·백혈구감소증 흔함 — 주로 병용 화학요법 FOLFIRI에 기인) |
| 구토 유발성 등급 | 저~중등도 (단독 투여 시 낮으나 FOLFIRI 병용 시 중등도) |
| 모니터링 항목 | CBC (분류 포함), 혈압, 신기능(단백뇨 24시간 측정 또는 PCR), 간기능, 상처 치유 상태, 혈전색전 증상 |
| 취급 방호 | 정맥 제형(Zaltrap): 항암제 취급 규정 준수 필요 / 유리체 내 주사 제형(Eylea): 일반 생물의약품 취급 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
내사시에 대한 Aflibercept의 임상 근거(임상시험·문헌)가 전혀 존재하지 않으며, VEGF 경로와 내사시 사이의 기전적 연관성이 확립되지 않아 재창출 가설 자체가 성립하지 않습니다. TxGNN 고점수(99.38%)는 안과 질환 노드 근접성 효과로 설명될 가능성이 높습니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 데이터 보완 (DrugBank API 조회, DG002 해소)
- 대만 허가사항(TFDA 仿單) PDF 수집 및 경고·금기 정보 확인 (DG001 해소)
- 내사시에서의 VEGF 역할에 관한 기초 연구(동물 모델·전임상 데이터) 사전 확인
- 재창출 가설 성립 여부를 위한 전임상(in vitro/in vivo) 검증 선행 필요

---

## 전체 예측 요약 (TW-DB08885-multi)

이 보고서는 10개 예측 적응증을 포함하는 멀티 후보 패키지입니다. 모든 예측이 L5 수준이며 권장 결정은 아래와 같습니다.

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 | 결정 | 비고 |
|------|------------|-----------|---------|------|------|
| 1 | 내사시 (Esotropia) | 99.38% | L5 | Hold | 안과 노드 근접성 효과 추정 |
| 2 | 출혈성 식도 정맥류 (Esophageal Varices w/ Bleeding) | 97.56% | L5 | Hold | 성숙 혈관에 항VEGF 효과 불확실; 출혈 악화 우려 |
| 3 | 비출혈성 식도 정맥류 (Esophageal Varices w/o Bleeding) | 97.56% | L5 | Hold | 전신 항VEGF의 간기능 장애 환자 독성 위험 |
| 4 | 정맥류 질환 (Varicose Disease) | 96.95% | L5 | Hold | 혈류역학적 질환이 주기전; 혈관신생이 부주기전 |
| 5 | 요도 결석 (Urethral Calculus) | 95.97% | L5 | Hold | VEGF와 결석 형성 간 합리적 가설 없음 |
| 6 | 아데노신탈아미노효소 결핍증 (ADA Deficiency) | 95.76% | L5 | Hold | 면역결핍 질환; VEGF 경로와 무관 |
| 7 | 신생아 출혈증 (Hemorrhagic Disease of Newborn) | 95.56% | L5 | Hold | 방향 반대 (항VEGF → 출혈 악화 가능); 조회된 임상시험은 무관 (CNV 시험) |
| 8 | 외간엽종 (Ectomesenchymoma) | 94.52% | L5 | Hold | 극희귀 종양; 항혈관신생 일반 가설만 존재 |
| 9 | 악성 피부 과립세포종 (Malignant Cutaneous GCT) | 94.51% | L5 | Hold | 극희귀 신경초막 종양; 특이적 VEGF 문헌 없음 |
| 10 | 중이 신경내분비종양 (Middle Ear NET) | 94.42% | L5 | **Research Question** | NETs에서 VEGF/PlGF 발현 문헌 있음; 수술 고위험 해부 위치로 전신 약물 임상 필요성 존재 |

> ⚠️ **주의**: 순위 10위인 중이 신경내분비종양만 `decision_stage: S1`으로 분류되었습니다. NETs에서의 항VEGF 근거(RADIANT 시리즈)와 중이의 수술 고위험 특성을 고려할 때, 추가 연구 질문 설정이 가능한 유일한 후보입니다. 단, 중이 특이적 데이터는 현재 전무합니다.

---

> **면책 조항**: 본 보고서는 TxGNN 모델 예측 및 공개 데이터베이스 기반 연구 참고 자료로만 활용되어야 하며, 의료 행위의 근거 또는 의학적 조언으로 사용될 수 없습니다. 모든 재창출 후보는 임상 검증을 거쳐야 합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

