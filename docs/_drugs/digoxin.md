---
layout: default
title: Digoxin
parent: 모델 예측만 (L5)
nav_order: 279
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Digoxin: 예측 신규 적응증 프린츠메탈 협심증 (Prinzmetal angina) (근거 수준 L5). 기존 적응증: 허가 적응증 텍스트가 링크 형태로만 제공되어 구체적인 내용을 확인할 수 없음"
monitor_inn: "DIGOXIN"
predicted_indications: ["Prinzmetal angina", "duodenal obstruction", "duodenal ulcer (disease)", "duodenogastric reflux", "obsolete susceptibility to ischemic stroke", "hypoalphalipoproteinemia"]
---

# Digoxin
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **6** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 약사 평가 보고서

</div>

# Digoxin: 심부전·심방세동에서 프린츠메탈 협심증으로

## 한 문장 요약

Digoxin은 강심배당체(cardiac glycoside) 계열 약물로, 한국에서 주사제·정제·엘릭서제로 시판되고 있습니다. TxGNN 모델은 **프린츠메탈 협심증(Prinzmetal angina)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 임상시험은 **0건**이고 직접 관련된 문헌도 없어 근거는 모델 예측 수준(L5)에 머뭅니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 텍스트가 링크 형태로만 제공되어 구체적인 내용을 확인할 수 없음 |
| 예측 신규 적응증 | 프린츠메탈 협심증 (Prinzmetal angina) |
| TxGNN 예측 점수 | 99.81% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 4건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 Digoxin은 Na⁺/K⁺-ATPase를 억제하는 양성 변력성 약물로 알려져 있지만, 이번 데이터에서는 확인되지 않았습니다.

프린츠메탈 협심증은 관상동맥 경련(vasospasm)이 원인이며, 칼슘채널차단제와 질산제로 치료합니다. Digoxin이 혈관 경련을 완화할 것이라고 기대하기는 어렵고, 오히려 이론적으로 혈관 긴장도를 높일 수 있습니다. 즉, 기전상 설득력 있는 연결고리는 확인되지 않았으며 높은 예측 점수(99.81%)는 지식 그래프에 기반한 예측일 뿐입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Review | Acta Physiol Pharmacol Bulg | 시간약리학과 항고혈압 치료에 미치는 영향을 다룬 종설로, Digoxin의 프린츠메탈 협심증 효능을 직접 지지하는 내용은 아님 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199200648 | 제일제약디곡신주사액(수출용) | 앰플 주사제 | 허가사항 문서 참조 |
| 196300001 | 디고신정(디곡신) | 정제 | 허가사항 문서 참조 |
| 196300035 | 아주디곡신주사액 | 앰플 주사제 | 허가사항 문서 참조 |
| 199102792 | 카데프엘릭서(디곡신) | 엘릭서제 | 허가사항 문서 참조 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건의 상호작용이 확인되었으며, 이 중 일부는 다음과 같습니다.
  - 중등도: Acarbose, Rabeprazole, Doxycycline, Epinephrine, Hydrocortisone, Cholecalciferol, Metformin, Amphotericin B, Bupropion, Triamcinolone, Acetylsalicylic acid, Dexamethasone, Betamethasone, Tetracycline, Calcium Phosphate
  - 경미: Albiglutide, Hyoscyamine, Atropine, Glycopyrronium
- **지식 그래프 기반 금기 관련 질환** (허가사항 문구가 아닌 예측 모델의 지식 그래프 정보): 신장 질환, 칼륨 결핍, 고칼슘혈증, 심근경색, 폐성심, 볼프-파킨슨-화이트 증후군, 동기능부전증후군, 심실세동, 비후성 심근병증, 방실차단, 점액부종·갑상선기능저하증, 심근염, 수축성 심낭염, 제한성 심근병증 등

허가사항의 경고 및 금기 문구는 이번 데이터에 포함되어 있지 않으므로, 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
프린츠메탈 협심증에 대한 임상시험과 직접적인 문헌 근거가 없으며, 기전상으로도 Digoxin이 관상동맥 경련을 완화한다고 보기 어렵습니다. 높은 TxGNN 점수는 모델 예측일 뿐이므로 현 단계에서는 진행을 보류합니다.

**진행하려면 필요한 것:**
- Digoxin의 상세 작용 기전(MOA) 데이터 확보
- 식약처 허가사항(적응증, 경고, 금기) 원문 확보 및 분석
- 혈관 경련에 대한 Digoxin의 영향을 다룬 전임상·임상 근거 확보
- 같은 예측 목록의 다른 후보(십이지장 폐쇄, 십이지장 궤양, 십이지장위 역류, 저알파지단백혈증 등)도 현재 L5 수준이며 기전적 근거가 없어 우선순위가 낮음
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

