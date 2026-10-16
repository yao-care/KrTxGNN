---
layout: default
title: Ramipril
parent: 모델 예측만 (L5)
nav_order: 641
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ramipril: 예측 신규 적응증 허혈성 뇌졸중 감수성 (obsolete susceptibility to ischemic stroke) (근거 수준 L5). 기존 적응증: 허가증에 적응증 원문이 제공되지 않아(허가사항 링크만 있음) 확인 불가. 문헌상 고혈압, 심부전, 신병증…"
---

# Ramipril
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

# Ramipril: 고혈압·심혈관 질환에서 허혈성 뇌졸중 감수성으로

## 한 문장 요약

Ramipril은 ACE 억제제로, 한국에서 단일제 4건이 허가되어 시판 중입니다. TxGNN 모델은 **허혈성 뇌졸중 감수성(obsolete susceptibility to ischemic stroke)**에 효과가 있을 수 있다고 예측하지만, 이 항목에는 연결된 임상시험이나 문헌이 **0건**입니다. 같은 뇌혈관 계열인 **뇌졸중(stroke disorder)**과 **뇌혈관 질환(cerebrovascular disorder)** 항목에서는 HOPE, ONTARGET 등 대규모 RCT가 근거로 확인됩니다.

> 참고: 1순위 예측 항목은 더 이상 사용되지 않는 온톨로지 용어로, 뇌졸중 관련 다른 항목과 중복되는 것으로 보입니다. 따라서 이 보고서는 1순위 항목을 기준으로 하되, 근거가 확인된 뇌졸중·뇌혈관 질환 항목을 함께 평가합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에 적응증 원문이 제공되지 않아(허가사항 링크만 있음) 확인 불가. 문헌상 고혈압, 심부전, 신병증, 심혈관 사건 예방에 사용됨 |
| 예측 신규 적응증 | 허혈성 뇌졸중 감수성 (obsolete susceptibility to ischemic stroke) |
| TxGNN 예측 점수 | 99.95% |
| 근거 수준 | L5 (1순위 항목 기준) / 뇌졸중·뇌혈관 질환 항목은 L1 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 4건 (모두 유효, 단일제) |
| 권장 결정 | 1순위 항목: Hold / 뇌졸중·뇌혈관 질환 항목: Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 없습니다. 다만 수집된 문헌에 따르면 Ramipril은 지속형 ACE 억제제로, 프로드럭으로서 간에서 활성 대사체 ramiprilat로 전환됩니다. 안지오텐신 I이 안지오텐신 II로 바뀌는 것을 억제해 혈관 수축과 알도스테론 분비를 줄입니다.

혈압 상승은 뇌졸중의 가장 중요한 조절 가능 위험인자입니다. ACE 억제는 혈압 강하와 함께 내피 기능 개선, 혈관 리모델링 억제, 염증 감소 등 혈관 보호 효과를 낼 수 있습니다. 그래서 기존의 고혈압·심혈관 적응증에서 뇌졸중 위험 감소로 이어지는 것은 기전상 자연스럽습니다.

다만 1순위 항목 자체는 모델 예측만 있고 독립적인 근거가 없습니다. 뇌졸중 위험 감소에 대한 실제 근거는 HOPE 시험(고위험 환자에서 Ramipril이 뇌졸중을 포함한 심혈관 사건을 줄임)과 ONTARGET 시험에서 나옵니다.

## 임상시험 근거

