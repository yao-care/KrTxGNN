---
layout: default
title: Estramustine
parent: 모델 예측만 (L5)
nav_order: 320
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Estramustine: 예측 신규 적응증 전립선암/뇌암 감수성 (prostate cancer/brain cancer susceptibility) (근거 수준 L5). 기존 적응증: 전립선암 (허가 적응증 원문은 링크로만 제공되어 허가사항에서 확인 필요)"
monitor_inn: "estramustine"
predicted_indications: ["prostate cancer/brain cancer susceptibility", "fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "prostate leiomyoma", "male reproductive organ cancer", "benign prostate phyllodes tumor", "female breast carcinoma", "HIV infectious disease", "breast fibrocystic disease"]
---

# Estramustine
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

# Estramustine: 전립선암에서 전립선암/뇌암 감수성으로

## 한 문장 요약

Estramustine은 에스트라디올과 질소 머스터드 카바메이트가 결합된 경구 항종양제로, 원래 전립선암 치료에 사용되었습니다.
TxGNN 모델은 **전립선암/뇌암 감수성(prostate cancer/brain cancer susceptibility)**에 효과가 있을 수 있다고 예측했지만, 이 항목을 직접 뒷받침하는 **임상시험과 문헌은 0건**입니다.
또한 이 항목은 치료 대상 질환이 아니라 유전적 감수성 개념이어서 치료 적응증으로서 의미가 크지 않습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 전립선암 (허가 적응증 원문은 링크로만 제공되어 허가사항에서 확인 필요) |
| 예측 신규 적응증 | 전립선암/뇌암 감수성 (prostate cancer/brain cancer susceptibility) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L5 (모델 예측만 있음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 데이터에는 상세한 작용 기전 항목이 비어 있습니다. 다만 수집된 문헌에 따르면 estramustine은 에스트라디올과 질소 머스터드 카바메이트가 연결된 약물입니다. 주된 항종양 작용은 미세소관 관련 단백질(MAP)과 튜불린에 결합해 미세소관을 해체하고 세포를 G2/M기에 정지시키는 항유사분열 작용으로 보고되어 있습니다. 전립선 조직에서는 estramustine 결합 단백질(EMBP)에 결합해 조직 선택적으로 축적될 수 있습니다.

예측 점수는 매우 높지만, 이 질환은 "감수성"이라는 유전적 개념입니다. 따라서 약물로 치료할 수 있는 표적 질환이라고 보기 어렵습니다. 점수는 전립선암과의 지식그래프상 근접성을 반영했을 가능성이 큽니다. 전립선암은 이미 이 약의 기존 사용 영역이며, 데이터상 "남성 생식기관 암" 항목으로 별도 평가됩니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199906840 | 에스트라시트캡슐140밀리그램(에스트라머스틴인산나트륨수화물) | 경질캡슐 (회백색 분말 충전) | 허가사항 원문 참조 (한국화이자제약) |

## 참고: 같은 약물의 다른 예측 후보

1순위 항목에는 근거가 없으므로, 근거가 있는 다른 후보를 간략히 정리합니다.

| 예측 질환 | 점수 | 근거 | 평가 |
|---------|------|------|------|
| 남성 생식기관 암 (실질적으로 전립선암) | 99.99% | 임상시험 다수(Phase 3 포함, 예: [NCT00004001](https://clinicaltrials.gov/study/NCT00004001) 770명, [NCT00002855](https://clinicaltrials.gov/study/NCT00002855) 306명, [NCT00055731](https://clinicaltrials.gov/study/NCT00055731) 413명)와 문헌 | 신규 재창출이 아닌 기존 사용 영역. 데이터 평가는 L1, Proceed with Guardrails |
| 여성 유방암 | 99.99% | Phase 2 1건([NCT00003066](https://clinicaltrials.gov/study/NCT00003066), 40명, 상태 불명), 문헌 다수(예: [PMID 11697838](https://pubmed.ncbi.nlm.nih.gov/11697838/) 안트라사이클린·탁산 실패 후 단독요법 활성) | 무작위·Phase 3 근거 없음. 연구 질문 수준 |
| 양성 생식계 신생물 | 99.99% | EMBP 바이오마커 등 문헌 8편 | 치료 효능 근거 아님. Hold |
| 전립선 섬유종, Brenner 종양, 전립선 평활근종, 양성 전립선 엽상종양, HIV 감염, 유방 섬유낭성질환 | 99.95~99.99% | 근거 없음 | 모두 Hold |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (에스트라디올–질소 머스터드 결합체, 항유사분열 작용) |
| 골수억제 위험 | 문헌상 혈액학적 독성이 적다고 보고됨 (단, 병용요법에서는 병용약 영향 고려) |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 혈전색전증·심혈관계·위장관 독성 (병용 시 CBC, 간기능 포함) |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

## 안전성 고려사항

- **금기 가능 질환 (지식그래프 기반, 허가사항 아님)**: 고혈압, 울혈성 심부전, 관상동맥질환·심근경색, 뇌혈관 질환, 혈전정맥염, 당뇨병, 신장·간 질환, 담낭 질환, 고칼슘혈증, 간질, 편두통 등이 연결되어 있습니다. 허가사항 금기와 대조가 필요합니다.
- **약물 상호작용**: 총 111건이 확인되었고, 표시된 항목은 모두 Moderate 수준입니다.
  - 코르티코스테로이드: hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone
  - 혈당강하제: metformin, acarbose, canagliflozin, dapagliflozin, empagliflozin, linagliptin, alogliptin, albiglutide, dulaglutide, chlorpropamide
  - 칼슘 제제: calcium acetate, calcium phosphate
  - 기타: amphotericin B, calcitriol
- **병용 시 주의**: 에스트로겐 성분 때문에 혈전색전증과 심혈관계 위험에 주의해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
1순위 예측(전립선암/뇌암 감수성)은 모델 점수만 높을 뿐 임상시험과 문헌이 전혀 없고, 치료 대상 질환이 아니라 유전적 개념이어서 재창출 후보로 평가하기 어렵습니다. 실질적으로 근거가 있는 영역은 이미 사용 중인 전립선암이며, 유방암은 초기 단계 근거만 있어 연구 질문 수준입니다.

**진행하려면 필요한 것:**
- 허가사항 원문에서 적응증, 경고, 금기 확인 (현재는 링크로만 제공됨)
- 상세 작용 기전 데이터 보완
- 재평가 대상을 치료 가능한 질환(예: 유방암)으로 재설정하고, 현재 표준치료 대비 효능 비교 근거 확보
- 혈전색전증·심혈관계 위험이 있는 환자군에 대한 안전성 모니터링 계획
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