1순위 항목(허혈성 뇌졸중 감수성)에는 등록된 임상시험이 없습니다. 아래는 근거가 확인된 뇌졸중·뇌혈관 질환 항목의 시험입니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00741585](https://clinicaltrials.gov/study/NCT00741585) | Phase 4 | 완료 | 21,983 | 24시간 활동혈압 패턴의 예후 가치를 본 연구로, Ramipril 직접 시험이 아니어서 근거 강도는 약함 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [10639539](https://pubmed.ncbi.nlm.nih.gov/10639539/) | 2000 | RCT (HOPE) | N Engl J Med | 고위험 환자에서 Ramipril의 심혈관 사건 감소 효과를 평가 |
| [18378520](https://pubmed.ncbi.nlm.nih.gov/18378520/) | 2008 | RCT (ONTARGET) | N Engl J Med | 혈관질환 또는 고위험 당뇨 환자에서 Ramipril, telmisartan, 병용을 비교 |
| [11967789](https://pubmed.ncbi.nlm.nih.gov/11967789/) | 2000 | RCT 요약 (HOPE) | J Renin Angiotensin Aldosterone Syst | HOPE 시험의 Ramipril 투여군과 당뇨 하위집단 결과 정리 |
| [33186492](https://pubmed.ncbi.nlm.nih.gov/33186492/) | 2021 | RCT (polypill) | N Engl J Med | 스타틴, 혈압강하제, 아스피린 복합 polypill 전략 평가 |
| [36018037](https://pubmed.ncbi.nlm.nih.gov/36018037/) | 2022 | Review | N Engl J Med | 아스피린, ACE 억제제, 스타틴 polypill을 심근경색 후 2차 예방에 적용 |
| [12076194](https://pubmed.ncbi.nlm.nih.gov/12076194/) | 2002 | Review | Drugs | Ramipril의 심혈관 결과 예방 용도 검토 |
| [16833041](https://pubmed.ncbi.nlm.nih.gov/16833041/) | 2006 | Review | Clin Exp Hypertens | 고혈압 치료와 뇌졸중 예방 최신 동향 |
| [21901125](https://pubmed.ncbi.nlm.nih.gov/21901125/) | 2011 | 전임상(동물) | PLoS One | 쥐 뇌졸중 모델에서 telmisartan, Ramipril, 병용의 예방·신경보호 효과 |

## 한국 시판 정보

허가증에 적응증 원문이 포함되어 있지 않아(허가사항 문서 링크만 제공) 적응증 열은 생략합니다. 자세한 적응증은 식약처 허가사항을 확인하세요.

| 허가번호 | 제품명 | 제형 | 제조사 |
|---------|------|------|--------|
| 200502436 | 알파라미프릴캡슐(라미프릴)(수출용) | 캡슐 | 알파제약(주) |
| 200500140 | 하트프릴정2.5밀리그램(라미프릴) | 정제 | (주)종근당 |
| 200600028 | 하트프릴프로텍트정(라미프릴) | 정제 | (주)종근당 |
| 200300699 | 트리아핀정5/5mg | 필름코팅정 | (주)한독 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 확인된 주요 항목은 다음과 같습니다.
  - **Major**: potassium citrate, potassium bicarbonate (고칼륨혈증 위험)
  - **Moderate**: 코르티코스테로이드(hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), 당뇨병 치료제(metformin, glimepiride, chlorpropamide, alogliptin, SGLT2 억제제인 canagliflozin, dapagliflozin, empagliflozin), 아스피린, morphine, bupropion, dronabinol, 장정결제(picosulfuric acid, polyethylene glycol)
- **일반적 주의사항**: ACE 억제제 계열의 통상적 주의사항(혈관부종, 고칼륨혈증, 신기능, 임신)은 허가사항을 참조하세요. 허가사항 경고·금기 데이터는 이번 자료에 수집되지 않았습니다.

## 결론 및 다음 단계

**결정: 1순위 항목(허혈성 뇌졸중 감수성) Hold / 뇌졸중·뇌혈관 질환 항목 Proceed with Guardrails**

**사유:**
1순위 항목은 모델 예측뿐이고 임상시험·문헌이 없으며, 폐기된 온톨로지 용어로 다른 뇌졸중 항목과 중복될 가능성이 큽니다. 반면 뇌졸중·뇌혈관 질환 항목은 HOPE, ONTARGET 같은 대규모 RCT가 뒷받침하지만, 이는 이미 알려진 심혈관 위험 감소 효과와 겹치므로 엄밀한 의미의 신규 재창출은 아닙니다. 또 연결된 임상시험(NCT00741585)은 Ramipril 직접 시험이 아닙니다.

**진행하려면 필요한 것:**
- 식약처 허가사항(적응증, 경고, 금기) 확보 및 확인 (현재 안전성 검토 진행을 막는 핵심 공백)
- 작용 기전 데이터 보완 (DrugBank 등)
- 1순위 항목과 기존 뇌졸중 항목의 온톨로지 중복 여부 정리
- 이차 예방 또는 고위험 집단으로 대상을 한정하고, 신기능·칼륨·혈압 모니터링 계획 수립 (급성 뇌졸중 치료 용도는 아님)
- 다수의 상호작용 약물(특히 칼륨 제제)에 대한 병용 주의 지침 마련
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

